import pygame
import sys
import Motor
import Constantes

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO, ALTO = Constantes.ANCHO_VENT, Constantes.ALTO_VENT
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mathmix")

# Colores marrones
FONDO = (205, 133, 63)
COLOR_LETRAS = (110, 44, 0)
COLOR_RECTANGULO = (235, 152, 78)
COLOR_CONTORNO = (110, 44, 0)

# Fuentes
fuente_grande = pygame.font.Font(None, 65)
fuente_pequena = pygame.font.Font(None, 36)

def dibujar_texto_centrado(texto, fuente, color, superficie, y):
    objeto_texto = fuente.render(texto, True, color)
    rect_texto = objeto_texto.get_rect(center=(ANCHO // 2, y))
    superficie.blit(objeto_texto, rect_texto)

def dibujar_rectangulo_redondeado_con_texto(texto, fuente, color_texto, color_fondo, color_contorno, superficie, x, y, padding=20, radio=20):
    objeto_texto = fuente.render(texto, True, color_texto)
    rect_texto = objeto_texto.get_rect()

    rect_fondo = pygame.Rect(x, y, rect_texto.width + 2 * padding, rect_texto.height + 2 * padding)
    pygame.draw.rect(superficie, color_fondo, rect_fondo, border_radius=radio)
    pygame.draw.rect(superficie, color_contorno, rect_fondo, 2, border_radius=radio)

    superficie.blit(objeto_texto, (x + padding, y + padding))
    return rect_fondo

def menu_principal():
    while True:
        pantalla.fill(FONDO)
        dibujar_texto_centrado('Juego Educativo de Matemáticas', fuente_grande, COLOR_LETRAS, pantalla, 100)
        
        rect_jugar = dibujar_rectangulo_redondeado_con_texto('Jugar', fuente_pequena, COLOR_LETRAS, COLOR_RECTANGULO, COLOR_CONTORNO, pantalla, ANCHO // 1.8 - 100, 250, padding=20)  # Modificado el valor de 'y'
        rect_salir = dibujar_rectangulo_redondeado_con_texto('Salir', fuente_pequena, COLOR_LETRAS, COLOR_RECTANGULO, COLOR_CONTORNO, pantalla, ANCHO // 1.775 - 100, 400, padding=20)  # Modificado el valor de 'y'

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_jugar.collidepoint(evento.pos):
                    seleccionar_dificultad()
                if rect_salir.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

def seleccionar_dificultad():
    while True:
        pantalla.fill(FONDO)
        dibujar_texto_centrado('Selecciona la Dificultad', fuente_grande, COLOR_LETRAS, pantalla, 100)

        rect_facil = dibujar_rectangulo_redondeado_con_texto('Fácil', fuente_pequena, COLOR_LETRAS, COLOR_RECTANGULO, COLOR_CONTORNO, pantalla, 100, 250, padding=20)  # Modificado el valor de 'x' y 'y'
        rect_normal = dibujar_rectangulo_redondeado_con_texto('Normal', fuente_pequena, COLOR_LETRAS, COLOR_RECTANGULO, COLOR_CONTORNO, pantalla, 300, 250, padding=20)  # Modificado el valor de 'x' y 'y'
        rect_dificil = dibujar_rectangulo_redondeado_con_texto('Difícil', fuente_pequena, COLOR_LETRAS, COLOR_RECTANGULO, COLOR_CONTORNO, pantalla, 500, 250, padding=20)  # Modificado el valor de 'x' y 'y'

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_facil.collidepoint(evento.pos):
                    jugar(1)
                if rect_normal.collidepoint(evento.pos):
                    jugar(2)
                if rect_dificil.collidepoint(evento.pos):
                    jugar(3)

        pygame.display.flip()

def jugar(dificultad):
    vidas = 3
    aciertos = 0
    errores = 0

    while vidas > 0:
        operacion = Motor.generar_operaciones(dificultad)
        opciones = Motor.posibles_resultados(operacion[-2], dificultad)

        respondido = False

        while not respondido:
            pantalla.fill(FONDO)
            
            # Mostrar la operación
            operacion_str = f"{operacion[0]} {operacion[-1]} {operacion[1]}"
            dibujar_texto_centrado(operacion_str, fuente_grande, COLOR_LETRAS, pantalla, 100)

            # Mostrar opciones de respuesta
            rects_opciones = []
            for i, opcion in enumerate(opciones):
                rect_opcion = dibujar_rectangulo_redondeado_con_texto(f"{opcion}", fuente_pequena, COLOR_LETRAS, COLOR_RECTANGULO, COLOR_CONTORNO, pantalla, ANCHO // 2 - 100, 210 + i * 70, padding=20)
                rects_opciones.append(rect_opcion)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    for i, rect_opcion in enumerate(rects_opciones):
                        if rect_opcion.collidepoint(evento.pos):
                            if opciones[i] == operacion[-2]:
                                dibujar_texto_centrado("Correcto!", fuente_grande, COLOR_LETRAS, pantalla, 480)
                                aciertos += 1
                            else:
                                dibujar_texto_centrado(f"Incorrecto! La respuesta correcta es {operacion[-2]}", fuente_grande, COLOR_LETRAS, pantalla, 480)
                                errores += 1
                                vidas -= 1
                            respondido = True
                            pygame.display.flip()
                            pygame.time.wait(2000)

            pygame.display.flip()

    mostrar_estadisticas(aciertos, errores)

def mostrar_estadisticas(aciertos, errores):
    pantalla.fill(FONDO)
    dibujar_texto_centrado("Juego Terminado", fuente_grande, COLOR_LETRAS, pantalla, 100)
    dibujar_texto_centrado(f"Aciertos: {aciertos}", fuente_pequena, COLOR_LETRAS, pantalla, 200)
    dibujar_texto_centrado(f"Errores: {errores}", fuente_pequena, COLOR_LETRAS, pantalla, 250)
    dibujar_texto_centrado("Presiona R para Reiniciar o Q para Salir", fuente_pequena, COLOR_LETRAS, pantalla, 300)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    menu_principal()
                if evento.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        
menu_principal()