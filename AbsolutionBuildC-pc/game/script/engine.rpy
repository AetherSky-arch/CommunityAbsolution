default day = 1
default month = 1
default route = "no"
default easymeter = True
default tutorials = True

default le = False
default he = False

image bmtitle:
    "gui/f/black.png" with dissolve
    pause 1
    "gui/bmain/title.png" with dissolve
    pause 1
image intro1 = "cg/intro1.png"
image intro2 = "cg/intro2.png"

##CALENDAR #####################################################################
image cal = "gui/day/bg.png"
image caw = "gui/day/wind.png"
image nov = "gui/day/nov.png"
image dec = "gui/day/dec.png"

image 1 = "gui/day/1.png"
image 2 = "gui/day/2.png"
image 3 = "gui/day/3.png"
image 4 = "gui/day/4.png"
image 5 = "gui/day/5.png"
image 6 = "gui/day/6.png"
image 7 = "gui/day/7.png"
image 8 = "gui/day/8.png"
image 9 = "gui/day/9.png"

image 12 = "gui/day/12.png"
image 22 = "gui/day/22.png"
image 32 = "gui/day/32.png"
image 42 = "gui/day/42.png"
image 52 = "gui/day/52.png"
image 62 = "gui/day/62.png"
image 72 = "gui/day/72.png"
image 82 = "gui/day/82.png"
image 92 = "gui/day/92.png"
image 0 = "gui/day/0.png"

image w1 = "gui/day/w1.png"
image w2 = "gui/day/w2.png"
image w3 = "gui/day/w3.png"
image w4 = "gui/day/w4.png"
image w5 = "gui/day/w5.png"
image w6 = "gui/day/w6.png"

image mon = "gui/day/mon.png"
image tu = "gui/day/tu.png"
image wed = "gui/day/wed.png"
image th = "gui/day/th.png"
image fri = "gui/day/fri.png"
image sat = "gui/day/sat.png"
image sun = "gui/day/sun.png"

image first = "gui/day/first.png"

### THE CALENDAR #####################################
######################################################
label calendar:
    stop music fadeout 2
    scene black
    scene cal with dissolve
## Months ############################################
    if month == 1:
        show nov with dissolve
    else:
        show dec with dissolve 
## A WILD WINDOW APPEARS #############################
    ## whoosh
    show caw with moveinright
## Days (dzięsiątki i mniejsze od 10) ################
    play sound "cal3.ogg" fadein 1
    if day == 1:
        show 1:
            xpos 0.025
        with dissolve
    elif day > 9 and day < 20:
        show 1 with dissolve
    elif day == 2:
        show 2:
            xpos 0.025
        with dissolve
    elif day > 19 and day < 30:
        show 2 with dissolve
    elif day == 3:
        show 3:
            xpos 0.025
        with dissolve
    elif day > 29:
        show 3 with dissolve
    elif day == 4:
        show 4:
            xpos 0.025
        with dissolve
    elif day == 5:
        show 5:
            xpos 0.025
        with dissolve
    elif day == 6:
        show 6:
            xpos 0.025
        with dissolve
    elif day == 7:
        show 7:
            xpos 0.025
        with dissolve
    elif day == 8:
        show 8:
            xpos 0.025
        with dissolve
    elif day == 9:
        show 9:
            xpos 0.025
        with dissolve
## Days (jedności) ################################### 
    if day == 10 or day == 20 or day == 30:
        show 0 with dissolve
    elif day == 11 or day == 21:
        show 12 with dissolve
    elif day == 12 or day == 22:
        show 22 with dissolve
    elif day == 13 or day == 23:
        show 32 with dissolve
    elif day == 14 or day == 24:
        show 42 with dissolve
    elif day == 15 or day == 25:
        show 52 with dissolve
    elif day == 16 or day == 26:
        show 62 with dissolve
    elif day == 17 or day == 27:
        show 72 with dissolve
    elif day == 18 or day == 28:
        show 82 with dissolve
    elif day == 19 or day == 29:
        show 92 with dissolve

