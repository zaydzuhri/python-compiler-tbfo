from dfa import accepts, dfa_transitions
from tokenizer import file_tokenizer

regexes = {
    r'[A-z0-9]*' : ["string"],
    r'[0-9]*' : ["number"],
    r'[A-Za-z_][A-Za-z_0-9]*' : ["variable"],
}

def get_cnf(file_path):
    rules = open(file_path).read().split('\n')
    cnf_dict = {}

    for rule in rules:
        production = rule.split(" -> ")
        left_side = production[0]
        right_side = production[1].split(" | ")
        for i in range(len(right_side)):
            if ' ' in right_side[i]: right_side[i] = right_side[i].split(" ")
        cnf_dict.update({left_side : right_side})
    
    return cnf_dict
    
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

    print(table)
    return 'S' in table[0][str_length - 1]

if __name__ == "__main__":
    tokenized = file_tokenizer("cyk/test2.py")
    print(tokenized)
    print(cyk_parse(tokenized, get_cnf("cyk/cnf.txt")))