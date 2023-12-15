# 소문자 대문자 숫자 공백

while True:
    try:
        string = input()
        result = [0 for _ in range(4)]
        for char in string:
            if char.isdigit():
                result[2] += 1
            if char.islower():
                result[0] += 1
            if char.isupper():
                result[1] += 1
            if char == " ":
                result[3] += 1
        print(result[0], result[1], result[2], result[3])
    except EOFError:
        break