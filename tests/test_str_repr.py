from lazymap import LazyMap


def test_str_evaluates() -> None:
    container = [0]
    lazy_map = LazyMap(lazy={1: container.pop})
    assert str(lazy_map) == "LazyMap({1: 0})"
    assert not container


def test_repr_not_evaluated() -> None:
    container = [0]
    lazy_map = LazyMap(lazy={1: container.pop})
    assert repr(lazy_map) == "LazyMap({1: <lazy>})"
    assert container
