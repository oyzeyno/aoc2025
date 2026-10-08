def file_read(pathname):
    with open(pathname) as f:
        input_file = f.read().splitlines()
    return input_file


def find_character_index(s, ch):
    return [k for k, ltr in enumerate(s) if ltr == ch]


def insert_character(s, c, pos):
    # Insert character at specified position
    return s[:pos] + c + s[pos+1:]


def put_dash_and_count(mymap):
    start_pos = find_character_index(mymap[0], 'S')
    mymap[1] = insert_character(mymap[1], '|', start_pos[0])
    hit_count = 0
    index_range = [x for x in range(2, len(mymap)-1) if x % 2 == 0]

    for j in index_range:
        beam_index = find_character_index(mymap[j-1], '|')
        block_index = find_character_index(mymap[j], '^')
        hit_index = list(set(beam_index).intersection(set(block_index)))
        non_hit_index = list(set(beam_index).difference(set(hit_index)))
        hit_count = hit_count + len(hit_index)
        # insert beams
        for k in hit_index:
            mymap[j+1] = insert_character(mymap[j+1], '|', k - 1)
            mymap[j+1] = insert_character(mymap[j+1], '|', k + 1)

        for k in non_hit_index:
            mymap[j+1] = insert_character(mymap[j+1], '|', k)

    return hit_count
