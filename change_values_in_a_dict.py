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







if __name__ == '__main__':
    main()