__all__ = ["parse_input"]

from ._restroom_redoubt import _Robot


def parse_input(path: str) -> list[_Robot]:
    robots = []
    with open(path, "r") as file:
        while line := file.readline().strip("\n").replace("p=", "").replace("v=", ""):
            p, v = line.split()
            px, py = p.split(",")
            vx, vy = v.split(",")
            robots.append(
                _Robot(
                    position=(int(px), int(py)),
                    velocity=(int(vx), int(vy)),
                )
            )
    return robots
