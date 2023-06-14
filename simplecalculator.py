from stack import Stack


def doeval(a, b, c):
    a = int(a)
    c = int(c)
    if b == "+":
        return float(a) + float(c)
    elif b == "-":
        return float(a) - float(c)
    elif b == "*":
        return float(a)*float(c)
    elif b == "/":
        return float(a)/float(c)


class SimpleCalculator:
    def __init__(self):
        """
        Instantiate any data attributes
        """
        self.history = []

    def evaluate_expression(self, input_expression):
        """
        Evaluate the input expression and return the output as a float
        Return a string "Error" if the expression is invalid
        """
        k = input_expression[:]
        input_expression = input_expression.replace(" ", "")
        operator = None
        operator_list = ["+", "-", "*", "/"]
        ind = None
        for i in range(len(input_expression)):
            if input_expression[i] in operator_list:
                operator = input_expression[i]
                ind = i
                break
        if operator is None or ind == len(input_expression) - 1 or ind == 0:
            self.history.append((k, "Error"))
            return "Error"
        a = input_expression[:ind]
        b = input_expression[ind + 1:]
        if a.isdigit() and b.isdigit():
            result = doeval(a, operator, b)
            self.history.append((k, result))
            return result
        self.history.append((k, "Error"))
        return "Error"

    def get_history(self):
        """
        Return history of expressions evaluated as a list of (expression, output) tuples
        The order is such that the most recently evaluated expression appears first
        """
        return self.history[::-1]
