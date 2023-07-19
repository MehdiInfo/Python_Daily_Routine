import numpy as np
# 1. Write a Numpy program to get the Numpy version and show the Numpy build configuration.
def exo1():
    print(np.__doc__)
    print(np.__version__)
    print(np.show_config())

# 2. Write a NumPy program to get help with the add function.
def exo2():
    print(np.info(np.add))

# 3. Write a NumPy program to test whether none of the elements of a given array are zero. 
def exo3():
    # np.all test if all array elements are true or != 0
    print(np.info(np.all))
    arr = np.array([1,2,3,4,5])
    arr2 = np.array([0,1,2,3,4])
    if(np.all(arr)):
        print("Arr is zeroless")
    else:
        print("Arr has zero")
    if(np.all(arr2)):
        print("Arr is zeroless")
    else:
        print("Arr has zero")

# 4. Write a NumPy program to test if any of the elements of a given array are non-zero. 
def exo4():
    # np.count_nonzero count non zero values can use np.any as well opposit of all
    arr = np.zeros(5, dtype = "uint8")
    arr2 = np.append(arr, 1)
    print(np.nonzero(arr))
    print(arr2)
    if(np.count_nonzero(arr) > 0):
        print("There is a nonzero elment")
    else:
        print("There are only zeros")
    if(np.count_nonzero(arr2) > 0):
        print("There is a nonzero elment")
    else:
        print("There are only zeros")
# 5. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a number).
def exo5():
    a = np.array([1,2,np.nan,np.inf])
    print(a)
    print("Test a given array element-wise for finiteness")
    print(np.isfinite(a))
# 6. Write a NumPy program to test elements-wise for positive or negative infinity. 
def exo6():
    a = np.array([1,2,np.NINF,np.Inf])
    print(a)
    print("Test negative infinity")
    print(np.isneginf(a))
    print("Test positive infinity")
    print(np.isposinf(a))
# 7. Write a NumPy program to test element-wise for NaN of a given array.
def exo7():
    a = np.array([1,2,np.nan,np.nan])
    print(a)
    print("Test Nan element")
    print(np.isnan(a))
# 8. Write a NumPy program to test element-wise for complex numbers, real numbers in a given array. Also test if a given number is of a scalar type or not. 
def exo8():
    a = np.array([1+1j,1+2j,3.5,2,1+0j])
    print(a)
    print("Test complex numbers")
    print(np.iscomplex(a))
    print("Test real numbers")
    print(np.isreal(a))
    print("Test scalar type")
    print(np.isscalar(a))
    print(np.isscalar(3))
    print(np.isscalar([1]))
if __name__ == "__main__":
    exo8()
# https://www.w3resource.com/python-exercises/numpy/basic/index.php
# https://www.w3resource.com/python-exercises/numpy/index.php