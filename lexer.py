from ply import lex as lex
import sys

tokens = [
    'Character', 'Digit', 'LParentesis', 'RParentesis',
    'LBracket', 'RBracket', 'LCurlyBrace', 'RCurlyBrace',
    'Comma', 'Colon',
    'Dot', 'Apostrophe', 'Equals',
    'LessThan', 'GreaterThan', 'Or', 'And', 'Exp', 'Type',
]

reservedWords = {
        'def' : 'DEF',
        'canvas' : 'CANVAS',
        'dimensions' : 'DIMENSIONS',
        'backgroundColor' : 'BGCOLOR',
        'draggable' : 'DRAGGABLE',
        'position' : 'POSITION',
        'structure' : 'STRUCTURE',
        'struct' : 'STRUCT',
        'data' : 'DATA',
        'draw' : 'DRAW',
        'object' : 'OBJ',
        'stroke' : 'STROKE',
        'strokeColor' : 'STROKECOLOR',
        'true' : 'TRUE',
        'false' : 'FALSE',
        'type': 'TYPE',
        'intParam' : 'INT',
        'arrayParam' : 'ARR',
        'stack' : 'STACK',
        'queue' : 'QUEUE',
        'arrayStructure' : 'ARRAY',
        'doublyLinkedList' : 'DLL',
        'binarySearchTree' : 'BST',
        'number' : 'NUMBER',
        'id' : 'ID',
}

tokens += list(reservedWords.values())

t_LParentesis = r'\('
t_RParentesis = r'\)'
t_LBracket = r'\['
t_RBracket = r'\]'
t_LCurlyBrace = r'\{'
t_RCurlyBrace =  r'\}'
t_Colon  = r'\:'
t_Comma = r'\,'
t_Dot = r'\.'
t_Apostrophe = r'\''
t_Equals = r'\='
t_LessThan = r'\<'
t_GreaterThan = r'\>'
t_And = r'\&'
t_Or = r'\|'
t_Character = r'[a-zA-Z\_]'
t_Digit = r'[0-9]'

t_ignore  = ' \t'

def t_RESERVED(t):
    r'def | canvas | dimensions | backgroundColor | draggable | position | structure | struct | data | draw | object | stroke | strokeColor | true | false | type | intParameter | arrayParameter | structureClass | stack | queue | arrayStructure | doublyLinkedList'
    if t.value in reservedWords:
        t.type = reservedWords[t.value]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print('Illegal characters!')
    t.lexer.skip(1)


test = '''
def canvas(
    dimensions:<400,400>
    bgColor:Color.BLACK
    draggable:false
    position:<500,700>
)

def structures(
    struct:Struct.BINARY_TREE
    data:<tyer='int', arr=[10,7,5,3,1,0]>
)

def draw(
    obj:structure
    stroke:10px
    strokeColor:Color.WHITE
) '''

lexer = lex.lex()

lexer.input(test)


while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)