# literal table\
def getClas(operator):
    clas = 0
    for i in EMOT:
        if i[0] == operator:
            clas = i[1]
    return clas


EMOT = [
    ["STOP", 1, 0],
    ["ADD", 1, 1],
    ["SUB", 1, 2],
    ["MULT", 1, 3],
    ["MOVER", 1, 4],
    ["MOVEM", 1, 5],
    ["COMP", 1, 6],
    ["BC", 1, 7],
    ["DIV", 1, 8],
    ["READ", 1, 9],
    ["PRINT", 1, 10],
    ["START", 3, 1],
    ["END", 3, 2],
    ["ORIGIN", 3, 3],
    ["EQU", 3, 4],
    ["LTORG", 3, 5],
    ["DS", 2, 1],
    ["DC", 2, 2],
    ["AREG", 4, 1],
    ["BREG", 4, 2],
    ["CREG", 4, 3],
    ["DREG", 4, 4],
]
file = open("ASSEMBLY CODE.txt", "r")
lines = file.readlines()
tokens = []
for line in lines:
    tokens.append(line.split())
n = len(tokens)
lc = int(tokens[0][-1])
# print(lc)
lcList = []
for i in tokens:
    lcList.append(lc)
    length = len(tokens)
    # print("length= ", length)
    if length == 4:
        operator = i[1]
        clas = getClas(operator)
        if clas == 1:
            lc += 1
        elif clas == 2:
            if operator == "DS":
                incr = int(i[-1])
                # print("incr= ", incr)
                lc += incr
            else:
                lc += 1
        # lcList.append(lc)
    else:
        if "DS" in i or "DC" in i:
            operator = i[1]
        else:
            operator = i[0]
        clas = getClas(operator)
        # print(operator, clas)
        if clas == 1:
            lc += 1
        elif clas == 2:
            if operator == "DS":
                incr = int(i[-1])
                # print("incr= ", incr)
                lc += incr
            else:
                lc += 1
        elif clas == 3:
            pass
        # lcList.append(lc)
# print(lcList)
# print(len(lcList))

lt = []
for i in tokens:
    if i[-1][0] == "=":
        lt.append([i[-1], -1])

# print(lt)
end = lcList[-1]
for i in lt:
    i[-1] = end
    end += 1
for i in lt:
    print(i)
