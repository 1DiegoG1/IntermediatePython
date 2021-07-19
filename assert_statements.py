"""
- [name] program_finish
- [summary] Display a finish program message.
- [return] "Program finish" message.
"""
def program_finish():
    return print("Progran Finish")
    
"""
- [name] divisors.
- [summary] calculates num's divisors.
- [param] num, a integer number.
- [return] num's divisors
"""
def divisors():
    num = int(input('Enter a number: '))
    assert int(num) > 0, "You can't enter negative numbers"
    divisors = [ i for i in range(1, num + 1) if num % i == 0]
    return print(divisors)
  
    
def main():
    divisors()        
    program_finish()
    
if __name__ == '__main__':
    main()