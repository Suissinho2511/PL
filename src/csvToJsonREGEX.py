################################################################################
# NAME:      CSV TO JSON
# PURPOSE:   Converting a generic csv file to a json file
#GROUP:     5
# ELEMENTS:  a93234 - Diogo Matos
#           a83630 - Duarte Serrão
#           a932xx - Vasco Oliveira
################################################################################
import re
import sys

################################################################################
# FUNCTION:  Main body that will control the program
################################################################################


def main():
    input = sys.argv[1]
    output = sys.argv[2]
    fi = open(input, "r", encoding="UTF-8")
    fo = open(output, "w", encoding="UTF-8")

    # Getting the header
    line = fi.readline()
    header = getFields(line)

    content = readContent(fi, header)

    dicToJson(fo, content)

    fi.close()
    fo.close()
    return

################################################################################
# FUNCTION:  Regex pattern if we solved it without ply.lex
################################################################################

def getRegex():
    # Textqualified -> in between double quotes
    textqualified = r'(?P<TEXTQUALIFIED>")?'
    # if it found the first double quote character, then it will try to find the pair
    is_textqualified = r'(?(TEXTQUALIFIED)")'

    # Inside 'raw' fields we can't have commas or new lines
    # We can have spaces in between words
    raw_field = r'( *[^,\n ]+)+'

    # Fields can be textqualified (between double quotes) or raw
    # If the group TEXTQUALIFIED exists, then we will accept whatever
    field = r'(?P<FIELD>(?(TEXTQUALIFIED).*?|' + raw_field + '))'
    # A field can't have spaces before or after it's content, so we seperate it from
    # the FIELD group.
    # We could just use the .strip() function, but this way we can use regex
    spaces = r' *'
    # The comma is optional, since the last one doesnt have it
    comma = r',?'
    
    return spaces + textqualified + field + is_textqualified + spaces + comma

################################################################################
# FUNCTION:  Getting fields with regex pattern
################################################################################

def getFields(line):
    regex_pattern = getRegex()

    matches = re.finditer(regex_pattern, line)
    fields = []

    # Getting all the fields
    for match_obj in matches:
        fields.append(match_obj.group('FIELD'))
    return fields

################################################################################
# FUNCTION:  Getting each entry and put it in a dictionary
################################################################################


def readContent(file, header):
    dic = []
    for line in file:
        fields = getFields(line)
        dic.append(dict(zip(header, fields)))
    return dic

################################################################################
# FUNCTION:  Converting the list of dictionaries to a json file
################################################################################


def dicToJson(fo, content):
    i = 0
    # Begining of json file
    print("{", file=fo)

    for dic in content:
        print("\t\"entry" + str(i) + "\": {", file=fo)
        printKeys(dic, fo)

        # If it is the end of the dictionary list, we just end the entry
        if list(content)[-1] == dic:
            print("\t}", file=fo)
        # If its not, we go to the next entry
        else:
            print("\t},", file=fo)
            i = i + 1

    # End of json file
    print("}", file=fo)
    return

################################################################################
# FUNCTION:  Print to the file every entry of the dictionary
################################################################################


def printKeys(dic, fo):
    for entry in dic.keys():
        line = "\t\t\"" + str(entry) + "\": \"" + str(dic[entry]) + "\""
        # If it is NOT the end of the dictionary, we need a comma to let it know there are more keys
        if list(dic)[-1] != entry:
            line += ","
        print(line, file=fo)
    return


main()
