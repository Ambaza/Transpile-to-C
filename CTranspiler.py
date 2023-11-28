class CTranspiler:
    def __init__(self):
        self.variable_counter = 0

    def transpile(self, ast):
        c_code = "#include <stdio.h>\n"
        c_code += "#include <stdlib.h>\n\n"
        c_code += self.transpile_ast(ast)
        return c_code

    def transpile_ast(self, ast):
        if isinstance(ast, list):  # It's an S-expression
            operator = ast[0]
            if operator == '+':
                return f"({self.transpile_ast(ast[1])} + {self.transpile_ast(ast[2])})"
            elif operator == '-':
                return f"({self.transpile_ast(ast[1])} - {self.transpile_ast(ast[2])})"
            elif operator == '*':
                return f"({self.transpile_ast(ast[1])} * {self.transpile_ast(ast[2])})"
            elif operator == '/':
                return f"({self.transpile_ast(ast[1])} / {self.transpile_ast(ast[2])})"
            else:
                raise ValueError(f"Unknown operator: {operator}")
        elif isinstance(ast, int):  # It's a literal number
            return str(ast)
        else:
            raise ValueError(f"Unexpected AST node: {ast}")

# Example usage:
ast = ['+', 3, ['*', 4, 5]]  # Represents (+ 3 (* 4 5))
transpiler = CTranspiler()
c_code = transpiler.transpile(ast)
print(c_code)
