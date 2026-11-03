# Circumsphere of the effective-resistance simplex (statement + proof)

Setting. G connected, vertices 1..n, positive edge conductances c_ij (c_ij=0 for non-edges), Laplacian L (L_ii = sum_j c_ij, L_ij = -c_ij), Lp its Moore-Penrose pseudoinverse, d_i = Lp_ii,
effective resistance R_ij = d_i + d_j - 2 Lp_ij (R_ii = 0), R = d 1^T + 1 d^T - 2 Lp.
Write kf = sum_{i<j} R_ij (Kirchhoff index; kf = n * tr Lp), F_i = sum_k R_ik, and
  w_i = 2 - sum_j c_ij R_ij .
(By Kirchhoff, c_ij R_ij = P(edge ij in the weighted random spanning tree T), so w_i = 2 - E[deg_T(i)].)
Let x_1..x_n be points with |x_i - x_j|^2 = R_ij (they exist, are affinely independent, span R^{n-1}: Gram matrix of x_i - x_n is the inverse of the reduced Laplacian).

Theorem.
(A) w_1+...+w_n = 2 and R w = c 1 for a constant c. The points x_i lie on a sphere whose centre is p = sum_i (w_i/2) x_i, i.e. has barycentric coordinates
      lambda_i = 1 - (1/2) E[deg_T(i)].
(B) Its squared radius is rho^2 = c/4 = kf/n^2 + (1/4) sum_{i<j} c_ij (d_i - d_j)^2 = kf/n^2 + (1/(4 n^2)) sum_{i<j} c_ij (F_i - F_j)^2,
    and |p - centroid|^2 = (1/(4n^2)) sum_{i<j} c_ij (F_i - F_j)^2.
Consequences. (i) circumcentre = centroid iff F_i is the same for all i iff E[deg_T(i)] = 2 - 2/n for all i. (ii) circumcentre lies in the closed simplex iff E[deg_T(i)] <= 2 for all i. (iii) For a tree with unit weights, lambda_i = 1 - deg(i)/2 and rho^2 = (n-1)/4.

Proof.
1. L R = (L d) 1^T + 0 - 2 L Lp = (Ld)1^T - 2(I - J/n), using L1 = 0, L Lp = I - J/n.
   Diagonal entries: (LR)_ii = sum_j L_ij R_ji = -sum_{j!=i} c_ij R_ij  (as R_ii = 0). Comparing with the formula, (Ld)_i - 2 + 2/n = -sum_j c_ij R_ij, i.e.
   (Ld)_i = w_i - 2/n.  Hence L R = w 1^T - 2I.      (*)
2. Multiply (*) on the left by 1^T: 0 = (1^T w) 1^T - 2 * 1^T, so 1^T w = 2.
3. Multiply (*) on the right by w: L(Rw) = w (1^T w) - 2 w = 0, so Rw lies in ker L = span(1): Rw = c 1.
4. Let lambda = w/2, so sum lambda = 1 and R lambda = (c/2) 1. For any lambda with sum 1 and p = sum lambda_j x_j one has |x_i - p|^2 = (R lambda)_i - (1/2) lambda^T R lambda.
   Here lambda^T R lambda = (c/2) sum lambda = c/2, so |x_i - p|^2 = c/2 - c/4 = c/4 for every i. Thus p is equidistant from all vertices and lies in their affine hull, so it is the circumcentre, rho^2 = c/4.
5. Compute c. Rw = d (1^T w) + 1 (d^T w) - 2 Lp w = 2d + (d^T w) 1 - 2 Lp w. By step 1, w = L d + (2/n) 1, so Lp w = (I - J/n) d = d - (sum d / n) 1.
   Therefore Rw = (d^T w + 2 sum d / n) 1, c = d^T w + 2 (sum d)/n, and d^T w = d^T L d + (2/n) sum d. So c = d^T L d + 4 (sum d)/n.
   Using sum d = tr Lp = kf/n and d^T L d = sum_{i<j} c_ij (d_i - d_j)^2 gives rho^2 = c/4 = kf/n^2 + (1/4) sum c_ij (d_i-d_j)^2.
   Since F_i = sum_k (d_i + d_k - 2 Lp_ik) = n d_i + sum d, d_i - d_j = (F_i - F_j)/n.
