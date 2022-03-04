n = int(input('Start: '))
m = int(input('End: '))

if 1 <= n < m <= 10000:

    for number in range(n, m+1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
            continue
        elif number % 3 == 0:
            print("Fizz")
            continue
        elif number % 5 == 0:
            print("Buzz")
            continue
        print(number)
else:
    print("Input data should be between 1 and 10000")
