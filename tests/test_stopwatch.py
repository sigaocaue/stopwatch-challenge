import unittest
from src.stopwatch import Stopwatch


class TestStopwatch(unittest.TestCase):
    def setUp(self):
        """Inicializa um novo stopwatch para cada teste."""
        self.stopwatch = Stopwatch()

    def test_start(self):
        """Testa se o stopwatch inicia corretamente."""
        self.stopwatch.start()
        self.assertIsNotNone(self.stopwatch.start_time)

    def test_stop(self):
        """Testa se o stopwatch para corretamente."""
        self.stopwatch.start()
        self.stopwatch.stop()
        self.assertFalse(self.stopwatch.running)

    def test_restart(self):
        """Testa se o stopwatch reinicia corretamente."""
        self.stopwatch.start()
        self.stopwatch.reset()
        self.assertIsNone(self.stopwatch.start_time)
        self.assertFalse(self.stopwatch.running)

    def test_display(self):
        """Testa a exibição do tempo decorrido."""
        self.stopwatch.start()
        # Aqui você precisaria simular uma espera ou ajustar o método para permitir testes
        # Por exemplo, passar um tempo específico para display() como argumento para teste
        self.stopwatch.stop()
        elapsed_time = self.stopwatch.display()
        self.assertIsNotNone(elapsed_time)
        # Adicione mais asserções específicas sobre o formato ou valor de elapsed_time


if __name__ == '__main__':
    unittest.main()
