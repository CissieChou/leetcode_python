class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort(lambda x,y:(int(str(y) + str(x))) - int(str(x) + str(y)))
        result = "".join([str(num) for num in nums]).lstrip("0")
        if len(result) > 0:
            return result
        else:
            return "0"