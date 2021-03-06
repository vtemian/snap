from snap.parsers.lexer import lexer
from snap.parsers.parser import parser


class TestParser(object):
    def test_sum(self):
        assert parser.parse(lexer.lex(' 1 + 1')).eval() == 2

    def test_minus(self):
        assert parser.parse(lexer.lex('1 -  1')).eval() == 0

    def test_mul(self):
        assert parser.parse(lexer.lex('2 * 2')).eval() == 4

    def test_div(self):
        assert parser.parse(lexer.lex('2 / 2')).eval() == 1

    def test_open_param(self):
        assert parser.parse(lexer.lex('(1 + 2) * (4 - 1)')).eval() == 9

    def test_concat(self):
        assert parser.parse(lexer.lex('"a" + "b"')).eval() == "ab"
