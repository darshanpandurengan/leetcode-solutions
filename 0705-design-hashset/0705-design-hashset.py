class MyHashSet(object):

    def __init__(self):
        self.arr = [0] * (10**6 + 1) 

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.arr[key] = 1 
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.arr[key] = 0 

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.arr[key] == 1 


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)