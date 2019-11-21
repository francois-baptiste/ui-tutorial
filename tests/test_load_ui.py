import sys
from tests.mocks import ui
import pytest

# mock pythonista ui package
sys.modules['ui'] = ui

testdata = [
    "AreYouEnabledView.pyui",
    "pop-over.pyui",
    "switchview1.pyui",
    "hello_world_v2.pyui",
    "po.pyui",
    "SwitchViews.pyui",
    "layout2.pyui",
    "segmented-control.pyui",
    "UsingSubviews.pyui",
    "layout.pyui",
    "shoppinglist.pyui",
    "Webbrowser.pyui",
    "load_ui.pyui",
    "ShowTableView.pyui",
    "NavigationViewExample.pyui",
    "SpecialButton.pyui",
]


@pytest.mark.parametrize("filename", testdata)
def test_load_view(filename):
    view = ui.load_view(filename)
    view.present("fullscreen")