# SESSION OVERRIDE (from Jacob, supersedes timings in the brief below)
- Session 1: work until **18:35 UTC (6:35pm)**, then commit, push, cancel wake-ups, and STOP. Do not schedule wake-ups past 18:35 UTC.
- Jacob will give the all-clear later (before ~20:00 UTC). After that, continue until he says stop; the "07:00 UK" deadline and backup chain in the brief are then replaced by his instructions.
- Scheduling tool available: `send_later` (mcp__claude-code-remote). Wake-up trig_01Gp3VLD71dJXms2az36cHVd set for 18:10 UTC.

# findformula4: overnight discovery brief

You are working in the GitHub repo **JacobGoodchild/findformula4** (new and empty). Work **all night without stopping until 07:00 UK time (07:00 UTC; the clocks are on GMT)**. Don't ask me questions; I'm asleep. Make the most reasonable choice, write down why in the log, and keep going. Never stop early because "enough has been done".

**First thing:** copy this whole brief into `CLAUDE.md` at the top of the repo, with an empty `## Progress log` section underneath. That file is your memory if you get restarted.

---

## 0. Usage limits: keep a wake-up alarm set (set this up FIRST)

A usage limit can stop you partway through the night, and you can't make a tool call once it hits. So keep a "dead man's switch" running:

1. **Right at the start**, use your scheduling tool (`send_later`, or `ScheduleWakeup`; search your tools for "schedule" if neither shows) to schedule a message back into **this same session** about **45 minutes** from now, saying:
   `WAKE-UP CHECK: if you were stopped by a usage limit, re-read CLAUDE.md (brief + progress log), check git status and git log, and carry on from where you left off until 07:00 UK. If you are already mid-task, ignore this, but make sure a new wake-up is scheduled.`
2. **After every commit**, schedule a fresh wake-up about 45 minutes ahead, and cancel the older one if your tool allows it.
3. **Backup chain:** at the start, also schedule wake-ups at **23:00, 00:30, 02:00, 03:30, 05:00 and 06:15 UK**.
4. **After any restart**, first re-read CLAUDE.md and `git log`. Never redo committed work. The machine restarted about every 40 minutes last time, killing background jobs, so write long jobs to **save progress to disk and resume**, and check/relaunch them after every wake-up.
5. **At about 06:45 UK**, cancel any wake-ups scheduled after 07:00.
6. **If no scheduling tool exists in this session**, write that as the first line of the progress log.

Commit and push after every small step, with a short progress-log entry each time.

---

## 1. What I want (read this twice)

I want **one result that people would actually cite**: a genuine theorem or law of the kind that could end up with a name on it. Think of results like Kirchhoff's matrix-tree theorem, Pick's theorem, or a surprising universal law. Something general, clean and surprising, not a footnote.

**What I do NOT want:**
- closed forms or digit-matching for individual constants;
- lower/upper bounds, or pushing a known range or record slightly further;
- chasing loose ends, typos or passing remarks in recent papers;
- a "conjecture generator" that spits out dozens of unproved observations;
- obscure objects that hardly anyone studies;
- famous moonshots (P vs NP, Riemann, Navier–Stokes, …) and benchmark problems that big AI labs are already hammering (Erdős problems, cap sets, packing records, autocorrelation constants, matrix-multiplication ranks, kissing numbers).

**What a good result looks like:**
1. It is about a **central, widely taught object** (graphs and matrices, polynomials, random walks, triangles/polygons/polytopes, integer sequences, permutations, classical mechanics, electrical networks, probability distributions, …).
2. It is a statement about a **whole infinite family**, not one value.
3. It is **surprising** or **connects two areas** that weren't known to be linked.
4. It is **clean enough to state in two lines** and it is **proved** (or, at minimum, proved in a substantial special case with overwhelming evidence for the rest).
5. A mathematician outside the narrow area would say "huh, that's neat".

