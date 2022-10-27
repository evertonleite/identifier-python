import pytest
import src.ident.identifier as identifier

class TestClass:
    def test_identifier_1(self):
        string = ''
        assert identifier.validate(string) == 'Invalido'
        
    def test_identifier_2(self):
        string = 'a'
        assert identifier.validate(string) == 'Valido'
        
    def test_identifier_3(self):
        string = 'a12345'
        assert identifier.validate(string) == 'Valido'
        
    def test_identifier_4(self):
        string = 'a123456'
        assert identifier.validate(string) == 'Invalido'
        
    def test_identifier_5(self):
        string = 'abc1*'
        assert identifier.validate(string) == 'Invalido'
        
    def test_identifier_6(self):
        string = 'A#$12'
        assert identifier.validate(string) == 'Invalido'
