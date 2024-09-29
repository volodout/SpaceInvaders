from help_funcs import *
import globals


def begin(paused=False, testing=False):
    if not paused:
        obstacles_group.empty()
        create_aliens()
        create_obstacles()
        player_group.add(player)
        player.hp = 3

    shooting_count = 0
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pause()

        screen.fill('black')

        alien_shooting(shooting_count // 300)
        shooting_count += 1

        update_and_draw_groups()
        draw_ui()
        check_player()

        pg.display.flip()

        clock.tick(60)

        if testing:
            running = False


def pause(testing=False):
    paused = True
    while paused:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    begin(True)
                elif event.key == pg.K_BACKSPACE:
                    globals.bullets_count = 1
                    globals.is_creative = False
                    clear_groups()
                    menu()

        print_text_to_center('PRESS ESC TO CONTINUE', 50, 300, (255, 0, 0), True)
        print_text_to_center('PRESS BACKSPACE TO EXIT IN MENU', 35, 350, (255, 0, 0), True)

        pg.display.update()
        clock.tick(60)

        if testing:
            paused = False


def menu(testing=False):
    globals.difficult_aliens = 0
    globals.difficult_obstacles = 0
    colors = ['white', 'white', 'white']
    colors[globals.difficult_aliens] = 'green'

    show = True
    while show:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    begin()
                elif event.key == pg.K_UP:
                    globals.difficult_aliens = max(0, globals.difficult_aliens - 1)
                    globals.difficult_obstacles = max(0, globals.difficult_obstacles - 1)
                elif event.key == pg.K_DOWN:
                    globals.difficult_aliens = min(2, globals.difficult_aliens + 1)
                    globals.difficult_obstacles = min(2, globals.difficult_obstacles + 1)
                elif event.key == pg.K_c:
                    globals.is_creative = True
                    create_level()
                colors = ['white', 'white', 'white']
                colors[globals.difficult_aliens] = 'green'

        screen.fill('black')
        print_text_to_center('SPACE', 150, 80, (0, 255, 0))
        print_text_to_center('INVADERS', 130, 180)

        print_text_to_center('EASY', 80, 350, colors[0])
        print_text_to_center('MEDIUM', 80, 450, colors[1])
        print_text_to_center('HARD', 80, 550, colors[2])

        print_text_to_center('PRESS C TO CREATE YOUR LEVEL', 60, 700, 'white')

        pg.display.update()
        clock.tick(60)

        if testing:
            show = False


def create_level():
    colors = ['white', 'white', 'white', 'white']
    stage = 0
    colors[stage] = 'green'

    show = True
    while show:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    begin()

                if event.key == pg.K_UP:
                    stage = max(0, stage - 1)
                elif event.key == pg.K_DOWN:
                    stage = min(len(colors) - 1, stage + 1)

                elif event.key == pg.K_LEFT:
                    if stage == 0:
                        globals.difficult_aliens = max(0, globals.difficult_aliens - 1)
                    elif stage == 1:
                        globals.difficult_obstacles = max(0, globals.difficult_obstacles - 1)
                    elif stage == 2:
                        globals.player_speed = max(1, globals.player_speed - 1)
                    elif stage == 3:
                        globals.bullets_count = max(1, globals.bullets_count - 1)

                elif event.key == pg.K_RIGHT:
                    if stage == 0:
                        globals.difficult_aliens = min(3, globals.difficult_aliens + 1)
                    elif stage == 1:
                        globals.difficult_obstacles = min(2, globals.difficult_obstacles + 1)
                    elif stage == 2:
                        globals.player_speed = min(15, globals.player_speed + 1)
                    elif stage == 3:
                        globals.bullets_count = min(5, globals.bullets_count + 1)

                colors = ['white', 'white', 'white', 'white']
                colors[stage] = 'green'

        screen.fill('black')

        print_text_to_center(f'SPEED OF ALIENS < {globals.difficult_aliens + 1} >', 50, 150, colors[0])
        print_text_to_center(f'DIFFICULT OF OBSTACLES < {globals.difficult_obstacles} >', 50, 250, colors[1])
        print_text_to_center(f'SPEED OF PLAYER < {globals.player_speed} >', 50, 350, colors[2])
        print_text_to_center(f'NUMBER OF YOUR BULLETS < {globals.bullets_count} >', 50, 450, colors[3])

        print_text_to_center('PRESS ENTER TO START', 70, 550, 'yellow')

        pg.display.update()
        clock.tick(60)


def game_over(testing=False):
    globals.player.image = pg.image.load("sprites/player_death.png")
    globals.player.isKilled = True
    globals.player.hp = 0

    alien_bullet_group.empty()
    alien_group.empty()
    bullet_group.empty()

    if not globals.is_creative:
        check_records()
    globals.score = 0

    show = True
    while show:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    globals.bullets_count = 1
                    globals.is_creative = False
                    menu()

        print_text_to_center('GAME OVER', 120, 300)
        print_text_to_center('PRESS ENTER TO EXIT IN MENU', 60, 450)

        pg.display.update()
        clock.tick(60)

        if testing:
            show = False
