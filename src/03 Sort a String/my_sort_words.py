def sort_words(text):
  result = sorted(text.split(), key=str.casefold)

  return result

text = input("Enter text: ")
print(sort_words(text))