from Engine.main import Engine, Player, get_pg, check_collision
import Assets.UI.button as btns
import sys
import time

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
start_night_timer = 0

# night 1 data
inner_start_night_1_timer = 0
start_inner_start_night_1_timer = True
inner_start_wake_up_night_1_timer = 0
start_wake_up_night_1_timer = False

show_awake_image = False

# animated texts
gameplay_text = "Uh, again it is night and moon comes up.\nI wish I don't have any nightmares this time.\nPress (e) to continue."
gameplay_index = 0
gameplay_last_time = 0
gameplay_speed = 50
gameplay_animation_complete = False
draw_text_state = "-"
start_animation_of_sleep_smash = False

dialogue_index = 0
dialogues = [
    "Uh, again it is night and moon comes up.\nI wish I don't have any nightmares this time.\nPress (e) to continue.",
    "I can't forget those monsters, jungle, those dark shadows...\nPress (e) to continue.",
    "Let's go to bed and sleep.\nThink positive to not think about those... , never mind\nPress (e) to continue."
]

e_key_cooldown = 0
e_key_delay = 0.4

# menu action
def start():
    global state
    state = "loading"

# functions
def draw_sleep_animation():
    global start_animation_of_sleep_smash, start_night_timer, state, subject

    if state == "sleep-time":
        main.draw_text(f"Night {night}", "white", 100, 100, big_font, True)
        subject = ""
        if not start_animation_of_sleep_smash:
            smash_sound.play()
            pg.time.wait(2000)
            strange_sound.play()
            start_animation_of_sleep_smash = True

        if start_night_timer != 500:
            start_night_timer += 1
        else:
            state = "night-1"

def renderNight1():
    global inner_start_night_1_timer, start_inner_start_night_1_timer, gameplay_text, draw_text_state, dialogue_index
    global inner_start_wake_up_night_1_timer, start_wake_up_night_1_timer
    global show_awake_image, state

    if state == "night-1":
        if not show_awake_image:
            bg = main.load_image("Assets/Image/Background/Room/sleep.png")
        else:
            bg = main.load_image("Assets/Image/Background/Room/not-sleep-with-open-eyes.png")

        bg = main.transform_image(bg, (window_w, window_h))
        main.render_image(bg, (0, 0))

        if inner_start_night_1_timer < 300 and start_inner_start_night_1_timer:
            inner_start_night_1_timer += 1
            return

        if start_inner_start_night_1_timer:
            gameplay_text = "Uh ... , what was that fucking sound?\nPress (e) to continue."
            draw_text_state = "first-10"
            start_inner_start_night_1_timer = False
            paranormal_sound.play(0)

            if "Uh ... , what was that fucking sound?" not in dialogues[0]:
                dialogues.append("Uh ... , what was that fucking sound?\nPress (e) to continue.")

            show_awake_image = True
            start_wake_up_night_1_timer = True
            return

        if start_wake_up_night_1_timer:
            if inner_start_wake_up_night_1_timer < 140:
                inner_start_wake_up_night_1_timer += 1
                return
            else:
                start_wake_up_night_1_timer = False
                state = "night-1-start"
                inner_start_wake_up_night_1_timer = 0
                gameplay_text = "What is that sound? It doesn't looks normal.\nPress (e) to continue."
                draw_text_state = "first-10"
                return

        drawAnimatedText()

def roomInStartedNight1():
    global state, draw_text_state, gameplay_text, gameplay_animation_complete

    if state == "night-1-start":
        bg = main.load_image("Assets/Image/Background/Room/room.png")
        bg = main.transform_image(bg, (window_w, window_h))
        main.render_image(bg, (0, 0))

        player.update()

        if draw_text_state != "-":
            drawAnimatedText()

        main.draw_text(f"Subject: {subject}\nNight: {night}", "white", main.win.width - 450, 100, font)

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
    if state == "game-play" or state == "night-1-start":
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
        main.draw_text(gameplay_text, "white", 100, 100, font)

