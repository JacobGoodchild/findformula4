# Interim summary (session 1; updated 17:57 UTC)

**Best result:** none that outsiders would cite. Honest answer to "would people outside this narrow area cite this?": **No.**

**What I tried (five deep dives, all landed in known territory):**
1. *Random target lemma (Kemeny's constant) for higher moments.* The average hitting time to a random target is the same from every start. The natural second-moment version is NOT start-independent (I derived why). Known territory (Hunter; Levene-Loizou).
2. *Cayley-Menger determinant of the effective-resistance matrix.* It equals a fixed constant divided by the number of spanning trees (volume of the "resistance simplex"). Checked exactly on all 994 small connected graphs. Already in the literature (Devriendt & Van Mieghem 2018, from Fiedler).
3. *Circumsphere of that same simplex.* Centre = 1 - (1/2)(expected degree in a random spanning tree); radius^2 equals a quarter of the "energy" of the resistance-from-vertex-i function, the same for every i; radius^2 <= (1/4) x (sum of edge resistances), with equality exactly for trees. Proved, two fresh referee agents found no errors, exact checks on ~1100 graphs. But the centre and the energy identity are already known (Devriendt-Lambiotte "resistance curvature"; a Van Mieghem preprint); the rest are minor corollaries. Details: `results/circumsphere/`.
4. *Gaps between roots of a polynomial and its derivative:* Riesz's theorem, known.
5. *Kemeny constant vs Kirchhoff index:* star is extremal numerically; area already studied.
Also a blind scan of 15 graph invariants over all small graphs found no new relation.

**Most promising unfinished idea:** none strong. The only thing that might be new is the small package B/D in `results/circumsphere/` (a formula for the circumradius via "resistance-farness" differences and the tree-extremal upper bound); finishing would mean reading Fiedler's book and the cited Van Mieghem reference [13] to see if they are there already. Even then it would be a modest, niche result.

Everything is logged in CLAUDE.md, IDEAS.md, NOVELTY.md; `verify_all.py` runs and passes.
