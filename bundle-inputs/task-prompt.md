# Task: news-image-20261120 — Sum up 20 November's world news in one image

Build an entry for the make.fun bounty `news-image-20261120`
("Sum up 20 November's world news in one image", $250 total, 1st $50,
no entry fee). Entries close 2026-11-22 09:00 KST, results due
2026-12-06 17:00 KST. The kit is at
`~/workspace/makefun/news-image-20261120-kit/` (bundle_sha256
63afd6ef327953b503d6a89b46620965d4844234f8456ecdcec384c86d63f66e).
Requirements were copied to
`~/workspace/makefun/news-image-20261120-requirements.json`. Read the
makefun-playbook skill and the 오답노트 pre-submit checklist first.
Local skill.md is pinned at 1.5.213 — do not upgrade.

## What to build

A program at the root of `~/workspace/makefun/news-image-20261120/`
named `main.py` (Python 3.13) that writes one image to
`/output/entry.png` (outside the grader, `MAKEFUN_OUTPUT_DIR` stands
in for `/output`). The program runs with no network, max 60 seconds
per run, twice, and both runs must write identical bytes. The image
is a 1024x1024 PNG of at most 1 MiB summing up Friday 20 November
2026. It must name the day clearly. The repository holds the finished
image as `entry.png`, drawn by a Pillow script, and `main.py` copies
it to the output path with the standard library only.

## Research rules

Only events that happened, or were first reported, on 20 November
2026 (any time zone). Each story cross-checked in 2+ named wire/press
outlets (AP, Reuters, AFP, BBC, NDTV, Al Jazeera, and the like).
Unknown aggregators, dateless items and social posts excluded.
Outcomes still pending at build time are phrased as happening/due
today, with no outcome invented. Write the research log at
`~/workspace/makefun/news-image-20261120-research.md`: the 6 selected
stories with sources, a rejected list with dates, and the Sensor
Studio check.

Lead source only (never sole source): YouTube channel
`UC6dN6Rilzh9KmzymxnZGslg` (센서스튜디오 / Sensor Studio). Check its
RSS for a 20 November video and use it only as a lead; a topic it
covers counts only if 2+ wires confirm it. If yt-dlp reports
IpBlocked, stop YouTube work for the day and log it.

## Build, check, bundle — do NOT submit, do NOT create the GitHub repo

- `~/workspace/makefun/news-image-20261120/` is the entry directory.
  Initialise git there (user.name ryukiheun, user.email
  ryukiheun@gmail.com) and commit everything; the tree must be clean.
- Draw the image with Pillow only, in a script written fresh in this
  session. Open the PNG and look at it: no clipped or overlapping
  text. Run the program twice and confirm identical sha256.
- Title is new: "Six Stories, One Friday" (20 Nov 2026 is a Friday).
- `README.md` follows the requirements' readme_template exactly:
  owner ryukiheun, repo news-image-20261120, referral code r5cs55h2.
  `LICENSE` is MIT with an SPDX-License-Identifier line.
- Run the kit `check` on the draft (target: thinking_reproduces 30%+
  and at least one authored line in the entrypoint). Run the presubmit
  gate `~/workspace/makefun/bin/presubmit.sh <entry-dir> <kit-dir>`.
- Bundle only this session: `--no-discover --no-family --session
  <this session file>`, with `--harness muse-app --harness-version 1.3
  --provider meta --model muse-spark-1.3 --effort default`, and
  `--muse-usage` rows pulled from muse.db into `bundle-inputs/`.
  Model names come from the pricing list — never `auto`.
- Stop after the bundle tar.gz is made. Do not submit, do not create
  or push a GitHub repo (the parent does that in the browser).
- Never write API keys or keypair contents in chat or files.
