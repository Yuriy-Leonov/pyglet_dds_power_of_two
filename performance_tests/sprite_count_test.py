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

    def get_tex_map(self, tex_coords):
        tex_map = tex_coords
        # mirror
        # 1 2   ->   2 1
        # 3 4   ->   4 3
        # tex_map = [
        #     tex_map[6], tex_map[1], tex_map[2],
        #     tex_map[9], tex_map[4], tex_map[5],
        #     tex_map[0], tex_map[7], tex_map[8],
        #     tex_map[3], tex_map[10], tex_map[11],
        # ]

        # diagonal mirror
        # 1 2   ->   1 3
        # 3 4   ->   2 4
        # tex_map = [
        #     tex_map[3], tex_map[10], tex_map[11],
        #     tex_map[6], tex_map[1], tex_map[2],
        #     tex_map[9], tex_map[4], tex_map[5],
        #     tex_map[0], tex_map[7], tex_map[8],
        # ]

        # horizontal mirror
        # 1 2   ->   1 4
        # 3 4   ->   3 2
        # tex_map = [
        #     tex_map[0], tex_map[7], tex_map[8],
        #     tex_map[3], tex_map[10], tex_map[11],
        #     tex_map[6], tex_map[1], tex_map[2],
        #     tex_map[9], tex_map[4], tex_map[5],
        # ]

        # diagonal mirror 2
        # 1 2   ->   4 2
        # 3 4   ->   3 1
        # tex_map = [
        #     tex_map[9], tex_map[4], tex_map[5],
        #     tex_map[0], tex_map[7], tex_map[8],
        #     tex_map[3], tex_map[10], tex_map[11],
        #     tex_map[6], tex_map[1], tex_map[2],
        # ]

        # counterclockwise rotation 90* (- 90*)
        # 1 2   ->   2 4
        # 3 4   ->   1 3
        # tex_map = [
        #     tex_map[9], tex_map[10], tex_map[11],
        #     tex_map[0], tex_map[1], tex_map[2],
        #     tex_map[3], tex_map[4], tex_map[5],
        #     tex_map[6], tex_map[7], tex_map[8],
        #
        # ]

        # rotation 180*
        # 1 2   ->   4 3
        # 3 4   ->   2 1
        # tex_map = [
        #     tex_map[6], tex_map[7], tex_map[8],
        #     tex_map[9], tex_map[10], tex_map[11],
        #     tex_map[0], tex_map[1], tex_map[2],
        #     tex_map[3], tex_map[4], tex_map[5],
        #
        # ]

        # + 90*
        # 1 2   ->   3 1
        # 3 4   ->   4 2
        # tex_map = [
        #     tex_map[3], tex_map[4], tex_map[5],
        #     tex_map[6], tex_map[7], tex_map[8],
        #     tex_map[9], tex_map[10], tex_map[11],
        #     tex_map[0], tex_map[1], tex_map[2],
        #
        # ]
        return tex_map

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
