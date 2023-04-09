import sys
import pygame
from menu import MainMenu
from single_player import SinglePlayer
from two_player import TwoPlayer
from settings import SettingsMenu

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Elemental Battle')
    clock = pygame.time.Clock()

    main_menu = MainMenu(screen)
    single_player_mode = SinglePlayer(screen)
    two_player_mode = TwoPlayer(screen)
    settings_menu = SettingsMenu(screen)

    # Add actions for buttons
    def start_single_player():
        nonlocal mode
        mode = single_player_mode
        single_player_mode.recruitment_end_time = pygame.time.get_ticks() + 60000  # Reset the recruitment timer

    def start_two_player():
        nonlocal mode
        mode = two_player_mode

    def open_settings():
        nonlocal mode
        mode = settings_menu

    main_menu.add_button('1 Player', 350, 200, 100, 50, (200, 0, 0), action=start_single_player)
    main_menu.add_button('2 Players', 350, 300, 100, 50, (0, 200, 0), action=start_two_player)
    main_menu.add_button('Settings', 350, 400, 100, 50, (0, 0, 200), action=open_settings)

    mode = main_menu

    while True:
        screen.fill((255, 255, 255))

        # Draw and update the current mode
        mode.draw()
        if mode != main_menu:
            mode.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            mode.handle_event(event)

    # ...

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
