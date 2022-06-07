**************************leet code  455 ***********************
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        greed=0
        cookies=0
        g.sort()
        s.sort()
        while(greed<len(g)and cookies<len(s)):
            if (s[cookies]>=g[greed]):
                greed+=1
            cookies+=1
        return greed
      
      ****************************by using heapq*****************
      class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        heapq.heapify(g)
        heapq.heapify(s)
        
        i = 0
        while g and s:
            if heapq.heappop(s) >= g[0]:
                i += 1
                heapq.heappop(g)
        return i
