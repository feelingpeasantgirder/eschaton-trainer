# Contributing to Guns of Eschaton Trainer

Thanks for wanting to help out. This is a community project and PRs are welcome.

## Ground rules

- Keep patches focused. One feature or fix per PR.
- Match existing style (PEP 8, type hints where practical).
- New offsets / signatures go into `eschaton_trainer/signatures/` and must
  include the game build number they were verified against.
- Do not commit compiled binaries, dumps, or memory snapshots.

## Local setup

```bash
git clone https://github.com/eschaton-community/eschaton-trainer
cd eschaton-trainer
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m eschaton_trainer --dry-run
```

## Reporting broken offsets

Open an issue with:
1. Game version (shown in the main menu footer)
2. Trainer log (`logs/trainer.log`)
3. What feature broke and what you expected

## Code of conduct

Be cool. No harassment, no leaking other people's private info.