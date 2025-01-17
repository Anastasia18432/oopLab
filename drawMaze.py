import classNode as cn
from generateMaze import generateMaze
import pygame

example = 0
FPS = 60


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.image = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.x * self.width, self.y * self.height))


def draw_maze(maze):
    pygame.init()
    pygame.display.set_caption("Maze")
    screen = pygame.display.set_mode((525, 525))
    running = True
    walls = pygame.sprite.Group()
    for node in maze.maze:
        if node.isWall:
            wall = Wall(node.coordinates[0], node.coordinates[1], 25, 25, "handpaintedwall2.png", screen)
            walls.add(wall)
            wall.draw()
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    maze = generateMaze((21, 21))

    instance = cn.Node((1, 1))
    draw_maze(maze)