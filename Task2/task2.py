f = open("strings.txt", "r")
first_line = f.readline()
print(len(first_line.strip().split())) 
f.close
