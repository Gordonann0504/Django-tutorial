from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    result = ""
    # Do fizzbuzz
    # defonition of the variables
    for number in range(1,21,1):
    # creating a while loop
        if number % 5 == 0 and number % 3 == 0:
            # this make sure when something is devided by 3 and 5 there is no remader
            result += ('FizzBuzz <br />')
        elif number % 3 == 0:
            result += ('Fizz <br />')
            # this make sure when something is devided by 3 there is no remader
        elif number % 5 == 0:
            # this make sure when something is devided by 5 there is no remader
            result += ('Buzz <br />')
        else:
            # prints the number even if is doesn't dived by 3 or 5
            result += (str(number) + '<br />')
    return HttpResponse(result)