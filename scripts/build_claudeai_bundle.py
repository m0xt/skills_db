#!/usr/bin/env python3
"""Build claude.ai-uploadable skill zips from the repo (source of truth).

claude.ai org Skills need: one zip per skill (folder containing SKILL.md), and a
description <= 200 chars. Repo SKILL.md descriptions stay rich (for Claude Code);
here we swap in a tight single-line description and zip each skill folder.

Re-run after editing any skill. Output: claude-ai-bundle/<skill>.zip
"""
import os, re, shutil, zipfile, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "plugins", "research-kit", "skills")
BUILD = os.path.join(ROOT, "claude-ai-bundle")
STAGE = os.path.join(BUILD, "_stage")

# Tight, trigger-preserving descriptions (<=200 chars) for claude.ai.
SHORT = {
 "initiating-coverage": "Create a full initiating-coverage report end to end: company research, financial model, valuation, charts, and the write-up. Use to start coverage on a new name.",
 "earnings-analysis": "Write a post-earnings update for a covered company: beat/miss vs estimates, key metrics, revised numbers, updated thesis. Use after a company reports quarterly results.",
 "earnings-preview": "Build a pre-earnings preview with scenarios: what to watch, consensus, and bull/base/bear setups. Use before a company reports to prep for the print.",
 "idea-generation": "Screen stocks and source investment ideas via quantitative screens and thematic sweeps. Use for 'find ideas', 'run a screen', or 'pitch me something'.",
 "sector-overview": "Create a sector/industry landscape report: market dynamics, key players, competitive positioning, and themes. Use for sector deep dives or thematic research.",
 "thesis-tracker": "Maintain and update investment theses over time: log data points, catalysts, milestones, and check if a thesis still holds. Use to update or review a position.",
 "catalyst-calendar": "Build a calendar of upcoming catalysts across your coverage: earnings, launches, regulatory and macro events. Use for 'what's coming up' or an earnings calendar.",
 "model-update": "Update an existing financial model with new data: refresh actuals, roll periods forward, re-run outputs. Use when new results or figures need to flow into the model.",
 "morning-note": "Draft a concise morning meeting note: overnight moves, key headlines, and takeaways for the day. Use to prep a daily market or coverage note.",
 "dcf-model": "Build a DCF valuation in Excel: pull financials, project cash flows, compute WACC, run sensitivity, output intrinsic value per share. Use to value a company.",
 "3-statement-model": "Build or fill a linked 3-statement model (income statement, balance sheet, cash flow) in Excel with correct formulas. Use to build a company's core operating model.",
 "comps-analysis": "Build a comparable-company analysis in Excel: operating metrics, valuation multiples, and peer benchmarking to spot over/undervaluation. Use for relative valuation.",
 "audit-xls": "Audit a spreadsheet or financial model for formula errors, broken links, and integrity issues (balance, cash tie-out, logic). Use to QA/debug a model or check formulas.",
}

def rewrite_frontmatter(text, name, desc):
    # replace everything between the first pair of --- lines with name+description
    m = re.match(r"^---\n.*?\n---\n", text, re.DOTALL)
    body = text[m.end():] if m else text
    return f"---\nname: {name}\ndescription: {desc}\n---\n{body}"

def main():
    if os.path.exists(BUILD):
        shutil.rmtree(BUILD)
    os.makedirs(STAGE)
    problems = []
    made = []
    for name in sorted(os.listdir(SKILLS)):
        src = os.path.join(SKILLS, name)
        if not os.path.isdir(src):
            continue
        if name not in SHORT:
            problems.append(f"{name}: no short description defined"); continue
        desc = SHORT[name]
        if len(desc) > 200:
            problems.append(f"{name}: short desc {len(desc)} > 200"); continue
        dst = os.path.join(STAGE, name)
        shutil.copytree(src, dst)
        skill_md = os.path.join(dst, "SKILL.md")
        with open(skill_md, encoding="utf-8") as f:
            text = f.read()
        with open(skill_md, "w", encoding="utf-8") as f:
            f.write(rewrite_frontmatter(text, name, desc))
        zip_path = os.path.join(BUILD, f"{name}.zip")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            for root, _, files in os.walk(dst):
                for fn in files:
                    full = os.path.join(root, fn)
                    arc = os.path.relpath(full, STAGE)  # top folder = skill name
                    z.write(full, arc)
        made.append((name, len(desc)))
    shutil.rmtree(STAGE)

    print(f"Built {len(made)} skill zips -> {BUILD}")
    for n, l in made:
        print(f"  {n:<22} desc {l:>3}/200  -> {n}.zip")
    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print("  -", p)
        sys.exit(1)

if __name__ == "__main__":
    main()
