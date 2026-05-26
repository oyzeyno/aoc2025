def file_read(pathname):
    with open(pathname) as f:
        input = f.read().splitlines()
    return input

# Part 1
def count_accessed_rolls(myinput, neighbor_limit):
    roll_count = 0
    # input_copy is needed for part 2
    input_copy = myinput.copy()
    # get indexes for roll positions
    for i in range(0, len(myinput)):
        for j, roll in enumerate(myinput[i]):
            neighbor_count = 0
            if roll == "@":
                # corners and edges
                if i == 0:
                    row_i = list(myinput[i])
                    row_i_plus_one = list(myinput[i+1])
                    if j == 0:
                        neighbor_count = row_i[j+1].find('@') + 1 + \
                                         row_i_plus_one[j].find('@') + 1 + \
                                         row_i_plus_one[j+1].find('@') + 1
                    elif j == len(myinput[i]) - 1:
                        neighbor_count = row_i[j - 1].find('@') + 1 + \
                                         row_i_plus_one[j - 1].find('@') + 1 + \
                                         row_i_plus_one[j].find('@') + 1
                    else:
                        neighbor_count = row_i[j-1].find('@') + 1 + \
                                         row_i[j+1].find('@') + 1 + \
                                         row_i_plus_one[j-1].find('@') + 1 + \
                                         row_i_plus_one[j].find('@') + 1 + \
                                         row_i_plus_one[j+1].find('@') + 1

                elif i == len(myinput) - 1:
                    row_i = list(myinput[i])
                    row_i_minus_one = list(myinput[i-1])
                    if j == 0:
                        neighbor_count = row_i[j + 1].find('@') + 1 + \
                                         row_i_minus_one[j].find('@') + 1 + \
                                         row_i_minus_one[j + 1].find('@') + 1
                    elif j == len(myinput[i]) - 1:
                        neighbor_count = row_i[j - 1].find('@') + 1 + \
                                         row_i_minus_one[j - 1].find('@') + 1 + \
                                         row_i_minus_one[j].find('@') + 1

                    else:
                        neighbor_count = row_i[j-1].find('@') + 1 +\
                                     row_i[j+1].find('@') + 1 +\
                                     row_i_minus_one[j-1].find('@') + 1 +\
                                     row_i_minus_one[j].find('@') + 1 +\
                                     row_i_minus_one[j+1].find('@') + 1
                else:
                    row_i = list(myinput[i])
                    row_i_minus_one = list(myinput[i-1])
                    row_i_plus_one = list(myinput[i+1])
                    if j == 0:
                        neighbor_count = row_i[j+1].find('@') + 1 +\
                                         row_i_minus_one[j].find('@') + 1 +\
                                         row_i_minus_one[j+1].find('@') + 1 +\
                                         row_i_plus_one[j].find('@') + 1 +\
                                         row_i_plus_one[j+1].find('@') + 1

                    elif j == len(myinput[i]) - 1:
                        neighbor_count = row_i[j-1].find('@') + 1 + \
                                         row_i_minus_one[j].find('@') + 1 + \
                                         row_i_minus_one[j-1].find('@') + 1 + \
                                         row_i_plus_one[j].find('@') + 1 + \
                                         row_i_plus_one[j-1].find('@') + 1

                    else:
                        neighbor_count = row_i[j-1].find('@') + 1 + \
                                         row_i[j+1].find('@') + 1 + \
                                         row_i_minus_one[j-1].find('@') + 1 + \
                                         row_i_minus_one[j].find('@') + 1 + \
                                         row_i_minus_one[j+1].find('@') + 1 + \
                                         row_i_plus_one[j-1].find('@') + 1 + \
                                         row_i_plus_one[j].find('@') + 1 + \
                                         row_i_plus_one[j+1].find('@') + 1

                #print(f'''row {i} col {j} n_neighbor {neighbor_count}''')
                if neighbor_count < neighbor_limit:
                    roll_count = roll_count + 1
                    # added for part 2: update the grid
                    input_copy[i] = str(input_copy[i][:j] + '.' + input_copy[i][j+1:])

    return roll_count, input_copy


# Part 2 with state update
def count_total_rolls_after_update(original_input):
    neighbor_cutoff = 4
    total_roll_count = 0
    roll_count = 1
    while roll_count > 0:
        roll_count, tmp_grid = count_accessed_rolls(original_input, neighbor_cutoff)
        total_roll_count = total_roll_count + roll_count
        original_input = tmp_grid

    return total_roll_count

# part 1
print(count_accessed_rolls(file_read(pathname), 4))
# part 2
print(count_total_rolls_after_update(file_read(pathname)))