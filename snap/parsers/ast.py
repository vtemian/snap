from rply.token import BaseBox


class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


class String(BaseBox):
    def __init__(self, value):
        self.value = value.replace("\"", "")

    def eval(self):
        return self.value


class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOp):
    def eval(self):
        if isinstance(self.left, Number) and isinstance(self.right, Number):
            return self.left.eval() + self.right.eval()
        elif isinstance(self.left, String) and isinstance(self.right, String):
            return "%s%s" % (self.left.eval(), self.right.eval())


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()
