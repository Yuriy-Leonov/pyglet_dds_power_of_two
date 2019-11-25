import pyglet
import uuid


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fps_display = pyglet.window.FPSDisplay(self)
        self.fps_display.label.color = (168, 168, 168, 255)
        self.fps_display.label.font_size = 10

        self.batch = pyglet.graphics.Batch()
        self.order_groups = [
            pyglet.graphics.OrderedGroup(z_ind)
            for z_ind in range(1)
        ]
        self.collection = []
        for x in range(20):
            for y in range(20):
                self.create_label(x, y)

        pyglet.clock.schedule_interval(self.update, 1 / 512)

    def update(self, delta_time):
        pass

    def create_label(self, x, y):
        x = x * 60
        y = y * 20 + 20
        label = pyglet.text.Label(
            f'{str(uuid.uuid4())[:5]}', font_name='Arial', font_size=12,
            x=x, y=y,
            anchor_x='left', anchor_y='bottom',
            color=(255, 255, 255, 255),
            group=self.order_groups[0],  # without group FPS is more than 300, with group - it's about 30-40
            batch=self.batch)
        self.collection.append(label)

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
