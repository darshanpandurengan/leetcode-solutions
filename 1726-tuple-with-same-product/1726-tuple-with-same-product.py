class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq_tuple_product = {}
        for i in range(len(nums)) :
            for j in range(i + 1 , len(nums)) :
                if nums[i] * nums[j] not in freq_tuple_product :
                    freq_tuple_product[nums[i] * nums[j]] = 1 
                else :
                    freq_tuple_product[nums[i] * nums[j]] += 1 
        res = 0 
        for v in freq_tuple_product.values() :
            if v >= 2  :
                res += 4 * v * (v - 1)
        return res