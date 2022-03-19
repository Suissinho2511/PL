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
    header = lexFunc(line, "HEADER")
    
    # Reading the content in dictinary format
    content = readContent(fi, header)

    # Writing in JSON file
    dicToJson(fo, content)

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
# FUNCTION:  Getting each entry and put it in a dictionary
################################################################################
def readContent(file, header):
    dic = []
    for line in file:
        #lines with no content are skipped
        if line != "\n":
            fields = lexFunc(line)
            dic.append(dict(zip(header, fields)))
    return dic


################################################################################
# FUNCTION:  Converting the list of dictionaries to a json file
################################################################################
def dicToJson(fo, content):
    
    # Begining of json file
    print("[", file=fo)

    # We iterate through every record except the last
    for dic in content[:-1]:
        print("\t{", file=fo)
        printKeys(dic, fo)
        print("\t},", file=fo)
        
    # The last record will have a slightly different behaviour (no comma)
    else:
        print("\t{", file=fo)
        printKeys(content[-1], fo)
        print("\t}", file=fo)
        
    # End of json file
    print("]", file=fo)
    return


################################################################################
# FUNCTION:  Print to the file every entry of the dictionary
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
