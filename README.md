# Equity Research Kit

A curated, shareable set of **equity-research and financial-modeling skills** for Claude Code —
packaged as an installable plugin so anyone can try them in one command. The point of this repo
is to **test each skill and keep the ones worth keeping**; treat the current 13 as a starting
roster, not a final one.

Skills are copied verbatim from Anthropic's `claude-for-financial-services` plugins
(`equity-research` 0.1.2 and `financial-analysis` 0.1.1) so they can be edited and curated here.

## Install

```
/plugin marketplace add <this-repo-url-or-local-path>
/plugin install research-kit@equity-research-kit
```

- From a local clone: `/plugin marketplace add ~/Projects/research-kit`
- From GitHub once pushed: `/plugin marketplace add m0xt/research-kit`

After installing, the skills appear as `research-kit:<skill>` and trigger on their descriptions
(or invoke directly, e.g. `/research-kit:dcf-model`).

## What's inside (13 skills)

### Equity research (9)
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

### Financial modeling (4)
| Skill | What it does |
|---|---|
| `dcf-model` | DCF valuation (pulls filings, builds projections + WACC, sensitivity, Excel out) |
| `3-statement-model` | Fill a linked income statement / balance sheet / cash flow model |
| `comps-analysis` | Comparable-company analysis with trading multiples |
| `audit-xls` | Audit a spreadsheet/model for formula errors and integrity |

## Evaluation log

Track verdicts as you test each one. **Keep** = use it; **Cut** = remove from the roster; **Tweak** = keep but modify.

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

## Curating

To drop a skill: delete its folder under `plugins/research-kit/skills/` and commit. To edit one:
change its `SKILL.md` (and any `references/`). Re-run `/plugin marketplace update equity-research-kit`
to pick up changes.

## Provenance

Source: Anthropic `claude-for-financial-services` marketplace — `equity-research` and
`financial-analysis` plugins. Original author: Anthropic FSI. Repackaged here for evaluation.
