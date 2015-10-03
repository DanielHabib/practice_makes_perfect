/*
Node is defined as 

typedef struct node
{
   int data;
   node * left;
   node * right;
}node;

  NOTES:
      We need to make use of binary search and in some instances this can happen in constant time.
      Since its a search tree, we just need to find what value is between the two, then we have the lca.
  This one is really simple and should be quick
*/


node * lca(node * root, int v1,int v2)
{
  int small, big;
  if (v1<v2){
    small = v1;
    big = v2;
  }
  else{
    small = v2;
    big = v1;
  }
  if (root->data >= small || root->data <= big){
    return root;
  } 
  else{
    if (small > root->data){
      lca(root.right, v1, v2);
  }else{
      lca(root.left, v1 ,v2);
    }
  
  }
  lca(root.left, v1, v2);

   
}

