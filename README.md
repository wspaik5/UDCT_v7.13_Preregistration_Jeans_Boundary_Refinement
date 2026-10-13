# UDCT v7.13 Preregistration — Refined Jeans Sign-Boundary and Hessian Diagnostics

Won Shik Paik | Independent Researcher, Auckland, New Zealand | 14 October 2026

## Permanent links and status

- GitHub repository: https://github.com/wspaik5/UDCT_v7.13_Preregistration_Jeans_Boundary_Refinement
- Zenodo reserved DOI: https://doi.org/10.5281/zenodo.23342971 **(reserved; not a published preregistration until Zenodo publication)**
- v7.12 post-registration results: https://doi.org/10.5281/zenodo.23296444
- v7.12 preregistration: https://doi.org/10.5281/zenodo.23280972
- GQUMOND prior-art correction: https://doi.org/10.5281/zenodo.23117541

## Scope

This is a **prospective plan and frozen-input preparation package**, not v7.13 results. The supplied v7.12 post-registration CSV has 363 fixed decisions: N=274, P=48, I=41. All 24 adaptive raw-sign brackets remain unresolved due to endpoint or midpoint numerical margins. We retain every inherited bracket, with no outcome-dependent cherry-picking. We do not assert that Hessian diagnostics already establish any universal threshold.

## Frozen materials

The four inherited scientific source files, v7.12 launcher, and two CSV tables are copied unchanged from the supplied v7.12 ZIP. `preregistration_plan.json` and the preparation script lock their SHA-256 digests. Do not edit these inputs. The supplied full compressed raw run and journal were not part of the lightweight source ZIP; their absence is disclosed.

## Proposed confirmatory experiment (NOT EXECUTED)

1. Run the inherited v7.12 four deciding grid/inner-limit combinations unchanged as baseline, for all 24 bracket endpoints and any new evaluation points. Verify isotropic and field gates.
2. Before any new production run, implement and freeze an independent higher-accuracy validation arm (including its precise discretization, resolution, tolerance and stopping rules) in a **separately versioned public protocol amendment**. The present package does not falsely claim that this new arm has been coded or registered.
3. Evaluate each target in B01–B24 order. A numerical sign is accepted only when its margin exceeds the declared numerical uncertainty across the registered validation arm. If not, report `unresolved_numerical_margin`, retaining the full attempt log.
4. Only a strict, robust opposite-sign pair may be labeled a sign bracket. A coordinate interval is not an exact critical root; no monotonicity or uniqueness is assumed. Do not use a P/N class switch as proof of a zero.
5. Record Hessian diagnostics only when they are computed from the inherited field model with a documented numerical estimator and its own convergence study. Correlation is not causation, and a one-dimensional Jeans sign test does not itself measure a 3-D Hessian.
6. Report all 24 cases, failed gates, missing data and unresolved cases. Do not revise rules after observing outcomes; deviations must be labeled exploratory.

**Registration gate:** publish the v7.13 Zenodo preregistration before executing new scientific simulations. A reserved DOI or saved draft alone is not public registration. The preflight script is safe to run beforehand because it only audits existing data.

## Preparation commands

```bash
python UDCT_v7_13_Preregistration_Preflight.py --selftest
python UDCT_v7_13_Preregistration_Preflight.py --inventory
```

Install `requirements.txt` only if reproducing inherited scientific sources. The preflight script itself uses the Python standard library. The v7.12 scientific runner remains included for historical reproducibility; it is **not** a completed v7.13 refinement runner.

## Interpretation

N = incompatible with the specified stationary Jeans closure; P = positive sampled second-moment candidate only; I = numerical indeterminacy. No nonnegative distribution function, equilibrium, stability, observational agreement, new law or MOND exclusion follows. v7.13 aims to clarify numerical limits before any physical interpretation.
