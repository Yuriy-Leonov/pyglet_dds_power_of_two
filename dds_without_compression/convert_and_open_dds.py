import pyglet


def convert():
    from wand import image
    with image.Image(filename="31_21.png") as img:
        img.strip()
        img.flip()
        image.library.MagickSetOption(img.wand, b"dds:mipmaps", b"0")
        image.library.MagickSetOption(img.wand, b"dds:compression", b"none")
        img.save(filename="31_21.dds")


def load():
    pyglet.image.load("31_21.dds")


if __name__ == '__main__':
    convert()
    load()

"""
Exception is 

Traceback (most recent call last):
  File "convert_and_open_dds.py", line 20, in <module>
    load()
  File "convert_and_open_dds.py", line 15, in load
    pyglet.image.load("31_21.dds")
  File "/<path to venv>/lib/python3.6/site-packages/pyglet/image/__init__.py", line 208, in load
    raise first_exception
  File "/<path to venv>/lib/python3.6/site-packages/pyglet/image/__init__.py", line 198, in load
    image = decoder.decode(file, filename)
  File "/<path to venv>/lib/python3.6/site-packages/pyglet/image/codecs/gdkpixbuf2.py", line 311, in decode
    return loader.get_pixbuf().to_image()
  File "/<path to venv>/lib/python3.6/site-packages/pyglet/image/codecs/gdkpixbuf2.py", line 137, in get_pixbuf
    self._finish_load()
  File "/<path to venv>/lib/python3.6/site-packages/pyglet/image/codecs/gdkpixbuf2.py", line 123, in _finish_load
    raise ImageDecodeException(_gerror_to_string(error))
pyglet.image.codecs.ImageDecodeException: GdkPixBuf Error: domain[66], code[3]: <ctypes.LP_c_char object at 0x7f824b832950>

"""

"""
identify -verbose 31_21.dds | grep -i "compression"
  Compression: None
"""
