import logging
import sys

import pygame

from eschaton_trainer.services.feature_service import FeatureService

log = logging.getLogger("eschaton.hud")

BG = (12, 12, 16)
FG = (220, 220, 230)
ACCENT = (255, 90, 60)

KEYBINDS = {
    pygame.K_F1: ("godmode", lambda f: f.set_godmode(True)),
    pygame.K_F2: ("refill ammo", lambda f: f.refill_ammo()),
    pygame.K_F3: ("godmode off", lambda f: f.set_godmode(False)),
}


class OverlayHud:
    def __init__(self, features: FeatureService):
        self.features = features

    def run(self) -> None:
        pygame.init()
        screen = pygame.display.set_mode((420, 260))
        pygame.display.set_caption("Guns of Eschaton Trainer v2.4")
        font = pygame.font.SysFont("consolas", 16)
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key in KEYBINDS:
                    label, fn = KEYBINDS[event.key]
                    log.info("hotkey -> %s", label)
                    try:
                        fn(self.features)
                    except Exception as exc:  # noqa: BLE001
                        log.error("hotkey failed: %s", exc)

            try:
                self.features.refresh()
            except Exception:
                pass

            screen.fill(BG)
            state = self.features.state
            lines = [
                f"HP    {state.health:6.1f} / {state.max_health:.0f}",
                f"AMMO  {state.ammo:6d} (+{state.reserve})",
                f"GOD   {'ON' if state.godmode else 'off'}",
                "",
                "F1 godmode on   F2 refill   F3 godmode off",
            ]
            for i, line in enumerate(lines):
                color = ACCENT if "GOD" in line and state.godmode else FG
                screen.blit(font.render(line, True, color), (16, 16 + i * 22))

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()
        sys.exit(0)