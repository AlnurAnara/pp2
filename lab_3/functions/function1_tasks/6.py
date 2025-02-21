def reverse_string():
    string = input()
    words = string.split()  # Split the sentence into words
    reverse = ' '.join(words[::-1])  # Reverse the words and join them back into a sentence
    return reverse

# Call the function to get the reversed sentence
print(reverse_string())


'''
Write a function that accepts string from user, return a sentence with the words reversed. 
We are ready -> ready are We

'''

