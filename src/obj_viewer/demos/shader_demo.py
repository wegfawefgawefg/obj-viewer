import pyglet
from pyglet import gl
from pyglet.graphics.shader import Shader, ShaderProgram


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
    vertex_shader_source = """
        #version 330 core
        in vec3 position;
        in vec4 colors;
        out vec4 color_out;
        uniform WindowBlock
        {
            mat4 projection;
            mat4 view;
        } window;
        void main() {
            color_out = colors;
            gl_Position = window.projection * window.view * vec4(position, 1.0);
        }
    """
    fragment_shader_source = """
        #version 330 core
        in vec4 color_out;
        out vec4 frag_color;
        void main() {
            frag_color = color_out;
        }
    """
    program = ShaderProgram(
        Shader(vertex_shader_source, "vertex"),
        Shader(fragment_shader_source, "fragment"),
    )

    verts = (
        160.0, 110.0, 0.0,
        360.0, 410.0, 0.0,
        560.0, 110.0, 0.0,
    )
    cols = (
        255, 80, 80, 255,
        80, 255, 120, 255,
        80, 140, 255, 255,
    )
    _vlist = program.vertex_list(
        3,
        gl.GL_TRIANGLES,
        batch=batch,
        position=("f", verts),
        colors=("Bn", cols),
    )

    gl.glClearColor(0.08, 0.06, 0.08, 1.0)
    pyglet.app.run()


if __name__ == "__main__":
    main()

