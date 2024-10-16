#The authors' names are Margaret and Colleen

def too_long(message):
    if len(message) <= 140:
        return "Your string is ok to be sent in a single SMS message"
    else:
        return "Your string is too long to be sent in a single SMS message"

    

def letter_numbers(word):
    total = 0
    for x in word:
        if x == "o":
            total = total + 1
    print(total)




def first_check(word):
    if word[0] == 'k':
        return True
    else:
        return False
