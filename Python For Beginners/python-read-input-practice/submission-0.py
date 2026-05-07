def add_two_numbers() -> int:
    string = input()
    string_list = string.split(",")

    cnt = 0
    for c in string_list:
        cnt += int(c)
    return cnt








# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
