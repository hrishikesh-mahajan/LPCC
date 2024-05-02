class Assembler:
    def __init__(self):
        self.symbol_table = {}
        self.literal_table = []
        self.pool_table = []
        self.location_counter = 0
        self.pool_start = 0

    def first_pass(self, source_code):
        for line in source_code:
            line = line.strip()
            if line.startswith("START"):
                self.location_counter = int(line.split()[1])
            elif line.startswith("END"):
                self.process_ltorg()
                break
            elif line:
                if "='" in line:
                    self.process_literal(line)
                elif line.startswith("LTORG"):
                    self.process_ltorg()
                else:
                    self.process_label(line)
                self.process_instruction(line)

    def process_instruction(self, line):
        if not line.startswith("DS") and not line.startswith("LTORG"):
            self.location_counter += 1

    def process_label(self, line):
        parts = line.split()
        if len(parts) > 2 and parts[1] == "DS":
            self.symbol_table[parts[0]] = self.location_counter
        elif len(parts) > 1 and parts[0] not in [
            "MOVER",
            "MOVEM",
            "ADD",
            "SUB",
            "COMP",
            "BC",
            "READ",
            "PRINT",
            "STOP",
        ]:
            self.symbol_table[parts[0]] = self.location_counter

    def process_literal(self, line):
        literal = line.split("='")[1].split("'")[0]
        self.literal_table.append([literal, ""])

    def process_ltorg(self):
        for i in range(self.pool_start, len(self.literal_table)):
            self.literal_table[i][1] = str(self.location_counter)
            self.location_counter += 1
        self.pool_table.append(self.pool_start)
        self.pool_start = len(self.literal_table)

    def generate_tables(self):
        print("Symbol Table:")
        print("Label\tAddress")
        for label, address in self.symbol_table.items():
            print(f"{label}\t{address}")

        print("\nLiteral Table:")
        print("Literal\tAddress")
        for literal, address in self.literal_table:
            print(f"{literal}\t{address}")

        print("\nPool Table:")
        for address in self.pool_table:
            print(address)

    def assemble(self, source_code):
        self.first_pass(source_code)
        self.generate_tables()


def main():
    source_code = [
        "START 100",
        "READ A",
        "MOVER AREG, ='1'",
        "MOVEM AREG, B",
        "MOVER BREG, ='6'",
        "ADD AREG, BREG",
        "COMP AREG, A",
        "BC GT, LAST",
        "LTORG",
        "NEXT SUB AREG, ='1'",
        "MOVER CREG, B",
        "ADD CREG, ='8'",
        "MOVEM CREG, B",
        "PRINT B",
        "LAST STOP",
        "A DS 1",
        "B DS 1",
        "END",
    ]

    assembler = Assembler()
    assembler.assemble(source_code)


if __name__ == "__main__":
    main()
