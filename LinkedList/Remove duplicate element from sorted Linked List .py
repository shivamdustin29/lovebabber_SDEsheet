def removeDuplicates(head):
      if not head:return None
      slow, fast = head, head.next
      while fast:
          if slow.data == fast.data:
              slow.next = fast.next
          else:
              slow = slow.next
          fast = fast.next
      return head
