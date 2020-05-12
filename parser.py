import ply.yacc as Yacc #parser generator
from lexer import tokens
import logging
from intermediate import queue,array,doublyLinkedList,stack
from main import load_data

logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s"
)


###PARSER###

funcDic = dict()

def p_Func(p):
    '''
        Func : DEF CANVAS Canvas DEF STRUCTURES Structure DEF DRAW Draw
    '''
    funcDic[p[2]] = p[3]
    funcDic[p[5]] = p[6]
    funcDic[p[8]] = p[9]

def p_Bool(p):
    '''
        Bool : true
             | false
    '''
    p[0] = p[1]

def p_Canvas(p):
    '''
        Canvas : LParenthesis Dimensions BgColor Position RParenthesis
    '''
    p[0] = [p[2], p[3], p[4]]

def p_Dimensions(p):
    '''
        Dimensions : DIMENSIONS Colon LessThan Integer Comma Integer GreaterThan
    '''
    p[0] = (p[4], p[6])

def p_BgColor(p):
    '''
        BgColor : BGCOLOR Colon Color
    '''
    p[0] = p[3]

def p_Color(p):
    """
        Color : BLACK
              | BLUE
              | YELLOW
              | RED
              | GREEN
              | WHITE
    """
    p[0] = p[1]


def p_Position(p):
    '''
        Position : POSITION Colon LessThan Integer Comma Integer GreaterThan
    '''
    p[0] = (p[4], p[6])

def p_Structure(p):
    '''
        Structure : LParenthesis Struct Data RParenthesis
                  
    '''
    p[0] = [p[2], p[3]]

def p_Struct(p):
    '''
        Struct : STRUCT Colon DS
    '''
    p[0] = p[3]

def p_DS(p):
    """
        DS : QUEUE
           | STACK
           | ARRAY
           | DLL
           | BST
    """
    p[0] = p[1]

def p_Data(p):
    '''
        Data : DATA Colon LessThan Type Comma Arr GreaterThan
    '''
    p[0] = (p[4], p[6])

def p_Type(p):
    '''
        Type : INT
    '''
    p[0] = p[1]

def p_Arr(p):
    '''
    Arr : Array
    '''
    p[0] = p[1]

def p_Draw(p):
    '''
    Draw : LParenthesis PenSize PenColor Animation RParenthesis
         | LParenthesis PenSize PenColor Animation StructureOp RParenthesis
    '''
    if p[5] == "STRUCTUREOP":
        p[0] = [p[2], p[3], p[4], funcDic['structures']]
    else:
        p[0] = [p[2], p[3], p[4]]

def p_StructureOp(p):
    '''
    StructureOp : STRUCTUREOP
                | 
    '''

def p_PenSize(p):
    '''
    PenSize : PENSIZE Colon Integer PX
    '''
    p[0] = (p[3], p[4])

def p_PenColor(p):
    '''
    PenColor : PENCOLOR Colon Color
    '''
    p[0] = p[3]

def p_Animation(p):
    """
    Animation : ANIMATION Colon Bool
    """
    p[0] = p[3]

def p_Int(p):
    '''
    Int : Digit
        | Digit Integer
    '''
    p[0] = p[1]

def p_error(p):
    print("Syntax error in input!")


parser = Yacc.yacc()
log = logging.getLogger()

while True:
    try:
        s = load_data('test.davis')
    except EOFError:
        break
    parser.parse(s, debug=log)
    break


################################
##CONNECTING INTERMIDEATE CODE##
################################
if len(funcDic['draw']) == 3:
    structureDimen = funcDic['canvas'][0]   # dimensions of the screen
    bgColor = funcDic['canvas'][1].lower()
    strucPos = funcDic['canvas'][2]         # tuple (x,y) x=pixels from left fo screen, y=pixels from top of screen
    structure=funcDic['structures'][0]      # type of data structures
    structureValue=funcDic['structures'][1] # data (list)
    penSize = funcDic['draw'][0]            # (int, str)
    penColor = funcDic['draw'][1].lower()
    structureAni = funcDic['draw'][2]       # animation
else:
    structureDimen = funcDic['canvas'][0]
    bgColor = funcDic['canvas'][1].lower()
    strucPos = funcDic['canvas'][2]
    structure= funcDic['draw'][4][0]
    structureValue=funcDic['draw'][4][1]
    penSize = funcDic['draw'][0] 
    penColor = funcDic['draw'][1].lower()
    structureAni = funcDic['draw'][2]


# In our language the syntax is lowercase but in and string
# but python uses a difrent syntax here we change that
if structureAni == 'true':
    structureAni = True
else:
    structureAni = False

if structure=='queue':
    queueValue=structureValue[1]
    queue=queue.Queue(queueValue, structureAni, structureDimen, bgColor, penColor, penSize, strucPos)
    queue.draw()
    
elif structure=='arrayStructure':
    arrayVal=structureValue[1]
    array=array.myArray(arrayVal, structureAni, structureDimen, bgColor, penColor, penSize, strucPos)
    array.draw()
    
elif structure=="stack":
    stackVal=structureValue[1]
    stack=stack.myStack(stackVal, structureAni, structureDimen, bgColor, penColor, penSize, strucPos)
    stack.draw()

elif structure == "doublyLinkedList":
    dllVal=structureValue[1]
    dll=doublyLinkedList.DoublyLinkedList(dllVal, structureAni, structureDimen, bgColor, penColor, penSize, strucPos)
    # for val in dllVal:
    #     dll.add(val)
    dll.draw()

else:
    print("The disired Structured is not implemented please contact the developers")


# {'canvas': [(400, 400), 'BLACK', (500, 700)],
# 'structures': ['queue', ('int', ['10', '7', '5', '3', '1', '0'])],
# 'draw': [(10, 'px'), 'WHITE', 'true']}
