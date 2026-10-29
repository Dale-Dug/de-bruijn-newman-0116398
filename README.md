# Retuned translated probes: Λ < 0.116398

**Dale James Raymond · Preprint · Version 1.0 · 10 October 2026**  
**Published paper and complete evidence:** [Zenodo record 23272725](https://zenodo.org/records/23272725)  
**Version-specific DOI:** [10.5281/zenodo.23272725](https://doi.org/10.5281/zenodo.23272725)

## Current mathematical status — 26 October 2026

The bound **Λ ≤ 0.116397726408291 < 0.116398** follows unconditionally by combining the deposited computer-assisted comparison with **OpenAI’s proved zero-free half-plane Re(s) > 7/8** ([30 September 2026, Theorem 1.1](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), with [accompanying Lean formalisation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean)). This supplies exactly the **H(7/8)** hypothesis used in the original deposit: every nontrivial zero of the Riemann zeta function has real part at most 7/8, including the boundary line. The pinned Lean theorem is `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`.

The archived publication retains its original conditional title and wording for citation and provenance. This clarification does not claim external peer review, an independently established world record, or end-to-end formal verification of the complete de Bruijn–Newman argument.

In the Polymath normalisation, the deposited exact comparison is:

```text
Λ ≤ 116397726408291 / 1000000000000000
  = 0.116397726408291
  < 0.116398.
```

The alternate exact ceiling is 0.116397726408312. Both main histories have 14,899 steps. The numerical checks concern the deposited comparison, not the external zero-free theorem. No proof of RH or global-optimality claim is made.

This repository is a lightweight companion to the published deposit. It follows the format of the separate [0.149396 companion](https://github.com/Dale-Dug/de-bruijn-newman-0149396); the earlier publication is not the DOI or hypothesis of this result.

## Research overview

Dale James Raymond · [ORCID 0009-0001-1682-8529](https://orcid.org/0009-0001-1682-8529)

- **8 September 2026:** [Phase-correlated certificates, Λ < 0.163297](https://zenodo.org/records/22626161).
- **21 September 2026:** [Correlated translated probes, Λ < 0.149396](https://zenodo.org/records/22867547).
- **10 October 2026:** [Retuned translated probes, Λ < 0.116398](https://zenodo.org/records/23272725), published with an original conditional title; see the [current mathematical status](https://github.com/Dale-Dug/de-bruijn-newman-0116398#current-mathematical-status--26-october-2026).
- **29 October 2026:** [A computer-assisted bound, Λ ≤ 0.107964910079](https://zenodo.org/records/23752103).

GitHub companions: [0.149396](https://github.com/Dale-Dug/de-bruijn-newman-0149396) · [0.116398](https://github.com/Dale-Dug/de-bruijn-newman-0116398) · [0.107965](https://github.com/Dale-Dug/de-bruijn-newman-0107965).

## Read the publication

1. [Main paper](deposit/Conditional_0116398.pdf) and [editable LaTeX](deposit/Conditional_0116398.tex)
2. [Matched-source analytic supplement](deposit/Matched_Source_Supplement.pdf)
3. [Verification guide](deposit/Verification_Guide.pdf) and [author-supplied pre-deposit execution receipt](deposit/Verification_Receipt.json)
4. [Complete manuscript sources](deposit/Manuscript_Sources.zip)

The two unchanged historical references are [Prior Analytic Foundations](deposit/Prior_Analytic_Foundations.pdf) and [Prior Correlated Translated Probes](deposit/Prior_Correlated_Translated_Probes.pdf). Read their Gaussian and wall estimates with the corrections in [Appendix B of the 10 October 2026 main paper](https://github.com/Dale-Dug/de-bruijn-newman-0116398/blob/main/deposit/Conditional_0116398.tex#L867) and the sharp-displacement discussion in the current supplement. The main histories use fixed shifts.

[Further Consequences](deposit/Further_Consequences.pdf) is a separate note. Its implication below 0.09 assumes the stronger strip **H(34/43)**. Its all-scale Möbius covariance cap is explicitly unproved. Neither statement is a premise of the H(7/8) theorem.

The paper combines 44 rational full-domain kernel certificates, a retuned physical-source schedule and matched finite logarithmic coefficients. The selected source covers 608 closed time cells and all six frequency classes, including the unbounded class.

## Preserved archival files and citation

The original publication of **10 October 2026, Version 1.0**, is titled **“Retuned translated probes and the conditional bound Λ < 0.116398 for the de Bruijn–Newman constant.”** That title remains the correct title for citation; the current status clarification above does not alter the deposit.

All 15 lightweight files in [`deposit/`](deposit/) are exact copies from the live Zenodo record. They retain their original pre-deposit wording, including a missing DOI in the archived citation and a null DOI in the archived manifest. These are historical publication bytes; this companion does not rewrite them or invalidate their checksums. Use the DOI above and the updated root [CITATION.cff](CITATION.cff) when citing this publication.

The sixteenth file, **Proof_and_Replay.zip**, remains on Zenodo. It is 123,031,589 bytes and has SHA-256:

```text
045bd7703019a78167e746c8260c0135803b80aa072d5ec0313d5a2b4cc85b89
```

## Verify and restore the complete deposit

[Download full Proof_and_Replay.zip from Zenodo](https://zenodo.org/api/records/23272725/files/Proof_and_Replay.zip/content) (123,031,589 bytes). The full scientific replay remains on Zenodo; this repository contains the lightweight companion.

The helpers require Python 3.10 or later and only the standard library. First check the files in this companion:

```sh
python3 -B Verify_GitHub_Files.py
```

To download the pinned scientific archive and restore all 16 original files into a new directory outside this repository:

```sh
python3 -B Prepare_Replay.py --download --output ../zenodo_23272725 --verify-deposit
```

Or reuse a copy downloaded from the record, without another network transfer:

```sh
python3 -B Prepare_Replay.py --archive /path/to/Proof_and_Replay.zip \
  --output ../zenodo_23272725 --verify-deposit
```

The helper verifies every original file against its expected size and SHA-256. It preserves the original filenames at the restored directory's root, as required by `Verify_Deposit.py`. The optional `--verify-deposit` runs that reviewed, unchanged integrity/configuration checker. It inspects ZIP members but does not extract or execute scientific programs. Existing output directories are never overwritten; a failed restoration is removed. Neither helper performs a mathematical replay.

For scientific audit and native replay commands, follow the [verification guide](deposit/Verification_Guide.pdf) after restoration. Full native production requires the documented pinned **CPython 3.13, Linux x86-64** runtime. Keep assertions enabled. Place scientific output outside the immutable evidence directory.

## Verification boundary

The archived receipt reports pre-deposit source reconstruction, exact-history regeneration and native reproduction. Both native interval constructions use **Arb/FLINT**, with different precisions, partitions and formulas; they are not independent transcendental libraries. The native replay retains earlier wall certificates and does not repeat the published finite-RH calculation. Analytic reductions and proof-to-code correspondence still require mathematical scrutiny.

This GitHub preparation preserves and checks the published files; it does **not** claim a fresh full native-producer replay or independent mathematical proof. No fresh wall production or Lean execution was performed for this review. Hash and restoration checks establish file identity, not correctness of the theorem. Review targets and reporting guidance are in [REVIEW.md](REVIEW.md).

## Rights and provenance

The live Zenodo record selects **CC BY 4.0**. The deposit has mixed-content rights, and no blanket software or third-party relicensing is asserted. See the [rights pointer](LICENSES_AND_RIGHTS.md) and [original rights notice](deposit/LICENSES_AND_RIGHTS.md).

The work was developed with AI assistance; the named author is responsible for the claims. Exact source URLs, file sizes, hashes and preparation scope are recorded in [REPOSITORY_PROVENANCE.json](REPOSITORY_PROVENANCE.json).
