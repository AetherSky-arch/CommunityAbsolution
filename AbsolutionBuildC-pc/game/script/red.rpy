define cr = Character("Caroline", color = '#ffffff')
define dvn = Character("Michael", color = '#ffffff', screen = "cinematic")

default DevilFreed = False
default DevilShip=False

##Black sprite
image dv bneutral = "sprites/devil/b/Neutral.png"
image dv bneu = "sprites/devil/b/Neu.png"
image dv bsmile = "sprites/devil/b/Smile.png"
image dv btalk = "sprites/devil/b/Talk.png"
image dv bhes = "sprites/devil/b/Hes.png"
image dv bsmirk = "sprites/devil/b/Smirk.png"
image dv bbreath = "sprites/devil/b/Breath.png"
image dv bneutalk = "sprites/devil/b/Neutalk.png"
image dv bangry = "sprites/devil/b/Angry.png"
image dv bangrytalk = "sprites/devil/b/AngryTalk.png"
image dv bsad = "sprites/devil/b/Sad.png"
image dv bsadtalk = "sprites/devil/b/SadTalk.png"
image dv bsadsmile = "sprites/devil/b/SadSmile.png"
image dv bcute = "sprites/devil/b/Cute.png"
image dv bblush = "sprites/devil/b/Blush.png"
image dv bshock = "sprites/devil/b/Shock.png"
image dv bsiden = "sprites/devil/b/Siden.png"
image dv bsidesmile = "sprites/devil/b/SideSmile.png"
image dv bsidetalk = "sprites/devil/b/SideTalk.png"
image dv bdevil = "sprites/devil/b/Devil.png"
image dv bfrust = "sprites/devil/b/Frust.png"
image dv bfrusttalk = "sprites/devil/b/Frusttalk.png"
image dv bmoment = "sprites/devil/b/Moment.png"
image dv bpant = "sprites/devil/b/Pant.png"
image dv bgasp = "sprites/devil/b/Gasp.png"
image dv bdark = "sprites/devil/b/Dark.png"
image dv bkh = "sprites/devil/b/Khhh.png"
image dv bkh2 = "sprites/devil/b/Khhh2.png"
image dv bdarktalk = "sprites/devil/b/DarkTalk.png"
image dv byandere = "sprites/devil/b/Yandere.png"
image dv bdarkgasp = "sprites/devil/b/Darkgasp.png"
image dv bcreepy = "sprites/devil/b/Creepy.png"
image dv bnoeyes = "sprites/devil/b/NoEyes.png"
image dv bnotalk = "sprites/devil/b/NoTalk.png"
image dv btwitch = "sprites/devil/b/Twitch.png"
image dv bdarkblush = "sprites/devil/b/DarkBlush.png"
image dv btsun = "sprites/devil/b/Tsun.png"
##Red sprite
image dv rneutral = "sprites/devil/r/Neutral.png"
image dv rneu = "sprites/devil/r/Neu.png"
image dv rsmile = "sprites/devil/r/Smile.png"
image dv rtalk = "sprites/devil/r/Talk.png"
image dv rhes = "sprites/devil/r/Hes.png"
image dv rsmirk = "sprites/devil/r/Smirk.png"
image dv rbreath = "sprites/devil/r/Breath.png"
image dv rneutalk = "sprites/devil/r/Neutalk.png"
image dv rangry = "sprites/devil/r/Angry.png"
image dv rangrytalk = "sprites/devil/r/AngryTalk.png"
image dv rsad = "sprites/devil/r/Sad.png"
image dv rsadtalk = "sprites/devil/r/SadTalk.png"
image dv rsadsmile = "sprites/devil/r/SadSmile.png"
image dv rcute = "sprites/devil/r/Cute.png"
image dv rblush = "sprites/devil/r/Blush.png"
image dv rshock = "sprites/devil/r/Shock.png"
image dv rsiden = "sprites/devil/r/Siden.png"
image dv rsidesmile = "sprites/devil/r/SideSmile.png"
image dv rsidetalk = "sprites/devil/r/SideTalk.png"
image dv rdevil = "sprites/devil/r/Devil.png"
image dv rfrust = "sprites/devil/r/Frust.png"
image dv rfrusttalk = "sprites/devil/r/Frusttalk.png"
image dv rmoment = "sprites/devil/r/Moment.png"
image dv rpant = "sprites/devil/r/Pant.png"
image dv rgasp = "sprites/devil/r/Gasp.png"
image dv rdark = "sprites/devil/r/Dark.png"
image dv rkh = "sprites/devil/r/Khhh.png"
image dv rkh2 = "sprites/devil/r/Khhh2.png"
image dv rdarktalk = "sprites/devil/r/DarkTalk.png"
image dv ryandere = "sprites/devil/r/Yandere.png"
image dv rdarkgasp = "sprites/devil/r/Darkgasp.png"
image dv rcreepy = "sprites/devil/r/Creepy.png"
image dv rnoeyes = "sprites/devil/r/NoEyes.png"
image dv rnotalk = "sprites/devil/r/NoTalk.png"
image dv rtwitch = "sprites/devil/r/Twitch.png"
image dv rdarkblush = "sprites/devil/r/DarkBlush.png"
image dv rtsun = "sprites/devil/r/Tsun.png"

image dv close = "sprites/devil/r/Close.png"

image devil1:
    "gui/f/black.png" with dissolve
    "cg/Devil1.png" with dissolve

image dattack1:
    "cg/Devilattack2.png" with Dissolve(0.2)
    pause 0.1
    "cg/Devilattack.png" with Dissolve(0.2)
    pause 0.1
    "cg/Devilattack2.png" with Dissolve(0.2)
    "cg/Devilattack.png" with dissolve
    pause 1.5
    repeat
image dattack2:
    "cg/Devilattack3.png" with dissolve
    pause 2
    "cg/Devilattack4.png" with Dissolve(0.2)
    "cg/Devilattack5.png" with Dissolve(0.2)
    "cg/Devilattack4.png" with Dissolve(0.2)

image caroline = "cg/Caroline.png"
image bg caroline = "bg/Caroline.png"

image cr neutral = "sprites/chariot/Neutral.png"
image cr talk = "sprites/chariot/Talk.png"
image cr neu = "sprites/chariot/Neu.png"
image cr smile = "sprites/chariot/Smile.png"
image cr gasp = "sprites/chariot/Gasp.png"
image cr angry = "sprites/chariot/Angry.png"
image cr angrytalk = "sprites/chariot/Angrytalk.png"
image cr evil = "sprites/chariot/Evil.png"
image cr trigger = "sprites/chariot/Trigger.png"
image cr sad = "sprites/chariot/Sad.png"
image cr sadtalk = "sprites/chariot/Sadtalk.png"
image cr sadsmile = "sprites/chariot/Sadsmile.png"
image cr siden = "sprites/chariot/Siden.png"
image cr sidetalk = "sprites/chariot/Sidetalk.png"
image cr sidesmile = "sprites/chariot/Sidesmile.png"
image cr frust = "sprites/chariot/Frust.png"
image cr frusttalk = "sprites/chariot/Frusttalk.png"
image cr frustsmile = "sprites/chariot/Frustsmile.png"
image cr baka = "sprites/chariot/Baka.png"
image cr regret = "sprites/chariot/Regret.png"
image cr regrettalk = "sprites/chariot/Regrettalk.png"
image cr regretsmile = "sprites/chariot/Regretsmile.png"

