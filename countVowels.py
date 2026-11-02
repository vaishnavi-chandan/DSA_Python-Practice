def count_vowels(n):
    count = 0
    for char in n.lower():
        if char in 'aeiou':
            count = count+1
    return count
print(count_vowels("aeiou"))
