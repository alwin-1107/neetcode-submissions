class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #approach 3 O(1) Space:
        # nums.sort()

        # for i in range(len(nums) - 1): #len-1 used to prevent IndexOutOfRange error
        #    if nums[i] == nums[i+1]:
        #       return True
        # return False

        nums.sort()   #same above code in diff style, above code is simpler mentally

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False        

            
            

        