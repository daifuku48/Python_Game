import pygame
import pygame as py


class Player:
    def __init__(self, x, y, width, height, stay_image, right_left):
        super().__init__()
        self.x = x
        self.y = y
        self.spawn_x = x
        self.spawn_y = y
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

    def spawn(self):
        self.x = self.spawn_x
        self.y = self.spawn_y

    def jump(self):
        self.is_jump = True

    def jump_move(self):
        self.y -= self.jump_vel
        self.jump_vel -= 5
        if self.jump_vel < -20:
            self.is_jump = False
            self.jump_vel = 20

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_jump = False
        self.radius = 10
        self.color = (255, 255, 255)
        self.velocity = [5, -5]
        self.withBallLeft = True
        self.jump_vel = 20
        self.vel_height = 250
        self.throw_right = True
        self.throw = False
        self.falling = False
        self.image = py.image.load("images\\ball.png")
        self.image = pygame.transform.scale(self.image, (60, 60))

    def move_left_left_boy(self):
        if self.x > -10:
            self.x -= 5

    def move_right_left_boy(self):
        if self.x < 250:
            self.x += 5

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def collide(self, player):
        if abs(self.x - player.x) < 50 and abs(self.y - player.y) < 50:
            self.velocity[1] = -self.velocity[1]
            self.x += self.velocity[0] * 2

    def draw_left_boy(self, screen):
        self.x = 180
        self.y = 320
        screen.blit(self.image, (self.x, self.y))

    def check_bounds(self):
        if self.x < 0 or self.x > 670:
            self.x = 330
            self.y = 200
            player1.has_ball = True
            player2.has_ball = False

        if self.y < 0 or self.y > 450:
            self.velocity[1] = -self.velocity[1]

    def jump_left_boy(self):
        self.is_jump = True

    def jump_move(self):
        self.y -= self.jump_vel
        self.jump_vel -= 5
        if self.jump_vel < -20:
            self.is_jump = False
            self.jump_vel = 20

    def throwing(self):
        if self.vel_height <= 0:
            self.falling = True
        if not self.falling:
            if self.throw_right:
                if self.vel_height > 0:
                    self.x += self.velocity[0]
                    self.y += self.velocity[1]
                    self.vel_height -= self.velocity[0]
        else:
            self.x += self.velocity[0]
            self.y += self.velocity[0]
            if self.vel_height != 100:
                self.vel_height += self.velocity[0]
            if self.y == 250:
                self.vel_height = 100
                self.falling = False

clock = pygame.time.Clock()

py.init()
py.display.set_caption("Volley")
icon = py.image.load("images\icon.png")
py.display.set_icon(icon)
screen = py.display.set_mode((670, 450))
backgroundImage = py.image.load("images\\background3.png")
stick = pygame.Surface((10, 180))
animation = 0
player2 = Player(120, 250, 70, 50, "images\\rigth\sprite_man_14.png", True)
player1 = Player(450, 250, 70, 50, "images/left/sprite_man_11.png", False)
ball = Ball(200, 200)
player1.spawn()
player2.spawn()
run = True
ball.draw_left_boy(screen)
ball.withBallLeft = True
while run:
    py.display.update()
    screen.blit(backgroundImage, (0, 0))
    screen.blit(stick, (330, 200))
    player1.draw(screen)
    player2.draw(screen)
    keys = py.key.get_pressed()
    ball.draw(screen)

    if keys[py.K_LEFT]:
        player1.move_left()

    if keys[py.K_RIGHT]:
        player1.move_right()

    if keys[py.K_UP] and not player1.is_jump:
        player1.jump()

    if player1.is_jump:
        player1.jump_move()

    if keys[py.K_w] and not player2.is_jump and not ball.withBallLeft:
        player2.jump()

    if player2.is_jump and not ball.withBallLeft:
        player2.jump_move()

    if keys[py.K_a] and not ball.withBallLeft:
        player2.move_left()

    if keys[py.K_d] and not ball.withBallLeft:
        player2.move_right()

    if keys[py.K_a] and ball.withBallLeft:
        player2.move_left()
        ball.move_left_left_boy()

    if keys[py.K_d] and ball.withBallLeft:
        player2.move_right()
        ball.move_right_left_boy()

    if keys[py.K_w] and not player2.is_jump and ball.withBallLeft and not ball.is_jump:
        player2.jump()
        ball.jump_left_boy()

    if player2.is_jump and ball.is_jump:
        player2.jump_move()
        ball.jump_move()

    if keys[py.K_SPACE]:
        ball.withBallLeft = False
        ball.throw = True

    if ball.throw:
        ball.throwing()

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
            py.quit()

    clock.tick(30)
