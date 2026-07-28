class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #approach 2:
        set_nums = set()
                         #For duplicates,we check if we alr entered into set
        for num in nums:
            if num in set_nums:
                return True

            set_nums.add(num)
        return False

#more efficient than sorting, as in case of duplicates toward front