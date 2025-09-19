import pygame
import sys
from Board import Board
pygame.init()
WIDTH = 600
HEIGHT = 700
SCREEN_COLOR = (20,51,205)

def draw_screen(screen):

    #start message
    start_font = pygame.font.Font(None, 70)
    mode_font = pygame.font.Font(None, 65)
    mode_selection_font = pygame.font.Font(None, 50) 

    mode1_message = mode_selection_font.render('EASY', True, (254, 240, 255))
    mode2_message = mode_selection_font.render('MEDIUM', True, (254, 240, 255))
    mode3_message = mode_selection_font.render('HARD', True, (254, 240, 255))

    start_message = start_font.render('Welcome to Sudoku', True, (0, 13, 51))
    start_message_rect = start_message.get_rect(center=(WIDTH // 2, 100))
    screen.blit(start_message, start_message_rect)

    
    mode_message = mode_font.render('Select Game Mode:', True, (0, 13, 51))
    mode_rect = mode_message.get_rect(center=(WIDTH // 2, 550))
    screen.blit(mode_message, mode_rect)

    mode1_surface = pygame.Surface((mode1_message.get_size()[0] + 20, mode1_message.get_size()[1] + 20))
    mode1_surface.fill((0, 13, 51))
    mode1_surface.blit(mode1_message, (10, 10))

    mode2_surface = pygame.Surface((mode2_message.get_size()[0] + 20, mode2_message.get_size()[1] + 20))
    mode2_surface.fill((0, 13, 51))
    mode2_surface.blit(mode2_message, (10, 10))

    mode3_surface = pygame.Surface((mode3_message.get_size()[0] + 20, mode3_message.get_size()[1] + 20))
    mode3_surface.fill((0, 13, 51))
    mode3_surface.blit(mode3_message, (10, 10))

    mode1_rect = mode1_message.get_rect(center=(WIDTH // 4, HEIGHT - 50))
    screen.blit(mode1_surface, mode1_rect)

    mode2_rect = mode2_message.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(mode2_surface, mode2_rect)

    mode3_rect = mode3_message.get_rect(center=(WIDTH * (3 / 4), HEIGHT - 50))
    screen.blit(mode3_surface, mode3_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode1_rect.collidepoint(event.pos):
                    return 30

                elif mode2_rect.collidepoint(event.pos):
                    return 40

                elif mode3_rect.collidepoint(event.pos):
                    return 50

        pygame.display.update()

def over_screen(screen , if_won,background):

    screen.blit(background,(0,0))

    over_font = pygame.font.Font(None,80)
    selection_font = pygame.font.Font(None, 50)
    if if_won == True:
        over_message = over_font.render("Game WON",True,(255,255,255))
        selection_button = selection_font.render("EXIT",True,(255,255,255))
    else:
        over_message = over_font.render("Game Over :(",True,(255,255,255))
        selection_button = selection_font.render("RESTART",True,(255,255,255))

    over_message_rect = over_message.get_rect(center=(WIDTH // 2, 300))
    screen.blit(over_message, over_message_rect)

    selection_button_surface = pygame.Surface((selection_button.get_size()[0]+20,selection_button.get_size()[1]+20))
    selection_button_surface.fill((0, 13, 51))
    selection_button_surface.blit(selection_button, (10, 10))

    selection_rect = selection_button.get_rect(center = (WIDTH//2, 500))
    screen.blit(selection_button_surface,selection_rect) 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selection_rect.collidepoint(event.pos):
                    if if_won == True:
                        sys.exit()
                    else:
                        return 'restart'
        pygame.display.update()


def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 700))
    pygame.display.set_caption("Sudoku Game")
    img = pygame.image.load("sha.jpeg")
    scaled_image = pygame.transform.scale(img, (600, 700))
    screen.blit(scaled_image, (0, 0))
    sudoku_main = Board(WIDTH, HEIGHT, screen, draw_screen(screen))
    return screen, scaled_image, sudoku_main

if __name__ == "__main__":
    screen, scaled_image, sudoku_main = initialize_game()
    running = True
    if_won = False
    
    while True:
        while running and not if_won:
            sudoku_main.draw()


            option_font = pygame.font.Font(None, 50)
            reset_button = option_font.render('RESET', True, (254, 240, 255))
            restart_button = option_font.render('RESTART', True, (254, 240, 255)) 
            exit_button = option_font.render('EXIT', True, (254, 240, 255))
            

            reset_button_surface = pygame.Surface((reset_button.get_size()[0] + 20, reset_button.get_size()[1] + 20))
            reset_button_surface.fill((0, 255, 255))
            reset_button_surface.blit(reset_button, (10, 10))

            restart_button_surface = pygame.Surface((restart_button.get_size()[0] + 20, restart_button.get_size()[1] + 20))
            restart_button_surface.fill((0, 255, 255))
            restart_button_surface.blit(restart_button, (10, 10))

            exit_button_surface = pygame.Surface((exit_button.get_size()[0] + 20, exit_button.get_size()[1] + 20))
            exit_button_surface.fill((0, 255, 255))
            exit_button_surface.blit(exit_button, (10, 10))


            reset_button_rect = reset_button.get_rect(center=(((WIDTH / 9) * 1.5) - 10, HEIGHT - 50))
            screen.blit(reset_button_surface, reset_button_rect)

            restart_button_rect = restart_button.get_rect(center=((WIDTH / 2) - 10, HEIGHT - 50))
            screen.blit(restart_button_surface, restart_button_rect)

            exit_button_rect = exit_button.get_rect(center=(((WIDTH / 9) * 7) + 10, HEIGHT - 50))
            screen.blit(exit_button_surface, exit_button_rect)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    col = pos[0]
                    row = pos[1]
                    coord = sudoku_main.click(row, col)

                    if row >= 0 and row <= WIDTH and col >= 0 and col <= WIDTH:
                        sudoku_main.select(coord[0], coord[1])
                    
                    if exit_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    
                    if reset_button_rect.collidepoint(event.pos):
                        sudoku_main.reset_to_original()
                    
                    if restart_button_rect.collidepoint(event.pos):
                        
                        screen, scaled_image, sudoku_main = initialize_game()
                        break 

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        number = 1
                        sudoku_main.sketch(1)

                    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        number = 2
                        sudoku_main.sketch(2)

                    if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        number = 3
                        sudoku_main.sketch(3)

                    if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        number = 4
                        sudoku_main.sketch(4)  

                    if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        number = 5
                        sudoku_main.sketch(5)

                    if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        number = 6
                        sudoku_main.sketch(6)

                    if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        number = 7
                        sudoku_main.sketch(7)  

                    if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        number = 8
                        sudoku_main.sketch(8)  

                    if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        number = 9
                        sudoku_main.sketch(9)

                    if event.key == pygame.K_UP:
                        if coord[1] == 0:
                            coord[1] = 8
                        else:
                            coord[1] = coord[1] - 1
                        sudoku_main.select(coord[0],coord[1])

                    if event.key == pygame.K_DOWN:
                        if coord[1] == 8:
                            coord[1] = 0
                        else:
                            coord[1] = coord[1] + 1 
                        sudoku_main.select(coord[0],coord[1])

                    if event.key == pygame.K_LEFT:
                        if coord[0] == 0:
                            coord[0] = 8
                        else:
                            coord[0] = coord[0] - 1
                        sudoku_main.select(coord[0],coord[1])

                    if event.key == pygame.K_RIGHT:
                        if coord[0] == 8:
                            coord[0] = 0
                        else:
                            coord[0] = coord[0] + 1
                        sudoku_main.select(coord[0],coord[1])
                    if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                        sudoku_main.clear()
                        
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        sudoku_main.place_number(number)
                        number = 0

                        
                        if sudoku_main.is_full():
                            if sudoku_main.check_board():
                                running = False
                                if_won = True
                                over_screen(screen,if_won,scaled_image)
                            running = False
                            a = over_screen(screen,if_won,scaled_image)
                            if a == 'restart':
                                screen, scaled_image, sudoku_main = initialize_game()
                                break 

            clock = pygame.time.Clock()
            clock.tick(60)
            pygame.display.update()