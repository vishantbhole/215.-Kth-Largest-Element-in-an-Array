#215. Kth Largest Element in an Array

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums.sort()
        # return nums[len(nums) - k]
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap,num)
