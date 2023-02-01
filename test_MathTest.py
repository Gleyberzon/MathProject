import MyFunctions
from tools.number.simp import *
from tools.col import *
import os
import pytest


dc = MyFunctions.get_vars("test.env")
path = dc["PATH_TEST_LOG"]

# Test sum with correct parametres
def test_sum_1():
    try:
        a = dc["PAR_A"]
        b = dc["PAR_B"]
        expected_sum = dc["EXP_SUM_A_B"]
        testName = "test_sum_1"
        testDescription = "Checking sum with correct numbers"
        parametres = f"A: {a}, B: {b}"
        expected = f"Sum = {expected_sum}"
        actual_sum = Simp.add(a,b)
        actual = f"Sum = {actual_sum}"
        assert actual_sum == expected_sum
        LogTest(path, testName, testDescription, parametres, expected, actual, True)
    except Exception as e:
        actual="Error"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
        assert False


# Test sum with incorrect parametres
def test_sum_2():
    try:
        a = dc["PAR_A"]
        b = dc["PAR_WRONG"]
        testName = "test_sum_2"
        testDescription = "Checking sum with incorrect numbers"
        parametres = f"A: {a}, B: {b}"
        expected = f"Raised Value Error"
        actual_sum = Simp.add(a, b)
        actual=f"Sum = {actual_sum}"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
        assert False
    except ValueError as e:
        actual = expected
        LogTest(path, testName, testDescription, parametres, expected, actual, True)
        assert True


# Test substraction with correct parametres
def test_sub_1():
    try:
        a = dc["PAR_A"]
        b = dc["PAR_B"]
        expected_sub = dc["EXP_SUB_A_B"]
        testName = "test_sub_1"
        testDescription = "Checking substruction with correct numbers"
        parametres = f"A: {a}, B: {b}"
        expected = f"A - B = {expected_sub}"
        actual_sub = Simp.sub(a,b)
        actual = f"A - B = {actual_sub}"
        assert actual_sub == expected_sub
        LogTest(path, testName, testDescription, parametres, expected, actual, True)
    except Exception as e:
        actual="Error"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
        assert False


# Test substraction with incorrect parametres
def test_sub_2():
    try:
        a = dc["PAR_A"]
        b = dc["PAR_WRONG"]
        testName = "test_sub_2"
        testDescription = "Checking substruction with correct numbers"
        parametres = f"A: {a}, B: {b}"
        expected = f"Raised Value Error"
        actual_sub = Simp.sub(a, b)
        actual=f"Sub = {actual_sub}"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
        assert False
    except ValueError as e:
        actual = expected
        LogTest(path, testName, testDescription, parametres, expected, actual, True)
        assert True


# Test polindrome with polindrome number
def test_polindrome_1():
    try:
        num = dc["PAR_NUM_POL"]
        expected_result = True
        testName = "test_polindrome_1"
        testDescription = "Checking is num is polindrome"
        parametres = f"Num: {num}"
        expected = f"Result = {expected_result}"
        Comp.flag=True
        actual_result = Comp.ispal(num)
        actual = f"Result = {actual_result}"
        assert expected_result == actual_result
        LogTest(path, testName, testDescription, parametres, expected, actual, True)
    except Exception as e:
        actual="Error"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
        assert False


# Test polindrome with polindrome number having only 1 digit
def test_polindrome_2():
    try:
        num = dc["PAR_NUM_POL_2"]
        expected_result = True
        testName = "test_polindrome_2"
        testDescription = "Checking is num is polindrome"
        parametres = f"Num: {num}"
        expected = f"Result = {expected_result}"
        Comp.flag=True
        actual_result = Comp.ispal(num)
        actual = f"Result = {actual_result}"
        assert expected_result == actual_result
        LogTest(path, testName, testDescription, parametres, expected, actual, True)
    except Exception as e:
        actual="Error"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
        assert False


# Test polindrome with not polindrome number
def test_polindrome_3():
    try:
        num = dc["PAR_NUM_NOT_POL"]
        expected_result = False
        testName = "test_polindrome_3"
        testDescription = "Checking is num is polindrome"
        parametres = f"Num: {num}"
        expected = f"Result = {expected_result}"
        Comp.flag=True
        actual_result = Comp.ispal(num)
        actual = f"Result = {actual_result}"
        assert expected_result == actual_result
        LogTest(path, testName, testDescription, parametres, expected, actual, True)
    except Exception as e:
        actual="Error"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
        assert False


