from typing import Dict, Any
from .config import Config

from invoke import Context, Result
from paramiko import SSHClient
from paramiko.transport import Transport


class Connection(Context):
    host: str
    original_host: str
    user: str
    port: int
    ssh_config: str
    gateway: Connection | str
    forward_agent: bool
    connect_timeout: int
    connect_kwargs: Dict[str, str]
    client: SSHClient
    transport: Transport
    def __init__(
        self,
        host: str,
        user: str = ...,
        port: int = ...,
        config: Config = ...,
        gateway: Connection | str = ...,
        forward_agent: bool = ...,
        connect_timeout: int = ...,
        connect_kwargs: Dict[str, str] = ...,
        inline_ssh_env: bool = ...,
    ) -> None: ...
    def sudo(self, command: str, **kwargs: Any) -> Result: ...
    def run(self, command: str, **kwargs: Any) -> Result: ...
