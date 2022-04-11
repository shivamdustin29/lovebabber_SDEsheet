def removeLoop(self, head):  
      if self.head is None:
          return
      if self.head.next is None:
          return
      slow = self.head
      fast = self.head
           
      while(slow_p and fast_p and fast_p.next):
          slow = slow.next
          fast = fast.next.next
  
          # If slow_p and fast_p meet at some point then
          # there is a loop
          if slow == fast:
            slow = self.head
              # Finding the begining of the loop
            while (slow.next != fast.next):
              slow = slow.next
              fast = fast.next
  
                # Sinc fast.next is the looping point
            fast.next = None  # Remove loop
      
      -----------------------------************--------------------------------
      with the help of set()
      
      def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        
        s=set()
        while head:
            if head not in s:
                s.add(head)
                if head.next in s:
                    # loop is present
                    # remove the loop
                    head.next=None
                    return
            head=head.next
