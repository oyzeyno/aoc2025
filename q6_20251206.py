import pandas as pd

# part 1 file read
def file_read(pathname):
    with open(pathname) as f:
        input_file = f.read().splitlines()

    number_data = []
    for i in range(0, len(input_file)):
        input_file[i] = input_file[i].strip()
        number_data.append(input_file[i].split())

    operator_list = input_file[-1].split()
    del number_data[-1]

    df = pd.DataFrame(number_data)
    column_names = []
    for i in range(1, len(df.columns)+1):
        column_names.append('col' + str(i))
    df.columns = column_names

    return df, operator_list


def insert_character(s, c, pos):
    # Insert character at specified position
    return s[:pos] + c + s[pos+1:]


def find_character_index(s, ch):
    return [k for k, ltr in enumerate(s) if ltr == ch]


# part 2 file read
def file_read_2(pathname):
    with open(pathname) as f:
        input_file = f.read().splitlines()

    space_index_data = []
    for i in range(0, len(input_file)-1):
        # Find all index for " "
        space_index_data.append(find_character_index(input_file[i], ' '))

    # Delimiter location
    del_loc = list(set(space_index_data[0]).intersection(*space_index_data))
    new_data = []
    str_number_data = []
    for i in range(0, len(space_index_data)):
        for j in del_loc:
            input_file[i] = insert_character(input_file[i], "-", j)
        new_data.append(input_file[i])
        str_number_data.append(new_data[i].split('-'))

    # rearrange numbers so that the numbers belonging to an operation will be in the same array
    rearranged_str_number_data = []
    for j in range(0, len(str_number_data[0])):
        v1 = []
        for i in range(0, len(str_number_data)):
            v1.append(str_number_data[i][j])
        rearranged_str_number_data.append(v1)

    operator_list = input_file[-1].split()
    # extract 'real' numbers
    real_numbers = []
    for i in rearranged_str_number_data:
        v1 = []
        char_len = len(i[0])
        for j in range(0, char_len):
            real_number = ''
            for k in i:
                real_number = real_number + k[j]
            v1.append(int(real_number))
        real_numbers.append(v1)

    return real_numbers, operator_list


def calculate_result(col_x, op_y):
    result = 0
    if op_y == '+':
        result = sum(col_x)

    if op_y == '*':
        result = 1
        for i in col_x:
            result = result * i
    return result


# part 1
def apply_operator(df, ops):
    res_sum = 0
    for i in range(0,len(ops)):
        v1 = list(map(int, df.iloc[:, i].values.tolist()))
        res_sum = res_sum + calculate_result(v1, ops[i])

    return res_sum


# part 1
df, op = file_read('day6_input_20251206.txt')
apply_operator(df, op)

# part 2
def apply_operator_2(myarray, ops):
    res_sum = 0
    for i in range(0,len(ops)):
        res_sum = res_sum + calculate_result(myarray[i], ops[i])

    return res_sum


# part 2
t, op = file_read_2('day6_input_20251206.txt')
apply_operator_2(t, op)



