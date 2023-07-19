import unittest
# 1. Write a Python unit test program to check if a given number is prime or not.
def is_prime(n):
    if n < 2: 
        return False
    else :
        for a in range(2,n-1,1):
            if (n % a ) == 0:
                return False
    return True
class PrimeNumberTestCase(unittest.TestCase):
    def test_prime_numbers(self):
        prime_numbers = [2,3,5,7,11,13,17,19,23,29,31]
        print("Prime Numbers :", prime_numbers)
        for number in prime_numbers:
            self.assertTrue(is_prime(number),f"{number} is not recognized as a prime number")

    def test_non_prime_numbers(self):
        non_prime_numbers = [1,4,6,8,9,10,12,14,15,16,18,20,21,22]
        print("Non Prime Numbers : ",non_prime_numbers)
        for number in non_prime_numbers:
            self.assertFalse(is_prime(number),f"{number} is recognized as a prime number")
if __name__ == "__main__":
    unittest.main()
