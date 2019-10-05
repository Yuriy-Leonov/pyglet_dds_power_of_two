import os
import pyglet
import traceback


def try_to_load_file(path):
    print(f"\nTry to open file {path}")
    try:
        pyglet.image.load(path)
    except Exception as e:
        traceback.print_exc()
    else:
        print("Successfully loaded.")


if __name__ == '__main__':
    files = [
        os.path.join("static_dist", "32_32.dds"),  # this file is loaded
        os.path.join("static_dist", "31_21.dds"),  # in GIMP this file doesn't contain mipmap
        os.path.join("static_dist", "40_20.dds"),  # in GIMP this file doesn't contain mipmap
    ]
    for file in files:
        try_to_load_file(file)

