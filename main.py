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
        self.is_throw = False
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
        self.throw_left = False
        self.throw = False
        self.falling = False
        self.fallen = False
        self.firstBall = True
        self.win = False
        self.image = py.image.load("images\\ball.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 60
        self.rect.y = 60

    def move_left_left_boy(self):
        if self.x > -10:
            self.x -= 5

    def move_right_left_boy(self):
        if self.x < 250:
            self.x += 5

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def draw_left_boy(self, screen):
        self.x = 180
        self.y = 320
        screen.blit(self.image, (self.x, self.y))

    def jump_left_boy(self):
        self.is_jump = True

    def jump_move(self):
        self.y -= self.jump_vel
        self.jump_vel -= 5
        if self.jump_vel < -20:
            self.is_jump = False
            self.jump_vel = 20

    def throwing(self):
        if self.throw_right:
            if self.vel_height <= 0:
                self.falling = True
            if not self.falling:
                if self.vel_height > 0:
                    self.x += self.velocity[0]
                    self.y += self.velocity[1]
                    self.vel_height -= self.velocity[0]
            else:
                self.x += self.velocity[0]
                self.y += self.velocity[0]
                if self.vel_height != 100:
                    self.vel_height += self.velocity[0]
                if self.y == 330:
                    self.vel_height = 150
                    self.falling = False
                    self.throw = False
                    self.fallen = True
        if self.throw_left:
            if self.vel_height <= 0:
                self.falling = True
            if not self.falling:
                if self.vel_height > 0:
                    self.x -= self.velocity[0]
                    self.y += self.velocity[1]
                    self.vel_height -= self.velocity[0]
            else:
                self.x -= self.velocity[0]
                self.y -= self.velocity[1]
                if self.vel_height != 100:
                    self.vel_height += self.velocity[0]
                if self.y == 330:
                    self.vel_height = 150
                    self.falling = False
                    self.throw = False
                    self.fallen = True


clock = pygame.time.Clock()

py.init()
py.font.init()
py.display.set_caption("Volley")
textfont = py.font.SysFont("Aerial", 30)
textFinish = py.font.SysFont("Aerial", 60)
icon = py.image.load("images\icon.png")
py.display.set_icon(icon)
screen = py.display.set_mode((670, 450))
backgroundImage = py.image.load("images\\background3.png")
stick = pygame.Surface((10, 200))
animation = 0
player2 = Player(120, 250, 70, 50, "images\\rigth\sprite_man_14.png", True)
player1 = Player(450, 250, 70, 50, "images/left/sprite_man_11.png", False)
ball = Ball(200, 200)
player1.spawn()
player2.spawn()
run = True
ball.draw_left_boy(screen)
ball.withBallLeft = True
wall = pygame.Rect(0, 0, 10, 200)
wall.x = 330
wall.y = 200
left_boy_catched = False

firstScore = 0
secondScore = 0
finish = False
while run:
    keys = py.key.get_pressed()
    if ball.x == 330 and left_boy_catched and not ball.firstBall:
        firstScore += 1

    if ball.x == 330 and not left_boy_catched and not ball.firstBall:
        secondScore += 1

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

    if abs(ball.x - player2.x) < 30 and abs(ball.y - player2.y) < 30 and left_boy_catched and player2.is_jump:
        ball.vel_height = 150
        ball.falling = False
        ball.throw_right = True
        ball.throw_left = False
        left_boy_catched = False

    if abs(ball.x - player1.x) < 30 and abs(ball.y - player1.y) < 30 and not left_boy_catched and player1.is_jump:
        ball.vel_height = 150
        ball.throw_left = True
        ball.throw_right = False
        ball.firstBall = False
        ball.falling = False
        left_boy_catched = True

    if abs(ball.x - 320) < 20 and abs(ball.y - 200) < 20:
        ball.throw = False
        finish = True

    if ball.fallen:
        finish = True

    if finish:
        if secondScore > firstScore:
            textFinish = textfont.render("Left player is win", True, (0, 0, 0))
        elif secondScore < firstScore:
            textFinish = textfont.render("Right player is win", True, (0, 0, 0))
        else:
            textFinish = textfont.render("Draw", True, (0, 0, 0))
        screen.blit(textFinish, (270, 100))

    if ball.throw:
        ball.throwing()
    py.display.update()
    screen.blit(backgroundImage, (0, 0))
    pygame.draw.rect(screen, (0, 0, 0), wall)
    player1.draw(screen)
    player2.draw(screen)
    ball.draw(screen)
    textScore = textfont.render("Score " + str(secondScore) + " : " + str(firstScore), True, (0, 0, 0))

    screen.blit(textScore, (50, 20))
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
            py.quit()

    clock.tick(25)