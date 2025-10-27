from __future__ import annotations
from dataclasses import dataclass
from typing import Literal, Dict, TypedDict, Any, cast

type BoundT = str
@dataclass
class MyClass[TVar : BoundT]:
    """
    Documentation comment.
    """

    _x : Literal["Just a regular string..."] = "Just a regular string..."
    
    @property
    def x(self) -> TVar:
        local_variable = 12
        return cast(TVar, self._x + ("." * local_variable))

    def 