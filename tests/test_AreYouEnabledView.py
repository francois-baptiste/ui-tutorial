import sys

from tests.mocks import ui, console, speech

# mock pythonista ui package
sys.modules['ui'] = ui
sys.modules['console'] = console
sys.modules['speech'] = speech
from AreYouEnabledView import AreYouEnabledView


def test_Name():
    toto = AreYouEnabledView()
#    toto.button_pressed(namedtuple('Sender', ['name', 'user text'])('print', 'toto'))
