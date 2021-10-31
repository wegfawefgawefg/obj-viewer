tri_verts = (
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
)

from pprint import pprint

#  flatten the list of tuples with *
tv_flat = list(sum(tri_verts, ()))

pprint(tv_flat)