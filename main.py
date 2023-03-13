import pygame
import pygame as py


class Player:
    def __init__(self, x, y, width, height, stay_image, right_left):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5  # скорость передвижения
        self.is_jump = False
        self.jump_count = 10
        self.walk_count = 0
        self.left = False
        self.right = False
        self.standing = True
        self.jump_height = 10
        self.jump_vel = 20
        self.walk_right = [pygame.image.load("images\\rigth\sprite_man_13.png"),
                           pygame.image.load("images\\rigth\sprite_man_14.png"),
                           pygame.image.load("images\\rigth\sprite_man_15.png")]

        self.walk_left = [pygame.image.load("images\left\sprite_man_10.png"),
                          pygame.image.load("images\left\sprite_man_09.png"),
                          pygame.image.load("images\left\sprite_man_11.png")]
        self.stand = pygame.image.load(stay_image)
        self.image = self.stand
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.orientation = right_left
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def move_left(self):
        self.image = self.walk_left[self.walk_count]

        if self.walk_count == 2:
            self.walk_count = 0
        else:
            self.walk_count = self.walk_count + 1
        if self.orientation:
            if self.x > -10:
                self.x -= self.vel
        else:
            if self.x > 330:
                self.x -= self.vel

    def move_right(self):
        self.image = self.walk_right[self.walk_count]

        if self.walk_count == 2:
            self.walk_count = 0
        else:
            self.walk_count = self.walk_count + 1
        if self.orientation:
            if self.x < 230:
                self.x += self.vel
        else:
            if self.x < 570:
                self.x += self.vel

    def jump(self):
        self.is_jump = True

    def jump_move(self):
        self.y -= self.jump_vel
        self.jump_vel -= 5
        if self.jump_vel < -20:
            self.is_jump = False
            self.jump_vel = 20

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


clock = pygame.time.Clock()

py.init()
py.display.set_caption("Volley")
icon = py.image.load("images\icon.png")
py.display.set_icon(icon)
screen = py.display.set_mode((670, 450))
backgroundImage = py.image.load("images\\background3.png")
stick = pygame.Surface((10, 180))
walk_left = [
    pygame.image.load("images\left\sprite_man_10.png"),
    pygame.image.load("images\left\sprite_man_09.png"),
    pygame.image.load("images\left\sprite_man_11.png")
]
walk_rigth = [
    pygame.image.load("images\\rigth\sprite_man_14.png"),
    pygame.image.load("images\\rigth\sprite_man_13.png"),
    pygame.image.load("images\\rigth\sprite_man_15.png")
]

walk_stay_right = [
    pygame.image.load("images\sprite_man_rigth_stay.png")
]

walk_stay_left = [
    pygame.image.load("images\sprite_man_stay_left2.png"),
]

animation = 0
player2 = Player(170, 245, 70, 50, "images\\rigth\sprite_man_14.png", True)
player1 = Player(500, 245, 70, 500, "images/left/sprite_man_11.png", False)

tr = True
while tr:
    py.display.update()
    screen.blit(backgroundImage, (0, 0))
    screen.blit(stick, (330, 200))
    player1.draw(screen)
    player2.draw(screen)
    keys = py.key.get_pressed()

    if keys[py.K_LEFT]:
        player1.move_left()

    if keys[py.K_RIGHT]:
        player1.move_right()

    if keys[py.K_UP] and player1.is_jump == False:
        player1.jump()

    if player1.is_jump:
        player1.jump_move()

    if keys[py.K_w] and player2.is_jump == False:
        player2.jump()

    if player2.is_jump:
        player2.jump_move()

    if keys[py.K_a]:
        player2.move_left()

    if keys[py.K_d]:
        player2.move_right()

    for event in py.event.get():
        if event.type == py.QUIT:
            tr = False
            py.quit()

    clock.tick(40)
