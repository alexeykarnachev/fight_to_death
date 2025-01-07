import pygame


class Game:
    def __init__(self) -> None:
        self._screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("FIGHT TO DEATH")
        self._clock = pygame.time.Clock()
        self._player_pos = pygame.Vector2(400, 300)

        self._is_running = False

    def _update(self):
        dt = self._clock.tick(60) / 1000.0

        for event in pygame.event.get():
            self._is_running = event.type != pygame.QUIT

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self._player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            self._player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            self._player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            self._player_pos.x += 300 * dt

    def _draw(self):
        self._screen.fill("gray20")
        pygame.draw.circle(self._screen, "red", self._player_pos, 40)
        pygame.display.flip()

    def run(self):
        self._is_running = True

        while self._is_running:
            self._update()
            self._draw()

        pygame.quit()
