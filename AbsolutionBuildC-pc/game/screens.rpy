################################################################################
## Initialization
################################################################################

init offset = -1
    
################################################################################
## Styles
################################################################################
style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button :
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    xsize 30
    ysize 300
    left_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
    bar_vertical True

style vbar:
    xsize 25
    ysize 300
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
    unscrollable "insensitive"
    bar_vertical False

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################

## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 1.0 yalign 1.0


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.2, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos -0.05
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos 0.2
    xsize gui.dialogue_width
    ypos 0.29


##Alternative textbox
screen cinematic(who, what):
    style_prefix "cinematic"

    window:
        id "cinematic_window"

        if who is not None:

            window:
                style "cinematic_namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 1.0 yalign 1.0


style cinematic_window:
    xalign 0.0
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    ypos 762

    background Image("gui/cin.png", xpos=0, ypos=-100)

style cinematic_namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos 20
    ysize gui.namebox_height
    background Image("gui/quickmenu.png")

style cinematic_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style cinematic_dialogue:
    properties gui.text_properties("dialogue")
    xpos 0.2
    xsize gui.dialogue_width
    ypos 200
## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign 0.5
            xpos 0.5
            xsize gui.dialogue_width
            ypos 0.3

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    add "gui/choicebg.png" at notify_appear
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action at notify_appear


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text


style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    activate_sound "click.ogg" 
    hover_sound "hover.ogg"

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:
        add "gui/quickmenu.png"

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.99

            textbutton _("Back ") action Rollback()
            textbutton _(" Skip ") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _(" Auto ") action Preference("auto-forward", "toggle")
            textbutton _(" History ") action ShowMenu('history')
            if journal:
                textbutton _(" Journal ") action ShowMenu('journal')
            textbutton _(" Save ") action ShowMenu('save')
            textbutton _(" Load ") action ShowMenu('load')
            textbutton _(" Settings ") action ShowMenu('preferences')
            textbutton _(" Main Menu ") action MainMenu()
            textbutton _(" Quit") action Quit(confirm=not main_menu)

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound "click.ogg" 
    hover_sound "hover.ogg"

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    

################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "Navigation"
        xalign 0.5
        ypos 0.52
        spacing gui.navigation_spacing
        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        textbutton _("New game") action Start()
        textbutton _("Continue") action ShowMenu("load")
        textbutton _("  Help") action ShowMenu("about")
        textbutton _("Credits") action ShowMenu("credits"):
            xpos 6
        textbutton _("Settings") action ShowMenu("preferences")

    if renpy.variant("pc"):
        textbutton _("Quit"): 
            yalign 0.997
            xalign 0.96
            action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    activate_sound "click.ogg" 
    hover_sound "hover.ogg"

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

        
## Game menu navigation screen ################################################

screen navimenu():

    vbox:
        style_prefix "Navigation"
        xpos 0.025
        ypos 0.3
        spacing gui.navigation_spacing
        if _in_replay:
            textbutton _(" End Replay") action EndReplay(confirm=True)
        if not main_menu:
            textbutton _("Save") action ShowMenu("save")
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Help") action ShowMenu("about")
        textbutton _("History") action ShowMenu("history")
        textbutton _("Settings") action ShowMenu("preferences")
        if not main_menu and journal:
            textbutton _("Journal") action ShowMenu("journal")
        if not main_menu and (month==2 or day>1):
            textbutton _("Statistics") action ShowMenu("statistics")

    if renpy.variant("pc"):
        textbutton _("Quit"): 
            yalign 0.997
            xalign 0.96
            action Quit(confirm=not main_menu)

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"
    ## add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass
    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 0.5
    xoffset -20
    xmaximum 800
    yalign 0.5
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("")

style main_menu_version:
    properties gui.text_properties("")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):
    
    
    style_prefix "game_menu"

    add gui.game_menu_background
        
    use navimenu
    
    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    textbutton _("Return"): 
        yalign 0.998
        xalign 0.01
        activate_sound "back.ogg" 
        hover_sound "hover.ogg"
        action Return()        

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 100
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 80
    right_margin 0
    top_margin 0

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 30

style game_menu_label:
    xpos 0.5
    ypos 100
    ysize 100

style game_menu_label_text:
    size 30
    color gui.accent_color
    yalign -0.2
    xalign -0.3

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0

screen statistics():
    tag menu
    use game_menu(_("Statistics")):
        hbox:
            xpos 100
            ypos 100
            spacing 10
            vbox:
                xsize 300
                text _("{size=30}Name: {color=#ffffff}[name] Hart")
                text _(" Sanity:\n  [sanity]/50")
                text _(" Empathy:")
                if he:
                    text _("  You are liked.")
                elif le:
                    text _("  You are disliked.")
                else:
                    text _("  You are somewhat liked.")
                if month==1:
                    text _("\n\n{size=30}{color=#ffffff}Days at work: [day]")
                else:
                    text _("\n\n{size=30}{color=#ffffff}Days at work: [day+30]")
            vbox:
                xsize 300
                text _("{size=30}Sessions spent with:{/size}\n Charlie: [blueinteract]\n Tom: [purpleinteract]\n Michael: [redinteract]\n William: [silverinteract]\n\n")
                text _("{size=30}Friends at the hospital:")
                if SunLink==0 and TempLink==0 and StarLink==0:
                    text _(" You have no friends yet.")
                if SunLink>0:
                    text _(" Sue: rank [SunLink]/6")
                if TempLink>0:
                    text _(" Julia: rank [TempLink]/6")
                if StarLink>0:
                    text _(" Dr. Young: rank [StarLink]/6")
    
