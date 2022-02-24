from typing import Type, NamedTuple, Any


def namedtuple_func_name(nt: Type[NamedTuple]) -> str:
    assert hasattr(nt, "_fields"), "Did not receive a valid NamedTuple!"
    return str(nt.__name__.casefold())


def namedtuple_extract_from_annotation(nt: Type[NamedTuple], _type: Any) -> str:
    """
    >>> from typing import NamedTuple; from datetime import datetime
    >>> class Test(NamedTuple): something: datetime
    >>> namedtuple_extract_from_annotation(Test, datetime)
    'something'
    """
    import inspect
    from autotui.typehelpers import get_union_args

    for attr_name, param in inspect.signature(nt).parameters.items():
        attr_type = param.annotation
        # Optional[(<class 'int'>, False)]
        res = get_union_args(attr_type)
        if res := get_union_args(attr_type):
            attr_types, _ = res
            assert len(attr_types) == 1
            attr_type = attr_types[0]

        if attr_type == _type:
            return attr_name
    raise TypeError(f"Could not find {_type} on {nt}")
