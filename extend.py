
def main():
    list1 = [1,2,3,4,5,]
    list2 = [5,6,7,8,9]

    list1.extend(list2)
    print(list1)

    list3 = [-1,-2,3]
    list1.extend(list3)
    list2.append(list3)

    print(list1)
    print(list2)

    list4 = list1 + list2

    print(list4)


if __name__ == '__main__':
    main()