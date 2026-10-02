


def countvowcons(userinput):
    vowel = "aeiouAEIOU"

    countvowel = 0
    countconsonant = 0

    for each in userinput:
        if(each.isalpha()):
            if(each in vowel):
                countvowel = countvowel+1
            else:
                countconsonant = countconsonant+1
    return countconsonant,countvowel

vowel ,consonant =countvowcons("Ahmad Raza")

print(vowel,"\n",consonant)