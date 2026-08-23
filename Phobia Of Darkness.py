from Engine.main import Engine, Player, get_pg, check_collision
import Assets.UI.button as btns
import sys

# vars
state = "menu"
loading_state = "-"
loading_text = "I'm oo .. only ..3.. no 4 years old.\nI am a giirl bbut I ammmm sc..scared from dd..darkness.\nMy Mom and Dad don'tttt ll.llet me out to sleep with them."
loading_index = 0
loading_speed = 50
last_time = 0
other_text = ""
subject = "-"
night = 1

# animated texts
gameplay_text = "Uh, again it is night and moon comes up.\nI wish I don't have any nightmares this time.\nPress (e) to continue."
gameplay_index = 0
gameplay_last_time = 0
gameplay_speed = 50
gameplay_animation_complete = False
draw_text_state = "-"
start_animation_of_sleep_smash = False

# menu action
def start():
    global state
    state = "loading"

# functions
def draw_sleep_animation():
    global start_animation_of_sleep_smash

    if state == "sleep-time":
        if not start_animation_of_sleep_smash:
            main.draw_text(f"Night {night}", "white", 100, 100, font, True)
            smath_sound.play()
            main.delay(2000)
            strange_sound.play()
            start_animation_of_sleep_smash = True

def render_menu():
    if state == "menu":
        main.render_image(main.transform_image(main.load_image("Assets/Image/Background/Menu/MenuBackground.png"),
                                               main.full_window_size()), (0, 0))
        menu_btn = btns.get_menu_start(main, font)
        for btn in menu_btn:
            btn.draw(main.win)
        btns.create_action(menu_btn, [start, sys.exit])

def render_loading():
    global state, loading_text, loading_index, last_time, loading_state

    if state == "loading":
        now = main.time()

        if now - last_time >= loading_speed / 400.0:
            last_time = now
            if loading_index < len(loading_text):
                loading_index += 1

        txt = loading_text[:loading_index]
        main.draw_text(txt, "white", 100, 100, font)
        main.draw_text("Press (e) to skip", "#7A0000", 100, main.win.height - 100, font)
        loading_state = "entertaiment-text"


def drawPlayer():
    global state
    if state == "game-play":
        player.update()


def drawMainRoom():
    global draw_text_state, gameplay_animation_complete

    if state == "game-play":
        if draw_text_state == "-":
            draw_text_state = "first-10"
            gameplay_animation_complete = False

        main_room = main.load_image("Assets/Image/Background/Room/room.png")
        main_room = main.transform_image(main_room, main.full_window_size())
        main.render_image(main_room, (0, 0))
        drawPlayer()
        drawAnimatedText()


def drawAnimatedText():
    global draw_text_state, gameplay_index, gameplay_last_time, gameplay_animation_complete

    if draw_text_state == "first-10":
        gameplay_index = 0
        gameplay_last_time = main.time()
        draw_text_state = "animating"

    elif draw_text_state == "animating" and not gameplay_animation_complete:
        now = main.time()

        if now - gameplay_last_time >= gameplay_speed / 400.0:
            gameplay_last_time = now
            if gameplay_index < len(gameplay_text):
                gameplay_index += 1

        txt = gameplay_text[:gameplay_index]
        main.draw_text(txt, "white", 100, 100, font)

        if gameplay_index >= len(gameplay_text):
            gameplay_animation_complete = True
            draw_text_state = "completed"

    elif draw_text_state == "completed":
        main.draw_text(gameplay_text, "white", 100, main.win.height - 100, font)


def isInGame():
    if state == "game-play":
        return True
    return False


def handle_condition():
    global other_text

    if isInGame():
        main.draw_text(f"Subject: {subject}\nNight: {night}\n{other_text}", "white", main.win.width - 400, 100, font)

        if check_collision(player.rect, BED_RECT):
            other_text = "Press (e) to sleep."
        else:
            other_text = ""


def update():
    main.set_color("black")
    render_menu()
    render_loading()
    drawMainRoom()
    handle_condition()
    draw_sleep_animation()


def eventFunc():
    global state, loading_state, subject, other_text
    global gameplay_text, gameplay_index, gameplay_last_time, gameplay_speed, gameplay_animation_complete, draw_text_state

    if main.is_clicked(pg.K_e):
        if state == "loading":
            if loading_state == "entertaiment-text":
                state = "game-play"
                loading_state = "-"
        elif state == "game-play":
            if draw_text_state == "completed" or draw_text_state == "animating":
                if gameplay_text == "Uh, again it is night and moon comes up.\nI wish I don't have any nightmares this time.\nPress (e) to continue.":
                    gameplay_text = "I can't forget that monsters, jungle, those dark shadows...\nPress (e) to continue."
                    gameplay_index = 0
                    gameplay_last_time = 0
                    gameplay_speed = 50
                    gameplay_animation_complete = False
                    draw_text_state = "-"
                elif gameplay_text == "I can't forget that monsters, jungle, those dark shadows...\nPress (e) to continue.":
                    gameplay_text = "Let's go to bed and sleep.\nThink positive to not think about those... , never mind\nPress (e) to continue."
                    gameplay_index = 0
                    gameplay_last_time = 0
                    gameplay_speed = 50
                    gameplay_animation_complete = False
                    draw_text_state = "-"
                elif gameplay_text == "Let's go to bed and sleep.\nThink positive to not think about those... , never mind\nPress (e) to continue.":
                    subject = "Go to bed and sleep."
                    gameplay_index = 0
                    gameplay_last_time = 0
                    gameplay_speed = 50
                    gameplay_animation_complete = False
                    draw_text_state = "-"

            elif other_text == "Press (e) to sleep.":
                other_text = ""
                state = "sleep-time"

main = Engine("Phobia Of Darkness", (True, (0, 0)))
font = main.load_font("Assets/Font/font.ttf", 32)
player = Player(main)
pg = get_pg()

window_w, window_h = main.full_window_size()
BED_RECT = get_pg().Rect(int(window_w * 0.25) + 150, int(window_h * 0.25), int(window_w * 0.25), int(window_h * 0.4))
smath_sound = main.load_music("Assets/Sound/smash.wav")
strange_sound = main.load_music("Assets/Sound/strange.mp3")

main.run(update, eventFunc)