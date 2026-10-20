import argparse
import sys

from eschaton_trainer.bootstrap.launcher import TrainerLauncher


def main() -> int:
    parser = argparse.ArgumentParser(prog="eschaton-trainer")
    parser.add_argument("--dry-run", action="store_true", help="load offsets, do not attach")
    parser.add_argument("--no-overlay", action="store_true", help="skip the pygame overlay")
    parser.add_argument("--config", default="config/default.yaml")
    args = parser.parse_args()

    launcher = TrainerLauncher(config_path=args.config)
    return launcher.run(dry_run=args.dry_run, overlay=not args.no_overlay)


if __name__ == "__main__":
    sys.exit(main())