screen journal():
    tag menu
    use game_menu(_("Journal")):
        add "gui/overlay/journal.png"
        text _("This is the journal screen. It updates whenever you gain new information about the world."):
            ypos 30
        hbox:
            style_prefix "Navigation"
            ypos 180
            spacing 50
            textbutton _("CHARACTERS\nView information\nabout the various\npeople you have met.") action ShowMenu("charnav")
            textbutton _("LOCATIONS\nView information about\nthe locations you have seen.") action ShowMenu("locations")

screen locations():
    tag menu
    use game_menu(_("")):
        add "gui/overlay/locations.png"
        text _("Which location would you like to view?"):
            ypos 0.0
            xpos 0.195
        vbox:
            style_prefix "Navigation"
            xpos 0.0
            ypos 0.2
            spacing gui.navigation_spacing
            textbutton _("Reception") action ShowMenu("area1")
            textbutton _("Cafeteria") action ShowMenu("area2")
            textbutton _("Patient rooms") action ShowMenu("area3")
            textbutton _("Central hall") action ShowMenu("area4")
            textbutton _("Offices") action ShowMenu("area5")
            if month>1 or day>2:
                textbutton _("Courtyard") action ShowMenu("area6")
            if explor0:
                textbutton _("Hospital map") action ShowMenu("area13")
        vbox:
            style_prefix "Navigation"
            xpos 0.25
            ypos 0.2
            spacing gui.navigation_spacing
            textbutton _("The hospital") action ShowMenu("area9")
            textbutton _("The town") action ShowMenu("area10")
            textbutton _("The woods") action ShowMenu("area11")
            if day>5 or month>1:
                textbutton _("My house") action ShowMenu("area12")

screen locnav():
    style_prefix "game_menu"

    add gui.game_menu_background
    add "gui/overlay/loc.png"
    
    textbutton _("Back to location selection"): 
        yalign 0.998
        xalign 0.01
        activate_sound "back.ogg" 
        hover_sound "hover.ogg"
        action ShowMenu("locations")
    
    textbutton _("Leave the Info screen"): 
        yalign 0.998
        xalign 0.98
        activate_sound "back.ogg" 
        hover_sound "hover.ogg"
        action Return()
        
screen area1():
    tag menu
    use locnav
    add "gui/loc/area1.png"
    text _("{color=#ffffff}THE RECEPTION{/color}\n\nThe first room in the hospital. There's always a nurse watching the front door to make sure nobody who shouldn't be here enters.\n\nThe reception is connected to the security room through a locked door, where guards watch the cameras."):
        xpos 0.25
        ypos 0.2
        xsize 500
screen area2():
    tag menu
    use locnav
    add "gui/loc/area2.png"
    text _("{color=#ffffff}THE CAFETERIA{/color}\n\nThe place where patients eat their meals. It gets a little busy around noon, but otherwise is mostly empty, save for certain nurses who have made it their hangout spot."):
        xpos 0.25
        ypos 0.2
        xsize 500
screen area3():
    tag menu
    use locnav
    add "gui/loc/area3.png"
    text _("{color=#ffffff}THE PATIENT ROOMS{/color}\n\nThere are eighteen patient rooms that open to this hallway and another, isolated one that connects to the nurses' office at the end of it, room XXI.\nMost nurses can rarely actually be found in the office, since they spend most of their work days doing various tasks around the hospital.\nMost patients can roam the areas accessible to them freely, while some, deemed dangerous, can only leave their rooms under supervision. The patient rooms get locked for the night so that nobody wanders around with only the night guard present."):
        xpos 0.25
        ypos 0.2
        xsize 500
screen area4():
    tag menu
    use locnav
    add "gui/loc/area4.png"
    text _("{color=#ffffff}THE CENTRAL HALL{/color}\n\nThis part of the hospital was never altered over the years. While it may seem pointless to use up so much space with no clear functionality, the hall has a clear role - lightening the atmosphere around the hospital with much-needed daylight.\nThe hall opens to the third floor and connects to most areas on the two floors, so people pass through there often."):
        xpos 0.25
        ypos 0.2
        xsize 500
screen area5():
    tag menu
    use locnav
    add "gui/loc/area5.png"
    text _("{color=#ffffff}THE OFFICES{/color}\n\nThere are four psychologist offices, numbered from I to IV. Mine is III. The psychiatrist offices, numbered V to VII, connect to the other side of the hallway. Office V belongs to Dr. Sharpe.\nThis hallway also ends with a staircase leading up to the third floor.\nPatients don't tend to pass through here unless they're waiting for a session, as the staircase is locked."):
        xpos 0.25
        ypos 0.2
        xsize 500
screen area6():
    tag menu
    use locnav
    add "gui/loc/area6.png"
    text _("{color=#ffffff}THE COURTYARD{/color}\n\nThis area, I imagine, gets quite crowded in the warmer seasons. Nurses are eager to let patients out to get some fresh air and sunlight and the other staffmembers seem to enjoy coming there. It's no surprise that this is a popular hangout spot for nurses and an even more popular location of patient fights and tensions that the staff has to then mediate in.\nThe area is surrounded by a high fence made of wire that separates the hospital from the Dawnbright Woods around it."):
        xpos 0.25
        ypos 0.2
        xsize 500
