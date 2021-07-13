def main():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Diego", "secondname": "González"}
    
    super_list = [
        {"firstname": "Geremy",
        "secondname": "Caicedo"},
        {"firstname": "Diego",
        "secondname": "Torrez"},
        {"firstname": "Jorge",
        "secondname": "Aguiar"},
        {"firstname": "Said",
        "secondname": "Vargas"}
    ]

    super_dict = {
        "natural_numbs": [1,2,3,4,5],
        "integer_numbs": [-1, -2, 0, 1 ,2],
        "floating_numbs": [1.1, 4.6, 6.46]
    }
    
    for i, b in super_dict.items():
        print(f'{i} -> {b}')
    print('-'*40)
        
    
    for i in super_list:
        for key, value in i.items():
            print(f'{key}: {value}')
            
        print('', sep='\n')
if __name__ ==  '__main__':
    main()