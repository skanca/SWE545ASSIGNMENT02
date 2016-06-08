import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:8000')

# Print Writer
def list_functions():
    return 'RND - Generates list of two random ints: RND \n' \
           'SUM - Sums two ints: SUM Number1 Number2 \n' \
           'PRD - Products two ints: PRD Number1 Number2 \n' \
           'GMN - Starts guessing game \n' \
           'EXT - Exits the client '


def list_gaming():
    return 'GSS - Guess a number: GSS Number \n' \
           'EXT - Exits the game '

def parse_input(input):
    parsed_text = input.split()
    command = parsed_text[0]
    parameters = []
    if len(parsed_text) > 1:
        for index in range (1, len(parsed_text)):
            parameters.append(parsed_text[index])
    return command, parameters


def parse_output(output):
    parsed_text = output.split()
    outcommand = parsed_text[0]
    parameters = []
    if len(parsed_text) > 1:
        for index in range(1, len(parsed_text)):
            parameters.append(parsed_text[index])
    if outcommand == '0110':
        print 'Game is started'
    if outcommand == '0120':
        if parameters[1] == '01':
            gaming = True
        else:
            gaming = False
    if outcommand == '0210':
        print 'Result is ' + parameters[1]
    elif outcommand == '0410':
        print 'The guess is correct'
    elif outcommand == '0510':
        print 'The guess is too high'
    elif outcommand == '0610':
        print 'The guess is too low'
    elif outcommand == '0910':
        print 'Can not run during a game'
    elif outcommand == '0999':
        print 'Game has not been started'
    else:
        print 'Undefined response'


response = ''
running = True;
gaming = False;

while True:
    parse_output(server.check())
    if gaming:
        print list_gaming();
    else:
        print list_functions();

    input = raw_input("Please Enter a Command")
    command, parameters = parse_input(input)
    if command == 'EXT':
        if not gaming:
            running = False;
        gaming = False
    elif command == 'GSS':
        number01 = int(parameters[0])
        parse_output(server.guess(number01))
    elif command == 'RND':
        parse_output(server.random())
    elif command == 'SUM':
        number01 = int(parameters[0])
        number02 = int(parameters[1])
        parse_output(server.sum(number01,number02))
    elif command == 'PRD':
        number01 = int(parameters[0])
        number02 = int(parameters[1])
        parse_output(server.product(number01,number02))
    elif command == 'GMN':
        gaming = True
        parse_output(server.start())
    else:
        print 'Invalid Input Command';


