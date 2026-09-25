class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # holds values to find repeat
        seen = set()

        # iterate unique vlaues
        for i in nums:
            # match then give true; else add it to holder
            if i in seen:
                return True
            seen.add(i)
        return False 