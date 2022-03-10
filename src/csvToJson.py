################################################################################
#NAME:      CSV TO JSON
#PURPOSE:   Converting a generic csv file to a json file
#GROUP:     5
#ELEMENTS:  a93234 - Diogo Matos
#           a83630 - Duarte Serrão
#           a932xx - Vasco Oliveira
################################################################################
import re
import sys

################################################################################
#FUNCTION:  Main body that will control the program
################################################################################
def main():
    input = sys.argv[1]
    #output = sys.argv[2]
    fi = open(input, "r", encoding="UTF-8")
    #fo = open(output, "w", encoding="UTF-8")
    groups = getGroups(fi)
    print(groups)
    #dicToJson(fo, content)
    fi.close()
    #fo.close()
    return

################################################################################
#FUNCTION:  Converting the list of dictionaries to a json file
################################################################################
def getGroups(file):
    #Grupo terá um nome geral
    #dentro do grupo não pode conter nenhuma virgula nem enter
    regex = r'(?:(?P<GROUP_ID>[^,\n]+),?)'
    matches = re.finditer(regex, file.readline().strip())
    groups = []
    for match_obj in matches:
        groups.append(match_obj.group('GROUP_ID'))
    return groups


################################################################################
#FUNCTION:  Getting each entry and put it in a dictionary
################################################################################
def readContent(file):
    regex = r'(?:(?P<ELEMENT>[^,\n]+),?)'
    dic = []
    for line in file:
        match = re.search(regex, line)
        if match:
            dic.append(match.groupdict())
    return dic

################################################################################
#FUNCTION:  Converting the list of dictionaries to a json file
################################################################################
def dicToJson(fo, content):
    i = 0
    #Begining of json file
    print("{", file=fo)

    for dic in content:
        print("\t\"entry" + str(i) + "\": {", file=fo)
        printKeys(dic, fo)

        #If it is the end of the dictionary list, we just end the entry
        if list(content)[-1] == dic:
            print("\t}", file=fo)
        #If its not, we go to the next entry
        else:
            print("\t},", file=fo)
            i = i + 1

    #End of json file
    print("}", file=fo)
    return

################################################################################
#FUNCTION:  Print to the file every entry of the dictionary
################################################################################
def printKeys(dic, fo):
    for entry in dic.keys():
        line = "\t\t\""  + str(entry) + "\": \"" + str(dic[entry]) + "\""
        #If it is NOT the end of the dictionary, we need a comma to let it know there are more keys
        if list(dic)[-1] != entry: line += ","
        print(line, file=fo)
    return


main()