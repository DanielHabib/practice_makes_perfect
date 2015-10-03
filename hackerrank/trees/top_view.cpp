/*
struct node
{
    int data;
    node* left;
    node* right;
};
  NOTES: logic question with simple graph traversal.
        Using two helper functions here would make this way simpler,
  BCR:O(1) Best Case
      O(log(N)) average
      O(N) Worst
  Steps:
    1. create helper functions to traverse exclusively in their directions, and print the values

  MISTAKES: Even though i got it right on the first try, i should have noticed off the bat it was a variation of an inorder traversal

*/

void top_view(node * root)
{
  traverseLeft(root.left);
  cout<<root.data<<" ";
  traverseRight(root.right);
}


void traverseLeft(node * node)
{
  if (node != NULL){
    traverseLeft(node->left);
    cout<<node->data<<" ";
  }
}

void traverseRight(node * node)
{
  if (node != NULL) {
    cout<<node->data<<" ";
    traverseRight(node->right);
  }
}
