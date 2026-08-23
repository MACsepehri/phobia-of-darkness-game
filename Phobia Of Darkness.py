from Engine.main import Engine
import Assets.UI.button as btns

# vars
state = "menu"

# functions
def render_menu():
    global state
    if state == "menu":
        main.render_image(main.load_image("Assets/Image/Background/Room/room.png"), (100, 100))
        for btn in btns.get_menu_start(main, font):
            btn.draw(main.win)

def update():
    main.set_color("black")
    render_menu()

main = Engine("Phobia Of Darkness", (True, (0,0)))
font = main.load_font("Assets/Font/font.ttf", 32)

main.run(update)