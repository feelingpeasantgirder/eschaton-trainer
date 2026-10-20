import ctypes
import logging
import struct

import pymem

log = logging.getLogger("eschaton.mem")

PROCESS_ALL_ACCESS = 0x1F0FFF


class MemoryReader:
    def __init__(self, pid: int):
        self.pid = pid
        self._pm: pymem.Pymem | None = None

    def attach(self) -> None:
        self._pm = pymem.Pymem()
        self._pm.open_process_from_id(self.pid)
        log.debug("opened handle to pid=%d", self.pid)

    def read_int(self, address: int) -> int:
        assert self._pm is not None, "attach() not called"
        return self._pm.read_int(address)

    def read_float(self, address: int) -> float:
        assert self._pm is not None
        return self._pm.read_float(address)

    def read_bytes(self, address: int, size: int) -> bytes:
        assert self._pm is not None
        return self._pm.read_bytes(address, size)

    def write_int(self, address: int, value: int) -> None:
        assert self._pm is not None
        self._pm.write_int(address, value)

    def write_float(self, address: int, value: float) -> None:
        assert self._pm is not None
        self._pm.write_float(address, value)

    def resolve_pointer(self, base: int, offsets: list[int]) -> int:
        addr = self.read_int(base)
        for off in offsets[:-1]:
            addr = self.read_int(addr + off)
        return addr + offsets[-1]