def search4vowels(word):
    '''Display and vowels found in an asked=for word.'''
    vowels = set('aeiou')
    #word = input("Provied a word to search for vowels : ")
# found = vowels.intersection(set(word))
 #   return bool(found)
    return vowels.intersection(set(word))


search4vowels('austin')