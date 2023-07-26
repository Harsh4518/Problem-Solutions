word="FlaG"

if word.isupper() or word.islower():

    print("True")

if word[0].isupper():

    if word[1:].islower():

        print("True")

    else:

        print("False")
