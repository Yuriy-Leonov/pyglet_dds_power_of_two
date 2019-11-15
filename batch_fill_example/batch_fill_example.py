# pyglet 1.4.7

import time
import pyglet
from wand import image


class Window(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.batch = pyglet.graphics.Batch()
        self.position = [0, 0, 600.0]
        self.vertices_list = []

        img = pyglet.image.load("example.dds")
        self.image_grid = pyglet.image.ImageGrid(img, 2, 2)
        self.texture_grid = self.image_grid.get_texture_sequence()
        self.texture_group = pyglet.graphics.TextureGroup(self.texture_grid)

        start = int(time.time() * 1000)
        for x in range(-100, 100):
            for y in range(-100, 100):
                self.add_rect(x=x, y=y)
        print(f"all was drawn in {int(time.time() * 1000) - start} seconds")

    def add_rect(self, x, y):
        x_ = 16 * x + 16
        y_ = 16 * y + 16
        x = x * 16
        y = y * 16
        tex_coords = ('t3f', self.texture_grid[0].tex_coords)

        start = int(time.time() * 1000 * 1000)
        vert_list = self.batch.add(
            4, pyglet.gl.GL_QUADS,
            self.texture_group,
            ('v3f', (x, y, 0,
                     x_, y, 0,
                     x_, y_, 0,
                     x, y_, 0)),
            tex_coords)
        print(f"batch.add was done in {int(time.time() * 1000 * 1000) - start} nanosec")

        self.vertices_list.append(vert_list)

    def set_3d(self):
        """ Configure OpenGL to draw in 3d.
        """
        import math
        width, height = self.get_size()
        pyglet.graphics.glEnable(pyglet.graphics.GL_BLEND)
        pyglet.graphics.glBlendFunc(
            pyglet.graphics.GL_SRC_ALPHA,
            pyglet.graphics.GL_ONE_MINUS_SRC_ALPHA)
        pyglet.graphics.glViewport(0, 0, width, height)
        pyglet.graphics.glMatrixMode(pyglet.graphics.GL_PROJECTION)
        pyglet.graphics.glLoadIdentity()
        pyglet.graphics.gluPerspective(90, width / height, 0.1, 6000.0)
        pyglet.graphics.glMatrixMode(pyglet.graphics.GL_MODELVIEW)
        pyglet.graphics.glLoadIdentity()
        x, y, z = self.position
        pyglet.graphics.glTranslatef(-x, -y, -z)

    def on_draw(self):
        self.clear()
        self.set_3d()
        self.batch.draw()


if __name__ == '__main__':
    window = Window(width=800, height=600, caption='Pyglet', resizable=True)
    pyglet.app.run()
