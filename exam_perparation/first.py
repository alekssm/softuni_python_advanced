from collections import deque

effects = deque(map(int, input().split(", ")))
powers = list(map(int, input().split(", ")))

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

showtime = False

while effects and powers:

    effect = effects.popleft()
    power = powers.pop()

    if not effect > 0:
        powers.append(power)
        continue
    if not power > 0:
        effects.appendleft(effect)
        continue

    firework = effect + power
    if firework % 3 == 0 and firework % 5 == 0:
        crossette_fireworks += 1
    elif firework % 3 == 0:
        palm_fireworks += 1
    elif firework % 5 == 0:
        willow_fireworks += 1
    else:
        effect -= 1
        effects.append(effect)
        powers.append(power)

    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        showtime = True
        break

if showtime:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in effects])}")

if powers:
    print(f"Explosive Power left: {', '.join([str(x) for x in powers])}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
