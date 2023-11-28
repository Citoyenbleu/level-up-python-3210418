def is_palindrome(text):
  letters = list(text.lower())

  checked_letters = []
  for char in letters:
    if char.isalpha():
      checked_letters.append(char)
  
  forwards = "".join(checked_letters)
  reverse = "".join(checked_letters[::-1])
  
  if forwards == reverse:
     return True
  else:
    return False

  # return result.join(checked_letters)

print(is_palindrome("Levels"))
