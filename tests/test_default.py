from pytest import fixture

from lazymap import LazyMap


@fixture
def lazy_map() -> LazyMap[int, int]:
    return LazyMap({1: 1}, default=lambda k: -k)


def test_getitem(lazy_map: LazyMap[int, int]) -> None:
    assert lazy_map[1] == 1
    assert lazy_map[2] == -2
