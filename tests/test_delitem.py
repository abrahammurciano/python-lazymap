from pytest import FixtureRequest, fixture, param, raises

from lazymap import LazyMap


@fixture(
    params=(
        param(LazyMap({1: 1}), id="static"),
        param(LazyMap(lazy={1: lambda: 1}), id="lazy"),
    )
)
def lazy_map(request: FixtureRequest) -> LazyMap[int, int]:
    return request.param


def test_delitem(lazy_map: LazyMap[int, int]) -> None:
    del lazy_map[1]
    with raises(KeyError):
        lazy_map[1]


@fixture(
    params=(
        param(LazyMap({1: 1}, default=lambda k: -k), id="static"),
        param(LazyMap(lazy={1: lambda: 1}, default=lambda k: -k), id="lazy"),
    )
)
def default_lazy_map(request: FixtureRequest) -> LazyMap[int, int]:
    return request.param


def test_delitem_default(default_lazy_map: LazyMap[int, int]) -> None:
    assert default_lazy_map[1] == 1
    del default_lazy_map[1]
    assert default_lazy_map[1] == -1
