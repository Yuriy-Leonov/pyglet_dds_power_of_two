import pyglet
import uuid


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fps_display = pyglet.window.FPSDisplay(self)
        self.fps_display.label.color = (168, 168, 168, 255)
        self.fps_display.label.font_size = 10
        self.picture = pyglet.image.load("example.png")

        self.batch = pyglet.graphics.Batch()
        self.order_groups = [
            pyglet.graphics.OrderedGroup(z_ind)
            for z_ind in range(1)
        ]
        self.collection = []
        for x in range(400):
            for y in range(200):
                self.create_sprite(x, y)

        pyglet.clock.schedule_interval(self.update, 1 / 512)

    def update(self, delta_time):
        pass

    def create_sprite(self, x, y):
        x = x * 32
        y = y * 32 + 20
        sprite = pyglet.sprite.Sprite(
            group=self.order_groups[0],  # with or without -> fps is same
            img=self.picture,
            batch=self.batch,
            x=x,
            y=y
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
        self.fps_display.draw()


if __name__ == '__main__':
    window = Window(width=1200, height=600, caption='Pyglet', resizable=True)
    pyglet.app.run()
