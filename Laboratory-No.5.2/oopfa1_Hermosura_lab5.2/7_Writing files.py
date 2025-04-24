fout = open('output.txt', 'w')
print(fout)

line1 = "This here's the wattle,\n"
print(fout.write(line1))

line2 = "the emblem of our land.\n"
print(fout.write(line2))

fout.close()
