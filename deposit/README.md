# Retuned translated probes: conditional Λ < 0.116398

Dale James Raymond · Version 1.0 · 10 October 2026  
ORCID: 0009-0001-1682-8529

## The result and its hypothesis

Assume **H(7/8)**: every nontrivial zero of the Riemann zeta function has real part at most 7/8. The boundary line is allowed. In the Polymath normalisation, the primary exact comparison gives

**Λ ≤ 116397726408291 / 10^15 = 0.116397726408291 < 0.116398.**

The alternate exact ceiling is 0.116397726408312. Both histories contain 14,899 steps. The numerical checks do not prove H(7/8), and this release does not assert an unconditional record, a global optimum, Λ < 0.09 under H(7/8), or RH.

This is the **first deposit** of the present result. The earlier 0.118 drafts were never deposited. They remain inside the frozen evidence solely as development history; any internal historical wording such as “previous publication” refers to a prepared draft, not a public record. The author's September record, DOI 10.5281/zenodo.22867547, is separate prior work. It is not the DOI of this release.

## Read these files in order

1. **Conditional_0116398.pdf** — standalone main paper: assumptions, physical-source argument, global first contact, continuous-domain kernel certificates, exact endpoint and corrected Gaussian remainder. The `.tex` file is the identical editable main source.
2. **Matched_Source_Supplement.pdf** — expanded finite logarithmic matching, source reconstruction and explicit treatment of historical corrections.
3. **Verification_Guide.pdf** — exact commands and proof-to-code map. **Verification_Receipt.json** records the completed pre-deposit checks and their limits.

**Prior_Analytic_Foundations.pdf** and **Prior_Correlated_Translated_Probes.pdf** are unchanged reference copies of the earlier analytic framework, not revised current-result papers. The present main paper's Appendix B replaces the historical Gaussian majorant and narrower wall-error comparison. The matched-source supplement explains the separate sharp-displacement correction. The main histories use fixed shifts only and do not consume a sharp-mode step or the old scalar endpoint.

**Further_Consequences.pdf** is a separate note. Its bound below 0.09 assumes H(34/43), not H(7/8). It proves a sufficient implication from an explicitly unproved all-scale Möbius covariance cap. Its restricted old-table limitation is not a lower bound on Λ. Neither result is a premise of the main paper.

## What improved

The complete rate, including the distinguished-pair subtraction, is optimised rather than the source floor in isolation. The new construction combines 44 rational full-domain kernel certificates with a source regenerated at 274 changed heights and a matched-logarithmic calculation that cancels shared finite convolution terms before taking absolute values.

The frozen selected source covers 608 closed time cells and six frequency classes, including the infinite exterior class and all future native cutoffs. All eleven same-class or adjacent-class translated pairs are retained. Selection copies a complete source row together with its certified height; no interpolation between heights is used.

The main histories use the same strict squared-height seed 9/16 + 10^-6 and the same 32 substeps per source cell as the undeposited 0.118 comparison. The gain is not from changing those two parameters.

## Verify without executing the mathematical programs

Keep all 16 public files in one directory and run:

```bash
python -B Verify_Deposit.py
```

This standard-library program checks the exact public file inventory, sizes, SHA-256 checksums, ZIP integrity and the binding between the release and the frozen main configuration. It does not download files or execute archived code. An integrity pass is not a proof-verification pass.

## Reconstruct the proof data and exact histories

Extract `Proof_and_Replay.zip`. It contains one root directory, `BCLD_Certified_Retuning_20261010`. From that directory run:

```bash
python -B RUN.py --audit --regenerate-histories --output ../retuning_full_audit
```

The output must be outside the immutable evidence directory. This command repeats the retained baseline audit, independently checks the new kernels, reconstructs the selected physical source from saved interval enclosures, verifies the two further algebraic implications, and regenerates and audits all eight final-source histories. **Only the two `main` histories use H(7/8).**

A separate native-production replay is available after the audit:

```bash
python -B code/replay_native.py --audit-dir ../retuning_full_audit \
  --output ../retuning_native_replay --workers 4
```

The native replay requires the pinned CPython 3.13, Linux x86-64 runtime documented in the guide. It regenerates all 608 retuned native rows in each interval construction, then the joint and matched-logarithmic coefficients. It checks that the resulting mathematical source exactly equals the stored retuned source. It retains the old wall files and does not regenerate focused continuum bands or the published finite-RH calculation. Do not disable Python assertions or use `-O`.

## Authoritative configuration and historical material

The headline is defined by `evidence/configs/main.json`, bound to `evidence/SOURCE_SELECTED.json` by SHA-256. The selected source deliberately retains some legacy plan metadata (`initial_q` and `strict_bound`) from its source-generation ancestry; those fields are not the current comparison configuration. Use `main.json` for the initial hypothesis, strict seed, subdivision and final ceilings.

The immutable evidence retains diagnostics, earlier source choices and archived draft text. Floating-point scouts are not certificates. Main-paper equations, the current configuration and the verified exact histories take precedence over historical descriptions. The release manifest identifies all current public documents explicitly.

## Editable sources

Extract `Manuscript_Sources.zip` and run `python BUILD_PDFS.py` inside its root to rebuild the four current PDFs. `--include-prior` additionally rebuilds the unchanged historical sources. A local TeX installation is needed; the build does not access the network. No font files are distributed.

## Verification boundary and rights

The analytic approximation and first-contact arguments remain mathematical inputs to the executable checks. Both native interval constructions use the same Arb/FLINT library, despite different precision, integer partitions and derivative formulas. A separately implemented rational auditor provides a different check of the scalar histories. This is not end-to-end formalisation or external referee certification.

The 7/8 manuscript, its different 11/12 companion, Polymath, Platt–Trudgian and the earlier numerical literature are cited with their roles stated. Planat is cited by the base arXiv identifier only; no inaccessible version, private endorsement or unannounced endpoint is asserted. See `LICENSES_AND_RIGHTS.md` for the mixed-content rights scope. The AI assisted with the work; the named author is responsible for the submitted claims.
