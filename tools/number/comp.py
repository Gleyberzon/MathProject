from MyFunctions import *


class Comp:
    flag=False
    dc = get_vars()

    # Calculates sum of digits by + 'mod' 10
    def sumofdigits(num):
        """
        Name: Roman Gleyberzon
        Date: 01/02/2023
        Description: This method calculates sum of all digits of number
        Input: int number
        Output: sum
        """
        Log(Comp.dc["PATH_LOG"], Comp.dc["LOG_MESS_CALLED"].format("sumofdigits"))
        if Comp.flag==False:
            Log(Comp.dc["PATH_LOG"], Comp.dc["LOG_MESS_FLAG_ERR"].format("sumofdigits"))
            raise ConnectionAbortedError(Comp.dc['ERR_NOT_CALLED_SIMP_FUN'])
        if not isinstance(num, int):
            Log(Comp.dc["PATH_LOG"], Comp.dc["ERR_NOT_INT_NUM"].format(num))
            raise ValueError(Comp.dc["ERR_NOT_INT_NUM"].format(num))
        sum = 0
        copynum=num
        while num != 0:
            sum += num % 10
            num = num // 10
        Log(Comp.dc["PATH_LOG"], Comp.dc["LOG_MESS_SUM_DIGITS"].format(copynum, sum))
        return sum


    # Recursive exam of polindrome number
    def ispal(num):
        """
        Name: Roman Gleyberzon
        Date: 01/02/2023
        Description: This method check if the given number is polindrome
        Input: int number
        Output: isPolindrome True / False
        """
        Log(Comp.dc["PATH_LOG"], Comp.dc["LOG_MESS_CALLED"].format("ispal"))
        if Comp.flag==False:
            Log(Comp.dc["PATH_LOG"], Comp.dc["LOG_MESS_FLAG_ERR"].format("ispal"))
            raise ConnectionAbortedError(Comp.dc['ERR_NOT_CALLED_SIMP_FUN'])
        if not isinstance(num, int):
            Log(Comp.dc["PATH_LOG"], Comp.dc["ERR_NOT_INT_NUM"].format(num))
            raise ValueError(Comp.dc["ERR_NOT_INT_NUM"].format(num))
        str_num = str(num)
        if len(str_num) == 1:
            return True
        if len(str_num) == 2:
            return str_num[0] == str_num[1]
        else:
            return str_num[0] == str_num[-1] and Comp.ispal(int(str_num[1:-1]))