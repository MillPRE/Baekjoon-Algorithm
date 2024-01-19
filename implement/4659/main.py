from sys import stdin

mo = ["a","e","i","o","u"]
acceptable = ['ee', 'oo']

def containsMo(password):
    result = False
    for p in password:
        if p in mo:
            result = True
    return result

def continueSameWord(password):
    prev = password[0]
    for p in password[1:]:
        if prev == p and prev+p not in acceptable:
            return True
        prev = p
    return False

def confinueThreeMoOrJa(password):
    three = ['', password[0], password[1]]
    for p in password[2:]:
        mo_num = 0
        ja_num = 0

        three.append(p)
        three = three[1:]

        for t in three:
            if t in mo:
                mo_num += 1
            else:
                ja_num += 1
        if mo_num >= 3 or ja_num >= 3:
            return True
    return False

while True:
    line = stdin.readline().strip()

    if line == "end":
        break

    password = list(line)
    notAcceptable = False
    # check mo
    if not containsMo(password):
        notAcceptable = True
    # print("checkmo: ", notAcceptable)

    # check 연속 같은 글자
    if not notAcceptable and continueSameWord(password):
        notAcceptable = True
    # print("checkContinue: ", notAcceptable)

    # 3연속 모음 또는 3연속 자음
    if not notAcceptable and len(password) >= 3 and confinueThreeMoOrJa(password):
        notAcceptable = True
    # print("checkContinueTree: ", notAcceptable)


    if notAcceptable:
        print(f'<{line}> is not acceptable.')
    else:
        print(f'<{line}> is acceptable.')