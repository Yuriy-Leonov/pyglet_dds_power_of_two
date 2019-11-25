import pyglet
import uuid


# below class is shared by caffeinepills#5210 in discord channel of pyglet
# and it solves the probles
class CustomLabel(pyglet.text.Label):
    ''' Pyglet label replacement using cached groups. '''

    _cached_groups = {}
    def _init_groups(self, group):
        if not group:
            return
        if group not in self.__class__._cached_groups.keys():
            top = pyglet.text.layout.TextLayoutGroup(group)
            bg = pyglet.graphics.OrderedGroup(0, top)
            fg = pyglet.text.layout.TextLayoutForegroundGroup(1, top)
            fg2 = pyglet.text.layout.TextLayoutForegroundDecorationGroup(2, top)
            self.__class__._cached_groups[group] = [top, bg, fg, fg2, 0]
        groups = self.__class__._cached_groups[group]
        self.top_group = groups[0]
        self.background_group = groups[1]
        self.foreground_group = groups[2]
        self.foreground_decoration_group = groups[3]
        groups[4] += 1

    def delete(self):
        pyglet.text.Label.delete(self)
        if self.top_group and self.top_group.parent:
            group = self.top_group.parent
            if group is not None:
                groups = self.__class__._cached_groups[group]
                groups[4] -= 1
                if not groups[4]:
                    del self.__class__._cached_groups[group]
        self.top_group = None
        self.background_self = None
        self.foreground_group = None
        self.foreground_decoration_group = None


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
        # label = pyglet.text.Label(
        label = CustomLabel(  # this is a solution of problem, Thanks to caffeinepills#5210 in discord channel of pyglet
            f'{str(uuid.uuid4())[:5]}', font_name='Arial', font_size=12,
            x=x, y=y,
            anchor_x='left', anchor_y='bottom',
            color=(255, 255, 255, 255),
            # group=self.order_groups[0],  # without group FPS is more than 300, with group - it's about 30-40
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
