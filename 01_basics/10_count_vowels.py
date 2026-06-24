# def count_vowels(sentence):
#     vowels = 'aeiouAEIOU'
#     count = 0
#     for char in sentence:
#         if char in vowels:
#             count += 1
#     return count
  
# sentence = input("Enter a sentence: ")
# vowel_count = count_vowels(sentence)
# print(f"The number of vowels in the sentence is: {vowel_count}")

# Option: 2
text = input("Enter a text: ")
vowel_count = sum(1 for char in text if char in 'aeiouAEIOU')
print(f"The number of vowels in the text is: {vowel_count}")
