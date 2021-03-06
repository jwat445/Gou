import tcod as libtcod


def menu(con, header, options, width, screen_width, screen_height):
    if len(options) > 26:
        raise ValueError("Cannot have menu with more than 26 options.")

    # calculate header height and give one line per option
    header_height = libtcod.console_get_height_rect(
        con, 0, 0, width, screen_height, header
    )
    height = len(options) + header_height

    # create an off-screen console for the menu window
    window = libtcod.console_new(width, height)

    # print the header, with auto-wrap
    libtcod.console_set_default_foreground(window, libtcod.white)
    libtcod.console_print_rect_ex(
        window, 0, 0, width, height, libtcod.BKGND_NONE, libtcod.LEFT, header
    )

    # print the menu options
    y = header_height
    letter_index = ord("a")
    for option_text in options:
        text = "(" + chr(letter_index) + ")" + option_text
        libtcod.console_print_ex(window, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, text)
        y += 1
        letter_index += 1

    # blit the "window" to the root console
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2)
    libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)


def inventory_menu(con, header, player, inventory_width, screen_width, screen_height):
    if len(player.inventory.items) == 0:
        options = ["Inventory is empty."]
    else:
        options = []

        for item in player.inventory.items:
            if player.equipment.main_hand == item:
                options.append("{0} held in main hand".format(item.name))
            elif player.equipment.off_hand == item:
                options.append("{0} held in off hand".format(item.name))
            elif player.equipment.head == item:
                options.append("{0} worn on head".format(item.name))
            elif player.equipment.chest == item:
                options.append("{0} worn on chest".format(item.name))
            elif player.equipment.hands == item:
                options.append("{0} worn on hands".format(item.name))
            elif player.equipment.legs == item:
                options.append("{0} worn on legs".format(item.name))
            elif player.equipment.feet == item:
                options.append("{0} worn on feet".format(item.name))
            else:
                options.append(item.name)

    menu(con, header, options, inventory_width, screen_width, screen_height)


def main_menu(con, background_image, screen_width, screen_height):
    libtcod.image_blit_2x(background_image, 0, 0, 0)

    libtcod.console_set_default_foreground(0, libtcod.light_yellow)
    libtcod.console_print_ex(
        0,
        int(screen_width / 2),
        int(screen_height / 2) - 4,
        libtcod.BKGND_NONE,
        libtcod.CENTER,
        "GOU",
    )

    menu(
        con,
        "",
        ["New Game", "Continue", "Arena", "Quit"],
        24,
        screen_width,
        screen_height,
    )


def level_up_menu(con, header, player, menu_width, screen_width, screen_height):
    options = [
        "Constitution (+20 HP, from {0})".format(player.fighter.max_hp),
        "Strength (+1 attack, from {0})".format(player.fighter.power),
        "Agility (+1 defense, from {0})".format(player.fighter.defense),
        "Speed (-10 speed, from {0})".format(player.fighter.speed)
    ]

    menu(con, header, options, menu_width, screen_width, screen_height)


def character_screen(
    player, char_screen_width, char_screen_height, screen_width, screen_height
):
    window = libtcod.console_new(char_screen_width, char_screen_height)

    libtcod.console_set_default_foreground(window, libtcod.white)

    libtcod.console_print_rect_ex(
        window,
        0,
        1,
        char_screen_width,
        char_screen_height,
        libtcod.BKGND_NONE,
        libtcod.LEFT,
        "Character Information",
    )
    libtcod.console_print_rect_ex(
        window,
        0,
        2,
        char_screen_width,
        char_screen_height,
        libtcod.BKGND_NONE,
        libtcod.LEFT,
        "Level: {0}".format(player.level.current_level),
    )
    libtcod.console_print_rect_ex(
        window,
        0,
        3,
        char_screen_width,
        char_screen_height,
        libtcod.BKGND_NONE,
        libtcod.LEFT,
        "Experience: {0}".format(player.level.current_xp),
    )
    libtcod.console_print_rect_ex(
        window,
        0,
        4,
        char_screen_width,
        char_screen_height,
        libtcod.BKGND_NONE,
        libtcod.LEFT,
        "Experience to Level: {0}".format(player.level.experience_to_next_level),
    )
    libtcod.console_print_rect_ex(
        window,
        0,
        6,
        char_screen_width,
        char_screen_height,
        libtcod.BKGND_NONE,
        libtcod.LEFT,
        "Maximum HP: {0}".format(player.fighter.max_hp),
    )
    libtcod.console_print_rect_ex(
        window,
        0,
        7,
        char_screen_width,
        char_screen_height,
        libtcod.BKGND_NONE,
        libtcod.LEFT,
        "Attack: {0}".format(player.fighter.power),
    )
    libtcod.console_print_rect_ex(
        window,
        0,
        8,
        char_screen_width,
        char_screen_height,
        libtcod.BKGND_NONE,
        libtcod.LEFT,
        "Defense: {0}".format(player.fighter.defense),
    )
    libtcod.console_print_rect_ex(
        window,
        0,
        9,
        char_screen_width,
        char_screen_height,
        libtcod.BKGND_NONE,
        libtcod.LEFT,
        "Speed: {0}".format(player.fighter.speed),
    )

    x = screen_width // 2 - char_screen_width // 2
    y = screen_height // 2 - char_screen_height // 2
    libtcod.console_blit(
        window, 0, 0, char_screen_width, char_screen_height, 0, x, y, 1.0, 0.7
    )

def message_box(con, header, width, screen_width, screen_height):
    menu(con, header, [], width, screen_width, screen_height)
