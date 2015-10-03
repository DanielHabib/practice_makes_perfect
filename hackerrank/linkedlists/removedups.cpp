/*
  Remove all duplicate elements from a sorted linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }

  NOTES: check header for null
  BCR: O(N) 
  Steps:
    pre: check for empty list
    1. Loop through the list
       {Conditions}
    2. return head;

   Conditions: 
	1. if node.data == node.next.data : node.next = node.next.next ; delete node.next from existance;
		** Repeat this step until node.data != node.next.data
		** If the end of the list is hit, break away **
        2. node -> node.next   
*/
Node* RemoveDuplicates(Node *head)
{
  // This is a "method-only" submission. 
  // You only need to complete this method.
  if (head == NULL) {
    return NULL;
  }
  Node * current = head;
  while (current!=NULL) {
    if (current->next==NULL){
       break;
    }
    while(current->data == current->next->data) {
 	    if (current->next->next==NULL){
		current->next = NULL;
       		return head;
	    }
     	     current->next = current->next->next;
    }
    current = current->next;
  }
  return head;
}

