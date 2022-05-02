class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        v = str(x)
        ispal = True
        for i in range(len(v)):

            if v[i] != v[-i-1]:
                ispal = False
            
        return ispal