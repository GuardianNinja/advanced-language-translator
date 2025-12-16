class NaytrunesInterpreter:
    def __init__(self):
        self.stack = []
        self.vars = {}

    def execute(self, tokens):
        for tok in tokens:
            if tok == "spiral":  # replicate
                if self.stack: self.stack.append(self.stack[-1])
            elif tok == "triangle_eye":  # print
                if self.stack: print(self.stack.pop())
            elif tok == "heart":  # assign
                if self.stack: self.vars["A"] = self.stack.pop()
            else:
                self.stack.append(tok)
