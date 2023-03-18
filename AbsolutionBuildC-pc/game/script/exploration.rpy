default explor0 = False
default explor1 = False
default explor2 = False
default explor3 = False
default explor4 = False
default explor5 = False
default explor6 = False
default explor7 = False
default explor8 = False
default explor9 = False
default explor10 = False
default explor11 = False
default explor12 = False
default explor13 = False
default explor14 = False
default explor15 = False
default explor16 = False
default explor17 = False
default explor18 = False
default explor19 = False
default explor20 = False
default explor21 = False
default explor22 = False
default explor23 = False
default explor24 = False
default explor25 = False
default explor26 = False
default explor27 = False
default explor28 = False
default explor29 = False
default explor30 = False
default explor31 = False
    
define nra = Character("Chatty nurse", color='#ffffff')
define nrb = Character("Younger nurse", color='#ffffff')

image bg wheelstart = "gui/wheel/start.png"
image moondevil = "cg/MoonDevil.png"

label exploration:
    if explor0:
        $explore = renpy.random.randint(1, 60)
        if explore == 1 or explore == 2:
            if explor1:
                jump exploration
            else:
                jump explor1
        if explore == 3 or explore == 4:
            if explor2:
                jump exploration
            else:
                jump explor2
        if explore == 5 or explore == 6:
            if explor1:
                jump exploration
            else:
                jump explor3
        if explore == 7 or explore == 8:
            if explor4:
                jump exploration
            else:
                jump explor4
        if explore == 9 or explore == 10:
            if explor5:
                jump exploration
            else:
                jump explor5
        elif explore == 11 or explore == 12:
            if explor6:
                jump exploration
            else:
                jump explor6
        if explore == 13 or explore == 14:
            if explor7:
                jump exploration
            else:
                jump explor7
        elif explore == 15 or explore == 16:
            if explor8:
                jump exploration
            else:
                jump explor8
        if explore == 17 or explore == 18:
            if explor9:
                jump exploration
            else:
                jump explor9
        if explore == 19 or explore == 20:
            if explor10:
                jump exploration
            else:
                jump explor10
        if explore == 21 or explore == 22:
            if explor11:
                jump exploration
            else:
                jump explor11
        if explore == 23 or explore == 24:
            if explor12:
                jump exploration
            else:
                jump explor12
        elif explore == 25 or explore == 26 or explore == 27 or explore == 28:
            if explor13:
                jump exploration
            else:
                jump explor13
        elif explore == 29:
            if explor14:
                jump exploration
            else:
                jump explor14
        elif explore == 30 or explore == 31:
            if explor15:
                jump exploration
            else:
                jump explor15
        elif explore == 32 or explore == 33:
            if explor16:
                jump exploration
            else:
                jump explor16
        if explore == 34 or explore == 35:
            if explor17:
                jump exploration
            else:
                jump explor17
        if explore == 36 or explore == 37:
            if explor18:
                jump exploration
            else:
                jump explor18
        if explore == 38 or explore == 39:
            if explor19:
                jump exploration
            else:
                jump explor19
        if explore == 40 or explore == 41:
            if explor20:
                jump exploration
            else:
                jump explor20
        if explore > 41 and explore < 48:
            if explor21 or explor22 or explor23:
                jump exploration
            else:
                jump explor21
        elif explore > 47 and explore < 52:
            if explor24 or explor25 or month==2:
                jump exploration
            else:
                jump explor22
        elif explore == 52 or explore == 53:
            if explor29:
                jump exploration
            else:
                jump explor24
        elif explore == 54 or explore == 55:
            if explor29:
                jump exploration
            else:
                jump explor25
        elif explore == 56 or explore == 57:
            if explor29:
                jump exploration
            else:
                jump explor26
        elif explore == 58 or explore == 59:
            if explor29:
                jump exploration
            else:
                jump explor23
        elif explore == 60:
            if persistent.WheelCard:
                jump exploration
            else:
                jump explor27
        else:
            jump exploration
    else:
        $explor0 = True
        jump explor0
label explor0:
    play music "ost/hospital.wav" fadein 5
    scene bg offices with dissolve
    "I've decided to take a walk around the hospital during my break."
    scene bg central with dissolve
    "I'm not really sure where I want to go, so I just end up in the central hall."
    "Looking to my left, I notice something hanging on the wall."
    menu:
        "Check the wall":
            "Oh?"
    show map with dissolve
    $renpy.pause()
    show map 2 with dissolve
    "It's a {color=#f46666}map of the hospital{/color}. I can see all of the floors here..."
    "I examine it closely..."
    "All stairs and exits are marked here."
    "This map could come in handy sometime..."
    "I take a moment to memorize it in case I ever get lost."
    hide map with dissolve
    play sound "chars.ogg" 
    show screen notify("{size=24} Your Location Info screen has been updated!")
    stop music fadeout 3
    scene bg patients with dissolve
    "I wander around the second floor during the rest of my break."
    jump patientchoice
