# print() with end parameter
print("Everything", end=" ")
print("is", end=" ")
print("a", end=" ")
print("Widget")

list = ["Everything","is","a","Widget"]
for counter, value in enumerate(list):
    print(f"{counter}: {value}")