def file_read(pathname):
    with open(pathname) as f:
        input = f.read()
    return input

def extract_first_last_id(id_range):
    first, last = id_range.split('-')
    return int(first), int(last)


def invalid_id(first_id, last_id):
    invalid_id_list = []
    for i in range(first_id, last_id + 1):
        str_id = str(i)
        length_str = int(len(str_id))

        if length_str % 2 == 0:
            half_length = int(length_str / 2)
            first_half = str_id[:half_length]
            second_half = str_id[-half_length:]
            if first_half == second_half:
                invalid_id_list.append(i)

    return invalid_id_list


def invalid_id_2(first_id, last_id):
    invalid_id_list = []
    for i in range(first_id, last_id + 1):
        str_id = str(i)
        length_str = int(len(str_id))
        half_length = int(length_str // 2)
        for j in range(1, half_length+1):
            pattern = str_id[:j]
            how_many = int(length_str / j)
            if str_id == how_many * pattern:
                invalid_id_list.append(i)
    mylist = list(set(invalid_id_list))
    return mylist


def return_invalid_sum(input):
    range_list = input.split(',')
    id_sum = 0
    id_sum_2 = 0
    for i in range_list:
        first, last = extract_first_last_id(i)
        id_sum = id_sum + sum(invalid_id(first, last))
        id_sum_2 = id_sum_2 + sum(invalid_id_2(first, last))

    return id_sum, id_sum_2

print(return_invalid_sum(file_read(pathname)))