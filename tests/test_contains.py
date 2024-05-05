from pytest import FixtureRequest, fixture, param

from lazymap import LazyMap


@fixture(
    params=(
        param(LazyMap({1: 1}), id="static"),
        param(LazyMap(lazy={1: lambda: 1}), id="lazy"),
    )
)
def lazy_map_with(request: FixtureRequest) -> LazyMap[int, int]:
    return request.param


def test_contains(lazy_map_with: LazyMap[int, int]) -> None:
    assert 1 in lazy_map_with
    assert 2 not in lazy_map_with


@fixture(
    params=(
        param(LazyMap(), id="empty"),
        param(LazyMap(default=lambda k: k), id="default"),
    )
)
def lazy_map_without(request: FixtureRequest) -> LazyMap[int, int]:
    return request.param


def test_not_contains(lazy_map_without: LazyMap[int, int]) -> None:
    assert 1 not in lazy_map_without


def test_contains_lazy() -> None:
    unaffected = [0]
    lazy_map = LazyMap(lazy={1: unaffected.pop})
    assert 1 in lazy_map
    assert unaffected
