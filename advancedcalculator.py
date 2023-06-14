
from stack import Stack
from simple_calculator import SimpleCalculator

class AdvancedCalculator(SimpleCalculator):
    def __init__(self):
        super().__init__()

    def tokenize(self, input_expression):
        import re
        tokens = re.findall(r"(\d+|[+\-*/(){}])", input_expression)
        return [int(token) if token.isdigit() else token for token in tokens]

    def check_brackets(self, list_tokens):
        bracket_stack = Stack()
        opening_brackets = ["(", "{", "["]
        closing_brackets = [")", "}", "]"]
        for token in list_tokens:
            if token in opening_brackets:
                bracket_stack.push(token)
            elif token in closing_brackets:
                if bracket_stack.is_empty():
                    return False
                top = bracket_stack.peek()
                if (token == ")" and top == "(") or (token == "}" and top == "{") or (token == "]" and top == "["):
                    bracket_stack.pop()
                else:
                    return False
        return bracket_stack.is_empty()

    def evaluate_list_tokens(self, list_tokens):
        operator_stack = Stack()
        operand_stack = Stack()
        for token in list_tokens:
            if isinstance(token, int):
                operand_stack.push(token)
            elif token in ["+", "-", "*", "/"]:
                while not operator_stack.is_empty() and self.has_higher_precedence(token, operator_stack.peek()):
                    operator = operator_stack.pop()
                    operand2 = operand_stack.pop()
                    operand1 = operand_stack.pop()
                    result = self.doeval(operand1, operator, operand2)
                    if result == "Error":
                        return "Error"
                    operand_stack.push(result)
                operator_stack.push(token)
            elif token in ["(", "{", "["]:
                operator_stack.push(token)
            elif token in [")", "}", "]"]:
                while not operator_stack.is_empty() and not operator_stack.peek() in ["(", "{", "["]:
                    operator = operator_stack.pop()
                    operand2 = operand_stack.pop()
                    operand1 = operand_stack.pop()
                    result = self.doeval(operand1, operator, operand2)
                    if result == "Error":
                        return "Error"
                    operand_stack.push(result)
                if not operator_stack.is_empty() and operator_stack.peek() in ["(", "{", "["]:
                    operator_stack.pop()

        while not operator_stack.is_empty():
            operator = operator_stack.pop()
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = self.doeval(operand1, operator, operand2)
            if result == "Error":
                return "Error"
            operand_stack.push(result)

        return operand_stack.pop()

    def has_higher_precedence(self, op1, op2):
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
        return precedence[op1] > precedence[op2]

    def doeval(self, a, b, c):
        a = int(a)
        c = int(c)
        if b == "+":
            return float(a) + float(c)
        elif b == "-":
            return float(a) - float(c)
        elif b == "*":
            return float(a) * float(c)
        elif b == "/":
            if c == 0:
                return "Error"
            return float(a) / float(c)


