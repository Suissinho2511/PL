import re
import sys


def main():
    input = sys.argv[1]
    #output = sys.argv[2]
    fi = open(input, "r", encoding="UTF-8")
    #fo = open(output, "w", encoding="UTF-8")

    groups = getGroups(fi)
    print(groups)
    #csvToJson(fo, content)
    fi.close()
    #fo.close()
    return


def getGroups(file):
    #Grupo terá um nome geral
    #dentro do grupo não pode conter nenhuma virgula nem enter
    regex = r'(?:(?P<GROUP_ID>[^,\n]+),?)'
    matches = re.finditer(regex, file.readline().strip())
    groups = []
    for match_obj in matches:
        groups.append(match_obj.group('GROUP_ID'))
    return groups



def redContent(file):
    regex = r'(?:(?P<ELEMENT>[^,\n]+),?)'
    dic = []
    for line in file:
        match = re.search(regex, line)
        if match:
            dic.append(match.groupdict())
    return dic

def csvToJson(fo, content):
    i = 0
    #Begining of json file
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
