import pyglet
import multiprocessing


class CustomMusic:
    def __init__(self):
        pyglet.options["audio"] = ("openal", "pulse", "directsound", "silent")
        self.soundtrack = pyglet.media.load("example.wav")
        self.soundtrack.play()


def start_sub_process():
    CustomMusic()
    pyglet.app.run()


class CustomWindow(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pyglet.clock.schedule_interval(self.update, 1 / 60)

    def update(self, delta_time):
        pass


if __name__ == '__main__':
    p = multiprocessing.Process(target=start_sub_process)
    p.daemon = True
    p.start()
    window = CustomWindow(width=100, height=100, caption='window_1')
    pyglet.app.run()
