#Return the number (count) of vowels in the given string.

#We will consider a, e, i, o, u as vowels for this Kata (but not y).

#The input string will only consist of lower case letters and/or spaces.

def get_count(input_str):
    num_vowels = 0
    vowels = ["a","e","i","o","u"]
    # your code here
    for i in range(0,len(input_str)):
        if input_str[i] in vowels:
            num_vowels += 1
    
    return num_vowels
