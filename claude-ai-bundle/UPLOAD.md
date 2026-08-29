# claude.ai org upload bundle

These 13 `.zip` files are the skills packaged for **claude.ai's organization Skills**
(Team/Enterprise). Each zip is one skill folder (`SKILL.md` + any scripts/references),
with its description trimmed to claude.ai's **200-character limit**. The rich descriptions
stay in the repo for Claude Code — these trimmed copies are claude.ai-only.

## Upload (admin, one time)

1. In claude.ai, go to your **organization/admin settings → Skills** (the "skills shared
   across the organization" section).
2. **Add a skill** and upload each `.zip` in this folder — one per skill (13 total).
3. Once added, the skills are available to **every member** of the org with no per-user setup.

Individual users (any plan) can instead self-add a skill via **Customize → Skills** using the
same zips.

## When a skill changes

The repo (`plugins/research-kit/skills/`) is the source of truth. After editing any skill:

```bash
python3 scripts/build_claudeai_bundle.py
```

This regenerates every zip here. Re-upload the changed skill(s) to claude.ai (there is **no
auto-sync** from GitHub to claude.ai — uploads are manual).

## Notes

- Trimmed descriptions live in `scripts/build_claudeai_bundle.py` (the `SHORT` map). Edit them
  there, not in the zips.
- Claude Code users don't use these zips — they get skills via the marketplace
  (`/plugin marketplace add m0xt/skills_db`).
