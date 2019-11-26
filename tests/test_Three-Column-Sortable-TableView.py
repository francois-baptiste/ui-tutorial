import sys
from collections import namedtuple

from tests.mocks import ui
import pytest

# mock pythonista ui package
sys.modules['ui'] = ui
from Three_Column_Sortable_TableView import MyTableView




testdata_background_color = [
    "lightgrey",
    "white",
]

testdata_name = [
    "Name",
    "Size",
    "Date",
]

@pytest.mark.parametrize("background_color", testdata_background_color)
@pytest.mark.parametrize("name", testdata_name)
def test_Name(background_color,name):
    toto = MyTableView()
    toto.btn_action(namedtuple('Sender', ['name', 'background_color'])(name, background_color))


def test_Size():
    toto = MyTableView()
    toto.btn_action(namedtuple('Sender', ['name', 'background_color'])('Size', "white"))


def test_Daten():
    toto = MyTableView()
    toto.btn_action(namedtuple('Sender', ['name', 'background_color'])('Date', "lightgrey"))
