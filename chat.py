# 读取档案
def read_file(file_name):
    new_chat_list = []
    with open(file_name, 'r', encoding="utf-8-sig") as f:
        for line in f:
            new_chat_list.append(line.strip())
    return new_chat_list

# 转换档案
def convert(new_chat_list):
    person = None
    new = []
    for line in new_chat_list:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' + line)
    return new

# 写入档案
def write_to_file(file_name, lines):
    with open(file_name, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

# main
def main():
    new_chat_list = read_file('input.txt')
    new_chat_list = convert(new_chat_list)
    write_to_file('output.txt', new_chat_list)

if __name__ == '__main__':
    main()