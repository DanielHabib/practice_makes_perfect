/*
The structure of the node is

typedef struct node
{
    int freq;
    char data;
    node * left;
    node * right;

}node;
  NOTES: use string to navigate through the tree, when we hit a leaf, we add it to the output string, and return the root and continue iterat$


  Internal nodes have data='\0'(ϕ )
*/


void decode_huff(node * root, string s)
{
    node * current = new node;
    current = root;
    bool done = false;
    int i = 0;
    while (!done){
        string val;
        val = s[i];
        if (current->data!='\0'){
            cout<<current->data;
            current = root;
        }
        if (val=="1"){
            current=current->right;
        }
        else{ 
            current=current->left;
        }
        if (i==s.length()){
            done = true;
        }
        i++;
    }
}

