#!/usr/bin/env python3
"""Annotate the below function’s parameters and return
values with the appropriate types"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return anything"""
    if lst:
        return lst[0]
    else:
        return None
