class Comp:
    flag=False
    def sumofdigits(num):
        if Comp.flag==False:
            raise Exception("Not called function from Simp")
        sum = 0
        while num != 0:
            sum += num % 10
            num = num // 10

    def ispal(num):
        if Comp.flag==False:
            raise Exception("Not called function from Simp")
        str_num = str(num)
        if len(str_num) == 1:
            return True
        if len(str_num) == 2:
            return str_num[0] == str_num[1]
        else:
            return str_num[0] == str_num[-1] and Comp.ispal(num[1:-2])