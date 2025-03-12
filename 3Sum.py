class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        s_nums = sorted(nums)
        for n_i, i in enumerate(s_nums):
            for n_j, j in enumerate(s_nums[n_i+1:], n_i+1):
                for n_k, k in enumerate(s_nums[n_j+1:], n_j+1):
                    if i + j + k == 0:
                        ret.add((i, j, k))
        return list(ret)
