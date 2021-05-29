def main():
    alist = [12,3,4,5,6]

    for i in range(len(alist)):
        alist[i] +=1
    print(alist)

    for elem in alist:
        elem +=1
    print(elem)

if __name__ == '__main__':
    main()