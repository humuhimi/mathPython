qs = ["what is your name",
      "what is fav color ",
      "what is your request"]

n = 0

while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3
    print(a)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
added = []

for i in list1:
    for j in list2:
        added.append(i + j)
print(added)

