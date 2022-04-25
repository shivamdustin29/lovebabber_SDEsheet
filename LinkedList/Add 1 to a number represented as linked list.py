 ******************** Method 1*************
class Solution:
    def addOne(self,head):
        num=0
        last=head
        while last:
            num =num*10 + last.data
            last=last.next
        num = num+1
        return Node(num)
      
 ******************Method 2***************
class Solution:
    def addOne(self,head):
        num=''
        last=head
        while last:
            num +=str(last.data)
            last=last.next
        num = int(num)
        return Node(num+1)
            
