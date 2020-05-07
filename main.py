def load_data(INPUTFILE):
    fileHandler=open(INPUTFILE,'r')
    codeString = ""
    for line in fileHandler: #opens file
        codeString += str(line)
    return codeString

