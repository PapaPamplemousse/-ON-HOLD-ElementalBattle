import pygame
from unit import FireElemental, WaterElemental, AirElemental, EarthElemental
from player import Player

class SinglePlayer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 16)
        self.timer_font = pygame.font.Font(None, 48)
        self.gold_font = pygame.font.Font(None, 48)
        self.buttons = []
        self.player = Player("Player 1", [], 50)
        self.recruitment_end_time = pygame.time.get_ticks() + 60000  # 60 seconds

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
        # Draw timer and gold
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

    def update(self):
        # Check if the recruitment phase is over
        if pygame.time.get_ticks() >= self.recruitment_end_time:
            pass  # Move to the next phase

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button['rect'].collidepoint(mouse_pos):
                    button['action']()
                    break
