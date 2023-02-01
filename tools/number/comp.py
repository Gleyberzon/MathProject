import MyFunctions


class Comp:
    flag=False
    dc = MyFunctions.get_vars()
    def sumofdigits(num):
        """
        Name: Roman Gleyberzon
        Date: 01/02/2023
        Description: This method calculates sum of all digits of number
        Input: int number
        Output: sum
        """
        if Comp.flag==False:
            raise ConnectionAbortedError(Comp.dc['ERR_NOT_CALLED_SIMP_FUN'])
        if not isinstance(num, int):
            raise ValueError(Comp.dc["ERR_NOT_INT_NUM"])
        sum = 0
        while num != 0:
            sum += num % 10
            num = num // 10
        return sum

    def ispal(num):
        """
        Name: Roman Gleyberzon
        Date: 01/02/2023
        Description: This method check if the given number is polindrome
        Input: int number
        Output: isPolindrome True / False
        """
        if Comp.flag==False:
            raise ConnectionAbortedError(Comp.dc['ERR_NOT_CALLED_SIMP_FUN'])
        if not isinstance(num, int):
            raise ValueError(Comp.dc["ERR_NOT_INT_NUM"])
        str_num = str(num)
        if len(str_num) == 1:
            return True
        if len(str_num) == 2:
            return str_num[0] == str_num[1]
        else:
            return str_num[0] == str_num[-1] and Comp.ispal(int(str_num[1:-1]))