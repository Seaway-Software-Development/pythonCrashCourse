travel = ["Ireland", "England", "Scotland", "Italy", "Peru", "Australia"]

print(travel)

print("Sorted:")
print(sorted(travel))

print("Original List:")
print(travel)

print("Reverse Sorted:")
print(sorted(travel, reverse=True))

print(travel)

print("Reverse():")
travel.reverse()
print(travel)

print("Back to original order:")
travel.reverse()
print(travel)

travel.sort()
print(travel)

travel.sort(reverse=True)
print(travel)