import sys


if len(sys.argv) != 2:
	print("Error: There is an incorrect number of inputs on command line")
	sys.exit(1)
filename = sys.argv[1]

filedata = open(filename, 'r')
text = filedata.read()
filedata.close()

print(text)
splittext = text.split(", ")
print(splittext)

jointext = ''.join(splittext)
length = 8

packets = []
for index in range(0, len(jointext), length):
	substring = jointext[index:index+length]
	packets.append(substring)

conversionlist = [128, 64, 32, 16, 8, 4, 2, 1]
result = 0

for index, value in enumerate(conversionlist):
	if jointext[index] == '1':
		result += conversionlist[index]

print(result)

resultchr = chr(result)
print(resultchr)

outfile = open('output_task1.txt', "w+", encoding = "utf-8",
newline="\r\n")
outfile.write(resultchr)
outfile.close()
#print(list(econversionlist))

