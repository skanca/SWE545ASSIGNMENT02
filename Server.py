from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import random
gaming = False
seed = 0

def sum(number1, number2):
    if gaming:
        return '0910: Can not run during a game'
    result = number1 + number2
    return '0210' + result

def product(number1, number2):
    if gaming:
        return '0910: Can not run during a game'
    result = number1 * number2
    return '0210' + result

def random():
    if gaming:
        return '0910: Can not run during a game'
    return random.sample(xrange(0,101),2)

def guess(number):
    if not gaming:
        return '0999: Game has not been started'
    if number > seed:
        return '0510: The Guess is too high'
    elif number < seed:
        return '0610: The Guess is too low'
    else:
        return '0410: The Guess is correct'

def check ():
    if gaming:
        return '0120' + 01
    else:
        return '0120' + 99

def start():
    gaming = True
    seed = random.randint(0,100)
    return '0110: Game is started'

server = SimpleXMLRPCServer(('localhost', 8000), SimpleXMLRPCRequestHandler);
server.register_function(random, 'random')
server.register_function(sum, 'sum')
server.register_function(product, 'product')
server.register_function(start, 'start')
server.register_function(guess, 'guess')
server.register_function(check, 'check')

server.serve_forever()