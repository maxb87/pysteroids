import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
    self.velocity *= 100

  def update(self, dt):
    self.position += self.velocity * dt

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)