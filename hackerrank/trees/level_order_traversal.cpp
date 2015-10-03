
/*
struct node
{
    int data;
    node* left;
    node* right;
}

  NOTES: Breadth First Search, maybe use a queue, is there an easier way? Lets go with a queue, since it is awesome and prevents us from over complicating it
        write as if i have a queue, and ill go back and fill it in after 
 Steps:
    1. implement bfs and turn my "visit" into a print
 

    Plot Twist:
      No access to a queue. Now what.... custom linked list?
*/

struct LinkedList 
{
  llNode * head;
  llNode * tail;
}

struct llNode 
{
  node* Node;
  llNode * next;
}

node dequeue(LinkedList * ll)  
{
  ll->head = ll->head->next;
  return ll->head;
}

node enqueue(LinkedList * ll , node * Node) 
{
    ll->tail->next = Node;
    ll->tail == Node;
}

bool isEmpty( LinkedList *ll)
{
  if (ll.head != NULL){
    return True;    
  }
  return False;
}

void LevelOrder(node * root)
{
  

  if (root != NULL){
   LinkedList * list = new LinkedList;
   list->head = root;
   list->tail = root;
   while (list->head != NULL) {
      node * child = dequeue(list);
      cout<<node->data<<" ";
      if (node->left != NULL) {
        enqueue(node->left);
      }
      if (node->right != NULL){
        enqueue(node->right);
      }
    } 
  }
}

