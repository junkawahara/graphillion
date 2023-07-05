from graphillion import GraphSet
from graphillion import setset

class VertexSetSet(object):
    # TODO: 引数に入れられる値の種類を増やす
    def __init__(self, vertex_setset_or_constraints=None):
        obj = vertex_setset_or_constraints
        if isinstance(obj, VertexSetSet):
            self._ss = obj._ss.copy()
        elif isinstance(obj, setset):
            self._ss = obj.copy()
        else:
            if obj is None:
                obj = []
            elif isinstance(obj, (set, frozenset, list)): # a list of vertex lists
                for vertices in obj:
                    for vertex in vertices:
                        if vertex not in VertexSetSet._universe_vertices:
                            raise ValueError("invalid vertex:", vertex)

                l = []
                for vertices in obj:
                    l.append([VertexSetSet._vertex2obj[vertex] for vertex in vertices])
                obj = l
            self._ss = setset(obj)

    def copy(self):
        return VertexSetSet(self)

    def __nonzero__(self):
        return bool(self._ss)

    def __bool__(self):
        return bool(self._ss)

    def __repr__(self):
        return setset._repr(self._ss,
                            (self.__class__.__name__ + "([", "])"),
                            ("[", "]"),
                            obj_to_str=VertexSetSet._obj2str)

    @staticmethod
    def set_universe(vertices=None):
        if vertices is None: # adopt the vertex set of GraphSet's underlying graph
            # TODO: 実装する
            return

        assert len(vertices) <= len(setset.universe()), \
               f"the universe is too small, which has at least {len(vertices)} elements"

        vertex_num = len(vertices)
        if vertex_num != len(set(vertices)):
            raise ValueError("duplicated elements found")

        VertexSetSet._universe_vertices = set(vertices)

        low_level_objs = setset._int2obj[:vertex_num + 1]
        # TODO: 内包表記に書き換え
        for i, vertex in enumerate(vertices):
            VertexSetSet._vertex2obj[vertex] = low_level_objs[i + 1]
            VertexSetSet._obj2vertex[low_level_objs[i + 1]] = vertex
            VertexSetSet._obj2str[low_level_objs[i + 1]] = str(vertex)

        # VertexSetSet._universe_vertices = GraphSet._vertices
        # vertex_num = len(VertexSetSet._universe_vertices)


        # VertexSetSet._edges = GraphSet.universe()

        # VertexSetSet._int2edge = setset._int2obj[:vertex_num + 1]
        # vertex_iter = iter(VertexSetSet._universe_vertices)
        # for edge in VertexSetSet._int2edge[1:]:
        #     VertexSetSet._edge2vertex[edge] = next(vertex_iter)

    _universe_vertices = set() # TODO: listかsetか考える
    _vertex2obj = {}
    _obj2vertex = {}
    _obj2str = {}

    # _edges = set()
    # _edge2vertex = {}
    # _edge2int = {}
    # _int2edge = [None]