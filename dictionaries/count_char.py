TEXT = 'Happy day! I love the Code in Place community!'


def get_counts_dict(str):
    counts = {}
    for ch in str:
        if ch not in counts:
            counts[ch] = 1
        else:
            counts[ch] +=1

    return counts



def main():
    print(get_counts_dict(TEXT))

    count_dict = get_counts_dict(TEXT)


    print("Counts from dictionary")
    for key in get_counts_dict(TEXT):
        print(str(key) + " = " + str(count_dict[key]))








if __name__ == '__main__':
    main()