## Weeks #############################################       
    if month == 1:
        if day < 8:
            show w1 with dissolve
        elif day > 7 and day < 15:
            show w2 with dissolve
        elif day > 14 and day < 22:
            show w3 with dissolve
        elif day > 21 and day < 29:
            show w4 with dissolve
        else:
            show w5 with dissolve 
    else:
        if day < 6:
            show w5 with dissolve
        else:
            show w6 with dissolve
## Days of week ######################################
    if day == 1 or day == 8 or day == 15 or day == 22 or day == 29:
        if month == 1:
            show mon with dissolve
        else:
            show wed with dissolve
    elif day == 2 or day == 9 or day == 16 or day == 23 or day == 30:
        if month == 1:
            show tu with dissolve
        else:
            show th with dissolve
    elif day == 3 or day == 10 or day == 17 or day == 24:
        if month == 1:
            show wed with dissolve
        else:
            show fri with dissolve
    elif day == 4 or day == 11 or day == 18 or day == 25:
        if month == 1:
            show th with dissolve
        else:
            show sat with dissolve  
    elif day == 5 or day == 12 or day == 19 or day == 26:
        if month == 1:
            show fri with dissolve
        else:
            show sun with dissolve
    elif day == 6 or day == 13 or day == 20 or day == 27:
        if month == 1:
            show sat with dissolve
        else:
            show mon with dissolve
    else:
        if month == 1:
            show sun with dissolve
        else:
            show tu with dissolve
    $ renpy.pause(1, hard=True)
    if month==1:
        if day>7:
            if day>14:
                if day>28 and empathy>24:
                    $le=False
                    $he=True
                elif empathy>11:
                    $le=False
                    $he=True
            elif empathy>9:
                $le=False
                $he=True
        elif empathy>5:
            $le=False
            $he=True
    else:
        if day>5 and empathy>39:
            $le=False
            $he=False
        elif empathy>24:
            $le=False
            $he=True
    if day>8 and month>1:
        if empathy<4:
            $he=False
            $le=True
    elif empathy<5:
        $he=False
        $le=True
    if sanity<5:
        $renpy.pause()
        play sound "page.ogg" fadein 1
        show nosanity with dissolve
        $renpy.pause()
        return
    if easymeter and day is not {6,7,13,14,20,21}:
        call screen indicator
    scene black with dissolve
    $firstpatient = "no"
    $sessions = 0
    if month == 1 and day < 9:
        if day == 1:
            jump dayone
        elif day == 2:
            jump daytwo
        elif day == 5:
            jump dayfivelate
        elif day==6:
            jump momcall
        elif day==7:
            jump sundayweekone
        elif day==8:
            if SunLink>0:
                jump suemonday
            else:
                "It's my second week of work at the hospital. Let's get to work."
        else:
            jump patientchoice
    if month==1 and ((route=="red" and day==11) or (route=="blue" and day==9) or (route=="purple" and day==9) or (route=="silver" and day==10)):
        jump afterjanereveal
    if route=="red":
        jump rednav
    elif route=="blue":
        jump bluenav
    elif route=="purple":
        jump purplenav
    elif route=="silver":
        jump silvernav
    else:
        jump patientchoice
        
## LOOPING AND ADDING THE NEXT DAY ###################
label nextday:
    if day == 30:
        $day = 1
        $month = 2
        jump calendar
    else:
        $day += 1
        jump calendar
label start:
    scene black with dissolve
    nt "CONTENT WARNINGS"
    nt "This game contains:\nmental illness, blood and gore, suicide, murder, self-harm, sadism, masochism, sexual themes, rape, domestic abuse, jumpscares, and strong language."
    nt "While playing this game, you will be exposed to content sensitive readers may find disturbing."
    nt "Are you sure you want to begin?"
    menu:
        "Yes":
            nt "Enjoy the game."
        "No":
            return
    stop music fadeout 3
    pause 1
    show tw1 with dissolve
    $renpy.pause()
    show tw2 with dissolve
    $renpy.pause()
    show tw3 with dissolve
    $renpy.pause()
    show tw4 with dissolve
    $renpy.pause()
    show tw5 with dissolve
    $renpy.pause()
    scene black with dissolve
    call screen difficulty
    play music "ost/dream.wav" fadein 5
    scene intro1 with Dissolve(1.0)
    nt "...."
    scene intro2 with Dissolve(0.8)
    nt "A mental hospital..?"
    nt "You never cease to surprise me."
    nt "I wonder what this new path will lead you to..."
    nt "Happiness? Fulfillment?"
    nt "This is what you seek, isn't it?"
    nt "Or maybe..."
    nt "To death and suffering?"
    nt "The choice is yours."
    stop music fadeout 4
    nt "See you soon ~"
    pause 1
    scene black with Dissolve(1.0)
    scene first with dissolve
    pause 2
    jump tour

