import pyglet
from pyglet.gl import *

window = pyglet.window.Window(width=720, height=480)
window.projection = pyglet.window.Projection3D()
batch = pyglet.graphics.Batch()

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    glRotatef(1, dx, dy, 0)

def rotate(dt):
    glRotatef(0.5, dt, dt, dt)

if __name__ == "__main__":
    tri_verts = (
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 0),
    )
    tv_flat = list(sum(tri_verts, ()))

    #  make a triangle
    vlist = batch.add(3, GL_TRIANGLES, None,
        ('v3f', tv_flat),
        ('c3f', (1, 0, 0,
                 0, 1, 0,
                 0, 0, 1)))

    glTranslatef(0.5, 0, -3) 
    pyglet.clock.schedule_interval(rotate, 1/60.0)
    pyglet.app.run()