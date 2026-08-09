class Solution(object):
    def minPrice(self, prices, discounts):
        """
        :type prices: List[int]
        :type discounts: List[int]
        :rtype: float
        """
        def PriceAfterDiscount(price , discount) :
            """
            :type price: int
            :type discount: int
            :rtype: float
            """
            return (price * (100 - discount )) / float(100)
        prices.sort(reverse = True) 
        discounts.sort(reverse = True)
        res = 0 
        for price , discount in zip(prices ,discounts ) :
            res += PriceAfterDiscount(price , discount) 
        if len(prices) > len(discounts) :
            res += sum(prices[len(discounts)  : ])
        return res