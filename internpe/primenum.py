class PrimeChecker:
    def __init__(self, number):
        self.number = number

    def is_prime(self):
        if self.number <= 1:
            return False
        elif self.number <= 3:
            return True
        elif self.number % 2 == 0 or self.number % 3 == 0:
            return False
        i = 5
        while i * i <= self.number:
            if self.number % i == 0 or self.number % (i + 2) == 0:
                return False
            i += 6
        return True

# Test the class
num = int(input("Enter a number: "))
checker = PrimeChecker(num)
if checker.is_prime():
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
