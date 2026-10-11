#!/usr/bin/env python3
"""Check this deposit's integrity and configuration binding; execute no archived code.

Only the Python standard library is needed. This is an identity check, not a
verification of the analytic proof. Run the separate audit in the guide for
mathematical checks. No network access, extraction or subprocess is used here.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import sys
import zipfile

PUBLIC_FILES = {
    'Conditional_0116398.pdf', 'Conditional_0116398.tex',
    'Matched_Source_Supplement.pdf', 'Further_Consequences.pdf',
    'Prior_Analytic_Foundations.pdf', 'Prior_Correlated_Translated_Probes.pdf',
    'Verification_Guide.pdf', 'Verification_Receipt.json',
    'Manuscript_Sources.zip', 'Proof_and_Replay.zip', 'README.md',
    'CITATION.cff', 'LICENSES_AND_RIGHTS.md', 'Verify_Deposit.py',
    'Release_Manifest.json', 'SHA256SUMS.txt',
}
ROOT = 'BCLD_Certified_Retuning_20261010/'
SOURCE_SHA = 'a5064c427b11e73f13bfbae0efde00bf3691d9eb7bf8905929e183cd16fb6971'
PRIMARY = '116397726408291/1000000000000000'
ALTERNATE = '14549715801039/125000000000000'

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)

def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sha_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def read_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

def check_zip(path: Path) -> zipfile.ZipFile:
    archive = zipfile.ZipFile(path)
    seen: set[str] = set()
    try:
        for item in archive.infolist():
            name = item.filename
            pp = PurePosixPath(name)
            require(name not in seen, f'{path.name}: duplicate member {name}')
            seen.add(name)
            require(not pp.is_absolute() and '..' not in pp.parts and '\\' not in name,
                    f'{path.name}: unsafe member path {name}')
            require(not stat.S_ISLNK(item.external_attr >> 16),
                    f'{path.name}: symbolic link {name}')
        require(archive.testzip() is None, f'{path.name}: CRC failure')
        return archive
    except Exception:
        archive.close()
        raise

def verify(folder: Path) -> dict:
    require(folder.is_dir(), 'Deposit directory not found')
    actual = {p.name for p in folder.iterdir() if p.is_file()}
    # Benign operating-system files are ignored; unexpected publication files are not.
    actual -= {'.DS_Store', 'Thumbs.db', 'desktop.ini'}
    require(actual == PUBLIC_FILES,
            f'File inventory mismatch: missing={sorted(PUBLIC_FILES-actual)}, '
            f'extra={sorted(actual-PUBLIC_FILES)}')
    require(all(not (folder / n).is_symlink() for n in PUBLIC_FILES),
            'Public files must be regular files, not symbolic links')
    manifest = read_json(folder / 'Release_Manifest.json')
    require(manifest['schema'] == 'BCLD_ZENODO_DEPOSIT_V1', 'Manifest schema')
    require(manifest['version'] == '1.0' and manifest['first_deposit'] is True,
            'First-deposit identity')
    require(manifest['previous_0118_deposited'] is False, 'Undeposited-draft status')
    require(manifest.get('doi') is None, 'This package must not assign a prior DOI to this result')
    require(manifest['main_paper'] == 'Conditional_0116398.pdf', 'Main paper identity')
    require(manifest['hypothesis'] == 'H_7_8' and manifest['upper_exact'] == PRIMARY,
            'Main hypothesis or exact ceiling mismatch')
    declared = manifest['files']
    require(set(declared) == PUBLIC_FILES - {'Release_Manifest.json', 'SHA256SUMS.txt'},
            'Manifest must bind every payload file exactly once')
    hashes = {}
    for name in sorted(declared):
        path = folder / name
        require(path.stat().st_size == declared[name]['bytes'], f'Size mismatch: {name}')
        hashes[name] = sha_file(path)
        require(hashes[name] == declared[name]['sha256'], f'SHA-256 mismatch: {name}')
    checksums = {}
    for line in (folder / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        digest, name = line.split('  ', 1)
        require(name not in checksums, 'Duplicate SHA256SUMS entry')
        require(len(digest) == 64 and all(c in '0123456789abcdef' for c in digest),
                'Malformed SHA-256 value')
        checksums[name] = digest
    require(set(checksums) == PUBLIC_FILES - {'SHA256SUMS.txt'}, 'Checksum file coverage')
    for name, digest in checksums.items():
        require((hashes.get(name) or sha_file(folder / name)) == digest,
                f'Checksum mismatch: {name}')
    for name in PUBLIC_FILES:
        if name.endswith('.pdf'):
            data = (folder / name).read_bytes()
            require(data.startswith(b'%PDF-1.7') and b'%%EOF' in data[-1024:],
                    f'PDF header/trailer mismatch: {name}')
    with check_zip(folder / 'Manuscript_Sources.zip') as sources:
        prefix = 'Manuscript_Sources/'
        current = ['Conditional_0116398', 'Matched_Source_Supplement',
                   'Further_Consequences', 'Verification_Guide']
        require(all(prefix + name + '.tex' in sources.namelist() for name in current),
                'Current manuscript sources are incomplete')
        require(sources.read(prefix + 'Conditional_0116398.tex') ==
                (folder / 'Conditional_0116398.tex').read_bytes(),
                'Standalone main source differs from the source archive')
        require(all(not n.lower().endswith(('.ttf', '.otf', '.woff', '.woff2', '.pfb'))
                    for n in sources.namelist()), 'Standalone font file in manuscript archive')
    with check_zip(folder / 'Proof_and_Replay.zip') as proof:
        require(all(n.startswith(ROOT) for n in proof.namelist()), 'Scientific archive root')
        config = json.loads(proof.read(ROOT + 'evidence/configs/main.json'))
        source_digest = sha_bytes(proof.read(ROOT + 'evidence/SOURCE_SELECTED.json'))
        require(source_digest == SOURCE_SHA == config['source_sha256'], 'Selected-source binding')
        require(config['initial_alpha'] == '7/8' and
                config['initial_strip_q'] == '9/16' and
                config['initial_q'] == '562501/1000000' and config['parts'] == 32,
                'Active main configuration differs from the paper')
        require(Fraction(config['headline']) == Fraction(116398, 1000000), 'Rounded headline')
        for lane, bound in [('primary', PRIMARY), ('alternate', ALTERNATE)]:
            row = config['lanes'][lane]
            require(row['upper_exact'] == bound and row['steps'] == 14899,
                    f'{lane}: exact endpoint or step-count mismatch')
            require(row['modes_used'] == {'r_23_40': 1024, 'r_3_5': 13875},
                    f'{lane}: main history is not the declared fixed-shift history')
            data = proof.read(ROOT + f'evidence/histories/main_{lane}.json.gz')
            require(sha_bytes(data) == row['history_sha256'], f'{lane}: history identity')
            require(Fraction(bound) < Fraction(config['headline']), f'{lane}: headline rounding')
    receipt = read_json(folder / 'Verification_Receipt.json')
    require(receipt['PASS'] is True and receipt['version'] == '1.0', 'Verification receipt identity')
    require(receipt['proof_archive_sha256'] == hashes['Proof_and_Replay.zip'],
            'Receipt refers to a different scientific archive')
    require(receipt['selected_source_sha256'] == SOURCE_SHA, 'Receipt source identity')
    require(receipt['stored_source_and_history_audit']['PASS'] is True,
            'Stored-source audit did not pass')
    require(receipt['native_reproduction']['PASS'] is True and
            receipt['native_reproduction']['mathematical_source_exactly_reproduced'] is True,
            'Native reproduction did not pass')
    return {'PASS': True, 'public_files': len(PUBLIC_FILES), 'version': '1.0',
            'main_paper': manifest['main_paper'], 'hypothesis': 'H_7_8',
            'upper_exact': PRIMARY, 'selected_source_sha256': SOURCE_SHA,
            'scope': 'Integrity and configuration binding only; no mathematical code executed.'}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    try:
        result = verify(args.directory.resolve())
    except (ValueError, KeyError, OSError, zipfile.BadZipFile, TypeError) as exc:
        print(f'ZENODO_DEPOSIT_INTEGRITY_FAIL: {exc}', file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    print('ZENODO_DEPOSIT_INTEGRITY_PASS 16')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
