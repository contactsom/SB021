sentence="Python is easy and powerful and easy to learn. Python is easy to learn"

# 1. Find the word frequency
# KEY - WORD
# Value - frequency

words=sentence.lower().split() # List
print(words)
frequency={} # Empty Dictionary
for word in words: # From the List of words I am getting single words
    frequency[word]=frequency.get(word,0)+1
print(frequency)
