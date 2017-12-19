def anti_vowel(text):
  result = ""
  for index, char in enumerate(text):
    if char not in "aeiouAEIOU":
      result += char
  return result

n = anti_vowel("Hello Ther")
print (n)
