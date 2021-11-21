import re

def filter_unnecessary_tokens(tokens):
    # remove string with zero length
    result = filter(len, tokens)  
    # remove whitespaces
    whitespace = re.compile(r'[\t\r\v\f  ]+')
    result = list(filter(lambda x: not whitespace.match(x), result))
    return result


def file_tokenizer(file_name: str) -> list:
    file = open(file_name, "r")
    contents = file.read()
    file.close()

    operators = [
        r'\+', r'\-', r'\*', '/', r'\*\*', '//', '%',                
        '<', '>', '<=', '>=', '==', '!=',
        r'\(', r'\)', r'\{', r'\}', ';', ':', ',', '=', '\'', '\"', 
        '\n', ' '
    ]

    print(list(filter(filter_unnecessary_tokens, re.split('([' + r"".join(operators) + '])', contents))))

file_tokenizer("examples/inputAcc.py")