import unittest
from unittest.mock import patch
from main import main

class TestMain(unittest.TestCase):
    def testar_entrada_e_saída_valor(self):
        with self.subTest(self):
            with patch('builtins.input', side_effect=['jogador', '10', 'adicionar', 'sair']):
                with patch('builtins.print') as mock_print:
                    main()
                    mock_print.assert_called_with('Saindo do sistema.')
    
    def testar_entrada_e_saída_valor_string(self):
        with self.subTest(self):
            with patch('builtins.input', side_effect=['jogador', 'a', 'adicionar', 'sair']):
                with patch('builtins.print') as mock_print:
                    main()
                    mock_print.assert_called_with('Saindo do sistema.')

unittest.main(verbosity=True)