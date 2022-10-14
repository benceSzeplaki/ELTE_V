weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

try:
    weekdays[0] = 'NotMonday'
except TypeError:
    print("You cannot change an element of a tuple.")
finally:
    print("Finally...")

alphabet = 'abcdefghijklmnopqrstuvwxyz'
newAlphabet = ''

for char in alphabet:
    newAlphabet += char
    newAlphabet += char.upper()

print(newAlphabet)

newAlphabet = ''
for char in alphabet:
    newAlphabet += char
    newAlphabet += chr(ord(char)-32)

print(newAlphabet)


def to_ceaser_cipher(str):
    ret = ''
    for char in str:
        if char.isnumeric():
            ret += char
        else:
            if char.islower():
                if char == 'z':
                    ret += 'a'
                else:
                    ret += chr(ord(char) + 1)
            else:
                if char == 'Z':
                    ret += 'A'
                else:
                    ret += chr(ord(char) + 1)
    return ret

print(to_ceaser_cipher('abcD1Z'))