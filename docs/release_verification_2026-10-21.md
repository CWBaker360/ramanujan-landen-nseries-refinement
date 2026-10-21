# Independent numerical release audit — 2026-10-21

Repository: ramanujan-landen-nseries-refinement

An independently reconstructed Python/mpmath calculation (400 decimal digits) evaluated the theta-defined, rationalized gap
`delta(q) = lambda(q) / (1 + sqrt(1-lambda(q)))**2`
for q = 1e-6, 1e-9, 1e-12 and m = 2, 3, 4, 5, 6.

Checks: |R_m(q)-4**(1-m)| < 100*q**2, and |C_m(q)-4*m| < 1000*q**2.
All 15 modular pairs passed both checks. A separate Gauss-Legendre AGM computation (six rows, same precision) passed decreasing-error diagnostics for alpha_n/delta_n**2 -> 1/8 and alpha_(n+1)/alpha_n**2 -> 1/2.

At q=1e-12, the C_m values were:
- m=2: 8.000000000000000000000016
- m=3: 12.000000000000000000000054
- m=4: 16.000000000000000000000104
- m=5: 20.000000000000000000000170
- m=6: 24.000000000000000000000252

Scope: This is an independent numerical reproduction of the same formulas, **not** an execution of the exact checked-in `scripts/verify_modular_gap_law.py`. It does not certify analytic novelty, the full manuscript, interval arithmetic, or correctness of binary PDF build. The repository's `SHA256SUMS.txt` currently predates the revised files and must not be treated as current. The checked-in PDF and TeX have not yet been bytewise matched as one build. Do not change the repository to public on the basis of this note alone.
