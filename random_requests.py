import random

from main import fcfs_method, elevator_method


def get_random_requests():
    try:
        size = int(input('Enter size of requests: '))
    except:
        size = 1000

    time_range = 1000
    sector_range = 65535
    requests = list((random.randrange(0, time_range), random.randrange(0, sector_range)) for i in range(size))
    current_sector = random.randrange(65535)
    direction = random.choice([True, False])

    return current_sector, direction, requests


def make_file(fcfs, elevator):
    with open(f'data.csv', 'w') as myfile:
        myfile.write('time,fcfs,elevator,\n')
        for i, request in enumerate(zip(fcfs, elevator)):
            fcfs, elevator = request
            myfile.write(f'{i},{fcfs[1]},{elevator[1]},\n')


def random_method():
    current_sector, direction, requests = get_random_requests()

    fcfs_result = fcfs_method(requests, current_sector)
    elevator_result = elevator_method(requests, current_sector, direction)
    make_file(fcfs_result, elevator_result)


random_method()