label afterwork:
    scene black with dissolve
    "My work for today is over."
    $social = renpy.random.randint(1, 5)
    if social == 5:  
        scene bg frontsun with Dissolve(1)
        if SunLink>4:
            "I spot Sue by the exit and stop to chat."
            "Turns out she's staying here for the night, so we end up talking for a while before I leave the hospital."
        elif SunLink>0:
            "I pass by Sue on my way outside. She seems to be going the opposite way, though."
        else:
            "I make my way outside and go home."
    elif social==4: 
        if TempLink>4: 
            scene bg frontsun with Dissolve(1)
            "I make my way outside and head home, but I notice Julia going the same way."
            "We end up talking for a while until I reach my house."
        elif TempLink>1: 
            scene bg frontsun with Dissolve(1)
            "I pass by Julia in the reception before leaving. She smiles at me."
            "I make my way outside and go home as usual."
        elif SunLink>4:
            play music "rain.mp3" fadein 3
            scene bg rain with Dissolve(1)
            "It's raining... I spot Sue on her way out with an umbrella in her hand."
            "She follows me all the way to my house to protect me from the rain."
            "Thanks, Sue."
        else:
            scene bg frontsun with Dissolve(1)
            "I make my way outside and go home."
    elif social==3: 
        scene bg sunset with Dissolve(1)
        if StarLink>4:
            "I notice Dr. Young in the reception. He offers to walk me home."
            "We chat for a while."
        elif StarLink>0:
            "I pass by Dr. Young in the cafeteria, but he seems busy."
            "I make my way outside and go home as usual."
        else:
            "I make my way outside and go home."
    else:
        scene bg frontsun with Dissolve(1)
        "I make my way outside and go home."
    pause 0.5
    if route == "silver":
        if month==1:
            if day == 9:
                jump janeroute
            elif day == 11 and Moonship:
                jump moonrise
    elif route == "purple":
        if month==1:
            if day == 8:
                jump janeroute
            if day == 11:
                jump entrance
            if day == 17 and HangedShip:
                jump dungeon
    elif route == "red":
        if day == 10:
            jump janeroute
        elif day == 12 and DevilFreed:
            jump skycollapse
        elif day == 15 and DevilShip and RedHeart>=15:
            jump ladyinsun
    elif route== "blue":
        if day == 8:
            jump janeroute
        elif day == 10:
            jump darkforest
        elif day==12:
            jump alicehylophobia
    jump nextday
label breakchoice:
    pass
label breakreal:
    stop music fadeout 3
    scene desk with dissolve
    "What should I do on my break?"
    if day == 2 and month == 1 and tutorials:
        call screen tuto6
    menu:
        "Spend time with someone in the hospital":
            $empathy+=1
            if SunLink > 0 or TempLink > 0 or StarLink > 0:
                jump links
            elif month == 1 and day < 6 and PrsLink > 0:
                jump links
            else:
                "I don't know anyone here... I can try to explore the hospital instead."
                jump breakchoice
        "Explore the hospital":
            scene black with dissolve
            jump exploration
        "Stay in my office" if month==1 or day<5:
            "...."
            "I spent the break resting in my office."
            if sanity < 40:
                $sanity += 10
                "I feel more relaxed than before."
            elif sanity > 40 and sanity < 50:
                $sanity = 50
                "I feel more relaxed than before."
            jump patientchoice

