/*
Node is defined as 

typedef struct node
{
   int data;
   node * left;
   node * right;
}node;

  NOTES: simple binary tree insertion. The only thing I will need for this is to traverse the bst intelligently and add it on.
*/


node * insert(node * root, int value)
{
   node * newNode = new node;
   newNode->data = int;
  if (root == NULL){
    return newNode; 
  }
   node * current = root;
 
   while (current) {
      if (current->data < value)
      {
        if (current->right == NULL)
        {
          current->right = newNode;
          return root;
        }
        current = current->right
      }
      else {
        if (current->left == NULL)
        {
          current->left = newNode;
          return root;
        }
        current = current->left;
      }
    


   }
   return root;
}

