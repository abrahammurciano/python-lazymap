from pytest import FixtureRequest, fixture, param

from lazymap import LazyMap


@fixture(
    params=(
        param(LazyMap({1: []}), id="static"),
        param(LazyMap(lazy={1: list}, cache=True), id="lazy"),
        param(LazyMap(default=lambda _: [], cache=True), id="default"),
    )
)
def cached_map(request: FixtureRequest) -> LazyMap[int, list]:
    return request.param


def test_cache(cached_map: LazyMap[int, list]) -> None:
    first = cached_map[1]
    second = cached_map[1]
    assert first is second
    assert first == []


@fixture(
    params=(
        param(LazyMap(lazy={1: list}, cache=False), id="lazy"),
        param(LazyMap(default=lambda _: [], cache=False), id="default"),
    )
)
def uncached_map(request: FixtureRequest) -> LazyMap[int, list]:
    return request.param


def test_no_cache(uncached_map: LazyMap[int, list]) -> None:
    first = uncached_map[1]
    second = uncached_map[1]
    assert first is not second
    assert first == second == []


def test_change_cache() -> None:
    lazy_map: LazyMap[int, list] = LazyMap()
    lazy_map.lazy(1, lambda: [])
    first = lazy_map[1]
    second = lazy_map[1]
    assert first is second
    lazy_map.lazy(1, lambda: [], cache=False)
    first = lazy_map[1]
    second = lazy_map[1]
    assert first is not second