screen area9():
    tag menu
    use locnav
    add "gui/loc/area9.png"
    text ("{color=#ffffff}ST. AUGUSTINE'S HOSPITAL{/color}\nEstablished in 1863 to house patients from the nearby city, this hospital is long past its glory days. Understaffed and crowded, it houses around 30 patients while originally built as a small facility of up to 12, ran by the local church of St. Augustine. The institution has long since passed into secular hands as the church lost followers. Going from one more of less involved owner to the next, it's currently in the hands of some well-off businessman whose name escapes me.\nThe hospital has long been the subject of unfounded rumors typical of mental health facilities. Some people say that once you are admitted, you can't leave - it's obviously not true and only serves to feed the grudge many people already have against the institution."):
        xpos 0.25
        ypos 0.2
        xsize 500
screen area10():
    tag menu
    use locnav
    add "gui/loc/area10.png"
    text ("{color=#ffffff}THE TOWN OF AUGUSTINE{/color}\n\nThis town was built in the mid-19th century by the church of St. Augustine. For a long time it was ran by the local priests, along with the hospital, until it shifted to be under government control.\nIt is currently a small town, occupied mostly by older folk who refuse to leave for the city, and the staff of the local hospital."):
        xpos 0.25
        ypos 0.2
        xsize 500
screen area11():
    tag menu
    use locnav
    add "gui/loc/area11.png"
    text ("{color=#ffffff}THE WOODS{/color}\n\nThe Dawnbright Woods is a small forest that surrounds the hospital. The name is older than any local settlement. The forest used to be much larger and spread far to the north and east, but has since been split into two, by the town of Augustine and the hospital, the western half getting the name \"Sunset Forest\", much of which was cut down in the construction of the main road and the expansion of the city.\nThe forest, much like the hospital, is the subject of many unlikely rumors, some older townsfolk even claiming that it is the home of evil spirits."):
        xpos 0.25
        ypos 0.2
        xsize 500
screen area12():
    tag menu
    use locnav
    add "gui/loc/area12.png"
    text ("{color=#ffffff}MY HOUSE{/color}\n\nWell, it's not {i}actually{/i} my house. The house I live in belongs to my high school friend, Amelia. Upon hearing of my wanting a job at St. Augustine's, she graciously offered for me to move in temporarily while she's away on business.\nAnd so, I moved in a day before my job interview - some might call it overconfidence, but I knew I could get hired if I tried hard enough - besides, where's the harm in that?"):
        xpos 0.25
        ypos 0.2
        xsize 500
screen area13():
    tag menu
    use locnav
    add "gui/loc/area13.png"

## Characters navigation screen ##############################################
screen charnav():
    tag menu
    use game_menu(_("")):
        add "gui/mc.png"
        text _("Whose information would you like to view?"):
            ypos 0.0
            xpos 0.195
        vbox:
            style_prefix "Navigation"
            xpos 0.0
            ypos 0.2
            spacing gui.navigation_spacing
            if name == "Me":
               pass
            else:
                textbutton _("Dr. Hart") action ShowMenu("mc")
            if persistent.Julia:
                textbutton _("Julia") action ShowMenu("temp")
            if persistent.Sue:
                textbutton _("Sue") action ShowMenu("sun")
            if persistent.Sharpe:
                textbutton _("Dr. Sharpe") action ShowMenu("hier")
            if persistent.William:
                textbutton _("William") action ShowMenu("moon")
            if persistent.Charlie:
                textbutton _("Charlie") action ShowMenu("hermit")
            if persistent.Tom:
                textbutton _("Tom") action ShowMenu("tower")
            if persistent.Michael:
                textbutton _("Michael") action ShowMenu("devil")
            if persistent.Elizabeth:
                textbutton _("Elizabeth") action ShowMenu("priest")
        vbox:
            style_prefix "Navigation"
            xpos 0.25
            ypos 0.2
            spacing gui.navigation_spacing
            if persistent.Young:
                textbutton _("Dr. Young") action ShowMenu("star")
            if persistent.Mil:
                textbutton _("[persistent.Milfirst]") action ShowMenu("lovers")
            if persistent.Caroline:
                textbutton _("Caroline") action ShowMenu("chariot")

screen char(): ##this is where I'll have the structure
    
    style_prefix "game_menu"

    add gui.game_menu_background
    add "gui/overlay/char.png"
    vbox:
        text _("{size=30}First name:\nLast name:{/size}\n\nHeight:\nAge:\nBirthday:\n\n{size=30}Info:")
        xpos 0.55
        ypos 0.2
    
    textbutton _("Back to character selection"): 
        yalign 0.998
        xalign 0.01
        activate_sound "back.ogg" 
        hover_sound "hover.ogg"
        action ShowMenu("charnav")
    
    textbutton _("Leave the Info screen"): 
        yalign 0.998
        xalign 0.98
        activate_sound "back.ogg" 
        hover_sound "hover.ogg"
        action Return()