label explor1:
    if route=="no":
        jump exploration
    $explor1=True
    scene bg offices with dissolve
    play music "ost/emo.wav" fadein 6
    if route == "red" or route == "silver" or route=="green":
        show h full with dissolve
        "I notice Charlie in the hallway outside of my office."
        if firstpatient=="blue":
            "He must have taken his time leaving after our session."
            m conf "Hello, Charlie."
            h "[name]? Hi again~"
        else:
            "Maybe he wants to talk to me about something..."
            m conf "Hello, Charlie."
            h "[name]? It's good to see you ~"
        h "I'm waiting for my psychiatrist."
        "Oh."
        m gasp "Ah, okay."
        m talk "What a-{w} Oh?"
        play sound "doorclose.ogg" fadein 1
        show e neu:
            xpos -0.5
        with moveinright
        "Elizabeth walks out of the office labelled \"VII\"."
        show e baka with dissolve
        e "You.{w} Move."
        "Charlie looks at her, confused."
        m trigger "Um, Charlie?"
        h "Do I know you..?"
        show e angry with dissolve
        "He's staring at Elizabeth with wide eyes."
        show e angrytalk with dissolve
        e "Ugh, whatever."
        show e foc with dissolve
        play sound "doorclose.ogg" fadein 1
        hide e with moveoutright
        "She pushes Charlie out of the way and leaves."
        stop music fadeout 5
        h "...."
        m serious "Charlie? Are you okay?"
        h "I... am."
        m sadsmile "Don't worry about Elizabeth, she's just... like that."
        h "I see."
        "He's acting kind of strange, but I can't put my finger on it."
        "Well, I suppose I should leave him be."
        scene black with dissolve
        "I say goodbye to Charlie and spend the rest of my break in the central hall."
    else:
        show w full with dissolve
        "I notice William in the hallway outside of my office."
        "Before I can approach him, the door to Dr. Sharpe's office opens..."
        play music "ost/tension.ogg" fadein 6
        show moondevil with Dissolve(1.0)
        $renpy.pause()
        w "...Burnett."
        dv "Moore. How unexpected."
        w "I'm not in the mood for this."
        "He glances at the hallway as if searching for escape routes."
        dv "You aren't? And yet you're here early again, knowing that you're right after me."
        w "That doesn't mean anything. You're delusional."
        dv "It's almost as if you {i}wanted{/i} to run into me."
        w "You know I didn't."
        dv "...."
        "He takes a step closer."
        w "{i}...?"
        dv "Hmmm..."
        w "What are you... doing?"
        dv "Nothing.{w} Is there anything you would want me to be doing?"
        "William's eyes go wide."
        w "I-{w} No! You're insane."
        "He takes a step back."
        dv "We've been here together for two years now and I have yet to see you willing to talk."
        w "It's because I don't want to."
        dv "I see how it is. {w}I get it."
        "A strange smile flashes through Michael's face before his neutral expression returns."
        dv "Well..."
        hide moondevil with dissolve
        "He approaches William and passes by him on his way to the central hall."
        dv "I always thought we had a lot in common."
        stop music fadeout 4
        hide dv with moveoutright
        w "{i}I -"
        play sound "doorclose.ogg" fadein 1
        "He's gone."
        "William leans against the wall, clearly uncomfortable. {w}I decide to approach him."
        m neu "Hi."
        w "Dr. Hart-? I didn't see you before."
        if le:
            "He glances around the hallway."
            w "Umm... I should go."
            play sound "doorclose.ogg" fadein 1
            hide w with moveoutleft
            "He enters Dr. Sharpe's office without another word."
        else:
            w "I'm sorry you had to see that."
            m flirt "There's nothing to be sorry for."
            "He bores his eyes into the floor with an intense expression."
            play music "ost/emo.wav" fadein 5
            w "I hate it when he does that."
            w "Haven't I made it clear that I {i}don't{/i} want to talk to him?"
            m neu "Well..."
            w "What?"
            "I shrug."
            m fabtalk "Do you have anyone to talk to?"
            w "What are you saying? He's unhinged and creepy."
            w "Besides, I'd rather not talk to {i}anyone{/i} in this place. It drains my sanity."
            play sound "doorclose.ogg" fadein 1
            "The door to Dr. Sharpe's office opens once more."
            show d smirk:
                xpos -0.5
            with moveinleft
            d "Ms. Hart, are you by any chance stealing my patients from me?"
            show d neu with dissolve
            m conf "I'm not. I was just about to leave."
            show d calmsmile with dissolve
            d "Very well."
            hide d with dissolve
            hide w with dissolve
            "He invites William into his office and they both disappear behind the closed door."
        scene black with dissolve
        "That was... certainly interesting."
    jump patientchoice
label explor2:
    $explor2=True
    if TempLink>4:
        jump exploration
    else:
        pass
    scene bg central with dissolve
    "I overhear a conversation."
    show jl calm:
        xpos -0.2
    with dissolve
    play sound "doorclose.ogg" fadein 1
    show su neu:
        xpos 0.2
    with dissolve
    show su gasp with dissolve
    sue "Oh, sorry, I didn't see you there."
    show jl neu with dissolve
    jl "...."
    show su sadtalk with dissolve
    sue "Julia? Is everything okay?"
    show su neutral with dissolve
    show jl gasp with dissolve
    jl "Huh?"
    show jl calmtalk with dissolve
    jl "Oh, yeah, yeah I'm fine."
    show jl calm with dissolve
    show su sad with dissolve
    sue "You look pale."
    show jl talk with dissolve
    jl "You know, I was just... taking over for Lisa."
    show jl neu with dissolve
    show su talk with dissolve
    sue "Again?"
    show su neu with dissolve
    show jl calm with dissolve
    jl "She's sick. Apparently."
    show su angry with dissolve
    sue "I feel like she's always sick..."
    show jl angry with dissolve
    jl "It happens."
    show su smile with dissolve
    show jl neu with dissolve
    sue "Come on, let me take that shift. You should get a break."
    show jl gasp with dissolve
    jl "I mean..."
    show su laugh with dissolve
    sue "Don't go there. I've had enough breaks already."
    show su cute with dissolve
    show jl calm with dissolve
    "She points to the door of the nurses' office."
    show su neu with dissolve
    sue "In you go. Get some rest."
    jl "...."
    hide jl with dissolve
    "Reluctantly, Julia disappears in the nurses' office."
    "She really seemed tired."
    jump patientchoice
label explor3:
    if route == "blue":
        jump exploration
    else:
        $explor3=True
        scene bg offices with dissolve
        "I leave my office to take a walk, but suddenly hear voices coming from one of the offices."
        play music "ost/sunny.wav" fadein 10
        h "So..."
        h "I won't need this anymore?"
        s "Not quite. But the dose should be reduced."
        h "But... that's a good sign, right?"
        s "Of course it is. It means we're making progress."
        if he:
            h "It must be because of my psychologist. She's working really hard to help me ~"
            s "Is that so? I'm glad to hear that."
        else:
            h "Oh, and I have a new psychologist. Maybe she helped?"
        s "She's new here, isn't she?"
        h "I think so."
        s "You haven't had much luck when it comes to psychologists so far, I admit..."
        if he:
            s "I'm glad you finally came across one who understands you."
            s "I really hope she can help you."
        else:
            s "I hope this one will be different."
        h "...it looks like we're running out of time for today."
        h "Goodbye ~"
        s "Goodbye, Charlie. I'll see you soon."
        show h full with dissolve
        "Charlie leaves his psychiatrist's office and waves at me."
        h "Hi ~"
        m flirt "Hello, Charlie."
        if he:
            h "I was just talking to my psychiatrist about how great you are ~"
            m neu "I heard that."
            h "I think you two would get along. He's very nice to me as well."
            m cute "I imagine."
            "I spend the rest of my break chatting with Charlie."
        else:
            h "Did you... want to talk to me about something?"
            m uncom "Um, no. I was just -"
            h "Okay! I'll be on my way, then ~"
            hide h with moveoutright
            "Charlie disappears in the central hall. He seemed to be in a hurry..."
        jump patientchoice
