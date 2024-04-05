import pygame
import time
import os

pygame.font.init()
pygame.mixer.init()

# se crea una ventana con sus respectivas medidas, una fuente para las letras
# los colores necesarios , la velocidad y cantidad de balas vicibles en el juego 
Ventana = pygame.display.set_mode( ( 800, 600 ) )
miFuente = pygame.font.SysFont( "System", 60 )

Negro = ( 0, 0, 0 )
Blanco = ( 255, 255, 255 )

BULLET_VEL = 7
MAX_BULLETS = 3

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# funcion que muestra el ganador de la partida 
def draw_winner(text):
    draw_text = miFuente.render( text, 1, Blanco )
    Ventana.blit( draw_text, ( 800/2 - draw_text.get_width() / 2, 450/2 - draw_text.get_height()/2 ) )
    pygame.display.update()
    pygame.time.delay( 5000 )

#Esta función se encarga del movimiento de las balas, de la colisión de éstas
#y de eliminarlas cuando se salen de la pantalla
def handle_bullets( balas_amarillas, balas_rojas, jugador1, jugador2, cubo1, cactus, roca):
    for bullet in balas_amarillas:
        bullet.x += BULLET_VEL

        if jugador2.colliderect(bullet):
            pygame.event.post(pygame.event.Event( RED_HIT ) )
            balas_amarillas.remove( bullet )

        if cubo1.colliderect(bullet):
            balas_amarillas.remove(bullet)

        if cactus.colliderect(bullet):
            balas_amarillas.remove(bullet)
        
        if roca.colliderect(bullet):
            balas_amarillas.remove(bullet)

        elif bullet.x > 800:
            balas_amarillas.remove(bullet)

    
    for bullet in balas_rojas:
        bullet.x -= BULLET_VEL
        if jugador1.colliderect(bullet):
            pygame.event.post(pygame.event.Event( YELLOW_HIT )) #Sonido balas al chocar 
            balas_rojas.remove(bullet) #Elimina las balas al chocar
        
        if cubo1.colliderect(bullet):
            balas_rojas.remove(bullet)

        if cactus.colliderect(bullet):
            balas_rojas.remove(bullet)

        if roca.colliderect(bullet):
            balas_rojas.remove(bullet)
        
        elif bullet.x < 0:
            balas_rojas.remove(bullet)
