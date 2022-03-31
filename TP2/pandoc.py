################################################################################
# NAME:       PANDOC
# PURPOSE:    Converts from one markdown to another
# GROUP:      5
# DEVELOPERS: a93234 - Diogo Matos
#             a83630 - Duarte Serrão
#             a93208 - Vasco Oliveira
################################################################################
import grammar
import sys

################################################################################
# FUNCTION:  Main body that will control the program
################################################################################
def main():
    evalError(len(sys.argv) < 3 or len(sys.argv) > 3, "pandoc <imput-file.FORMAT> <output-file.FORMAT>")
    
    input = sys.argv[1]
    #TODO Choose formats available!!
    evalError(not input.endswith("htlm"), "Formats available for input: .html, etc.")
    
    output = sys.argv[2]
    evalError(not output.endswith(".txt"), "Formats available for output: .txt, etc.")
    
    fi = open(input, "r", encoding="UTF-8")
    fo = open(output, "w", encoding="UTF-8")

    #TODO READ INPUT FILE :D
    

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

