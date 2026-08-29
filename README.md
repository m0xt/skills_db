# skills_db

A shareable **database of Claude Code skill plugins** — a single marketplace we can keep
adding to. Each plugin is a themed bundle of skills; install the whole marketplace once and
pick which plugins/skills to use. Right now it holds one plugin (`research-kit`); more will be
added under `plugins/` over time.

## Install

```
/plugin marketplace add m0xt/skills_db
/plugin install research-kit@skills_db
```

- From GitHub: `/plugin marketplace add m0xt/skills_db`
- From a local clone: `/plugin marketplace add ~/Projects/skills_db`
- Install any plugin in the marketplace with `/plugin install <plugin>@skills_db`

After installing, a plugin's skills appear as `<plugin>:<skill>` and trigger on their
descriptions (or invoke directly, e.g. `/research-kit:dcf-model`).

---

## Plugins

### `research-kit` — Equity research + financial modeling (13 skills)

Copied verbatim from Anthropic's `claude-for-financial-services` plugins (`equity-research`
0.1.2 and `financial-analysis` 0.1.1) so they can be edited and curated here. The point is to
**test each skill and keep the ones worth keeping** — treat the roster as a starting point.

**Equity research (9)**
| Skill | What it does |
|---|---|
| `initiating-coverage` | Full initiation report via a 5-task workflow (research → model → valuation → charts → assembly) |
| `earnings-analysis` | Post-earnings update report (beat/miss, revised estimates, thesis check) |
| `earnings-preview` | Pre-earnings preview with scenarios |
| `idea-generation` | Stock screening + thematic idea sourcing |
| `sector-overview` | Industry/sector landscape report |
| `thesis-tracker` | Maintain/update investment theses over time |
| `catalyst-calendar` | Calendar of upcoming catalysts across a coverage universe |
| `model-update` | Update a financial model with new data |
| `morning-note` | Draft a morning meeting note |

**Financial modeling (4)**
| Skill | What it does |
|---|---|
| `dcf-model` | DCF valuation (pulls filings, builds projections + WACC, sensitivity, Excel out) |
| `3-statement-model` | Fill a linked income statement / balance sheet / cash flow model |
| `comps-analysis` | Comparable-company analysis with trading multiples |
| `audit-xls` | Audit a spreadsheet/model for formula errors and integrity |

#### Evaluation log — `research-kit`
**Keep** = use it · **Cut** = remove from the roster · **Tweak** = keep but modify.

| Skill | Tested? | Verdict | Notes |
|---|---|---|---|
| initiating-coverage | ☐ | | |
| earnings-analysis | ☐ | | |
| earnings-preview | ☐ | | |
| idea-generation | ☐ | | |
| sector-overview | ☐ | | |
| thesis-tracker | ☐ | | |
| catalyst-calendar | ☐ | | |
| model-update | ☐ | | |
| morning-note | ☐ | | |
| dcf-model | ☐ | | |
| 3-statement-model | ☐ | | |
| comps-analysis | ☐ | | |
| audit-xls | ☐ | | |

---

## Adding a new plugin

1. Create `plugins/<new-plugin>/.claude-plugin/plugin.json` (name, version, description, author).
2. Put its skills under `plugins/<new-plugin>/skills/<skill>/SKILL.md` (+ any `references/`, `assets/`, `scripts/`).
3. Add an entry to `.claude-plugin/marketplace.json` → `plugins[]` with its `source` path.
4. Commit and push. Users pick it up with `/plugin marketplace update skills_db`.

## Curating an existing plugin

- Drop a skill: delete its folder under `plugins/<plugin>/skills/` and commit.
- Edit a skill: change its `SKILL.md` (and any `references/`).
- Refresh installed copies: `/plugin marketplace update skills_db`.

## Provenance

`research-kit` is repackaged from Anthropic's `claude-for-financial-services` marketplace
(`equity-research` + `financial-analysis` plugins; original author: Anthropic FSI), for
evaluation and curation.