# funcion principal 
def batalla():
    pygame.init()
    pygame.mixer.init()
    # sonidos del juego
    imgFondo = pygame.image.load( "fondo.png" )	
    sonidoImpacto = pygame.mixer.Sound( "Grenade.wav" )
    sonidoBala = pygame.mixer.Sound( "Shot.wav" )
    # vida de los jugadores
    vidasJugador1 = 10
    vidasJugador2 = 10

    #coordenadas y dimenciones de las rocas y jugador
    PlayerAncho = 8
    PlayerAlto = 110
    R1AL = 95
    R1AN = 95
    R2AL = 20
    R2AN = 115
    R3AL = 110
    R3AN = 50

    clock = pygame.time.Clock()

    #Coordenadas y velocidad del jugador 1
    CoorPlayer1_X = 50
    CoorPlayer1_Y = 300 - 45
    player1Vel_Y = 0
    player1Vel_X = 0
    CoorPlayer1_SUBX = 0
    CoorPlayer1_SUBY = 0



    #Coordenadas y velocidad del jugador 2
    CoorPlayer2_X = 750 - PlayerAncho
    CoorPlayer2_Y = 300 - 45
    Player2Vel_Y = 0
    Player2Vel_X = 0
    CoorPlayer2_SUBX = 0
    CoorPlayer2_SUBY = 0

    game_over = False

    balas_rojas = []
    balas_amarillas = []

    flag1 = 1
    flag2 = 1

    # con estas declaraciones llamamos a las imagenes del juego y las asignamos en una variable 
    imgJugador2 = pygame.image.load( os.path.join( 'rojo1.png' ) )
    imgJugador1 = pygame.image.load( os.path.join( 'amarillo1.png' ) )
    R1 = pygame.image.load(os.path.join('miro_juego.jpg'))
    R1F = pygame.transform.scale(R1,(R1AL,R1AN))
    R2 = pygame.image.load(os.path.join('miro_juego.jpg'))
    R2F = pygame.transform.scale(R2,(R2AL,R2AN))
    R3 = pygame.image.load(os.path.join('miro_juego.jpg'))
    R3F = pygame.transform.scale(R3,(R3AL,R3AN))

    #ciclo del juego
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # se asignan los comandos de movimiento dependiendo la direccion de igual forma la imagen que se mostrara    
            if event.type == pygame.KEYDOWN:
                # Jugador 1
                if event.key == pygame.K_w:
                    player1Vel_Y = -3
                    imgJugador1 = pygame.image.load( os.path.join( 'amarillo2.png' ) )
                    flag1 = 2
                if event.key == pygame.K_s:
                    player1Vel_Y = 3
                    imgJugador1 = pygame.image.load( os.path.join( 'amarillo2.png' ) )
                    flag1 = 2
                if event.key == pygame.K_a:
                    player1Vel_X = -3
                    imgJugador1 = pygame.image.load( os.path.join( 'amarillo2.png' ) )
                    flag1 = 2
                if event.key == pygame.K_d:
                    player1Vel_X = 3
                    imgJugador1 = pygame.image.load( os.path.join( 'amarillo2.png' ) )
                    flag1 = 2
                
                # Jugador 2
                if event.key == pygame.K_UP:
                    Player2Vel_Y = -3
                    imgJugador2 = pygame.image.load( os.path.join( 'rojo2.png' ) )
                    flag2 = 2
                if event.key == pygame.K_DOWN:
                    Player2Vel_Y = 3
                    imgJugador2 = pygame.image.load( os.path.join( 'rojo2.png' ) )
                    flag2 = 2
                if event.key == pygame.K_LEFT:
                    Player2Vel_X = -3
                    imgJugador2 = pygame.image.load( os.path.join( 'rojo2.png' ) )
                    flag2 = 2
                if event.key == pygame.K_RIGHT:
                    Player2Vel_X = 3
                    imgJugador2 = pygame.image.load( os.path.join( 'rojo2.png' ) )
                    flag2 = 2
                # evento en el que preciona una tecla y dispara una bala
                if event.key == pygame.K_LCTRL and len( balas_amarillas ) < MAX_BULLETS:
                    bullet = pygame.Rect( jugador1.x + jugador1.width, jugador1.y + jugador1.height//2 + 5, 10, 5 )
                    balas_amarillas.append( bullet )
                    imgJugador1 = pygame.image.load( os.path.join( 'amarillo3.png' ) )
                    flag1 = 3
                    pygame.mixer.Sound.play( sonidoBala )
                
                #Se utilizan dos // en la división para que el resultado sea un número entero
                if event.key == pygame.K_RCTRL and len( balas_rojas ) < MAX_BULLETS:
                    bullet = pygame.Rect( jugador2.x, jugador2.y + jugador2.height//2 + 5, 10, 5 )
                    balas_rojas.append( bullet )
                    imgJugador2 = pygame.image.load( os.path.join( 'rojo3.png' ) )
                    flag2 = 3
                    pygame.mixer.Sound.play( sonidoBala )
                
            if event.type == pygame.KEYUP:
                # Jugador 1
                if event.key == pygame.K_w:
                    player1Vel_Y = 0
                    imgJugador1 = pygame.image.load( os.path.join( 'amarillo1.png' ) )
                    flag1 = 1
                if event.key == pygame.K_s:
                    player1Vel_Y = 0
                    imgJugador1 = pygame.image.load( os.path.join( 'amarillo1.png' ) )
                    flag1 = 1
                if event.key == pygame.K_a:
                    player1Vel_X = 0
                    imgJugador1 = pygame.image.load( os.path.join( 'amarillo1.png' ) )
                    flag1 = 1
                if event.key == pygame.K_d:
                    player1Vel_X = 0
                    imgJugador1 = pygame.image.load( os.path.join( 'amarillo1.png' ) )
                    flag1 = 1

                # Jugador 2
                if event.key == pygame.K_UP:
                    Player2Vel_Y = 0
                    imgJugador2 = pygame.image.load( os.path.join( 'rojo1.png' ) )
                    flag2 = 1
                if event.key == pygame.K_DOWN:
                    Player2Vel_Y = 0
                    imgJugador2 = pygame.image.load( os.path.join( 'rojo1.png' ) )
                    flag2 = 1
                if event.key == pygame.K_LEFT:
                    Player2Vel_X = 0
                    imgJugador2 = pygame.image.load( os.path.join( 'rojo1.png' ) )
                    flag2 = 1
                if event.key == pygame.K_RIGHT:
                    Player2Vel_X = 0
                    imgJugador2 = pygame.image.load( os.path.join( 'rojo1.png' ) )
                    flag2 = 1
                
            if event.type == RED_HIT:
                vidasJugador2 -= 1
                pygame.mixer.Sound.play( sonidoImpacto )

            if event.type == YELLOW_HIT:
                vidasJugador1 -= 1
                pygame.mixer.Sound.play( sonidoImpacto )

            

        winner_text = ""

        
        
        Ventana.blit( imgFondo, ( 0, 0 ) )
        
        #Zona de dibujo
        jugador1 = pygame.Rect( CoorPlayer1_X, CoorPlayer1_Y, PlayerAncho+50, PlayerAlto+2 )
        
        jugador2 = pygame.Rect( CoorPlayer2_X, CoorPlayer2_Y, PlayerAncho+50, PlayerAlto+2 ) 

        roca1 = pygame.draw.rect(Ventana, Negro,(350,50 , R1AL, R1AN) )

        roca2 = pygame.draw.rect(Ventana, Negro,(300, 400, R2AL, R2AN) )

        roca3 = pygame.draw.rect(Ventana, Negro,(450, 250, R3AL, R3AN) )

        superior =  pygame.Rect(1,1 , 1000, 1) 
        inferior=   pygame.Rect(1,599 , 1000, 1) 
        lateralI=   pygame.Rect(1,0 , 1, 1000) 
        lateralD=   pygame.Rect(799,1 , 1, 1000) 

        # Modifica las coordenadas para dar mov. a los jugadores/ pelota y sus coliciones con los muros
        # y evitar la salida de la pantalla
     
        if jugador1.colliderect(superior) :
            CoorPlayer1_Y += 3
        if jugador1.colliderect(inferior) :
            CoorPlayer1_Y -= 3
        if jugador1.colliderect(lateralD) :
            CoorPlayer1_X -= 3    
        if jugador1.colliderect(lateralI) :
            CoorPlayer1_X += 3
         
        if jugador1.colliderect(roca1) :
            CoorPlayer1_X = CoorPlayer1_SUBX 
            CoorPlayer1_Y = CoorPlayer1_SUBY
        if jugador1.colliderect(roca2) :
            CoorPlayer1_X = CoorPlayer1_SUBX 
            CoorPlayer1_Y = CoorPlayer1_SUBY
        if jugador1.colliderect(roca3) :
            CoorPlayer1_X = CoorPlayer1_SUBX 
            CoorPlayer1_Y = CoorPlayer1_SUBY
        
        CoorPlayer1_SUBX = CoorPlayer1_X
        CoorPlayer1_SUBY = CoorPlayer1_Y

        CoorPlayer1_Y += player1Vel_Y
        CoorPlayer1_X += player1Vel_X 
            
        

        
       
            
            

        #jugador 2        
        if jugador2.colliderect(superior) :
            CoorPlayer2_Y += 3
        if jugador2.colliderect(inferior) :
            CoorPlayer2_Y -= 3
        if jugador2.colliderect(lateralD) :
            CoorPlayer2_X -= 3    
        if jugador2.colliderect(lateralI) :
            CoorPlayer2_X += 3
         
        if jugador2.colliderect(roca1) :
            CoorPlayer2_X = CoorPlayer2_SUBX 
            CoorPlayer2_Y = CoorPlayer2_SUBY
        if jugador2.colliderect(roca2) :
            CoorPlayer2_X = CoorPlayer2_SUBX 
            CoorPlayer2_Y = CoorPlayer2_SUBY
        if jugador2.colliderect(roca3) :
            CoorPlayer2_X = CoorPlayer2_SUBX 
            CoorPlayer2_Y = CoorPlayer2_SUBY
        
        CoorPlayer2_SUBX = CoorPlayer2_X
        CoorPlayer2_SUBY = CoorPlayer2_Y

        CoorPlayer2_Y += Player2Vel_Y
        CoorPlayer2_X += Player2Vel_X 
        
        

                
        
        
        
        #Muestra jugadores (vaqueros) en ventana
        if flag1 == 1 or flag1 == 3:
            Ventana.blit( imgJugador1, ( CoorPlayer1_X, CoorPlayer1_Y ) )
        elif flag1 == 2:
            Ventana.blit( imgJugador1, ( CoorPlayer1_X, CoorPlayer1_Y ) )

        if flag2 == 1:
            Ventana.blit( imgJugador2, ( CoorPlayer2_X, CoorPlayer2_Y ) )
        elif flag2 == 2:
            Ventana.blit( imgJugador2, ( CoorPlayer2_X, CoorPlayer2_Y ) )
        elif flag2 == 3:
            Ventana.blit( imgJugador2, ( CoorPlayer2_X, CoorPlayer2_Y ) )

        MarcadorJugador1 = miFuente.render( "J1 " + str( vidasJugador1 ), False, ( 255, 255, 255 ) )
        MarcadorJugador2 = miFuente.render( "J2 " + str( vidasJugador2 ), False, ( 255, 255, 255 ) )
        Ventana.blit( MarcadorJugador1, ( 20, 0 ) )
        Ventana.blit( MarcadorJugador2, ( 680, 0 ) )

        #Muestra las rocas
        Ventana.blit(R1F,(350,50)) #Mostrar imagen en ventana
        Ventana.blit(R2F,(300, 400))
        Ventana.blit(R3F,(450, 250))

        # muestra las balas en pantalla
        for bullet in balas_rojas:
            pygame.draw.rect( Ventana, Blanco, bullet )
        for bullet in balas_amarillas:
            pygame.draw.rect( Ventana, Blanco, bullet )

        # muestra en pantalla el texto de quien gano 
        winner_text = ""
        if vidasJugador2 <= 0:
            winner_text = "Jugador 1 ganó !"

        if vidasJugador1 <= 0:
            winner_text = "Jugador 2 ganó!"

        if winner_text != "":
            draw_winner( winner_text )
            pygame.display.flip()

        handle_bullets( balas_amarillas, balas_rojas, jugador1, jugador2, roca1, roca2, roca3)

        pygame.display.flip()
        clock.tick( 60 )
    pygame.quit()

if __name__=='__main__':
    batalla()