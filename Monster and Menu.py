from GIF_animation import Flower, Zombie, Spider, Bee

import random
import pygame
import sys


# General setup
pygame.init()
clock = pygame.time.Clock()

# Screen/Window parameter
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flower GIF animation")

# Button class


class Button:
    """To create a button."""

    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        """Initializes the parameters of the button (image, position, text, font, color and color when the mouse is
        matching the position)."""

        super().__init__()

        # The image for the background of the button:
        self.image = image

        # The coordinates of the button:
        self.x_pos = pos[0]
        self.y_pos = pos[1]

        # Determine the font which will be used for the text:
        self.font = font

        # Determine the natural color of the text
        self.base_color = base_color
        # Determine the modified color of the text when the coordinates of the mouse will match the coordinates
        # of the button:
        self.hovering_color = hovering_color

        # Text to insert in the button:
        self.text_input = text_input
        # Apply the color to the text:
        self.text = self.font.render(self.text_input, True, self.base_color)

        # If we don't want to insert an image in the button (only clickable text):
        if self.image is None:
            self.image = self.text

        # Create the rectangle around the image with four parameters : the coordinates x and y, the width and the
        # height.
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def check_for_input(self, position):
        """Returns True if the user clicked on the rectangle covering the surface of the button.
        In brief, allows two make the connection between the button and the linked menu."""

        # The function is called once the 'click' of the user has already been detected.
        # If the coordinates of the 'click' are in the surface covered by the button, it sends the user to the game,
        # the game mode menu, or closes the library and the game.
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    def change_button_color(self, position):
        """Changes the color of the text if the mouse is over the button."""

        # Either the coordinates of the button's rectangle match the position of the mouse.
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        # Either it doesn't and the color of the text remains the same.
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def update(self, surface):
        """Updates the displayed button."""
        # If an image is provided :
        if self.image is not None:
            surface.blit(self.image, self.rect)
        # Update the text
        surface.blit(self.text, self.text_rect)


def create_sprites(coordinates_flower, coordinates_zombie, coordinates_spider, coordinates_bee):
    """Create the sprites for the FLOWER, ZOMBIE, SPIDER and BEE."""
    # Creating sprites and form a group with them for the FLOWER
    moving_sprites_flower = pygame.sprite.Group()
    flower = Flower(coordinates_flower[0], coordinates_flower[1])
    moving_sprites_flower.add(flower)

    # Creating sprites and form a group with them for the ZOMBIE
    moving_sprites_zombie = pygame.sprite.Group()
    zombie = Zombie(coordinates_zombie[0], coordinates_zombie[1])
    moving_sprites_zombie.add(zombie)

    # Creating sprites and form a group with them for the SPIDER
    moving_sprites_spider = pygame.sprite.Group()
    spider = Spider(coordinates_spider[0], coordinates_spider[1])
    moving_sprites_spider.add(spider)

    # Creating sprites and form a group with them for the BEE
    moving_sprites_bee = pygame.sprite.Group()
    bee = Bee(coordinates_bee[0], coordinates_bee[1])
    moving_sprites_bee.add(bee)

    return moving_sprites_flower, moving_sprites_zombie, moving_sprites_spider, moving_sprites_bee


