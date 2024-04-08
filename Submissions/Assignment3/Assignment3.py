# symbol table generation
def getClas(operator):
    clas = 0
    for i in EMOT:
        if i[0] == operator:
            clas = i[1]
    return clas


file = open("ASSEMBLY CODE.txt", "r")
lines = file.readlines()
tokens = []
for line in lines:
    tokens.append(line.split())
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
lc = int(tokens[0][-1])
lcList = []
for i in tokens:
    lcList.append(lc)
    length = len(tokens)
    if length == 4:
        operator = i[1]
        clas = getClas(operator)
        if clas == 1:
            lc += 1
        elif clas == 2:
            if operator == "DS":
                incr = int(i[-1])
                lc += incr
            else:
                lc += 1
    else:
        if "DS" in i or "DC" in i:
            operator = i[1]
        else:
            operator = i[0]
        clas = getClas(operator)
        if clas == 1:
            lc += 1
        elif clas == 2:
            if operator == "DS":
                incr = int(i[-1])
                lc += incr
            else:
                lc += 1
        elif clas == 3:
            pass

n = len(tokens)
st = []
entered_symbol = []
entered_label = []
for i in tokens:
    length = len(i)
    if length == 4:
        label = i[0]
        if label not in entered_label:
            index = tokens.index(i)
            lc = lcList[index]
            st.append([label, lc])
            entered_label.append(label)
        symbol = i[-1]
        if symbol[0] != "=":
            if symbol not in entered_symbol:
                st.append([symbol, 0])
                entered_symbol.append(symbol)
            if "DS" in i or "DC" in i:
                operator = i[2]
            else:
                operator = i[1]
            if operator == "DS":
                incr = int(i[-1])
                for s in st:
                    index = tokens.index(i)
                    lc = lcList[index]
                    if s[0] == symbol:
                        s[1] = lc
            else:
                for m in EMOT:
                    if m[0] == operator:
                        clas = m[1]
                if clas == 1:
                    pass
    else:
        if "DS" in i or "DC" in i:
            operator = i[1]
        else:
            operator = i[0]
        for m in EMOT:
            if m[0] == operator:
                clas = m[1]
        if clas == 3:
            pass
        elif clas == 1:
            symbol = i[-1]
            if (
                symbol not in entered_symbol
                and symbol not in entered_label
                and symbol[0] != "="
            ):
                st.append([symbol, 0])
                entered_symbol.append(symbol)
        elif clas == 2:
            # DC and DS
            symbol = i[0]
            index = tokens.index(i)
            lc = lcList[index]
            for s in st:
                if s[0] == symbol and symbol not in entered_label and symbol[0] != "=":
                    s[1] = lc
                    if operator == "DS":
                        pass
                    else:
                        pass

for i in st:
    print(i)
