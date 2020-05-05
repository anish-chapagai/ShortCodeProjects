import pygame as pg
pg.init()
screen_size = (800,600)
running = True
screen = pg.display.set_mode(screen_size)
font = pg.font.Font(None, 25)
base_x = (screen_size[0]-100)//2# Rectangle properties
base_y = screen_size[1]-20
x = base_x+100//2# Circle properties
y = base_y-10
x_vel = 4
y_vel = 2
pg.display.set_caption("Bouncer")
def check_for_exit():
	for event in pg.event.get():	# Check for exit signal
		return True if event.type == pg.QUIT else False
def check_corner():
	global x_vel, y_vel, running, points
	x_vel = x_vel * -1 if x >= screen_size[0]-10 or x <= 0 else x_vel
	y_vel = y_vel * -1 if y <= 0 else y_vel
	if (x >= base_x and x <= base_x+100 and y == base_y):	# If player successfully dodges
		y_vel *= -1
		points += 1
	running = False if y > base_y else True	# Game over
	return True
def start_game():
	global x,y, base_x, base_y, points
	constant = 1
	pg.time.delay(8)
	running = check_for_exit()
	keys = pg.key.get_pressed()
	constant = 2 if keys[pg.K_LCTRL] or keys[pg.K_RCTRL] else 1	# IF CTRL IS PREDDED INCREASES SPEED OF BASE BY TWICE ELSE SPEED IS NORMAL
	base_x -= 2 * constant	if keys[pg.K_LEFT] else 0
	base_x += 2 * constant if keys[pg.K_RIGHT] else 0
	x += x_vel
	y -= y_vel
	check_corner()
	screen.fill((0,0,0))
	pg.draw.circle(screen,(250,0,0),(x,y),10)
	pg.draw.rect(screen,(0,250,0),(base_x,base_y,100,20))
	text = font.render('Current Score: ' + str(points), True, (0, 128, 0))# Score container
	screen.blit(text, (550, 20))
points = 0
counter = False
while running:
	running = not check_for_exit()
	pg.draw.circle(screen,(250,0,0),(x,y),10)
	pg.draw.rect(screen,(0,250,0),(base_x,base_y,100,20))
	text = font.render('Press Space to Start', True, (100, 128, 0))
	screen.blit(text, (screen_size[0]//2-40, 300))
	if pg.key.get_pressed()[pg.K_SPACE]:
		counter = True
	start_game() if counter else print()
	pg.display.update()
font = pg.font.Font(None, 50)
text = font.render('You Scored: ' + str(points), True, (212,175,55))
screen.blit(text, (screen_size[0]//2-50, 300))
while not check_for_exit():
	pg.display.update()