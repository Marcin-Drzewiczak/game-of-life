import pygame.gfxdraw
import pygame_gui
import sys

from grid import Grid
from view import View


if __name__ == '__main__':

    WIDTH = 800
    HEIGHT = 1000
    ROWS = 20

    grid = Grid(ROWS)

    pygame.init()
    view = View(WIDTH, HEIGHT, ROWS)
    view.fill(view.BLACK)
    pygame.display.set_caption("Game of Life")

    # GUI
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    button_start_stop = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 900), (100, 50)),
                                                     text='Start/Stop', manager=manager)

    button_clear = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 900), (100, 50)), text='Clear',
                                                manager=manager)

    label_slider = pygame_gui.elements.ui_label.UILabel(relative_rect=pygame.Rect((270, 900), (100, 50)),
                                                        text=f"Rows: {ROWS}", manager=manager)

    slider_rows = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(relative_rect=pygame.Rect((390, 900), (300, 50)),
                                                                              start_value=20, value_range=(10, 100),
                                                                              manager=manager)

    is_running = False

    # GAME LOOP
    while 1:
        pygame.time.wait(50)
        time_delta = clock.tick(60) / 1000.0

        new_rows = slider_rows.get_current_value()
        label_slider.set_text(f"Rows: {new_rows}")

        if ROWS != new_rows:
            ROWS = new_rows
            view.set_rows(ROWS)
            grid.set_rows(ROWS)

        # EVENT HANDLING SECTION
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_start_stop:
                        is_running = not is_running

                        if is_running:
                            slider_rows.disable()
                            button_clear.disable()
                        else:
                            slider_rows.enable()
                            button_clear.enable()

                    if event.ui_element == button_clear:
                        grid.clear_grid()

            if pygame.mouse.get_pressed()[0] and not is_running:
                grid.cell_birth(view.mouse_position_to_index(pygame.mouse.get_pos()))

            if pygame.mouse.get_pressed()[2] and not is_running:
                grid.cell_kill(view.mouse_position_to_index(pygame.mouse.get_pos()))

            manager.process_events(event)
        manager.update(time_delta)

        # DRAW SECTION
        view.fill(view.BLACK)

        if is_running:
            grid.next_step()
            view.draw_grid(view.RED)
        else:
            view.draw_grid(view.GREEN)
        view.fill_grid(grid.get_grid())

        manager.draw_ui(view.get_screen())
        pygame.display.update()
