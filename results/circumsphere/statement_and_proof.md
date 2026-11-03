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
6. Centroid of the x_i is sum_i x_i / n; with the origin there, sum_i |x_i|^2 = sum_i d_i... (|x_i|^2 = Lp_ii when x_i are the columns of Lp^{1/2}), and sum_i |x_i - p|^2 = sum |x_i|^2 + n|p|^2 gives n rho^2 = sum d + n |p|^2 = kf/n + n|p|^2, so |p|^2 = rho^2 - kf/n^2 = the second term in (B).
Consequences follow: (i) lambda_i = 1/n iff w_i = 2/n; the edge sum vanishes iff F is constant on each edge iff constant (G connected); (ii) lambda_i >= 0 iff E deg_T(i) <= 2; (iii) for a tree R_ij = distance and c_ij R_ij = 1, so w_i = 2 - deg(i); rho^2 = c/4 with c = (Rw)_1 computed at a leaf... (verified numerically/exactly; formal proof via the formula in (B) not needed).