label rednotes:
    if month == 1:
        if day == 6 or day ==  7 or day == 13 or day == 14 or day > 17:
            jump rednav
    if ndevil1=="":
        $ndevil1 = renpy.input("Note 1 (max 50 characters):", length = 50)
    else:
        if ndevil2=="":
            $ndevil2 = renpy.input("Note 2 (max 50 characters):", length = 50)
        else:
            if ndevil3=="":
                $ndevil3 = renpy.input("Note 3 (max 50 characters):", length = 50)
            else:
                if ndevil4=="":
                    $ndevil4 = renpy.input("Note 4 (max 50 characters):", length = 50)
                else:
                    if ndevil5=="":
                        $ndevil5 = renpy.input("Note 5 (max 50 characters):", length = 50)
                    else:
                        if ndevil6=="":
                            $ndevil6 = renpy.input("Note 6 (max 50 characters):", length = 50)
                        else:
                            if ndevil7=="":
                                $ndevil7 = renpy.input("Note 7 (max 50 characters):", length = 50)
                            else:
                                if ndevil8=="":
                                    $ndevil8 = renpy.input("Note 8 (max 50 characters):", length = 50)
                                else:
                                    if ndevil9=="":
                                        $ndevil9 = renpy.input("Note 9 (max 50 characters):", length = 50)
                                    else:
                                        if ndevil10=="":
                                            $ndevil10 = renpy.input("Note 10 (max 50 characters):", length = 50)
                                        else:
                                            if ndevil11=="":
                                                $ndevil11 = renpy.input("Note 11 (max 50 characters):", length = 50)
                                            else:
                                                if ndevil12=="":
                                                    $ndevil12 = renpy.input("Note 12 (max 50 characters):", length = 50)
                                                else:
                                                    if ndevil13=="":
                                                        $ndevil13 = renpy.input("Note 13 (max 50 characters):", length = 50)
                                                    else:
                                                        if ndevil14=="":
                                                            $ndevil14 = renpy.input("Note 14 (max 50 characters):", length = 50)
                                                        else:
                                                            if ndevil15=="":
                                                                $ndevil15 = renpy.input("Note 15 (max 50 characters):", length = 50)
                                                            else:
                                                                if ndevil16=="":
                                                                    $ndevil16 = renpy.input("Note 16 (max 50 characters):", length = 50)
                                                                else:
                                                                    if ndevil17=="":
                                                                        $ndevil17 = renpy.input("Note 17 (max 50 characters):", length = 50)
                                                                    else:
                                                                        if ndevil18=="":
                                                                            $ndevil18 = renpy.input("Note 18 (max 50 characters):", length = 50)
                                                                        else:
                                                                            if ndevil19=="":
                                                                                $ndevil19 = renpy.input("Note 19 (max 50 characters):", length = 50)
                                                                            else:
                                                                                if ndevil20=="":
                                                                                    $ndevil20 = renpy.input("Note 10 (max 50 characters):", length = 50)
                                                                                else:
                                                                                    "I've already filled up all my notes."
                                                                                    "Should I rewrite one of my notes?"
                                                                                    menu:
                                                                                        "[ndevil1]":
                                                                                            $ndevil1 = renpy.input("Note 1 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil2]":
                                                                                            $ndevil2 = renpy.input("Note 2 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil3]":
                                                                                            $ndevil3 = renpy.input("Note 3 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil4]":
                                                                                            $ndevil4 = renpy.input("Note 4 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil5]":
                                                                                            $ndevil5 = renpy.input("Note 5 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil6]":
                                                                                            $ndevil6 = renpy.input("Note 6 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil7]":
                                                                                            $ndevil7 = renpy.input("Note 7 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil8]":
                                                                                            $ndevil8 = renpy.input("Note 8 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil9]":
                                                                                            $ndevil9 = renpy.input("Note 9 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil10]":
                                                                                            $ndevil10 = renpy.input("Note 10 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil11]":
                                                                                            $ndevil11 = renpy.input("Note 11 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil12]":
                                                                                            $ndevil12 = renpy.input("Note 12 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil13]":
                                                                                            $ndevil13 = renpy.input("Note 13 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil14]":
                                                                                            $ndevil14 = renpy.input("Note 14 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil15]":
                                                                                            $ndevil15 = renpy.input("Note 15 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil16]":
                                                                                            $ndevil16 = renpy.input("Note 16 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil17]":
                                                                                            $ndevil17 = renpy.input("Note 17 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil18]":
                                                                                            $ndevil18 = renpy.input("Note 18 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil19]":
                                                                                            $ndevil19 = renpy.input("Note 19 (maximum 50 characters):", length = 50)
                                                                                        "[ndevil20]":
                                                                                            $ndevil20 = renpy.input("Note 20 (maximum 50 characters):", length = 50)
                                                                                        "Don't rewrite":
                                                                                            jump breaknav
    "Write another note?"
    menu:
        "Yes":
            jump rednotes
        "No":
            if route=="red":
                jump breakreal
            jump breaknav


label rednav:
scene black with dissolve
pause 1
$firstpatient = "red"
$sessions += 1
########################## 
if month == 1:
    if day == 8:
        scene bg mcdesk with dissolve
        play music "ost/neutral.ogg" fadein 5
        "Last Friday, I've decided to keep seeing Michael every day."
        "He told me he'd explain the details of how he got here today, and I expect him to keep that promise."
        "He enters my office."
        if easymeter:
            show screen easymeter
            show screen redmeter
        show dv smirk with dissolve
        dv "Hello again, [name] ~"
        menu:
            "Good morning":
                $professional+=1
            "Hi":
                $personal+=1
                show dv gasp with dissolve
                dv "Oh? That's new, coming from you."
                show dv smirk with dissolve
                m fabtalk "I don't see a need to be that formal around you if it doesn't benefit your sessions."
                show dv smile with dissolve
                "He smiles."
        m talk "So..."
        stop music fadeout 5
        show dv shock with dissolve
        dv "I promised to tell you everything, right?"
        show dv neu with dissolve
        "I nod."
        show dv sidetalk with dissolve
        dv "Alright then... Let's start with..."
        show dv frust with dissolve
        dv "Actually, I mentioned being in a relationship last time. I should probably tell you about that."
        play music "ost/memory.ogg" fadein 8
        show rback 1 with dissolve
        dv "Her name's Caroline. We met in high school."
        dv "We were friends for a while after that... a few years, actually."
        dv "Then one day, she told me she'd had a crush on me since we met."
        dv "I honestly think one of her friends convinced her to tell me..."
        dv "And... you can probably imagine that with how I am, it was just... really weird for me."
        dv "I didn't know what to do, I didn't want to make her feel bad..."
        m fabtalk "Didn't you like her back?"
        dv "No- I mean... that wasn't really the problem, {cps=*3}since she was kind of hot-"
        dv "{i}Also{/i} I liked her a lot as a friend."
        dv "But, uh... no, the issue was me. As always."
        dv "Honestly, I just didn't want a girlfriend. Ever."
        dv "I was... worried about my condition affecting them."
        m talk "I see."
        dv "You know, I generally avoided people most of my life. It was a lot easier that way."
        dv "So suddenly being in a relationship with someone was... kind of overwhelming."
        dv "But once she told me, she was really, uh... persistent about it, and I didn't want her to think I didn't care about her at all..."
        dv "Obviously, she didn't know about my illness, like everyone else I knew."
        m fabtalk "You really managed to hide it from everyone for that long?"
        dv "Well... if you're desperate enough and don't interact with anyone much, it's possible."
        dv "Anyway..."
        dv "I... probably should've told her the truth then, so at least she'd have a reason for why I rejected her, but..."
        dv "I don't know, I guess I didn't really know what to say, and I didn't want to scare her off."
        dv "Because she would absolutely leave me if she found out."
        dv "And besides, I thought to myself: \"What are you so scared of? You won't know until you try\"."
        dv "\"...it can't be... as bad as you think.\""
        m talk "Was it better than you thought it would be in the end?"
        "He laughs."
        stop music fadeout 5
        dv "Oh, I wish..!"
        dv "Well... I told her that I liked her as well, and we started dating. That was a year before I was admitted here."
        hide rback with dissolve
        show dv frusttalk with dissolve
        play music "ost/hospital.ogg" fadein 8
        dv "Honestly, if it was fully my choice, I would've rejected her."
        show dv sadtalk with dissolve
        dv "But I could tell she was really serious about it, and... I guess I couldn't really bring myself to reject someone like that."
        show dv talk with dissolve
        dv "I was a lot different then... I made a lot of stupid choices."
        show dv neutral with dissolve
        menu:
            "Do you regret being with her?":
                show dv frusttalk with dissolve
                dv "That's actually a really good question..."
                show dv sidetalk with dissolve
                dv "Do I..?"
                show dv smirk with dissolve
                dv "Nah. I think it would've happened eventually."
                show dv frusttalk with dissolve
                dv "And in some ways, I feel better now than I did these four years ago."
            "So you didn't really feel the same way about her?":
                show dv sidetalk with dissolve
                dv "Uhh... yeah, I guess you're right."
                show dv frusttalk with dissolve
                dv "I never really {i}\"loved\"{/i} her in the traditional sense."
                show dv talk with dissolve
                dv "I just thought it would be a good idea to try it and see if I'm actually capable of being in a relationship with someone."
                show dv devil with dissolve
                dv "Spoiler alert: I'm not."
            "Did she really pressure you to be with her?":
                show dv sadtalk with dissolve
                dv "No, not that much... I pressured myself more."
                show dv talk with dissolve
                dv "Thinking about it now, it... may have all been in my head."
                show dv frusttalk with dissolve
                dv "I just didn't want to make her feel bad."
        show dv neutral with dissolve
        m fabtalk "I think we're running out of time for today."
        scene bg mc with dissolve
        "I lead him to the door."
        m conf "I'll see you tomorrow, Michael."
        dv "You better... I haven't even gotten to the good part of that story ~"
        hide screen redmeter
        hide screen easymeter
        "I'm not sure if that makes me more eager to know the rest, but okay."
        play sound "doorclose.ogg" fadein 1
        "He leaves."
        jump breakchoice
    elif day == 9:
        scene bg mcdesk with dissolve
        show dv neutral with dissolve
        play music "ost/neutral.ogg" fadein 5
        "Michael is back in my office."
        if easymeter:
            show screen easymeter
            show screen redmeter
        m talk "Last time you told me about your past girlfriend, Caroline, and how you became a couple..."
        show dv siden with dissolve
        m fabtalk "Will you tell me more about your relationship with her today?"
        show dv neu with dissolve
        "He nods."
        show dv talk with dissolve
        dv "When we first started dating, I was really nervous around her."
        show dv frusttalk with dissolve
        stop music fadeout 6
        dv "She thought I was just shy because she was my first... she didn't really have a problem with that, so I never told her the real reason."
        show dv frust with dissolve
        "I can already tell their relationship was far from perfect if he hid these things from her."
        show rback 2 with dissolve
        play music "ost/memory.ogg" fadein 8
        dv "But... when you're in a relationship, it's impossible to avoid... being close to someone."
        dv "The only thing I could do was try my best not to lose control around her."
        dv "It wasn't difficult at first, she took her time..."
        dv "But, obviously... it escalated over time."
        dv "And while I had no trouble at first, I just couldn't keep up with her."
        dv "The more time I spent with her, the more attached I grew to her."
        dv "And with that came these thoughts... of her."
        dv "I should probably explain."
        dv "Whenever I care about someone, they start appearing a lot in my thoughts... As well as those that aren't really my own."
        dv "She claimed I was \"cold\" towards her... heh..."
        dv "She did everything she could to make me care about her."
        dv "And... it probably worked."
        show rback 3 with dissolve
        dv "Eventually, every time she was close to me I found myself wanting to tear her apart."
        dv "It wasn't very difficult to make me feel that way."
        dv "Thanks to her, I learned that nothing can satisfy me."
        dv "Every time I touched her, it got worse. I wanted even more than I had before."
        dv "Nothing felt fulfilling to me. I was always holding back around her."
        dv "It was like touching the air."
        dv "I felt... trapped. And afraid."
        dv "But of course, she had no idea."
        dv "At some points, I even tried to stop myself from feeling anything at all, but these thoughts... they were still there."
        dv "So..."
        dv "I tried everything. I really did."
        dv "But nothing worked."
        dv "Over the one year when we were together, my illness developed way faster than what I was prepared for."
        dv "Every day, it took more and more willpower to keep seeing her."
        dv "I was bound to break eventually - that much was obvious."
        dv "I... needed some way to prevent that, even if I was trying to put off the inevitable."
        dv "My only hope was that she'd give up on me before I lost it."
        dv "I realized that there was only one person I could hurt without any regret, without consequences."
        show rback 5 with dissolve
        dv "And that person was myself."
        m shock "{i}!!!"
        m angrytalk "Are you saying you've been hurting yourself?"
        dv "Yeah."
        dv "The first time I did it was back in primary school, when my illness was just starting to take shape."
        dv "It demanded so little back then that I could satisfy it without hurting anyone severely. It was the only solution I had."
        dv "I stopped doing it once I saw how harmful it would be to keep doing everything I wanted to."
        dv "But over time, I realized I could cut myself to keep Caroline safe."
        dv "I tried it once, and it worked."
        "He looks at me suddenly."
        dv "I assume you've never done it."
        "I shake my head quickly. Of course I haven't."
        dv "Ughh... how do I explain..?"
        dv "It's not half as satisfying as doing the same to someone else, but it was enough to make me a little less desperate around her."
        dv "I knew it was a temporary solution that would either end with me dead or Caroline hurt, but there was nothing else I could do."
        dv "I made it a habit to spend at least half an hour doing whatever I would think of doing to her to myself instead every day."
        dv "That started about two months before I got here."
        dv "It took a lot of effort not to let her see the marks, but she never noticed..."
        stop music fadeout 5
        dv "At least not until I showed them to her myself."
        hide rback with dissolve
        show dv neutral with dissolve
        m serious "...Do you still hurt yourself?"
        play music "ost/hospital.ogg" fadein 6
        show dv sidetalk with dissolve
        dv "Nope, not a chance. Here, it would be impossible."
        show dv neu with dissolve
        "That's a relief..."
        show dv frusttalk with dissolve
        dv "But I still have some scars left from three years ago. These were... pretty deep cuts."
        show dv sad with dissolve
        "...."
        "I can see that."
        show dv neutalk with dissolve
        dv "You've been oddly quiet today."
        show dv neu with dissolve
        m uncom "I didn't want to disturb you."
        show dv sadsmile with dissolve
        dv "I think you're the one who's disturbed right now."
        show dv siden with dissolve
        m regret "...."
        show dv frusttalk with dissolve
        dv "Hey, I'm sorry. But you asked, and I just told you the truth."
        show dv angry with dissolve
        m neutral "I know."
        show dv sadtalk with dissolve
        dv "I'm not really... used to other people's reactions to all of that."
        show dv sad with dissolve
        m angry "It's fine. I wanted to know, and now I do."
        show dv neutral with dissolve
        m "Well..."
        "I check the time."
        "Shit. My break started five minutes ago."
        m fabtalk "I kept you here for a while today. You should get going."
        show dv neutalk with dissolve
        dv "See you tomorrow, [name]. I should be able to wrap this up in one more session."
        hide dv with dissolve
        hide screen easymeter
        hide screen redmeter
        m smile "Thank you, Michael."
        play sound "doorclose.ogg" fadein 1
        jump breakchoice
    elif day == 10:
        scene bg mc with dissolve
        play music "ost/hospital.ogg" fadein 8
        "I'm in my office earlier than usual today."
        "I still have time before Michael comes here again."
        "Our last session... He told me so much I wasn't expecting."
        "Thinking back to it, all he did makes sense to me in the context of his illness, but I just wouldn't have considered it before... god..."
        "Self-harm? I've only encountered it with suicidal patients so far."
        "But Michael..? I don't think that's the case. It's more that... he enjoys it, in a way?"
        scene bg sun with dissolve
        "By far the strangest thing about his past to me is... {i}why{/i}?"
        "Why didn't he leave that girl if he knew he couldn't be happy with her?"
        "Why did he not tell her the truth? Why did he consider it better to suffer trying to be with her than to stop it?"
        "I suppose I'll learn the answers eventually, once I understand him better."
        "I really hope he can live a normal life someday... Without having to lie to everyone about his problems."
        "He's really sacrificed a lot for that."
        "I don't think he can be fully cured at this point, because these urges will most likely stay in him for the rest of his life..."
        "But maybe there's still hope for him. Maybe I can at least make everything easier for him."
        stop music fadeout 4
        dv "Hello~ Lost in thought?"
        if easymeter:
            show screen easymeter
            show screen redmeter
        show bg mcdesk with dissolve
        show dv smirk with dissolve
        "I notice him already in my office. I get up to close the door."
        play music "ost/neutral.ogg" fadein 8
        m talk "No, not at all. Take a seat."
        show dv neu with dissolve
        m fabtalk "Before I listen to the rest of your story..."
        m angry "I wanted to ask you something."
        show dv neutral with dissolve
        m serious "How do you feel about sharing all this with me? I'll understand if you don't really-"
        show dv angrytalk with dissolve
        dv "No no, I'm fine. Honestly."
        show dv sidetalk with dissolve
        dv "You know, memories are like scars - they only hurt while they're fresh."
        show dv sad with dissolve
        dv "...and if you try to reopen them. That's not pleasant as well."
        show dv frusttalk with dissolve
        dv "Shit, this quote's falling apart..."
        show dv breath with dissolve
        dv "Anyway... You get the idea."
        show dv devil with dissolve
        dv "Besides, I meant it when I said I love answering your questions ~"
        show dv sad with dissolve
        dv "Plus, I'd be more worried about you not being prepared to hear about all of that."
        show dv smirk with dissolve
        dv "...But I guess that's not my problem, so I'll tell you whatever you want me to."
        m sadsmile "I just wanted to make sure you were okay with it."
        show dv sidetalk with dissolve
        dv "Yeah, I get it."
        show dv siden with dissolve
        stop music fadeout 5
        m talk "Alright then..."
        m fabtalk "You mentioned being arrested last Friday. What happened?"
        show dv sidetalk with dissolve
        dv "Well..."
        show rback 4 with dissolve
        play music "ost/memory.ogg" fadein 10
        dv "When I started cutting myself again, things got better between me and Caroline."
        dv "I was actually able to touch her without losing it."
        dv "Unless she did something {i}very{/i} weird and specific, but that almost never happened."
        dv "But... She pointed out a few times that I was getting kind of aggressive."
        dv "I never noticed that... I mean... I guess we had different standards. I never meant her harm."
        dv "But to be honest, sex never really affected me that much, so it wasn't that difficult to stay in control."
        m uncom "I'm sorry for getting off-topic, but-"
        dv "Oh, it's fine. Really."
        m angry "What actually affects you the most? What triggers these thoughts?"
        dv "It's... more psychological, I think. Physical pleasure rarely affects me at all."
        dv "And the things that trigger them... It all depends on the situation, there's a lot of them..."
        dv "Fear. Power. Screams. Blood. Tears. Violence. Anger. Hatred."
        dv "...love."
        dv "And as for touch... it would have to be really specific to trigger anything. I am {i}not{/i} a masochist, mind you." ##check?
        m boretalk "Thank you. Go on, please."
        dv "As time passed, she grew bolder. She made it a habit to always catch me by surprise whenever she could."
        dv "Of course, that didn't work too well with my illness... you can imagine."
        dv "But I managed to adjust to it and for about a month, everything was almost normal, {cps=*2}at least from her point of view."
        dv "I was struggling more than ever before, the cuts were only getting deeper every time she crossed a line."
        dv "I, uh... lost a lot of blood because of them. That caused me all sorts of problems."
        dv "But... she was happy. I think."
        dv "Then, one night..."
        scene black with dissolve
        dv "I just finished treating the newest wounds for the day before going to sleep."
        dv "I had a really weird dream..."
        dv "Uhhh.... it's relevant, I swear."
        dv "I was in Caroline's house."
        dv "I found her in her bedroom."
        dv "She was laying down on her bed, the sheets covering her body."
        dv "I knew it was a dream, so I asked her what she was doing there."
        dv "She was silent. Normally, she was never like this. She wasn't looking at me at all."
        scene rback 6 with dissolve
        dv "Suddenly, she stood up, the sheet covering her falling to the floor. She was naked."
        "I take a deep breath in preparation for whatever direction this may take."
        dv "She walked up to me and said that she knew everything I'm thinking about her. And that it's pointless to hide it from her, because she can tell how I feel."
        dv "She rolled up one of my sleeves to show me all the marks I left on my right arm."
        dv "Oh, you can't tell but I'm left-handed - so I usually cut my right arm. Though the left side is easier to cut on my neck, so..."
        "He pauses."
        dv "The point is, I had the most scars on my right forearm. And I still do."
        dv "In that dream, she looked at me and asked: \"Is this really worth it?\""
        dv "She said that it would be so much easier for me to hurt her the way I've wanted to from the start."
        dv "I couldn't say anything back to her in that dream, so she just kept going."
        dv "The... idea of her knowing about all of that made me feel... really ashamed of that, actually."
        dv "And she was using it to her advantage in that dream."
        dv "Then she got even closer to me suddenly and wrapped her arms around me."
        dv "I can't describe how I felt then... it felt wrong for a reason I don't really know. It just did."
        show rback 0 with dissolve
        dv "And then... I couldn't hear my own thoughts anymore."
        dv "Like I had none."
        dv "All I could hear was a voice in my head telling me to hurt her."
        dv "I was flooded with these thoughts like never before. I had no control over myself."
        dv "All I could see was her blood."
        dv "I'm not even sure if I really hurt her in that dream, or if it was only in my head."
        dv "But these thoughts of murdering her were so strong that I couldn't see or hear anything besides them."
        dv "It never happened to me before, I didn't know what was happening to me..."
        dv "I was... I was scared, [name]. Of whatever I became in that dream."
        dv "When I woke up the next day, I remembered it all perfectly."
        dv "I felt sick that day... I was really pale as well because of all the recent blood loss."
        dv "I looked at myself in the mirror and remembered that dream."
        dv "It felt disgusting. I've had dreams like this before, I constantly have them, but this one was so much different..."
        dv "It was about Caroline."
        show rback 9 with dissolve
        dv "For the first time in a long time, I started cutting myself outside of my usual routine."
        dv "I wanted to punish myself for whatever that dream was."
        dv "I didn't care about anything else. All that mattered to me was that I couldn't hurt Caroline. Ever."
        dv "No matter what could happen to me."
        dv "I started crying. Blood mixed with tears, but I didn't stop. I couldn't."
        dv "Once you start hurting yourself, it becomes addictive. At least for someone like me."
        dv "The worse I felt the more reasons I found to open another wound."
        dv "I didn't know for how long I was laying on the floor, crying."
        dv "I was crying because I felt weak. Worse than her."
        dv "She wasn't going through any of that because she was better than me."
        dv "She wasn't corrupted and broken. I was."
        dv "At that moment I was close to killing myself. If things took a different turn I'd do it without hesitation... not like I could control myself once I started."
        dv "But... Caroline called me."
        dv "I had to get up to answer her."
        dv "She asked me if she could come over for a few days."
        show rback 0 with dissolve
        dv "Uhh... I know it doesn't look that way, but over these past twenty years, I mastered the ability to move on very quickly or at least pretend to."
        dv "I always had to hide my illness from people. I couldn't let them notice that something was wrong."
        dv "So I managed to talk to her normally right after I was about to kill myself and for whatever reason I let her come to my house."
        dv "I think it was about that dream... I wanted to see her again so much... I needed to."
        dv "I was desperate for any company other than the edge of a knife, I think."
        dv "I got rid of all the blood before she got to my house. Another thing I became quite efficient at."
        dv "When she arrived, she told me she had a free week so she'd thought it would be nice to see me again and spend some time with me."
        scene black with dissolve
        dv "Skipping the details, we started making out."
        dv "Somehow, the dream couldn't leave my head. I was seeing her as she appeared there, telling me to just hurt her already..."
        dv "I couldn't stop these thoughts, just like in the dream."
        dv "I was terrified. I had no idea what was happening to me."
        dv "The next thing I saw was her body on the floor."
        scene rback 0 with dissolve
        dv "She was still alive, just unconscious."
        dv "At first, I wanted to help her, but..."
        dv "Seeing her knocked out like that, completely at my mercy... it was too much."
        dv "She picked the single worst day to see me."
        dv "At that moment, all of that pain, the fifteen years of always having to hold back, and my desire for her then, a thought was created."
        dv "I wasn't exactly myself that day, I was borderline delirious - and what remained of my mind that day told me to keep her there - tie her up and hurt her until I've had enough."
        dv "She was mine. Mine to torture and kill."
        scene rback 7 with dissolve
        dv "So at that moment of madness, I took her to the basement and tied her to a chair."
        dv "For the first time, I felt like I could do anything. I had someone who could be used to give these thoughts what they demanded."
        dv "There was no more holding back, and no more thinking."
        dv "I didn't allow myself to question my actions at that time. I couldn't look back, because I knew I would regret it."
        dv "There was only me and the passion. The urge."
        dv "I took a while to clean up all the knives I used for cutting myself before and gathered them in the basement."
        dv "From then I just waited for her to wake up."
        dv "By the time she did, I already considered how much time I had before the police would come looking for her - a whole week, up to two."
        dv "My mind was clear enough by then to give myself one rule: \"don't kill her, no matter how much you want to.\""
        dv "At first, she didn't understand what I did."
        dv "I made myself wait one last time for her to fully comprehend her situation before I told her the truth."
        dv "She was terrified of me."
        dv "I showed her all the cuts I had left, including the fresh ones I didn't have the time to treat."
        dv "I... took one of my knives and walked up to her."
        dv "I was overwhelmed. I didn't know what to do."
        dv "She tried to struggle and break free... obviously."
        dv "I've never seen her more beautiful than at that moment, with tears in her eyes, begging me to let her go."
        show rback 8 with dissolve
        dv "I kissed her, burying the blade in her skin. She screamed."
        dv "The cut wasn't deep at all, but for someone completely untouched their whole life, it was probably painful."
        dv "I knew that tying her up was necessary."
        dv "If she'd tried to run, I would have forgotten about my one rule and killed her before she could leave. I know I would have."
        dv "And since she had very little room for struggling, she couldn't provoke me."
        dv "Knowing that I couldn't kill her under these conditions, I let go. Completely."
        dv "I don't remember much of what happened later, it was like a dream."
        dv "All these feelings eating away at me - I set them free."
        dv "I should've died that morning before she called. I didn't."
        dv "But I couldn't care less. I felt like I died that day. Or at least, a part of me did."
        dv "The one I've always hated so much - my \"conscience\", you could call it."
        "I imagine after 23 years of constantly punishing himself for these thoughts, it would become unbearable."
        "There's only so much a person can take... still, the outcome was rather tragic."
        dv "I really can't go back to the way I was before then. I'm just not the same person anymore."
        dv "I let it all out onto her, because I sincerely stopped caring. About her, or anything else."
        dv "The moment I decided to cut myself that morning, the path was already set before me."
        dv "There was no going back then, and no regret."
        scene black with dissolve
        dv "I don't know for how long I kept her there. I barely remember the police arriving at all."
        dv "Well, they arrested me. But since they noticed I wasn't exactly sane, they sent me here."
        stop music fadeout 6
        dv "And that's it."
        scene bg mcdesk with dissolve
        m regret "...."
        show dv cute with dissolve
        dv "What?"
        show dv frusttalk with dissolve
        dv "If you don't mind, I should be leaving about now."
        show dv angry with dissolve
        m frusttalk "...right."
        hide screen redmeter
        hide screen easymeter
        show dv neutalk with dissolve
        dv "See you tomorrow..? Maybe...?"
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        "He leaves."
        jump breakchoice
    elif day == 11:
        scene bg patients with dissolve
        play sound "footsteps.ogg" fadein 5
        "I'm on my way to my office."
        nn "Hey! Hey, [name]!"
        "I turn my head towards the sound of a familiar voice."
        scene bg closeXV with dissolve
        dv "You're not mad at me after yesterday or anything?"
        show bg closeXV2 with dissolve
        "He's in his room, but I can see him through the door."
        "Before I can reply, I hear another voice from somewhere behind me."
        play music "ost/tension.ogg" fadein 6
        nn "Hey, aren't you the craziest freak here?"
        nn "Burnett, was it?"
        m angrytalk "Tom -!"
        "I forgot his room is right behind me. XVI, I think."
        t "Some patients you got, Hart... I almost feel sorry for you."
        dv "For once I agree."
        t "You have a sharp tongue, don't you?"
        dv "Oh, but I'm just warming up ~"
        t "Something has to make up for your hands, after all."
        "Woah, that's... unfair."
        dv "Hmmm?"
        t "I could've sworn they're long dead under that straitjacket."
        dv "Think again."
        "He touches the glass. I didn't notice before that he's actually free right now."
        dv "I can assure you - these hands are more than capable of things yours have never done."
        t "Excuse me?"
        dv "You look like you haven't been with a woman in fifteen years."
        dv "Or a man, for that matter."
        t "Th-That's none of your business!"
        "Tom retreats further into his room."
        dv "If you're so sensitive, don't start arguments like that, you moron."
        stop music fadeout 5
        m angry "Are you two done yet?"
        "Michael looks at me as if he's just noticed me."
        dv "We are, apparently."
        m fabtalk "I'll see you in a moment, then."
        play sound "footsteps.ogg" fadein 3
        scene bg central with dissolve
        "I make my way to my office quickly."
        "I'm not sure how to feel about what I just saw and heard."
        scene bg mc with dissolve
        "...."
        play music "ost/neutral.ogg" fadein 6
        dv "Hey, I'm back."
        if easymeter:
            show screen easymeter
            show screen redmeter
        scene bg mcdesk with dissolve
        show dv neu with dissolve
        m frust "...."
        show dv angrytalk with dissolve
        dv "Jeez, what was I supposed to do? I'm not the type of person to back out of the only fun there is in this place."
        show dv frusttalk with dissolve
        dv "Also, he started it."
        show dv neutalk with dissolve
        dv "And I don't take kindly to being insulted. I have some dignity."
        show dv neu with dissolve
        m fabtalk "I know, I know..."
        show dv talk with dissolve
        dv "Just letting you know - I meant everything I said."
        show dv neutral with dissolve
        "I was aware of that."
        m talk "Does that happen often here?"
        show dv frusttalk with dissolve
        dv "Maybe once a week, I don't know... The guy from XVI has some issues."
        show dv shock with dissolve
        dv "He's one of your other patients, right? The guy whose name I didn't recognize."
        show dv cute with dissolve
        m boretalk "He is..."
        show dv sidetalk with dissolve
        dv "You mentioned him last week. On Thursday, I think..?"
        show dv siden with dissolve
        m angry "That's right. I'm surprised you remembered it."
        show dv devil with dissolve
        stop music fadeout 6
        dv "I have pretty good memory when it comes to details."
        show dv smirk with dissolve
        m serious "Umm... Do you mind if I refer to what you said yesterday? I didn't get to comment on it then."
        show dv neutalk with dissolve
        play music "ost/hospital.ogg" fadein 8
        dv "Go ahead."
        show dv neutral with dissolve
        m talk "Do you really not regret doing any of that?"
        show dv frusttalk with dissolve
        dv "I haven't \"regretted\" anything in three years."
        show dv sadtalk with dissolve
        dv "I used to blame myself for everything that happened - I stopped doing that already."
        show dv talk with dissolve
        dv "No, I don't regret it - I honestly don't give a fuck anymore."
        show dv neutral with dissolve
        menu:
            "I find that hard to believe":
                $professional+=1
                show dv neutalk with dissolve
                dv "It's the truth."
            "So you've given up?":
                $RedHeart+=1
                show dv talk with dissolve
                dv "Yes, I have. And it's better that way."
                show drk with Dissolve(0.75)
                show r 1 with dissolve
                show r 3 with Dissolve(0.3)
                show r 2 with Dissolve(0.3)
                $renpy.pause(0.75, hard = True)
                hide r with Dissolve(0.5)
                hide drk with dissolve
            "You could have murdered her!":
                $personal+=1
                show dv frust with dissolve
                dv "...and? I knew I wouldn't."
        stop music fadeout 5
        show dv sidetalk with dissolve
        dv "I told you yesterday, I stopped caring the morning I decided to cut myself."
        show dv angrytalk with dissolve
        dv "Why? {i}Why{/i} would I want to care? Tell me."
        show dv angry with dissolve
        play music "ost/tension.ogg" fadein 8
        m regret "...."
        m sadtalk "Because it's pointless to live without caring about anything."
        show dv sidetalk with dissolve
        dv "You think I don't know that? Of course it's pointless - but it's better than how I used to live."
        show dv siden with dissolve
        m angry "Why is that?"
        show dv frust with dissolve
        dv "...."
        show dv sadtalk with dissolve
        dv "...because caring hurts."
        show dv notalk with dissolve
        dv "It hurts, having to always be afraid of being with someone you care about."
        show dv sadtalk with dissolve
        dv "Lying to them and telling yourself it's for the best."
        show dv angrytalk with dissolve
        dv "Always wanting more than you can ever have."
        show dv noeyes with dissolve
        dv "Caring is my curse, [name]. I care too much."
        show dv notalk with dissolve
        dv "So it's easier to stop caring at all."
        show dv kh with dissolve
        dv "[name]..."
        show dv darktalk with dissolve
        dv "I'm still lying to myself."
        show dv kh2 with dissolve
        dv "...when I say I don't care."
        show dv noeyes with dissolve
        dv "I have to constantly stop myself from caring."
        show dv notalk with dissolve
        dv "I used to not let myself hurt her because I cared too much... but now I'm not letting myself care so it doesn't happen again."
        show dv sadtalk with dissolve
        dv "And it hurts as well..."
        show dv noeyes with dissolve
        dv "I want to care... but if I start caring again, all I'll feel is guilt."
        show dv angrytalk with dissolve
        dv "I don't want that..."
        show dv angry with dissolve
        "I never realized any of that..."
        menu:
            "And you don't care now?":
                show dv sadtalk with dissolve
                dv "...I can't."
                show dv angry with dissolve
                dv "I don't want to care if it only brings me pain."
            "How can you care \"too much\"?":
                show dv sadtalk with dissolve
                dv "With Caroline, I... I couldn't stop thinking about her. Consciously and otherwise."
                show dv frusttalk with dissolve
                dv "I couldn't do anything on my own."
                show dv angrytalk with dissolve
                dv "She was always there... and being with her changed nothing."
                show dv frusttalk with dissolve
                dv "I always wanted more from her."
                show dv sadtalk with dissolve
                dv "I can't care like that ever again."
                show dv notalk with dissolve
                dv "I can't."
            "So you could make yourself care again?":
                show dv neutalk with dissolve
                dv "I could, just like anyone with a knife in their hand could kill themselves."
                show dv angrytalk with dissolve
                dv "But I can't. I won't."
        show dv angry with dissolve
        m serious "Do you think... anything could make you willing to care again?"
        show dv gasp with dissolve
        dv "What?"
        show dv dark with dissolve
        m talk "Maybe if you started caring, you could have a chance to leave this place."
        show dv shock with dissolve
        dv "No, that's..."
        show dv angrytalk with dissolve
        dv "That's impossible."
        show dv frust with dissolve
        m gasp "How do you know?"
        show dv frusttalk with dissolve
        stop music fadeout 6
        dv "I've tried everything already. It won't work."
        show dv angry with dissolve
        m regrettalk "Think about it, please. This may be the only way for me to help you."
        show dv neutral with dissolve
        "He nods in silence."
        play music "ost/neutral.ogg" fadein 8
        m fabtalk "...oh. I wanted to ask you something else."
        show dv neu with dissolve
        m talk "What happened to Caroline after all of that?"
        show dv sad with dissolve
        dv "...."
        show dv frusttalk with dissolve
        dv "...I don't know."
        show dv neutalk with dissolve
        dv "She's still alive for sure. I didn't hurt her severely enough to kill her."
        show dv neutral with dissolve
        m fabtalk "So she never made any attempt at contacting you?"
        show dv frusttalk with dissolve
        dv "I don't think anyone would after what happened."
        show dv talk with dissolve
        dv "I could tell she was freaked out when I told her about my illness. She would've left me even if I hadn't hurt her."
        show dv neutral with dissolve
        m regrettalk "I understand."
        m angry "Though I can't see why your illness alone would bother her so much if you managed to never hurt her."
        show dv sad with dissolve
        m uncom "It wouldn't be a threat to her if it was treated properly beforehand."
        show dv frust with dissolve
        dv "...."
        m talk "Do you think she still lives here?"
        show dv talk with dissolve
        stop music fadeout 5
        dv "As far as I know, she has nowhere else to go. Why do you-"
        show dv angry with dissolve
        dv "{i}Wait."
        show dv frusttalk with dissolve
        dv "You're not actually planning to find her, right?"
        play music "ost/hospital.ogg" fadein 6
        show dv neutral with dissolve
        m fabtalk "If it's possible, I'd like to hear her take on what happened."
        m conf "It would help me understand you better."
        show dv sadtalk with dissolve
        dv "If you say so..."
        show dv frust with dissolve
        "He gives me all the information I need to find her, including where she lived three years ago."
        show dv neutalk with dissolve
        dv "Good luck, I guess."
        show dv neu with dissolve
        m talk "I'll try to dig into that this weekend."
        "We still have some time left."
        m uncom "When you got here, did it take you long to get used to being restrained like that?"
        show dv talk with dissolve
        dv "No, not at all, actually."
        show dv sidetalk with dissolve
        dv "In a way, it's pleasant to know that I can't hurt anyone."
        show dv frust with dissolve
        dv "Being tied up like this makes it easier for me stop trying to struggle with these thoughts."
        show dv sidetalk with dissolve
        dv "They're still there, but I don't care because I know they can't affect anything."
        show dv talk with dissolve
        dv "So you could say the staff here is doing me a favor by making it easier for me to give up."
        show dv siden with dissolve
        "I'm not sure if that's a good thing... if it makes him lazier in fighting his illness on his own."
        show dv frust with dissolve
        m gasp "So it doesn't bother you at all to be that way?"
        show dv neutalk with dissolve
        dv "Uhh, that depends... most of the time it doesn't."
        show dv noeyes with dissolve
        stop music fadeout 4
        "He looks at me with an unreadable expression."
        show dv kh with dissolve
        dv "But there are times when I wish I were free."
        show dv noeyes with dissolve
        m fabtalk "What do you mean?"
        show dv darkblush with dissolve
        dv "N-Nothing -"
        play music "ost/neutral.ogg" fadein 6
        show dv smile with dissolve
        dv "Nothing in particular, [name] ~"
        show dv sidesmile with dissolve
        "His laugh is so adorable..."
        "{i}Wait, what?"
        show dv neu with dissolve
        m talk "You should get going now."
        show dv talk with dissolve
        dv "You're right."
        hide screen redmeter
        hide screen easymeter
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        "He leaves in a hurry. I'm not sure what just happened."
        jump breakchoice
    elif day == 12:
        scene bg mc with dissolve
        "It's Friday. I need to try and come up with a way to help him soon."
        m flirt "Hi ~"
        play music "ost/neutral.ogg" fadein 8
        scene bg mcdesk with dissolve
        show dv smile with dissolve
        "He greets me as well and takes a seat."
        show dv sidetalk with dissolve
        dv "Soo... What are we doing today?"
        if easymeter:
            show screen easymeter
            show screen redmeter
        show dv neu with dissolve
        m angry "...I've been thinking... about ways to help you."
        show dv shock with dissolve
        dv "Wait, you don't actually mean \"help\" as in \'get me out of this place\'?"
        show dv cute with dissolve
        m fabtalk "That's the plan."
        show dv breath with dissolve
        "He takes a deep breath."
        show dv angrytalk with dissolve
        dv "Alright... but how do you plan to accomplish that?"
        show dv angry with dissolve
        m talk "That's exactly what I want to figure out."
        show dv breath with dissolve
        dv "Ah."
        show dv sidetalk with dissolve
        dv "I can answer some questions if that helps you..."
        show dv neu with dissolve
        "...."
        m uncom "Last time you said that being restrained makes it easier for you to give up struggling with these thoughts."
        show dv neutalk with dissolve
        dv "In a way, yeah."
        show dv neutral with dissolve
        m angry "Could you describe how exactly being like this affects your illness?"
        show dv talk with dissolve
        dv "Uhh... it kind of... tames everything."
        show dv frusttalk with dissolve
        dv "Muffles, I guess."
        show dv sidetalk with dissolve
        dv "Everyone tends to avoid me here and since I can't touch anyone anymore, and I have no doubt about not being able to free myself, the urge to hurt anyone is really... irrelevant."
        show dv cute with dissolve
        stop music fadeout 5
        "I lean in a bit and look straight into his eye."
        m uncom "How about now? Do you want to hurt me?"
        show dv noeyes with dissolve
        "His head twitches."
        show dv darktalk with dissolve
        dv "Hurt... you?"
        show dv kh2 with dissolve
        dv "I..."
        play music "ost/hospital.ogg" fadein 8
        show dv notalk with dissolve
        dv "Why did you ask me that?"
        show dv noeyes with dissolve
        m angry "Because I need to know."
        show dv breath with dissolve
        "He inhales slowly."
        show dv notalk with dissolve
        dv "You made me... think about it... so now I do."
        show dv frust with dissolve
        m neu "I see."
        show dv talk with dissolve
        dv "But... it's barely there."
        show dv notalk with dissolve
        dv "If I were free it would be much... much worse, I can assure you."
        show dv kh with dissolve
        "If he were free..."
        m fabtalk "Would you be able to control yourself if you were free now?"
        show dv sadtalk with dissolve
        dv "I can't tell... I was never free here when..."
        show dv neutral with dissolve
        "He looks at me."
        show dv frusttalk with dissolve
        dv "Someone else was with me."
        show dv frust with dissolve
        m regrettalk "That... may have been a mistake."
        show dv angrytalk with dissolve
        dv "What do you mean?"
        show dv angry with dissolve
        m fabtalk "If they tried to make you more comfortable with the things that trigger these thoughts instead of attempting to stop them completely, you wouldn't be so desperate now."
        "I think I'm going in the right direction with this."
        m frust "You say you're not prepared to be freed because you'd be overwhelmed - so your psychologist's objective should be to try and prepare you for that."
        show dv shock with dissolve
        dv "What -?"
        stop music fadeout 6
        show dv notalk with dissolve
        dv "How would they do that?"
        show dv noeyes with dissolve
        m fabtalk "I think..."
        m talk "The only way to to do it is the..."
        show dv dark with dissolve
        m neu "...practical. one."
        play music "ost/tension.ogg" fadein 10
        "Even I am stunned by this conclusion."
        show dv darktalk with dissolve
        dv "You're not... actually saying that..?"
        show dv kh with dissolve
        menu:
            "I mean it":
                $RedHeart+=1
                show drk with Dissolve(0.75)
                show r 1 with dissolve
                show r 3 with Dissolve(0.3)
                show r 2 with Dissolve(0.3)
                $renpy.pause(0.75, hard = True)
                hide r with Dissolve(0.5)
                hide drk with dissolve
                show dv frusttalk with dissolve
                dv "No... no, you can't do that."
                show dv angrytalk with dissolve
                dv "I won't let you."
                show dv angry with dissolve
                m gasp "Why? You'll never learn to control yourself if you never try."
                show dv frust with dissolve
                m sadtalk "If you keep giving up you'll never be able to live a normal life!"
                show dv notalk with dissolve
                dv "But it's not about me!"
                show dv moment with dissolve
                "I get back a little out of instinct."
                show dv pant with dissolve
                dv "I'll... I'll hurt you..."
                show dv moment with dissolve
                m talk "And how does that make you feel?"
                show dv kh with dissolve
                dv "...."
                show dv notalk with dissolve
                dv "I don't... know..."
                show dv sadtalk with dissolve
                dv "It's like my mind is tied up as well... Nothing makes sense anymore."
                show dv noeyes with dissolve
                m conf "I understand. You don't have to answer all of my questions."
                show dv notalk with dissolve
                dv "I want to... but I just don't know."
                show dv dark with dissolve
                m serious "Maybe... if you were free, it would be clearer for you."
                show dv darktalk with dissolve
                dv "It would, but... I don't want that."
                show dv kh2 with dissolve
                dv "If you set me free, I'll have to start feeling things again to keep myself from hurting you."
                show dv sadtalk with dissolve
                dv "[name]... don't do this to me... I'm not ready for any of that."
                show dv sad with dissolve
                menu:
                    "It's the only way":
                        $RedHeart+=1
                        $dominant+=1
                        show drk with Dissolve(0.75)
                        show r 1 with dissolve
                        show r 3 with Dissolve(0.3)
                        show r 2 with Dissolve(0.3)
                        $renpy.pause(0.75, hard = True)
                        hide r with Dissolve(0.5)
                        hide drk with dissolve
                        m angrytalk "No matter how much we try, the psychologists can't help you on their own."
                        show dv angry with dissolve
                        m angry "You need a reason to want to keep struggling with it."
                        m uncom "You need to fight it on your own. All I can do is support you in every way possible."
                        show dv sadtalk with dissolve
                        dv "It's not worth it..."
                        show dv kh2 with dissolve
                        dv "I'm not worth any of that, [name]."
                        show dv dark with dissolve
                        m angrytalk "Don't say that. You deserve to be helped, just like everyone else here."
                        show dv notalk with dissolve
                        dv "I don't think everyone here's done the things that I've done..."
                        show dv frust with dissolve
                        m angrytalk "You've been suffering your whole life because of this illness. I won't let this go on."
                        m serious "I'm going to save you - but I need your help."
                        show dv moment with dissolve
                        "I get up from my chair and put my hands on the desk."
                        show dv angry with dissolve
                        m sadtalk "Do you believe me when I say I can help you?"
                        show dv kh with dissolve
                        dv "...."
                        show dv angrytalk with dissolve
                        dv "I don't. It's impossible."
                        show dv frusttalk with dissolve
                        dv "You're not the first to try that..."
                        show dv kh2 with dissolve
                        "I bend down over my desk until my face is inches away from his."
                        show dv noeyes with dissolve
                        m frust "I'm not going to give up on you like they have."
                        show dv frusttalk with dissolve
                        dv "You're going to keep trying until you regret it. And then you'll give up."
                        show dv kh with dissolve
                        dv "Or die."
                        show dv frust with dissolve
                        m angry "I won't."
                        "And I can prove it. But is this the right time..?"
                        menu:
                            "{color=#bc0b17}FREE HIM":
                                $RedHeart+=1
                                $dominant+=2
                                show drk with Dissolve(0.75)
                                show r 1 with dissolve
                                show r 3 with Dissolve(0.3)
                                show r 2 with Dissolve(0.3)
                                $renpy.pause(0.75, hard = True)
                                hide r with Dissolve(0.5)
                                hide drk with dissolve
                                scene bg mcdark with dissolve
                                "I make my way to his side of my desk and take a deep breath."
                                stop music fadeout 6
                                "I'm really going to free him now."
                                "Looking for a way to untie him, I slowly place my hands on his back."
                                scene devil1
                                play music "ost/fight.ogg" fadein 6
                                "He seems really anxious."
                                dv "What are you doing -?"
                                m angry "Freeing you."
                                dv "[name], stop and listen to me for once."
                                "I obey his request."
                                dv "Do you even realize what you're doing? There's a reason why I'm always like this."
                                m talk "I know."
                                dv "And you don't care about the consequences?"
                                m angry "I care about helping you more, and this is the only way."
                                dv "But... this isn't right, [name]..."
                                dv "I don't want to hurt you... and I know I will."
                                m regrettalk "I won't let you. You trust me, right?"
                                dv "Not with this."
                                dv "You don't even know what I'm capable of."
                                m fabtalk "That's why I need to find out."
                                dv "...."
                                show drk with dissolve
                                dv "[name], don't do this..."
                                dv "I'll beg you if I have to."
                                "He sounds really desperate."
                                menu:
                                    "Free him":
                                        $dominant +=2
                                        "I promised I wouldn't give up, no matter how much he tempts me not to."
                                    "Wait":
                                        $dominant+=1
                                        m neu "...."
                                        dv "Please, [name]... don't do this to yourself..."
                                        dv "Seriously, I'll do anything, just don't let me hurt you..."
                                    "Obey him":
                                        $submissive+=2
                                        stop music fadeout 5
                                        m regrettalk "If that's what you want..."
                                        "I let go of him and move back to my chair."
                                        play music "ost/hospital.ogg" fadein 8
                                        jump devilinchains
                                $DevilFreed = True
                                scene bg mcdeskdark with dissolve
                                "I set him free at last and quickly get back to my side of the desk."
                                show dv bnoeyes with dissolve
                                stop music fadeout 4
                                "He's speechless for a moment."
                                show dv bnotalk with dissolve
                                dv "Did you... really just..?"
                                show dv bkh with dissolve
                                "I nod."
                                play music "ost/tension.ogg" fadein 8
                                show dv bdark with dissolve
                                "I decide to give him a moment to recover from the initial shock."
                                show bg mcdesk with dissolve
                                show dv bsiden with dissolve
                                "He looks around my office, as if he's seeing it for the first time."
                                show dv bfrust with dissolve
                                "I notice that he carefully avoids looking at me and instead fixes his gaze somewhere on the floor after a while."
                                m uncom "Michael..."
                                show dv bkh2 with dissolve
                                "His head twitches ever so slightly."
                                show dv bfrusttalk with dissolve
                                dv "Um... try not to use my name when I'm like this."
                                show dv bsadtalk with dissolve
                                dv "It... makes everything more difficult."
                                show dv bfrust with dissolve
                                m neu "Alright. I won't."
                                "Maybe I shouldn't stare at him for too long. It might bother him as well."
                                m talk "How do you feel now?"
                                show dv bsadtalk with dissolve
                                dv "I... I don't know..."
                                show dv bnotalk with dissolve
                                dv "It feels really strange."
                                show dv bnoeyes with dissolve
                                "He doesn't quite know what to do with his hands."
                                show dv bkh with dissolve
                                dv "I'm... trying not to think too much."
                                show dv bsad with dissolve
                                m conf "There's nothing to worry about."
                                show dv bsadsmile with dissolve
                                dv "H-Heh... Maybe not in {i}your{/i} head..."
                                show dv bnoeyes with dissolve
                                "He closes his eyes in an attempt to calm down."
                                m serious "Is it worse than before you got here?"
                                show dv bkh2 with dissolve
                                "He nods slowly, uncertainly."
                                m sadtalk "I'm sorry-"
                                show dv bangrytalk with dissolve
                                dv "You should be."
                                show dv bangry with dissolve
                                m angry "I'm doing it to help you."
                                show dv bsadtalk with dissolve
                                dv "I know."
                                show dv bangry with dissolve
                                m gasp "Is there anything I can do?"
                                show dv bdark with dissolve
                                dv "...."
                                show dv bfrusttalk with dissolve
                                dv "No."
                                show dv bfrust with dissolve
                                dv "Give me a moment..."
                                show dv bsadtalk with dissolve
                                dv "I need to... calm down..."
                                show dv bsad with dissolve
                                m conf "No problem. We have time."
                                show dv bkh with dissolve
                                dv "You're so... considerate, [name]..."
                                show dv bhes with dissolve
                                m "I'm only doing what everyone should've done from the start."
                                show dv bfrusttalk with dissolve
                                dv "Well... nobody did..."
                                show dv bsadtalk with dissolve
                                dv "I was expecting you to... ask me things..."
                                show dv bneutalk with dissolve
                                dv "But... you're waiting..."
                                show dv bfrust with dissolve
                                m cute "I am."
                                show dv bsadsmile with dissolve
                                dv "...thank you."
                                play music "ost/fight.ogg" fadein 8
                                show bg mcdeskdark with hpunch
                                show dv bdarktalk with dissolve
                                dv "{i}...gah-!"
                                show dv bkh2 with dissolve
                                "His head twitches violently."
                                show dv bnotalk with dissolve
                                dv "...[name]. Get away from me... please..."
                                scene mcshock
                                "I get up from my chair and move as far back as I can until my back is against the window behind me."
                                "He looks at me, panicked, and his head falls onto my desk suddenly."
                                "He's shaking."
                                show drk with dissolve
                                dv "I won't... I can't hurt you..."
                                "I can't see his face."
                                dv "I don't trust myself anymore, [name]..."
                                dv "Not after what I did to Caroline."
                                dv "Oh god... "
                                dv "It's all coming back to me now..."
                                dv "She'll never forgive me, will she..? She can't..."
                                dv "Caroline..."
                                dv "...what have I done?"
                                m sad "What happened isn't your fault."
                                dv "...no."
                                dv "You're lying... that can't be true..."
                                m angry "I'm not."
                                "He looks at me suddenly."
                                show bg mcdeskdark with dissolve
                                show dv bkh with dissolve
                                dv "[name]... [name]... [name]..."
                                show dv bdarktalk with dissolve
                                dv "I'm so sorry!"
                                show dv bnoeyes with dissolve
                                stop music fadeout 5
                                dv "I can't... It's too much..."
                                show bg mcdesk with dissolve
                                m angry "I didn't expect you to win against it yet."
                                play music "ost/tension.ogg" fadein 6
                                show dv bsad with dissolve
                                m serious "It will take time, but I need you to keep struggling. Please."
                                m angrytalk "If you don't, your only chance to get out of this place will be gone forever."
                                show dv bangry with dissolve
                                m frust "I meant it when I said I'm going to save you."
                                show dv bsadtalk with dissolve
                                dv "[name]..."
                                show dv bfrusttalk with dissolve
                                dv "[name], you..."
                                show dv bsadsmile with dissolve
                                dv "...You're so kind to me..."
                                show dv bkh with dissolve
                                dv "I'm... sorry that... I'm not worth it..."
                                "I can't go on like this."
                                "I sit down in my chair again and look straight at him."
                                m angry "Michael."
                                show dv bdark with dissolve
                                "He looks back at me suddenly."
                                show dv bkh2 with dissolve
                                m sadtalk "You're worth that and more. That's why I'm going to keep freeing you every day until you feel comfortable with it."
                                show dv bsadtalk with dissolve
                                dv "You... You shouldn't..."
                                show dv bfrusttalk with dissolve
                                dv "No, don't do that again..."
                                show dv bfrust with dissolve
                                m talk "I will. It's for your own good."
                                show dv bnoeyes with dissolve
                                dv "...."
                                m angrytalk "I'm taking full responsibility for what happens from now on."
                                m serious "So if I get hurt, it's my fault for freeing you. Alright?"
                                show dv bneutral with dissolve
                                "He nods slowly."
                                stop music fadeout 7
                                m neu "Don't worry about anything."
                                show dv bdevil with dissolve
                                dv "Yeah, like I'm not going to spend the whole weekend thinking about it now..."
                                show dv bneutral with dissolve
                                m uncom "I'm really sorry that I can't stay with you for the weekend to support you - I'll be back before you know it."
                                show dv bhes with dissolve
                                dv "I hope so..."
                                play music "ost/neutral.ogg" fadein 8
                                show dv bsiden with dissolve
                                "He looks around for a moment."
                                show dv bneutalk with dissolve
                                dv "Uh, now that I'm calmer, I have to say - it's kind of cold in here."
                                show dv bneutral with dissolve
                                m gasp "Cold?"
                                "I mean... I do tend to open the windows sometimes in the morning before I meet anyone just to let some fresh air in, but... it never occured to me."
                                show dv bfrusttalk with dissolve
                                dv "Yeah. I'll rethink my outfit choice next time if you're going to... free me... again."
                                show dv bangry with dissolve
                                "He glares at me quickly."
                                show dv btalk with dissolve
                                dv "Are you... okay?"
                                show dv bneutral with dissolve
                                m conf "Mhm. Absolutely."
                                show dv bsadtalk with dissolve
                                dv "And you're fine with me being... like this?"
                                show dv bangry with dissolve
                                "I nod."
                                show dv bshock with dissolve
                                dv "So you're not... scared? At all?"
                                show dv bcute with dissolve
                                m flirt "Nope."
                                show dv bsidetalk with dissolve
                                dv "Even after hearing what I told you about my past?"
                                show dv bfrust with dissolve
                                m cute "Even after that."
                                stop music fadeout 4
                                show dv bsadsmile with dissolve
                                dv "[name], there must be something seriously wrong with you if you don't feel threatened right now."
                                play music "ost/tension.ogg" fadein 6
                                show dv bhes with dissolve
                                dv "I mean... I could..."
                                show dv bmoment with dissolve
                                "He reaches out with his hand for the first time, but stops suddenly."
                                show dv bkh2 with dissolve
                                dv "I could... touch you... like this..."
                                show dv bpant with dissolve
                                "He gets away from me suddenly."
                                show dv bfrusttalk with dissolve
                                stop music fadeout 4
                                dv "I'm sorry. I should be going now."
                                show dv bsad with dissolve
                                "I check the time quickly. My break is nearly over."
                                show dv bsadtalk with dissolve
                                dv "Sorry about taking up your break."
                                scene bg mc with dissolve
                                "He gets up in a hurry and it only takes me a moment to restrain him again."
                                m talk "I'll see you on Monday, Michael."
                                hide screen redmeter
                                hide screen easymeter
                                dv "Yeah... see you then."
                                play sound "doorclose.ogg" fadein 1
                                "He leaves, clearly shaken."
                                play music "ost/hospital.ogg" fadein 6
                                "I feel so strange... I'm glad he managed not to hurt me, and even refrained from touching me in any way."
                                "But at the same time, I feel like I've done something wrong."
                                "I know I'll need to keep what happened today a secret from the rest of the staff here, even if I feel like it's the right thing to do."
                                "I'm helping Michael... I don't care for the consequences."
                                "As long as I get to save him, it's all worth it to me. No matter if he hurts me in the process."
                                jump patientchoice
                            "{color=#bc0b17}DON'T":
                                stop music fadeout 4
                                "I shouldn't rush it... It wouldn't be very wise."
                                pause 1
                                play music "ost/hospital.ogg" fadein 8
                                jump devilinchains
                    "You're right":
                        stop music fadeout 5
                        show dv hes with dissolve
                        "He falls back onto his chair."
                        show dv sadsmile with dissolve
                        play music "ost/hospital.ogg" fadein 8
                        dv "Thank you..."
                        jump devilinchains
            "That's just theoretical":
                stop music fadeout 5
                show dv neutalk with dissolve
                dv "Oh. Alright."
                show dv sadsmile with dissolve
                dv "[name], you almost gave me a heart attack..."
                play music "ost/hospital.ogg" fadein 8
                show dv sidesmile with dissolve
                "He laughs."
                jump devilinchains
    elif day == 13:
        if DevilFreed:
            scene black with dissolve
            "Was... was that a nightmare..?"
            play music "ost/emo.ogg" fadein 5
            "I... can't exactly remember what I saw, but... it felt so... odd."
            "I must've been more affected by freeing him than I thought."
            "...."
            "...it'll be fine, right?"
            stop music fadeout 5
            "I can't distract myself with a dream like that. I have things to do."
        jump carolineweekend
    elif day == 14:
        jump nextday
##########################         
    elif day == 15:
        if DevilFreed:
            scene bg mc with dissolve
            play music "ost/neutral.ogg" fadein 6
            "I'm back at the hospital."
            "I plan to keep my promise and release Michael today for the second time."
            "Last time things got... messy towards the end, but overall I'm really proud of him for controlling himself enough not to hurt me."
            "I wonder if he'll be more comfortable today than he was on Friday."
            "He enters my office."
            dv "Hey, it's me again."
            if easymeter:
                show screen easymeter
                show screen redmeter
            m conf "Hi."
            show drk with dissolve
            "He doesn't sit down as usual. Instead, he glares at me nervously."
            dv "So... are you really going to free me?"
            stop music fadeout 4
            "I nod and walk up to him."
            dv "Wait-"
            "I freeze."
            dv "...."
            dv "How do you know I'm wearing anything underneath?"
            play music "ost/sunny.ogg" fadein 6
            m fabtalk "You are, right?"
            dv "Of course I am..."
            dv "...Or am I?"
            "I inhale loudly."
            m frusttalk "You may have just found my only weakness. Congrats."
            "He managed to make me ever so slightly uncomfortable."
            dv "Hell yes ~!"
            m talk "But I won't fall for that... I'm still going to free you."
            dv "Shit..."
            stop music fadeout 5
            m fabtalk "Are you ready?"
            dv "Nope."
            dv "But I guess it won't be any better."
            hide drk with dissolve
            play music "ost/hospital.ogg" fadein 8
            "I set him free again."
            scene bg mcdesk with dissolve
            show dv rneu with dissolve
            "Yesterday I didn't really get the chance to just talk to him more calmly or ask him anything."
            "I hope today we can start over a little."
            m serious "How do you feel today?"
            show dv rsidetalk with dissolve
            dv "Umm... a bit better than last time."
            show dv rfrusttalk with dissolve
            dv "I had to, uh... rethink all that... over the weekend."
            show dv rangry with dissolve
            "I've already noticed he seems much more tense whenever he isn't restrained around me. It's understandable."
            m talk "Did you come to any conclusions, then?"
            show dv rtalk with dissolve
            dv "Yes."
            show dv rsadtalk with dissolve
            dv "I... I really hate the thought of hurting you in some way."
            show dv rneutalk with dissolve
            dv "But, if it happens, I can't quite blame myself - it's your irresponsibility that's at fault."
            show dv rneu with dissolve
            m fab "Fair enough. That's what I said last time."
            "He nods."
            show dv rsidetalk with dissolve
            dv "I also... thought a lot about Caroline... and about what I've done."
            show dv rsiden with dissolve
            "I remember last Saturday."
            stop music fadeout 5
            m talk "I found her."
            show dv rgasp with dissolve
            dv "You... you did?"
            show dv rshock with dissolve
            dv "What did she say?"
            show dv rcute with dissolve
            m fabtalk "That she doesn't want anything to do with you and that I should get lost."
            play music "ost/sunny.ogg" fadein 6
            show dv rdevil with dissolve
            "He laughs."
            show dv rsmirk with dissolve
            dv "That's... that actually seems very much like her."
            show dv rgasp with dissolve
            dv "Oh my god... I can't believe you two've really met..."
            show dv rcute with dissolve
            "I'm glad the news made him a bit more relaxed, at least."
            show dv rsmile with dissolve
            "Even if I haven't learned much, he seems distracted enough to be comfortable around me."
            show dv rneutalk with dissolve
            dv "So... how was she?"
            show dv rneutral with dissolve
            m frust "I only saw her for maybe a minute, but..."
            "I bite my tongue before I can say anything too personal."
            m talk "Honestly, she didn't seem too nice..."
            show dv rfrusttalk with dissolve
            dv "Yeah, she really isn't... now that I think about it."
            show dv rcute with dissolve
            dv "Well, we all make mistakes ~"
            show dv rsmile with dissolve
            m boretalk "I guess that's one way to put it..."
            stop music fadeout 6
            "There's a moment of silence before he speaks up again."
            show dv rfrusttalk with dissolve
            dv "Listen, I... I realized one other thing."
            show dv rfrust with dissolve
            m neu "What is it?"
            play music "ost/tension.ogg" fadein 6
            show dv rkh with dissolve
            dv "I... I care... about you."
            show dv rdarktalk with dissolve
            dv "More than I do about anyone else here."
            show dv rkh2 with dissolve
            dv "Hell, more than I did about Caroline!"
            show dv rnoeyes with dissolve
            "I get back, away from him."
            "I don't know how to respond to that... It's so sudden."
            show dv rsadtalk with dissolve
            dv "I just... don't want to hurt you so much..."
            show dv rnotalk with dissolve
            dv "I don't care about anyone else, but you... you don't deserve it..."
            show dv rkh with dissolve
            menu:
                "Thank you":
                    $personal+=1
                    show dv rsadsmile with dissolve
                    dv "I really don't think... you should be grateful for that..."
                "How can you say that?":
                    $professional+=1
                    show dv rangrytalk with dissolve
                    dv "...I mean it."
                    show dv rnotalk with dissolve
                    dv "I wouldn't care if I hurt anyone other than you."
                "Nobody deserves it":
                    show dv rnotalk with dissolve
                    dv "I... I meant that..."
                    show dv rkh2 with dissolve
                    dv "You're more than that, [name]. You just are."
            show dv rnoeyes with dissolve
            dv "...."
            show dv rfrusttalk with dissolve
            dv "I just... wanted to let you know. I don't really care what you think of that."
            show dv rsad with dissolve
            dv "And I'll get it if... I mean absolutely nothing... to you."
            show dv rangrytalk with dissolve
            dv "Don't worry, I understand that not everyone is like me... like... this."
            show dv rsadtalk with dissolve
            dv "And you probably aren't even capable of caring about someone after two weeks, but..."
            show dv rangry with dissolve
            dv "I am. And it's just the way I feel."
            show dv rsidetalk with dissolve
            dv "I only realized that after overthinking last Friday for way too long... and what I thought... about you then."
            show dv rangrytalk with dissolve
            stop music fadeout 6
            dv "I think... the thoughts of you are only going to get worse the more time I'm allowed to be with you like this."
            show dv rneutral with dissolve
            "He pauses."
            show dv rneutalk with dissolve
            dv "There, I said it. I haven't been this honest in a while."
            play music "ost/tran.ogg" fadein 5
            show dv rsiden with dissolve
            m fabtalk "I'm... glad you're so open about this..."
            "I'm not sure what else to say to that."
            show dv rdevil with dissolve
            dv "Really, you should be proud of yourself. I don't think I've ever talked like this to anyone."
            show dv rneutalk with dissolve
            dv "And once I got here, nobody was really that... inviting, I guess."
            show dv rtalk with dissolve
            dv "There was always this weird sense of hostility I got from the doctors before you."
            show dv rdevil with dissolve
            dv "Like they just wanted to get away from me."
            show dv rsidetalk with dissolve
            dv "So none of them ever got this far with me..."
            show dv rneu with dissolve
            "I smile at him."
            m conf "It's only because I got you to cooperate. You're the one who did all the work."
            show dv rsidesmile with dissolve
            dv "Heh, maybe..."
            show dv rfrust with dissolve
            "He keeps fidgeting in his chair."
            stop music fadeout 5
            show dv rsad with dissolve
            "Suddenly, he flinches and a pained expression passes through his face for a brief moment."
            show dv rneutral with dissolve
            m gasp "What's wrong?"
            show dv rhes with dissolve
            dv "It's nothing..."
            play music "ost/tension.ogg" fadein 6
            show dv rangry with dissolve
            "He looks at me, a burning intensity in his gaze."
            show dv rfrust with dissolve
            "Suddenly, he withdraws his hands from my desk."
            "Wait... his hands..."
            "I have a feeling that I know exactly what's going on."
            m angry "Michael. Could you put your hands back on the desk?"
            show dv rnoeyes with dissolve
            "He freezes momentarily, but obeys my request."
            show dv rneutral with dissolve
            m fab "I just need to confirm something."
            menu:
                "{color=#bc0b17}Check his right arm":
                    $DevilShip=True
                    show dv rneu with dissolve
                    "I lean in and reach out with my hand slowly."
                    m fabtalk "May I?"
                    show dv rtalk with dissolve
                    dv "Yeah, go on."
                    show dv rdevil with dissolve
                    dv "...Like I have a choice..."
                    show dv rfrust with dissolve
                    show drk with dissolve
                    stop music fadeout 6
                    "I carefully place my hands around his wrist and roll his sleeve up to his elbow."
                    "I freeze."
                    "His skin is covered with marks."
                    play music "ost/emo.ogg" fadein 8
                    scene mcshock
                    "Dozens of old scars, one over the other, too many to even fit on the small amount of space."
                    "Way too many for one person."
                    "I can see some which appear particularly old, and must've grown along with his skin. So they must be from childhood."
                    "His wrist is a particularly unpleasant sight. It looks way too butchered for his hand to even work properly."
                    "But by far the worst thing I'm seeing right now are the fresh marks."
                    "A couple of relatively small bruises, nasty-looking scratches and even teeth marks which all must've been made a few days ago at most."
                    "They're all completely untouched - obviously, he had no way of treating these without alerting the staff."
                    "If he never treated these, some of them must've been bleeding for a while."
                    "Why would he do this to himself now..?"
                    "I keep my hands on his arm, careful not to hurt him any more than he's already hurt himself, but not letting him hide this from me again."
                    scene mcdark with dissolve
                    m sad "Michael... Just tell me why."
                    show dv rneu with dissolve
                    "He looks at me slowly, devoid of emotion."
                    stop music fadeout 5
                    show dv rneutalk with dissolve
                    dv "Why? Why did I do it?"
                    show dv rsidetalk with dissolve
                    dv "Isn't it obvious?"
                    show dv rfrust with dissolve
                    m serious "What do you mean?"
                    play music "ost/tension.ogg" fadein 6
                    show dv rtalk with dissolve
                    dv "It's because of you, [name]. I did this to protect you from myself."
                    show dv rneu with dissolve
                    show mcshock
                    "My eyes go wide."
                    "No... this can't be happening..."
                    "Someone just hurt themselves because of me..."
                    "I'm supposed to be helping him, not let him do this to himself -!"
                    "I need to stop this madness."
                    hide mcshock with dissolve
                    show dv rneutral with dissolve
                    m sadtalk "Michael..."
                    m talk "No matter why you did this, it's not right."
                    m regret "Hurting anyone is never the right option... even if you don't care about how it affects you."
                    show dv rneu with dissolve
                    stop music fadeout 5
                    m sad "Please..."
                    m angry "There's too much hurt in this world already. Don't add to it."
                    play music "ost/emo.ogg" fadein 6
                    show dv rsidetalk with dissolve
                    dv "You don't understand at all, [name]..."
                    show dv rangrytalk with dissolve
                    dv "This is nothing compared to what I could do to you if I lost it, like with Caroline."
                    show dv rfrust with dissolve
                    m regret "But still..."
                    m angry "If you hurt me, it doesn't matter - I just don't want you to be in pain."
                    show dv rdevil with dissolve
                    "He laughs."
                    show dv rsmirk with dissolve
                    dv "Funny, how we both use the same argument against each other..."
                    show dv rsidetalk with dissolve
                    dv "I really don't care if I end up hurt because of this."
                    show dv rsiden with dissolve
                    m sjw "But I do!"
                    show dv rdevil with dissolve
                    dv "Heh..."
                    show dv rsmirk with dissolve
                    dv "So I guess I must care about what happens to you as well."
                    stop music fadeout 5
                    hide dv with dissolve
                    show drk 2 with Dissolve(1.0)
                    "I look at the scars again. It's so... wrong."
                    "He's staring at me curiously."
                    play music "ost/hospital.ogg" fadein 6
                    dv "Does it... bother you to look at that?"
                    m frusttalk "It's... unpleasant, but it doesn't matter."
                    "I lean in a bit to examine the marks more closely."
                    m angry "When exactly did you make these?"
                    dv "Uhh... last night, mostly. Some of them on Friday, right after I left your office."
                    "I point to one of the bigger scars on his wrist which seems new."
                    m fabtalk "Is this from Friday?"
                    "He chuckles."
                    stop music fadeout 5
                    dv "Nah, this one's fresh. Let me show you what the ones from Friday look like..."
                    "He hesitantly grabs my wrist and guides my fingers to a barely visible scar."
                    play music "ost/tension.ogg" fadein 8
                    "His hands are trembling."
                    "I carefully touch the faded mark with my fingertips."
                    "His skin is so warm... I can feel his blood rushing under my touch."
                    "To my relief, he seems to heal quite quickly - I suppose he has to, after all the harm he's done to himself."
                    "Fascinated by the amount of scars on his skin, I slowly drag my fingertips towards his wrist."
                    "He hisses when I brush against a recent bruise."
                    m gasp "Sorry -"
                    dv "It's fine. I'm used to a lot more than that."
                    "I reach his wrist and and slowly examine the layers of scars and fresh cuts."
                    m talk "How did you get these last night if you don't have access to anything sharp..?"
                    dv "Uhh... nails are very effective, if you're determined enough. And it hurts more than a knife - it's not a very clean cut."
                    "I look at one of the teeth marks on his wrist."
                    m neu "Did you actually..?"
                    dv "Yeah. It's probably the easiest thing to do if you don't have any tools for it."
                    dv "And besides, if you scratch it, the blood could stain something. Which is bothersome."
                    "...oh. I get it."
                    dv "And, uh... It does more damage. So it's more effective."
                    stop music fadeout 5
                    "I let my hand roam across his skin, butchered with scars."
                    show dv close with dissolve
                    show drk 2 with dissolve
                    "I freeze when I feel his uneven breath on my ear."
                    play music "ost/fight.ogg" fadein 6
                    show drk with dissolve
                    "His face is an inch away from mine. I didn't realize that before."
                    "His pale wide eye looks almost feverish as he stares back at me, panicked."
                    "I know I should be at least as frightened as him right now - but I'm not."
                    "I'm perfectly calm, despite how close he is and how easily he could hurt me right now."
                    m regret "I'm sorry. I didn't realize I got this close."
                    "I move away from him slowly, watching him."
                    show dv rnoeyes with dissolve
                    stop music fadeout 6
                    "He's silent."
                    "I withdraw my hand carefully."
                    show dv rkh2 with dissolve
                    dv "Wait-"
                    "He grabs my wrist suddenly."
                    play music "ost/tension.ogg" fadein 6
                    show dv rdarktalk with dissolve
                    dv "{i}Don't leave me yet."
                    show dv rdark with dissolve
                    "I don't think he's fully in control of himself right now..."
                    menu:
                        "Touch his hand":
                            $RedHeart+=2
                            $personal+=1
                            "I don't care. If even a borderline delirious part of him wants it so desperately, it's still him."
                            "And I'll respect his wishes if it helps him."
                            show dv rkh with dissolve
                            "I slowly free my hand from his hold and intertwine my fingers with his."
                            show dv rmoment with dissolve
                            dv "...."
                            "He's completely still for a while."
                            show dv rsadtalk with dissolve
                            dv "Thank you, [name]..."
                            show dv rsadsmile with dissolve
                            dv "I... I don't know what's happening to me, but being with you... makes it so much easier."    
                            show drk with Dissolve(0.75)
                            show r 1 with dissolve
                            show r 3 with Dissolve(0.3)
                            show r 2 with Dissolve(0.3)
                            $renpy.pause(0.75, hard = True)
                            hide r with Dissolve(0.5)
                            hide drk with dissolve    
                            show dv rsmirk with dissolve
                            "He laughs suddenly."
                            show dv rsadsmile with dissolve
                            dv "I shouldn't... let you do that..."
                            show dv rsiden with dissolve
                            "He looks at our hands."
                            show dv rfrusttalk with dissolve
                            dv "I'm sorry."
                            show dv rfrust with dissolve
                            "He withdraws his hand, and so do I."
                        "Don't":
                            $professional+=1
                            show dv rsad with dissolve
                            "I have to be careful no matter what. If he's not thinking straight, I should."
                            "I can't stand to look into his dejected eyes."
                            m regrettalk "It's for the best."
                            show dv rangry with dissolve
                            dv "I know."
                    hide drk with Dissolve(1.0)
                    stop music fadeout 10
                    show dv rhes with dissolve
                    dv "I..."
                    show dv rfrusttalk with dissolve
                    dv "The thing is, I really shouldn't be doing any of that... I mean touching people."
                    show dv rsad with dissolve
                    dv "...especially like this."
                    show dv rtalk with dissolve
                    dv "Since..."
                    show dv rsidetalk with dissolve
                    dv "The more I do, the more..."
                    show dv rfrust with dissolve
                    "He pauses."
                    play music "ost/hospital.ogg" fadein 6
                    show dv rsadtalk with dissolve
                    dv "I don't like how that turns out."
                    show dv rangry with dissolve
                    m talk "I understand."
                    show dv rneutalk with dissolve
                    dv "Why didn't you just refuse and get it over with?"
                    show dv rneutral with dissolve
                    m frust "Because..."
                    "I don't know. I felt like I shouldn't. That it would be cruel."
                    show dv rsad with dissolve
                    m regrettalk "I didn't want to leave you like that."
                    show dv rbreath with dissolve
                    dv "...Oh."
                    show dv rsidetalk with dissolve
                    dv "You're too kind, [name]. That's going to get you hurt eventually."
                    show dv rneutral with dissolve
                    m neu "Maybe."
                "{color=#bc0b17}Check his left arm":
                    "I lean in and reach out with my hand slowly."
                    m fabtalk "May I?"
                    show dv rtalk with dissolve
                    dv "Yeah, go on."
                    show dv rdevil with dissolve
                    dv "...Like I have a choice..."
                    show dv rfrust with dissolve
                    show drk with dissolve
                    stop music fadeout 5
                    "I carefully place my hands around his wrist and roll his sleeve up to his elbow."
                    "And... nothing."
                    show dv rsiden with dissolve
                    play music "ost/tran.ogg" fadein 6
                    "I let out the breath I was holding, seeing no fresh marks on his skin."
                    "Although there's still a lot of nasty-looking old scars, nothing looks new. I flinch a bit."
                    show dv rneu with dissolve
                    m conf "Alright... I just had to make sure you're okay."
                    show dv rsidetalk with dissolve
                    dv "I get it."
                    show dv rneutral with dissolve
                    "He slips his hand out of my grip."
                    hide drk with dissolve
                    show dv rsmile with dissolve
                    dv "As you can see, I'm still fine."
                    m flirt "I'm relieved to hear that."
                    show dv rneu with dissolve
                    "I let out a nervous laugh."
                    m regrettalk "You know, I really... thought you... You know..."
                    show dv rsad with dissolve
                    m talk "...hurt yourself again. I don't know why."
                    show dv rsadtalk with dissolve
                    dv "I'm sorry, [name]."
                    show dv rangry with dissolve
                    m gasp "For what?"
                    show dv rfrusttalk with dissolve
                    dv "You shouldn't worry about me like that."
                    show dv rneutral with dissolve
                    stop music fadeout 5
                    m fabtalk "Why not? I'm trying to help you."
                    show dv rsadtalk with dissolve
                    dv "...Would you really be worried if I did hurt myself?"
                    play music "ost/tension.ogg" fadein 8
                    show dv rsiden with dissolve
                    m angry "Of course I would be."
                    show dv rshock with dissolve
                    dv "Why?"
                    show dv rcute with dissolve
                    m trigger "Because you would be hurt, of course!"
                    show dv rfrusttalk with dissolve
                    dv "But... if I felt the need to hurt myself, it would be to stop myself from hurting {i}you."
                    show dv rtalk with dissolve
                    dv "So... of course you'd care about that."
                    show dv rneutral with dissolve
                    m angrytalk "No! You're more important than that, I'm supposed to be helping you."
                    show dv rsiden with dissolve
                    m regret "...."
                    "I need him to realize he can't just hurt himself like that."
                    "But... I guess I'll have to wait until tomorrow."
            "I think our time for today is running out. I don't want to rush it like last time."
            stop music fadeout 4
            m fabtalk "You should get going soon if we want to wrap this up in time."
            show dv rdark with dissolve
            "He freezes."
            m gasp "What..?"
            play music "ost/sunny.ogg" fadein 6
            show dv rkh with dissolve
            dv "Is that literally the most horrible pun I've ever heard?"
            show dv rnoeyes with dissolve
            "Oh."
            show dv rsidesmile with dissolve
            dv "Seriously [name], if I didn't know any better, I would be offended right now."
            m boretalk "...It wasn't intentional, I swear."
            show dv rsmirk with dissolve
            "He glares at me in amusement for a moment."
            stop music fadeout 5
            show dv rsmile with dissolve
            dv "Alright then."
            scene bg mc with dissolve
            "He gets up and I tie him back up carefully."
            hide screen redmeter
            hide screen easymeter
            play music "ost/hospital.ogg" fadein 6
            show drk with dissolve
            "Once his hands are restrained again, I walk up to him and look him in the eye."
            "It's not fair for him to have to be like this..."
            if DevilShip:
                m regrettalk "Michael..."
                "I don't know what to say."
                "He steps away from me before I can make up my mind about what was going through my head just now."
            dv "I'll see you tomorrow."
            hide drk with dissolve
            m talk "...bye."
            play sound "doorclose.ogg" fadein 1
            if DevilShip:
                "I have no words for what just happened."
            "I watch him leave my office in silence."
            $persistent.DevilRed=True
            show screen notify("{size=24} Your Characters Info screen has been updated!")
            jump breakchoice
        else:
            scene bg mc with dissolve
            "I'm back at the hospital."
            scene bg mcdesk with dissolve
            play music "ost/sunny.ogg" fadein 6
            dv "Hi again."
            if easymeter:
                show screen easymeter
                show screen redmeter
            show dv smile with dissolve
            "I greet him with a smile and he sits down."
            m fab "So..."
            m conf "How was the weekend?"
            show dv sidetalk with dissolve
            dv "It was alright... I managed to last these two days without you."
            show dv devil with dissolve
            "He laughs."
            show dv neutalk with dissolve
            dv "Why do you ask?"
            show dv neutral with dissolve
            m talk "I don't know... since you said you'd miss me..."
            stop music fadeout 5
            m kawaii "I was concerned."
            show dv sidetalk with dissolve
            dv "Ah. I see."
            show dv sadtalk with dissolve
            play music "ost/neutral.ogg" fadein 6
            dv "Well... the weekends are always kind of dull."
            show dv talk with dissolve
            dv "I don't get to leave my room much."
            show dv neu with dissolve
            dv "Since... I'm too lazy to make them go through the trouble of tying me up. And all that."
            show dv neutral with dissolve
            "...oh. I remember our last session."
            m serious "You... You meant it when you said I shouldn't free you, right?"
            show dv kh2 with dissolve
            stop music fadeout 4
            "He freezes."
            show dv notalk with dissolve
            dv "Of... Of course I did, [name]. Why wouldn't I?"
            show dv frust with dissolve
            m regret "...."
            play music "ost/tran.ogg" fadein 8
            show dv smile with dissolve
            dv "Hey, don't feel bad about it. It's really for the best."
            show dv neutral with dissolve
            m gasp "You think so?" 
            show dv smirk with dissolve
            dv "I know so."
            show dv sidetalk with dissolve
            dv "You really wouldn't feel as comfortable around me as you are now, trust me."
            show dv sidesmile with dissolve
            dv "You'd probably just run away after one session..."
            show dv neu with dissolve
            m boresmile "It can't be that bad..."
            show dv angry with dissolve
            dv "I swear, [name], it is. I'm always restrained for a reason."
            show dv sadtalk with dissolve
            dv "I wouldn't really... be able to control myself. And, uh..."
            show dv sadsmile with dissolve
            dv "...that scares me, to be honest."
            show dv neutral with dissolve
            m talk "I see."
            show dv sad with dissolve
            m conf "It's fine, really. I wouldn't want you to feel uncomfortable here."
            show dv frust with dissolve
            m regrettalk "Besides, I don't think the rest of the staff would approve of me doing something as risky."
            show dv sadtalk with dissolve
            dv "Yeah."
            show dv neutalk with dissolve
            stop music fadeout 4
            dv "So... can we just forget you even brought that up?"
            show dv frusttalk with dissolve
            dv "I don't want to even think about it..."
            show dv angry with dissolve
            menu:
                "I won't mention it again":
                    play music "ost/sunny.ogg" fadein 8
                    show dv devil with dissolve
                    dv "Great."
                    show dv smile with dissolve
                    dv "Thanks, [name] - you're really something ~"
                "Why don't you want to think about it?":
                    show dv sadtalk with dissolve
                    play music "ost/hospital.ogg" fadein 8
                    dv "B... Because..."
                    show dv talk with dissolve
                    dv "I just don't. I don't want to, uh... hope for something that I know won't do any good."
                    show dv angry with dissolve
                "Isn't that still a possibility?":
                    play music "ost/tension.ogg" fadein 6
                    show dv gasp with dissolve
                    dv "What?!"
                    show dv notalk with dissolve
                    dv "No no no, that's not happening. For real."
                    show dv angry with dissolve
                    m gasp "Why?"
                    show dv frusttalk with dissolve
                    dv "Because it just shouldn't. And I won't let you argue with me about that."
                    show dv sadtalk with dissolve
                    dv "I'm sorry, but this one topic is something I won't let you change my mind about."
                    stop music fadeout 4
            show dv sad with dissolve
            dv "...."
            "I decide to change the subject."
            show dv neu with dissolve
            "We spend the rest of the session discussing other things."
            show dv sidetalk with dissolve
            dv "I should be going now."
            show dv neutral with dissolve
            m uncom "Is it that late already..?"
            "I follow him to the door."
            hide screen redmeter
            hide screen easymeter
            m conf "I'll see you tomorrow, Michael."
            stop music fadeout 5
            show dv smile with dissolve
            "He nods and leaves."
            play sound "doorclose.ogg" fadein 1
            $route="no" ##that means she'll get the apathy ending
            jump patientsattack
    elif day == 16:
        scene bg mcdesk with dissolve
        "Michael enters my office."
        show dv sidetalk with dissolve
        play music "ost/neutral.ogg" fadein 8
        dv "...Hey."
        if easymeter:
            show screen easymeter
            show screen redmeter
        show dv frust with dissolve
        "He seems tired for some reason."
        m uncom "Are you okay?"
        show dv hes with dissolve
        "He takes a moment to realize what I just asked him."
        show dv frusttalk with dissolve
        dv "Yeah, I'm fine."
        hide dv with Dissolve(1.0)
        "I untie him as usual and he sits down."
        show dv rsiden with dissolve
        "He definitely seems less energetic than usual."
        show dv rneutral with dissolve
        "Regardless, he focuses on me."
        show dv rangrytalk with dissolve
        dv "[name], I wanted to tell you something."
        if DevilShip:
            #attacks her as written
            show dv rsadtalk with dissolve
            stop music fadeout 5
            dv "It has to do with yesterday..."
            show dv rfrust with dissolve
            "I lean in a bit to hear him out."
            show dv rneutral with dissolve
            m talk "What is it?"
            show dv rhes with dissolve
            play music "ost/tension.ogg" fadein 6
            dv "I... realized that... when you're close to me like this, it's not the same as it was with Caroline."
            show dv rfrusttalk with dissolve
            dv "She was... she was so pathetic."
            show dv rsadtalk with dissolve
            dv "All I could think about was how to stop myself from hurting her."
            show dv rangry with dissolve
            dv "And with you, it's... it's so much different."
            show dv rsadtalk with dissolve
            dv "You know how I am, and you're not even unsettled by me."
            show dv rsadsmile with dissolve
            stop music fadeout 5
            dv "I feel like... I can focus on something other than the things in my head."
            show dv rangry with dissolve
            "He looks at me."
            play music "ost/hospital.ogg" fadein 6
            show dv rhes with dissolve
            dv "I'm thinking about you, [name]."
            show dv rsidetalk with dissolve
            dv "Not just in these thoughts, but on my own as well."
            dv "Because I want to. And not because I'm forced to think of that."
            show dv rsmirk with dissolve
            dv "You have no idea how special that is."
            m sadsmile "I'm... glad you're making progress."
            stop music fadeout 5
            show dv rsadtalk with dissolve
            dv "It's not just that..."
            show dv rangrytalk with dissolve
            dv "It's personal. For me, at least."
            play music "ost/tension.ogg" fadein 8
            show dv rhes with dissolve
            dv "It's always about you, [name]... You're always there."
            show dv rfrusttalk with dissolve
            dv "When we talk, when I'm alone, on days, nights... it doesn't matter. I can't stop thinking about you."
            show dv rsad with dissolve
            dv "I..."
            show dv rangrytalk with dissolve
            dv "I care a lot more than I'd like to."
            show dv rkh2 with dissolve
            dv "I care enough to hurt myself because of you." 
            show dv rnotalk with dissolve
            stop music fadeout 6
            dv "I care so much it makes me feel pain whenever I'm not with you."
            play music "ost/fight.ogg"
            show dv rpant with dissolve
            dv "I don't want you to leave me, [name]."
            show dv rdarktalk with dissolve
            dv "I feel like I would die if you left."
            show dv rkh with dissolve
            dv "My life doesn't matter either way and you're the only one who can make it worth it."
            show dv rnotalk with dissolve
            dv "[name]."
            dv "[name], [name], [name]"
            show dv rkh2 with dissolve
            dv "It's all because of you."
            show dv rkh with dissolve
            m serious "Michael..."
            "He's scaring me a little... I try to remain calm."
            show dv rnotalk with dissolve
            dv "Yesterday, when you touched my skin, I felt something."
            show dv rkh with dissolve
            dv "I would never name it in front of anyone else, but [name]... I'll tell you."
            show drk with dissolve
            show dv rdark with dissolve
            "He gets closer to me suddenly, and I search for any hint of rationality in his eyes - there's none."
            "He's completely lost right now."
            show dv rkh2 with dissolve
            dv "[name]..."
            "I can feel his breath on my skin."
            show dv rkh with dissolve
            dv "{i}I  want  you."
            show dv rdarktalk with dissolve
            dv "I want to touch you. I want to be closer to you."
            show drk 2 with dissolve
            show dv rnoeyes with dissolve
            "He bends down a bit, even closer to me. His breath on my neck is making my mind want to give up."
            "I don't know what to do... I can't move."
            show dv rnotalk with dissolve
            dv "I want to taste your neck and feel the blood under your skin."
            show dv rkh with dissolve
            dv "I... I..."
            stop music fadeout 6
            show dv rnoeyes with dissolve
            "His voice gives up. He seems to be having trouble breathing."
            hide drk with dissolve
            "I pull back in my chair, away from him."
            "I don't know what I should say, or if I should even say anything."
            play music "ost/tension.ogg" fadein 6
            "After carefully putting a safe distance between us, I look at him once again."
            show dv rkh2 with dissolve
            "He's panting, eyes wide, fixated somewhere on my desk."
            "I can't imagine how intense that must've been for him."
            m sadtalk "Michael?"
            "He can't hear me."
            show dv rangry with dissolve
            "Suddenly, he looks at me again."
            show dv rfrusttalk with dissolve
            dv "But..."
            show dv rhes with dissolve
            dv "...I can't."
            "He grips his head with both hands."
            show drk 2 with dissolve
            ## show dv hiden with Dissolve(1.0)
            dv "No, no, I can't..."
            dv "{i}[name]..?{/i} No, that's not -"
            dv "God, this is all wrong..."
            dv "I'm sorry, I'm so sorry..."
            m talk "It's okay."
            stop music fadeout 5
            dv "...."
            "I look at him closely, concerned."
            show dv rkh with Dissolve(1.0)
            hide drk with dissolve
            m uncom "How do you feel now?"
            play music "ost/hospital.ogg" fadein 6
            show dv rfrusttalk with dissolve
            dv "Uh... unstable?"
            show dv rsad with dissolve
            m sad "Is there anything I can do to help?"
            show dv rneutalk with dissolve
            dv "...Nah. You heard all that. There's no point."
            show dv rneutral with dissolve
            "...oh."
            show dv rsad with dissolve
            dv "Yesterday, when you touched me, I realized that it's pointless."
            show dv rfrusttalk with dissolve
            dv "That I'll never have what I want."
            show dv rsadtalk with dissolve
            dv "And that every time you touch me, you just make me more miserable."
            show dv rnotalk with dissolve
            dv "There's no end to it... There's no way to stop it..."
            show dv rsadtalk with dissolve
            dv "I don't think there's anything you can do. Or anyone else, for that matter."
            show dv rangrytalk with dissolve
            dv "I may be just destined to suffer. Like last night."
            show dv rneutral with dissolve
            "He looks down and slowly rolls up his sleeve. There's dozens of fresh marks I haven't seen yesterday."
            "He's been doing it again..."
            show dv rfrusttalk with dissolve
            dv "Yesterday, I just..."
            show dv rsad with dissolve
            dv "Kept thinking about what happened."
            show dv rnotalk with dissolve
            dv "And the more I thought about it, the more desperate I got."
            show dv rsadtalk with dissolve
            dv "I'm sorry about grabbing your hand that time... I couldn't stop myself."
            show dv rfrust with dissolve
            m neu "I understand."
            show dv rsad with dissolve
            dv "And you... let me do that to you..."
            show dv rhes with dissolve
            dv "Why?"
            show dv rsadtalk with dissolve
            dv "Why are you torturing me, [name]?"
            show dv rangrytalk with dissolve
            dv "You're... letting me believe that I could do what I want."
            show dv rhes with dissolve
            dv "Which isn't true."
            show dv rsad with dissolve
            dv "So why would you give me hope?"
            show dv rangry with dissolve
            m fabtalk "Why wouldn't I? It's not like what you did yesterday bothered me."
            show dv rfrust with dissolve
            dv "...."
            show dv rhes with dissolve
            dv "Don't say things like that..."
            show dv rangry with dissolve
            m angrytalk "I would've stopped you if I'd been bothered by it."
            show dv rsidetalk with dissolve
            dv "...You won't have a choice if you keep acting like this. Really."
            show dv rfrusttalk with dissolve
            dv "And you wouldn't like any of the things I'd actually like to do."
            stop music fadeout 5
            show dv rsad with dissolve
            dv "...."
            show dv rsadtalk with dissolve
            dv "[name], my room feels so empty compared to this place."
            show dv rangry with dissolve
            play music "ost/tension.ogg" fadein 6
            dv "I can't sleep at night... I keep thinking about you."
            show dv rfrusttalk with dissolve
            dv "Last night, I kept seeing what happened yesterday... And what... could've happened."
            show dv rangrytalk with dissolve
            dv "I made this rule with Caroline: whenever I'm about to hurt her in my thoughts, I hurt myself instead."
            show dv rneutral with dissolve
            "He lays his scarred right arm on my desk."
            show dv rneutalk with dissolve
            dv "This is how it ended up."
            show dv rsiden with dissolve
            "There's so many fresh ones... does he really want to hurt me so much?"
            show dv rhes with dissolve
            dv "I curled up on my bed and bit myself."
            show dv rsidetalk with dissolve
            dv "It's like a high of sorts..."
            show dv rfrust with dissolve
            dv "The pain fueled the thoughts, so I couldn't stop."
            show dv rsadtalk with dissolve
            dv "And despite everything, I still felt so... alone."
            show dv rangrytalk with dissolve
            dv "I just... wanted so badly for you to be there with me. Wanted {i}someone{/i} to be there."
            show dv rsadtalk with dissolve
            dv "Then I wouldn't feel so... hollow. Meaningless."
            show dv rnotalk with dissolve
            dv "Like the pain and everything else has no importance to anyone."
            show dv rkh with dissolve
            dv "And I'm just... one lonely person who suffers while really nobody cares."
            show dv rdarktalk with dissolve
            dv "Like you didn't really care, since if you had, you would've been there with me."
            show dv rsadtalk with dissolve
            dv "And I know I shouldn't think that, but... it's difficult to convince myself."
            show dv rfrust with dissolve
            m sadtalk "Would you stop hurting yourself if I were there?"
            show dv rtalk with dissolve
            dv "I would want to, I can't say I would be able to, though."
            show dv rneutral with dissolve
            m uncom "I see..."
            show dv rsadtalk with dissolve
            dv "I'm sorry about thinking that way about you. I can't help it."
            show dv rfrust with dissolve
            dv "You keep trying so hard, and I just -"
            stop music fadeout 4
            show dv rshock with dissolve
            dv "...What are you doing?"
            show dv rdark with dissolve
            "I place my hand in his slowly."
            play music "ost/tran.ogg" fadein 6
            m serious "You shouldn't feel bad about what you think of me. I know it must be confusing for you."
            show dv rnoeyes with dissolve
            m conf "But... I care as well. And I really want to do whatever it takes to help you."
            show dv rnotalk with dissolve
            dv "You... care about me?"
            show dv rdark with dissolve
            m angry "Of course I do. It's my job to help you get out of here."
            show dv rfrusttalk with dissolve
            dv "...oh."
            show dv rfrust with dissolve
            m fabtalk  "But..."
            m talk "If I could, I would've stayed with you last night until you wouldn't want to hurt yourself."
            show dv rneutral with dissolve
            m sadtalk "I... It doesn't feel right that you have to suffer while I can't do anything but wait."
            "I sigh."
            show dv rsad with dissolve
            "Turns out I'm the one venting here."
            m talk "But that's not possible."
            show dv rneutalk with dissolve
            dv "Because I'm a patient here?"
            show dv rneutral with dissolve
            m angry "And because I'm your psychologist."
            show dv rangry with dissolve
            m frusttalk"But if I could, I would help you in any way possible."
            show dv rsidetalk with dissolve
            dv "I believe you."
            show dv rsmile with dissolve
            dv "Thank you, [name] - I can't express how grateful I am right now."
            show dv rsiden with dissolve
            "I move my fingertips across his skin carefully."
            show dv rhes with dissolve
            dv "And, uh..."
            show dv rfrust with dissolve
            stop music fadeout 5
            "He glares at my hand and clears his throat quickly."
            show dv rsadsmile with dissolve
            dv "Thank you, but... it's getting difficult... for me to breathe..."
            show dv rneutral with dissolve
            "I remove my hand."
            show dv rneu with dissolve
            dv "...."
            show dv rfrust with dissolve
            dv "...."
            play music "ost/tension.ogg" fadein 6
            show dv rkh with dissolve
            dv "Khhh..."
            show dv rdark with dissolve
            "He pulls back and away from me suddenly."
            m uncom "What's wrong?"
            show dv rnotalk with dissolve
            dv "I..."
            show dv rkh with dissolve
            dv "It's... these thoughts again..."
            show dv rsad with dissolve
            dv "They -"
            show dv rnotalk with dissolve
            dv "{i}Khhh-"
            show dv rkh2 with dissolve
            dv "{i}They won't stop."
            m serious "What are they about?"
            show dv rangry with dissolve
            "He glares at me."
            show dv rhes with dissolve
            dv "You."
            show dv rnoeyes with dissolve
            "It seems worse than the last times. It's the sudden sense of emergency that causes me to act more boldly."
            m sjw "What's going on? You have to tell me."
            show dv rfrust with dissolve
            dv "...."
            show dv rsadtalk with dissolve
            dv "You... You don't need to know..."
            show dv rangry with dissolve
            m angrytalk "I do. No matter what it is."
            show dv rhes with dissolve
            dv "I..."
            show dv rfrusttalk with dissolve
            dv "I want... to hurt you..."
            show dv rfrust with dissolve
            m talk "Go on."
            "Somehow, I don't really care that he wants to hurt me."
            stop music fadeout 6
            "Helping him is the most important thing to me right now. Way more important than my feelings."
            show drk with dissolve
            show dv rangrytalk with dissolve
            play music "ost/fight.ogg"
            dv "I want to... do what I did to myself last night... and all the nights before..."
            show dv rkh with dissolve
            "He's trembling."
            show dv rnotalk with dissolve
            dv "I want to make you bleed -"
            show dv rdark with dissolve
            dv "Bite into your skin-"
            show dv rkh2 with dissolve
            dv "I... want... to..."
            show dv rmoment with dissolve
            dv "...I want to rip you apart."
            show dv rdarktalk with dissolve
            dv "Tear your heart out and watch you die, slowly and painfully, as I destroy what remains of your body and bathe in your blood."
            show dv rkh with dissolve
            dv "I want to see you afraid and hear your screams with my own ears."
            show drk with dissolve
            show dv rnotalk with dissolve
            dv "[name]-"
            show dv rsadtalk with dissolve
            dv "[name], just kill me already... I shouldn't be allowed to exist alongside someone like you."
            show dv rkh with dissolve
            "He reaches up with his hand and nearly covers his left eye."
            show dv rdarktalk with dissolve
            dv "[name]... {i}Ahhh- It hurts..."
            show dv rnoeyes with dissolve
            m scream "Michael -!"
            stop music fadeout 5
            "Before I can do anything to stop him, he digs his nails into the skin on his forehead and drags his hand down across his face."
            show dv rkh with dissolve
            "He's not bleeding, but I can see red marks on his skin where he hurt himself."
            "I can't allow that. Not in my office. Not when I can do something to stop it."
            "I can't look at something like that and be helpless."
            show drk with dissolve
            "I get up and rush over to his side of my desk."
            m scream "Michael!"
            show dv rnoeyes with dissolve
            "I grab his shaky wrist with my hand and look straight into his eyes."
            m sjw "Don't say these things. You're worth as much as I am and nothing gives you the right to think otherwise."
            m angrytalk "I'll never let you hurt yourself in front of me."
            m sad "Michael, please... stop it."
            show dv rdark with dissolve
            dv "...."
            "He looks back at me, his eyes feverish."
            show dv rcreepy with dissolve
            dv "[name]..."
        else:
            ##shows her marks
            show dv rsadtalk with dissolve
            dv "I... may not have been... entirely honest with you."
            stop music fadeout 5
            show dv rfrust with dissolve
            m gasp "What do you mean..?"
            show dv rsidetalk with dissolve
            dv "About... hurting myself."
            play music "ost/tension.ogg" fadein 8
            show dv rneutral with dissolve
            "...oh no."
            m regrettalk "Have you really... done it again?"
            show dv rnotalk with dissolve
            dv "I... I couldn't stop myself..."
            show dv rkh with dissolve
            dv "It's all... because of you... Because of how much... I care about you."
            show dv rangrytalk with dissolve
            dv "I wasn't lying yesterday. I really care."
            show dv rsadtalk with dissolve
            dv "You... you just... don't deserve to be... hurt like that."
            show dv rtalk with dissolve
            dv "...I do."
            stop music fadeout 4
            show dv rangry with dissolve
            m sadtalk "Don't say that."
            show dv rdarktalk with dissolve
            dv "[name]... [name], look at me..."
            show dv rclose with dissolve
            "He rolls up his right sleeve." 
            play music "ost/fight.ogg" 
            m scream "!!!"
            "His arm is completely butchered with scars."
            "Fresh ones, as well."
            show dv rdark with dissolve
            m angry "Why... Why would you do that to yourself?"
            dv "Can't you see it, [name]...? [name], it's all because of you. It was always because of you."
            show dv rkh with dissolve
            dv "I... I can't... I can't handle being without you."
            show dv rkh2 with dissolve
            dv "I..."
            show dv rdarktalk with dissolve
            dv "...I care so much about you..."
            show dv rkh2 with dissolve
            "His breath grows uneven."
            show dv rnotalk with dissolve
            dv "I care enough... to hurt myself because of you."
            show dv rdark with dissolve 
            dv "I care so much it... makes me feel {i}pain{/i}... whenever I'm not with you -"
            show dv rpant with dissolve
            dv "I don't want you to leave me, [name]... Ever."
            show dv rdarktalk with dissolve
            dv "{i}I feel like I would die if you left-!"
            show dv rangry with dissolve
            dv "[name]."
            show dv rangrytalk with dissolve
            dv "{i}[name], [name], [name]"
            show dv rdarktalk with dissolve
            dv "{i}This is all for you."
            show dv rkh with dissolve
            "I can't handle looking at the scars on his skin... There's way too many... How could I've missed them yesterday?"
            "I should've checked both of his arms... I shouldn't have trusted him when he said he's fine..."
            "How could I have failed so much...?"
            m sadtalk "Michael, don't do this to yourself... Please don't..."
            show dv rdark with dissolve
            "He can't hear me. He's completely lost right now."
            m regrettalk "Michael..."
            show dv rkh2 with dissolve
            dv "[name]... You didn't even care... when I did all of that to myself..."
            show dv rkh with dissolve
            m sjw "I didn't know!"
            show dv rnotalk with dissolve
            dv "You... you don't even... appreciate the things I've done... to be with you."
            show dv rnoeyes with dissolve
            m scream "No, it's not like that! Michael, listen to me!"
            show dv rangrytalk with dissolve
            dv "{b}NO."
            show dv rkh with dissolve
            show drk with dissolve
            "He touches my cheek with his hand. The marks on his wrist are still bloody."
            "I force myself to stay still despite the smell of blood making me flinch."
            stop music fadeout 5
            show dv rtalk with dissolve
            dv "You'll listen to me this time."
            show dv rshock with dissolve
            dv "[name], I... I've wanted this for so long now."
            show dv rdarktalk with dissolve
            dv "Wanted... to... touch you... Like this."
            play music "ost/tension.ogg" fadein 8
            show dv rdark with dissolve
            "I force myself to remain calm. I don't think it would be very smart to push him away now."
            m sadtalk "Why..?"
            show dv rfrust with dissolve
            dv "...."
            show dv rsadtalk with dissolve
            dv "[name], you really wouldn't understand..."
            show dv rhes with dissolve
            show drk 2 with dissolve
            "He touches my face with the bloody marks on his wrist."
            show dv rkh with dissolve
            dv "...."
            "He's panting heavily. He seems to be barely in control of himself right now."
            m bloody "Michael..."
            show dv rnoeyes with dissolve
            dv "...."
            show dv rsadtalk with dissolve
            stop music fadeout 4
            dv "[name]... Maybe... if you really don't care... You won't care about this."
            show dv rneutral with dissolve
            "He pulls away from me and digs his nails into a bloody wound on his wrist."
            show drk with dissolve
            play music "ost/tension.ogg" fadein 6
            m bloodtalk "No!"
            show dv rneu with dissolve
            "He doesn't make a single sound. Like that's nothing for him."
            m "Michael, don't do this to yourself!"
            show dv rneutalk with dissolve
            dv "Why?"
            show dv rtalk with dissolve
            dv "What can you do to stop me?"
            show dv rneutral with dissolve
            "That's it. I can't allow that. Not in my office."
            "I can't look at something like that and be helpless."
            hide drk with dissolve
            show dv rnoeyes with dissolve
            "I get up and rush over to his side of my desk."
            m bloody "Michael, look at me - do I look like I don't care?"
            stop music fadeout 6
            m bloodtalk "Of course I do! I won't let you hurt yourself like that."
            show dv rdark with dissolve
            dv "...."
            "He glares at me in silence for a moment. His bloody left hand is twitching."
        hide screen redmeter
        hide screen easymeter
        show dv rkh with dissolve
        dvn "You're on the wrong side of the desk right now."
        play music "ost/fight.ogg" fadein 5
        scene black with vpunch
        nt "Before I can react, I'm pushed down and hit the floor with a loud thud."
        nt "He's on top of me."
        dvn "I'm sorry."
        if DevilShip and RedHeart>=15: 
            show dattack1
        else:
            show dattack2
        nt "He grabs both of my wrists before I can even try to struggle."
        nt "His weight pressing me down onto the ground makes it impossible for me to even free myself."
        nt "He stares down at me for a while, panting heavily, unsure of what to do."
        if DevilShip and RedHeart>=15: 
            nt "If I alert someone now, I may not be allowed to keep seeing him, and he'll never be helped."
            nt "I decide to wait and hope I can get out of this without anyone knowing what happened."
            dvn "[name]..."
            nt "He moves even closer to me."
            nt "I can feel the tip of his nose brushing against my neck, moving down slowly."
            nt "His head falls onto my chest. I can barely see his eyes."
            nt "My heart skips a beat. I'm terrified."
            nt "He's still and quiet for a while. I... can't feel anything but pity for him right now..."
            nt "He hurt himself so much just to prevent this..."
            nm "Michael..."
            nt "I touch his hand with my fingers, unable to hold it."
            nm "If you let go of me, I can still help you."
            dvn "You..."
            dvn "{i}You'd run away from me. Everyone would."
            nm "I would never do that to you."
            dvn "...."
            nt "His grip on my wrists tightens, and I'm forced to let go of his hand."
            nt "If he kills me now, I'll never be able to help him. Nobody will."
            nt "I freeze when I feel his tongue slipping between the buttons of my shirt."
            nt "My whole body shivers at the softness of his touch. I can't help it."
            nt "He moves his shaky fingers on my wrists, attempting to steady his grip."
            nt "He lifts his head back up ever so slightly, looking at me."
            dvn "[name]... Until you leave me, you're mine."
            nt "Slowly, he bends down again to place his lips on my neck."
            nt "I can feel him begin to tremble even more than he did before when he does."
            nt "His breath on my skin is the last thing I feel before he kisses the left side of my neck."
            dvn "...mine."
            nt "It's... difficult not to give in. I'm trying to stay rational."
            nt "I'm really trying, but..."
            nt "His kisses, his warmth, his touch..."
            nt "It's all so intense and so sudden, but a part of me doesn't want it to end."
            nt "A part of me doesn't even care than I could die."
            nt "I shut my eyes. I'm far from calm, but there's nothing I can do to stop him."
            nt "His pace quickens, but it still doesn't hurt."
            nt "I've always wanted to set him free. To let him be closer to me, if it's what he wanted."
            nt "This... wasn't my intention, but after being unable to touch him at all for so long, this feels... probably more right than it should ever feel."
        else:
            ##she tries to struggle
            nt "I struggle as hard as I can. I can't let him kill me!"
            nm "Michael, Michael please don't do this..."
            dvn "...."
            dvn "You're so... soft, [name]. So fragile..."
            nt "I can feel the tip of his nose brushing against my neck."
            m no "{i}!!!"
            dvn "Shhh... Quiet."
            nt "I have no way to even move like this. I'm trapped."
        dvn "...."
        nt "He pauses and shifts a bit. What's going on..?"
        nt "I gasp when he sinks his teeth into my neck."
        m no "{i}Michael -"
        nt "He doesn't stop."
        nt "It hurts like hell, but I don't think I'm bleeding yet."
        nt "His whole body is twitching on top of me."
        nt "His grip on my hands loosens enough for me to free one of them."
        if DevilShip and RedHeart>=15: 
            nt "But instead of attempting to push him away, which would only agitate him further, my first instinct is to touch the back of his head gently."
            nt "He freezes. The twitches become less violent."
            nm "Michael... Please listen to me."
            nm "I won't leave you if I have a choice. But if you really hurt me, I won't be able to come back."
            nm "Please..."
            nm "Neither of us wants it to end like this."
            nm "I can help you... All you have to do is stop right now."
            nt "I sob. It hurts..."
            m "...You're hurting me."
            nt "He pauses."
            dvn "It's... too late."
            nt "He pulls back, but doesn't look at me."
            dvn "I have to do this, [name]."
            nt "He bites deeper into my neck and buries his nails in the skin of my forearms, right below my wrists."
            m "{i}Gah -!"
            nt "I start to struggle, unable to bear the amounts of pain he's subjecting me to."
            nm "Please... {i}{cps=5}stop it..."
            show drk with dissolve
            nt "I can feel his hand on my throat. I can't breathe."
            nt "He presses down onto me harder, still clawing at my skin."
            nt "I think I'm bleeding. I can't tell."
            scene black with Dissolve (2.0)
            "...."
            stop music fadeout 5
            nt "I nearly pass out before the door to my office slams open."
            nn "Dr. Hart! Can you hear me?!"
            nt "I lose consciousness."
            $renpy.pause(3, hard=True)
        else:
            nt "Now's my chance to free myself!"
            scene black with hpunch
            nt "Using his distraction to my advantage, I push him off of me and try to get up."
            dvn "[name]."
            nt "He's faster than me. He grabs the collar of my shirt and pushes me back onto the ground."
            nt "I hit the floor with a thud. It hurts..."
            dvn "[name]... I was trying to be nice."
            nt "He bends down over me again, still holding me by the collar."
            dvn "...."
            scene mcblood
            nm "No... don't do this..."
            dvn "Oh [name], you have no idea how much I want to."
            nt "His hand moves to my throat. He's still making it impossible for me to move."
            dvn "You want to run away from me so badly... I knew you were lying to me the whole time."
            nt "I can't breathe."
            dvn "You never really wanted to help me."
            dvn "You're just like everyone else."
            dvn "You... You hate me, don't you..?"
            nt "Is he actually... crying?"
            m "...."
            dvn "...."
            nt "He grabs my arm with his other hand."
            dvn "[name]... You don't even know what pain is."
            nt "His hand touches my forearm."
            dvn "...nothing."
            dvn "Unlike me."
            nt "He intertwines his fingers with mine and lets his scarred forearm touch mine."
            nt "His skin feels so rough..."
            dvn "[name]... [name]... I envy you."
            dvn "I'll never be like you. I'll never be like everyone else."
            nt "He bends down over me even further. Closer."
            m "!!!"
            nt "He kisses me."
            nt "He doesn't let his grip on me loosen. I can't run away."
            nt "I can barely struggle."
            nt "He pulls away from me and looks into my eyes."
            dvn "I know, [name]. I know how it is."
            dvn "Who... Who would ever love someone like... me?"
            nt "He's really crying."
            dvn "[name]... I know you wouldn't. So... I have nothing to lose."
            nt "He digs his nails into my wrist."
            m "{i}!!!"
            nt "He drags his hand across all of my forearm, leaving deep, bloody cuts."
            m "{i}Ah.... Aahhhhhh....."
            nt "I can't handle this. I... Ive never felt this much pain at once."
            dvn "Now... Now you're like me."
            dvn "[name]..."
            nt "He bites the wound on my arm, making it bleed even more."
            scene black
            stop music
            dvn "{cps=*1/3}{i}I \ \ l o v e \ \ y o u ."
            nt "I'm fading..."
            nt "Everything is getting so blurry..."
            nt "He... He's killing me..."
            $renpy.pause(4,hard)
            scene black with Dissolve(2.0)
            $persistent.deaths+=1
            $renpy.quit()
        show bg mc with Dissolve(2.0)
        play music "ost/tran.ogg" fadein 12
        show jl talk with dissolve
        jl "Oh, you're awake. Good."
        show jl neutral with dissolve
        "I sit up slowly and touch my neck carefully. It hurts."
        show jl angrytalk with dissolve
        jl "Try not to mess that up even more. I did my best to clean it up, but it'll take a while to heal."
        show jl angry with dissolve
        m sad "Thanks..."
        "I struggle to get up. I'm alone in my office with Julia, the nurse whom I've met at the reception two weeks ago."
        show jl talk with dissolve
        jl "Here."
        show jl neutral with dissolve
        stop music fadeout 6
        "She helps me up and I sit down in a chair by my desk."
        "Well..."
        "I think I'm in trouble."
        m gasp "I... I can explain..."
        show jl angrytalk with dissolve
        play music "ost/hospital.ogg" fadein 8
        jl "Don't give me that, Hart. You'll tell everything to Dr. Sharpe in person."
        show jl neu with dissolve
        "I freeze. Now I'm really going to be punished."
        "What if he fires me for this..?"
        "What if I'll never be able to see Michael again?"
        show jl calmtalk with dissolve
        jl "Come on, follow me. It's getting late."
        show jl neutral with dissolve
        "Resisting the urge to ask her all the questions I have right now, I follow her out of my office."
        "I'm a bit dizzy... but I'll live."
        show bg offices with dissolve
        "I don't feel like talking, and I can tell Julia wants to get it over with quickly."
        show jl neu with dissolve
        "She stops by the door to Dr. Sharpe's office."
        m sadsmile "I really owe you, Julia."
        show jl calmtalk with dissolve
        jl "Like I'm the only one who saved you back there... I was just assigned to stay with you. Nothing personal."
        show jl neutral with dissolve
        m talk "Regradless, you helped me."
        m flirt "So I'm grateful for that."
        show jl talk with dissolve
        jl "Right... I need to go."
        show jl angrytalk with dissolve
        jl "It's not like I don't have any other duties in this place than chatting with you."
        show jl neutral with dissolve
        jl "Don't keep Sharpe waiting."
        hide jl with moveoutleft
        "She leaves. I guess I can't put off the inevitable any longer."
        play sound "knock.ogg" fadein 1
        m sadtalk "Dr. Sharpe? It's me, [name] Hart."
        d "Come in."
        scene bg doctor with dissolve
        stop music fadeout 25
        show d neutral with dissolve
        "I enter Dr. Sharpe's office."
        show d talk with dissolve
        d "Take a seat, Ms. Hart. You have a lot of explaining to do."
        show d cold with dissolve
        "The gravity of the situation hits me again."
        "Not only have I acted extremely recklessly by releasing him, I also caused an incident in which I, but most importantly other staff members or even patients could've been hurt."
        "I'm torn. Was it worth it?"
        show d foctalk with dissolve
        d "I assume you have a lot to say, but spare me the apologies - I do not appreciate changing the topic of our conversation at a time like this."
        show d foc with dissolve
        "I nod."
        play music "ost/hier.ogg" fadein 10
        show d cold with dissolve
        "He glares at me."
        show d coldtalk with dissolve
        d "Explain yourself. Why have you allowed him to be free?"
        show d cold with dissolve
        menu:
            "Out of pity":
                show d frusttalk with dissolve
                d "Ms. Hart..."
                show d frust with dissolve
                "I can sense the annoyance in his voice."
                show d coldtalk with dissolve
                d "I have warned you of this..."
                show d cold with dissolve
                menu:
                    "He was so miserable...":
                        show d foctalk with dissolve
                        d "You are acting like a child. Do you not understand what you have caused?"
                        jump devilhierfired
                    "I wanted to help":
                        show d regret with dissolve
                        d "...."
                        jump devilhierright
            "Out of fear":
                show d pant with dissolve
                d "\"Fear\"?"
                show d talk with dissolve
                d "Ms. Hart, are you telling me you are afraid of your patients?"
                show d cold with dissolve
                menu:
                    "Yes":
                        show d frust with dissolve
                        d "...."
                        "He signs in annoyance."
                        jump devilhierfired
                    "Only of him":
                        show d talk with dissolve
                        d "And why would you be afraid of him?"
                        jump devilhierfail
            "It was necessary":
                show d neu with dissolve
                m talk "I had to do it because..."
                menu:
                    "He made me":
                        show d neutalk with dissolve
                        d "What are you saying?"
                        jump devilhierfail
                    "It was the only way to help him":
                        show d neutalk with dissolve
                        d "How so?"
                        show d neutral with dissolve
                        m angrytalk "Doctor, I've spent two weeks working with this man before I came to the conclusion that I need to do it in order to have any chance to help him."
                        jump devilhierright
        jump breakchoice
    elif day == 17:
        scene bg mcdark with dissolve
        "I'm not allowed to see Michael until the end of the week."
        "I go about my day as usual, trying my best with all my other patients."
        jump nextday
    elif day == 18:
        scene bg mc with dissolve
        "Another day without seeing Michael..."
        "It's still a bit strange for me, but I focus on my other patients."
        scene black with dissolve
        scene bg mcdark with dissolve
        "I finish my work for the day and gather my belongings."
        scene bg offices with dissolve
        play music "footsteps.ogg" fadein 3
        "These past two days've passed in quite a blur."
        "Work goes by quickly since Michael attacked me on Tuesday."
        scene bg central with dissolve
        "I keep rethinking what happened..."
        "The wound on my neck is healing more slowly than I expected it to."
        "It's not that it hurts, I guess it's more about... having a physical mark of what happened."
        scene bg patients with dissolve
        play music "ost/tension.ogg" fadein 7
        "The patients' rooms hallway."
        "Every time I pass through this place, I feel uneasy..."
        "XVII, XVI..."
        scene bg closeXV with dissolve
        "...Room XV."
        "It won't leave me alone."
        "Should I just ignore it?"
        menu:
            "Approach the door":
                "No. I can't keep pretending he doesn't exist."
                "This... must be as difficult for him as it is for me."
                "It would be cruel of me not to help him now."
                "...to leave him."
                m sadtalk "Michael?"
                ##inside room cg?
                show bg closeXV2 with dissolve
                dv "...[name]? Is that really you?"
                "He looks straight at me."
                "Even though I can't see his face, a shiver runs down my spine."
                "It reminds me of our first session..."
                "\"Stay calm. He can't hurt you\", I told myself."
                "Well, now he can't."
                m talk "I wasn't allowed to see you until the end of the week."
                dv "You..."
                dv "There must be something seriously wrong with you if you actually want to see me again after this."
                m fabtalk "I'm your psychologist - it's my job."
                dv "No, there's more to that, I know it... Anyone else would've left me by now."
                "He approaches the door. His face is inches away from the glass."
                dv "But you... you're different."
                dv "You said you \"care\". Is that it?"
                "I suppose he's right... I still care a lot about helping him."
                "I nod."
                m frusttalk "Michael, I won't give up on you like everyone else has."
                m angrytalk "With my help, you can leave this place for good. I swear."
                dv "Do you... really mean that? After what I've done?"
                m conf "Of course I do."
                "I step closer to the door."
                "I wish I didn't need to be so cautious around him, but the wound on my neck reminds me it's necessary."
                dv "When can I... see you again?"
                m talk "As soon as possible. I should be able to arrange it even tomorrow."
                dv "You... you'd do that for me?"
                m "I'll try."
                m serious "Are you... in the right state to see me so soon after... what happened?"
                dv "I think so. It's not like I need a week to recover or anything... by Wednesday I was already pretty much normal."
                "He lowers his voice."
                stop music fadeout 10
                dv "As long as you don't try to free me again, I'll be fine."
                "I nod."
                m angry "Got it."
                "I attempt to look at him more closely in the dim light."
                m serious "Are you hurt?"
                play music "ost/hospital.ogg" fadein 10
                "He shakes his head."
                dv "...heh. Depends on your definition of \"hurt\"."
                "I remember the last time he said that to me."
                dv "I wasn't hurt on Tuesday when I attacked you, if that's what you mean."
                "...oh."
                "Given how often he's been harming himself recently, I assume he's done it again."
                m talk "Will you be okay?"
                "He laughs."
                dv "You're kiddng, right? It's been worse, that's really nothing."
                "At least it should heal quickly."
                dv "Well..."
                dv "It's kind of late. Go home, enough pitying me for one day."
                m regrettalk "I..."
                dv "Come on, I'll be fine. You really should get going."
                m talk "If you say so..."
                "I move away from the door."
                m cute "I'll see you tomorrow ~"
                dv "Hey, [name]..."
                m gasp "Yes?"
                dv "Thanks for staying with me. I know it wasn't easy for you..."
                m frusttalk "Nonsense. I'll be fine."
                dv "You sound just like me..."
                stop music fadeout 5
                dv "Take care of yourself, [name]."
                m smile "You too."
                play music "ost/tran.ogg" fadein 6
                scene bg patients with dissolve
                "I walk away."
                "My mind feels a lot clearer after I decided to approach him."
                "It wasn't so scary, after all."
                scene black with dissolve
                "I'm not sure what I feared, really..."
                "It's not like he's changed in any way, since I just haven't seen that side of him yet."
                "The moment I considered freeing him, I acknowledged the risk of him attacking me."
                "And now that it's happened, we'll both be more careful."
                "Plus, having gotten to see him like this should help me understand exactly what he feels and how I can help."
                "I hope Dr. Sharpe lets me see him so soon..."
            "Don't":
                $DevilFail=True
                scene bg patients with dissolve
                "I keep my gaze on the floor and hurry through the hallway."
                "I don't want anything to do with him right now."
                "I'm just not ready to face him after this."
                scene black with dissolve
                stop music fadeout 5
                nt "I make my way outside and go home. Tomorrow I'll go back to the rest of my patients... the ones I can actually bring myself to talk to."
        jump nextday
    elif day == 19:
        if DevilFail:
            play music "ost/tension.ogg" fadein 5
            scene bg mcdark with dissolve
            "I've made up my mind. I can't handle Michael. I just can't."
            "I spoke to Dr. Sharpe before work and he agreed to assign Michael to one of the other psychologists, in recognition of the trauma went through."
            "I'll have someone new to work with soon."
            "I'll never have to see Michael again."
            jump patientsattack
        scene bg doctor with dissolve
        show d talk with dissolve
        d "Today?"
        show d neutral with dissolve
        play music "ost/hospital.ogg" fadein 10
        m conf "That's right."
        show d coldtalk with dissolve
        d "Are you sure you can handle seeing him so soon?"
        show d neu with dissolve
        m "Of course I can. The sooner the better."
        show d sidetalk with dissolve
        d "If you say so..."
        show d talk with dissolve
        d "You are free to keep seeing him as of today."
        show d neutral with dissolve
        m flirt "Thank you."
        stop music fadeout 5
        scene bg mc with dissolve
        "Alright then, I can see Michael again now."
        "Let's get back to work..."
        if easymeter:
            show screen easymeter
            show screen redmeter
        dv "I'm... back, I guess."
        play music "ost/neutral.ogg" fadein 8
        scene bg mcdesk with dissolve
        show dv frust with dissolve
        m serious "Are you alright?"
        show dv hes with dissolve
        dv "Yeah. Don't worry about me."
        show dv frust with dissolve
        m sad "...."
        "I want to comfort him somehow, but I remind myself to keep my distance."
        show dv neutral with dissolve
        "It feels so strange, being unable to touch him after these three days when he was free."
        "...What am I thinking? It's the way it has to be."
        stop music fadeout 3
        show dv hes with dissolve
        dv "[name]?"
        show dv frust with dissolve
        m talk "Yes?"
        show dv sadtalk with dissolve
        play music "ost/tension.ogg" fadein 5
        dv "You really... don't hate me now?"
        show dv angry with dissolve
        m fabtalk "No, why would I?"
        show dv angrytalk with dissolve
        dv "I hurt you... you should've given up on me by now."
        show dv siden with dissolve
        m talk "I told you, I'm not like your previous psychologists."
        show dv sidetalk with dissolve
        dv "I know you aren't..."
        show dv frusttalk with dissolve
        dv "Uh... What I said last time."
        show dv sadtalk with dissolve
        dv "...About it being personal."
        show dv angry with dissolve
        dv "I still... I meant that."
        show dv frust with dissolve
        "...."
        "I don't know how to feel about his confession from Tuesday... I almost forgot about it among everything else that happened."
        show dv angry with dissolve
        m regrettalk "I'm sorry if... I never responded to that."
        m frust "I just... I need time to think about... all of that."
        show dv angrytalk with dissolve
        dv "Why are you even apologizing?"
        show dv sadtalk with dissolve
        dv "...I wouldn't expect anyone to respond to something like that."
        show dv sad with dissolve
        menu:
            "I still really care about you":
                show dv angry with dissolve
                dv "You... You shouldn't say such things."
                show dv frusttalk with dissolve
                dv "It just... makes me want more from you."
                show dv frust with dissolve
                m sad "...."
            "I thought you weren't thinking straight":
                show dv neutalk with dissolve
                dv "I wasn't."
                show dv darkblush with dissolve
                dv "But..."
                show dv tsun with dissolve
                dv "...I've never been this honest before."
            "I don't want to rush it":
                show dv sidetalk with dissolve
                dv "I get it."
                show dv siden with dissolve
                m serious "No, really. I wouldn't want to say something that wouldn't be true, so I'd rather wait and make up my mind about it."
        stop music fadeout 6
        show dv frusttalk with dissolve
        dv "You really don't have to say anything like that to me."
        show dv devil with dissolve
        dv "It would be, uh... unprofessional."
        play music "ost/hospital.ogg" fadein 6
        "There's something odd about his behavior today."
        show dv siden with dissolve
        m fabtalk "Why aren't you looking at me today?"
        show dv darkblush with dissolve
        dv "I..."
        show dv sadtalk with dissolve
        dv "It's... that wound... on your neck."
        show dv frust with dissolve
        "Oh."
        stop music fadeout 5
        show dv sadtalk with dissolve
        dv "I don't... I can't look at it."
        show dv sad with dissolve
        m "Why is that?"
        show dv frusttalk with dissolve
        dv "I'm scared that... I may lose it again if I see it."
        show dv siden with dissolve
        m talk "It's barely visible now. You can look."
        show dv kh with dissolve
        dv "I... I can?"
        show dv sad with dissolve
        "I nod."
        play music "ost/tran.ogg" fadein 6
        show dv hes with dissolve
        dv "Oh."
        show dv neu with dissolve
        "He tilts his head a bit to look at it more closely."
        show dv talk with dissolve
        dv "It's..."
        show dv darkblush with dissolve
        dv "It looks like it was worse than I thought."
        show dv kh with dissolve
        m gasp "But... it's almost healed now..."
        show dv angrytalk with dissolve
        dv "I've seen enough wounds to know how that looked three days ago."
        show dv frusttalk with dissolve
        dv "That's... such a mess..."
        stop music fadeout 4
        show dv angrytalk with dissolve
        dv "I'm sorry, [name]. About everything I did that time."
        show dv sadtalk with dissolve
        dv "About... restraining you. And about, uhh... invading your personal space. A lot."
        play music "ost/hospital.ogg" fadein 6
        m pity "It's okay. I've already forgiven you for all of that."
        show dv gasp with dissolve
        dv "You... you have?"
        m talk "Of course."
        show dv frusttalk with dissolve
        dv "You shouldn't say these things so lightly."
        show dv angrytalk with dissolve
        dv "I wanted to kill you, [name]. If I were given the chance to, I would do that again."
        show dv notalk with dissolve
        dv "There's no way to stop me."
        show dv frusttalk with dissolve
        dv "There's no way... to control me."
        show dv sidetalk with dissolve
        dv "Can't you see? It's hopeless."
        show dv sad with dissolve
        m "It's not. There's still a way for me to help you."
        show dv talk with dissolve
        dv "What way?"
        show dv neutral with dissolve
        m "If I can get you used to everything that triggers these thoughts in a safe way, you won't have to be restrained anymore."
        show dv angrytalk with dissolve
        dv "There {i}is{/i} no \"safe way\" with me."
        show dv angry with dissolve
        m "I'll figure it out, trust me."
        show dv frust with dissolve
        dv "...."
        show dv sidetalk with dissolve
        stop music fadeout 6
        dv "Alright, whatever you want. It's not like I can do anything worse to you now."
        show dv sad with dissolve
        m conf "It'll be okay, I promise."
        show dv neu with dissolve
        play music "ost/ring.ogg"
        "Oh? My phone is ringing. Why now..?"
        "It's an unknown number."
        show dv neutral with dissolve
        "I glare at Michael."
        show dv smile with dissolve
        dv "Come on, don't mind me. It could be something important."
        show dv siden with dissolve
        m frust "I'll be quick."
        scene bg mc with dissolve
        "I get up from my chair and answer the phone."
        play music "ost/sunny.ogg" fadein 6
        show drk with dissolve
        m gasp "Hello?"
        nn "{i}This is Caroline. The one whose house you barged into last weekend."
        m talk "I recognized the voice. What is it?"
        cr "{i}Well, I... I've made up my mind."
        cr "{i}You can come to my house sometime, if you still want to."
        cr "{i}And we can, like... talk. About stuff."
        m cute "Of course I still want to. I'd love that."
        cr "{i}Jeez, you sounds so enthusiastic I'm starting to regret it..."
        cr "{i}Alright, I'll call you next week once I'm free. You can come if you really want to."
        m smile "Thanks -"
        "She hung up."
        "That was... unexpected."
        m regrettalk "Sorry about that."
        scene bg mcdesk with dissolve
        "I sit by my desk again."
        show dv sidetalk with dissolve
        dv "Are you sure you don't have anything to tell me, [name]?"
        show dv devil with dissolve
        m gasp "Huh?"
        show dv frusttalk with dissolve
        dv "You can't fool me... I'd recognize that voice anywhere."
        show dv smirk with dissolve
        dv "That was Caroline, right?"
        show dv smile with dissolve
        m talk "Yes. She just called me to say I can come talk to her sometime next week, if I still want to."
        show dv sidesmile with dissolve
        dv "Oh, that's great!"
        show dv talk with dissolve
        dv "You're... going to see her, right?"
        show dv neutral with dissolve
        m conf "Of course I am. I'd never miss an opportunity like that."
        show dv frusttalk with dissolve
        dv "Uhhh... when you see her, tell her that..."
        show dv neutalk with dissolve
        dv "Tell her I'm sorry, but I don't regret a thing."
        show dv sadtalk with dissolve
        dv "...Actually, just tell her I'm sorry. It'll be... better, I think."
        show dv neutral with dissolve
        m fabtalk "As you wish. I'll tell her."
        stop music fadeout 5
        show dv smile with dissolve
        dv "Thanks. And, uh... you'll have to tell me how she feels about... all of that."
        show dv sidetalk with dissolve
        dv "Caroline..."
        play music "ost/hospital.ogg" fadein 6
        show dv talk with dissolve
        dv "The strange thing is, all those three years I barely thought about her."
        show dv frusttalk with dissolve
        dv "But... after you freed me, I... it all somehow came back to me."
        show dv sadtalk with dissolve
        dv "All these feelings I... didn't really want."
        show dv kh with dissolve
        dv "And for a moment, I really felt guilt."
        show dv sadsmile with dissolve
        dv "...But it passed as quickly as it came."
        show dv sidesmile with dissolve
        m fab "I'm glad it did. You shouldn't dwell on the past too much."
        show dv neutalk with dissolve
        dv "Yeah, that's what I thought as well..."
        show dv sidetalk with dissolve
        stop music fadeout 4
        dv "Hey, can I ask you something? About Tuesday..."
        show dv angry with dissolve
        m talk "Go ahead."
        play music "ost/tension.ogg" fadein 6
        show dv frusttalk with dissolve
        dv "You... You didn't even try to struggle, or call for help..."
        show dv talk with dissolve
        dv "Why?"
        show dv neutral with dissolve
        menu:
            "I didn't want anyone to know what happened":
                show dv angrytalk with dissolve
                dv "Why..? That doesn't make any sense."
                show dv angry with dissolve
                m regrettalk "I wanted to protect you."
                show dv siden with dissolve
                dv "...oh."
                show dv sadtalk with dissolve
                dv "I..."
                show dv talk with dissolve
                dv "Thank you, [name]. I don't know what else to say."
            "I wanted to see what would happen":
                show dv frust with dissolve
                dv "That's..."
                show dv sadtalk with dissolve
                dv "You shouldn't have. Really."
                show dv angrytalk with dissolve
                dv "You knew nothing good would've come out of it... You should've at least tried to stop me."
            "I thought I could convince you to stop":
                show dv sidetalk with dissolve
                dv "Well..."
                show dv angrytalk with dissolve
                dv "You couldn't."
                show dv smile with dissolve
                dv "I wouldn't say it was worth a try, but I appreciate the effort. Thanks."
            "I enjoyed it":
                dv "Wait, {i}what?!"
                show dv angry with dissolve
                dv "Don't tell me you're..."
                show dv gasp with dissolve
                dv "Were you a freaking masochist the whole time and never bothered to tell me?"
                show dv cute with dissolve
                m tsun "No no, I didn't enjoy it {i}like that..."
                show dv neutral with dissolve
                m blushu "I meant... that..."
                m uncom "After not even being able to touch you for so long it felt very... intense."
                show dv frusttalk with dissolve
                dv "I get it. \"Intense\" is a good word for that."
                show dv neutral with dissolve
                m neu "So, until a certain point, I'd say I even enjoyed it."
                show dv smirk with dissolve
                m frust "...Which sounds weird now that I say it, considering what happened."
                stop music fadeout 6
                show dv sidesmile with dissolve
                dv "You're weird, [name]... Well, I guess not {i}that weird."
                show dv sadtalk with dissolve
                dv "Man, I wish there were more masochists willing to cooperate in this world..."
        play music "ost/neutral.ogg" fadein 8
        show dv neu with dissolve
        m talk "Can I ask you about it as well?"
        show dv neutalk with dissolve
        dv "Sure."
        show dv neutral with dissolve
        m uncom "How did you feel during the whole... attack? I couldn't quite tell."
        show dv siden with dissolve
        dv "...oh."
        show dv sidetalk with dissolve
        dv "That was a lot of different feelings at once."
        show dv sadtalk with dissolve
        dv "I'm not sure if I can name all of them... I'll try."
        show dv frusttalk with dissolve
        dv "At first, I... I tried to fight these thoughts about you..."
        show dv kh with dissolve
        dv "But when I saw how close you were and I realized you just touched me again, I..."
        show dv darkblush with dissolve
        dv "I couldn't really fight it anymore."
        show dv angrytalk with dissolve
        stop music fadeout 5
        dv "That was the moment when I realized I've lost and that you're going to get hurt."
        show dv talk with dissolve
        dv "At first, when I pinned you down, I..."
        show dv frusttalk with dissolve
        play music "ost/hospital.ogg" fadein 8
        dv "It was just like last time, with the nurses. Except a lot worse."
        show dv sadtalk with dissolve
        dv "Now that I had you for my own for once and I could do whatever I wanted to, I..."
        show dv angrytalk with dissolve
        dv "I couldn't decide. Too many thoughts rushing through my head."
        show dv frusttalk with dissolve
        dv "It... it hurt, [name]. It really did."
        show dv hes with dissolve
        dv "So I... I didn't do anything at first."
        show dv sadtalk with dissolve
        dv "I wanted it all to go away, so I laid my head on you."
        show dv talk with dissolve
        dv "I, uh... I'm sorry about that."
        show dv neutral with dissolve
        m talk "It's fine. Go on."
        show dv frusttalk with dissolve
        dv "It was... hearing your heartbeat so close to me was... calming."
        show dv notalk with dissolve
        dv "I... I felt like I could stay that way for... a really long time."
        show dv noeyes with dissolve
        "This is heartbreaking to listen to. I know that he can't be freed yet, but hearing this... really makes me want to do it again."
        show dv kh with dissolve
        dv "But... the thoughts came back. I don't remember everything that happened afterwards... it was a blur."
        show dv sadtalk with dissolve
        dv "I remember that... you tried to struggle at one point..."
        show dv neutalk with dissolve
        dv "Don't get me wrong, it's understandable, but..."
        show dv frusttalk with dissolve
        stop music fadeout 6
        dv "...I don't want to say that I enjoyed it, but I did."
        show dv frust with dissolve
        "...oh."
        show dv kh2 with dissolve
        dv "I... I also... remember the taste... of your blood."
        play music "ost/tension.ogg" fadein 6
        show dv neutral with dissolve
        m confusion "...."
        show dv sadtalk with dissolve
        dv "I-I mean... It's not easy to forget something like that."
        show dv siden with dissolve
        m serious "Is it... any different than yours?"
        show dv talk with dissolve
        dv "You know, it might just be psychological, but it varies a lot from person to person. At least for me."
        show dv neu with dissolve
        m neu "I... see."
        stop music fadeout 6
        "Another thing I probably will never understand, but I take note of what he said."
        show dv sadtalk with dissolve
        dv "I'm sorry if I... disturbed you by mentioning that."
        show dv frust with dissolve
        play music "ost/hospital.ogg" fadein 6
        m sadsmile "It's fine. I just... can't quite relate."
        show dv smirk with dissolve
        dv "Heh, not a lot of people can..."
        m fabtalk "Overall, would you say you, um... enjoyed that?"
        show dv sidetalk with dissolve
        dv "Not really. In the end, I never enjoy these things."
        show dv frust with dissolve
        dv "I may think I'm enjoying them at first, but... no."
        show dv angrytalk with dissolve
        dv "The danger is just too much for me to even consider enjoying that consciously."
        show dv neutral with dissolve
        m gasp "So it was just like the previous times when it happened?"
        show dv frusttalk with dissolve
        dv "...Actually."
        show dv sidesmile with dissolve
        dv "Who am I kidding..?"
        show dv neutalk with dissolve
        dv "To an extent, I'll admit that I enjoyed this one. Unlike the others."
        show dv neutral with dissolve
        stop music fadeout 4
        m fabtalk "What was different this time?"
        show dv hes with dissolve
        dv "...you."
        show dv frusttalk with dissolve
        dv "You were..."
        show dv darkblush with dissolve
        play music "ost/tension.ogg" fadein 5
        dv "...different."
        show dv noeyes with dissolve
        dv "...."
        show dv frusttalk with dissolve
        dv "I... think I should be leaving for today... If you don't mind."
        show dv neutral with dissolve
        m fab "I don't. Go ahead."
        scene bg mc with dissolve
        "I follow him to the door."
        "For some reason, I feel a sudden urge to do something... more than that."
        "Should I..?"
        menu:
            "Touch his shoulders":
                show drk with dissolve
                $RedHeart+=1
                "I place my hands on his shoulders."
                dv "[name]..?"
                m smile "Take care of yourself, Michael. I really forgive you."
                dv "...thanks."
                hide drk with dissolve
            "Touch his face":
                $RedHeart+=2
                show drk with dissolve
                "I let my fingertips brush against the small scar on his jaw."
                dv "Akhhh... [name], don't..."
                dv "I... I'm way too sensitive to that."
                hide drk with dissolve
                "He steps away from me, still glaring at me."
            "Don't":
                $professional+=1
                m talk "Goodbye, Michael. I'll see you tomorrow."
        stop music fadeout 6
        hide screen redmeter
        hide screen easymeter
        dv "...I really should be going now."
        play sound "doorclose.ogg" fadein 1
        "He leaves in a hurry."
        jump patientsattack
    elif day == 20:
        jump breakevent1
    elif day == 21:
        jump breakevent2
########################## WEEK IV       
    elif day == 22:
        scene bg mcliving with dissolve
        play music "ost/ring.ogg"
        "My phone is ringing."
        play music "ost/sunny.ogg" fadein 6
        m talk "Hello? Is this Caroline?"
        cr "{i}Who else?"
        cr "{i}Listen, if you really want to talk, come to my house tomorrow."
        cr "{i}If you have work, you can drop it if you really care that much - I don't."
        m talk "Is 10 AM alright?"
        cr "{i}Whatever."
        m fabtalk "I'll be there."
        "She hung up. That was quick."
        if SunLink>0 and social>0:
            pause 1
            "I remember Sue wanted to meet me today."
            if social>1:
                if social>2:
                    if social>3:
                        "Dr. Young and Julia apparently wanted to come with her as well."
                    else:
                        "Dr. Young planned to come as well."
                else:
                    "Julia is going to tag along as well."
            jump visitbreak
        jump nextday
    elif day == 23:
        jump carolinetalk
    elif day == 24:
        scene bg mcbed with dissolve
        play music "ost/emo.ogg" fadein 6
        "What... was that nightmare..?"
        "I can faintly recall... a woman? Sitting on..."
        "Bodies. They were moving, but looked long dead."
        "And the things she said to me... what does it mean?"
        "This is the third nightmare I have that seems oddly... out of place."
        "I never had nightmares like that before..."
        "...before I started working here."
        m no "Am I okay..?"
        "Or am I going insane? Something is definitely weird about these dreams..."
        "That last one must have to do with what I've learned about Michael yesterday."
        "It would be a lie to say that didn't change anything. Maybe..."
        "...maybe I'm afraid of going back to the hospital. Maybe I exaggerated everything in my head."
        "Still, it really doesn't {i}feel{/i} like a dream I could have. Something about it just feels so unfamiliar..."
        stop music fadeout 5
        "...."
        "\"Spit it out already, [name].\" I think to myself. \"It'll be easier once you say it\"."
        "It feels like someone else's dream. That's what makes me so uneasy."
        play music "ost/tension.ogg" fadein 6
        "In fact, all three of them do. But that's impossible, what am I thinking..?"
        "The only thing I can do is try to deal with what she's told me. Do I really believe her?"
        "And should I ask Michael about it directly?"
        "If he really..."
        "No, I can't assume that yet. I need to know, but I'll have to be careful."
        "I don't want to lose his trust."
        stop music fadeout 5
        scene black with dissolve
        "God, why does it have to be so difficult..?"
        "Right when I thought I knew how to help him, that I understood him..."
        m no "Michael, you better have an explanation for this."
        jump janeback2
    elif day == 25:
        jump breakevent3
    elif day == 26:
        jump mysterycall
    elif day == 27:
        jump gmeeting
    elif day == 28:
        jump breakend

label devilaftertalk1:
    scene bg sunset with dissolve
    play music "ost/hospital.ogg" fadein 10
    "I lock up my office for the day and make my way outside." 
    "I can't stop thinking about what Michael told me today... He's in so much pain right now..."
    "I have to find a way to help him. Finding that Caroline girl might be a good idea, just to learn some things, but I need to act."
    "Something needs to be done... something that none of his previous psychologists thought of."
    "He fears losing control and hurting someone he cares about - but how can that be changed?"
    "First of all, I won't go anywhere with this if I don't make him care again... But how?"
    "He's made it clear that he's not willing to start feeling like that again. He's given up fighting his illness a while ago... what could give him the strength to keep struggling?"
    "...what would be worth the pain he would go through because of the guilt and fear?"
    "I haven't found my answer yet, but this must be the way to saving him, I'm sure of it."
    jump nextday
label devilinchains:
    $submissive+=3
    scene bg mcdesk with dissolve
    show dv breath with dissolve
    "He takes a deep breath."
    show dv devil with dissolve
    dv "For a moment, I thought you were really going to do it... You scared me..."
    show dv smirk with dissolve
    m serious "You're probably right - it's way too early to make such a decision."
    "He nods."
    show dv talk with dissolve
    dv "Definitely."
    show dv sidetalk with dissolve
    dv "Hell, I don't think I'll {i}ever{/i} be ready for something like that..."
    show dv sadsmile with dissolve
    "He laughs, but I feel as though he's telling the truth."
    "What if I never get to free him now? What if he'll have to spend the rest of his life like this..?"
    "No, what am I thinking? Freeing him now would be ridiculously risky."
    "Besides, I haven't even asked the rest of the staff about it."
    "I shouldn't rush it. I really shouldn't."
    show dv neu with dissolve
    "We spend the rest of the session commenting on what he's told me yesterday."
    show dv talk with dissolve
    dv "I'll see you next week, then."
    show dv neu with dissolve
    m gasp "Oh, right. It's Friday."
    show dv smile with dissolve
    dv "Heh. I'll miss you ~"
    play sound "doorclose.ogg" fadein 1
    scene bg mc with dissolve
    "He leaves. I'm not sure if he really meant it or not, but I smile to myself."
    hide screen easymeter
    hide screen redmeter
    jump breakchoice
label carolineweekend: ##Act I, shutting the door on MC
    scene black with dissolve
    play music "ost/mc.ogg" fadein 6
    "It's Saturday already."
    "I promised Michael I'd look for his past girlfriend, Caroline, today."
    "I kept my word - it didn't take long to learn that she still lives where she used to."
    "I decided to take a bus to the city and find her house there."
    scene bg sun with dissolve
    "While walking through the streets, I wonder - was this really a good idea?"
    "Based on the fact that she's made no attempts at contacting him after what happened three years ago, I'd assume she doesn't want anything to do with him."
    "It's understandable, really..."
    "Though she does possess information that's vital to my research."
    "And if she's willing to cooperate with me, I'll be able to learn what really happened - by confronting both of their versions of events."
    "This is it. This must be her house."
    play sound "knock.ogg" fadein 2
    stop music fadeout 5
    "I knock on the front door."
    cr "One moment!"
    "I hear rushed footsteps before the door opens."
    show caroline with Dissolve(1.0)
    $renpy.pause()
    cr "...."
    m neu "...."
    "I pictured her a lot differently."
    "She seems young, definitely younger than me."
    m fabtalk "Caroline Reed?"
    cr "Yeah, that's me. What do you want?"
    m conf "I'm [name] Hart. I work as a psychologist at St. Augustine's hospital."
    cr "...oh."
    play music "ost/tension.ogg" fadein 6
    cr "It's... about {i}Him{/i}, isn't it?"
    "I nod."
    cr "How come none of you guys ever bothered me in three years, and suddenly you're here? What is this?"
    m talk "I've only started working there."
    cr "Oh great, so you're new. You wanna impress your boss or something?"
    cr "Listen. If I wanted to talk to any of you, I would've gone there myself."
    cr "I don't want any more of your fucked up shit in my life. I thought that much was clear."
    cr "Get lost."
    "I take a step back."
    m fabtalk "In case you change your mind, here's my phone number - your help would be greatly appreciated."
    cr "Yeah, right."
    "She looks at it as if she's going to throw it away at any moment."
    play sound "doorclose.ogg" fadein 1
    scene black with dissolve
    stop music fadeout 5
    nt "She shuts the door on me."
    nt "That didn't go well... But what did I expect? What Michael put her through three years ago must've been really traumatic for her."
    play music "ost/hospital.ogg" fadein 5
    nt "I can't blame her for wanting to stay as far away as possible from him."
    nt "Still, if she rethinks it, maybe she could help me despite everything."
    nt "I should get going."
    nt "It was worth a try - I should let Michael know what happened on Monday."
    $persistent.Caroline=True
    show screen notify("{size=24} Your Characters Info screen has been updated!")
    jump nextday
label devilhierright:
    show d coldtalk with dissolve
    d "And do you believe this was your only option?"
    show d neutral with dissolve
    "I nod."
    m angrytalk "I needed to get him to realize that he has to {i}want{/i} to change in order to get better."
    m serious "And no progress could've been made in his current state."
    show d sidetalk with dissolve
    d "Well then..."
    show d coldtalk with dissolve
    d "I am sure you realize the danger you have caused to the whole hospital today."
    show d regrettalk with dissolve
    d "If it wasn't for these few nurses who were nearby and barged into your office, there's no telling what could have happened because of your irresponsibility."
    show d frust with dissolve
    m sad "I understand. I'm really sorry."
    m regrettalk "I was sure I had everything under control until... I didn't."
    show d neutalk with dissolve
    d "Make no mistake, I understand your point of view perfectly. And I have no right to fire you, given the circumstances."
    show d talk with dissolve
    d "Mr. Burnett is merely one of the patients you need to be especially careful around."
    show d calmsmile with dissolve
    d "Regardless of today's incident, I admire the direction you are going in. I believe you are still the most fit to work with him."
    show d foctalk with dissolve
    d "However..."
    show d frusttalk with dissolve
    d "A few days of rest might be beneficial for both of you after this."
    show d talk with dissolve
    d "I would advise you not to see him for the rest of this week."
    show d calmtalk with dissolve
    d "Take as much time as you think is necessary."
    show d calm with dissolve
    "That's... surprisingly considerate of him."
    show d neu with dissolve
    m smile "Thank you."
    show d talk with dissolve
    d "You are free to leave for the day. You should rest."
    show d neutral with dissolve
    "He stands up to follow me to the door."
    show d cold with dissolve
    "He's oddly silent for a moment."
    show d regrettalk with dissolve
    d "How is the wound on your neck? The nurses informed me it was quite troublesome for them."
    show d regret with dissolve
    m frusttalk "It's... it's really nothing, it should heal in a few days."
    show d frusttalk with dissolve
    d "...I am relieved to hear that. I would hate for any of the staff to have to come to work injured."
    show d neutral with dissolve
    "I nod quickly and move towards the door to leave."
    show d neutalk with dissolve
    d "One more detail, Ms. Hart."
    show d sidetalk with dissolve
    d "A piece of advice, if you will."
    show d neu with dissolve
    m sadtalk "What is it?"
    "He steps closer to me and lowers his voice."
    show d sidetalk with dissolve
    d "I never said I disapproved of you releasing him."
    show d calmtalk with dissolve
    d "Although today may have been too early, if the time is right, and with proper caution, it would be beneficial to do it eventually."
    show d neu with dissolve
    "For a moment, I'm completely shook."
    m boretalk "I... thought I wasn't allowed to free him at all..." 
    show d calmsmile with dissolve
    "He chuckles."
    show d smirk with dissolve
    d "That is exactly why you should have come here in the first place, before making that choice."
    show d sidetalk with dissolve
    d "Though I cannot predict if the other psychiatrists here would approve of it, given Mr. Burnett's... history, I still encourage you to release him, when the time is right."
    show d frusttalk with dissolve
    d "But this should not get out of my office. Do you understand?"
    show d cold with dissolve
    "Sounds fair, to be honest."
    "Turns out the only problem was that he attacked me."
    "That makes things a bit easier for me in the future, if I ever deem him stable enough to consider releasing him again."
    "I'm glad to at least have his approval."
    show d smirk with dissolve
    m smile "Thank you, Dr. Sharpe. I'll make sure to be very careful in the future."
    show d calmtalk with dissolve
    d "Whatever it takes to help, as long as you do not endanger other patients or any of the staff, yourself included."
    show d regrettalk with dissolve
    d "I do not think I could cover it up as easily if you caused another incident."
    show d neutral with dissolve
    "I nod and open the door to leave."
    stop music fadeout 7
    show d calmtalk with dissolve
    d "Goodbye, Ms. Hart. You are excused from work for the rest of the day."
    show d neu with dissolve
    m talk "Goodbye."
    play music "ost/hospital.ogg" fadein 8
    scene bg offices with dissolve
    "That went a lot better than I expected it to."
    "Dr. Sharpe didn't even seem mad at me."
    scene bg central with dissolve
    "I remind myself that even if he didn't \"seem\" angry, he might've been."
    "I mean, he has every right to be disappointed at least - I put a lot of people in danger and..."
    "Ugh, there's no point overthinking it. I can't let it happen again."
    "Though he let me free Michael again sometime... I guess that's a possibility for the future."
    scene bg patients with dissolve
    "All this time, I didn't consider what happened to Michael after he attacked me."
    "I assume he was restrained again and taken back to his room."
    "XV... it's empty. They must've moved him to XXI temporarily."
    "I hope he recovers from this quickly and I can keep seeing him."
    "I don't think I should really blame him for what happened... I knew he's capable of such things..."
    "So why do I suddenly feel unsettled at the prospect of seeing him again after this?"
    "I guess... talking about it is one thing, and actually falling prey to him is completely different."
    "Regardless, I'll have a few days to rethink everything carefully. I should clear everything up by then."
    jump nextday
label devilhierfail:
    show d foc with dissolve
    m regrettalk "He... He forced me to free him."
    show d frusttalk with dissolve
    d "And how exactly did he achieve that?"
    show d cold with dissolve
    m sadtalk "He made it seem like... there was no other way to help him."
    m frust "And I didn't think to refuse..."
    show d sadtalk with dissolve
    d "Ms. Hart..."
    show d frusttalk with dissolve
    d "If you were being pressured by a patient, you should have come to me before taking any actions."
    show d cold with dissolve
    m regret "I understand."
    show d sidetalk with dissolve
    d "I will not fire you for this incident, but it would be unwise to allow you to keep working with Mr. Burnett after what transpired today."
    show d neutral with dissolve
    "I take a deep breath. So that's how it is..."
    "I thought I could talk my way out of this somehow by blaming him - after all, he was already guilty of attacking me."
    "Turns out my strategy was wrong."
    "I'll never see Michael again."
    scene black with dissolve
    $DevilFail=True
    jump nextday
label devilhierfired:
    show d sidetalk with dissolve
    d "I do not think you are fit to keep working here."
    show d coldtalk with dissolve
    d "If you cannot handle your own responsibilities, there is no point keeping you here."
    show d frusttalk with dissolve
    d "I have no choice but to fire you."
    show d cold with dissolve
    d "You are of no use to this institution in your current state."
    "Oh no..."
    stop music fadeout 5
    show d sadtalk with dissolve
    d "Leave, Ms. Hart. I am sorry it had to come to this."
    scene fired with dissolve
    "You were fired. Return to your last save file and make different choices to alter your ending."
    return
label carolinetalk: 
    scene bg sun with dissolve
    play music "ost/tran.ogg" fadein 8
    "I'm on my way to Caroline's house. I have so many questions I need to ask her..."
    "I hope I can get some useful information out of her."
    "It's a rare opportunity to look at Michael from a different perspective."
    "He {i}actually hurt her..."
    "Not like he hasn't done the same to me, but... I feel like what happened to her was a lot worse."
    "Probably a lot more conscious on his part, too, which scares me a little."
    scene black with dissolve
    nt "It's not the same Michael I know... This is going to be difficult."
    play sound "knock.ogg"
    pause 1
    stop music fadeout 5
    cr "Coming..."
    play sound "doorclose.ogg" fadein 1
    nt "She opens the door for me and lets me inside."
    scene bg caroline with Dissolve(1.0)
    play music "ost/neutral.ogg" fadein 8
    m sidesmile "Thank you for letting me talk to you about this. I know it must've been hard..."
    show cr talk:
        ypos 5
    with dissolve
    cr "Skip the pleasantries, Ms. Psychologist. Why are you here?"
    show cr neutral with dissolve
    m talk "I wanted to hear about what happened three years ago. And the year before that."
    show cr sidetalk with dissolve
    cr "Has he told you about it?"
    show cr angry with dissolve
    m "He has. But I only heard it from his point of view."
    show cr frusttalk with dissolve
    cr "Bullshit."
    show cr frust with dissolve
    m gasp "Excuse me?"
    show cr trigger with dissolve
    cr "Haven't you noticed? How can you even believe someone like him?"
    show cr angry with dissolve
    m serious "I don't quite understand -"
    show cr frusttalk with dissolve
    cr "He's completely insane. Fucking delusional."
    show cr neutral with dissolve
    m neu "Actually, I don't think that's..."
    stop music fadeout 6
    show cr sidetalk with dissolve
    cr "Stop it with the excuses. I know what he's really like."
    show cr frust with dissolve
    m "...."
    m sadtalk "I'm truly sorry about what he's done to you."
    play music "ost/hospital.ogg" fadein 8
    m regret "All I want is to ensure that it never happens again."
    show cr talk with dissolve
    cr "Good luck with that. He can't be stopped."
    show cr neu with dissolve
    m fabtalk  "What do you mean?"
    show cr sidetalk with dissolve
    cr "It's incurable, isn't it? At least in his case."
    show cr neutral with dissolve
    m angry "It can definitely be controlled with enough time and effort."
    show cr evil with dissolve
    cr "Don't make me laugh... So you want to tame him? Like I had?"
    m talk "You didn't know about his illness."
    show cr baka with dissolve
    cr "Does it matter? I knew what he's like. And I know it can't change."
    show cr neu with dissolve
    m fab "Can you tell me about how you two met? What was he like back then?"
    show cr talk with dissolve
    cr "Different, let me tell you that."
    show cr frusttalk with dissolve
    cr "It was... 8 years ago."
    show cr siden with dissolve
    cr "I was 17, he was 18."
    show cr sadsmile with dissolve
    cr "I don't know what I saw in him... I must've been really dumb back then."
    show cr trigger with dissolve
    cr "...What's that look for?"
    m frustsmile "He said the same thing once. That he's made a lot of stupid choices."
    show cr sidesmile with dissolve
    cr "I bet."
    show cr frusttalk with dissolve
    cr "I... I don't know, I just..."
    stop music fadeout 5
    show cr angrytalk with dissolve
    cr "Jeez, I liked him, alright?! I was a stupid teenager."
    show cr baka with dissolve
    m neutral "I get it."
    play music "ost/memory.ogg" fadein 10
    show cr talk with dissolve
    cr "I knew he'd never had a girlfriend before, so I thought if I just told him, he wouldn't have any reasons to reject me."
    show cr regret with dissolve
    cr "But... I was so scared to talk to him."
    show cr sidetalk with dissolve
    cr "I don't know, I guess we were friends but we weren't all that close."
    show cr frust with dissolve
    cr "And there was always this sense of... weirdness to him."
    show cr talk with dissolve
    cr "Like, you never knew what he'd do. Totally unpredictable."
    show cr frusttalk with dissolve
    cr "Most of the time, he was really quiet and all, but when he did speak up..."
    show cr neu with dissolve
    cr "We were all shocked. I mean, not always in the bad way."
    show cr regrettalk with dissolve
    cr "The point is - he wasn't one of the people you just walk up to and tell this stuff to."
    show cr neutral with dissolve
    m uncom "I understand. So why did you confess after such a long time?"
    show cr frust with dissolve
    cr "I, uh... I was meeting some old friends from school. We hadn't seen each other for a few years."
    show cr talk with dissolve
    cr "I was already a bit more, um, experienced than I was back when we met."
    show cr sidetalk with dissolve
    cr "So I thought it's not all that intimidating anymore and I told him."
    show cr neu with dissolve
    cr "Honestly, my friends convinced me. They knew I had this crush on him for years."
    show cr angrytalk with dissolve
    cr "So, I finally got a grip and told him."
    show cr regret with dissolve
    cr "And it was the worst mistake I've ever made."
    show cr frusttalk with dissolve
    cr "I should've avoided people like him from the start."
    show cr angry with dissolve
    m fab "\"Like him\"?"
    show cr frustsmile with dissolve
    cr "Oh come on, you know what I mean."
    show cr neu with dissolve
    cr "You could just see there was something wrong with him."
    show cr sidetalk with dissolve
    cr "Could never focus on anything, I felt like he wasn't actually listening to me whenever I talked to him."
    show cr regret with dissolve
    cr "He was always... somewhere else. Like nobody else even existed most of the time."
    show cr neu with dissolve
    m talk "I see. At that time, have you ever seen him experiencing strong emotions?"
    show cr sidetalk with dissolve
    cr "No. It was like he never felt anything."
    show cr angry with dissolve
    cr "I could never tell what he was thinking, and that annoyed the shit outta me."
    show cr talk with dissolve
    cr "Why do you ask? What's he like now?"
    show cr neutral with dissolve
    m "Based on what I've heard from you and what I've seen, he's changed a lot."
    m fabtalk "He's gotten a lot more... talkative, I think."
    show cr sidetalk with dissolve
    cr "Sounds contradictory to me. It was always such a pain to get him to say anything more than what was necessary."
    show cr neutral with dissolve
    m talk "How did you feel when he accepted your feelings?"
    show cr sidesmile with dissolve
    cr "What can I say? I was happy. How could I'd known what would happen?"
    m boretalk "Can you describe your relationship from your point of view?"
    show cr neutral with dissolve
    cr "Compared to my other boyfriends, he was... a lot less affectionate."
    show cr siden with dissolve
    cr "Like he wanted to get away from me half the time."
    show cr angrytalk with dissolve
    cr "God dammit, if he agreed to be with me, what harm would it do him to act like it?"
    show cr talk with dissolve
    cr "...At least, that's what I thought of it then."
    show cr siden with dissolve
    cr "Still..."
    show cr neutral with dissolve
    cr "If I were him, I wouldn't try to trick people into thinking I'm normal."
    show cr frust with dissolve
    "She pauses and looks out the window, clearly irritated."
    show cr frusttalk with dissolve
    cr "He could've said \"no\" and it would've been over."
    show cr angry with dissolve
    m sad "Do you think you may have pressured him to agree?"
    "That's how he justified it, at least."
    stop music fadeout 6
    show cr frustsmile with dissolve
    cr "\"Pressured him\"? Is that a joke?"
    show cr trigger with dissolve
    cr "How could I expect anyone to be this impressionable? If he didn't want me, it was his choice."
    show cr neutral with dissolve
    play music "ost/neutral.ogg" fadein 6
    m regrettalk "He didn't want you to feel rejected and think it was your fault."
    show cr frustsmile with dissolve
    cr "So he was with me out of pity? That's just great."
    show cr angrytalk with dissolve
    cr "Tell me, Hart. Did he even love me?"
    show cr neutral with dissolve
    "I think back to what he said..."
    m bored "He tried to."
    show cr siden with dissolve
    "She scoffs."
    show cr frusttalk with dissolve
    cr "So he's not even capable of that. I should've guessed."
    show cr angry with dissolve
    m fabtalk "So you weren't satisified with your relationship because of him?"
    show cr baka with dissolve
    cr "I mean... I guess it couldn't have been that bad... if I lasted a whole year with him."
    show cr regret with dissolve
    "She could've ended it as well as him, if she felt unhappy."
    "I know she's the victim in this, but I can't help but be on his side..."
    "I can't stop myself from defending him."
    stop music fadeout 5
    "Get a grip, [name], you're supposed to be the objective one..."
    m neutral "Did you love him, then?"
    show cr gasp with dissolve
    play music "ost/tension.ogg" fadein 6
    cr "A- Why would you want to know that?"
    show cr angrytalk with dissolve
    cr "Of course I did, you idiot! Before he turned out to be a fucking murderous psychopath!"
    show cr frust with dissolve
    m neu "So you loved the person you thought he was."
    show cr trigger with dissolve
    cr "Are you serious? Who would ever love a monster like him?!"
    "...."
    show cr siden with dissolve
    "It doesn't feel right to call him a monster, even after everything he's done."
    stop music fadeout 5
    show cr neutral with dissolve
    m sadtalk "Did you never notice him acting like something is wrong? In regards to his illness, I mean."
    play music "ost/rev.ogg" fadein 8
    show cr frusttalk with dissolve
    cr "Ummm... he was always kind of a freak, anyway. Everyone knew that much."
    show cr frust with dissolve
    "I'm not sure why I feel insulted by that."
    show cr neu with dissolve
    cr "I knew he was probably sort of weird from the start, so I wasn't particularly surprised when he started acting different around me after we started dating."
    m frust "\"Different\"?"
    show cr talk with dissolve
    cr "He got more paranoid around me. And even quieter."
    show cr frusttalk with dissolve
    cr "I kind of assumed he was just nervous since I was his first and all, on top of him being asocial as fuck."
    show cr neutral with dissolve
    m fabtalk "Were you usually the one to take the initiative in your relationship?"
    show cr trigger with dissolve
    cr "Always. He was so indecisive..."
    show cr baka with dissolve
    cr "Like he didn't even know what he wanted from me."
    show cr angry with dissolve
    "That sounds nothing like the Michael I know."
    m angry "Did it ever seem like he was holding back around you for some reason?"
    show cr neu with dissolve
    "She's silent for a moment."
    show cr sidetalk with dissolve
    cr "I know what you mean, now that I know how fucked up he was the whole time, but..."
    show cr talk with dissolve
    cr "No. It never occured to me."
    cr "If anything, I'd say he seemed uninterested in me."
    show cr frust with dissolve
    cr "Ughh..."
    m talk "What is it?"
    show cr trigger with dissolve
    cr "I know people like that. Ones who are into the kinky shit."
    show cr regret with dissolve
    cr "If he'd just told me that, I wouldn't hold it against him, I guess."
    show cr angrytalk with dissolve
    cr "But he... it wasn't just that. He's bloodthirsty, seriously. And that's not something you just accept and move on."
    show cr angry with dissolve
    m boretalk "Of course. But he never told you, anyway."
    show cr gasp with dissolve
    cr "Exactly."
    show cr neutral with dissolve
    m fab "And you really never noticed the marks on his skin?"
    show cr talk with dissolve
    cr "Not once. At least, not for long enough to realize what they were."
    show cr sidetalk with dissolve
    cr "Actually..."
    show cr neu with dissolve
    cr "I think... everything he did was calculated for me not to notice it."
    show cr frusttalk with dissolve
    cr "I can't wrap my head around how he did it, but I never noticed it."
    show cr frust with dissolve
    m neutral "He showed them to you afterwards?"
    show cr neu with dissolve
    cr "Yes. All of them."
    m serious "How bad is it?"
    show cr sidetalk with dissolve
    cr "He's pretty much butchered all over."
    show cr regret with dissolve
    cr "Makes me sick that someone would do that to anyone."
    stop music fadeout 5
    show cr neutral with dissolve
    cr "Though it would be better for everyone if he just stopped at himself."
    m neu "What do you mean?"
    play music "ost/emo.ogg" fadein 5
    show cr talk with dissolve
    cr "Is he suicidal?"
    show cr neu with dissolve
    m bored "...."
    show cr trigger with dissolve
    cr "What? You can't tell me? Then what reason do I have to trust you with any of this?"
    show cr angry with dissolve
    m frusttalk "...He is."
    show cr regrettalk with dissolve
    cr "Then why didn't he just kill himself when he had the chance?"
    show cr angrytalk with dissolve
    cr "Nobody else would have to get hurt then."
    show cr angry with dissolve
    "...."
    "No... {i}That's not right..."
    "If Michael heard this, everything I've been trying to accomplish with him would instantly be undone."
    m sadtalk "Caroline. I know how much you must hate him for what he's done, but do you really think he deserves to die?"
    show cr trigger with dissolve
    cr "More than I did. What did {i}I{/i} do to deserve what he's done?!"
    show cr frust with dissolve
    "...."
    m "Neither of you were fully at fault."
    show cr angrytalk with dissolve
    cr "Shut up!"
    show cr sad with dissolve
    cr "You don't even know what he's like."
    show cr sadtalk with dissolve
    cr "You don't {b}know him{/b}, [name]. Nobody does."
    show cr regrettalk with dissolve
    cr "But I've seen what he's really like. And I never want to see it again."
    show cr regret with dissolve
    "She thinks I can't understand her, as a psychologist who's only heard about what happened."
    stop music fadeout 5
    "I could prove her wrong and get her to trust me, but... there\'s a catch."
    menu:
        "{color=#f7663e}Show her the marks on my neck":
            m angrytalk "You're wrong. I've seen him out of control. Bloodthirsty."
            show cr trigger with dissolve
            cr "Oh, did you now? You don't -"
            play music "ost/ship.ogg" fadein 5
            show cr angry with dissolve
            "I let my hair drop down onto my back, revealing the marks still visible on the side of my neck."
            show cr neu with dissolve
            cr "...."
            show cr gasp with dissolve
            cr "When?"
            m talk "Last week."
            show cr neu with dissolve
            "She freezes."
            show cr trigger with dissolve
            cr "And... that's just teeth?"
            "I nod."
            show cr sadsmile with dissolve
            "She lets out a nervous chuckle."
            show cr regretsmile with dissolve
            cr "At least... at least he used knives on me."
            show cr angry with dissolve
            cr "Wait."
            show cr frusttalk with dissolve
            cr "Isn't he like, restrained, or something?"
            show cr neutral with dissolve
            "I decide to skip the details."
            m boretalk "Most of the time."
            show cr regrettalk with dissolve
            cr "...Did it hurt?"
            show cr sad with dissolve
            m frusttalk "Like hell."
            m uncom "I wasn't allowed to see him for two days afterwards."
            show cr angrytalk with dissolve
            cr "...And you still weren't discouraged? What the fuck is wrong with you?"
            show cr frust with dissolve
            stop music fadeout 6
            m sadsmile "I swore to myself I wouldn't give up until he's... \"normal\", I guess."
            show cr neu with dissolve
            "She stares at me, bewildered."
        "Don't":
            "It's too risky. Who knows how she might react."
            m conf "No, I don't know him. But I'm trying to understand."
    show cr sadtalk with dissolve
    cr "Why..?"
    show cr regrettalk with dissolve
    cr "I don't get it at all... For someone like him..."
    show cr neu with dissolve
    "She glares at me suddenly."
    play music "ost/tension.ogg" fadein 6
    show cr gasp with dissolve
    cr "...."
    show cr sadtalk with dissolve
    cr "...don' tell me."
    m serious "What is it?"
    show cr evil with dissolve
    cr "You... You like him, don't you? You actually like him!"
    m shock "W-{i}What?"
    show cr talk with dissolve
    cr "It's the only reason why you'd be so determined to help him. Why else would you try as hard for his sake?"
    show cr frustsmile with dissolve
    cr "Man, I thought you were one of those annoying perfectionists..."
    "...."
    "She's wrong."
    show cr neu with dissolve
    m frust "I'm doing this because I don't want him to suffer."
    show cr talk with dissolve
    cr "Why?"
    show cr smile with dissolve
    m angrytalk "Because it's my job!"
    show cr regretsmile with dissolve
    cr "He's been there for three years, and somehow no other psychologist ever bothered to talk to me."
    stop music fadeout 6
    show cr angry with dissolve
    cr "There's a reason why I wanted so desperately for him to be admitted there."
    m gasp "You... wanted it?"
    play music "ost/emo.ogg" fadein 6
    show cr talk with dissolve
    cr "Haven't you heard?"
    show cr sidetalk with dissolve
    cr "There's rumors going around... about that hospital."
    show cr frust with dissolve
    cr "They say once you get there, you can't leave."
    "That's just nonsense. A lot of patients have left the hospital alive and well."
    show cr neu with dissolve
    cr "I wanted that to be his fate. I hope he never leaves that place."
    show cr angrytalk with dissolve
    cr "That he rots there for the rest of his pathetic life. Because he can't be cured."
    show cr frust with dissolve
    cr "There's no way."
    m regret "...."
    m frusttalk "It sounds unfair."
    show cr trigger with dissolve
    cr "What?"
    show cr angrytalk with dissolve
    cr "You want him to hurt even more people?"
    show cr frust with dissolve
    m serious "No. But... I'm sure I can help him."
    stop music fadeout 6
    m regrettalk "It's been going well until..."
    show cr neu with dissolve
    cr "Until he lost it again? I know how it is with him."
    play music "ost/tension.ogg" fadein 6
    show cr angry with dissolve
    cr "He will {i}never{/i} be normal. Never."
    show cr regrettalk with dissolve
    cr "You're just trying to make him something he's not. Just like I have."
    show cr sadtalk with dissolve
    cr "And in the end, he'll hurt you. He'll hurt you like he hurt me."
    show cr regretsmile with dissolve
    cr "Because it's just the way he is."
    m sad "...He said he's sorry. For what happened three years ago."
    show cr trigger with dissolve
    cr "He's \"sorry\"? That's it?"
    m talk "He had no control over what happened."
    show cr angry with dissolve
    cr "Do I look like I care?"
    show cr baka with dissolve
    cr "Seriously, what is it that you see in him? Even knowing what he's done?"
    m angry "Do I need a reason to want to help him?"
    show cr angry with dissolve
    cr "That's not what I asked."
    stop music fadeout 5
    m bored "...."
    "I don't know. I just want to save him from this hell he's in."
    play music "ost/ship.ogg" fadein 6
    show cr sidetalk with dissolve
    cr "Is it... that weird charm he somehow has when you least expect it?"
    show cr sadsmile with dissolve
    cr "Is it the way his eyes light up and the way he smiles when it's actually genuine..?"
    show cr regret with dissolve
    "She pauses."
    show cr sadtalk with dissolve
    cr "I get it, [name], I really get it."
    show cr frusttalk with dissolve
    cr "I've been there. I used to feel the same way."
    show cr regret with dissolve
    m gasp "But I-"
    show cr trigger with dissolve
    cr "Stop denying it and listen to me."
    show cr sadsmile with dissolve
    cr "I really thought he was something special. One of a kind."
    stop music fadeout 3
    show cr angrytalk with dissolve
    cr "That was before he tied me to a chair and cut me in more ways than I thought imaginable."
    play music "ost/rev.ogg" fadein 6
    show cr regrettalk with dissolve
    cr "You'll never understand what it's like."
    show cr trigger with dissolve
    cr "I've spent two weeks straight alone with that monster."
    show cr regrettalk with dissolve
    cr "He was nothing like what he seemed to be before. Nothing."
    show cr angrytalk with dissolve
    cr "Whatever it is you see in him now, forget about it before it's too late."
    show cr sidetalk with dissolve
    cr "And whatever you think you know about him, it's not real. He's just pretending to be whatever makes people trust him."
    show cr sadtalk with dissolve
    cr "He told me so! He told me it's true."
    show cr angry with dissolve
    m serious "What... did he tell you, exactly?"
    stop music fadeout 5
    show cr frusttalk with dissolve
    cr "That..."
    show cr regret with dissolve
    "She stutters and looks away for a moment."
    m sadtalk "Caroline..?"
    play music "ost/emo.ogg" fadein 5
    show cr angry with dissolve
    cr "...he wanted me to trust him. So it would be more fun to hurt me."
    "No. That can't be true..."
    show cr talk with dissolve
    cr "I wouldn't lie to you about it. You'll regret making my mistake."
    show cr frust with dissolve
    m fab "And what was your mistake?"
    show cr sidetalk with dissolve
    cr "Trusting him. Believing him when he said he loved me."
    show cr angrytalk with dissolve
    cr "Don't believe him, whatever he says to you."
    show cr regrettalk with dissolve
    cr "He's not capable of caring about anyone, much less of love."
    show cr neutral with dissolve
    cr "Even if by some miracle you get him out of that place, he won't be normal."
    m frust "...."
    show cr neu with dissolve
    m angrytalk "How do you know?"
    m boretalk "He wasn't in the state to make rational decisions three years ago."
    show cr gasp with dissolve
    cr "Was he?"
    show cr angrytalk with dissolve
    cr "How do you know what he's really like? How can you ever justify what he's done?"
    stop music fadeout 5
    show cr regrettalk with dissolve
    cr "And what do you think you call someone who was so well-prepared for kidnapping me, it's almost as if he's planned it for weeks?"
    show cr frust with dissolve
    m wut "What..?"
    play music "ost/tension.ogg" fadein 5
    show cr talk with dissolve
    cr "Knives and all, everything in a perfect order. And the knots on my hands - that was the work of someone fully committed to doing what he did."
    show cr trigger with dissolve
    cr "If {i}he{/i} didn't know what he was doing, then who does?"
    show cr evil with dissolve
    m shock "You... you can't mean that..."
    show cr frustsmile with dissolve
    cr "Of course he planned it all beforehand. Were you really stupid enough to think that he was acting on impulse?"
    show cr talk with dissolve
    cr "I can tell you that much - nothing he does is for no reason, with no purpose."
    show cr angry with dissolve
    cr "I knew him for years, and I've never seen him do anything \"on impulse\"."
    stop music fadeout 5
    menu:
        "Because you never saw him out of control":
            $professional+=1
            $RedHeart+=1
            m angrytalk "He's been acting on impulse his whole life. He never wanted any of that."
            play music "ost/neutral.ogg" fadein 8
            show cr trigger with dissolve
            cr "How do you know, anyway? You only know what he tells you."
            show cr angry with dissolve
            m talk  "I can tell when someone is hiding the truth from me."
            show cr frustsmile with dissolve
            cr "Really? We'll see what you say when you end up just like me."
        "So what if you never saw it?":
            m talk "That doesn't mean anything. You didn't know many things about him."
            play music "ost/hospital.ogg" fadein 6
            m regret "Like his illness. The scars on his forearms."
            m neutral "Out of the two of us, you're the one who doesn't really know him."
            show cr neu with dissolve
            "She glares at me with a blank expression."
            show cr sidetalk with dissolve
            cr "Really, Hart..? Now we're fighting over him? Count me out."
            show cr frust with dissolve
            m gasp "I'm not -"
        "Being with you broke him":
            $personal+=2
            $RedHeart+=1
            show cr trigger with dissolve
            cr "So now I'm the one at fault? Me?"
            play music "ost/tension.ogg" fadein 5
            show cr angrytalk with dissolve
            cr "Tell me, what did I ever do to hurt him?"
            show cr angry with dissolve
            m regret "...."
            show cr frusttalk with dissolve
            cr "Nothing? That's right. He's the one to blame for all of this."
            show cr frust with dissolve
            m sadtalk "You didn't hurt him. But he hurt himself because of you. Because he cared too much about you."
            show cr trigger with dissolve
            cr "You {i}dirty little -"
            "She stops."
            show cr frust with dissolve
            cr "Nevermind. Say what you want about him, it's not my fault if you end up hurt next."              
        "{color=#ed1e02}Stay silent":
            play music "ost/neutral.ogg" fadein 6
            show cr frust with dissolve
            cr "...."
    show cr angrytalk with dissolve
    cr "Whatever. If you want to be a stubborn idiot, be my guest."
    show cr neutral with dissolve
    m boretalk "I wasn't trying to justify him."
    show cr trigger with dissolve
    cr "Then what do you want from me?"
    show cr angry with dissolve
    m angry "I want to know the truth. I need the truth."
    show cr frusttalk with dissolve
    cr "And I'm trying to warn you!"
    stop music fadeout 5
    show cr regret with dissolve
    "...."
    show cr angry with dissolve
    m talk "How severely did he hurt you in the end?"
    play music "ost/rev.ogg" fadein 8
    show cr sidetalk with dissolve
    cr "Not enough to kill me - he kept me alive on purpose."
    show cr frust with dissolve
    m regrettalk "If he'd killed you, he wouldn't be able to hurt you anymore."
    "I remember the strange dream I had recently, with a younger Caroline in it."
    "She was dead in that dream."
    show cr neutral with dissolve
    cr "Of course."
    m boretalk "Besides..."
    show cr neu with dissolve
    m angrytalk "He didn't want to kill you."
    "I refuse to believe that, despite everything she said. Even if he planned to kidnap her and lied to me, he couldn't have wanted to kill her."
    "Even if it was for a pragmatic, selfish reason, he didn't want it."
    show cr gasp with dissolve
    cr "Is that what he told you?"
    show cr frustsmile with dissolve
    "She scoffs."
    show cr trigger with dissolve
    cr "Like I could believe that!"
    show cr angry with dissolve
    cr "I've seen how he looked at me in the darkness - like he wanted to tear me apart. Like an animal about to devour me."
    "I have to stop trying to argue with her. I know she won't change her mind and I can't expect her to."
    m talk "Did he only cut you?"
    show cr evil with dissolve
    cr "Ha, I wish!"
    show cr sidetalk with dissolve
    cr "No. It was... a lot more than just that."
    show cr frust with dissolve
    cr "He, uh... bit me. A lot."
    show cr neutral with dissolve
    cr "Made me bleed to drink my blood. I don't know how I even survived this much blood loss."
    "I suppose he must know how to go about it, after hurting himself for so long and not sustaining any serious damage."
    show cr angrytalk with dissolve
    cr "It took months for all of that to heal."
    show cr frusttalk with dissolve
    cr "And I still have the scars... Nothing will remove them."
    show cr angry with dissolve
    cr "Just like nothing can change my mind about him and what happened."
    "...."
    m regrettalk  "Did he ever, umm... force you to..?"
    show cr neu with dissolve
    cr "No. Not a single time."
    show cr trigger with dissolve
    cr "Though I'd rather that than what he ended up doing - he nearly killed me, do you understand that?"
    show cr frust with dissolve
    "That's a bold statement, but I can see why she would prioritize her life in a situation like this."
    show cr sidetalk with dissolve
    cr "Besides. He seriously doesn't care about that."
    show cr talk with dissolve
    cr "All he wanted this whole time was to hurt me, so why would he want to do anything but that?"
    show cr angry with dissolve
    "True."
    m neu "How did you manage to escape?"
    show cr talk with dissolve
    cr "I got him to free my hands. He was getting less careful over time. Sloppy."
    show cr sidesmile with dissolve
    cr "It was just a question of waiting for the right time to ask him to free me."
    show cr frustsmile with dissolve
    cr "Heck, {i}beg him{/i} to free me."
    show cr talk with dissolve
    cr "You should know that he has a soft spot for being begged, one of the things I've learned over those two weeks."
    show cr smile with dissolve
    cr "Once I lowered his guard enough, I was able to free myself fully and slip out."
    show cr evil with dissolve
    cr "He was furious, I could tell."
    show cr sidetalk with dissolve
    cr "I knew that if he caught me trying to escape, he would kill me."
    show cr regret with dissolve
    "A feeling of pure dread washes over me when she says that. Would he really want to kill her for it?"
    "Suddenly, I'm glad that I decided not to struggle when he attacked me."
    show cr gasp with dissolve
    cr "You look... surprised. Of course he would've killed me."
    stop music fadeout 6
    show cr neu with dissolve
    cr "I wouldn't be surprised if I hadn't been the first."
    "No, he's not like that... is he?"
    "This conversation is starting to make me question everything I know about him."
    play music "ost/emo.ogg" fadein 6
    "I..."
    "No. I know what he's really like, I know he was at his lowest when he attacked me."
    "And I could see that he was far from controlling anything at that point."
    "I saw everything he was trying to repress when it took over."
    "He wasn't... angry, or hateful..."
    "He was just... desperate. For closeness. For someone to understand him."
    "I really felt like that was the case."
    "But... I have to confront him about what she said. I need to know if he planned to kidnap her from the start."
    show cr neutral with dissolve
    m talk "How would you feel if I managed to get him out of the hospital?"
    show cr sidetalk with dissolve
    cr "That's impossible. He wouldn't be able to function normally - he's a threat to everyone around him."
    show cr frust with dissolve
    cr "But, if you somehow managed that..."
    show cr neutral with dissolve
    cr "I'd want to see him again. Just to see if he even has any remorse."
    show cr regretsmile with dissolve
    cr "I doubt it."
    menu:
        "I'm really sorry":
            show cr neutral with dissolve
            m regret "I'm sorry it had to be you. I really am."
            m sadtalk "I shouldn't pick sides in this, and I won't. I only want to help my patient."
        "He regrets it so much":
            show cr angry with dissolve
            m regrettalk "It took him a lot of pain to talk about what happened three years ago."
            m sad "Especially about... how responsible he felt for everything."
            m talk "I really think he regrets what he's done. You were both placed in a very unfortunate situation."
            show cr frustsmile with dissolve
            cr "Keep telling yourself that, Hart. Sure."
    stop music fadeout 5
    m fabtalk "How has your life changed since what happened?"
    show cr siden with dissolve
    cr "Umm... a lot, I can tell you that."
    play music "ost/neutral.ogg" fadein 6
    show cr talk with dissolve
    cr "I... realized I can't trust people too much. Shouldn't believe them blindly."
    show cr frusttalk with dissolve
    cr "I changed my appearance. A lot. It's possible I would be unrecognizable to him after all this time."
    show cr siden with dissolve
    m gasp "Why is that?"
    show cr regrettalk with dissolve
    cr "I don't... want to look like the same naive teenage idiot who just wanted to be noticed by people."
    show cr neutral with dissolve
    cr "So I, uh... changed. I just did."
    show cr angrytalk with dissolve
    cr "I'm not the same person anymore, Hart."
    show cr neu with dissolve
    m fabtalk "If... it's not too personal of a question, have you been in a relationship since then?"
    show cr talk with dissolve
    cr "No. Didn't want to get too attached."
    show cr angrytalk with dissolve
    cr "And before you start yelling at me that it's some psychological trauma, I don't give a shit."
    show cr sidetalk with dissolve
    cr "It suits me. I like it better that way."
    show cr smile with dissolve
    m neu "No no, I understand."
    show cr frusttalk with dissolve
    cr "Well, that doesn't mean I've been avoiding... men in general. It's just better not to get too involved."
    show cr siden with dissolve
    m talk "And... would you say you're happy now? Despite what happened?"
    m fab "That you've... moved on with your life?"
    show cr regrettalk with dissolve
    cr "That's difficult, I don't know... Don't give me that, Hart."
    show cr neu with dissolve
    m neutral "Have you sought the help of a psychologist since then?"
    stop music fadeout 6
    show cr angrytalk with dissolve
    cr "No. I don't think I was the problematic one."
    show cr siden with dissolve
    "Hard to argue with that."
    play music "ost/tran.ogg" fadein 6
    show cr regrettalk with dissolve
    cr "I guess... life's easier once you know some things for sure."
    show cr frust with dissolve
    cr "I know what I want. And I know I don't need anyone else to be happy."
    m talk  "So your experiences with Michael, though surely traumatic, have taught you some things about life. And about yourself."
    show cr talk with dissolve
    cr "Yeah. I think I'm more... independent now."
    show cr neu with dissolve
    m cute "That's good to know."
    show cr evil with dissolve
    cr "In fact, tell him that. Tell him I'm happier than I've ever been, especially happier than I was with him."
    m flirt "I'll relay the message next time I see him."
    stop music fadeout 5
    show cr smile with dissolve
    cr "Good."
    show cr siden with dissolve
    "She's silent for a bit, waiting for my next question."
    play music "ost/hospital.ogg" fadein 6
    show cr neu with dissolve
    m talk "Caroline, unless you have anything else to add, I won't take up any more of your time."
    "I get up and head for the door."
    m smile "Thank you so much for agreeing to speak to me about your past."
    m neutral "I think it will benefit my work considerably."
    show cr baka with dissolve
    cr "...whatever."
    stop music fadeout 5
    show cr frust with dissolve
    "A final question comes to my mind."
    show cr angry with dissolve
    m fabtalk "Why did you agree to talk to me if you wanted nothing to do with him?"
    play music "ost/emo.ogg" fadein 6
    show cr frusttalk with dissolve
    cr "I... I guess... after something like that, I wanted some closure."
    show cr regret with dissolve
    cr "Some explanation about... why he did the things he did."
    m talk "And you deserve answers, really."
    show cr sad with dissolve
    m conf "If you ever want to talk, you can always call me. I'll gladly help."
    show cr sadsmile with dissolve
    cr "Thanks."
    show cr gasp with dissolve
    cr "Hey, listen..."
    show cr sidetalk with dissolve
    cr "If you actually do like him..."
    show cr talk with dissolve
    cr "Don't bother. I don't think he's even into, uh... normal things."
    show cr sidesmile with dissolve
    m neu "...."
    m talk "Well. I should get going now."
    show cr neu with dissolve
    m flirt "Thank you for your time."
    stop music fadeout 6
    show cr smile with dissolve
    cr "Don't get killed out there. You mean well, don't let him ruin it."
    play sound "doorclose.ogg" fadein 1
    scene black with dissolve
    nt "That was... actually way more informative than I expected it to be."
    play music "ost/tran.ogg" fadein 6
    nt "She was surprisingly talkative... she didn't hesitate telling me everything, even the hardest parts."
    nt "Caroline seems very straightforward and confident for someone who's been through what he's done to her."
    nt "I actually pictured her being more troubled by her past... If she is, she doesn't show it."
    nt "That said, making that huge a turn in one's way of acting seems like a response to trauma more than anything."
    nt "It's just like with Michael - he's also changed considerably after what happened three years ago."
    nt "It's fair to say she took it better than him, especially being the victim."
    nt "Except she was emotionally stable when it happened - he clearly wasn't."
    stop music fadeout 6
    scene bg sunset with Dissolve(1.0)
    "There's no judgement to be made here, but I have to wonder... Was she telling the truth about his intentions?"
    "I can't bring myself to consider Michael a bad person, despite everything.\nHe just seems... lost."
    "But I will have to ask him a thing or two regarding what she said. Maybe it would be a good place to start, once I'm back at work."
    jump motherharlot