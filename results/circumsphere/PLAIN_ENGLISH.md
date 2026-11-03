# The "resistance ball" of a network, in plain English

**Setup.** Treat a network as an electrical circuit (each link is a 1-ohm resistor). The resistance between two nodes is a number R. Remarkably, you can place the nodes as points in space so that the *square* of the distance between any two points equals their resistance. The points form a simplex (a triangle for 3 nodes, a tetrahedron for 4, and so on).

**What we found / proved (all checked exactly by computer on every network up to 7 nodes, plus weighted ones):**
1. All the points sit on the surface of one ball. Its centre is described by a simple recipe: node *i* gets weight 1 - half of its expected number of links in a random spanning tree of the network. (**Already known**: this is the "resistance curvature" of Devriendt and Lambiotte.)
2. The ball's radius squared is the same number whichever node you start from: it equals a quarter of the "energy" of the resistance-from-that-node landscape. (**Already known**, e.g. in a preprint by Van Mieghem.)
3. The radius squared is at most a quarter of the total resistance of all the links; for ordinary networks that means at most (nodes - 1)/4, and the bound is hit exactly by tree-shaped networks (no loops). (**Not found in anything I read**, but it follows in two lines from items 1 and 2, so it is a small corollary.)
4. A formula for the radius using how much each node's total resistance to everyone else differs from its neighbours'. (**Not found**, also elementary.)

**Would outsiders cite it?** No. It is a tidy corollary of a known identity in a small corner (the geometry of networks). Two independent referee agents and an independent recomputation found no errors.
