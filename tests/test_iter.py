from typing import Set, Tuple

from pytest import FixtureRequest, fixture, param

from lazymap import LazyMap


@fixture(
    params=(
        param((LazyMap(), set()), id="empty"),
        param((LazyMap({1: 1}), {1}), id="static"),
        param((LazyMap(lazy={1: lambda: 1}), {1}), id="lazy"),
        param((LazyMap(default=lambda _: 0), set()), id="default"),
        param((LazyMap({1: 1}, lazy={2: lambda: 2}), {1, 2}), id="static_getters"),
        param((LazyMap({1: 1}, default=lambda _: 0), {1}), id="static_default"),
        param(
            (LazyMap(lazy={1: lambda: 1}, default=lambda _: 0), {1}),
            id="getters_default",
        ),
        param(
            (LazyMap({1: 1}, lazy={2: lambda: 2}, default=lambda _: 0), {1, 2}),
            id="static_getters_default",
        ),
    )
)
def lazy_map_and_keys(request: FixtureRequest) -> Tuple[LazyMap[int, int], Set[int]]:
    return request.param


def test_iter(lazy_map_and_keys: Tuple[LazyMap[int, int], Set[int]]) -> None:
    lazy_map, keys = lazy_map_and_keys
    assert set(lazy_map) == keys
    assert len(lazy_map) == len(keys)
    assert len(lazy_map) == len(keys)
