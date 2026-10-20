"""Signatures verified against Guns of Eschaton build 2026.03.1178."""

BUILD = "2026.03.1178"

SIGNATURES = {
    "player_base": {
        "module_base": "Eschaton.exe",
        "pattern": "48 8B 05 ?? ?? ?? ?? 48 85 C0 74 ?? 48 8B 88",
        "offsets": [0x0, 0x18, 0x2A0],
    },
    "weapon_ptr": {
        "module_base": "Eschaton.exe",
        "pattern": "48 8D 15 ?? ?? ?? ?? 48 8B 0D ?? ?? ?? ?? E8",
        "offsets": [0x8, 0x40],
    },
    "world_tick": {
        "module_base": "Eschaton.exe",
        "pattern": "F3 0F 11 05 ?? ?? ?? ?? F3 0F 10 05",
        "offsets": [0x0],
    },
}