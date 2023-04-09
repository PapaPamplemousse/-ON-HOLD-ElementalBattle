import pygame
from unit import FireElemental, WaterElemental, AirElemental, EarthElemental
from player import Player
from board import Board

class SinglePlayer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 16)
        self.timer_font = pygame.font.Font(None, 48)
        self.gold_font = pygame.font.Font(None, 48)
        self.buttons = []
        self.player = Player("Player 1", [], 50)
        self.recruitment_end_time = pygame.time.get_ticks() + 10000  # 10 seconds
        self.board = Board()
        self.dialog_open = False
        self.dialog_buttons = []
        self.selected_unit = None
        self.unit_placement_x = None
        self.unit_placement_y = None
        self.player1_placing_units = True
        self.phase = 1

        # Create buttons for unit recruitment
        self.create_button('Fire', FireElemental, 100, 300, (255, 0, 0))
        self.create_button('Water', WaterElemental, 250, 300, (0, 0, 255))
        self.create_button('Air', AirElemental, 400, 300, (128, 0, 128))
        self.create_button('Earth', EarthElemental, 550, 300, (139, 69, 19))

    def create_button(self, label, unit_class, x, y, color):
        def recruit_unit():
            if self.player.recruit_unit(unit_class, self.player):  # Add self.player as an argument
                count = self.player.count_units(unit_class)
                button['label'] = f"{label} ({count})"
                self.draw()
                pygame.display.flip()

        button = {
            'label': label,
            'unit_class': unit_class,
            'x': x,
            'y': y,
            'color': color,
            'rect': pygame.Rect(x, y, 150, 75),
            'action': recruit_unit
        }
        self.buttons.append(button)

    def draw(self):
        self.screen.fill((255, 255, 255))
        if self.phase == 1:
            # Draw timer, gold and buttons as before
            remaining_time = max(0, self.recruitment_end_time - pygame.time.get_ticks()) // 1000
            timer_text = self.timer_font.render("Time: {}s".format(remaining_time), True, (0, 0, 0))
            self.screen.blit(timer_text, (20, 20))

            gold_text = self.gold_font.render("Gold: {}".format(self.player.gold), True, (255, 215, 0))
            self.screen.blit(gold_text, (220, 20))

            # Draw buttons
            for button in self.buttons:
                pygame.draw.rect(self.screen, button['color'], button['rect'])
                count = self.player.count_units(button['unit_class'])
                label = f"{button['label']} ({count})"
                text = self.font.render(label, True, (255, 255, 255))
                text_rect = text.get_rect(center=button['rect'].center)
                self.screen.blit(text, text_rect)
        elif self.phase == 2:
            self.draw_board()
            if self.dialog_open:
                for button in self.dialog_buttons:
                    pygame.draw.rect(self.screen, button['color'], button['rect'])
                    text = self.font.render(button['label'], True, (0, 0, 0))
                    text_rect = text.get_rect(center=button['rect'].center)
                    self.screen.blit(text, text_rect)

    def update(self):
        if self.phase == 1:
            if pygame.time.get_ticks() >= self.recruitment_end_time:
                self.phase = 2
        elif self.phase == 2:
            pass  # Add logic for the battle phase here


    def handle_event(self, event):
        if self.phase == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button['rect'].collidepoint(mouse_pos):
                        button['action']()
                        break
        elif self.phase == 2:
            self.handle_board_event(event)

    def setup_board_phase(self):
        self.phase = 2
        self.board = Board()
        self.board_end_time = pygame.time.get_ticks() + 30000  # 30 seconds
        self.player1_placing_units = True  # Whether player 1 is placing units or not
    
    def draw_board(self):
        cell_size = 60
        for i in range(self.board.size):
            for j in range(self.board.size):
                pygame.draw.rect(self.screen, (255, 255, 255), (i * cell_size, j * cell_size, cell_size, cell_size), 0)
                pygame.draw.rect(self.screen, (0, 0, 0), (i * cell_size, j * cell_size, cell_size, cell_size), 1)

    def create_dialog(self):
        self.dialog_buttons = []
        x, y = 100, 100
        button_width, button_height = 120, 50

        for unit_class in [FireElemental, WaterElemental, AirElemental, EarthElemental]:
            count = self.player.inventory.count(unit_class)
            if count > 0:
                def place_unit():
                    self.selected_unit = unit_class(self.player)
                    self.dialog_open = False

                button = {
                    'label': f"{unit_class.__name__} ({count})",
                    'unit_class': unit_class,
                    'x': x,
                    'y': y,
                    'color': (255, 255, 255),
                    'rect': pygame.Rect(x, y, button_width, button_height),
                    'action': place_unit
                }
                self.dialog_buttons.append(button)
                y += button_height + 20

    def handle_board_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if self.dialog_open:
                for button in self.dialog_buttons:
                    if button['rect'].collidepoint(mouse_pos):
                        button['action']()
                        break

                if self.selected_unit is not None:
                    self.board.place_unit(self.selected_unit, self.unit_placement_x, self.unit_placement_y)
                    self.player.inventory.remove(self.selected_unit.__class__)
                    self.selected_unit = None
                    self.draw_board()
                    pygame.display.flip()
            else:
                cell_size = 60
                x, y = mouse_pos[0] // cell_size, mouse_pos[1] // cell_size

                if self.player1_placing_units and y < 4 or not self.player1_placing_units and y >= 6:
                    self.create_dialog()
                    self.dialog_open = True
                    self.selected_unit = None
                    self.unit_placement_x, self.unit_placement_y = x, y
    
    def draw_board(self):
        cell_size = 60
        for i in range(self.board.size):
            for j in range(self.board.size):
                pygame.draw.rect(self.screen, (0, 0, 0), (i * cell_size, j * cell_size, cell_size, cell_size), 1)
                unit = self.board.cells[j][i]
                if unit is not None:
                    unit_image = unit.get_image()
                    self.screen.blit(unit_image, (i * cell_size + 5, j * cell_size + 5))


