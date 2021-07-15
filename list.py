def main():
    # my_list = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_list.append(i ** 2)
    
    my_list = [i**2 for i in range(1, 10) if i % 3 != 0]
    list2 = [i for i in range(1, 99999) if i % 36 == 0]
    list1 = [1, 4, 5, 6, 9, 13, 19, 21]
    list3 = [i for i in list1 if i % 2 != 0 ]
    odd = list(filter(lambda x: x%2 != 0, list1))
    b = [2, 2, 2, 2, 2]
    add = [i**i for i in b]
    print(odd)
    print(list3)
    print(add)

                    

if __name__ == '__main__':
    main()