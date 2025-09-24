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
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,num)

        return heap[0]

if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    print("Output is : ", sol.findKthLargest(nums, k))

    nums2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    print("Output is : ", sol.findKthLargest(nums2, k2))


