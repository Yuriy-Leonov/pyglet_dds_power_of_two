# Describes exception with loading DDS files not power-of-two sizes

### create_files_from_png.py
Describes how `.dds` files were created

### pyglet_load_files.py
Produces following exceptions:

```
Try to open file static_dist/32_32.dds
Successfully loaded.

Try to open file static_dist/31_21.dds
Traceback (most recent call last):
  File "pyglet_load_files.py", line 9, in try_to_load_file
    pyglet.image.load(path)
  File "<path>/v_pyglet/lib/python3.6/site-packages/pyglet/image/__init__.py", line 198, in load
    image = decoder.decode(file, filename)
  File "<path>/v_pyglet/lib/python3.6/site-packages/pyglet/image/codecs/dds.py", line 223, in decode
    'GL_EXT_texture_compression_s3tc', decoder)
  File "<path>/v_pyglet/lib/python3.6/site-packages/pyglet/image/__init__.py", line 1234, in __init__
    raise ImageException('Dimensions of %r must be powers of 2' % self)
  File "<path>/v_pyglet/lib/python3.6/site-packages/pyglet/image/__init__.py", line 399, in __repr__
    return '<%s %dx%d>' % (self.__class__.__name__, self.width, self.height)
AttributeError: 'CompressedImageData' object has no attribute 'width'

Try to open file static_dist/40_20.dds
Traceback (most recent call last):
  File "pyglet_load_files.py", line 9, in try_to_load_file
    pyglet.image.load(path)
  File "<path>/v_pyglet/lib/python3.6/site-packages/pyglet/image/__init__.py", line 198, in load
    image = decoder.decode(file, filename)
  File "<path>/v_pyglet/lib/python3.6/site-packages/pyglet/image/codecs/dds.py", line 223, in decode
    'GL_EXT_texture_compression_s3tc', decoder)
  File "<path>/v_pyglet/lib/python3.6/site-packages/pyglet/image/__init__.py", line 1234, in __init__
    raise ImageException('Dimensions of %r must be powers of 2' % self)
  File "<path>/v_pyglet/lib/python3.6/site-packages/pyglet/image/__init__.py", line 399, in __repr__
    return '<%s %dx%d>' % (self.__class__.__name__, self.width, self.height)
AttributeError: 'CompressedImageData' object has no attribute 'width'
```