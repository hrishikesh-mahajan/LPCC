class ThreeAddressGenerator:
    def __init__(self):
        self.temp_count = 0
        self.code = []

    def precedence(self, op):
        if op == "+" or op == "-":
            return 1
        elif op == "*" or op == "/":
            return 2
        else:
            return 0

    def infix_to_postfix(self, expression):
        postfix = []
        stack = []
        for char in expression.split():
            if char.isalnum():
                postfix.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop()  # Discard '('
            else:
                while stack and self.precedence(stack[-1]) >= self.precedence(char):
                    postfix.append(stack.pop())
                stack.append(char)
        while stack:
            postfix.append(stack.pop())
        return "".join(postfix)

    def generate_code(self, expression):
        postfix_expression = self.infix_to_postfix(expression)
        stack = []
        for token in postfix_expression:
            if token.isalnum():
                stack.append(token)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = "t" + str(self.temp_count)
                self.temp_count += 1
                self.code.append((token, operand1, operand2, result))
                stack.append(result)
        return self.code

    def display_code(self):
        print("Three Address Code:")
        for op, op1, op2, result in self.code:
            print(f"{result} = {op1} {op} {op2}")


# Take user input for the expression
expression = input("Enter the infix expression: ")

# Generate and display three-address code
generator = ThreeAddressGenerator()
code = generator.generate_code(expression)
generator.display_code()
