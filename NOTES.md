# NOTES (dead ends)
- Linear-relation scan on 15 graph invariants finds nothing new: all clean ratios are K_n or tree extremals and sit in the Kirchhoff/Kemeny/Wiener-index literature. A blind scan of this kind is unlikely to yield a citeable theorem; need a structural question instead.

## Leads for the next session (none verified as promising)
1. Find a *natural* weighting on target SETS (not pairs) for which the random-target lemma holds (weights exist in the nullspace but are unnatural); relate to determinantal/capacity structure. Risk: may be trivial or known (Aldous-Fill-type).
2. Resistance-simplex package (results/circumsphere): check Fiedler's book and ref [13] of Van Mieghem's preprint for B and D; otherwise very niche.
3. Approach D on permutation statistics (equidistribution search) with FindStat as the novelty oracle - needs network access to findstat.org; heavily mined area.
4. Lesson: blind invariant scans and 'obvious' generalisations land in known territory (5 of 5 today). Prefer a question where an *unexpected link* is suggested by data first, then literature.

## Data point (19:22 UTC): labelled 2-dimensional hypertrees (Q-acyclic 2-trees) on n vertices
Exact counts by determinant enumeration (results/higher_dim/torsion5.py, torsion6.py; cobase = edges avoiding vertex 0): n=3,4,5,6 -> 1, 4, 125, 46620 (n=6: 46608 Z-acyclic + 12 with H_1 = Z/2, i.e. RP^2 triangulations). Compare Kalai n^{C(n-2,2)} = 1, 4, 125, 46656. OEIS searches for '1,4,125,46620' and '4,125,46620' returned nothing (oeis.org search, fmt=text). Not claimed new: DKM (arXiv:1506.06819) say the true count 'probably has no closed form' and deviates at n=6, d=2. a(7) would need ~3.2e9 determinants (35 choose 15) - a C program with modular rank would do it; a possible lead for a later session, low value.
Also: weighted tree counts with weights on EDGES (face weight = product of its 3 edge weights), n=5: single edge weight s gives 5 s (2s+3)^2, matching the proved law N = 1 + Bin(2,2/5) (consistency check); two disjoint edges s,t: s t (2s+3)(2t+3)(2s+2t+1); two adjacent edges: s t (st+s+t+2)(3st+7s+7t+8) (results/higher_dim/ridgeweights2.py). No clean general product formula seen.
