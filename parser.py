import ply.yacc as Yacc #parser generator
from lexer import tokens
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s"
)


###PARSER###

def p_Func(p):
    """

        Func : DEF CANVAS Canvas DEF STRUCTURES Structure DEF DRAW Draw
    """

# def p_Def(p):
#     '''
#         Def : Exp
#     '''
def p_Bool(p):
    '''
        Bool : true
             | false
    '''
def p_Canvas(p):
    '''
        Canvas : LParenthesis Dimensions BgColor Position RParenthesis
    '''

def p_Dimensions(p):
    '''
        Dimensions : DIMENSIONS Colon LessThan Int Comma Int GreaterThan
    '''
def p_BgColor(p):
    '''
        BgColor : BGCOLOR Colon Color
    '''
def p_Color(p):
    """
        Color : BLACK
              | BLUE
              | YELLOW
              | RED
              | GREEN
              | WHITE
    """
def p_Position(p):
    '''
        Position : POSITION Colon LessThan Int Comma Int GreaterThan
    '''
def p_Structure (p):
    '''
        Structure : LParenthesis Struct Data RParenthesis
    '''

def p_Struct(p):
    '''
        Struct : STRUCT Colon DS
    '''
def p_DS(p):
    """
        DS : QUEUE
           | STACK
           | ARRAY
           | DLL
           | BST
    """
def p_Data(p):
    '''
        Data : DATA Colon LessThan Type Comma LBracket Arr RBracket GreaterThan
    '''

def p_Type(p):
    '''
        Type : INT
    '''
def p_Arr(p):
    '''
    Arr : Int
        | Arr Comma Int
    '''
def p_Draw(p):
    '''
    Draw : LParenthesis PenSize PenColor RParenthesis
    '''
# def p_Obj(p):
#     '''
#     Obj : OBJ Colon Exp
#     '''
def p_PenSize(p):
    '''
    PenSize : PENSIZE Colon Int PX
    '''
def p_PenColor(p):
    '''
    PenColor : PENCOLOR Colon Color
    '''
def p_Animation(p):
    """
    Animation : ANIMATION Colon Bool
    """
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