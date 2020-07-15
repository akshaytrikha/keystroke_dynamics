from pynput.keyboard import Key, Listener
import time
import csv

REPEAT_NUMBER = 5
esc_count = 0
keys = [[] for i in range(REPEAT_NUMBER)]
print(keys)

#
# record list_of_rows into a csv called filename
#
def write_to_csv(list_of_rows, filename):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open(filename, "w", newline='')
        filewriter = csv.writer(csvfile, delimiter=",")
        for row in list_of_rows:
            filewriter.writerow(row)
        # filewriter.writerows(list_of_rows)
        csvfile.close()

    except:
        print("File", filename, "could not be opened for writing...")

#
# function called on keypress
#
def on(key):
    """records an input key into keys list alongside the timestamp when it was pressed"""
    # start_time = time.time()
    # print("{0} pressed".format(key), time.perf_counter())

    global keys, esc_count, REPEAT_NUMBER

    # caps, shift, etc. aren't automatically registered as strings
    if type(key) == Key:
        keys[esc_count].append((str(key), time.perf_counter(), "pressed"))
    else:
        keys[esc_count].append((key, time.perf_counter(), "pressed"))

    if key == Key.esc:
        esc_count = esc_count + 1
        print(esc_count)
        if esc_count >= REPEAT_NUMBER:
            print("\n\n", keys, "\n\n")
            write_to_csv(keys, "test_data.csv")
            print("wrote to test_data.csv")
            return False

#
# function called on key release
#
def off(key):
    """records an input key into keys list alongside the timestamp when it was released"""
    # print("{0} released".format(key), time.perf_counter())

    global keys, esc_count

    # caps, shift, etc. aren't automatically registered as strings
    if type(key) == Key:
        keys[esc_count].append((str(key), time.perf_counter(), "released"))
    else:
        keys[esc_count].append((key, time.perf_counter(), "released"))

# with Listener(on_press=on, on_release=off) as listener:
#     listener.join()

listener = Listener(on_press=on, on_release=off)
listener.start()
listener.join()

# .tie5Roanle
