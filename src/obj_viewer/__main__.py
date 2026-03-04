import argparse
import importlib
from typing import Callable


DEMOS: dict[str, str] = {
    "shapes": "obj_viewer.demos.shapes_demo",
    "model": "obj_viewer.demos.model_demo",
    "tri": "obj_viewer.demos.tri_demo",
    "field": "obj_viewer.demos.field_demo",
    "shader": "obj_viewer.demos.shader_demo",
}


def _run_demo(name: str, model: str) -> None:
    module_name = DEMOS[name]
    module = importlib.import_module(module_name)
    demo_main = getattr(module, "main", None)
    if not callable(demo_main):
        raise RuntimeError(f"Demo module '{module_name}' has no callable main()")
    if name == "model":
        runner: Callable[[], None] = lambda: demo_main(model=model)
    else:
        runner = demo_main
    runner()


def main() -> None:
    parser = argparse.ArgumentParser(description="Run obj-viewer demos.")
    parser.add_argument(
        "--demo",
        choices=sorted(DEMOS.keys()),
        default="model",
        help="Demo to run (default: model)",
    )
    parser.add_argument(
        "--model",
        choices=("cube", "logo3d"),
        default="cube",
        help="Model asset for --demo model (default: cube)",
    )
    args = parser.parse_args()
    _run_demo(args.demo, args.model)


if __name__ == "__main__":
    main()
