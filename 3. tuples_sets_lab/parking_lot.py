def inside(record, car_num):
    record.add(car_num)


def outside(record, car_num):
    if car_num in record:
        record.discard(car_num)


n = int(input())

cars = set()

for _ in range(n):
    command, car = input().split(", ")
    if command == "IN":
        inside(cars, car)
    elif command == "OUT":
        outside(cars, car)

if cars:
    while cars:
        print(cars.pop())
else:
    print("Parking Lot is Empty")