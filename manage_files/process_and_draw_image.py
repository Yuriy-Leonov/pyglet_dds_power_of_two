import os
import sys
import time
import pyglet

from wand import image


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch = pyglet.graphics.Batch()
        self.collection = []
        self.create_as_sprite("example.png")  # 0
        self.create_as_sprite("example.dds")  # 1
        self.collection[0].x = 30
        self.collection[0].y = 30

        self.collection[1].x = 400
        self.collection[1].y = 30

    def create_as_sprite(self, path):
        picture = pyglet.image.load(path)
        sprite = pyglet.sprite.Sprite(
            img=picture,
            batch=self.batch
        )
        self.set_filter()
        sprite.scale = 40
        self.collection.append(sprite)

    def set_filter(self):
        gl_filter = pyglet.graphics.GL_NEAREST
        pyglet.graphics.glTexParameteri(
            pyglet.graphics.GL_TEXTURE_2D,
            pyglet.graphics.GL_TEXTURE_MAG_FILTER,
            gl_filter
        )
        pyglet.graphics.glTexParameteri(
            pyglet.graphics.GL_TEXTURE_2D,
            pyglet.graphics.GL_TEXTURE_MIN_FILTER,
            gl_filter
        )

    def make_screenshot(self):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        name = f"screenshots{os.path.sep}Screenshot_{int(time.time() * 1000)}.png"
        pyglet.image.get_buffer_manager().get_color_buffer().save(name)
        print(f"print screen was made: {name}")

    def on_key_press(self, KEY, MOD):
        if KEY == pyglet.window.key.ESCAPE:
            self.close()
            sys.exit(0)
        if MOD & pyglet.window.key.MOD_CTRL and KEY == pyglet.window.key.P:
            self.make_screenshot()
            return

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
        img.flip()
        img.compression = "dxt5"
        image.library.MagickSetOption(img.wand, b"dds:mipmaps", b"0")
        img.save(filename="example.dds")

    window = Window(width=1000, height=600, caption='Pyglet', resizable=True)
    pyglet.app.run()
