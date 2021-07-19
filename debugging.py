    
"""
- [name] divisors
- [summary] The function calculates all of [num] divisors.
- [param] num, type: int
"""
def divisors(num):
    divisors = [ i for i in range(1, num + 1) if num % i == 0]
    return divisors
    
def main():
    try:
        num = int(input('Enter a number: '))        
        print(divisors(num))     
        print("solo enteros") 
        print("The program finish")
    except ValueError:
        
        print("You have to enter a number")
if __name__ == '__main__':
    main()