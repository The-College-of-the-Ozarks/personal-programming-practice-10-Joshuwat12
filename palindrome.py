# palindrome.py


# Function
def isPalindrome(string):
  if len(string) < 2:
    return True
  elif string[0] == string[-1]:
    return isPalindrome(string[1:-1])
  return False


# Main program
string = input("Enter a string: ")
if isPalindrome(string):
  print(string, "is a palindrome.")
else:
  print(string, "is not a palindrome.")