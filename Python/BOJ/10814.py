people = []
for i in range(int(input())):
    [a, b] = input().split()
    people.append([int(a), b])
people.sort(key=lambda x: x[0])
for i in range(len(people)):
    print(people[i][0], people[i][1])