class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Turn everything to set to remove unique pairs
        check = set(nums)
        set_length = len(check)
        # If length is the same, then no unique pairs
        if set_length == len(nums):
            return False
        else:
            return True        