def solution(new_id = '...!@BaT#*..y.abcdefghijklm'):
    answer = ''
    new_id = new_id.lower()
    new_st = new_id[:]
    new_id = ''
    for item in new_st:
        if item.isdecimal() or item .isalpha():
            new_id += item
        elif item == '_' or item == '-' or item == '.':
            new_id += item
    while True:
        print(new_id)
        if '..' in new_id:
            new_id = new_id.replace('..','.')
        if '..' not in new_id:
            break
    while True:
        change = False
        if len(new_id) != 0 and new_id[0] == '.':
            new_id = new_id[1:]
            change = True
        if len(new_id) != 0 and new_id[len(new_id) - 1] == '.':
            new_id = new_id[:-1]
            change = True
        if new_id == '':
            new_id = 'a'
            change = True
        if len(new_id) >= 16:
            new_id = new_id[:15]
            change = True
        if len(new_id) <= 2:
            new_id += new_id[-1]
            new_id += new_id[-1]
            new_id += new_id[-1]
            new_id = new_id[:3]
            change = True
        if change == False:
            break
    return new_id