label explor4:
    $explor4 = True
    play music "ost/hospital.wav" fadein 5
    scene bg offices with dissolve
    show d neutral with dissolve
    "I leave my office and instantly notice Dr. Sharpe outside of his."
    show d neu with dissolve
    "He turns to me quickly when I approach him."
    show d talk with dissolve
    d "Ms. Hart? Were you going somewhere?"
    show d neu with dissolve
    m fabtalk "No, I was only taking a walk through the hospital using my scheduled break."
    "I make a mental note to remind him that I have every right to be here."
    show d sidetalk with dissolve
    d "I see..."
    if he:
        show d calmtalk with dissolve
        d "Well, I have matters to attend to elsewhere."
        show d smirk with dissolve
        d "I wish you a pleasant break."
        show d neu with dissolve
    else:
        show d coldtalk with dissolve
        d "Unlike you, I have matters to attend to now."
        show d cold with dissolve
    d "If you'll excuse me..."
    m gasp "Of course."
    stop music fadeout 3
    hide d with dissolve
    "He leaves in a hurry."
    show bg central with dissolve
    "Deciding not to bother him at this point, I turn the other way and spend the rest of my break in the central hall."
    jump patientchoice
label explor5:
    if route == "no" or route=="silver":
        jump exploration
    else:
        $explor5=True
        scene bg offices with dissolve
        "I leave my hospital to take a walk, but suddenly hear voices coming from one of the offices."
        d "So... the new dose still wasn't enough?"
        w "...not really."
        play music "ost/tension.ogg" fadein 8
        w "It's only been getting worse these past few months."
        d "...."
        d "It... may be too much to increase it again. Especially for you, William."
        w "So what should be done instead?"
        d "I have been considering going back to antidepressants."
        w "What -?"
        d "A month has passed and there have been no improvements at all."
        d "It might be harmful to continue this way, given how you seem to be developing a tolerance of sorts."
        w "You can't... do this to me now..."
        d "It is the only way."
        w "I... {i}I need it."
        w "It got better a month ago..."
        d "Until it only started escalating again."
        d "You have to trust me with this, William. I am doing all I can to help you."
        w "But it's not working... {i}Nothing's working!"
        d "It would only get worse after an overdose."
        w "...."
        w "I can... still take more. {i}I need more, dammit!"
        d "...."
        d "Your safety is still my priority."
        stop music fadeout 6
        d "Now... if you don't mind - you are invading my personal space."
        w "...."
        w "I'm sorry -!"
        play music "ost/hospital.wav" fadein 8
        w "I... I don't know what came over me."
        d "Back to antidepressants. Definitely."
        w "And... it won't get worse?"
        d "It might at first."
        w "...."
        d "There is nothing to worry about. It will pass."
        w "If you say so... I won't argue with that."
        d "It would be unwise."
        d "Medication is not something to be used recklessly."
        w "I understand."
        d "I should not keep you here any longer. You may leave."
        w "Goodbye, Dr. Sharpe."
        d "Goodbye, William."
        "I get back to my office once the voices go silent."
        jump patientchoice
label explor6:
    if route == "silver":
        jump exploration
    else:
        $explor6=True
        scene bg patients with dissolve
        "I'm walking through the patients' rooms hallway."
        scene bg patients with hpunch
        play music "ost/tension.ogg" fadein 5
        "What?"
        "I hear a muffled cry coming from one of the rooms."
        "Instantly, I turn my head to see the source of the sound - room number XIX."
        "Walking up to the door slowly, I hear William's voice."
        show bg closeXIX with dissolve
        w "{i}No..."
        w "{i}Not again..."
        "It sounds like he's in pain."
        "He still hasn't noticed me..."
        "I'm not sure if it would do him any good for me to interfere now."
        "But I would feel bad about leaving him like this..."
        menu:
            "Say something":
                $empathy += 2
                "I carefully approach the door."
                m serious "William? Are you okay?"
                "His head snaps in my direction."
                w "What are you doing here?"
                m uncom "I was just passing by and I heard your voice - I wanted to make sure everything is fine."
                if le:
                    "He looks at me with a somewhat surprised expression, but quickly regains his composure."
                    w "I didn't ask for your help. Go away."
                else:
                    w "...Oh."
                    w "You should leave... {color=#fff1c1}I'm alright."
                    m serious "Are you sure...?"
                    "His expression is tense."
                    w "{b}Yes. I am."
                stop music fadeout 3
                "I guess I have no choice but to leave him be now..."
                show bg patients with dissolve
                "I nod and head back to my office."
            "Stay silent":
                "I decide it's best not to make my presence known."
                stop music fadeout 3
                "I don't think he would be willing to talk to me in his current state anyway..."
                w "...."
                show bg patients with dissolve
                "I should leave him be."
        jump patientchoice
