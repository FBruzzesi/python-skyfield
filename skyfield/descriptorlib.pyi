from typing import Callable, Generic, TypeVar, overload

_T = TypeVar("_T")
_Owner = TypeVar("_Owner")

class reify(Generic[_T]):
    method: Callable[..., _T]
    __name__: str
    __doc__: str | None
    def __init__(self, method: Callable[..., _T]) -> None: ...
    @overload
    def __get__(self, instance: None, objtype: type[_Owner]) -> reify[_T]: ...
    @overload
    def __get__(self, instance: _Owner, objtype: type[_Owner] | None = ...) -> _T: ...
    def __get__(self, instance: _Owner | None, objtype: type[_Owner] | None = ...) -> reify[_T] | _T: ...
