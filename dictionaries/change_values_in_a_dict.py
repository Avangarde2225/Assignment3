def have_birth(dict, name):
    print("You are one year older, "+ name + "!")
    dict[name] +=1



def main():
    ages={'Chris':33, "Julia": 22, "Mehran": 55}
    print(ages)
    have_birth(ages,'Chris')
    print(ages)
    have_birth(ages,'Mehran')
    print(ages)


    for key in ages.keys():
        print(str(key) + "-> " + str(ages[key]))

    for key in ages:
        print(key + "-> " + str(ages[key]))

    for value in ages.values():
        print(value)

#removing elements
    ages.pop('Chris')
    print(ages)

    ages.clear()
    print(ages)






if __name__ == '__main__':
    main()