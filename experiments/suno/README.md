# Suno Experiment Harness

Use this directory to record model-versioned prompt and render tests before promoting Suno-specific guidance into universal repository docs.

## Why this exists

Suno behavior changes over time. A tag, slider setting, field limit, or prompt strategy may work differently across model versions. Experiment logs give the repository evidence before updating claims in `core/claims/claim-registry.yml` or methodology in `core/methodology/suno-optimization.md`.

## How to use

1. Copy `TEMPLATE.yml` to a dated file, for example `2026-06-09-no-repeat-tag.yml`.
2. Fill in model version, settings, source song, prompt fields, and expected behavior.
3. Generate one or more renders.
4. Record observations and whether the tested claim should be accepted, rejected, or retested.
5. If the conclusion changes repo guidance, add or update a claim in `core/claims/claim-registry.yml`.

## Promotion rule

Do not promote a Suno behavior claim to universal guidance unless the experiment record includes:

- model version,
- test date,
- full prompt/lyrics context or a source song path,
- relevant settings,
- observed result,
- conclusion,
- confidence,
- retest date.
