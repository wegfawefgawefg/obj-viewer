import pyglet
from pyglet import gl
from pyglet.graphics import get_default_shader

window = pyglet.window.Window(width=720, height=480)
batch = pyglet.graphics.Batch()

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_resize(width, height):
    h = max(height, 1)
    gl.glViewport(0, 0, width, h)
    return pyglet.event.EVENT_HANDLED

def main() -> None:
    tri_verts = (
        (120, 100, 0),
        (360, 400, 0),
        (600, 100, 0),
    )
    tv_flat = list(sum(tri_verts, ()))

    program = get_default_shader()
    colors = (
        255, 0, 0, 255,
        0, 255, 0, 255,
        0, 0, 255, 255,
    )
    _vlist = program.vertex_list(
        3,
        gl.GL_TRIANGLES,
        batch=batch,
        position=("f", tv_flat),
        colors=("Bn", colors),
    )

    gl.glClearColor(0.08, 0.08, 0.1, 1.0)
    pyglet.app.run()


if __name__ == "__main__":
    main()
