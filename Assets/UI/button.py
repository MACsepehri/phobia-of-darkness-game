from Engine.Assets.UI import Button


def get_menu_start(main, font):
    start = main.button(
        main.win.width / 2 - 200 / 2,
        main.win.height / 2 - 90,
        200,
        90,
        "Start",
        font,
        button_color="#0A0A0A",
        text_color="#7A0000"
    )
    exit_btn = main.button(
        main.win.width / 2 - 200 / 2,
        main.win.height / 2 - 90 / 2 + 90,
        200,
        90,
        "Exit",
        font,
        button_color="#0A0A0A",
        text_color="#7A0000"
    )
    return [start, exit_btn]

def create_action(btn, action):
    if isinstance(btn, list):
        i = 0
        for button in btn:
            if button.is_clicked():
                action[i]()
            i += 1
    else:
        if btn.is_clicked():
            action()