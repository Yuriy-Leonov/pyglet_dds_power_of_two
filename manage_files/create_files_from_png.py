import os

from wand import image


def create_file(path):
    destination_path = os.path.join(
        "static_dist",
        *path.split(os.sep)[1:])
    destination_root = destination_path[:-3]
    destination_path = destination_root + "dds"
    with image.Image(filename=path) as img:
        img.flip()
        img.compression = "dxt3"
        img.save(filename=destination_path)


if __name__ == '__main__':
    files = [
        os.path.join("static_source", "31_21.png"),
        os.path.join("static_source", "32_32.png"),
        os.path.join("static_source", "40_20.png"),
    ]
    for file in files:
        create_file(file)
