################################################################################
# NAME:     CSV TO JSON
# PURPOSE:  Converting a generic csv file to a json file
#GROUP:     5
# ELEMENTS: a93234 - Diogo Matos
#           a83630 - Duarte Serrão
#           a93208 - Vasco Oliveira
################################################################################
import sys
from lexer import lexFunc

################################################################################
# FUNCTION:  Main body that will control the program
################################################################################
def main():
    evalError(len(sys.argv) < 3 or len(sys.argv) > 3, "csvToJson <imput-file.csv> <output-file.json>")
        
    input = sys.argv[1]
    evalError(not input.endswith(".csv"), "Input file needs to end with '.csv'")
    
    output = sys.argv[2]
    evalError(not output.endswith(".json"), "Output file needs to end with '.json'")
    
    fi = open(input, "r", encoding="UTF-8")
    fo = open(output, "w", encoding="UTF-8")

    # Getting the header
    line = fi.readline()
    header, lists, funcs = lexFunc(line, "HEADER")
    #print(header)
    #print(lists)
    #print(funcs)
    
    # Reading the content in list format
    content = readContent(fi)

    # Writing in JSON file
    dicToJson(fo, content, header, lists, funcs)

    fi.close()
    fo.close()
    return

################################################################################
# FUNCTION: Evaluations a "deadly" predicate, terminating the program if true
################################################################################
def evalError(predicate, error = "Something ain't right"):
    if predicate:
        print(error)
        quit()
    return

################################################################################
# FUNCTION:  Getting each entry and put it in a list
################################################################################
def readContent(file):
    content = []
    for line in file:
        #lines with no content are skipped
        if line != "\n":
            content.append(lexFunc(line))
    return content


################################################################################
# FUNCTION:  Converting the list of entries to a json file
################################################################################
def dicToJson(fo, content, header, lists, funcs):
    
    # Begining of json file
    print("[", file=fo)

    is_first = True
    # We iterate through every record except the last
    for line in content:
        i = 0
        dic = {}

        if is_first:
            print("\t{", file=fo)
            is_first = False
        else:
            print(",\n\t{", file=fo)

        for entry in header:
            if entry in lists:
                # É uma lista
                min_size, max_size = lists[entry]

                if entry in funcs:
                    # Tem uma função aplicada
                    func = funcs[entry]

                    if func == "sum":
                        # SUM
                        result = 0
                        for value in line[i:i+max_size]:
                            result += int(value)
                        dic[entry] = result

                    elif func == "avg":
                        # AVERAGE
                        result = 0
                        n = 0
                        for value in line[i:i+max_size]:
                            result = (result * n + int(value)) / (n+1)
                            n += 1
                        dic[entry] = result

                    else:
                        #função inválida (deveria dar erro)
                        pass

                else:
                    # É uma lista normal
                    dic[entry] = line[i:i+max_size]

                i += max_size
            else:
                # É uma entrada normal
                dic[entry] = line[i]
                i += 1

        printKeys(dic, fo)
        print("\t}", file=fo, end="")
        
    # End of json file
    print("\n]", file=fo)
    return


################################################################################
# FUNCTION:  Print to the file every entry of the dictionary
# TODO: listas e resultados de funções não deverão ter ""
################################################################################
def printKeys(dic, fo):
    keys = list(dic.keys())
    # We iterate through every key except the last
    for entry in keys[:-1]:
        print ("\t\t\"" + str(entry) + "\": \"" + str(dic[entry]) + "\",", file=fo)
    # The last key will have a slightly different behaviour
    else:
        print ("\t\t\"" + str(keys[-1]) + "\": \"" + str(dic[keys[-1]]) + "\"", file=fo)
    return


main()
