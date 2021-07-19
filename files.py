"""
- [name] spaces
- [summary] The program creates spaces between names.
- [param] a, type: list.
- [param] f, type: file.
"""
def spaces(a, f):
    for i  in a:
        f.write(i)
        f.write("\n")
        

"""
- [name] read
- [summary] The fuction reads a file and gets file's lines. 
"""
def read():
    
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        numbers = [int(line) for line in f]
        # for line in f:
        #     numbers.append(int(line))
    print(numbers)

"""
- [name] write
- [summary] The function writes in the last line of the file.
"""
def write():
    names = ["Diego", "Geremy", "Jorge", "Adrian"]
    with open("./files/names.txt", "a", encoding="utf-8") as f:
        spaces(names, f)



def main():
    write()


if __name__ == '__main__':
    main()
    