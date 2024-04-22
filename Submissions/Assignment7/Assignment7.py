file = open("Macro Assembly Code.asm")

lines = file.readlines()

tokenized_lines = []

for line in lines:
    tokens = line.split()
    tokenized_lines.append(tokens)

MNTP = 0
MDTP = 0
# Macro name, MDT pointer
MNT = []
# Definition
MDT = []
# [[arg1, #1, ]]
ALA = []


def formatString(word):
    return word.split(",")[0]


def prepALA(parameters):
    d = {}
    for i in range(len(parameters)):
        d[parameters[i]] = "#" + str(i + 1)
    return d


def formatLine(ALA, line):
    parameters = list(ALA.keys())
    for i in range(len(line)):
        if line[i] in parameters:
            line[i] = ALA[line[i]]
    return line


entry = 0
total_lines = len(tokenized_lines)
for line in tokenized_lines:
    for entry in range(len(line)):
        line[entry] = formatString(line[entry])
entry = 0
ALAPointer = 0
while entry < total_lines:
    line = tokenized_lines[entry]
    if line[0] == "MACRO":
        print(line)
        MNT.append([line[1], MDTP])
        MDT.append(line)
        MDTP += 1
        ALA = prepALA(line[2:])
        ALAPointer += 1
        print("ALA ", ALAPointer)
        for z in ALA:
            print(z, ALA[z])
        print()
        j = entry + 1
        line = tokenized_lines[j]
        while j < total_lines and line[0] != "MEND":
            j += 1
            line = tokenized_lines[j]
            l = formatLine(ALA, line)
            MDT.append(l)
            MDTP += 1
        entry = j
    elif line[0] == "MEND":
        entry += 1
        MDTP += 1
        MNTP += 1
    else:
        entry += 1

print("MNT")

for entry in MNT:
    print(entry)
print("\nMDT")

for entry in MDT:
    print(entry)
