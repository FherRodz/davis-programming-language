import ply.yacc as Yacc #parser generator
from lexer import tokens
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s"
)


### PARSER###

def p_EXP(p):
    '''
        Exp : Character
            | Character Exp
    '''
def p_Def(p):
    '''
        Def : Exp
    '''
def p_Bool(p):
    '''
        Bool : true
             | false
    '''
def p_Canvas(p):
    '''
        Canvas : LParenthesis Dimensions Bgcolor Draggable Position RParenthesis
    '''


def p_Draggable(p):
    '''
        Draggable : Bool

    '''
def p_Dimensions(p):
    '''
        Dimensions : Colon LessThan Int Comma Int GreaterThan
    '''
def p_Bgcolor(p):
    '''
        Bgcolor : Colon Exp Dot Exp
    '''
def p_Position(p):
    '''
        Position : Dimensions
    '''
def p_Structure (p):
    '''
        Structure : LParenthesis Struct Data RParenthesis
    '''

def p_Struct(p):
    '''
        Struct : Bgcolor
    '''
def p_Data(p):
    '''
        Data : Colon LessThan Type Comma Arr GreaterThan
    '''

def p_Type(p):
    '''
        Type : Equals Apostrophe Exp Apostrophe
    '''
def p_Arr(p):
    '''
    Arr : Equals LBracket Int Comma RBracket
        | Equals LBracket Arr RBracket
    '''
def p_Draw(p):
    '''
    Draw : LParenthesis Obj Stroke Strokecolor RParenthesis
    '''
def p_Obj(p):
    '''
    Obj : Colon Exp
    '''
def p_Stroke(p):
    '''
    Stroke : Colon Int
           | Stroke Exp
    '''
def p_Strokecolor(p):
    '''
    Strokecolor : Colon Bgcolor
    '''
def p_Int(p):
    '''
    Int : Digit
        | Digit Int
    '''

def p_error(p):
    print("Syntax error in input!")


parser = Yacc.yacc()
log = logging.getLogger()


while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s, debug=log)