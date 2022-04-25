
''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

def findIntersection(head1,head2):
    if not head1 and not head2:
       return None
   
    elif not head1:
        return head2
   
    elif not head2:
        return head1
    else:
        dummy = Node(None)
        prev = dummy
        l1 = head1
        l2 = head2
       
        while l1 and l2:
            if l1.data < l2.data:
                l1 = l1.next
           
            elif l2.data < l1.data:
                l2 = l2.next
           
            else:
                new_node = Node(l1.data)
                dummy.next = new_node
                dummy = new_node
                l1 = l1.next
                l2 = l2.next
    return prev.next

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        n1,n2 = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        
        result = findIntersection(ll1.head,ll2.head)
        printList(result)
        print()

# } Driver Code Ends
