"""intaClone views."""


#Django
from django.http import HttpResponse


#Utilities
from datetime import datetime
import json


def hello_world(request):
    """Returns a greeting."""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(
        'Oh, hi! Current server time is {now}'.format(now))


def sort_integers(request):
    """Returns a JSON response with sorted integers."""
    numbers = [
        int(i) for i in request.GET['numbers'].split(',')
        ]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully'
    }
    return HttpResponse(
        json.dumps(data, indent = 4),
        content_type = 'application/json'
    )


def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, yo are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to instClone'.format(name)
    return HttpResponse(message)