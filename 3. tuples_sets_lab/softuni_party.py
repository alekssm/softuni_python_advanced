numm = int(input())

regulars = set()
vips = set()

for _ in range (numm):
    guest_id = input()
    if len(guest_id) == 8:
        if guest_id[0].isdigit():
            vips.add(guest_id)
        else:
            regulars.add(guest_id)

ppl = set()

while True:
    person = input()
    if person == "END":
        break
    else:
        ppl.add(person)

vips_not_present = list(vips.difference(ppl))
regulars_not_present = list(regulars.difference(ppl))

vips_not_present.sort()
regulars_not_present.sort()

print(len(vips_not_present) + len(regulars_not_present))
while vips_not_present:
    print(vips_not_present.pop(0))
while regulars_not_present:
    print(regulars_not_present.pop(0))



#print(regulars)
#print(vips)