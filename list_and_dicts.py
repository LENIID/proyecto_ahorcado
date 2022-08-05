def run():
    my_list = [1, "Helo", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "Garcia"}


    super_list = [
        {"firstname": "Facundo", "lastname": "Garcia"},
        {"firstname": "Jose", "lastname": "Garcia"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Susana", "lastname": "Martines"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
    ]

    super_dic = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }


    for value in super_list:
        print( value)

    # for values in super_list:
    #     for key, value in values.items():
    #         print(f'{key} - {value}')

     

if __name__ == "__main__":
    run()