label explor7:
    if route == "blue":
        jump exploration
    $explor7=True
    scene bg central with dissolve
    play music "ost/sunny.wav" fadein 10
    "I'm passing through the central hall, but stop at a curious sight."
    show su cute:
        xpos -0.1    
    with dissolve
    show h full:
        xpos 0.1
    with dissolve
    h "Thanks for agreeing to hang out with me, Sue ~"
    show su happy with dissolve
    sue "No problem. I had a free break anyway."
    show su smile with dissolve
    h "...."
    show su gasp with dissolve
    sue "...What did you want to talk about?"
    show su smile with dissolve
    h "I don't know..."
    show su gasp with dissolve
    sue "I have an idea."
    h "...?"
    show su cute with dissolve
    sue "I'm thinking about someone from the hospital. You have to guess who it is."
    show su smile with dissolve
    h "Ooh, I love games ~"
    h "Are they a staff member or a patient?"
    show su talk with dissolve
    sue "I can only say yes or no, it would be too easy otherwise."
    show su neu with dissolve
    h "Right, right..."
    h "Do I know them?"
    show su cute with dissolve
    sue "Yes."
    show su smile with dissolve
    h "Are they older than me?"
    show su talk with dissolve
    sue "Umm... I think so."
    h "...Are they taller than me?"
    show su laugh with dissolve
    "She giggles."
    show su smile with dissolve
    sue "No, definitely not."
    h "Is it a girl?"
    show su neu with dissolve
    sue "It is."
    h "Does she live in any of the rooms in that hallway?"
    show su talk with dissolve
    sue "No."
    show su neu with dissolve
    h "...."
    show su smile with dissolve
    h "...Does she have long, black hair?"
    show su neutral with dissolve
    sue "...?"
    show su gasp with dissolve
    sue "No, there's nobody like that here."
    show su happy with dissolve
    h "...oh."
    show su smile with dissolve
    h "I thought so."
    h "Is she a staff member?"
    show su cute with dissolve
    sue "Yes, she is."
    h "So... it's a girl, older than me, who works here..."
    show su smile with dissolve
    h "Is it Julia?"
    show su gasp with dissolve
    sue "No, keep asking questions until you're sure."
    show su neu with dissolve
    h "...."
    h "Oh! I know~!"
    show su smile with dissolve
    h "Are they a psychologist?"
    show su cute with dissolve
    sue "Yes ~"
    show su smile with dissolve
    h "You're thinking about [name]! My psychologist!"
    if le:
        "I approach them."
        m talk "I heard you two talking about me behind my back."
        show su talk with dissolve
        sue "Umm... yeah.{w} We were talking about you."
        show su neu with dissolve
        sue "Is that a problem?"
        show su angry with dissolve
        m neu "No. Carry on."
        "Things got kind of awkward, so I decide to leave them be."
    else:
        "I approach them with a smile."
        show su gasp with dissolve
        m cute "I heard you two talking about me behind my back."
        show su cute with dissolve
        sue "Speak of the devil... You sure are sneaky."
        show su smile with dissolve
        h "[name] ~!"
        "I spend the rest of my break chatting with the two."
        "They're both really nice."
    jump patientchoice
label explor8:
    $explor8 = True
    scene bg patients with dissolve
    play music "ost/hospital.wav" fadein 5
    "I'm walking through the patients' rooms hallway."
    "I can hear voices from a distance."
    dv "Hey, do you mind stopping by for a bit?"
    gu "-huh?"
    dv "Yeah, you. Sue, right?"
    "The nurse I recognize, Sue, walks over to the door of Michael's room."
    "She doesn't look very happy to be that close to him, and, honestly, I can't blame her."
    sue "Is there... anything I can help you with?"
    dv "Uhh... aside of the obvious, not really."
    sue "{i}\"The obvious\"{/i} being...?"
    dv "Opening the door, of course~"
    sue "No."
    "Sue hesitates, clearly not liking the harshness of her tone."
    sue "I-I mean... you're..."
    dv "Yeah, yeah, I get it - I'm not allowed out of this room with my hands free."
    sue "...Right."
    "I can tell the topic is uncomfortable for the staff here."
    dv "You're acting like it's your fault."
    sue "I-"
    dv "Well, since that's not happening anytime soon..."
    dv "I just wanted to talk."
    sue "Oh..."
    pt "Don't you have anything better to do than flirting with nurses?"
    "Michael seems moderately insulted by that."
    dv "Just so you know - I really don't!"
    dv "Find yourself another nurse if you're that desperate for attention-!"
    sue "Umm..."
    dv "Sorry about that. These people never shut up whenever I'm talking to someone."
    pt "That's because you're always the one who starts it!"
    dv "Hey, watch your tongue, room X!"
    pt "I have a name, you know?!"
    dv "Yeah, nobody cares."
    sue "Excuse me..."
    sue "I think I should get going."
    dv "{i}{color=#bc0b17}WAIT-"
    "I hear a thud on Michael's door."
    dv "Nobody talks to me unless I get some staff member to stop here."
    dv "Could you spare me a few minutes...?"
    sue "Um... I suppose."
    dv "...."
    sue "What are you doing...?"
    dv "Looking at you."
    dv "People usually ignore me when I try to talk to them here. But you've been here for... seven minutes now?"
    sue "You asked, so I didn't want to reject you like that."
    dv "You're alright, Sue. I wish more nurses were like that."
    sue "..."
    sue "Is there anything I can do for you?"
    dv "...I appreciate the effort, but you seem really tense by now. I wouldn't want to scare you more."
    sue "-oh."
    sue "It's fine, it's just that..."
    dv "No need to explain. I get that nobody here really feels, uh... comfortable around me."
    dv "You should probably get going. Thanks for stopping by."
    sue "Well..."
    stop music fadeout 6
    sue "Goodbye."
    "She walks away in silence."
    jump patientchoice
