
def display_list(lst):

    for item in lst:
        if item.isdigit():
            print(item * 3)
        else:
            print(item + "#")


data = ['23', 'MAN', 'GIRIRAJ', '24', 'ZARA']

display_list(data)
