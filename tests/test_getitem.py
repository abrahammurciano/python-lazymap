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


def test_getitem(lazy_map: LazyMap[int, int]) -> None:
    assert lazy_map[1] == 1


def test_getitem_missing(lazy_map: LazyMap[int, int]) -> None:
    with raises(KeyError):
        lazy_map[2]
