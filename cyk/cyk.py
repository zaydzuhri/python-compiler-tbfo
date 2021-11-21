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

if __name__ == "__main__":
    print(get_cnf("cyk/cnf.txt"))
    