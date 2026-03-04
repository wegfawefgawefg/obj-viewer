import pyglet
from pyglet import gl
from pyglet.graphics import get_default_shader

window = pyglet.window.Window(width=1000, height=1000, resizable=True)
batch = pyglet.graphics.Batch()

@window.event
def on_draw():
    window.clear()
    gl.glPointSize(4.0)
    batch.draw()

@window.event
def on_resize(width, height):
    h = max(height, 1)
    gl.glViewport(0, 0, width, h)
    return pyglet.event.EVENT_HANDLED

def main() -> None:
    field_dims = (40, 40)
    margin = 80

    vs = []
    for yii in range(field_dims[1]):
        for xii in range(field_dims[0]):
            x = margin + (window.width - 2 * margin) * (xii / (field_dims[0] - 1))
            y = margin + (window.height - 2 * margin) * (yii / (field_dims[1] - 1))
            vs.append((x, y, 0))

    vs_flat = list(sum(vs, ()))
    cs = []
    for x, y, _ in vs:
        cs.extend((int(x * 255), int(y * 255), 180, 255))

    program = get_default_shader()
    _vlist = program.vertex_list(
        len(vs_flat) // 3,
        gl.GL_POINTS,
        batch=batch,
        position=("f", vs_flat),
        colors=("Bn", cs),
    )

    gl.glClearColor(0.05, 0.07, 0.09, 1.0)
    pyglet.app.run()


if __name__ == "__main__":
    main()
