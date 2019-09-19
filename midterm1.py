# print() with end parameter
print("Everything", end=" ")
print("is", end=" ")
print("a", end=" ")
print("Widget")

list = ["Everything","is","a","Widget"]
for counter, value in enumerate(list):
    print(f"{counter}: {value}")

# Break Statement
for i in range(1, 11):
    if i is 5:
        break
    else:
        print(i)

# Continue Statement
for i in range(1,11):
    if i is 5:
        continue
    else:
        print(i)


list = {"name": "He", "She": "It"}
connector = " is "
print(connector.join(list))

string = "***Welcome***"
print(string.lstrip("*"))
print(string.rstrip("*"))

alnum = "Hello555"
print(alnum.isalnum())