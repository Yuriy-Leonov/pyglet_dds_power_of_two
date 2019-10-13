import pyglet
from wand import image


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch = pyglet.graphics.Batch()
        self.collection = []
        self.create_as_sprite("example.png")  # 0
        self.create_as_sprite("example.dds")  # 1
        self.collection[1].x = 400
        self.create_as_texture_grid("example.png")  # 2
        self.collection[2].y = 300
        self.create_as_texture_grid("example.dds")  # 3
        self.collection[3].x = 400
        self.collection[3].y = 300

    def create_as_sprite(self, path):
        picture = pyglet.image.load(path)
        sprite = pyglet.sprite.Sprite(
            img=picture,
            batch=self.batch
        )
        self.collection.append(sprite)

    def create_as_texture_grid(self, path):
        picture = pyglet.image.load(path)
        image_grid = pyglet.image.ImageGrid(picture, 1, 1)
        texture_grid = image_grid.get_texture_sequence()
        sprite = pyglet.sprite.Sprite(
            img=texture_grid[0],
            batch=self.batch
        )
        self.collection.append(sprite)

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
        self.set_2d()
        self.batch.draw()


if __name__ == '__main__':
    with image.Image(filename="example.png") as img:
        img.strip()
        img.compression = "dxt3"
        img.save(filename="example.dds")
    window = Window(width=1000, height=600, caption='Pyglet', resizable=True)
    pyglet.app.run()
