from ply import lex as lex
import sys

tokens = [
    'Character', 'Digit', 'LParenthesis', 'RParenthesis',
    'LBracket', 'RBracket','Comma', 'Colon',
    'Dot', 'Apostrophe', 'Equals',
    'LessThan', 'GreaterThan', 'Or',
]

reservedWords = {
        'true' : 'true',
        'false' : 'false',
        'stack' : 'STACK',
        'queue' : 'QUEUE',
        'arrayStructure' : 'ARRAY',
        'doublyLinkedList' : 'DLL',
        'binarySearchTree' : 'BST',
        'number' : 'NUMBER',
        'id' : 'ID',
}

tokens += list(reservedWords.values())

t_LParenthesis = r'\('
t_RParenthesis = r'\)'
t_LBracket = r'\['
t_RBracket = r'\]'
t_Colon  = r'\:'
t_Comma = r'\,'
t_Dot = r'\.'
t_Apostrophe = r'\''
t_Equals = r'\='
t_LessThan = r'\<'
t_GreaterThan = r'\>'
t_Character = r'[a-zA-Z\_]'
t_Digit = r'[0-9]'

t_ignore  = ' \t'

def t_RESERVED(t):
    r'true | false | stack | queue | arrayStructure | doublyLinkedList | binarySearchTree | number | id'
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