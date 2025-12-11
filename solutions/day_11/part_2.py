import logging
from collections import Counter

from solutions.types import Section

logger = logging.getLogger(__name__)


type NodeDict = dict[str, list[str]]
type NodeResult = dict[str, int]


def solve(inputs: Section) -> int:
    nodes = read_nodes(inputs)
    start_node_name = "svr"
    start_node = nodes[start_node_name]
    memo: dict[str, NodeResult] = {}
    return find_paths(nodes, memo, start_node).get("all", 0)


def find_paths(
    nodes: NodeDict, memo: dict[str, NodeResult], destinations: list[str]
) -> dict[str, int]:
    count: Counter[str] = Counter()
    for dest in destinations:
        reached: NodeResult
        if dest == "out":
            reached = {"out": 1}
        else:
            reached = (
                memo[dest] if dest in memo else find_paths(nodes, memo, nodes[dest])
            )
            if dest == "dac":
                reached["dac"] = reached["out"]
                reached["all"] = reached["fft"] if "fft" in reached else 0
            elif dest == "fft":
                reached["fft"] = reached["out"]
                reached["all"] = reached["dac"] if "dac" in reached else 0
            memo[dest] = reached
        count += Counter(reached)

    return count


def read_nodes(values: Section) -> NodeDict:
    nodes: NodeDict = {}
    for val in values:
        id_, destinations = val.split(": ")
        destinations = destinations.split(" ")
        nodes[id_] = destinations
    return nodes