def game_mode():
    """Game loop for the GAME MODE menu."""

    # Display the background
    main_menu_background = pygame.transform.scale(pygame.image.load("assets/main_menu_bg.png"), (1200, 600))
    screen.blit(main_menu_background, (0, 0))

    # Initialize the basic color of the text buttons
    base_color_easy = '#d7fcd4'
    base_color_medium = '#d7fcd4'
    base_color_hard = '#d7fcd4'

    while True:
        # Get the position of the mouse
        game_mode_mouse_pos = pygame.mouse.get_pos()

        # Display the title of the menu : GAME MODE
        game_mode_text = pygame.font.Font("assets/Font_SaintCarellClean.otf", 45).render("GAME MODE", True, "#eae6e5")
        game_mode_rect_text = game_mode_text.get_rect(center=(600, 150))
        screen.blit(game_mode_text, game_mode_rect_text)

        # Create the 'EASY' game mode button
        game_mode_easy_button = Button(image=None, pos=(400, 300), text_input="EASY",
                                       font=pygame.font.Font("assets/Font_SaintCarellClean.otf", 30),
                                       base_color=base_color_easy, hovering_color="#76c893")
        # Create the 'MEDIUM' game mode button
        game_mode_medium_button = Button(image=None, pos=(600, 300), text_input="MEDIUM",
                                         font=pygame.font.Font("assets/Font_SaintCarellClean.otf", 30),
                                         base_color=base_color_medium, hovering_color="#76c893")
        # Create the 'HARD' game mode button
        game_mode_hard_button = Button(image=None, pos=(800, 300), text_input="HARD",
                                       font=pygame.font.Font("assets/Font_SaintCarellClean.otf", 30),
                                       base_color=base_color_hard, hovering_color="#76c893")

        # Create the 'BACK' button
        game_mode_back_button = Button(image=None, pos=(60, 30), text_input="BACK",
                                       font=pygame.font.Font("assets/Font_SaintCarellClean.otf", 30),
                                       base_color="#d7fcd4", hovering_color="White")

        # If the mouse of the player is on a button, the color of the text changes
        # - For the 'BACK' button:
        game_mode_back_button.change_button_color(game_mode_mouse_pos)
        game_mode_back_button.update(screen)
        # - For the 'EASY' button:
        game_mode_easy_button.change_button_color(game_mode_mouse_pos)
        game_mode_easy_button.update(screen)
        # - For the 'MEDIUM' button:
        game_mode_medium_button.change_button_color(game_mode_mouse_pos)
        game_mode_medium_button.update(screen)
        # - For the 'HARD' button:
        game_mode_hard_button.change_button_color(game_mode_mouse_pos)
        game_mode_hard_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Shut down the pygame library
                pygame.quit()
                # Exit the program
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_mode_back_button.check_for_input(game_mode_mouse_pos):
                    # Go back to the main menu
                    main_menu()
                if game_mode_easy_button.check_for_input(game_mode_mouse_pos):
                    difficulty = 1
                    # 'EASY' button gets the accentuated color
                    base_color_easy = '#e9190f'
                    # 'MEDIUM and 'HARD' get the basic color
                    base_color_medium = '#d7fcd4'
                    base_color_hard = '#d7fcd4'
                if game_mode_medium_button.check_for_input(game_mode_mouse_pos):
                    difficulty = 2
                    # 'MEDIUM' button gets the accentuated color
                    base_color_medium = '#e9190f'
                    # 'EASY' and 'HARD' get the basic color
                    base_color_easy = '#d7fcd4'
                    base_color_hard = '#d7fcd4'
                if game_mode_hard_button.check_for_input(game_mode_mouse_pos):
                    difficulty = 3
                    # 'HARD' gets the accentuated color
                    base_color_hard = '#e9190f'
                    # 'EASY' and 'MEDIUM' get the basic color
                    base_color_easy = '#d7fcd4'
                    base_color_medium = '#d7fcd4'

        pygame.display.flip()


def pause_state():
    """Pauses the game and displays a little menu"""
    pause = True
    while pause:
        # Get the position of the mouse
        pause_mouse_pos = pygame.mouse.get_pos()

        # Create the 'resume' button to pause the game
        resume_button = Button(image=None, pos=(55, 60), text_input="RESUME",
                               font=pygame.font.Font("assets/Font_Gameplay.ttf", 20),
                               base_color="White",
                               hovering_color="Black")

        main_menu_button = Button(image=None, pos=(70, 100), text_input="MAIN MENU",
                                  font=pygame.font.Font("assets/Font_Gameplay.ttf", 20),
                                  base_color="White",
                                  hovering_color="Black")

        # If the mouse of the player is on a button, the color of the text changes
        resume_button.change_button_color(pause_mouse_pos)
        main_menu_button.change_button_color(pause_mouse_pos)
        resume_button.update(screen)
        main_menu_button.update(screen)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                # Shut down the pygame library
                pygame.quit()
                # Exit the program
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # Resume the game
                if resume_button.check_for_input(pause_mouse_pos):
                    # Return to the game
                    pause = False
                if main_menu_button.check_for_input(pause_mouse_pos):
                    # Go back to the main menu
                    main_menu()

        pygame.display.flip()


