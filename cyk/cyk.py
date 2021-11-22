from nfa import accepts, nfa
from tokenizer import file_tokenizer

def get_cnf(file_path):
    lines = open(file_path).read().splitlines()
    for i in range(len(lines)):
        j = 0
        while lines[i][j] == ' ':
            j += 1
        lines[i] = lines[i][j:]

    rules = []
    i = 0
    j = 0
    while i < len(lines):
        if lines[i][0] != '|':
            if j < len(lines) - 1: j += 1 
            while lines[j][0] == '|':
                j += 1
            if j == i + 1 or j == i:
                rules.append(lines[i])
            else:
                rules.append(' '.join(lines[i:j]))
        i += 1
        j = i
    
    cnf_dict = {}

    for rule in rules:
        production = rule.split(" -> ")
        left_side = production[0]
        right_side = production[1].split(" | ")
        for i in range(len(right_side)):
            if ' ' in right_side[i]: right_side[i] = right_side[i].split(" ")
        cnf_dict.update({left_side : right_side})
    
    return cnf_dict

def clean_tokenized(tokenized):
    reserved_terms = open("txt/reserved_terms.txt").read().split(' ')
    inOneLiner = False
    openString = False
    closeString = False
    inString = False

    for i in range(len(tokenized)):
        if tokenized[i] == '"' or tokenized[i] == "'":
            if not openString and not inString:
                openString = True
                inString = True
            elif inString:
                openString = False
                inString = False
        elif tokenized[i] == '#':
            inOneLiner = True
            inString = True
        elif tokenized[i] == '\n':
            if inString and not inOneLiner:
                tokenized[i] = 'strcontent'
            if inOneLiner:
                    inOneLiner = False
                    inString = False
        elif (inString or inOneLiner):
                tokenized[i] = 'strcontent'
                openString = False
        
        if not inString and not inOneLiner and not tokenized[i] in reserved_terms:
            if tokenized[i] == '\n':
                tokenized[i] = 'newline'
            elif tokenized[i].isnumeric():
                tokenized[i] = 'number'
            elif tokenized[i] == 'True':
                tokenized[i] = 'true'
            elif tokenized[i] == 'False':
                tokenized[i] = 'false'
            elif accepts(nfa, 0, {1}, tokenized[i]):
                tokenized[i] = 'variable'
            
    return tokenized
        

def cyk_parse(tokenized, grammar):
    str_length = len(tokenized)
    grammar_length = len(grammar)
    table = [[[] for i in range(str_length)] for j in range(str_length)]

    for i in range(str_length):
        for left_side in grammar.keys():
            if tokenized[i] in grammar[left_side]:
                table[i][i].append(left_side)

    for length in range(2, str_length + 1):
        for start in range(0, str_length - length + 1):
            stop = start + length - 1
            for i in range(start, stop):
                for left_side in grammar.keys():
                    if isinstance(grammar[left_side], list):
                        for right_terms in grammar[left_side]:
                            if right_terms[0] in table[start][i] and right_terms[1] in table[i+1][stop]:
                                table[start][stop].append(left_side)
    i = 0
    for elmt in table[0]:
        print(i, elmt)
        i += 1
    return 'S' in table[0][str_length - 1]

if __name__ == "__main__":
    tokenized = file_tokenizer("examples/inputAcc.py")
    clean = clean_tokenized(tokenized)
    i = 0
    for token in clean:
        print(i, token)
        i += 1
    print(cyk_parse(clean, get_cnf('txt/cnfweb.txt')))
    