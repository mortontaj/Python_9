# Write a small program to display info on the
# four clocks whose functions we have just looked at
# i.e time(), perf_counter, monotonic, and process_time
#
# Use the doc for the get_clock_info() function
# to work out how to call it for each of the clocks

import time

def display_time():
    """
    Shows the current time for the four clocks

    :return:
    """
    x = time.get_clock_info('time')
    y = time.get_clock_info('perf_counter')
    z = time.get_clock_info('monotonic')
    a = time.get_clock_info('process_time')
    watch = (x, y, z, a)


    return watch


print(display_time())

# print("time(): \t\t\t", time.get_clock_info('time'))
# print("per_counter(): \t\t", time.get_clock_info('perf_counter'))
# print("monotonic(): \t\t", time.get_clock_info('monotonic'))
# print("process_time(): \t", time.get_clock_info('process_time'))
