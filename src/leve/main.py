from typing import List, Optional
import functools

TRACE_CACHE = False

if TRACE_CACHE:

    def dump_cache(cache):
        for row in cache:
            for item in row:
                print(("-" if item is None else str(item)).ljust(3), end=" ")
            print()
        print()
else:

    def dump_cache(*args): ...


def _lev_impl_cache(
    s1: str, s2: str, n1: int, n2: int, cache: List[List[Optional[int]]]
) -> int:
    """Recursive way of doing it, but with custom cache"""
    if cache[n1][n2] is not None:
        return cache[n1][n2]
    if n1 == 0:
        cache[n1][n2] = n2
        dump_cache(cache)
        return cache[n1][n2]
    if n2 == 0:
        cache[n1][n2] = n1
        dump_cache(cache)
        return cache[n1][n2]
    if s1[n1 - 1] == s2[n2 - 1]:
        cache[n1][n2] = _lev_impl_cache(s1, s2, n1 - 1, n2 - 1, cache)
        dump_cache(cache)
        return cache[n1][n2]

    cache[n1][n2] = 1 + min(
        _lev_impl_cache(s1, s2, n1 - 1, n2, cache),  # added
        _lev_impl_cache(s1, s2, n1, n2 - 1, cache),  # removed
        _lev_impl_cache(s1, s2, n1 - 1, n2 - 1, cache),  # replaced
    )
    dump_cache(cache)
    return cache[n1][n2]


@functools.lru_cache()
def _lev_impl(s1: str, s2: str, n1: int, n2: int) -> int:
    """
    Recursive way of doing it, with builtin python functools cache
    """
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if s1[n1 - 1] == s2[n2 - 1]:
        return _lev_impl(s1, s2, n1 - 1, n2 - 1)
    return 1 + min(
        _lev_impl(s1, s2, n1 - 1, n2),  # added
        _lev_impl(s1, s2, n1, n2 - 1),  # removed
        _lev_impl(s1, s2, n1 - 1, n2 - 1),  # replaced
    )


def _lev_impl_iter(s1: str, s2: str) -> int:
    n1, n2 = len(s1), len(s2)
    cache: List[List[Optional[int]]] = [[None] * (n2 + 1) for _ in range(n1 + 1)]
    for n2 in range(len(s2) + 1):
        n1 = 0
        cache[n1][n2] = n2
        dump_cache(cache)

    for n1 in range(len(s1) + 1):
        n2 = 0
        cache[n1][n2] = n1
        dump_cache(cache)

    for n1 in range(1, len(s1) + 1):
        for n2 in range(1, len(s2) + 1):
            if s1[n1 - 1] == s2[n2 - 1]:
                cache[n1][n2] = cache[n1 - 1][n2 - 1]
                dump_cache(cache)
                continue
            cache[n1][n2] = 1 + min(
                cache[n1 - 1][n2],
                cache[n1][n2 - 1],
                cache[n1 - 1][n2 - 1],
            )
            dump_cache(cache)
    return cache[n1][n2]


def edit_distance(s1: str, s2: str) -> int:
    """Returs the lavenstein edit distance between two strings"""
    return _lev_impl_iter(s1, s2)
