def run():
    
    # squares = []

    # for i in range (1, 101):
    #     if i % 3 != 0:
    #      squares.append(i**2)
    
    # squares = [i for i in range (1, 100000) if i % 36 == 0]
    
    my_list = [1, 2, 3, 4, 5]
    
    # squares = [i**2 for i in range (1, 6)]
    squares = [i**2 for i in my_list]

    



    print(squares)


if __name__ == "__main__":
    run()