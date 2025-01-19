import pygame

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
    self.velocity *= 100

  def update(self, dt):
    self.position += self.velocity * dt
