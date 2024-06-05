def evaluate(expr, variables):
    def apply_operator(op, a, b):
        if op == '+': return a + b
        elif op == '-': return a - b
        elif op == '*': return a * b
        elif op == '/': return a / b

    postfix = in2post(expr)
    stack = ListStack()

    for token in postfix:
        if token in variables:
            stack.push(variables[token])
        elif token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            result = apply_operator(token, a, b)
            stack.push(result)
        else:
            # Handle unexpected characters
            raise ValueError(f"Unknown token: {token}")

    return stack.pop()

# Example usage
variables = {'A': 12, 'B': 4, 'C': 3, 'D': 8, 'E': 2}
expr = "A/(B*C)-(D+E)"
print(evaluate(expr, variables))