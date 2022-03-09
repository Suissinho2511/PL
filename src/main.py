import re
import sys


def main():
    input = sys.argv[1]
    output = sys.argv[2]
    fi = open(input, "r", encoding="UTF-8")
    fo = open(output, "w", encoding="UTF-8")

    content = readHeaderv2(fi)
    csvToJson(fo, content)
    fi.close()
    fo.close()
    return


def readHeader(file):
    line = file.readline().strip()
    split = line.split(",")
    return split


def readHeaderv2(file):
    alunoRegex = r'(?:\"(?P<id>.+)\",)(?:\"(?P<nome>.+)\",)(?:\"(?P<curso>.+)\",)(?:(?P<TPC1>\d+),)?(?:(?P<TPC2>\d+),)?(?:(?P<TPC3>\d+),)?(?:(?P<TPC4>\d+))?'
    dic = []
    for line in file:
        match = re.search(alunoRegex, line)
        if match:
            dic.append(match.groupdict())
    return dic


def csvToJson(fo, content):
    i = 0
    print("{", file=fo)
    for dic in content:
        if list(content)[-1] == dic:
            print("\t\"entry" + str(i) + "\"" + ": {", file=fo)
            for entry in dic.keys():
                if list(dic)[-1] == entry:
                    print("\t\t" + "\"" + str(entry) + "\"" + ": " +
                          "\"" + str(dic[entry]) + "\"", file=fo)
                else:
                    print("\t\t" + "\"" + str(entry) + "\"" +
                          ": " + "\"" + str(dic[entry]) + "\",", file=fo)
            print("\t}", file=fo)
        else:
            print("\t\"entry" + str(i) + "\"" + ": {", file=fo)
            for entry in dic.keys():
                if list(dic)[-1] == entry:
                    print("\t\t" + "\"" + str(entry) + "\"" + ": " +
                          "\"" + str(dic[entry]) + "\"", file=fo)
                else:
                    print("\t\t" + "\"" + str(entry) + "\"" +
                          ": " + "\"" + str(dic[entry]) + "\",", file=fo)
            print("\t},", file=fo)
            i = i + 1
    print("}", file=fo)
    return


main()
