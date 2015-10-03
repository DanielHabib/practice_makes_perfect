
/*The tree node has data, left child and right child 
struct node
{
    int data;
    node* left;
    node* right;
};



  NOTES: Will have to touch every node, so a tree traversal is in order.
  BCR: O(N)
  Steps:
    1. traverse the binary tree and return the height of the branch, and from there return the higher of the two heights
*/
int height(node * root)
{
  return height_helper(root, 1);
}
  
int height_helper(node * root, int height)
{
  if (root!=NULL){
    int leftH = height_helper(root->left, height+1);
    int rightH = height_helper(root->right, height+1);
    if(leftH < rightH) {
      return rightH;
    }
    else {
      return leftH;
    }
  }  
}

