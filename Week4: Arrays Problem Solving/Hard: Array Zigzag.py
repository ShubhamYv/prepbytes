class Solution(object):
   def solve(self,nums,start):
      k = 0
      for i in range(start,len(nums),2):
         left = 100000 if i-1<0 else nums[i-1]
         right = 10000 if i+1>=len(nums) else nums[i+1]
         temp= (min(left,right)-1 - nums[i])
         if temp<0:
            k+=abs(temp)
      return k
   def movesToMakeZigzag(self, nums):
      ans = self.solve(nums,0)
      ans = min(ans,self.solve(nums,1))
      return ans
ob = Solution()
int(input())
print(ob.movesToMakeZigzag(list(map(int,input().split()))))
