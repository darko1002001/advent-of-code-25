import logging

from solutions.types import Section

logger = logging.getLogger(__name__)


type NodeDict = dict[str, list[str]]


def solve(inputs: Section) -> int:
    nodes = read_nodes(inputs)
    start_node = nodes["you"]
    return find_paths(nodes, start_node)


def find_paths(nodes: NodeDict, destinations: list[str]) -> int:
    count = 0
    for dest in destinations:
        if dest == "out":
            count += 1
        else:
            count += find_paths(nodes, nodes.get(dest, []))

    return count


def read_nodes(values: Section) -> NodeDict:
    nodes: NodeDict = {}
    for val in values:
        id_, destinations = val.split(": ")
        destinations = destinations.split(" ")
        nodes[id_] = destinations
    return nodes
