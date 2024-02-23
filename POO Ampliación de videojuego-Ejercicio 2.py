import pygame

pygame.init()
#Creacion de ventana de juego 
ventana = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Tom y Jerry")

#Implementacion de la pelota, obetener su recuadro, posicion inicila y la velocidad
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [4, -4]
ballrect.move_ip(500, 500)

#fuente
fuente = pygame.font.Font(None, 36)

# Crea el objeto bate, obtengo su rectángulo, posicion inicial del bate
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
baterect.move_ip(650, 500)

#cargar la imagen del fondo y tambien obtenemos su rectangulo
Fondo = pygame.image.load("estrellas.png")
fondorect = Fondo.get_rect()

# cargamos la imagen del ladrillo 
ladrillo_img = pygame.image.load("Ladrillo.png")

# creacion de los ladrillos
ladrillos = []
for i in range(1):
    for j in range(1):
            ladrillorect = ladrillo_img.get_rect()
            ladrillorect.move_ip(100 * i , 80 * j)
            ladrillos.append(ladrillorect)

# Dibujar Ladrillos en la ventana
for ladrillo in ladrillos:
    ventana.blit(ladrillo_img, ladrillo)


# Velocidad inicial y factor de aceleración
bate_ini = 5
aceleracion = 0.25

# Bucle inicial
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Se comprueba si se ha cerrado la ventana
            jugando = False

    # Compruebo si se ha pulsado alguna tecla, también aquí se le agrega la velocidad de la barra manteniendo apretado el botón
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and baterect.left > 0:
        baterect = baterect.move(-bate_ini, 0)
        bate_ini += aceleracion
    elif keys[pygame.K_RIGHT] and baterect.right < ventana.get_width():
        baterect = baterect.move(bate_ini, 0)
        bate_ini += aceleracion
    else:
        # si se deja de pulsar se reinicia
        bate_ini = 5

    # Compruebo si hay colisión en las paredes de la ventana 
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]
        
    # Colision del ladrillo y la eliminacion del mismo
    for ladrillo in ladrillos:
        if ladrillo.colliderect(ballrect):
            ladrillos.remove(ladrillo)
            speed[1] = -speed[1]
            break
    
    # Has ganado
    if len(ladrillos) == 0:
        texto_ganador = fuente.render("¡ESTO ES TODO AMIGOS!", True, (255, 255, 255))
        ventana.blit(texto_ganador, (ventana.get_width() // 2 - texto_ganador.get_width() // 2, ventana.get_height() // 2 - texto_ganador.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # Al pasar 2 seg la ventana se cierra
        jugando = False
        
    # game over
    if ballrect.bottom >= ventana.get_height():
        texto_game_over = fuente.render("Game Over", True, (255, 230, 205))
        ventana.blit(texto_game_over, (ventana.get_width() // 2 - texto_game_over.get_width() // 2, ventana.get_height() // 2 - texto_game_over.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # Al pasar 2 seg la ventana se cierra
        jugando = False

    # Blit, volvemos a pintar los elementos en la ventana
    ventana.blit(Fondo, fondorect)
    ventana.blit(ball, ballrect)
    ventana.blit(bate, baterect)
    for ladrillo in ladrillos:
        ventana.blit(ladrillo_img, ladrillo)

    pygame.display.flip()
    
    pygame.time.Clock().tick(100)

pygame.quit()