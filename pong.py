from pygame import *
from random import randint
#фоновая музыка
plyer2_x = 0
plyer2_y = 0
plyer1_x = 0
plyer1_y = 0
speed_x = 10
speed_y = 10

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE', True, (190,0,0))
lose2 = font1.render('PLAYER 2 LOSE', True, (190,0,0))
#нам нужны такие картинки:
img_back = "background.png" #фон игры
img_player = "raketka.png" #герой
img_ball = 'ball.png'
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
 
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
#класс главного
class Player1(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 120:
            self.rect.y += self.speed
        def returncrds():
            plyer1_x = self.rect.x
            plyer1_y = self.rect.y
            return plyer1_x, plyer1_y
class Player2(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 120:
            self.rect.y += self.speed




#Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))


plyer = Player1(img_player, 0, 250, 35, 120, 17)
plyer2 = Player2(img_player, 665, 250, 35, 120, 17)
ball = GameSprite(img_ball, 350, 250, 50, 50, 15)

#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#Основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
           run = False
    if not finish:
        #обновляем фон
        window.blit(background,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        plyer.update()
        plyer.reset()
        plyer2.reset()
        plyer2.update()
        ball.update()
        ball.reset()
    # Проверка того, что шарик столкнулся с блоком
    if sprite.collide_rect(plyer, ball) or sprite.collide_rect(plyer2, ball):
        speed_x *= -1
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if ball.rect.x > 650:
        finish = True
        window.blit(lose2, (200, 200))


    display.update()
    #цикл срабатывает каждую 0.05 секунд
    time.delay(40)