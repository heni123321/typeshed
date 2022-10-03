from invoke.config import Config as InvokeConfig, merge_dicts

from stdlib.typing import Any


class Config(InvokeConfig):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
