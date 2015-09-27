## Things to pay attention when dealing with Graphs
* Is this search? If so whether to use BFS or DFS
* Always ask what details are available on the nodes
* Consider if anything can be gained from knowing the depth of the tree
* Maintaining access to the size of the subtrees can yield information that can be used to know exactly what lies below you at any given node in a tree

## General Takes Aways
* Understanding the Time Complexity associated with Trees and Graphs is crucial to understanding why they are so important
* Generating random numbers can be very expensive.

## Mistakes
* BST's are smallest to the left and larger to the right, not the other way around
* BST's follow the criteria that the entire left subtree is smaller than the current node and the entire right subtree is greater, when trying to validate a bst we must take this in to accound
* When trying to see if a Binary Tree is balanced, it doesn't suffice to just check the leaves, this would neglect all nodes with only 1 child. The nodes with 1 child aren't neccesary 1 away from the end
* If asked to build some datastructure from scratch, it usually means that the datastructure must be tweaked to suite your needs
