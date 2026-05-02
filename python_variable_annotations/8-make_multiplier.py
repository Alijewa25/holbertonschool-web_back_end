#!/usr/bin/env python3
"""function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """izah"""
    def inner(x: float) -> float:
        return x * multiplier
    return inner
