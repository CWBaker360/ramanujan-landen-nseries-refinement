# Verification Script

`verify_modular_gap_law.py` performs two independent numerical checks.

## Modular gap law

It computes

```text
R_m(q) = delta(q^m) / delta(q)^m
C_m(q) = q^(-2) * (R_m(q) / 4^(1-m) - 1)
```

for the requested degree range.

## AGM linkage

It reconstructs the lower Gauss-Legendre sequence and computes

```text
alpha_n / delta_n^2
alpha_(n+1) / alpha_n^2
```

Run from the repository root:

```bash
python scripts/verify_modular_gap_law.py --precision 400 --outdir outputs
```

Use `--help` to view all parameters.
