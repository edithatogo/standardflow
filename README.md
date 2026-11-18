# StandardFlow legacy renderer

> **Migration status:** this repository is the historical Python/Graphviz implementation and is now a migration source for the primary StandardFlow work in [`edithatogo/standards_check`](https://github.com/edithatogo/standards_check). It remains runnable during parity work, but it is not a second source of standards authority.

This code generates research artefacts including PRISMA, CONSORT and STROBE diagrams and checklist outputs. Its schemas, fixtures, tests and Git history will be imported into the primary repository through an evidence-gated, history-preserving migration.

## Current use

```bash
git clone https://github.com/edithatogo/standardflow.git
cd standardflow
pip install -r requirements.txt
python -m src.cli generate data/prisma_data.json -o prisma-example.svg
```

Graphviz is required for diagram generation; TIFF conversion also requires ImageMagick.

## Authority and migration boundary

- The code and tests in this repository describe legacy behaviour, not authoritative standard text.
- Hard-coded PRISMA/CONSORT/STROBE classes are migration inputs for generic, validated artefact recipes and a deterministic accessible scene graph.
- The primary repository owns Canonical Standard Packs, stable requirement IDs, rights/provenance, applicability, evidence state and future Rust interfaces.
- SearchRight remains authoritative for systematic-review state and PRISMA counts.
- This repository will not be archived until parity, migration, downstream links, licensing and rollback have observed evidence.

See [`docs/migration/STANDARDS_CHECK_ADOPTION.md`](docs/migration/STANDARDS_CHECK_ADOPTION.md) and the Conductor track under [`conductor/`](conductor/tracks.md).

## Supported legacy artefacts

- PRISMA 2020 and updated-review flow diagrams;
- CONSORT and cluster-randomised flow diagrams;
- STROBE and cohort flow diagrams;
- CONSORT, STROBE and STARD-family checklist generation;
- JSON-schema validation, CLI, Flask UI, examples and snapshot tests.

The migration inventory is machine-readable at [`integration/standards-check-adoption.json`](integration/standards-check-adoption.json).

## Licence

This repository is licensed under the Apache License 2.0. Imported code and notices must retain those obligations in the primary repository.
