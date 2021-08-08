def word_list(words):
    file = open('words.txt', 'r')
    list = []
    lst = file.read().splitlines()
    for line in lst:
        list.append(line)

    new_list = []

    for i in list:
        try:
            item = i.split(' ', 1)
            new_list.append(item[1])
        except IndexError:
            pass
    return new_list
print(word_list('words.txt'))

