from collections import deque

green_light_duration = int(input())
free_window = int(input())

car_crash = False
cars_at_crossroad = deque()
cars_passed = 0

while True:
    new_car = input()
    if new_car == "END":
        break

    if new_car == "green":
        green_time_left = green_light_duration

        while cars_at_crossroad:
            car = cars_at_crossroad[0]
            if green_time_left > 0:
                if len(car) <= green_time_left:
                    cars_at_crossroad.popleft()
                    green_time_left -= len(car)
                    cars_passed += 1
                else:
                    cars_at_crossroad.popleft()
                    part_of_car_left = len(car) - green_time_left
                    green_time_left = 0
                    if part_of_car_left <= free_window:
                        cars_passed += 1
                    else:
                        hit = part_of_car_left - free_window
                        print("A crash happened!")
                        print(f"{car} was hit at {car[-hit]}.")
                        car_crash = True
                        break
            else:
                break

    else:
        cars_at_crossroad.append(new_car)

    if car_crash:
        break

if not car_crash:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
