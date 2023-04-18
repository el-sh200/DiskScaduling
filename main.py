ROTATIONAL_DELAY = 4.17
TRANSFER_DELAY = 0.13


def get_input():
    current_sector = int(input('Enter Starting Position: '))
    request_length = int(input('Enter Length of requests: '))
    print('Enter Request Details in format "sector arrival time"')
    requests = []
    for i in range(request_length):
        sector, arrival = input().split(' ')
        requests.append((int(arrival), int(sector)))
    return current_sector, requests


def go_to_the_sector(selected_sector, current_time, current_sector):
    start_stop_time = 0 if selected_sector == current_sector else 1
    current_time += ROTATIONAL_DELAY + TRANSFER_DELAY + abs(current_sector - selected_sector) / 4000 + start_stop_time
    return selected_sector, round(current_time, 1)


def fcfs_method(requests, current_sector):
    current_time = 0
    result = []
    for arrive_time, sector in requests:
        current_sector, current_time = go_to_the_sector(sector, current_time, current_sector)
        result.append((sector, current_time))
    return result


def print_result(result, method):
    print(f'The Method: {method.upper()}')
    for x, y in enumerate(result):
        print(f'   {x}   {y[1]}')


def elevator_goes_up(already, current_sector):
    selected = [request for request in already if (int(request[1]) - current_sector >= 0)]
    return min(selected) if selected else None


def elevator_goes_down(already, current_sector):
    selected = [request for request in already if (current_sector - int(request[1]) >= 0)]
    return max(selected) if selected else None


def elevator_method(requests, current_sector, direction_is_up=True):
    current_time = 0

    # Sort requests by time
    requests.sort(key=lambda x: x[0])

    result = []
    while requests:
        already = [request for request in requests if current_time >= request[0]]
        if not already:
            current_time = requests[0][0]
            already = [request for request in requests if (request[0] == current_time)]

        if direction_is_up:
            selected_request = elevator_goes_up(already, current_sector)
            if not selected_request:
                selected_request = elevator_goes_down(already, current_sector)
                direction_is_up = False
        else:
            selected_request = elevator_goes_down(already, current_sector)
            if not selected_request:
                selected_request = elevator_goes_up(already, current_sector)
                direction_is_up = True
        current_sector, current_time = go_to_the_sector(
            selected_request[1],
            current_time,
            current_sector)
        result.append((selected_request[1], current_time))
        requests.remove(selected_request)
    return result


def main():
    current_sector, requests = get_input()
    fcfs_result = fcfs_method(requests, current_sector)
    print_result(fcfs_result, 'fcfs')
    elevator_result = elevator_method(requests, current_sector, direction_is_up=True)
    print_result(elevator_result, 'elevator')


if __name__ == '__main__':
    main()
