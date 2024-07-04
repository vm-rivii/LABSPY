#CH 7 Get Acronyms 
def get_acro(text):
    acro = ''
    text = text.split() #split into words at whitespaces
    for word in text:
        if (word[0].isupper()): #check only index[0] for first letter of word
            acro += word[0]        #add word to string
            acro += '.'            #add '.' after the letter
    
    return acro
    

if __name__ == '__main__':
    phrase = input('Enter name or phrase: ')
    acronym = get_acro(phrase)
    print(acronym)
