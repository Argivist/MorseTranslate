from morsedictionary import morse as Morse
from morsedictionary import morse_code_dict as MorseCode_

text = str.upper(input("enter value"))


def convertor(textVal):
    space = False
    morseValue = ""
    for i in textVal:
        if i != " " and space == False:
            morseValue = morseValue + " "
        else:
            space = False
        if i == " ":
            space = True
        morseValue = morseValue + Morse.get(i)

    return morseValue

def reverter(morseVal):
    space = False
    textVal = ""
    for i in morseVal.split(" "):
        print(i)
        if i != " " and space == False:
            textVal = textVal + " "
        else:
            space = False
        if i == " ":
            space = True
        textVal = textVal + str(MorseCode_.get(i))

    return textVal


def light(text):
    morse = convertor(text)
    for i in morse:
        if i == ".":
            '''  #on for 1 ratio
            #of for 1 ratio'''
        elif i == "-":
            '''#on for 3 ratio
            #off for 1 ratio'''
        elif i == " ":
            '''#off for 3 ratio'''
        elif i == "/":
            '''#off for 7 ratio'''
        else:
            '''#blink 5 dots for error'''
            break


def sound(text):
    morse = convertor(text)
    for i in morse:
        if i == ".":
            ''' #beep for 1 ratio'''

        elif i == "-":
            '''  #beep for 3 ratio'''

        elif i == " ":
            '''#off for 3 ratio'''
        elif i == "/":
            ''' #off for 7 ratio'''
        else:
            '''#dot 5 dots for error'''
            break


print(convertor(text))
print(reverter(convertor(text)))