6. Choose x_i = columns of Lp^{1/2} (so sum x_i = 0, centroid at the origin, |x_i|^2 = d_i). Then sum_i |x_i - p|^2 = sum |x_i|^2 + n|p|^2 gives n rho^2 = sum d + n |p|^2 = kf/n + n|p|^2, so |p|^2 = rho^2 - kf/n^2 = the second term in (B).
Consequences. (i) w_i = 2/n for all i iff Ld = 0 iff d constant iff F constant (G connected). (ii) lambda_i >= 0 iff E deg_T(i) <= 2. (iii) Tree, unit weights: R_ij = dist, c_ij R_ij = 1, w_j = 2 - deg(j). Fix any vertex i, D_j = dist(i,j), S = sum D_j. c = (Rw)_i = 2S - sum_j D_j deg(j); deg(j) = 1 + children(j) for j != i, and sum_j D_j children(j) = sum_{k != i}(D_k - 1) = S - (n-1), so sum D_j deg(j) = 2S - (n-1) and c = n-1, rho^2 = (n-1)/4. (Referee-supplied proof.)

## Theorem C (added after referee round 1) and the upper bound
(C) For EVERY vertex i:  4 rho^2 = c = sum_{ab in E} c_ab (R_ia - R_ib)^2   (Dirichlet energy of the function a -> R(i,a)).
Proof: column i of R is R e_i; by (*) L R e_i = w - 2 e_i, so (R e_i)^T L (R e_i) = (R e_i)^T (w - 2e_i) = (Rw)_i - 2 R_ii = c.
(D) rho^2 <= (1/4) sum_E c_ab R_ab^2 = (1/4) sum_E q_e R_e <= (1/4) sum_E R_e, where q_e = c_e R_e = P(e in T) <= 1; equality in the last step iff every q_e = 1 iff G is a tree (in which case the first is equality too). For unit weights: rho^2 <= (n-1)/4 (Foster: sum_E R_e = n-1), equality iff G is a tree.
Proof: resistance distance is a metric (triangle inequality), so |R_ia - R_ib| <= R_ab; insert in (C).
Lower bound: rho^2 >= kf/n^2 (from B), and kf >= n-1 for unit weights (K_n minimal), so rho^2 >= (n-1)/n^2, equality iff K_n.
Exact rational checks: results/resistance_simplex/exact_C.py (1080 graphs incl. weighted), numeric scan up to n=25 weighted (results/circumsphere/ub.py).

## Referee round 2 additions (fresh agent; verdict: C, D, lower bound correct; gaps filled below)
- Triangle inequality for R (Klein-Randic 1993; short proof): for k, let v = Lp(e_i - e_k), harmonic off {i,k}, so v_k <= v_j <= v_i (maximum principle). R_ij = (e_i-e_j)^T Lp (e_i-e_k) + (e_i-e_j)^T Lp (e_k-e_j) = (v_i - v_j) + (u_j - u_i) with u = Lp(e_j - e_k), u_k <= u_i; so R_ij <= (v_i - v_k) + (u_j - u_k) = R_ik + R_jk. Valid for positive weights.
- q_e = c_e R_e = P(e in T) <= 1 (Kirchhoff / leverage score of a projection). Equality q_e = 1 for all e iff all edges are bridges iff G is a tree.
- Foster sum_E R_e = n-1 is the UNIT-WEIGHT case only; for weighted graphs the bound is rho^2 <= (1/4) sum_E q_e R_e <= (1/4) sum_E R_e.
- Lower bound (unit weights, simple graph): kf = n * sum_{i>=2} 1/mu_i, and mu_i <= n, so kf >= n-1, equality iff all nonzero mu_i = n iff G = K_n. False for weighted graphs.
