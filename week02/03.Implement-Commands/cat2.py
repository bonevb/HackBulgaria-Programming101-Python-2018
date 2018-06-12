import sys

arguments = sys.argv
print(arguments)


def cat2(arguments):
    for i in arguments[1:]:
    	with open(i, 'r') as f:
    		lines = f.readlines()
    		for line in lines:
    			print(line)
    	print()


def main():
    cat2(arguments)

if __name__ == '__main__':
    main()