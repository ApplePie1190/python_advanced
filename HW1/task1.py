def find_duplicates(lst):
    return [item for item in set(lst) if lst.count(item) > 1]


if __name__ == '__main__':
    my_list = [1, 2, 2, 3, 4, 4, 5]
    new_list = find_duplicates(my_list)
    print(new_list)
