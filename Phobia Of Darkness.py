from Engine.main import Engine, get_pg
import Assets.UI.button as btns
import sys

# vars
state = "menu"
loading_state = "-"
loading_text = "I'm oo .. only ..3.. no 4 years old.\nI am a giirl bbut I ammmm sc..scared from dd..darkness.\nMy Mom and Dad don'tttt ll.llet me out to sleep with them."
loading_index = 0
loading_speed = 50
last_time = 0

# menu action
def start():
    global state
    state = "loading"

# functions
def render_menu():
    if state == "menu":
        main.render_image(main.transform_image(main.load_image("Assets/Image/Background/Menu/MenuBackground.png"), main.full_window_size()), (0, 0))
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

def update():
    main.set_color("black")
    render_menu()
    render_loading()

def eventFunc():
    global state, loading_state
    if main.is_clicked(pg.K_e):
        if state == "loading":
            if loading_state == "entertaiment-text":
                state = "game-play"
                loading_state = "-"

main = Engine("Phobia Of Darkness", (True, (0,0)))
font = main.load_font("Assets/Font/font.ttf", 32)
pg = get_pg()

main.run(update, eventFunc)