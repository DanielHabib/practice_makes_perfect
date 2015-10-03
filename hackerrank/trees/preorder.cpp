/* you only have to complete the function given below.  
Node is defined as  

struct node
{
    int data;
    node* left;
    node* right;
};

*/

void Preorder(node *root) {
  
  // DIDNT READ THE QUESTION CAREFULLY ENOUGH AND MISSED THE EXTRA WHITESPACE
  if (root!=NULL){
   cout<<root->data<<" ";
   Preorder(root.left)
   Preorder(root.right)
 }
}
