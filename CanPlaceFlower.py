class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l=len(flowerbed)
        i=0
        amount=0
        #front corner case
        if flowerbed==[0]:
            return True
        
        if flowerbed[0]==0 and flowerbed[1]==0:
                amount+=1
                flowerbed[0]=1
                i+=2
        else:
                i+=1
                
        while i<(l-1):
            if flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0:
                flowerbed[i]=1
                amount+=1
                i+=2
            else:
                i+=1
        #rear corner case
        if flowerbed[l-2]==0 and flowerbed[l-1]==0:
            amount+=1
        
        if amount>=n:
            return True
        else:
            return False
