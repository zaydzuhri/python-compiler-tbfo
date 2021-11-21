import re

def filter_unnecessary_tokens(tokens: list) -> list:
    # remove string with zero length and remove whitespace
    result = filter(len, tokens)
    whitespace = re.compile(r'[\s]+')
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
        '\n', ' ', '\t'
    ]

    res = re.split('([' + r"".join(operators) + '])', contents)

    return filter_unnecessary_tokens(res)


if __name__ == "__main__":
    print(file_tokenizer("examples/inputAcc.py"))