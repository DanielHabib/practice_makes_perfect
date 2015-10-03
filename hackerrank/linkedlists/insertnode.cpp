/*
  Insert Node at the end of a linked list   head pointer input could be NULL as well for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Insert(Node *head,int data)
{
  // Complete this method
        if (!head) {
                Node *newHead = Node(data);
                return newHead;
        }
        Node * current = head;
        while (current) {
                if (!current->next) {
                        Node* tail = Node(data);
                        current.next = tail;
                        break;
                }
                current=current->next;
        }
        return head;
}

