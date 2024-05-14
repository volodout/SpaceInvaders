from help_funcs import *
import globals


def begin(paused=False):
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

        alien_shooting(shooting_count // 300, alien_group)
        shooting_count += 1

        update_and_draw_groups()
        draw_ui()
        check_player()

        pg.display.flip()

        clock.tick(60)


def pause():
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
                    clear_groups()
                    menu()

        print_text_to_center('PRESS ESC TO CONTINUE', 50, 300, (255, 0, 0), True)
        print_text_to_center('PRESS BACKSPACE TO EXIT IN MENU', 35, 350, (255, 0, 0), True)

        pg.display.update()
        clock.tick(60)


def menu():
    colors = ['white', 'white', 'white']
    colors[globals.level] = 'green'

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
                    globals.level = max(0, globals.level - 1)
                elif event.key == pg.K_DOWN:
                    globals.level = min(2, globals.level + 1)
                colors = ['white', 'white', 'white']
                colors[globals.level] = 'green'
                print(globals.level)

        screen.fill('black')
        print_text_to_center('SPACE', 150, 80, (0, 255, 0))
        print_text_to_center('INVADERS', 130, 180)

        print_text_to_center('EASY', 80, 350, colors[0])
        print_text_to_center('MEDIUM', 80, 450, colors[1])
        print_text_to_center('HARD', 80, 550, colors[2])

        pg.display.update()
        clock.tick(60)


def game_over():
    alien_bullet_group.empty()
    alien_group.empty()
    bullet_group.empty()

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
                    menu()

        print_text_to_center('GAME OVER', 120, 300)
        print_text_to_center('PRESS ENTER TO EXIT IN MENU', 60, 450)


        pg.display.update()
        clock.tick(60)