import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# Run time is still above 1 sec (1.44s) could use work
for names_2 in names_2:
    if names_2 in names_1:
        duplicates.append(names_2)

# Method used in stretch below (Uses a set, which was restricted), results in a runtime > 0.01s
# cache = {}
# for names_1 in names_1:
#     cache[names_1] = names_1
# for names_2 in names_2:
#     if names_2 in cache:
#         duplicates.append(names_2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
cache = {}
for names_1 in names_1:
    cache[names_1] = names_1
for names_2 in names_2:
    if names_2 in cache:
        duplicates.append(names_2)
