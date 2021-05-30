def main():
    EXAMPLE = 'Kayak'
    SHORT = 'A man, a plan, a canal - Panama!'

    reversed = ""
    for i in range(len(EXAMPLE)):
        ch = EXAMPLE[i]
        reversed = ch + reversed
    reverse = reversed.casefold()
    print(reverse)

    if reverse == EXAMPLE:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")






if __name__ == '__main__':
        main()