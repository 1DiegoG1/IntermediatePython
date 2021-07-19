"""
- [name] palindrome
- [summary] The function verify if a string is palindrome or not.
- [param] string, type: string.
"""
def palindrome(string):
    return string == string[::-1]
def main():
   try:
    print(palindrome(1))
   except TypeError:
       print("Only strings!")
    

if __name__ == '__main:__':
    main()