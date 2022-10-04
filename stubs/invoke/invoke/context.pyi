from contextlib import AbstractContextManager
from typing import overload

from .config import Config, DataProxy
from .runners import Result

class Context(DataProxy):
    def __init__(self, config: Config | None = ...) -> None: ...
    @property
    def config(self) -> Config: ...
    @config.setter
    def config(self, value: Config) -> None: ...
    def run(self, command: str, **kwargs) -> Result: ...
    @overload
    def sudo(self, command: str, *, password: str = ..., user: str = ..., **kwargs) -> Result: ...
    @overload
    def sudo(self, command: str, **kwargs) -> Result: ...
    def prefix(self, command: str) -> AbstractContextManager[None]: ...
    @property
    def cwd(self) -> str: ...
    def cd(self, path: str) -> AbstractContextManager[None]: ...

class MockContext(Context):
    def __init__(self, config: Config | None = ..., **kwargs) -> None: ...
    def run(self, command: str, *args, **kwargs): ...
    def sudo(self, command: str, *args, **kwargs): ...
    def set_result_for(self, attname, command, result) -> None: ...
