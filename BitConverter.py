import sys
import binascii

def convertbits(text, encoding='utf-8', errors='surrogatepass'):
	bits = bin(int.from_bytes(text.encode(encoding, errors), 'big')) [2:]
	return bits.zfill(8 * ((len(bits) + 7) // 8))

if len(sys.argv) !=2:
	print("Not enough arguments")
	sys.exit(1)

filename = sys.argv[1]
filedata = open(filename, "r")
text = filedata.read()
print(text)

result = convertbits(text)
print(text)

outfile = open('output_task2.txt', "w+", encoding='utf-8',
newline = "\r\n")
outfile.write(result)
outfile.close()