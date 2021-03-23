with open("file1.txt") as f1:
    with open("file2.txt") as f2:
        string1 = f1.readlines()
        string2 = f2.readlines()
        common = [int(word.strip()) for word in string1 if word in string2]

print(common)
