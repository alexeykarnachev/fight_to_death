import pygame

from fight_to_death.settings import Settings


class Game:
    def __init__(self) -> None:
        self._dt = 1.0 / 60.0
        self._settings = Settings()

        pygame.display.init()
        pygame.display.set_caption("FIGHT TO DEATH")

        width, height = map(int, self._settings.graphics.resolution.split("x"))
        flags = pygame.FULLSCREEN if self._settings.graphics.is_fullscreen else 0

        self._screen = pygame.display.set_mode(
            (width, height),
            flags,
            vsync=self._settings.graphics.is_vsync,
        )

        self._clock = pygame.time.Clock()
        self._player_pos = pygame.Vector2(width // 2, height // 2)
        self._is_running = False

    def _update(self):
        for event in pygame.event.get():
            self._is_running = event.type != pygame.QUIT

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self._player_pos.y -= 300 * self._dt
        if keys[pygame.K_s]:
            self._player_pos.y += 300 * self._dt
        if keys[pygame.K_a]:
            self._player_pos.x -= 300 * self._dt
        if keys[pygame.K_d]:
            self._player_pos.x += 300 * self._dt

    def _draw(self):
        self._screen.fill("gray20")
        pygame.draw.circle(self._screen, "red", self._player_pos, 40)
        pygame.display.flip()

    def run(self):
        self._is_running = True
        accum_time = 0

        while self._is_running:
            accum_time += self._clock.tick() / 1000.0

            while accum_time >= self._dt:
                self._update()
                accum_time -= self._dt

            self._draw()