screen charnotes():
    style_prefix "game_menu"
    add gui.game_menu_background
    add "gui/overlay/char.png"
    
    textbutton _("Back to character selection"): 
        yalign 0.998
        xalign 0.01
        activate_sound "back.ogg" 
        hover_sound "hover.ogg"
        action ShowMenu("charnav")
    
    textbutton _("Leave the Info screen"): 
        yalign 0.998
        xalign 0.98
        activate_sound "back.ogg" 
        hover_sound "hover.ogg"
        action Return()
    
screen mc():
    tag menu
    use char
    add "gui/chars/mc.png"
    vbox:
        text _("{size=30}                        [name]\n                        Hart{/size}\n\n                 165 cm (5'5\")\n          28\n                    24th of October \n\n\n\nI'm just a psychologist hoping to help people in need.")
        if gameon:
            vbar:
                value side+30
                range 60
                left_bar "gui/alaw.png"
                right_bar "gui/achaos.png"
                xysize(600, 30)
                xpos -90
                ypos 90
        xpos 0.55
        ypos 0.2
        
screen temp():
    tag menu
    use char
    add "gui/chars/temp.png"
    vbox:
        text _("{size=30}                        Julia\n                        [persistent.Julialast]{/size}\n\n                 168 cm (5'6\")\n          30\n                    12th of April \n\n\n\nA nurse at St. Augustine's hospital.\nShe was the first person I met when I arrived\nthere, working as the receptionist at the time.\nShe seems to dislike her job.")
        xpos 0.55
        ypos 0.2

screen sun():
    tag menu
    use char
    add "gui/chars/sun.png"
    vbox:
        text _("{size=30}                        Sue\n                        [persistent.Suelast]{/size}\n\n                 156 cm (5'1\")\n           28\n                    28th of March \n\n\n\nA nurse at St. Augustine's hospital.\nShe showed me around before my job interview.\nShe seems to really care about her coworkers and likes\nto spend her breaks with Julia, a fellow nurse.")
        xpos 0.55
        ypos 0.2  
        
screen hier():
    tag menu
    use char
    add "gui/chars/hier.png"
    vbox:
        text _("{size=30}                        [persistent.Sharpefirst]\n                        Sharpe{/size}\n\n                 191 cm (6'3\")\n           [persistent.Sharpeage]\n                    11th of November \n\n\n\nThe overseeing psychiatrist at St. Augustine's hospital.\nHe interviewed me when I first came to the hospital.\nHe seems very proffessional and strict, but the staff\nappears to appreciate what he does.")
        xpos 0.55
        ypos 0.2

screen moon():
    tag menu
    use char
    add "gui/chars/moon.png"
    vbox:
        text _("{size=30}                        William\n                        Moore{/size}\n\n                 176 cm (5'9\")\n           26\n                    1st of July \n\n\n\nOne of my patients, diagnosed with GAD.\nHe's been here for two years now.\nDespite his condition, he refuses to cooperate\nwith most staff members.")
        xpos 0.55
        ypos 0.2
    vbox:
        textbutton _("Show notes"):
            activate_sound "back.ogg" 
            hover_sound "hover.ogg"
            action ShowMenu("moonnotes")
        yalign 0.855
        xalign 0.348
screen moonnotes():
    tag menu
    use charnotes
    add "gui/chars/moon.png"
    vbox:
        text _("{size=30}My notes{size=17}\n1. [nmoon1]\n2. [nmoon2]\n3. [nmoon3]\n4. [nmoon4]\n5. [nmoon5]\n6. [nmoon6]\n7. [nmoon7]\n8. [nmoon8]\n9. [nmoon9]\n10. [nmoon10]\n11. [nmoon11]\n12. [nmoon12]\n13. [nmoon13]\n14. [nmoon14]\n15. [nmoon15]\n6. [nmoon16]\n17. [nmoon17]\n18. [nmoon18]\n19. [nmoon19]\n20. [nmoon20]")
        xpos 0.55
        ypos 0.2
    vbox:
        textbutton _("Hide notes"):
            activate_sound "back.ogg" 
            hover_sound "hover.ogg"
            action ShowMenu("moon")
        yalign 0.855
        xalign 0.348
        
screen hermit():
    tag menu
    use char
    add "gui/chars/hermit.png"
    vbox:
        text _("{size=30}                        Charlie\n                        ????{/size}\n\n                 187 cm (6'1\")\n           23?\n                     ????\n\n\nOne of my patients, diagnosed with schizophrenia.\nHe seems friendly and \"normal\" compared to\nother patients, but he can't provide any information\nabout his past and doesn't seem to realize the problem.")
        xpos 0.55
        ypos 0.2
    vbox:
        textbutton _("Show notes"):
            activate_sound "back.ogg" 
            hover_sound "hover.ogg"
            action ShowMenu("hermitnotes")
        yalign 0.855
        xalign 0.348
screen hermitnotes():
    tag menu
    use charnotes
    add "gui/chars/hermit.png"
    vbox:
        text _("{size=30}My notes{size=17}\n1. [nhermit1]\n2. [nhermit2]\n3. [nhermit3]\n4. [nhermit4]\n5. [nhermit5]\n6. [nhermit6]\n7. [nhermit7]\n8. [nhermit8]\n9. [nhermit9]\n10. [nhermit10]\n11. [nhermit11]\n12. [nhermit12]\n13. [nhermit13]\n14. [nhermit14]\n15. [nhermit15]\n6. [nhermit16]\n17. [nhermit17]\n18. [nhermit18]\n19. [nhermit19]\n20. [nhermit20]")
        xpos 0.55
        ypos 0.2
    vbox:
        textbutton _("Hide notes"):
            activate_sound "back.ogg" 
            hover_sound "hover.ogg"
            action ShowMenu("hermit")
        yalign 0.855
        xalign 0.348

