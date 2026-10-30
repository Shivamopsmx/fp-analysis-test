# fp-analysis-test

A small, deliberately insecure sample app used to exercise **false-positive (FP) analysis**
for both:

- **SAST** — source-code findings (SQL injection, command injection, insecure deserialization,
  weak crypto, hardcoded secrets, unsafe YAML, `eval`, `shell=True`) in `app.py` / `utils.py`.
- **SCA** — dependency CVEs from pinned vulnerable versions in `requirements.txt`.

> This repository intentionally contains insecure code and vulnerable dependencies **for security
> testing only**. Do not use any of it in production.
