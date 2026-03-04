import math
from pathlib import Path

import pyglet
from pyglet import gl
from pyglet.graphics import get_default_shader
from pyglet.math import Mat4, Vec3


window = pyglet.window.Window(width=720, height=480, resizable=True)
batch = pyglet.graphics.Batch()

base_positions: list[float] = []
vertex_list = None
angle = 0.0


def _load_obj_triangles(path: Path) -> tuple[list[tuple[float, float, float]], list[tuple[int, int, int]]]:
    vertices: list[tuple[float, float, float]] = []
    triangles: list[tuple[int, int, int]] = []

    with path.open("r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if line.startswith("v "):
                _, x, y, z = line.split(maxsplit=3)
                vertices.append((float(x), float(y), float(z)))
            elif line.startswith("f "):
                parts = line.split()[1:]
                face: list[int] = []
                for part in parts:
                    idx = int(part.split("/")[0]) - 1
                    face.append(idx)
                for i in range(1, len(face) - 1):
                    triangles.append((face[0], face[i], face[i + 1]))

    return vertices, triangles


def _set_camera(width: int, height: int) -> None:
    h = max(height, 1)
    gl.glViewport(0, 0, width, h)
    window.projection = Mat4.perspective_projection(aspect=width / h, z_near=0.1, z_far=100.0, fov=60)
    window.view = Mat4.look_at(position=Vec3(2.7, 2.0, 3.5), target=Vec3(0, 0, 0), up=Vec3(0, 1, 0))


@window.event
def on_draw():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    batch.draw()


@window.event
def on_resize(width, height):
    _set_camera(width, height)
    return pyglet.event.EVENT_HANDLED


def _update(dt: float) -> None:
    global angle
    angle += dt * 1.2
    cos_y = math.cos(angle)
    sin_y = math.sin(angle)
    cos_x = math.cos(angle * 0.7)
    sin_x = math.sin(angle * 0.7)

    rotated: list[float] = []
    for i in range(0, len(base_positions), 3):
        x = base_positions[i]
        y = base_positions[i + 1]
        z = base_positions[i + 2]

        x1 = x * cos_y + z * sin_y
        z1 = -x * sin_y + z * cos_y
        y2 = y * cos_x - z1 * sin_x
        z2 = y * sin_x + z1 * cos_x
        rotated.extend((x1, y2, z2))

    vertex_list.position = rotated


def main(model: str = "cube") -> None:
    global vertex_list, base_positions

    model_paths = {
        "cube": "cube.obj",
        "logo3d": "logo3d.obj",
    }
    obj_path = Path(__file__).resolve().parents[1] / "assets" / model_paths.get(model, "cube.obj")
    vertices, triangles = _load_obj_triangles(obj_path)
    if not vertices:
        raise RuntimeError(f"No vertices found in {obj_path}")
    if not triangles:
        raise RuntimeError(f"No faces found in {obj_path}")

    base_positions = []
    colors: list[int] = []
    for ia, ib, ic in triangles:
        for idx in (ia, ib, ic):
            x, y, z = vertices[idx]
            base_positions.extend((x, y, z))
            colors.extend((int((x + 1.0) * 127.5), int((y + 1.0) * 127.5), int((z + 1.0) * 127.5), 255))

    program = get_default_shader()
    vertex_list = program.vertex_list(
        len(base_positions) // 3,
        gl.GL_TRIANGLES,
        batch=batch,
        position=("f", base_positions),
        colors=("Bn", colors),
    )

    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glClearColor(0.04, 0.04, 0.06, 1.0)
    _set_camera(window.width, window.height)
    pyglet.clock.schedule_interval(_update, 1 / 60.0)
    pyglet.app.run()


if __name__ == "__main__":
    main()