screen tower():
    tag menu
    use char
    add "gui/chars/tower.png"
    vbox:
        text _("{size=30}                        Tom\n                        Richards{/size}\n\n                 183 cm (6'0\")\n           29\n                    16th of September \n\n\n\nOne of my patients, diagnosed with\nDID, and three alters.\nDue to being recently admitted, seems to feel\nout of place here - he claims there's nothing\nwrong with him.")
        xpos 0.55
        ypos 0.2
    vbox:
        textbutton _("Show notes"):
            activate_sound "back.ogg" 
            hover_sound "hover.ogg"
            action ShowMenu("towernotes")
        yalign 0.855
        xalign 0.348
        
screen towernotes():
    tag menu
    use charnotes
    add "gui/chars/tower.png"
    vbox:
        text _("{size=30}My notes{size=17}\n1. [ntower1]\n2. [ntower2]\n3. [ntower3]\n4. [ntower4]\n5. [ntower5]\n6. [ntower6]\n7. [ntower7]\n8. [ntower8]\n9. [ntower9]\n10. [ntower10]\n11. [ntower11]\n12. [ntower12]\n13. [ntower13]\n14. [ntower14]\n15. [ntower15]\n6. [ntower16]\n17. [ntower17]\n18. [ntower18]\n19. [ntower19]\n20. [ntower20]")
        xpos 0.55
        ypos 0.2
    vbox:
        textbutton _("Hide notes"):
            activate_sound "back.ogg" 
            hover_sound "hover.ogg"
            action ShowMenu("tower")
        yalign 0.855
        xalign 0.348

screen devil():
    tag menu
    use char
    add "gui/chars/devil.png"
    if persistent.DevilRed:
        add "gui/chars/devil2.png"
    vbox:
        text _("{size=30}                        Michael\n                        Burnett{/size}\n\n                 172 cm (5'7\")\n           26\n                    9th of June \n\n\n\nOne of my patients, diagnosed with\nObsessive Compulsive Disorder.\nHe's been here for three years. Most patients and\nstaff members claim to be unsettled by him due\nto his extremely aggressive nature that's caused\nmultiple incidents.")
        xpos 0.55
        ypos 0.2
    vbox:
        textbutton _("Show notes"):
            activate_sound "back.ogg" 
            hover_sound "hover.ogg"
            action ShowMenu("devilnotes")
        yalign 0.855
        xalign 0.348
screen devilnotes():
    tag menu
    use charnotes
    add "gui/chars/devil.png"
    if persistent.DevilRed:
        add "gui/chars/devil2.png"
    vbox:
        text _("{size=30}My notes{size=17}\n1. [ndevil1]\n2. [ndevil2]\n3. [ndevil3]\n4. [ndevil4]\n5. [ndevil5]\n6. [ndevil6]\n7. [ndevil7]\n8. [ndevil8]\n9. [ndevil9]\n10. [ndevil10]\n11. [ndevil11]\n12. [ndevil12]\n13. [ndevil13]\n14. [ndevil14]\n15. [ndevil15]\n6. [ndevil16]\n17. [ndevil17]\n18. [ndevil18]\n19. [ndevil19]\n20. [ndevil20]")
        xpos 0.55
        ypos 0.2
    vbox:
        textbutton _("Hide notes"):
            activate_sound "back.ogg" 
            hover_sound "hover.ogg"
            action ShowMenu("devil")
        yalign 0.855
        xalign 0.348

screen priest():
    tag menu
    use char
    add "gui/chars/priest.png"
    vbox:
        text _("{size=30}                        Elizabeth\n                        [persistent.Elizabethlast]{/size}\n\n                 160 cm (5'3\")\n           20\n                     21st of May \n\n\n\nA patient I met, diagnosed with Schizoid\nPersonality Disorder.\nShe seems to dislike being around other people.")
        xpos 0.55
        ypos 0.2

screen star():
    tag menu
    use char
    add "gui/chars/star.png"
    vbox:
        text _("{size=30}                        Charles\n                        Young{/size}\n\n                 178 cm (5'10\")\n           34\n                    13th of March\n\n\n\nA psychiatrist at St. Augustine's hospital.\nHe seems to enjoy my company.")
        xpos 0.55
        ypos 0.2
 
screen lovers():
    tag menu
    use char
    add "gui/chars/lovers.png"
    vbox:
        text _("{size=30}                        [persistent.Milfirst]\n                        [persistent.Millast]{/size}\n\n                 169 cm (5'6\")\n           29\n                    16th of February \n\n\n\n[persistent.Milbio]")
        xpos 0.55
        ypos 0.2    
        
