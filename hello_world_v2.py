# coding: utf-8

import time
import ui


def change_label(label):
    if label.text == "Hello":
        label.text = "World"
    else:
        label.text = "Hello"


if __name__ == '__main__':
    view = ui.load_view("hello_world_v2")
    my_label = view["label1"]
    view.present("fullscreen")

    while True:
        time.sleep(1)
        change_label(my_label)
