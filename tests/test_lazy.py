from pytest import FixtureRequest, fixture, param

from lazymap import LazyMap


@fixture(
    params=(
        param(LazyMap(), id="empty"),
        param(LazyMap({1: 1}), id="static"),
        param(LazyMap(lazy={1: lambda: 1}), id="lazy"),
        param(LazyMap(default=lambda _: 0), id="default"),
    )
)
def lazy_map(request: FixtureRequest) -> LazyMap[int, int]:
    return request.param


def test_lazy(lazy_map: LazyMap[int, int]) -> None:
    lazy_map.lazy(1, lambda: -1)
    lazy_map.lazy(2, lambda: -2)
    assert lazy_map[1] == -1
    assert lazy_map[2] == -2
