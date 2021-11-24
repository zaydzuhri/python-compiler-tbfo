from modules.cyk import cyk_parse, clean_tokenized, get_cnf
from modules.tokenizer import file_tokenizer
import argparse

parser = argparse.ArgumentParser(description='Parse a python file with CYK.', usage= "py main.py <input program .py>")
parser.add_argument('file_path', metavar='fp', type=str, help='Python file path.')
args = parser.parse_args()

if __name__ == "__main__":
    file_path = "input/" + args.file_path
    tokenized = file_tokenizer(file_path)
    clean = clean_tokenized(tokenized)
    raw = file_tokenizer(file_path)

    print("\nChecking syntax of " + args.file_path + "...")

    result, error_line = cyk_parse(raw, clean, get_cnf('modules/grammar/cnf.txt'))

    print("Syntax is correct!" if result else ("Syntax is wrong. Error at line "+str(error_line)))
    print()