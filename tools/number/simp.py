import numbers

from MyFunctions import *
from tools.number.comp import Comp


class Simp:
    dc = get_vars()

    # Calculates sum of numbers
    def add(a, b):
        """
        Name: Roman Gleyberzon
        Date: 01/02/2023
        Description: This method calculates sum of given numbers
        Input: a,b
        Output: a+b
        """
        Log(Simp.dc["PATH_LOG"], Simp.dc["LOG_MESS_CALLED"].format("add"))
        if not ((isinstance(a,int) or isinstance(a,float)) and (isinstance(b,int) or isinstance(b,float))):
            Log(Simp.dc["PATH_LOG"], Simp.dc["ERR_NOT_NUM"].format(a,b))
            raise ValueError(Simp.dc["ERR_NOT_NUM"].format(a,b))
        Comp.flag = True
        result = a+b
        Log(Simp.dc["PATH_LOG"], Simp.dc["LOG_MESS_SUM"].format(a,b,result))
        return result


    # Calculates substraction of numbers
    def sub(a, b):
        """
        Name: Roman Gleyberzon
        Date: 01/02/2023
        Description: This method calculates differ of given numbers
        Input: a,b
        Output: a-b
        """
        Log(Simp.dc["PATH_LOG"], Simp.dc["LOG_MESS_CALLED"].format("sub"))
        if not ((isinstance(a,int) or isinstance(a,float)) and (isinstance(b,int) or isinstance(b,float))):
            Log(Simp.dc["PATH_LOG"], Simp.dc["ERR_NOT_NUM"].format(a,b))
            raise ValueError(Simp.dc["ERR_NOT_NUM"].format(a,b))
        Comp.flag = True
        result = a-b
        Log(Simp.dc["PATH_LOG"], "Calculated subtraction: {}-{}={}".format(a,b,result))
        return result