label explor9:
    if route == "purple":
        jump exploration
    else:
        $explor9=True
        scene bg patients with dissolve
        "I'm walking through the patients'rooms hallway."
        play music "ost/hospital.wav"
        show t full:
            xpos 200
        with dissolve
        t "Hey, you! Nurse."
        show jl talk:
            xpos -200
            ypos 40
        with moveinleft
        jl "...What is it?"
        show jl neu with dissolve
        t "What day is it today? I'm losing track of time in this place."
        show jl calmtalk with dissolve
        if month == 1:
            if day == 1 or day == 21:
                jl "It's the [day]st of November."
            elif day == 2 or day == 22:
                jl "It's the [day]nd of November."
            elif day == 3 or day == 23:
                jl "It's the [day]rd of November."
            else:
                jl "It's the [day]th of November."
        else:
            if day == 1:
                jl "It's the [day]st of December."
            elif day == 2:
                jl "It's the [day]nd of December."
            elif day == 3:
                jl "It's the [day]rd of December."
            else:
                jl "It's the [day]th of December."
        $tomtimeframe=28+day
        if month == 2:
            $tomtimeframe+=30
        show jl neutral with dissolve
        t "[tomtimeframe] days... It feels like an eternity."
        show jl calm with dissolve
        jl "...."
        show jl angrytalk with dissolve
        jl "So you're stuck here?"
        show jl neutral with dissolve
        t "Until they let me leave... which doesn't seem like it's going to be soon."
        show jl calmtalk with dissolve
        jl "That must suck..."
        show jl neutalk with dissolve
        jl "You have a family back there?"
        show jl neutral with dissolve
        t "No."
        t "I have work."
        show jl angry with dissolve
        jl "Ah, I see."
        show jl neu with dissolve
        t "...."
        t "How long have you been here?"
        show jl calmtalk with dissolve
        jl "Almost two years."
        show jl calm with dissolve
        t "How can you work in a place like this? I would've quit after a month..."
        show jl talk with dissolve
        jl "Well... it's my job."
        show jl neutral with dissolve
        t "You're surrounded by crazy people."
        show jl calmtalk with dissolve
        jl "Aren't you one of them?"
        show jl neu with dissolve
        t "I'm not."
        show jl talk with dissolve
        jl "Then why are you here?"
        show jl neutral with dissolve
        "He scoffs."
        t "None of your business."
        show jl calmtalk with dissolve
        jl "Thought so."
        show jl talk with dissolve
        jl "For your information, I wouldn't stay here if I had a choice."
        show jl neutalk with dissolve
        jl "I would be more than glad not to have to rot in this place."
        show jl calm with dissolve
        jl "But life's not that easy. And you have to deal with that."
        t "Like you can lecture me about that..."
        show jl neutalk with dissolve
        jl "You asked."
        show jl neutral with dissolve
        t "...."
        t "...I'm glad some people here are just as done with this place as I am."
        show jl smile with dissolve
        jl "Yeah."
        show jl neutral with dissolve
        t "At least you could quit if you really wanted to."
        show jl calmtalk with dissolve
        jl "So could you."
        show jl neu with dissolve
        t "Huh..?"
        show jl neutalk with dissolve
        jl "I have stuff to do. See you around."
        hide jl with moveoutright
        "Julia disappears in the staircase leading to the first floor."
        jump patientchoice
label explor10:
    $explor10=True
    play music "ost/hospital.wav" fadein 6
    scene bg outside with dissolve
    "I find myself in the green area behind the hospital."
    "I overhear a conversation beetween two nurses watching over the patients..."
    show jl neu:
        xpos -125
    with dissolve
    show l left:
        xpos 125
    with dissolve
    jl "Looks like we're stuck here together."
    show l sidesadtalk with dissolve
    "The other nurse chuckles nervously."
    gu "It... seems so."
    show l pity with dissolve
    gu "...."
    show jl talk with dissolve
    jl "I don't recall ever talking to you like this. Are you new or something?"
    show jl neutral with dissolve
    show l shock with dissolve
    gu "Oh no, I've been here for over a year now."
    show l neu with dissolve
    show jl calmtalk with dissolve
    jl "Huh. I barely see you around here."
    show jl neu with dissolve
    show l sadsmile with dissolve
    "She shrugs."
    show l sidetalk with dissolve
    gu "Our schedules must be quite different."
    show jl calm with dissolve
    show l neu with dissolve
    jl "Maybe."
    show jl talk with dissolve
    jl "So, uh... Milena, is it?"
    $persistent.Milfirst="Milena"
    show jl neutral with dissolve
    show l gasp with dissolve
    l "That's right, Ms. Watts."
    $persistent.Julialast="Watts"
    play sound "chars.ogg" 
    show screen notify("{size=24} Your Characters Info screen has been updated!")
    show jl smile with dissolve
    show l neu with dissolve
    jl "You can use my first name, you know? We're coworkers, there's no need to be this formal."
    show l cute with dissolve
    l "Oh... thank you." 
    show l regrettalk with dissolve
    l "I'm just... not used to being this straightforward."
    show jl calmtalk with dissolve
    show l sidesmile with dissolve
    jl "I see."
    show jl calm with dissolve
    "...."
    show jl talk with dissolve
    jl "You're from Europe, right?"
    show jl neutral with dissolve
    show l neu with dissolve
    "She nods."
    show l regrettalk with dissolve
    l "I moved here with my mother when I was six. I don't remember much."
    show l pity with dissolve
    show jl calmtalk with dissolve
    jl "Sorry, it's just the way you talk..."
    show jl neutral with dissolve
    show l blush with dissolve
    l "It's... difficult. But I try."
    show jl neutalk with dissolve
    jl "Not that it bothers me, of course, but... I don't know, it's curious."
    show l pity with dissolve
    l "...."
    show l neutral with dissolve
    show jl calmtalk with dissolve
    jl "I haven't been to Europe in a while..."
    show jl calm with dissolve
    show l gasp with dissolve
    l "Huh?"
    show l neu with dissolve
    show jl talk with dissolve
    jl "My parents took me to Spain once during summer when I was a kid."
    show jl neutral with dissolve
    show l cute with dissolve
    l "That must've been nice."
    show jl neutalk with dissolve
    jl "Yeah. Not like I could afford that now on my own."
    show jl calm with dissolve
    show l sadtalk with dissolve
    l "...I'm sorry."
    show l regret with dissolve
    show jl neutral with dissolve
    jl "...."
    show jl neutalk with dissolve
    jl "Do you ever travel to where you're from anymore?"
    show l talk with dissolve
    l "With my mother, usually once a year for Christmas."
    show l sidesadtalk with dissolve
    l "My family would probably die if we didn't visit them enough, heh..."
    show l pity with dissolve
    show jl calmtalk with dissolve
    jl "You're that close with them?"
    show l gasp with dissolve
    show jl neu with dissolve
    l "Of course! And my mother is worried sick about me ever since I'm on my own... she calls me all the time."
    show l cute with dissolve
    show jl smile with dissolve
    jl "Sounds like they all really care about you."
    show l left with dissolve
    l "I mean... maybe families are closer where I'm from. I don't really know."
    show l regret with dissolve
    show jl neu with dissolve
    jl "I see."
    show l neu with dissolve
    show jl smile with dissolve
    jl "It must be nice to have all these people who support you."
    show l sidetalk with dissolve
    l "Umm... I still like it here more."
    show l neu with dissolve
    show jl calm with dissolve
    jl "I guess that's what matters."
    "I decide it's time to get back to my office."
    jump patientchoice
