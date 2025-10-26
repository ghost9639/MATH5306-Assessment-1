
# Task 6: Is the number prime?
def IsItPrime(num):
    
    if num == 1:
        return False
    if num == 2:
        return True
    
    top = num - 1
    for val in range(2, top):
        if num % val == 0:
            return False
    return True


print(f"Is 2 prime? This is {IsItPrime(2)}!")
print(f"Is 3 prime? This is {IsItPrime(3)}!")
print(f"Is 51 prime? This is {IsItPrime(51)}!")
print(f"Is 39 prime? This is {IsItPrime(39)}!")
print(f"Is 17 prime? This is {IsItPrime(17)}!")

if IsItPrime(19):
    print("19 is prime!")
else:
    print("19 isn't prime??")

MyNumber = int(input("Please enter your own number for testing: "))
print(f"Is {MyNumber} prime? This is {IsItPrime(MyNumber)}!")