# Test polindrome with not number
def test_polindrome_4():
    try:
        num = dc["PAR_WRONG"]
        testName = "test_polindrome_4"
        testDescription = "Checking is num is polindrome"
        parametres = f"Num: {num}"
        expected = f"Raised Value Error"
        Comp.flag=True
        actual_result = Comp.ispal(num)
        actual = f"Result = {actual_result}"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
        assert False
    except ValueError as e:
        actual=expected
        LogTest(path, testName, testDescription, parametres, expected, actual, True)
        assert True


# Test sum of digits with correct number
def test_sum_digits_1():
    try:
        num = dc["PAR_SOME_INT_NUM"]
        expected_sum = dc["EXP_SUM_OF_DIGITS"]
        testName = "test_sum_digits_1"
        testDescription = "Checking digit's sum of correct integer number"
        parametres = f"Num: {num}"
        expected = f"Sum = {expected_sum}"
        Comp.flag=True
        actual_sum = Comp.sumofdigits(num)
        actual = f"Sum = {actual_sum}"
        assert actual_sum == expected_sum
        LogTest(path, testName, testDescription, parametres, expected, actual, True)
    except Exception as e:
        actual="Error"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
        assert False


# Test sum of digits with incorrect number
def test_sum_digits_2():
    try:
        num = dc["PAR_WRONG"]
        testName = "test_sum_digits_2"
        testDescription = "Checking digit's sum of incorrect parameter"
        parametres = f"Num: {num}"
        expected = f"Raised Value Error"
        Comp.flag=True
        actual_sum = Comp.sumofdigits(num)
        actual = f"Sum = {actual_sum}"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
        assert False
    except ValueError as e:
        actual=expected
        LogTest(path, testName, testDescription, parametres, expected, actual, True)
        assert True


# Check acsess to functions of Comp with previously calling function in Simp
def test_script_1():
    try:
        num = dc["PAR_SOME_INT_NUM"]
        a = dc["PAR_A"]
        b = dc["PAR_B"]
        testName = "test_script_1"
        testDescription = "Run function SUM from Simp, and after run function SUMOFDIGITS from Comp"
        parametres = f"Num: {num}, a: {a}, b: {b}"
        expected = f"Not raised error"
        Comp.flag = False
        Simp.add(a,b)
        Comp.sumofdigits(num)
        actual = expected
        assert True
        LogTest(path, testName, testDescription, parametres, expected, actual, True)
    except Exception as e:
        actual = "Raised error"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
        assert False


# Check acsess to functions of Comp without calling function in Simp
def test_script_2():
    try:
        num = dc["PAR_SOME_INT_NUM"]
        a = dc["PAR_A"]
        b = dc["PAR_B"]
        testName = "test_script_2"
        testDescription = "Run function SUMOFDIGITS from Comp, and after run function SUM from Simp"
        parametres = f"Num: {num}, a: {a}, b: {b}"
        expected = f"Raised error"
        Comp.flag=False
        Comp.sumofdigits(num)
        Simp.add(a, b)
        actual = "Not raised error"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
        assert False
    except ConnectionAbortedError as e:
        actual = expected
        LogTest(path, testName, testDescription, parametres, expected, actual, True)
        assert True

@pytest.mark.zip
# Check myzip function with correct path
def test_myzip_1():
    try:
        folder1 = dc["PATH_FOLDER_1"]
        folder2 = dc["PATH_FOLDER_2"]
        testName = "test_myzip_1"
        testDescription = "Trying to create zip file from given folders"
        parametres = f"Path to folder 1: {folder1}\t, path to folder 2: {folder2}"
        expected = f"Created zip file: {dc['PATH_ZIP_FILE']}"
        Zip.myzip(folder1,folder2)
        if os.path.exists(dc["PATH_ZIP_FILE"]):
            actual = expected
            assert True
            LogTest(path, testName, testDescription, parametres, expected, actual, True)
        else:
            assert False
    except AssertionError:
        actual="Zip file was not created"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
    except Exception as e:
        actual=f"Happend error during procedure: {e}"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
        assert False


# Check myzip function with incorrect path
def test_myzip_2():
    try:
        folder1 = dc["PATH_FOLDER_1"]
        folder2 = dc["PATH_WRONG"]
        testName = "test_myzip_2"
        testDescription = "Trying to create zip file from given folders"
        parametres = f"Path to folder 1: {folder1}\t, path to folder 2: {folder2}"
        expected = f"Raised FileExistError"
        Zip.myzip(folder1,folder2)
        if os.path.exists(dc["PATH_ZIP_FILE"]):
            actual = f"Created zip file: {dc['PATH_ZIP_FILE']}"
            raise AssertionError
    except FileExistsError:
        actual=expected
        LogTest(path, testName, testDescription, parametres, expected, actual, True)
        assert True
    except AssertionError:
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
    except Exception as e:
        actual=f"Raised other exception: {e}"
        LogTest(path, testName, testDescription, parametres, expected, actual, False)
