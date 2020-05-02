from ply import lex as lex
import sys

tokens = [
    'Digit', 'LParenthesis', 'RParenthesis',
    'LBracket', 'RBracket', 'Comma', 'Colon',
    'LessThan', 'GreaterThan',
]

reservedWords = {
        'true' : 'true',
        'false' : 'false',
        'def' : 'DEF',
        'canvas' : 'CANVAS',
        'structures' : 'STRUCTURES',
        'draw' : 'DRAW',
        'dimensions' :  'DIMENSIONS',
        'bgColor' : 'BGCOLOR',
        'position' : 'POSITION',
        'struct' : 'STRUCT',
        'data' : 'DATA',
        'int' : 'INT',
        'penSize' : 'PENSIZE',
        'px': 'PX',
        'penColor' : 'PENCOLOR',


}

colors = {
    'black' : 'BLACK',
    'blue' : 'BLUE',
    'yellow' : 'YELLOW',
    'red' : 'RED',
    'green' : 'GREEN',
    'white' : 'WHITE',
}

dataStructures = {
    'queue' : 'QUEUE',
    'stack' : 'STACK',
    'arrayStructure': 'ARRAY',
    'doublyLinkedList': 'DLL',
    'binarySearchTree': 'BST',
}


tokens += list(reservedWords.values())
tokens += list(colors.values())
tokens += list(dataStructures.values())

t_LParenthesis = r'\('
t_RParenthesis = r'\)'
t_LBracket = r'\['
t_RBracket = r'\]'
t_Colon  = r'\:'
t_Comma = r'\,'
t_LessThan = r'\<'
t_GreaterThan = r'\>'
t_Digit = r'[0-9]'

t_ignore  = ' \t'

def t_RESERVED(t):
    r'true | false | def | canvas | structures | draw | dimensions | bgColor | position | struct | data | int | penSize  | px | penColor'
    if t.value in reservedWords:
        t.type = reservedWords[t.value]
    return t

def t_COLORS(t):
    r'black | blue | yellow | red | green | white'
    if t.value in colors:
        t.type = colors[t.value]
    return t

def t_DATASTRUCTURES(t):
    r'queue | stack | arrayStructure | doublyLinkedList | binarySearchTree'
    if t.value in dataStructures:
        t.type = dataStructures[t.value]
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
    bgColor:black
    position:<500,700>
)

def structures(
    struct:queue
    data:<int, [10,7,5,3,1,0]>
)

def draw(
    penSize:10px
    penColor:white
) '''

lexer = lex.lex()
lexer.input(test)


while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)