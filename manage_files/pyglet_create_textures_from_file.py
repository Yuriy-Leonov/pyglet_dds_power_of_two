import os
import pyglet


def get_texture_group(path, sprite_rows, sprite_column):
    image = pyglet.image.load(path)
    image_grid = pyglet.image.ImageGrid(image, sprite_rows, sprite_column)
    texture_grid = image_grid.get_texture_sequence()

    return (
        pyglet.graphics.TextureGroup(texture_grid),
        texture_grid
    )


if __name__ == '__main__':
    files = [
        os.path.join("static_dist", "32_32.dds"),
        os.path.join("static_dist", "31_21.dds"),
        os.path.join("static_dist", "40_20.dds"),
    ]
    for file in files:
        texture_group, tex_grid = get_texture_group(path=file, sprite_rows=2, sprite_column=2)
        print(tex_grid, tex_grid[0])
