from Engine.main import Engine
import Assets.UI.button as btns
import sys

# vars
state = "menu"

# menu action
def start():
    pass

# functions
def render_menu():
    global state
    if state == "menu":
        main.render_image(main.transform_image(main.load_image("Assets/Image/Background/Menu/MenuBackground.png"), main.full_window_size()), (0, 0))
        menu_btn = btns.get_menu_start(main, font)
        for btn in menu_btn:
            btn.draw(main.win)
        btns.create_action(menu_btn, [start, sys.exit])

def update():
    main.set_color("black")
    render_menu()

main = Engine("Phobia Of Darkness", (True, (0,0)))
font = main.load_font("Assets/Font/font.ttf", 32)

main.run(update)