def isInGame():
    if state == "game-play":
        return True
    return False

def handle_condition():
    global other_text

    if isInGame() or state == "night-1-start":
        main.draw_text(f"Subject: {subject}\nNight: {night}\n{other_text}", "white", main.win.width - 450, 100, font)

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
    renderNight1()
    roomInStartedNight1()

def eventFunc():
    global state, loading_state, subject, other_text
    global gameplay_text, gameplay_index, gameplay_last_time, gameplay_speed, gameplay_animation_complete, draw_text_state
    global dialogue_index, e_key_cooldown

    current_time = time.time()
    if main.is_clicked(pg.K_e) and current_time - e_key_cooldown >= e_key_delay:
        e_key_cooldown = current_time

        if state == "loading":
            if loading_state == "entertaiment-text":
                state = "game-play"
                loading_state = "-"
                dialogue_index = 0
                gameplay_text = dialogues[0]
                gameplay_index = 0
                gameplay_last_time = main.time()
                gameplay_speed = 50
                gameplay_animation_complete = False
                draw_text_state = "first-10"

        elif state == "game-play":
            if other_text == "Press (e) to sleep." and draw_text_state == "completed" and check_collision(player.rect, BED_RECT):
                other_text = ""
                state = "sleep-time"
                return

            if draw_text_state == "completed" or draw_text_state == "animating":
                current_text = gameplay_text
                found_index = -1
                for i, text in enumerate(dialogues):
                    if text == current_text:
                        found_index = i
                        break

                if found_index != -1:
                    if found_index + 1 < len(dialogues):
                        dialogue_index = found_index + 1
                        gameplay_text = dialogues[dialogue_index]
                        gameplay_index = 0
                        gameplay_last_time = main.time()
                        gameplay_speed = 50
                        gameplay_animation_complete = False
                        draw_text_state = "first-10"
                    else:
                        subject = "Go to bed and sleep."
                        gameplay_text = ""
                        gameplay_index = 0
                        gameplay_last_time = main.time()
                        gameplay_speed = 50
                        gameplay_animation_complete = False
                        draw_text_state = "completed"
                else:
                    if current_text not in dialogues:
                        dialogues.append(current_text)
                        dialogue_index = len(dialogues) - 1

                    if dialogue_index + 1 < len(dialogues):
                        dialogue_index += 1
                        gameplay_text = dialogues[dialogue_index]
                        gameplay_index = 0
                        gameplay_last_time = main.time()
                        gameplay_speed = 50
                        gameplay_animation_complete = False
                        draw_text_state = "first-10"
                    else:
                        subject = "Go to bed and sleep."
                        gameplay_text = "..."
                        gameplay_index = 0
                        gameplay_last_time = main.time()
                        gameplay_speed = 50
                        gameplay_animation_complete = False
                        draw_text_state = "completed"

        elif state == "night-1-start":
            if draw_text_state == "completed" or draw_text_state == "animating":
                if gameplay_text == "What is that sound? It doesn't looks normal.\nPress (e) to continue.":
                    gameplay_text = "..."
                    gameplay_index = 0
                    gameplay_last_time = main.time()
                    gameplay_speed = 50
                    gameplay_animation_complete = False
                    draw_text_state = "first-10"

main = Engine("Phobia Of Darkness", (True, (0, 0)))
font = main.load_font("Assets/Font/font.ttf", 32)
big_font = main.load_font("Assets/Font/font.ttf", 48)
player = Player(main)
pg = get_pg()

window_w, window_h = main.full_window_size()
BED_RECT = get_pg().Rect(int(window_w * 0.25) + 150, int(window_h * 0.25), int(window_w * 0.25), int(window_h * 0.4))
smash_sound = main.load_music("Assets/Sound/smash.wav")
strange_sound = main.load_music("Assets/Sound/strange.mp3")
paranormal_sound = main.load_music("Assets/Sound/paranormal.mp3")

main.run(update, eventFunc)