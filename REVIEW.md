# Independent review and reproducibility reports

This is a conditional preprint offered for mathematical scrutiny. The H(7/8) zero-free assertion is a hypothesis; running numerical checks does not prove it. Neither this companion nor the author-supplied execution receipt constitutes external peer review or end-to-end formal verification.

Useful review targets include:

1. The analytic implication from H(7/8), the strict initial seed and the global first-contact argument.
2. Physical-source reconstruction, finite logarithmic matching, cancellation before absolute values and the use of each certified time-height cell.
3. All 44 full-domain kernel certificates, the distinguished-pair subtraction and the handling of unbounded frequency and future-cutoff ranges.
4. The corrected Gaussian remainder and wall-error comparison in the current main paper, including their relationship to unchanged historical references.
5. Correspondence between the written estimates, `evidence/configs/main.json`, the selected source and both exact 14,899-step histories.
6. The distinction between the main H(7/8) theorem, separate stronger-strip consequences and unproved covariance assumptions.

For numerical reports, include the version-specific DOI, file or commit identity, operating system, architecture, Python version, exact command and earliest failing check. Both native lanes share Arb/FLINT; report precisely which stage was run. Do not replace an unresolved interval sign with ordinary floating-point arithmetic.

For mathematical objections, give the exact section or assertion and distinguish an incorrect conclusion from an insufficient proof or a proof-to-code discrepancy. Any correction should preserve archival versions and explain the change explicitly.

Preparation of this companion checks file integrity and restoration. It makes no claim that the full native producers were rerun for the GitHub upload. Published execution receipts record their own earlier verification scope.

## Checks and a wording issue noted during companion preparation

The live 16-file deposit matched the Zenodo API MD5 checksums and all applicable published SHA-256 checksums. Both ZIP CRC checks passed, the standalone main LaTeX matched its manuscript-archive member, and the main source/configuration/history bindings checked out. A separate comparison found all 44 displayed kernel constants consistent with the rational certificates. These are scoped consistency checks, not a full proof review. The scientific archive also matches the previously audited archive byte-for-byte. No full pipeline replay, fresh wall production or Lean execution was performed in this review.

One point worth clarifying in a future version: page 3 of the Matched Source Supplement says both numerical wall constructions were regenerated at 256/384 bits, while sections 5.1 and 8 of the main paper describe walls retained rather than regenerated for retuning. The supplement may be referring to an earlier baseline run, but the run/date is not established by this wording. An explicit run/date would resolve that ambiguity. The frozen documents are preserved unchanged here.
