import pygame
import sys

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []

    def add_button(self, text, x, y, width, height, color, action=None):
        button = {
            'text': text,
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'color': color,
            'action': action
        }
        self.buttons.append(button)

    def draw(self):
        for button in self.buttons:
            pygame.draw.rect(self.screen, button['color'], (button['x'], button['y'], button['width'], button['height']))
            font = pygame.font.Font(None, 36)
            text = font.render(button['text'], True, (0, 0, 0))
            text_rect = text.get_rect(center=(button['x'] + button['width'] // 2, button['y'] + button['height'] // 2))
            self.screen.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button['x'] <= mouse_pos[0] <= button['x'] + button['width'] and button['y'] <= mouse_pos[1] <= button['y'] + button['height']:
                    if button['action']:
                        button['action']()
