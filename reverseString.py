# def rev_string(text):
#     return text[::-1]
# print(rev_string("RedBull"))

#  Palindrome
# def palindrome(text):
#     # if text == text[::-1]:
#     #     print("Its Palindrome.")
#     # else:
#     #     print("Not a Palindrome.")
#     return text.lower() == text[::-1].lower()
# print(palindrome("Madam"))

text = "Welcome to Python"
print(text[::-1]) # reverse characters
words = text.split()
print(" ".join(words[::-1]))