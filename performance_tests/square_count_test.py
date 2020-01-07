import pyglet
import uuid


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = [0, 0, 600.0]

        self.fps_display = pyglet.window.FPSDisplay(self)
        self.fps_display.label.color = (168, 168, 168, 255)
        self.fps_display.label.font_size = 10
        self.picture = pyglet.image.load("example.png")
        self.image_grid = pyglet.image.ImageGrid(self.picture, 1, 1)
        self.texture_grid = self.image_grid.get_texture_sequence()
        self.texture_group = pyglet.graphics.TextureGroup(self.texture_grid)

        self.batch = pyglet.graphics.Batch()
        self.order_groups = [
            pyglet.graphics.OrderedGroup(z_ind)
            for z_ind in range(1000)
        ]
        self.vertices_list = []
        for x in range(400):
            for y in range(200):
                self.add_rect_as_texture_grid(x, y)

        pyglet.clock.schedule_interval(self.update, 1 / 512)

    def add_rect_as_texture_grid(self, x, y, z=0):
        x = x * self.texture_group.texture.width
        y = y * self.texture_group.texture.height
        x_ = (self.texture_group.texture.width + x)
        y_ = (self.texture_group.texture.height + y)
        tex_coords = ('t3f', self.texture_grid[0].tex_coords)

        vert_list = self.batch.add(
            4, pyglet.gl.GL_QUADS,
            self.texture_group,
            ('v3f', (x, y, z,
                     x_, y, z,
                     x_, y_, z,
                     x, y_, z)),
            tex_coords)
        self.vertices_list.append(vert_list)

    def update(self, delta_time):
        pass

    def set_3d(self):
        """ Configure OpenGL to draw in 3d.
        """
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

    def set_2d(self):
        width, height = self.get_size()
        pyglet.graphics.glEnable(pyglet.graphics.GL_BLEND)
        pyglet.graphics.glViewport(0, 0, width, height)
        pyglet.graphics.glMatrixMode(pyglet.graphics.GL_PROJECTION)
        pyglet.graphics.glLoadIdentity()
        pyglet.graphics.glOrtho(0, width, 0, height, -1, 1)
        pyglet.graphics.glMatrixMode(pyglet.graphics.GL_MODELVIEW)
        pyglet.graphics.glLoadIdentity()

    def on_draw(self):
        self.clear()
        self.set_3d()
        self.batch.draw()
        self.set_2d()
        self.fps_display.draw()


if __name__ == '__main__':
    window = Window(width=1200, height=600, caption='Pyglet', resizable=True)
    pyglet.app.run()
