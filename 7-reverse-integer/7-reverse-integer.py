class Solution(object):
    def reverse(self, num):
        """
        :type x: int
        :rtype: int
        """
        value = num > pow(-2,31) and num < pow(2,31) - 1

        if num < 0:
            num = -1 * num
            val = str(num)
            val2 = ""
            for i in val:
                val2 = i + val2
            num2 = int('-' + val2)
        else:
            val = str(num)
            val2 = ""
            for i in val:
                val2 = i + val2
            num2 = int(val2)
        if num2 > pow(-2,31) and num2 < pow(2,31) - 1:
            return num2
        else:return 0
            
        