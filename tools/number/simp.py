import numbers

import MyFunctions
from tools.number.comp import Comp


class Simp:
    dc = MyFunctions.get_vars()
    def add(a, b):
        """
        Name: Roman Gleyberzon
        Date: 01/02/2023
        Description: This method calculates sum of given numbers
        Input: a,b
        Output: a+b
        """
        if not ((isinstance(a,int) or isinstance(a,float)) and (isinstance(b,int) or isinstance(b,float))):
            raise ValueError(Simp.dc["ERR_NOT_NUM"])
        Comp.flag = True
        return a + b

    def sub(a, b):
        """
        Name: Roman Gleyberzon
        Date: 01/02/2023
        Description: This method calculates differ of given numbers
        Input: a,b
        Output: a-b
        """
        if not ((isinstance(a,int) or isinstance(a,float)) and (isinstance(b,int) or isinstance(b,float))):
            raise ValueError(Simp.dc["ERR_NOT_NUM"])
        Comp.flag = True
        return a - b