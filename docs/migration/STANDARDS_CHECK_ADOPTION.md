# Adoption into the primary StandardFlow repository

## Decision

`edithatogo/standards_check` is the primary adoption repository. Verified foundation revision `f248d7c4dd40dd34cb45b5b6150b4750a5b28864` defines the initial Canonical Standard Pack, artefact-recipe and ecosystem-evidence contracts. This exact pin is a reviewed integration target and must not update automatically.

## What migrates

| Legacy surface | Target role |
| --- | --- |
| `src/diagram.py` | renderer adapter and golden-behaviour fixture |
| `src/prisma.py`, `src/consort.py`, `src/strobe.py` | declarative diagram recipes plus family invariants |
| `src/checklist.py` | generic checklist/form renderer fixture |
| `schemas/` | compatibility inputs mapped to versioned StandardFlow contracts |
| `tests/` and snapshots | differential/golden regression suite |
| `data/` and examples | rights-reviewed fixtures and tutorials |
| Flask/Docker surfaces | optional clients of the shared future application facade |

## Migration method

1. Record a clean exact source revision and inventory.
2. Audit licences, generated files, fixtures and dependencies.
3. Import Git history into a quarantined namespace; do not copy-and-delete.
4. Establish differential fixtures before refactoring.
5. Convert standards-specific code to data-driven recipes behind compatibility adapters.
6. Prove deterministic and accessible parity, including all four PRISMA 2020 templates.
7. Migrate users, links and releases with rollback.
8. Archive this repository only after the primary repository records the cutover receipt.

## Hard boundaries

The migration does not relicense third-party standard text, does not make Markdown canonical, and does not permit this repository to overwrite primary packs. Runtime integration is disabled by default. Exact pins, fixtures and explicit approval are required for every cutover step.
