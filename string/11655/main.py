plainText = input()
result = ""
for i in range(len(plainText)):
    if plainText[i] == " ":
        result += plainText[i]
    if plainText[i].isdigit():
        result += plainText[i]
    if plainText[i].isupper():
        newOrd = ord(plainText[i])+13
        if newOrd <= ord('Z'):
            result += chr(newOrd)
        else:
            result += chr(ord('A') + (newOrd - ord('Z'))-1)
    if plainText[i].islower():
        newOrd = ord(plainText[i])+13
        if newOrd <= ord('z'):
            result += chr(newOrd)
        else:
            result += chr(ord('a') + (newOrd - ord('z'))-1)

print(result)