label explor11:
    if route == "green":
        jump exploration
    else:
        $explor11=True
        play music "ost/hospital.wav" fadein 6
        scene bg offices with dissolve
        "I overhear a conversation coming from one of the offices."
        s "What is it? Is there a problem?"
        d "Actually, there is. A patient of yours came into my office today."
        d "He asked for a transfer to Dr. Bright."
        d "I was hoping you could shed some light on the situation."
        s "I... You must mean Nicholas, right?"
        s "He's been a bit... unstable recently. I didn't want to bother you, I thought it would -"
        d "You neglected to inform me of this because you did not want to bother me?"
        s "That's... that's right."
        d "Charles, being \"bothered\" is what I am here for. You should have told me earlier."
        s "...."
        s "I know. It's just that you always seem busy with more important things."
        d "There is nothing more important than the wellbeing of your patients."
        d "If something like this happens again, please inform me as soon as you can."
        s "I will."
        d "Do you have anything to say about his transfer to Dr. Bright?"
        s "No. You should let him transfer."
        d "That is all, then. Thank you for your time, Charles."
        s "I'm... always happy to help."
        "I think I should get going."
        jump patientchoice
label explor12:
    $explor12=True
    play music "ost/hospital.wav" fadein 5
    scene bg patients with dissolve
    "I'm walking through the patients' rooms hallway when I stumble upon an interesting sight."
    show e baka:
        xpos -0.3    
    with dissolve
    e "What?"
    show dv full:
        xpos 0.3
    with dissolve
    dv "I don't know you. You must be new."
    show e calmtalk with dissolve
    e "I don't know you either and I don't want to. Scram."
    show e neu with dissolve
    dv "...?"
    "He takes a step towards her and looks closely at her face for a moment before stepping away."
    stop music fadeout 4
    dv "...Interesting."
    show e talk with dissolve
    e "Huh?"
    show e neu
    dv "I don't think I want to know you, either."
    show e angry with dissolve
    e "{i}???"
    dv "Goodbye."
    show e talk with dissolve
    hide dv with moveoutright
    "I look at Elizabeth standing there, dumbfounded, wondering what he meant."
    hide e with dissolve
    "Well, I guess I'll be on my way."
    play music "ost/tension.ogg" fadein 6
    show dv full with vpunch
    dv "Hey."
    m hfh "Jesus! Michael -"
    dv "Which one is it?"
    "He's laughing at me. Of course he is."
    m trigger "Shouldn't you be under supervision at all times?"
    dv "Isn't your supervision enough?"
    "Uhh..."
    m wut "I... I'm not a nurse..?"
    dv "Well, we can wait for one if you want. They're awfully busy, you see."
    "...."
    menu:
        "What's up with you and Elizabeth?":
            dv "Me and..?"
            dv "Oh, her. {w}Nothing, apparently."
            m fabtalk "What do you mean? Weren't you interested in her?"
            dv "Why would I be interested in her?"
            m talk "I don't know, she's... a woman?"
            dv "And you think that makes her interesting to me?"
            m uncom "Well, if the nurses are any indication, that makes her a target."
            dv "...."
            "He bores his eyes into the floor."
            dv "You really don't understand."
            m gasp "What don't I understand?"
            "He tilts his head back and glances around the area before turning his full attention back to me."
            dv "It's not about what they look like. Or what gender they are."
            dv "That Elizabeth lady... I looked at her and I saw nothing. She's like a blank page."
            m frust "Well she... isn't very expressive."
            dv "That's not the problem. I like people who \"aren't very expressive\". It takes more digging with them."
            dv "Thing is, with her there's nothing at the bottom."
            "I think I'm beginning to understand. Still..."
            m angry "And you can tell that just by looking at her?"
            dv "I've rarely been wrong about people."
            stop music fadeout 5
            "There's a healthy dose of skepticism in my mind."
            "But I've known him to be perceptive, so I'll give him that."
            dv "You're not convinced."
            dv "Well, I was trying to explain, not persuade. You can think whatever you want."
            m talk "Gee, thanks."
            dv "...?"
            play music "ost/emo.wav" fadein 5
            "He looks at me and smiles."
            dv "What? It can't be that bad."
            m gasp "Huh?"
            dv "Talking to me."
            m angrytalk "The talking part is fine, it's the attacking people part that isn't."
            dv "Ah."
            "We stand around for a bit in awkward silence before one of the nurses approaches us."            
        "So you just want to stand around?":
            dv "Is that a problem?"
            stop music fadeout 4
            m "Umm..."
            dv "Hmm~?"
            m "Yeah, no. I don't think I want to do that."
            hide dv with dissolve
            "I look around and see a nurse passing by, so I ask her to watch him and leave."
        "I have things to do":
            stop music fadeout 4
            dv "Do you? Isn't this your break?"
            "...shit. {w}He's right."
            hide dv with dissolve
            "I look around and see a nurse passing by, so I ask her to watch him and leave."
    scene black with dissolve
    "That sure was... interesting."
    jump patientchoice
