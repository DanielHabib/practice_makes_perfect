""" 2.4 Partition """



def parition:
    """
        time: 11:11
    """
    def partition(x, llist):
        head = llist.head
        current = head
        while current:
            if current.data < x:
                llist.addnewhead(current)
                temp = current
                llist.delnode(current)
                current = temp.next
