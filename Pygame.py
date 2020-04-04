import pygame as pg

pg.init()
# Разрешения окна
Window = pg.display.set_mode((1280, 728))

# Название окна
pg.display.set_caption('MyGame')
run = True

# Настройки Игрока по умолчанию
class Player:
    name = 'Player'
    x = 550
    y = 650
    widht = 50
    high = 50
    speed = 1

pl = Player()

# Настройки которые выбрал игрок
class SettingsPlayer(Player):
    def ChangeSett(self):
        SpeedChange = input('Хотите изменить свою скорость?')
        if SpeedChange == 'Да' or SpeedChange == 'да':
            speeds = int(input('Укажите Скорость'))
            pl.speed = speeds
        if SpeedChange == 'Нет' or SpeedChange == 'нет':
            pl.speed = pl.speed
spl = SettingsPlayer()
spl.ChangeSett()

while run:
    pg.time.delay(100)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    # Считывание кнопок передвижение и другие
    keys = pg.key.get_pressed()
    if keys [pg.K_LEFT]:
        pl.x -= pl.speed

    if keys[pg.K_RIGHT]:
        pl.x += pl.speed
    
    if keys[pg.K_UP]:
        pl.y -= pl.speed
    
    if keys[pg.K_DOWN]:
        pl.y += pl.speed
    #Удаление Предыдущих рисунков
    Window.fill((0,0,0)) 
    # Цвет Игрока
    pg.draw.rect(Window, (0,0,255), (pl.x, pl.y, pl.widht, pl.high))
    pg.display.update()
# выход
pg.quit()