import pyglet
from wand import image


class Window(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.batch = pyglet.graphics.Batch()
        self.position = [0, 0, 600.0]
        self.vertices_list = []

        self.add_rect_as_texture_grid("example.png", x=-400, y=200, z=0)
        self.add_rect_as_texture_grid("example.dds", x=0, y=200, z=0)

        self.or_simple_add_from_texture("example.png", x=-400, y=-200, z=0)
        self.or_simple_add_from_texture("example.dds", x=0, y=-200, z=0)

    def add_rect_as_texture_grid(self, file_name, x, y, z):
        img = pyglet.image.load(file_name)
        image_grid = pyglet.image.ImageGrid(img, 1, 1)
        texture_grid = image_grid.get_texture_sequence()
        texture_group = pyglet.graphics.TextureGroup(texture_grid)
        x_ = (texture_group.texture.width + x)
        y_ = (texture_group.texture.height + y)
        tex_coords = ('t3f', texture_grid[0].tex_coords)

        vert_list = self.batch.add(
            4, pyglet.gl.GL_QUADS,
            texture_group,
            ('v3f', (x, y, z,
                     x_, y, z,
                     x_, y_, z,
                     x, y_, z)),
            tex_coords)
        self.vertices_list.append(vert_list)

    def or_simple_add_from_texture(self, file_name, x, y, z):
        img = pyglet.image.load(file_name)
        texture_group = pyglet.graphics.TextureGroup(img.get_texture())
        x_ = (texture_group.texture.width + x)
        y_ = (texture_group.texture.height + y)
        tex_coords = ('t3f', texture_group.texture.tex_coords)

        vert_list = self.batch.add(
            4, pyglet.gl.GL_QUADS,
            texture_group,
            ('v3f', (x, y, z,
                     x_, y, z,
                     x_, y_, z,
                     x, y_, z)),
            tex_coords)
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
    with image.Image(filename="example.png") as img:
        img.strip()
        img.compression = "dxt3"
        img.save(filename="example.dds")
    window = Window(width=800, height=600, caption='Pyglet', resizable=True)
    pyglet.app.run()