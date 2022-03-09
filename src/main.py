import re
import sys


def main():
    input = sys.argv[1]
    output = sys.argv[2]
    fi = open(input, "r", encoding="UTF-8")
    fo = open(output, "w", encoding="UTF-8")

    line = readHeader(fi)
    print("{" + str(line) + "}\n", file=fo)

    fi.close()
    fo.close()
    return


def readHeader(file):
    line = file.readline().strip()
    split = line.split(",")
    return split


main()
