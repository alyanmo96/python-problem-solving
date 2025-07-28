def reverse_words(s):
    #convert_to_list = s.split(' ') # A list of strings
    #reversed_list = convert_to_list[::-1] #  Reverses the order of words in a given sentence.
    #revesed_text = " ".join(reversed_list) #A new string with the order of words reversed, while preserving the original words.

    return " ".join(s.split(' ')[::-1])

print(reverse_words('The greatest victory is that which requires no battle'))
#Output: battle no requires which that is victory greatest The