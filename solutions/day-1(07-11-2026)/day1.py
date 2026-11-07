class Solution():
    def twoSum(self, nums, target):
        dict={}

        for i in range(len(nums)):
            need=target-nums[i]

            if need in dict:
                return dict[need],i
                break

            dict[nums[i]]=i
                

s=Solution()
ans=s.twoSum([2,7,11,15], target = 9)
print(ans)