screen chariot():
    tag menu
    use char
    add "gui/chars/chariot.png"
    vbox:
        text _("{size=30}                        Caroline\n                        Reed{/size}\n\n                 152 cm (5'0\")\n          25\n                    14th of August \n\n\n\nMichael's ex girlfriend.\nHe was admitted to the hospital after kidnapping\nand torturing her for two weeks before she escaped.\nShe wants nothing to do with him anymore and\nseems to hate him deeply for what he's done.")
        xpos 0.55
        ypos 0.2  
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
    tag menu
    use game_menu(_(""), scroll="viewport"):
        vbox:
            text _("This game was made using the Ren'py visual novel engine.\n\n{size=26}{color=#ffffff}Controls{/color}{/size}\n\n{b}H{/b}/{color=#a51010}Middle click{/color} — hide user interface\n{b}S{/b} — take a screenshot\n{b}V{/b} — toggle automatic self-voicing\n\n{b}Escape{/b}/{color=#a51010}Right click{/color} — pause menu\n\n{b}Space{/b} — advance dialogue\n{b}Enter{/b}/{color=#a51010}Right click{/color} — advances dialogue and activate the interface\n{b}Arrow keys{/b}/{color=#a51010}Mouse{/color} — navigate the interface\n{b}Page Up{/b}/{color=#a51010}Mouse wheel up{/color} — roll back to earlier dialogue\n{b}Page Down{/b}/{color=#a51010}Mouse wheel down{/color} — roll forward to later dialogue\n\n{b}Control{/b} (hold) — skip dialogue that's already been seen\n{b}Tab{/b} — toggle dialogue skipping")        
            xpos 0
            ypos 0.0
        
screen credits():
    tag menu
    use game_menu(_(""), scroll="viewport"):
        hbox:
            spacing 30
            vbox:
                xsize 250
                spacing 20
                text _("{size=30}Acknowledgements")
                add "gui/overlay/ack.png":
                    xpos -20
                    ypos -50
                text _("Story concept help:\n Katya"):
                    ypos -60
                text _("Pre-demo testing:\nJulia, Katya, Qilinia, Kornelia, Zofia, Kinga"):
                    ypos -60
                text _("Demo testing:\nSugary Sweet, WitchAngelNekora, the Visual Novelty"):
                    ypos -60
                text _("Act I testing:\nSugary Sweet, Julia, Valiola"):
                    ypos -60
                text _("Act II testing:\nSugary Sweet, Julia, Valiola, Casper Swann"):
                    ypos -60
                text _("Act III testing:\nValiola, megid0la"):
                    ypos -60
                text _("Easter egg character credit:\nCasper Swann: Jasper Finley\nSugarySweet: Lily Greene\nKatya: herself\nValiola: Maya\nOnyx: Saika"):
                    ypos -60
                text _("Additional thanks go to Stompy, Aether, Juno and Halszka for their contributions to the discord community."):
                    ypos -60
                text _("{i}Dedicated to friends, fans and my psychiatrist. For keeping me alive."):
                    ypos -60
            vbox:
                xsize 250
                spacing 20
                text _("{size=30}Voice acting")
                add "gui/overlay/va.png"
                text _("Red Queen: Milena and Lily Greene")
                text _("Onyx: Julia Watts and Saika")
                text _("Arthur Tisseront: Jasper Finley")
                text _("Valiola: Maya")
                
            vbox:
                xsize 250
                spacing 20
                text _("{size=30}Disclaimers")
                add "gui/overlay/dc.png"
                text _("CONTENT WARNINGS\nThis game contains:\nmental illness, blood and gore, suicide, murder, self-harm, sadism, masochism, sexual themes, rape, domestic abuse, jumpscares, and strong language.")
                text _("The opinions and beliefs expressed in this game do not necessarily reflect those of the developer or of those involved in the project.")
                text _("This game is not meant to be an accurate representation of life and work in a mental hospital.")
                text _("An effort was made to portray mental illness in an accurate and respectful manner. However, the developer does not guarantee complete accuracy to diagnosing criteria of every illness portrayed due to individual differences between patients.")
                text _("Please support mental health care and spread awareness.")
                text _("Bible quotes in english from:\nTHE HOLY BIBLE, NEW INTERNATIONAL VERSION®,\nNIV® Copyright © 1973, 1978, 1984, 2011 by Biblica, Inc.™\nUsed by permission. All rights reserved worldwide.")
        
## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_(""))


screen load():

    tag menu

    use file_slots(_(""))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Saves"), auto=_("Automatic saves"))
    add gui.game_menu_background
    use game_menu(title):
        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.32
                yalign -0.05
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign -0.7
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + i 

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%d %B - %H:%M"), empty=_("Empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                
                xalign 0.0
                yalign 1.0

                spacing gui.page_spacing

                if config.has_autosave:
                    textbutton _("  {#auto_page}Automatic ") action FilePage("auto")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 6):
                    textbutton "  [page]  " action FilePage(page)

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 40
    ypadding 0