label explor13:
    if StarLink == 0:
        scene bg offices with dissolve
        $StarLink=1
        $explor13=True
        play music "ost/hospital.wav" fadein 5
        "Walking outside my office, I spot {color=#81abe2}a man I've never seen before{/color}."
        "He looks at me curiously."
        show s talk with dissolve
        s "Have we met?"
        show s neu with dissolve
        m fabtalk "I don't think so."
        m conf "I'm [name] Hart - I work here as a psychologist."
        show s neutalk with dissolve
        s "I can tell by your office..."
        show s neutral with dissolve
        "I turn around to realize that the door is labelled with my name."
        show s talk with dissolve
        s "Since when do you work here, exactly...?"
        show s neu with dissolve
        m fabtalk "The beginning of November."
        show s gasp with dissolve
        s "Oh. That certainly explains some things."
        if le:
            show s neutral with dissolve
            s "Well, if you don't mind, I have things to do."
            m gasp "Of course."
            hide s with moveoutright
            "He leaves and I'm left to wonder who he was."
            jump patientchoice
        show s smile with dissolve
        s "It's strange that we weren't introduced before... {color=#81abe2}Charles Young, psychiatrist."
        $star = "Dr. Young"
        if route=="blue":
            m gasp "Oh, you must be Charlie's psychiatrist - he's one of my patients."
        m happy "It's nice to meet you, Dr.Young."
        show s sadtalk with dissolve
        s "...Where are my manners? I assumed you had the time to chat, Ms. Hart..."
        show s neutral with dissolve
        m "It's fine. I was just taking a stroll on my break."
        show s smirk with dissolve
        s "I see."
        show s neutalk with dissolve
        s "A walk through the hospital is surely relaxing beetween sessions with patients..."
        show s smile with dissolve
        "Dr. Young smiles at me. He seems genuinely friendly."
        stop music fadeout 1
        scene black with Dissolve(1.5)
        show s smile with dissolve
        "{color=#81abe2}I feel a bond forming beetween me and the psychiatrist..."
        "I smile back."
        play music "ost/hospital.wav" fadein 3
        scene bg offices with dissolve
        show s cute with dissolve
        "We spend the rest of our break chatting in the offices hallway."
        show s neutalk with dissolve
        s "I should probably go back to my office soon..."
        show s smile with dissolve
        s "It's {color=#81abe2}the one to your right, close to the central hall{/color}."
        show s talk with dissolve
        s "You should be able to find it easily if you ever need anything from me."
        show s smirk with dissolve
        s "It's good to have a new coworker here - things get awfully dull without the right company."
        show s cute with dissolve
        m flirt "I'll see you again soon~"
        scene black with dissolve
        "With that, I step back into my office and leave Dr. Young."
        "I realize he's the only therapist I know here other than Dr. Sharpe."
        stop music fadeout 5
        $persistent.Young=True
        play sound "chars.ogg" 
        show screen notify("{size=24} Your Characters Info screen has been updated!")
        "It would be interesting to talk to someone who understands the nature of my work."
        "And since he's been here for longer than me, I might learn some things about the hospital as well..."
        "If I ever want to talk to him again, I can find him in {color=#81abe2}HIS OFFICE{/color} during the break."
        jump patientchoice
    else:
        jump exploration
label explor14:
    $explor14=True
    scene bg mc with dissolve
    play music "ost/hospital.wav" fadein 5
    "My office..."
    "Somehow, I can't think of any place to go for now."
    show bg sun with dissolve
    "I look out the window. The weather seems alright."
    "It's 12 PM..."
    show bg mc with dissolve
    "I'm... bored?"
    "But at the same time I can't quite find the strength to go anywhere."
    "So I'll just stay here."
    "I feel too lazy to walk right now."
    "Damn, it would really help to have something to drink around here... I wouldn't mind a hot cup of tea."
    play sound "page.ogg"
    "I look through my notes about the patients so far. I'm quite proud of these."
    "Umm... what else is there to do in my office...?"
    "I spend the rest of my break pondering my progress with the patients... and the tea, of course."
    jump patientchoice
label explor15:
    $explor15=True
    scene bg central with dissolve
    "I find myself in the central hall."
    "Since there isn't anyone I recognize here, I stop by one of the windows."
    play music "sun.ogg" fadein 5
    "The view is breathtaking..."
    "The {color=#f46666}small town{/color} I live in as of november is located almost right outside of the hospital."
    "Only a desolate road seperates the building from the town."
    "And further to the west, ahead of me, is only the darkness spread by a massive {color=#f72c2c}forest."
    "Beyond the forest lies {color=#f46666}the city{/color} most of the patients used to live in."
    "I can barely make out some of the taller buildings lurking in the distance."
    "I know there's another, {color=#f46666}smaller forest{/color} behind the hospital, to the east."
    "Looking down, I get slightly dizzy from realising I'm quite far from the ground. It's the second floor, after all."
    stop music fadeout 2
    "I take a while to watch the people going around the small town, and children playing near the forest."
    scene black with dissolve
    pause 0.5
    jump patientchoice
label explor16:
    $explor16=True
    scene bg central with dissolve
    play music "ost/hospital.wav" fadein 5
    "I find myself in the central hall."
    "As per usual, I can't help but glare at the third floor above me."
    "I can't help but wonder what it looks like, exactly..."
    "I know it's where doctors and psychologists stay for the night, but I never got the chance to go there yet."
    "It would be interesting to be chosen for the nightshift someday..."
    "I imagine it's no easy task, and I likely wouldn't get much sleep, but still..."
    "Being able to get to the patients at night in case of an emergency sounds like a great way to help."
    "And I could support my fellow staff members while doing so."
    "I'm sure the nurses and doctors would appreciate my help."
    "Either way, I better wait to be chosen for the nightshift, instead of rushing in."
    "I suspect part of the reason why I have to wait is that I'm new here." 
    "Obviously, Dr.Sharpe seems to have the assumption that I can't handle all the tasks that other psychologists have."
    "...Is it strange that I'm just standing around here, staring at the third floor?"
    stop music fadeout 4
    "Yeah, it would be a bit suspicious if someone found me like this..."
    "I should get back to my office."
    jump patientchoice
label explor17:
    jump exploration
