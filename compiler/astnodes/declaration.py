from .node import Node
from .identifier import Identifier
from typing import List


class Declaration(Node):
    def __init__(self, location: List[int], kind: str):
        super().__init__(location, kind)

    def getIdentifier(self) -> Identifier:
        raise Exception("Not implemented")