def play():
    """Game loop for the game."""
    game_paused = False

    x_im_plant = random.randint(50, 1150)


    coordinates_flower = (x_im_plant, 440)
    coordinates_zombie = (random.randint(50, 1150), random.randint(50, 550))
    coordinates_spider = (random.randint(50, 1150), 0)
    coordinates_bee = (random.randint(50, 1150), random.randint(50, 550))

    moving_sprites_flower, moving_sprites_zombie, moving_sprites_spider, moving_sprites_bee = create_sprites(
        coordinates_flower, coordinates_zombie, coordinates_spider, coordinates_bee)

    ###################################################
    time_shoot_enemy = 0
    blow_plant = pygame.image.load(r'Images/ball2.png')
    acid_spider = pygame.image.load(r'Images/button_resume.png')
    fire_plant = False
    x_im_plant += 50
    x_plant = x_im_plant
    y_plant = 460

    while True:
        while not game_paused:

            # We need to draw the elements:
            # - Screen color
            screen.fill((214, 159, 126))

            # Get the position of the mouse
            play_mouse_pos = pygame.mouse.get_pos()

            # print(play_mouse_pos) ##########################

            # Create the '||' button to go back to pause the game
            play_back_button = Button(image=None, pos=(20, 20), text_input="| |",
                                      font=pygame.font.Font("assets/Font_Gameplay.ttf", 20), base_color="White",
                                      hovering_color="Black")

            # If the mouse of the player is on the button, the color of the text changes
            play_back_button.change_button_color(play_mouse_pos)
            play_back_button.update(screen)

            # - Draw the sprites
            moving_sprites_flower.draw(screen)
            moving_sprites_zombie.draw(screen)
            moving_sprites_spider.draw(screen)
            moving_sprites_bee.draw(screen)

            # - Update the displayed sprites
            moving_sprites_flower.update(0.02)
            moving_sprites_zombie.update(0.05)
            moving_sprites_spider.update(0.15)
            moving_sprites_bee.update(0.5)

            ################################################
            time_shoot_enemy += 1

            if round(time_shoot_enemy) % 500 == 0:
                fire_plant = True

            if fire_plant:
                x_plant += 5
                screen.blit(blow_plant, (x_plant, y_plant))

            if x_plant < 0 or x_plant > 1200:
                fire_plant = False
                x_plant = x_im_plant

            ####################################

            ##################################################
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Shut down the pygame library
                    pygame.quit()
                    # Exit the program
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_back_button.check_for_input(play_mouse_pos):
                        # Pause the game
                        pause_state()

            # - Update what is displayed on the screen
            pygame.display.flip()
            clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Shut down the pygame library
                pygame.quit()
                # Exit the program
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Exit the pause menu
                game_paused = False

        pygame.display.flip()


def main_menu():
    """Game loop for the MAIN MENU."""
    while True:
        # Display the background
        main_menu_background = pygame.transform.scale(pygame.image.load("assets/main_menu_bg.png"), (1200, 600))
        screen.blit(main_menu_background, (0, 0))

        # Get the position of the mouse
        menu_mouse_pos = pygame.mouse.get_pos()

        # Display the title of the menu
        menu_text = pygame.font.Font("assets/Font_SaintCarellClean.otf", 100).render("MAIN MENU", True, "#eae6e5")
        menu_rect_text = menu_text.get_rect(center=(600, 120))
        screen.blit(menu_text, menu_rect_text)

        # Create the 'PLAY' button
        play_button = Button(image=pygame.image.load("assets/button_background.png"), pos=(600, 250), text_input="PLAY",
                             font=pygame.font.Font("assets/Font_SaintCarellClean.otf", 40), base_color="#d7fcd4",
                             hovering_color="White")
        # Create the 'GAME_MODE' button
        game_mode_button = Button(image=pygame.image.load("assets/button_background.png"), pos=(600, 400),
                                  text_input="GAME MODE", font=pygame.font.Font("assets/Font_SaintCarellClean.otf", 40),
                                  base_color="#d7fcd4", hovering_color="White")
        # Create the 'QUIT' button
        quit_button = Button(image=pygame.image.load("assets/button_background.png"), pos=(600, 550), text_input="QUIT",
                             font=pygame.font.Font("assets/Font_SaintCarellClean.otf", 40), base_color="#d7fcd4",
                             hovering_color="White")

        # The color of the text displayed on the button changes if the mouse is on it
        for button in [play_button, game_mode_button, quit_button]:
            button.change_button_color(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Shut down the pygame library
                pygame.quit()
                # Exit the program
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(menu_mouse_pos):
                    play()
                if game_mode_button.check_for_input(menu_mouse_pos):
                    game_mode()
                if quit_button.check_for_input(menu_mouse_pos):
                    # Shut down the pygame library
                    pygame.quit()
                    # Exit the program
                    sys.exit()

        pygame.display.flip()


if __name__ == '__main__':
    main_menu()
