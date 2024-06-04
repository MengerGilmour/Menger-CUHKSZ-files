class ListStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def top(self):
        return self.items[-1] if not self.is_empty() else None

def in2post(expr):
    prec = {'*': 2, '/': 2, '+': 1, '-': 1}
    s = ListStack()
    postFix = ''
    for c in expr:
        if c.isalpha() or c.isdigit():
            postFix += c
        elif c == '(':
            s.push(c)
        elif c == ')':
            t = s.pop()
            while t != '(':
                postFix += t
                t = s.pop()
        else:
            while not s.is_empty() and s.top() != '(' and prec[s.top()] >= prec[c]:
                postFix += s.pop()
            s.push(c)
    while not s.is_empty():
        postFix += s.pop()
    return postFix


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
