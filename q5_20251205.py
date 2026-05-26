def file_read(file_pathname):
    with open(file_pathname) as f:
        input_file = f.read().splitlines()
    range_list = []
    ids = []
    for i in input_file:
        if i.find('-') > -1:
            range_list.append(i)
        else:
            ids.append(i)  # First element will be ''
    return range_list, ids[1:]


def extract_first_last_id(my_id_range):
    first, last = my_id_range.split('-')
    return int(first), int(last)


# part 1
def spoiled_ids(file_pathname):
    id_range, id_list = file_read(file_pathname)
    not_spoiled = [0] * len(id_list)
    for i in id_range:
        first_id, last_id = extract_first_last_id(i)
        index = 0
        for j in id_list:
            if int(j) >= int(first_id) and int(j) <= int(last_id):
                not_spoiled[index] = 1
            index = index + 1

    return id_list, not_spoiled

item_ids, freshness = spoiled_ids('day5_input_20251205.txt')
print(sum(freshness))


# part 2: extract all fresh ids
def fresh_id_list_size(id_range):
    # sort id_range based on first id
    full_first_ids = []
    full_last_ids = []
    for i in id_range:
        first, last = extract_first_last_id(i)
        full_first_ids.append(first)
        full_last_ids.append(last)

    previous_first_ids = [0] * len(full_first_ids)
    previous_last_ids = [0] * len(full_last_ids)
    change_flag = True

    while change_flag:
        sorted_index = sorted(range(len(full_first_ids)), key=lambda k: full_first_ids[k])
        sorted_full_first_ids = [full_first_ids[k] for k in sorted_index]
        sorted_full_last_ids = [full_last_ids[k] for k in sorted_index]

        first_ids = [sorted_full_first_ids[0]]
        last_ids = [sorted_full_last_ids[0]]

        for i in range(1, len(sorted_full_first_ids)):
            first_id = sorted_full_first_ids[i]
            last_id = sorted_full_last_ids[i]
            j = 0
            append_flag = False
            # check all previous ranges
            while j < len(first_ids):
                if (last_id < first_ids[j]) or \
                        (first_id > last_ids[j]):
                    append_flag = True
                else:
                    if first_id < first_ids[j] <= last_id <= last_ids[j]:
                        first_ids[j] = first_id
                        append_flag = False
                    elif last_id > last_ids[j] >= first_id >= first_ids[j]:
                        last_ids[j] = last_id
                        append_flag = False
                    elif first_id < first_ids[j] and last_id > last_ids[j]:
                        first_ids[j] = first_id
                        last_ids[j] = last_id
                        append_flag = False
                    else:
#                        print(f'''first id {first_id} and last id {last_id} within range {first_ids[j]}-{last_ids[j]}''')
                        append_flag = False
                j = j + 1
            if append_flag:
                first_ids.append(first_id)
                last_ids.append(last_id)

        if previous_first_ids == full_first_ids and previous_last_ids == full_last_ids:
            change_flag = False

        previous_first_ids = full_first_ids[:]
        previous_last_ids = full_last_ids[:]
        full_first_ids = first_ids[:]
        full_last_ids = last_ids[:]

    len_array = []
    for i in range(0,len(full_first_ids)):
        len_array.append(full_last_ids[i] - full_first_ids[i] + 1)
    return sum(len_array)


id_range, id_list = file_read('day5_input_20251205.txt')
print(fresh_id_list_size(id_range))