label explor18:
    $explor18=True
    scene bg greet with dissolve
    play music "ost/hospital.wav" fadein 5
    "I find myself wandering into the reception."
    show jl calm with dissolve
    "Julia is here again. I approach her."
    show jl neu with dissolve
    m flirt "Hello, Julia."
    "She seems bored."
    show jl gasp with dissolve
    jl "Huh?"
    show jl talk with dissolve
    if TempLink>1:
        jl "Oh, it's you. Take a seat, Hart."
        show jl smile with dissolve
        "She points to another chair behind the reception desk."
        show jl talk with dissolve
        jl "So what brings you here? Boredom?"
        show jl neu with dissolve
        m conf "Pretty much."
        show jl calmtalk with dissolve
        jl "Well, you've come to the wrong place. Nothing ever happens here."
        show jl neu with dissolve
        m cute "You're here."
        show jl blush with dissolve
        jl "...."
        show jl smile with dissolve
        jl "That's cute, Hart. You can stay."
        show jl calm with dissolve
        "We sit around with Julia for a bit before I decide to get back to my office."
    else:
        jl "You're a psychologist, right?"
        show jl angry with dissolve
        m smile "I am."
        "Last time I met her, I wasn't even hired yet."
        "I'm surprised she remembers me."
        show jl talk with dissolve
        jl "What's a psychologist like you doing here? Heading home already?"
        show jl neu with dissolve
        m cute "I'm just walking around on my break."
        show jl calm with dissolve
        jl "Huh."
        scene black with dissolve
        "I leave Julia be and wander around some more."
    jump patientchoice
label explor19:
    jump exploration
label explor20:
    jump exploration
label explor21:
    scene bg hallway with dissolve
    "I'm walking through the first floor."
    "I stop when I hear voices coming from behind the door leading to the area for visitors."
    play music "ost/hospital.wav" fadein 6
    if explore == 42 or explore == 43:
        $explor21=True
        wm "Kate, darling, can you hear me?"
        wm "Please tell me you can..."
        doc "Miss, I'm afraid your daughter's state will not allow her to communicate with you yet."
        wm "It happened so suddenly... how could she have changed like this?"
        doc "We're doing our best, but an episode like this can take some time."
        wm "She's never had any problems... Why now?"
        doc "It may be a defense mechanism of some kind."
        wm "Defense against what? Doctor, with all due respect, we've been taking care of her as best we could, how can you accuse us of -"
        doc "I am not accusing anyone. Kate needs time and professional care right now."
        wm "I'm sorry, Doctor... it's just that this tragedy really hit me and my husband..."
        wm "...I trust you when you say that she'll be back."
        doc "As you should. There's no need to worry."
        "Poor girl..."
    elif explore == 44 or explore == 45:
        $explor22=True
        mn "I'm sorry I couldn't see you before, work kept me busy all this time..."
        wm "It's okay..."
        "Her voice sounds weak..."
        wm "I know you're trying your best for me."
        mn "...."
        mn "You look miserable. Do they even feed you here?"
        wm "It's not about them, David... I..."
        wm "It's been getting worse. I can't eat like everyone else here... I just can't."
        mn "Are you sure you're comfortable here? Do you have everything you need?"
        wm "...."
        wm "They sent all your gifts back since I'm here."
        mn "What?"
        wm "They said... I don't need all that and that I'll get everything once I'm out."
        mn "The nerve! I wasn't told of that..."
        wm "But... the last shoes were nice."
        mn "I was hoping you'd wear them for my visit today, but..."
        wm "They didn't allow me to bring half of my clothes - you wouldn't believe how much I had to leave at home!"
        mn "...."
        mn "How long will this take?"
        wm "A month, they said."
        mn "A month?!"
        mn "How are you supposed to last that long here?"
        wm "They said there's no way I can leave earlier..."
        mn "...."
        wm "I'll be back as soon as I can, I promise."
        mn "I'll get you as much as you want once you are."
        "I'm uncomfortable."
    elif explore == 46 or explore == 47:
        $explor23=True
        wm "How do you feel..?"
        mn "...I told you you shouldn't be here."
        mn "You should just forget about me."
        wm "Why should I? I... I don't want to leave you like that..."
        mn "You heard the doctors... what part of \"mentally ill\" do you not understand?"
        wm "No, that's no reason for me to give up on you..."
        mn "Why? What the hell's wrong with you?"
        wm "I love you, dammit!"
        mn "...."
        mn "I'm sorry, Jess, I just... thought it was for the best."
        mn "I don't know anymore..."
        wm "It's okay. We've been together for two years now. We can get through this."
        mn "...."
        mn "...I love you, too."
        "This is... so heartwarming."
        "I'm glad some people here have the support of their loved ones."
    scene black with dissolve
    "I decide it's best to stop listening to people I don't know talking and leave the first floor."
    jump patientchoice
label explor22:
    play music "ost/hospital.wav" fadein 5
    scene bg outside
    "I end up going outside to where I first met Elizabeth on my second day of work."
    if explore == 48 or explore == 49:
        $explor24=True
        "Leaning against the wall, I spot a nurse I recognize."
        if SunLink > 0:
            "It's Sue."
            "I wave at her when she looks in my direction."
            "She's a bit far away, but she notices me nonetheless."
            sue "Oh, [name]! I didn't see you there~!"
            "She smiles at me, but keeps watching the patients near her."
        else:
            "It's the one who lead me to Dr.Sharpe's office for my job interview."
            "I don't know her name, but she's definitely familiar."
            "She seems to be watching over some patients here... I shouldn't disturb her."
        "I spend some time watching the patients."
    else:
        $explor25=True
        "A pair of patients catches my eye."
        "They seem to be arguing about something."
        "I hear one of them start to yell at the other, but before I can step in, a nurse walks towards them."
        "She seems to have stopped their argument."
        "Damn, it must be tough being a nurse..."
    stop music fadeout 2
    "I leave the courtyard area before the end of my break."
    jump patientchoice
label explor23:
    jump exploration
label explor24: 
    $explor26=True
    scene bg front with dissolve
    play music "ost/tran.ogg" fadein 6
    "I end up going outside the hospital."
    "I figured a walk might do me some good."
    "It's... a little chilly. Good thing I grabbed my jacket."
    "It's rare to get a moment where there's literally nothing going on and I can just... think."
    "Recent events come to my mind."
    "...."
    "I hope I'm doing everything right."
    scene black with dissolve
    "On my way back to my office, I feel somewhat invigorated."
    if sanity<40:
        $sanity+=10
    else:
        $sanity=50
    jump patientchoice
label explor25:
    jump exploration
label explor26:
    jump exploration
label explor27:
    jump exploration
