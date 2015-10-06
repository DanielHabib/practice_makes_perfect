/*
  Insert Node at a given position in a linked list 
  head can be NULL 
  First element in the linked list is at position 0
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* InsertNth(Node *head, int data, int position)
{
  // Complete this method only
  // Do not write main function. 
  if (head==NULL && position==0) {
    return head;
  }
  
  int i = 0;
  Node * current = new Node;
  current = head;
  while (i!=) {
    current = current.next;
    i++;
  }
  if (current.next){
    if (current.next.next){
        Node newNode = new Node;
        newNode->data = data;
        newNode->next = current->next->next;
        current->next = newNode;
        return head;
    }
  }
}

