import pyglet
from pyglet.gl import *
from pprint import pprint

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
    vs = (
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 0),
    )
    cs = (
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
    )

    stack = tuple(zip(vs, cs))

    # vs_f = list(sum(vs, ()))
    # cs_f = list(sum(cs, ()))
    stacks = [(*vs[i], *cs[i]) for i in range(len(vs))]
    s_f = list(sum(stacks, ()))

    #  make a triangle
    # vlist = batch.add(3, GL_TRIANGLES, None,
    #     ('v3f', vs_f),
    #     ('c3f', cs_f))

    vertex_shader_source = """
        #version 330
        in layout(location = 0) vec3 position;
        in layout(location = 1) vec3 color;
        out vec3 color_out;
        void main() {
            color_out = color;
            gl_Position = vec4(position, 1.0);
        }
    """
    fragment_shader_source = """
        #version 330
        in vec3 color_out;
        out vec4 color;
        void main() {
            color = vec4(color_out, 1.0);
        }
    """

    glTranslatef(0.5, 0, -3) 
    pyglet.clock.schedule_interval(rotate, 1/60.0)
    pyglet.app.run()