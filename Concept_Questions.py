def is_isogram(word):
    counts = {}
    for letter in word:
        lower_letter = letter.lower()
        if lower_letter in counts:
            return False
        else:
            counts[lower_letter] = 1
    return True

# testing out
print(is_isogram("hello"))