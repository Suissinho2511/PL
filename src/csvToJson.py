################################################################################
# NAME:     CSV TO JSON
# PURPOSE:  Converting a generic csv file to a json file
#GROUP:     5
# ELEMENTS: a93234 - Diogo Matos
#           a83630 - Duarte Serrão
#           a93208 - Vasco Oliveira
################################################################################
import sys
from lexer import lexFunc#, removeEmpty

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
    
    # Reading the content in dictionary format
    content = readContent(fi, header)
    #content = readContent(fi, header, lists, funcs)

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
# FUNCTION:  Getting each entry and put it in a list
################################################################################
def readContent(file, header):
    content = []
    for line in file:
        #lines with no content are skipped
        if line != "\n":
            record = contentToDic(lexFunc(line), header)
            #If it returns an empty dictionary, then it skips the line
            if record != {}:
                content.append(record)
    return content




################################################################################
# FUNCTION:  
################################################################################
def contentToDic(fields, header):
    i = 0
    dic = {}
    for category in header:
        # If it is just a string, then its a simple category
        if isinstance(category, str):
            dic[category] = fields[i]
        #If it isn't, then it involves a list
            i += 1
        else:
            # If the size is a tuple, then we have a min and a max
            if isinstance(category[1], tuple):
                (min_size, size) = category[1]
            # if it is just a number, then thats the fixed size
            else:
                size = category[1]
                
            cat_list = prepareList(fields[i:(i+size)])
            
            # updating size to the real value
            size = len(cat_list)
            
            #if the record is missing values, then it is not valid
            if size < min_size:
                return {}
            
            # If there are no functions, then we just save the list
            if len(category) < 3:
                dic[category[0]] = cat_list
                continue 
            
            if category[2] == "sum":
                # SUM
                result = 0
                for value in cat_list:
                    result += int(value)
                dic[category[0] + "_" + category[2]] = result
                
            elif category[2] == "avg":
                # AVERAGE
                result = 0
                for value in cat_list:
                    result += int(value)
                dic[category[0] + "_" + category[2]] = result / size
                
            # else is for invalid functions
            else:
                dic[category[0]] = cat_list
                
            i += size
    return dic


################################################################################
# FUNCTION:  
################################################################################
def prepareList(input):
    output = []
    for elem in input:
        if elem != '':
            output.append(elem)
    return output

################################################################################
# FUNCTION:  Converting the list of entries to a json file
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
        value = dic[entry]
        
        # checking if this entry is a list
        if isinstance(value, list):
            print ("\t\t\"" + str(entry) + "\": [", file=fo, end ="")
            #printing each element of the list
            for elem in value[:-1]:
                print(str(elem) + ", ", file=fo , end ="" )
            else:
                print(str(value[-1]) + "],", file=fo)
        else:
            print ("\t\t\"" + str(entry) + "\": \"" + str(value) + "\",", file=fo)
    # The last key will have a slightly different behaviour (no comma)
    else:
        entry = keys[-1]
        value = dic[entry]
        if isinstance(value, list):
            print ("\t\t\"" + str(entry) + "\": [", file=fo, end ="")
            for elem in value[:-1]:
                print(str(elem) + ", ", file=fo, end ="")
            else:
                print(str(value[-1]) + "]", file=fo)
        else:
            print ("\t\t\"" + str(entry) + "\": \"" + str(value) + "\"", file=fo)
    return


main()
