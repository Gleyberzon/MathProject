from tools.number.comp import Comp


class Simp:
    def add(a, b):
        Comp.flag = True
        return a + b

    def sub(a, b):
        Comp.flag = True
        return a - b