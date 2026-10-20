# Security Policy

## Supported versions

| Trainer version | Game build support |
|-----------------|--------------------|
| 2.x             | 2026.x             |
| 1.x             | legacy, no fixes   |

## Reporting a vulnerability

This trainer reads and writes to the Guns of Eschaton process memory.
If you find an issue that could corrupt save data, crash the game, or
leak the user's local paths/logs, please report it privately.

- Email: security@eschaton-trainer.dev (PGP key in `docs/` once we add it)
- Or open a **draft** security advisory on GitHub.

Please do not open public issues for memory-corruption bugs.

## Scope

In scope: the Python trainer, the injected overlay, the offset loader.
Out of scope: the game itself, anti-cheat vendors, third-party mods.

## Disclaimer

Use at your own risk. This project is for single-player / private-coop
educational modding. Using it on official ranked servers violates the
game's ToS and may get your account banned.