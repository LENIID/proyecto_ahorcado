def run():
    
    # dic_natural = {}

    # for i in range (1, 101):
    #     if i % 3 != 0:
    #      dic_natural[i] = i**3

    # print(dic_natural)

    dic_natural = {i: pow(i, 0.5) for i in range (1, 1001)}

    print(dic_natural)




if __name__ == "__main__":
    run()