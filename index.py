import argparse
import random


parser = argparse.ArgumentParser(description='Generate a random password')
parser.add_argument('-l', '--lenght', action='store', type=int, default=10,
                    help='lenght of the password (default:10)')
parser.add_argument('-s', '--special_char', action='store', type=bool, default=False,
                    help='activates special characthers')
parser.add_argument('-n', '--numbers', action='store', type=bool, default=False,
                    help='activates numbers')
args = parser.parse_args()


# define possible values for password
_letters =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
_special_char = ['/','#','(',')','-','_','%','+']
_numbers = ['0','1','2','3','4','5','6','7','8','9']

# constructing possible values

# by default _letters
possible_values = _letters

# if special_char
if args.special_char:
    possible_values = possible_values + _special_char
# if numbers
if args.numbers:
    possible_values = possible_values + _numbers

# generating the password
password = []
for i in range(0, args.lenght):
    password.append(possible_values[random.randint(0, len(possible_values) -1 )])

print("Generated password \"{}\"".format(''.join(password)))