My best earlier result is a model of the *style* (not the topic): in findformula, the quantum-walk trapping problem turned out to be secretly the same as electrical current flow (Kirchhoff's transfer currents), which gave one universal inequality for all lattices of a certain type, with exact equality on honeycomb, diamond and Laves. A hidden link between two areas, then a general theorem.

Be honest: this is hard, and a night may end with nothing citeable. That's acceptable. Padding the report with small results is not.

---

## 2. Method: try these discovery approaches (not paper-chasing)

Spend the first ~45 minutes choosing a **playground**: a classical area where computation is cheap and the objects are central. Pick 2–3 playgrounds and say why in `PLAN.md`. Then use these approaches; invent better ones if you see them.

**A. Bridge hunting.** Take one family of objects (e.g. all small graphs, all lattice polygons, all polynomials of a type) and compute invariants **from different areas of maths** on the same objects: spectral, combinatorial, probabilistic, geometric, algebraic. Then search for **exact relations between invariants from different areas** that hold across the whole family. A relation linking two areas is the prize. (This is how the transfer-current link was found.)

**B. Generalise a classical theorem.** Take a famous classical theorem and search computationally for a natural generalisation that holds *exactly*: to weights, to higher dimensions, to a "quantum", "q-" or "signed" version, to a different geometry, to random versions. Before working, check thoroughly that the generalisation isn't already known (most obvious ones are).

**C. Universal laws.** Compute one natural quantity over thousands of random or exhaustive instances and look for something that is **always** true: an invariant, an equality, a sharp inequality whose extreme cases are all a recognisable family. Then explain *why*, and prove it.

**D. Hidden structure.** When an exhaustive computation shows a sequence or table, check whether it matches something from a totally different area (search OEIS, the online encyclopedia of integer sequences, then the literature). An unexpected match between two areas suggests a bijection or identity: find and prove it.

Workflow for each idea: **explore → spot a pattern → test it hard on much bigger/different cases (try to break it) → check the literature → prove it → write it up.** Drop patterns quickly when they're already known or only hold for small cases.

**Prove things.** Proofs are the goal; numbers are only evidence. Use computer algebra to check every step of a proof, and rigorous arithmetic (interval/ball arithmetic, exact rationals) for any computation a proof depends on.

---

## 3. Novelty checking (lessons from last time)

Last time, **4 of 13 results turned out to be already known** after a proper search. So for every pattern before you invest time in proving it, and again before recording it:
- at least 5 different web searches, including the **classical** literature (old results are the most likely rediscoveries), textbooks, and surveys of the area;
- search OEIS for any integer sequence that appears;
- if a related paper turns up, read its **latest version**, its **follow-ups and citing papers**, and the **end of the PDF** (corrigenda, addenda);
- render any formula you quote from a PDF as an image and read it, rather than trusting garbled text;
- **never** write a citation from memory, and never invent authors, titles or quotes. Only cite what you opened.

Record searches and verdicts in `NOVELTY.md`: "not found" / "probably known" / "known", with links.

---

## 4. Checking results

- Every recorded result gets **independent verification**: spawn a **fresh agent** (Agent tool) that has not seen your work, give it only the statement and the proof, and ask it to referee sceptically (gaps, hidden assumptions, missed cases). Fix and re-referee until clean, or downgrade.
- Numerical claims are recomputed by a fresh agent with fresh code, by a different method where possible.
- Labels: **PROVED**, **PROVED (special case) + strong evidence**, **CONJECTURE (strong evidence)**. Be honest.
- At most 3 items should end up in `results.md`. Quality over quantity: one real theorem beats ten observations.

---

## 5. Time plan

- **Start–22:15:** set up wake-ups, CLAUDE.md, choose playgrounds (`PLAN.md`).
- **22:15–05:30:** discovery and proving. Timebox each idea to about 2 hours unless it is clearly going somewhere (then keep going and say so in the log). Keep a running `IDEAS.md`: each idea, what was tried, status (dead / known / promising / proved).
- **05:30–06:30:** verification of the best result(s) by fresh referees; novelty checks re-done.
- **06:30–07:00:** wrap-up.

---

## 6. Rules (non-negotiable)

1. **Verify everything.** If a check fails, the result is wrong until shown otherwise.
2. **Never invent citations, numbers, quotes or authors.**
3. **Honest labels.** Proved means proved. New means searched.
4. **Computing only on this session's own machine. Never use GitHub Actions** or any cloud service. Don't hammer websites.
5. **Never post, upload, email, comment or submit anything anywhere.** I decide what gets shared.
6. Long jobs in the background with logs and resumable progress; no orphaned processes; never `pkill -f`/`pgrep -f` with a pattern that matches your own shell.
7. **AI disclosure** in the README: the research was carried out by Claude (Anthropic), via Claude Code, under the direction of Jacob Goodchild, as in my earlier repos.

### Repo layout
`CLAUDE.md` (brief + log), `PLAN.md`, `IDEAS.md`, `NOVELTY.md`, `results.md` (at most 3 items: statement, label, proof or proof location, verification, novelty), `results/<name>/` (code, logs, proofs), `NOTES.md` (dead ends, leads), `verify_all.py`.

---

## 7. Wrap-up (06:30)

1. Run `verify_all.py`; fix or downgrade anything that fails.
2. Write `MORNING_SUMMARY.md` in **plain English, no jargon**:
   - the best result (if any), in two lines, with its label, and an honest answer to: **"Would people outside this narrow area cite this? Why or why not?"**
   - what was explored and didn't work, briefly;
   - the most promising unfinished idea, and what it would take to finish it.
   No draft emails.
3. Update the README (with the AI disclosure), commit, push, and cancel leftover wake-ups.

Go. Set up the wake-ups, write CLAUDE.md, then start.


## Progress log

- 17:26 UTC: started; sympy/numpy/scipy/networkx installed; wake-up set.
- 17:29 UTC: PLAN/IDEAS/NOVELTY/NOTES created; graph scan (results/graphs_explore) found nothing new. Next: a structured generalisation search (approach B).
- 17:29 UTC: UST probe (I3) dead; results.md/README/verify_all stubs written.
- 17:30 UTC: interim stop. Wake-up trig_01Gp3VLD71dJXms2az36cHVd to be deleted. Waiting for Jacob's all-clear.
- 17:39 UTC: deep dive 1 (random target lemma, higher moments) dead; logged. Continuing with next single theorem.
- 17:41 UTC: deep dive 2 (CM det of resistance matrix) verified on 994 graphs but KNOWN (Devriendt-Van Mieghem 2018 eq 28). Next: pick another.
- 17:45 UTC: deep dive 3 (resistance-simplex circumsphere): Thm A known (Devriendt-Lambiotte resistance curvature); B formula proved, minor. Referee agent launched. Trying to prove rho^2 <= (n-1)/4.
- 17:47 UTC: referee round 1 passed on A/B; added C and upper bound D (proved, exact-checked). Niche, not citeable by outsiders. Need referee round 2 on C/D.
- 17:51 UTC: referee round 2 passed (C, D, lower bound); gaps filled.
- 17:53 UTC: Van Mieghem preprint shows Thm C already known. Deep dive 3 = known territory. Next: pick deep dive 4.
- 17:54 UTC: probes 4,5 (root gaps; Kemeny vs Kirchhoff) known. No headline result so far.
- 17:57 UTC: probes 6,7 dead; next-session leads in NOTES.md.
- 17:58 UTC: probes 8,9 dead/known.
- 18:00 UTC: independent recomputation of numerical claims PASSED.
- 18:13 UTC: probes 11,12 dead; large-n check of circumsphere theorems passed. Final wrap wake-up set 18:31 UTC.
- 18:30 UTC: SESSION 1 STOP. All work committed. Wake-ups cancelled. Waiting for Jacob's all-clear; on resume re-read this file, MORNING_SUMMARY.md, IDEAS.md, NOTES.md (leads).
- 19:07 UTC: Jacob gave the go-ahead: work until 19:40 UTC (higher dimensions / formulas / anything interesting).
- 19:10 UTC: higher-dim face-degree law proved but KNOWN (Vander Werf 2022 Thm 2 corollary).
- 19:18 UTC: hypertree counts 1,4,125,46620 (data point); ridge-weighted counts consistency; no new theorem.
- 19:34 UTC: SESSION 2 STOP (Jacob's 19:40 deadline). Work committed. Wake-ups cancelled/fired. Waiting for Jacob.
- 19:48 UTC: OVERNIGHT low-usage mode started: scripts in overnight/, wake-ups every ~75 min (21:00,22:15,23:30,00:45,02:00,03:15,04:30,05:45,06:45 UTC), each wake-up only runs overnight/status.sh. No agents.
- 21:01 UTC: check 21:00: machine had restarted; relaunched hypertree7 (118/128ish prefixes, 259.7M bases so far), relminer 7x and 8 (n=8 graph count 11117 ok).
- 22:16 UTC: check 22:15: hypertree7 DONE: n=7 -> 281314537 hypertrees (torsion Z/2: 386904; sum|H|^2 = 7^10 verified). relminer 7x/8 relaunched (restart-killed).
