# results.md
No headline result (nothing a mathematician outside this narrow area would cite). One modest, referee-checked item:

## 1. Circumsphere of the effective-resistance simplex  -- PROVED (modest, niche)
Statement and full proof: results/circumsphere/statement_and_proof.md.
In short, for a connected weighted graph, the points whose squared distances are the effective resistances lie on a sphere with
- centre having barycentric coordinates 1 - (1/2)E[deg_T(i)] (T = random spanning tree)  [KNOWN: this is the "resistance curvature" of Devriendt-Lambiotte];
- squared radius rho^2 = kf/n^2 + (1/(4n^2)) sum_edges c_ij (F_i - F_j)^2, F_i = sum_k R_ik;
- 4 rho^2 = sum_edges c_ab (R_ia - R_ib)^2 for EVERY vertex i;
- rho^2 <= (1/4) sum_edges R_e, equality iff the graph is a tree (unit weights: (n-1)/n^2 <= rho^2 <= (n-1)/4).
Verification: two fresh referee agents (no errors; small gaps fixed); exact rational checks on 1080 graphs (verify_all.py); numeric checks to n=40.
Novelty: first item known; the formula for rho^2, the Dirichlet-energy identity and the upper bound not found in the papers opened (see NOVELTY.md), but closely related to Fiedler / Devriendt / Van Mieghem work -> probably known or minor.