style page_label_text:
    text_align 0.5
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")
    activate_sound "click.ogg" 
    hover_sound "hover.ogg"

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")
    activate_sound "click.ogg" 
    hover_sound "hover.ogg"

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu
    
    style_prefix "game_menu"

    add gui.game_menu_background
        
    use navimenu
    add "gui/overlay/prefs.png":
        ypos 0
        xpos 0
    
    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    vbox:
        hbox:
            box_wrap False

            if renpy.variant("pc"):

                vbox:
                    style_prefix "default"
                    spacing gui.navigation_spacing
                    label _("Window Size")
                    textbutton _("Windowed") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    ypos 100
                    xpos 360
            vbox:
                style_prefix "default"
                spacing gui.navigation_spacing
                label _("Skip")
                textbutton _("Unseen Text") action Preference("skip", "toggle")
                textbutton _("After Choices") action Preference("after choices", "toggle")
                ypos 100
                xpos 600
                
                    ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

        null height (5 * gui.pref_spacing)

        hbox:
            style_prefix "slider"
            box_wrap True

            vbox:

                label _("Text Speed")

                bar value Preference("text speed")

                label _("Auto-Forward Time")

                bar value Preference("auto-forward time")
                    
                xpos 360
                ypos 60
            vbox:

                if config.has_music:
                    label _("Music Volume")
                    hbox:
                        bar value Preference("music volume")

                if config.has_sound:

                    label _("Sounds Volume")

                    hbox:
                        bar value Preference("sound volume")
                label _("Voice Volume")

                hbox:
                    bar value Preference("voice volume")

                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing

                    textbutton _("Mute"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"
                        xpos -130
                        ypos -50
                xpos 320
                ypos 230               
       
    textbutton _("Return"): 
        yalign 0.998
        xalign 0.01
        activate_sound "back.ogg" 
        hover_sound "hover.ogg"
        action Return()

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    activate_sound "click.ogg" 
    hover_sound "hover.ogg"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    activate_sound "click.ogg" 
    hover_sound "hover.ogg"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10
    activate_sound "click.ogg" 
    hover_sound "hover.ogg"

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450
    
## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict True

    use game_menu(_(""), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_label_text

style history_text is default

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill False
    ysize gui.history_height

style history_name:
    xpos 0.2
    xanchor gui.history_name_xalign
    ypos 0
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos 0.25
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize 500
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
     

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("  Skipping ")

            text ". " at delayed_blink(0.0, 1.0)
            text ". " at delayed_blink(0.2, 1.0)
            text ". " at delayed_blink(0.4, 1.0)


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .1 alpha 1.0
        pause .1
        linear .1 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos 0
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)

style skip_text:
    size 55

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "Jellyka Delicious Cake.ttf"

## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    add "gui/bgnotify.png" at notify_appear
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.5 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .5 alpha 1.0
    on hide:
        linear 1.0 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")

screen patientsintro():
    modal True

    imagemap:
        ground "gui/patientsintro1.png"
        idle "gui/patientsintro1.png"
        hover "gui/patientsintro2.png"
        insensitive "gui/patientsintro3.png"

        hotspot (44,35,594,294) action [SensitiveIf(redintro == 0), Jump ("redintro"), Return()]
        hotspot (44,338,595,294) action [SensitiveIf(purpleintro == 0), Jump ("purpleintro"), Return()]
        hotspot (644,334,596,298) action [SensitiveIf(silverintro==0), Jump ("silverintro"), Return()]
        hotspot (644,35,588,298) action [SensitiveIf(blueintro==0), Jump ("blueintro"), Return()]
        
screen patients():
    modal True

    imagemap:
        ground "gui/patients1.png"
        idle "gui/patients1.png"
        hover "gui/patients2.png"
        insensitive "gui/patients3.png"

        hotspot (44,35,594,294) action [SensitiveIf(not firstpatient == "red" and not DevilFail), Jump ("red"), Return()]
        hotspot (44,338,595,294) action [SensitiveIf(not firstpatient == "purple"), Jump ("purple"), Return()]
        hotspot (644,334,596,298) action [SensitiveIf(not firstpatient == "silver"), Jump ("silver"), Return()]
        hotspot (644,35,588,298) action [SensitiveIf(not firstpatient == "blue"), Jump ("blue"), Return()]

screen difficulty():
    tag menu
    add "difficulty" at notify_appear
    hbox:
        textbutton _("{size=40}On"):
            activate_sound "click.ogg" 
            hover_sound "hover.ogg"
            action SetVariable("easymeter", True) 
            at notify_appear
            ypos 100
        textbutton _("{size=40}Off"):
            activate_sound "click.ogg" 
            hover_sound "hover.ogg"
            action SetVariable("easymeter", False) 
            at notify_appear
            ypos 100
            xpos 50
        xpos 0.25
        ypos 150
    hbox:
        textbutton _("{size=40}On"):
            activate_sound "click.ogg" 
            hover_sound "hover.ogg"
            action SetVariable("tutorials", True) 
            at notify_appear
            ypos 100
        textbutton _("{size=40}Off"):
            activate_sound "click.ogg" 
            hover_sound "hover.ogg"
            action SetVariable("tutorials", False) 
            at notify_appear
            ypos 100
            xpos 50
        xpos 0.25
        ypos 300
    hbox:
        textbutton _("Done"): 
            activate_sound "back.ogg" 
            hover_sound "hover.ogg"
            action Return()
        xpos 0.7
        ypos 0.8
        
screen tutorial():
    tag menu
    add "gui/tutorial/bg.png" at notify_appear
    hbox:
        textbutton _("{size=20}I understand"): 
            activate_sound "back.ogg" 
            hover_sound "hover.ogg"
            action Return()
        xpos 0.694
        ypos 0.8

screen tuto1():
    tag menu
    use tutorial
    add "gui/tutorial/choices.png" at notify_appear
screen tuto2():
    tag menu
    use tutorial
    add "gui/tutorial/coworkers.png" at notify_appear
screen tuto25():
    tag menu
    use tutorial
    add "gui/tutorial/journal.png" at notify_appear
screen tuto3():
    tag menu
    use tutorial
    add "gui/tutorial/sessions.png" at notify_appear
screen tuto4():
    tag menu
    use tutorial
    add "gui/tutorial/dreams.png" at notify_appear
screen tuto5():
    tag menu
    use tutorial
    add "gui/tutorial/tm1.png" at notify_appear
screen tuto6():
    tag menu
    use tutorial
    add "gui/tutorial/tm2.png" at notify_appear
screen tuto7():
    tag menu
    use tutorial
    add "tuto7" at notify_appear
image tuto7:
    "gui/tutorial/routes.png"
    pause 30
    "gui/tutorial/someoneelse.png"
    pause .5
    "gui/tutorial/routes.png"
    pause .2
    "gui/tutorial/someoneelse.png"
    pause .5
    "gui/tutorial/routes.png"
    pause 1.5
    "gui/tutorial/someoneelse.png"
    pause .5
    "gui/tutorial/veryveryangry.png"
    pause .3
    "gui/tutorial/routes.png"
    pause .2
    "gui/tutorial/routesfull.png"
    pause 1
    "gui/tutorial/routes.png"
    pause 10
    "gui/tutorial/routesfull.png"
screen tuto8():
    tag menu
    use tutorial
    add "gui/tutorial/side.png" at notify_appear
screen easymeter():
    add "gui/bar/easymeter.png" at notify_appear
  
screen empathymeter():
    hbox:
        bar value AnimatedValue(empathy, 11, 0.2)
        text _("Empathy\n{size=30}    [empathy]"):
            ypos 300 
            xpos -60            
        xpos 0.87
        ypos 100
        
screen greenmeter():    
    hbox:   
        bar value AnimatedValue(GreenHeart+9, 17, 0.2)
        text _("Points\n{size=30}   [GreenHeart]"):
            ypos 300 
            xpos -40            
        xpos 0.93
        ypos 100  
        
screen redmeter():    
    hbox:   
        bar value AnimatedValue(RedHeart, 24, 0.2)
        text _("Michael\n{size=30}[RedHeart]"):
            ypos 300  
            xpos -60
        xpos 0.87
        ypos 100
screen bluemeter():    
    hbox:   
        bar value AnimatedValue(BlueHeart, 32, 0.2)
        text _("Charlie\n{size=30}[BlueHeart]"):
            ypos 300  
            xpos -60
        xpos 0.87
        ypos 100
screen purplemeter():    
    hbox:   
        bar value AnimatedValue(PurpleHeart, 19, 0.2)
        text _("Tom\n{size=30}[PurpleHeart]"):
            ypos 300  
            xpos -60
        xpos 0.87
        ypos 100
screen silvermeter():    
    hbox:   
        bar value AnimatedValue(SilverHeart, 25, 0.2)
        text _("William\n{size=30}[SilverHeart]"):
            ypos 300  
            xpos -60
        xpos 0.87
        ypos 100
        
screen proper():
    hbox:
        bar value AnimatedValue(professional-personal+20, 40, 0.2)
        text _("professionalism\n{size=30}    [professional]\[personal]"):
            ypos 300 
            xpos -60            
        xpos 0.87
        ypos 100 
        
screen sanity():
    hbox:
        bar value AnimatedValue(sanity, 50, 0.2)
        text _("Sanity"):
            ypos 300 
            xpos -60            
        xpos 0.87
        ypos 100 
        
screen disorder():
    tag menu
    add "gui/tutorial/disbg.png" at notify_appear
    hbox:
        textbutton _("{size=20}I understand"): 
            activate_sound "back.ogg" 
            hover_sound "hover.ogg"
            action Return()
        xpos 0.694
        ypos 0.8

screen schizophrenia():
    tag menu
    use disorder
    add "gui/tutorial/schizo.png" at notify_appear
screen ocd():
    tag menu
    use disorder
    add "gui/tutorial/ocd.png" at notify_appear
screen gad():
    tag menu
    use disorder
    add "gui/tutorial/gad.png" at notify_appear
screen did():
    tag menu
    use disorder
    add "gui/tutorial/did.png" at notify_appear

screen indicator():
    tag menu
    add "gui/statistics.png" at notify_appear
    vbox:
        xpos 0.2
        ypos 0.35
        spacing 30
        hbox:
            text _("{color=#ffffff}{size=30}Empathy:  ")
            if he:
                text _("{size=30}You are {color=#ffffff}liked")
            elif le:
                text _("{size=30}You are {color=#ffffff}disliked")
            else:
                text _("{size=30}You are {color=#ffffff}somewhat liked")
        text _("{color=#ffffff}{size=30}Sanity:  ")
        vbar:
            value sanity
            range 50
            left_bar "gui/bar/timeright.png"
            right_bar "gui/bar/timeleft.png"
            xysize(600, 30)
    textbutton _("{size=40}Continue") action Return():
        xpos 0.8
        yalign 0.5
        
## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()

style window:
    variant "small"
    background "gui/phone/textbox.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
