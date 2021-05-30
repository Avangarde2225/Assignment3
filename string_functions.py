def main():
    s = 'So long and thanks for all the fish '

    #print(s.find('o'))

    print(s.replace("l", "m"))

    print(s.find('t'))

    #print(s.strip())


    reversed = ""
    for i in range(len(s)):
        ch = s[i]
        reversed = ch + reversed
    print(reversed)

    










if __name__ == '__main__':
    main()