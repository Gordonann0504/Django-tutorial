
# defonition of the variables
for number in range(1,21,1):
   # creating a while loop
    if number % 5 == 0 and number % 3 == 0:
        # this make sure when something is devided by 3 and 5 there is no remader
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
        # this make sure when something is devided by 3 there is no remader
    elif number % 5 == 0:
        # this make sure when something is devided by 5 there is no remader
        print('Buzz')
    else:
        # prints the number even if is doesn't dived by 3 or 5
        print(number)