label redsession:
    scene bg mcdesk with dissolve
    "I spent another session with Michael."
    $mood = renpy.random.randint(1, 4)
    if mood==1:
        show dv neu with dissolve
        "Not much happened today, but I think we're making progress."
    elif mood==2:
        show dv smile with dissolve
        "He seemed a lot happier than usual today. I'm glad he feels comfortable around me."
    elif mood==3:
        show dv sad with dissolve
        "He seemed a lot less cheerful than usual... I'm not sure what happened."
    else:
        show dv noeyes with dissolve
        "He... seemed a bit... agitated today. Like he wanted to hurt me."
        "I can't let it discourage me. I'm safe."
    if sessions == 0:
        $firstpatient = "red"
    $redinteract += 1
    $sessions += 1
    jump breaknav
label bluesession:
    scene bg mcdesk with dissolve
    "I spent another session with Charlie."
    $mood = renpy.random.randint(1, 4)
    if mood==1:
        show h neu with dissolve
        "Not much happened today, but I think we're making progress."
    elif mood==2:
        show h cute with dissolve
        "He seemed more cheerful than usual today... it's always a good sign."
    elif mood==3:
        show h sad with dissolve
        "Surprisingly, he seemed somewhat melancholic today."
    else:
        show h siden with dissolve
        "He wasn't very... responsive today. I have to keep trying."
    if sessions == 0:
        $firstpatient = "blue"
    $blueinteract += 1
    $sessions += 1
    jump breaknav
label purplesession:
    scene bg mcdesk with dissolve
    "I spent another session with Tom."
    $mood = renpy.random.randint(1, 4)
    if mood==1:
        show t neutral with dissolve
        "Not much happened today, but I think we're making progress."
    elif mood==2:
        show t smile with dissolve
        "He opened up to me today... I really think I can help him."
    elif mood==3:
        show t sad with dissolve
        "He... wasn't very talkative today. I tell myself I've done all I could."
    else:
        show t frust with dissolve
        "He... got angry with me today, but I'll keep doing my best."
    if sessions == 0:
        $firstpatient = "purple"
    $purpleinteract += 1
    $sessions += 1
    jump breaknav
label silversession:
    scene bg mcdesk with dissolve
    "I spent another session with William."
    $mood = renpy.random.randint(1, 4)
    if mood==1:
        show w neutral with dissolve
        "Not much happened today, but I think we're making progress."
    elif mood==2:
        show w smile with dissolve
        "He opened up to me today... I really think I can help him."
    elif mood==3:
        show w regret with dissolve
        "He... seemed down today. I'm not sure if it was my fault."
    else:
        show w angry with dissolve
        "Things got a little out of hand today, but I can handle it."
    if sessions == 0:
        $firstpatient = "silver"
    $silverinteract += 1
    $sessions += 1
    if route == "no" and day == 16 and sessions == 1:
        jump patientsattack
    jump breaknav

label breaknav:
    if month==1:
        if day == 1:
            if sessions == 1:
                jump aftersessiononefirstday
            elif sessions == 2:
                jump firstdaybreak
            elif sessions == 3:
                jump afterworkfirstday
            else:
                jump dayoneafterwork
        elif day == 2:
            if sessions == 1:
                jump goldenintroduction
            else:
                jump daytwoafterwork
        elif day == 5 and sessions == 2:
            jump fridayjudgement
    if sessions == 1:
        jump breakchoice
    else:
        if route == "silver":
            if day == 10:
                jump hierweek2
            elif day == 12 and ShadowTalk:
                jump moonaftertalk
            elif day == 15 and ShadowTalk:
                jump shadowaftertalk
            elif day==29:
                jump waftermonday
        if route == "blue":
            if day == 10:
                jump charliestar
            elif day == 11 and HermitFail==False:
                jump hierweek2
            elif day == 12:
                jump blueafterkiss
        elif route == "red":
            if day == 10:
                jump hierweek2
        elif route == "purple":
            if day == 10:
                jump hierweek2 
        jump afterwork

label before_main_menu:
    image beforemm = "gui/overlay/main_menu.png"
    image logo = "gui/logo.png"
    scene black 
    pause 1
    show logo with Dissolve(1.0)
    $renpy.pause(2, hard=True)
    scene black with dissolve
    show bmshow
    pause 0.2
    show bmtitle
    $renpy.pause()
    hide bmtitle with dissolve
    hide logo with dissolve
    show beforemm with dissolve
    show screen main_menu
