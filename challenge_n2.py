"""
- [name] divisord
- [summary] The function calculates all of [num] divisors, using list comprehesions.    
"""
def divisors(num):
    try:
        if num <= 0:
            raise ValueError("Don't enter negatives numbers")
        divisors = [ i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        return ve
        
            


def main():
    number = int(input("Enter a number: "))
    print(divisors(number))


if __name__ == '__main__':
    main()