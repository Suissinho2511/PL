################################################################################
# NAME:       GRAMMAR
# PURPOSE:    
# GROUP:      5
# DEVELOPERS: a93234 - Diogo Matos
#             a83630 - Duarte Serrão
#             a93208 - Vasco Oliveira
################################################################################
import ply.yacc as yacc

#TODO Terá de ser uma gramática abstrata
#TODO Começar talvez pela gramática de htlm e dps passar para abstrata?


################################################################################
# FUNCTION:  
################################################################################
def grammar(line):
    parser = yacc.yacc()
    parser.parse(line)