from math import floor
from collections import deque


def get_sec_from_time(time):
    hours, minutes, seconds = list(map(int, time.split(":")))
    return hours * 60 * 60 + minutes * 60 + seconds


def get_time_from_sec(seconds):
    seconds = seconds % (24 * 60 * 60)
    hours = seconds // (60 * 60)
    minutes = floor((seconds / 60) % 60)
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


class Robot:

    def __init__(self, name, processing_time):
        self.name = name
        self.processing_time = processing_time
        self.busy_until = 0


robots_input = input().split(";")

robots = []
for robot_input in robots_input:
    robot_name, processing_time = robot_input.split("-")
    robots.append(Robot(robot_name, int(processing_time)))

time_in_sec = get_sec_from_time(input())

items = deque()

while True:
    product = input()
    if product == "End":
        break
    items.append(product)

while items:
    current_item = items[0]
    time_in_sec += 1
    found_robot = False

    for r in robots:
        if time_in_sec >= r.busy_until:
            r.busy_until = time_in_sec + r.processing_time
            found_robot = True
            print(f"{r.name} - {current_item} [{get_time_from_sec(time_in_sec)}]")
            break

    if found_robot:
        items.popleft()
    else:
        items.append(items.popleft())
