def file_read(pathname):
    with open(pathname) as f:
        input = f.read().splitlines()
    return input

def find_joltage(number):
    tt = list(number)
    tt.sort(reverse=True)
    max_digit = tt[0]
    max_index = number.find(max_digit)
    # if max_index is at the end, find the second max
    if max_index == len(number) - 1:
        max_digit = tt[1]
        max_index = number.find(max_digit)

    # search for max available digit after max_digit's position

    tt_2 = list(number[max_index + 1:])
    tt_2.sort(reverse=True)
    max_digit_2 = tt_2[0]
    joltage = int(max_digit + max_digit_2)
    return joltage


def find_joltage_12(number):
    slice_size = 12

    def find_max_index(sliced_number, chunk_size):
        find_max_flag = False
        counter = 0
        tt = list(sliced_number)
        tt.sort(reverse=True)
        max_digit = tt[0]
        max_index = sliced_number.find(max_digit)
        # find max digit with at least (chunk_size - 1) characters after
        while not find_max_flag:
            if max_index + chunk_size <= len(sliced_number):
                find_max_flag = True
            else:
                counter = counter + 1
                max_digit = tt[counter]
                max_index = sliced_number.find(max_digit)
        return max_digit, max_index

    joltage = []

    # Find max digit for the specified slice size
    first_max_digit, first_max_index = find_max_index(number, slice_size)

    joltage.append(first_max_digit)
    tmp = first_max_index
    for j in reversed(range(1, slice_size)):
        max_digit_second, max_index_second = find_max_index(number[tmp + 1:], j)

        # Find real index based in number, it should be after previous max digit
        for i, character in enumerate(number):
            if character == max_digit_second and i > tmp:
                max_index_second_real = i
                joltage.append(max_digit_second)
                tmp = max_index_second_real
                break

    joltage_value = int(''.join(joltage))
    return joltage_value


def find_joltage_sum(input):
    joltage_sum = 0
    joltage_12_sum = 0
    for i in input:
        joltage = find_joltage(i)
        joltage_sum = joltage_sum + joltage

        joltage_12 = find_joltage_12(i)
        joltage_12_sum = joltage_12_sum + joltage_12

    return joltage_sum, joltage_12_sum


print(find_joltage_sum(file_read('day3_input_20251203.txt')))