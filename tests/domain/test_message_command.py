import unittest

from src.domain.message_command import MessageCommand

class TestMessageCommand(unittest.TestCase):

    def test_translate(self):
        command = MessageCommand("message-content")
        expectedTranslation = "M:message-content"
        translation = command.translate()
        self.assertEqual(translation, expectedTranslation)

    
if __name__ == '__main__':
    unittest.main()
