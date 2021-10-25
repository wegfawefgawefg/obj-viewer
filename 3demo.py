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
    glEnable(GL_MULTISAMPLE_ARB)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    for i in range(100):
        cube = pyglet.model.load("cube.obj", batch=batch)
        #cube = pyglet.resource.model("cube.obj", batch=batch)
        cube.translation = i * 1, 0, 0
        cube.rotation = 0, 0, 0
        cube.scale = 1, 1, 1

    scale = 0.1
    glScalef(scale, scale, scale)
    glTranslatef(0.5, 0, -10) 
    pyglet.clock.schedule_interval(rotate, 1/60.0)
    pyglet.app.run()