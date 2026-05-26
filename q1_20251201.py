def file_read(pathname):
    with open(pathname) as f:
        input = f.read().splitlines()
    return input


def times_zero(input):
    # Dial starts from position 50, with a range 0-99
    new_pos = 50

    # Counter for how many times the dial points to zero
    zero_counter = 0

    # Counter for how many times rotation goes over zero
    rotate_zero_counter = 0

    # follow instruction input
    for i in input:
        n_clicks = i.strip("R")
        n_clicks = n_clicks.strip("L")
        n_clicks = int(n_clicks)

        if new_pos == 0 and n_clicks % 100 == 0:
            rotate_zero_counter = rotate_zero_counter - 1

        if i.startswith("R"):
            new_pos = new_pos + n_clicks
            # Integer division - floor
            rotate_zero_counter = rotate_zero_counter + (new_pos // 100)
            new_pos = new_pos % 100

        if i.startswith("L"):
            old_pos = new_pos
            new_pos = new_pos - n_clicks

            rotate_zero_counter = rotate_zero_counter + ((new_pos // 100) * -1)

            # if starting position is 0, then floor division yields rotation + 1
            if old_pos == 0 and n_clicks % 100 != 0:
                rotate_zero_counter = rotate_zero_counter - 1

            new_pos = new_pos % 100

            # Increase rotation if we end up at 0
            if new_pos == 0:
                rotate_zero_counter = rotate_zero_counter + 1

        # Counter for part 1
        if new_pos == 0:
            zero_counter = zero_counter + 1

    return zero_counter, rotate_zero_counter


print(times_zero(file_read('day1_input_20251201.txt')))
