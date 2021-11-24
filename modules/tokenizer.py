import re

def filter_unnecessary_tokens(tokens: list) -> list:
    # remove string with zero length and remove whitespace
    result = filter(len, tokens)
    whitespace = re.compile(r'[\r\t\v ]+')
    result = list(filter(lambda x: not whitespace.match(x), result))
    return result


def file_tokenizer(file_name: str) -> list:
    with open(file_name, 'r') as f:
        contents = f.read()

    delimiters = [
        r'\+', r'\-', r'\*', '/', r'\*\*', '//', '%', '<', '>', '<=', '>=',
        '==', '!=', r'\(', r'\)', r'\{', r'\}', ';', ':', ',', '=', '\'',
        '\"', ':=', '\n', ' ', '\t', '.', r'\[', r'\]'
    ]

    res = re.split('([' + r"".join(delimiters) + '])', contents)

    return filter_unnecessary_tokens(res)


if __name__ == "__main__":
    print(file_tokenizer("examples/inputAcc.py"))
