from ply import lex as lex
import sys
from main import load_data

tokens = [
    'Digit', 'LParenthesis', 'RParenthesis',
    'LBracket', 'RBracket', 'Comma', 'Colon',
    'LessThan', 'GreaterThan', 'Integer', 'Array'
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
    'funcStructures' : 'STRUCTUREOP',
    'struct' : 'STRUCT',
    'data' : 'DATA',
    'int' : 'INT',
    'penSize' : 'PENSIZE',
    'px': 'PX',
    'penColor' : 'PENCOLOR',
    'animation' : 'ANIMATION',
}

colors = {
    'BLACK' : 'BLACK',
    'BLUE' : 'BLUE',
    'YELLOW' : 'YELLOW',
    'RED' : 'RED',
    'GREEN' : 'GREEN',
    'WHITE' : 'WHITE',
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
    r'true | false | def | canvas | structures | draw | dimensions | bgColor | position | funcStructures | struct | data | int | penSize  | px | penColor | animation'
    if t.value in reservedWords:
        t.type = reservedWords[t.value]
    return t

def t_COLORS(t):
    r'BLACK | BLUE | YELLOW | RED | GREEN | WHITE'
    if t.value in colors:
        t.type = colors[t.value]
    return t

def t_DATASTRUCTURES(t):
    r'queue | stack | arrayStructure | doublyLinkedList | binarySearchTree'
    if t.value in dataStructures:
        t.type = dataStructures[t.value]
    return t

def t_Integer(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_Array(t):
    r'\[[0-9,]+[0-9]*\]'
    temp = t.value
    temp = temp.split(',')

    for i in temp:
        if(i.find('[') == 0):
            temp[temp.index(i)] = i.replace('[', '')
        elif(i.find(']') == 1):
            temp[temp.index(i)] = i.replace(']', '')

    temp_list = list()

    for i in temp:
        temp_list.append(int(i))

    t.value = temp_list
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print('Illegal characters!')
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input(load_data("test.davis"))

while True:
    tok = lexer.token()
    # print(tok)
    if not tok:
        break
