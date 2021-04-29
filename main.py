# fibonacci sequence calculator
def fib(num):  # Calculates fibonacci number for 1 term
    if num <= 1:
        return num
    else:
        return fib(num-1) + fib(num-2)


while True:  # while loop allows user to retry input if invalid value obtained
    try:
        no_of_terms = int(input("Number of fibonacci terms desired: "))
        if no_of_terms < 0:
            print("Must be a positive integer. Retry")
            print("")
            continue
    except ValueError:
        print("Not an Integer. Retry")
        print("")
        continue
    break
print("")
print("Fibonacci sequence for {} terms:".format(no_of_terms))
for x in range(no_of_terms):
    print(fib(x), end="    ")  # prints each fibonacci terms for number of terms stipulated, creating a sequence
