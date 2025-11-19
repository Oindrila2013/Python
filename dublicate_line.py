outputfile = open('codingal_update.txt', 'w')
inputfile = open('codingal.txt', 'r')

line_seen_so_far = set()

print("Eliminating dublicated lines.")

for line in inputfile:
    if line not in line_seen_so_far:
        outputfile.write(line)
        line_seen_so_far.add(line)

inputfile.close()
outputfile.close()