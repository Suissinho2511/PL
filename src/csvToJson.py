################################################################################
# NAME:     CSV TO JSON
# PURPOSE:  Converting a generic csv file to a json file
# GROUP:    5
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
# FUNCTION:  Converts content to a dictionary
################################################################################
def contentToDic(fields, header):
    i = 0
    dic = {}
    for category in header:
        # If it is just a string, then its a simple category
        if isinstance(category, str):
            dic[category] = fields[i]
            i += 1
        #If it isn't, then it involves a list
        else:
            # If the size is a tuple, then we have a min and a max
            if isinstance(category[1], tuple):
                (min_size, max_size) = category[1]
            # if it is just a number, then thats the fixed size
            else:
                max_size = category[1]
            
            cat_list = prepareList(fields[i:(i+max_size)])
            i += max_size
            
            # updating size to the real value
            size = len(cat_list)
            
            #if the record is missing values, then it is not valid
            if isinstance(category[1], tuple):
                if size < min_size:
                    return {}
            elif size < max_size:
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
                dic[category[0] + "_" + category[2]] = str(result)
                
            elif category[2] == "avg":
                # AVERAGE
                result = 0
                for value in cat_list:
                    result += int(value)
                dic[category[0] + "_" + category[2]] = str(result / size)
                
            # else is for invalid functions
            else:
                dic[category[0]] = cat_list
                
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
        printEntry(dic, entry, fo)
        print(",", file=fo)
    # The last key will have a slightly different behaviour (no comma)
    else:
        entry = keys[-1]
        printEntry(dic, entry, fo)
        print("", file=fo)
        
    return

################################################################################
# FUNCTION:  Print to the file one entry
################################################################################
def printEntry(dic, entry, fo):
    value = dic[entry]
    if isinstance(value, list):
        printList(entry, value, fo)
    else:
        print ("\t\t\"" + str(entry) + "\": ", file=fo, end="")
        printElem(value, fo)
    return


################################################################################
# FUNCTION:  Print to the file a list
################################################################################
def printList(entry, value, fo):
    print ("\t\t\"" + str(entry) + "\": [", file=fo, end ="")
    
    for elem in value[:-1]:
        printElem(elem, fo)
        print(", ", file=fo, end ="")
    else:
        printElem(value[-1], fo)
        print("]", file=fo, end="")
    return

################################################################################
# FUNCTION:  Print to the file an element in string or numeric form
################################################################################
def printElem(elem, fo):
    # First we will try to turn it into a number
    try:
        print(int(elem), end = "", file=fo)
    except:
        try:
            # Print float with 2 decimals
            print('%.2f' %float(elem), end = "", file=fo)
        # If it doesn't work, we will print it as a string
        except:
            print("\"" + str(elem) + "\"", end = "", file=fo)   
    return

main()
