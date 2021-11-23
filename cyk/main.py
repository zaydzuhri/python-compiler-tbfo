from cyk import cyk_parse, clean_tokenized, get_cnf
from tokenizer import file_tokenizer
import argparse

parser = argparse.ArgumentParser(description='Parse a python file with CYK.')
parser.add_argument('file_path', metavar='fp', type=str, help='Python file path.')
args = parser.parse_args()

if __name__ == "__main__":
    file_path = args.file_path
    tokenized = file_tokenizer(file_path)
    clean = clean_tokenized(tokenized)

    result = cyk_parse(clean, get_cnf('txt/cnf.txt'))

    print("Syntax is correct!" if result else "Syntax is wrong.")