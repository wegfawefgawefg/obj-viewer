from pprint import pprint

import pyglet
from pyglet import gl
from pyglet.gl import *

from tqdm import tqdm


window = pyglet.window.Window(width=1000, height=1000, resizable=True)
window.projection = pyglet.window.Projection3D()
batch = pyglet.graphics.Batch()

scale = 1

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    glRotatef(1, dx, dy, 0)

@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    global scale
    scale += scroll_y * 0.1
    scale = max(0.1, scale)
    scale = min(10, scale)
    glScalef(scale, scale, scale)
    return pyglet.event.EVENT_HANDLED

@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60., width / height, .1, 1000.)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

def rotate(dt):
    glRotatef(0.5, 1.0*dt, 20.0*dt, 2.5*dt)

if __name__ == "__main__":
    field_dims = (20,)*2

    vs = []
    for yii in tqdm(range(field_dims[1])):
        for xii in range(field_dims[0]):
            x = xii / field_dims[0]
            y = yii / field_dims[1]
            vs.append((x, y, 0))

    vs_flat = list(sum(vs, ()))
    cs = [int(c*255) for c in vs_flat]

    # make a triangle of just points
    vlist = batch.add(len(vs_flat)//3, GL_POINTS, None, 
        ('v3f', vs_flat),
        ('c3B', cs)
    )

    glTranslatef(-0.2, -0.2, -3) 
    pyglet.clock.schedule_interval(rotate, 1/60.0)
    pyglet.app.run()