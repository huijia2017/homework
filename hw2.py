# read and show the text file
txt = open("numbers.txt")
content = txt.read()
print(content)
print('-'*60)

# counting with dictionary function
d = dict()
for line in content:
    line = line.strip()
    numbers = line.split(" ")
    for word in numbers:
        if word in d:
            d[word] += 1  # d[word] + 1
        else:
            d[word] = 1
for key in list(d.keys()):
    print(key, ":", d[key])
