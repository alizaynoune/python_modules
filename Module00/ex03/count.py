from collections import Counter
import sys


def text_analyzer(text=None):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text
    '''
    pass
    if not text:
        text = input("What is the text to analyze?\n")
    if text.isnumeric():
        sys.exit('AssertionError: argument is not a string')
    textInfo = Counter(
                                    "lower" if c.islower() else
                                    "upper" if c.isupper() else
                                    "space" if c.isspace() else
                                    "punctuation" if not c.isdigit() else
                                    'other' for c in text)

    print("The text contains %d character(s):" % len(text))
    print("- {upper} upper letter(s)\n- {lower} lower letter(s)\
    ".format(upper=textInfo['upper'], lower=textInfo['lower'],))
    print("- {punctuation} punctuation mark(s)\n- {space} space(s)\
    ".format(punctuation=textInfo['punctuation'], space=textInfo['space']))


if __name__ == "__main__":
    if (len(sys.argv) == 1):
        text_analyzer()
    elif (len(sys.argv) == 2):
        text_analyzer(sys.argv[1])
    else:
        sys.exit('AssertionError: more than one argument are provided')
