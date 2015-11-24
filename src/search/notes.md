## Different Graph Traversals

* Dijkstra
 * This is the same as BFS, BFS uses a queue, Dijkstra uses a Priority queue which is a max heap, assuming higher priority means higher preference.
 * Also when visiting a node, we need to check whether the length of the path to the node is shorter than its current path valu8e, otherwise we don't go there.
 * Building the priority queue is the kicker here, otherwise it is very straightforward

* Astar
 * Astar also makes use of a priority queue but has a special method for determining priority, a heuristic function.
 * a heuristic function is some function that evaluates which node is closer to our goal, usually by some distance formula.
 * We would use a min-heap - priority queue.
 * This is used to attempt to get to the goal i nthe shortest time, not the shortest distance.
