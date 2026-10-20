import re

import pymem


def pattern_to_regex(pattern: str) -> re.Pattern:
    parts = []
    for tok in pattern.split():
        if tok in ("??", "?"):
            parts.append(b".")
        else:
            parts.append(re.escape(bytes([int(tok, 16)])))
    return re.compile(b"".join(parts), re.DOTALL)


def scan_module(pm: pymem.Pymem, module_name: str, pattern: str) -> int | None:
    module = pymem.process.module_from_name(pm.process_handle, module_name)
    if module is None:
        return None
    data = pm.read_bytes(module.lpBaseOfDll, module.SizeOfImage)
    rx = pattern_to_regex(pattern)
    m = rx.search(data)
    if not m:
        return None
    return module.lpBaseOfDll + m.start()