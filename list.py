def main():
    # my_list = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_list.append(i ** 2)
    
    my_list = [i**2 for i in range(1, 10) if i % 3 != 0]
    list = [i for i in range(1, 99999) if i % 36 == 0]
            
                    
    print(list)

if __name__ == '__main__':
    main()