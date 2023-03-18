default HangedShip = False
default HangedFail = False

image edward 1 = "cg/edward2.png"
image edward 2 = "cg/edward1.png"
image edward 3 = "cg/edward3.png"

image bg tom = "bg/Tom.png"

image jm neutral = "sprites/emperor/Neutral.png"
image jm talk = "sprites/emperor/Talk.png"
image jm smile = "sprites/emperor/Smile.png"
image jm smirk = "sprites/emperor/Smirk.png"
image jm gasp = "sprites/emperor/Gasp.png"
image jm happy = "sprites/emperor/Happy.png"
image jm neu = "sprites/emperor/Neu.png"
image jm neutalk = "sprites/emperor/NeuTalk.png"
image jm angry = "sprites/emperor/Angry.png"
image jm angrytalk = "sprites/emperor/AngryTalk.png"
image jm evil = "sprites/emperor/Evil.png"
image jm siden = "sprites/emperor/Siden.png"
image jm sidetalk = "sprites/emperor/SideTalk.png"
image jm sidesmile = "sprites/emperor/Sidesmile.png"
image jm sadsmile = "sprites/emperor/Sadsmile.png"
image jm sad = "sprites/emperor/Sad.png"
image jm sadtalk = "sprites/emperor/SadTalk.png"
image jm regret = "sprites/emperor/Regret.png"
image jm regrettalk = "sprites/emperor/RegretTalk.png"
image jm regretsmile = "sprites/emperor/Regretsmile.png"
image jm frust = "sprites/emperor/Frust.png"
image jm frusttalk = "sprites/emperor/FrustTalk.png"
image jm frustsmile = "sprites/emperor/Frustsmile.png"
image jm wink = "sprites/emperor/Wink.png"
image jm winkblush = "sprites/emperor/WinkBlush.png"
image jm cute = "sprites/emperor/Cute.png"
image jm kawaii = "sprites/emperor/Kawaii.png"
image jm laugh = "sprites/emperor/Laugh.png"
image jm blush = "sprites/emperor/Blush.png"
image jm laughblush = "sprites/emperor/LaughBlush.png"
image jm fun = "sprites/emperor/Fun.png"
image jm trigger = "sprites/emperor/Trigger.png"
image jm full = "sprites/emperor/Full.png"

image james:
    "gui/f/black.png" with Dissolve(0.2)
    "cg/James.png" with dissolve

label purplenotes:
    if month == 1:
        if day == 6 or day ==  7 or day == 13 or day == 14 or day > 17:
            jump purplenav
    if ntower1=="":
        $ntower1 = renpy.input("Note 1 (max 50 characters):", length = 50)
    else:
        if ntower2=="":
            $ntower2 = renpy.input("Note 2 (max 50 characters):", length = 50)
        else:
            if ntower3=="":
                $ntower3 = renpy.input("Note 3 (max 50 characters):", length = 50)
            else:
                if ntower4=="":
                    $ntower4 = renpy.input("Note 4 (max 50 characters):", length = 50)
                else:
                    if ntower5=="":
                        $ntower5 = renpy.input("Note 5 (max 50 characters):", length = 50)
                    else:
                        if ntower6=="":
                            $ntower6 = renpy.input("Note 6 (max 50 characters):", length = 50)
                        else:
                            if ntower7=="":
                                $ntower7 = renpy.input("Note 7 (max 50 characters):", length = 50)
                            else:
                                if ntower8=="":
                                    $ntower8 = renpy.input("Note 8 (max 50 characters):", length = 50)
                                else:
                                    if ntower9=="":
                                        $ntower9 = renpy.input("Note 9 (max 50 characters):", length = 50)
                                    else:
                                        if ntower10=="":
                                            $ntower10 = renpy.input("Note 10 (max 50 characters):", length = 50)
                                        else:
                                            if ntower11=="":
                                                $ntower11 = renpy.input("Note 11 (max 50 characters):", length = 50)
                                            else:
                                                if ntower12=="":
                                                    $ntower12 = renpy.input("Note 12 (max 50 characters):", length = 50)
                                                else:
                                                    if ntower13=="":
                                                        $ntower13 = renpy.input("Note 13 (max 50 characters):", length = 50)
                                                    else:
                                                        if ntower14=="":
                                                            $ntower14 = renpy.input("Note 14 (max 50 characters):", length = 50)
                                                        else:
                                                            if ntower15=="":
                                                                $ntower15 = renpy.input("Note 15 (max 50 characters):", length = 50)
                                                            else:
                                                                if ntower16=="":
                                                                    $ntower16 = renpy.input("Note 16 (max 50 characters):", length = 50)
                                                                else:
                                                                    if ntower17=="":
                                                                        $ntower17 = renpy.input("Note 17 (max 50 characters):", length = 50)
                                                                    else:
                                                                        if ntower18=="":
                                                                            $ntower18 = renpy.input("Note 18 (max 50 characters):", length = 50)
                                                                        else:
                                                                            if ntower19=="":
                                                                                $ntower19 = renpy.input("Note 19 (max 50 characters):", length = 50)
                                                                            else:
                                                                                if ntower20=="":
                                                                                    $ntower20 = renpy.input("Note 10 (max 50 characters):", length = 50)
                                                                                else:
                                                                                    "I've already filled up all my notes."
                                                                                    "Should I rewrite one of my notes?"
                                                                                    menu:
                                                                                        "[ntower1]":
                                                                                            $ntower1 = renpy.input("Note 1 (maximum 50 characters):", length = 50)
                                                                                        "[ntower2]":
                                                                                            $ntower2 = renpy.input("Note 2 (maximum 50 characters):", length = 50)
                                                                                        "[ntower3]":
                                                                                            $ntower3 = renpy.input("Note 3 (maximum 50 characters):", length = 50)
                                                                                        "[ntower4]":
                                                                                            $ntower4 = renpy.input("Note 4 (maximum 50 characters):", length = 50)
                                                                                        "[ntower5]":
                                                                                            $ntower5 = renpy.input("Note 5 (maximum 50 characters):", length = 50)
                                                                                        "[ntower6]":
                                                                                            $ntower6 = renpy.input("Note 6 (maximum 50 characters):", length = 50)
                                                                                        "[ntower7]":
                                                                                            $ntower7 = renpy.input("Note 7 (maximum 50 characters):", length = 50)
                                                                                        "[ntower8]":
                                                                                            $ntower8 = renpy.input("Note 8 (maximum 50 characters):", length = 50)
                                                                                        "[ntower9]":
                                                                                            $ntower9 = renpy.input("Note 9 (maximum 50 characters):", length = 50)
                                                                                        "[ntower10]":
                                                                                            $ntower10 = renpy.input("Note 10 (maximum 50 characters):", length = 50)
                                                                                        "[ntower11]":
                                                                                            $ntower11 = renpy.input("Note 11 (maximum 50 characters):", length = 50)
                                                                                        "[ntower12]":
                                                                                            $ntower12 = renpy.input("Note 12 (maximum 50 characters):", length = 50)
                                                                                        "[ntower13]":
                                                                                            $ntower13 = renpy.input("Note 13 (maximum 50 characters):", length = 50)
                                                                                        "[ntower14]":
                                                                                            $ntower14 = renpy.input("Note 14 (maximum 50 characters):", length = 50)
                                                                                        "[ntower15]":
                                                                                            $ntower15 = renpy.input("Note 15 (maximum 50 characters):", length = 50)
                                                                                        "[ntower16]":
                                                                                            $ntower16 = renpy.input("Note 16 (maximum 50 characters):", length = 50)
                                                                                        "[ntower17]":
                                                                                            $ntower17 = renpy.input("Note 17 (maximum 50 characters):", length = 50)
                                                                                        "[ntower18]":
                                                                                            $ntower18 = renpy.input("Note 18 (maximum 50 characters):", length = 50)
                                                                                        "[ntower19]":
                                                                                            $ntower19 = renpy.input("Note 19 (maximum 50 characters):", length = 50)
                                                                                        "[ntower20]":
                                                                                            $ntower20 = renpy.input("Note 20 (maximum 50 characters):", length = 50)
                                                                                        "Don't rewrite":
                                                                                            jump breaknav
    "Write another note?"
    menu:
        "Yes":
            jump purplenotes
        "No":
            if route=="purple":
                jump breakreal
            jump breaknav

label purplenav:
scene black with dissolve
pause 1
$firstpatient = "purple"
$sessions += 1
########################## 
if month == 1:
    if day == 8:
        $hanged = "Edward"
        play music "ost/neutral.ogg" fadein 6
        scene bg mcdesk with dissolve
        "I've decided to keep seeing Tom every day."
        "Edward told me on Friday that we likely won't see each other today, so I'm assuming it'll either be Tom or the one I have yet to meet."
        if easymeter:
            show screen easymeter
            show screen purplemeter
        m smile "Hello again."
        show t neutral with dissolve
        stop music fadeout 5
        "I greet Tom with a smile. He doesn't look very enthusiastic about talking to me again."
        show t angry with dissolve
        "He takes a seat."
        play music "ost/tension.ogg" fadein 5
        show t madtalk with dissolve
        t "What the hell have you DONE-?!"
        show t mad with dissolve
        "What...? Why is he angry with me?"
        m serious "What's wrong?"
        show t frusttalk with dissolve
        t "The others... You... {i}you let them..."
        show t frust with dissolve
        "He pauses. He's clearly upset, but I don't think this could've been avoided."
        show t hurt with dissolve
        t "I don't remember three days..."
        show t angrytalk with dissolve
        t "Which one was it?"
        show t angry with dissolve
        m neu "The second one."
        show t madtalk with dissolve
        t "Christ, what did he tell you? Did he...?"
        show t frusttalk with dissolve
        t "It doesn't matter. He would tell you anyway if I didn't..."
        show t hurttalk with dissolve
        t "So... it's better if I just... tell you the truth. About why I'm here."
        show t talk with dissolve
        t "Because if I don't, they'll do it and tell you more than you need to know."
        show t angry with dissolve
        "I'm surprised to hear that from him. He'll tell me everything?"
        "I suppose it's reasonable."
        stop music fadeout 15
        show t neutral with dissolve
        m talk "Please, go ahead. I'm listening."
        show t frusttalk with dissolve
        t "That's what bothers me..."
        show t talk with dissolve
        t "I guess I'll start from the beginning..."
        show t neutral with dissolve
        "He's silent for a while."
        show t trigger with dissolve
        t "I... God, I can't do it if you're staring at me like that..."
        show t frusttalk with dissolve
        t "Just try not to interrupt me later on, alright?"
        show t angry with dissolve
        "I nod. Despite everything, he seems reluctant to start talking."
        play music "ost/memory.ogg" fadein 10
        show pback 1 with dissolve
        t "I... I never knew my father. He left my mother when he learned of her pregnancy."
        t "And he never showed up again."
        t "My mother was very young back then and she, uh... she didn't take it that well."
        t "I think what happened with my father really affected her. She never fully recovered from being left on her own with a child she didn't really want."
        t "Looking back at it, I think she was ill... mentally, that is. But I couldn't know that then."
        t "She was very harsh on me. She would get angry over really irrelevant things..."
        t "I think she was just frustrated with her life, and everyone else."
        t "She never stopped hating my father for leaving her with me, and she couldn't do anything to get back at him, so..."
        t "I suppose it's only natural that her anger turned to me."
        "I remember our conversations from last week... I think I'm starting to piece it all together."
        m serious "Did it affect your life at school?"
        show pback 2 with dissolve
        t "It did... I couldn't focus on studying at home because of her."
        t "Sometimes I think all she wanted was to drag me down with her, so I would be as miserable as her..."
        t "I hated school. I spent every moment I could studying so I wouldn't fail every single test, since I couldn't do that at home."
        "That sounds rough... No wonder he never made any friends during his childhood - he simply didn't have the time."
        t "And, uh... all of that lasted until my second year of middle school."
        t "Since I had no idea how to approach people by then, I still couldn't talk to anyone despite having the time to."
        t "I guess I just didn't want to... After what happened with my mother."
        "Now that he's telling me all of that, I feel like I understand him a lot better."
        m angry "Is your mother the reason you wanted to move out of this town? You mentioned that last week."
        show pback 3 with dissolve
        t "That's right..."
        t "Once everyone knew what happened, I couldn't keep living here."
        t "I felt like... they were all judging me for what she did..."
        m serious "I understand. Is this why you didn't want to tell me about it?"
        "He pauses."
        t "Mostly. I just... didn't want your pity. I've gotten a lot of it already."
        stop music fadeout 5
        m talk "Is that all? I don't mean to sound blunt, but I still don't know how both of your alters were created."
        t "I..."
        hide pback with dissolve
        show t hurt with dissolve
        play music "ost/neutral.ogg" fadein 10
        "I look at him more closely. He doesn't seem too eager to tell me more about it."
        m conf "You don't have to tell me today. Take your time, think about it, and we can talk about it tomorrow."
        show t hurttalk with dissolve
        t "I... I guess that's unavoidable now."
        show t neutral with dissolve
        m neu "Whatever happened, you can trust me. I'm doing this for your sake."
        show t talk with dissolve
        t "I know... Thanks, I guess."
        show t frusttalk with dissolve
        t "Sorry about yelling at you earlier, it's just that... I thought it was your fault that I lost control."
        show t hurttalk with dissolve
        t "For asking me all these things on Wednesday... about my mother..."
        show t sadtalk with dissolve
        t "You made me remember all of that. That's why he appeared the next day."
        show t angry with dissolve
        menu:
            "I'm sorry":
                $personal +=1
                m serious "I'm sorry about having caused you so much stress last week."
                show t frusttalk with dissolve
                t "No, it's probably for the best."
                show t frust with dissolve
            "It was necessary":
                $professional += 1
                $PurpleHeart += 1
                m talk "I need to meet all three of you before I can help."
                show t hurttalk with dissolve
                t "I'm really... trying to accept that - I know it's for the best."
                show t hurt with dissolve
                show drk with Dissolve(0.75)
                show p 2 with dissolve
                show p 3 with Dissolve(0.55)
                $renpy.pause(0.5, hard = True)
                hide p with moveoutbottom
                hide drk with dissolve
        show t neutral with dissolve
        "Our session is about to end. He stands up."
        m talk "Remember about tomorrow. I'll ask you to tell me the details then."
        m fabtalk "Is that fine?"
        show t calm with dissolve
        "He nods and heads towards the door."
        show t talk with dissolve
        t "I think I should be back tomorrow."
        show t neutral with dissolve
        t "Goodbye, Hart."
        scene mc with dissolve
        play sound "doorclose.ogg" fadein 1
        "He leaves."
        "I'm looking forward to learning more about him tomorrow..."
        "I honestly expected his past to be somewhat traumatic so the story about his mother makes a lot of sense to me."
        stop music fadeout 5
        hide screen easymeter
        hide screen purplemeter
        "Tomorrow, I should finally learn what exactly caused his other two personalities to emerge."
        jump breakchoice
    elif day == 9:
        play music "ost/neutral.ogg" fadein 12
        scene mcdesk with dissolve
        "I'm preparing to meet Tom again today."
        if easymeter:
            show screen easymeter
            show screen purplemeter
        t "It's me again."
        show t neutral with dissolve
        "It seems he hasn't switched."
        m serious "Are you ready to talk about it today? I won't pressure you if-"
        show t angrytalk with dissolve
        t "Don't say that. I'll do it."
        show t neutral with dissolve
        m talk "If you're sure, then..."
        m serious "I only wanted you to know that you can still say no."
        show t pa with dissolve
        "He doesn't respond, waiting for me to start questioning him."
        m serious "What has your mother done?"
        show t calm with dissolve
        stop music fadeout 8
        "He takes a deep breath. I wish I could support him somehow, but he wouldn't let me."
        show t calmtalk with dissolve
        t "Well... I said yesterday that her anger towards my father turned to me."
        show t talk with dissolve
        t "I meant it."
        play music "ost/memory.ogg" fadein 10
        show pback 3 with dissolve
        t "She sometimes... had these fits - she got really mad for no apparent reason."
        t "At first she'd just yell at me... I could get used to that, and I did."
        t "There were times when she'd get slightly violent with me, but it was never anything serious."
        t "That is, until I was 6."
        "He pauses, as if wondering if it's a good idea to tell me all of that."
        m neu "Go on. Whatever it is, you can tell me."
        "He looks at me, surprised."
        t "I don't remember what it was about anymore... something to do with school, I think."
        t "She got really angry. I think she may have been drunk as well..."
        "That doesn't sound good..."
        show pback 7 with dissolve
        t "She started walking towards me, and I tried to get away until my back was against a wall and she was in front of me."
        t "She, uh..."
        t "She hit me."
        t "Except this time it was a lot harder than before."
        t "I thought she would stop after doing it once, like she would before that day, but she did it again."
        t "At first, I was too shocked to even move, but after a while it got more painful since she was only getting angrier and angrier..."
        t "I tried to run, but she grabbed my arm and pulled me back."
        t "I'm not sure how long it lasted then..."
        t "Eventually, she just stopped and left me without a word."
        show drk with dissolve
        show pback 3 with dissolve
        t "I wasn't really... in the state to run away at that point, but I managed to drag myself to my room and sleep."
        t "She didn't mention it at all the next few days... I thought she just forgot about it like she usually did."
        t "I was convinced it was just a one-time thing and she wouldn't do that again."
        t "But... the next week she got angry again. It would usually end with just yelling, but this time she actually hit me like the time before."
        t "Then she looked at me with these dead, dark eyes for a while before she did it again."
        t "She said it's punishment for disobeying her, since yelling at me wasn't doing any good."
        t "She didn't take as long as the first time, and she let me go once she was done."
        "I don't want to distract him with questions right now... I'll ask once he's done talking."
        t "The day after, she suddenly called me to her bedroom. It was 4 PM."
        t "She locked the door behind me."
        t "She told me... she thought I needed more discipline than what she'd already done, since I keep ignoring and disrespecting her."
        t "In a way, she was right - still, it was her fault for being a horrible mother."
        t "From that day forward, it became a habit for her to make me come to her room exactly at 4 PM."
        t "It usually took her an hour, sometimes two."
        t "I always went to sleep immediately after she was done."
        t "Generally I would pass out quickly because of the pain."
        "God, this is... I didn't expect it to be this horrible..."
        stop music fadeout 5
        hide drk with dissolve
        m sadtalk "I'm so sorry... If there's anything in particular you want to talk about, I can-"
        t "Stop it. Don't pity me like everyone else does."
        t "...please."
        "....."
        play music "ost/memory.ogg" fadein 10
        t "I hated my mother."
        show pback 7 with dissolve
        t "I'm not scared to admit it, because I really did."
        t "There was never anyone whose death I wished for more than hers."
        t "Sometimes... when I couldn't feel anything anymore, and only heard blood running through my ears..."
        t "I just wanted her to die. As long as it meant her leaving me alone."
        "He sounds like he really means it... I can't imagine hating someone to the point of wanting them dead... especially a family member."
        t "She wasn't even angry anymore when she did it... She just did. Like it was out of hatred."
        t "Just that. Genuine hatred."
        t "She hated me as much as I hated her, or more accurately - she hated my father."
        t "It was easier to blame a child who couldn't even defend themselves instead of taking responsibility."
        hide pback with dissolve
        stop music fadeout 6
        show t angry with dissolve
        "He pauses and looks at me."
        show t hurttalk with dissolve
        play music "ost/hospital.ogg" fadein 10
        t "I... I got really talkative just now. You should ask now if you have any questions."
        show t angry with dissolve
        m talk "It's not a problem from me. The more you talk, the better."
        m pity "Before I ask anything else - thank you so much for telling me this."
        m serious "I realize now how difficult it must've been for you."
        show t neutral with dissolve
        "He nods with a neutral expression. I don't think he cares much for my gratitude."
        menu:
            "How long did it last?":
                show t talk with dissolve
                t "Until I was 14... so eight years in total."
            "Has she ever severely hurt you?":
                show t talk with dissolve
                t "Only the first time... Then she was more calculative about it, so she only hurt me in ways that couldn't be noticed later at school and cause her trouble."
                show t frusttalk with dissolve
                t "But... it still hurt for a few days. And since she never missed a day, there wasn't a time when I wasn't covered in bruises."
                show t talk with dissolve
                t "It got worse in winter, since she had more freedom then."
                show t hurttalk with dissolve
                t "And summer break... I won't go into the details."
            "Was she saying anything while doing it?":
                show t talk with dissolve
                t "Usually yes... I think she just hated the silence."
                show t frusttalk with dissolve
                t "It was mostly nonsense, though. She rarely said anything coherent then."
        show t neutral with dissolve
        m talk "What about the alters? When did they start to... develop?"
        show t frust with dissolve
        t "The second one..."
        stop music fadeout 8
        show t hurttalk with dissolve
        t "When I turned 10, it got a lot worse... She... became really violent with me then."
        show t hurt with dissolve
        "As if she wasn't violent already..."
        show t talk with dissolve
        t "And while I got used to what she did before then, that was..."
        play music "ost/neutral.ogg" fadein 8
        show t hurt with dissolve
        t "She found my limit."
        show t sadtalk with dissolve
        t "For the first time in some years, I tried to run, but it was impossible."
        show t sad with dissolve
        t "I... I couldn't stop fighting back."
        show t hurttalk with dissolve
        t "She told me it wouldn't hurt as much if I stopped struggling and just gave up."
        show t talk with dissolve
        t "I didn't listen to her the first time..."
        show t frusttalk with dissolve
        t "But the thought couldn't leave my mind as she did it again and again, and it got worse with each time."
        show t hurttalk with dissolve
        t "I kept telling myself that I can't give up, but I tried it once, and... It just felt so much easier. Better."
        show t talk with dissolve
        t "Eventually, I stopped resisting at all. I gave up the moment she would call me to her room."
        show t frusttalk with dissolve
        t "I stopped remembering what she did to me after maybe a month or less."
        show t talk with dissolve
        t "I had a gap in memory between 4PM and the next morning, but I didn't care."
        show t angry with dissolve
        t "I just remember waking up with fresh bruises every day. They helped me count days."
        show t frusttalk with dissolve
        t "And memory loss really was the least of my problems at that time."
        show t hurttalk with dissolve
        t "I had no idea that by giving up myself, I was forcing someone else to experience all of that."
        show t hurt with dissolve
        stop music fadeout 10
        m neu "I see."
        show t neutral with dissolve
        m talk "We're running out of time for today. Thank you for telling me all of that."
        show t siden with dissolve
        t "...."
        "He looks at the window behind me with an unreadable expression."
        m grim talk "What's wrong?"
        show t talk with dissolve
        play music "ost/hospital.ogg" fadein 8
        t "I'm... I just don't think we will see each other tomorrow."
        show t neutral with dissolve
        "...oh. Yes, I suppose it makes sense."
        m talk "Then... at least the others will spare you the trouble of telling me the rest of your story."
        show t hurt with dissolve
        t "...."
        m smile "Once you're back, I should know everything I need."
        show t talk with dissolve
        t "...Right."
        show t hurt with dissolve
        m talk "Once again, thank you for today."
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        hide screen easymeter
        hide screen purplemeter
        "He leaves, and I watch him disappear behind the door."
        "Domestic abuse... I suspected it, but not on this scale."
        "I've never heard of anyone treating their child with such cruelty..."
        "I still don't know anything about his third personality, or why his mother stopped abusing him at some point."
        stop music fadeout 5
        "Whoever I end up seeing tomorrow will probably be capable of answering at least some of my questions."
        jump breakchoice
    elif day == 10:
        scene bg mc with dissolve
        play sound "knock2.ogg" 
        "A knock on the door. I can already tell who's on the other side."
        m smile "Come in ~"
        play music "ost/neutral.ogg" fadein 10
        "The first thing I see is Edward's panicked, pale blue eye."
        "He's likely still in shock."
        if easymeter:
            show screen easymeter
            show screen purplemeter
        scene bg mcdesk with dissolve
        m conf "I'm glad to see you again. Take a seat, please."
        show hg smile with dissolve
        pr "thank you for inviting me here"
        show hg neutral with dissolve
        "He sits down. I wanted to ask him about his past, but now that he's changed..."
        m talk "How do you feel today?"
        show hg sadtalk with dissolve
        pr "i'm fine... i-i already know what day it is."
        show hg talk with dissolve
        pr "i was... actually surprised... to be back this soon."
        show hg hostile with dissolve
        m serious "I suppose a lot's... happened yesterday."
        m neu "The first started telling me about your past."
        m sad "Your mother specifically."
        stop music fadeout 6
        show hg pale with dissolve
        "His eyes go wide."
        show hg shock with dissolve
        pr "our... mother?"
        show hg pant with dissolve
        pr "he... he told you about... her?"
        show hg pale with dissolve
        play music "ost/hospital.ogg" fadein 10
        m serious "He said she used to hit you. Since you were 6."
        show hg neutral with dissolve
        pr "...oh. i don't remember much of it."
        show hg talk with dissolve
        pr "the first things i remember clearly happened when he was 9, i think."
        show hg hostile with dissolve
        "That reminds me of what Tom said yesterday..."
        m fabtalk "According to him, his memory loss started to occur at 10. It was because of you, right?"
        show hg calm with dissolve
        "He nods slowly."
        show hg calmtalk with dissolve
        pr "the evenings... that was me"
        show hg neutral with dissolve
        m serious "He also said that it got worse around the time you started to appear. Do you have any idea what he meant by that?"
        show hg angry with dissolve
        pr "...that coward."
        show hg sadtalk with dissolve
        pr "he knew we'd switch, so he wouldn't have to tell you this..."
        show hg pain with dissolve
        pr "...why does it always need to be me?"
        show hg calm with dissolve
        "He takes a deep breath. I don't think he has a choice not to tell me anymore."
        "If he doesn't, we won't get anywhere."
        m sadtalk "I'm sorry, but there's no other way."
        show hg talk with dissolve
        pr "you're too kind to me, dr.hart."
        show hg sadtalk with dissolve
        pr "it would be easier if you just forced me to tell you... we wouldn't be wasting so much time because of me."
        show hg sad with dissolve
        m serious "...."
        show hg talk with dissolve
        pr "i'll tell you everything, i swear-"
        show hg sadtalk with dissolve
        pr "i just... don't know where to start..."
        show hg sad with dissolve
        stop music fadeout 6
        menu:
            "What has she done to you?":
                show hg pale with dissolve
                pr "she..."
                show hg pant with dissolve
                pr "...sh-she... she..."
                show hg pain with dissolve
                pr "she raped me"
                show hg hiden with Dissolve(1.0)
                "He covers his face with his hands. I'm speechless for a moment."
                pr "there."
                show hg sadtalk with Dissolve(1.0)
                pr "i said it"
            "Did it hurt more than what she did before?":
                "Maybe that's the cause..."
                show hg talk with dissolve
                pr "...sometimes."
                show hg calmtalk with dissolve
                pr "i didn't get as many bruises as before... but it was..."
                show hg sadtalk with dissolve
                pr "worse."
            "Why did you want to give up?":
                show hg pain with dissolve
                pr "s-she said it would hurt less..."
                show hg sadtalk with dissolve
                pr "she was right... most of the time"
        play music "ost/memory.ogg" fadein 10
        show hg talk with dissolve
        show pback 3 with dissolve
        pr "it started when i was around 8... sometimes she'd make us take our shirt off before she started."
        pr "it was easier to count the bruises later that way..."
        pr "the day of our 10th birthday, she didn't start hitting me right away like she had before."
        pr "he thought she wouldn't do anything at all that day, so he tried to leave"
        pr "the door was locked. i knew she wouldn't let us out that easily, but he wouldn't listen."
        show pback 6 with dissolve
        pr "she... she grabbed us. and dragged us back into the room."
        pr "we were on the floor. she started to tear our clothes off."
        pr "i told him not to run, but he ignored me. he always has."
        pr "...i think he was scared."
        pr "i had to watch him try to run. she caught us again."
        pr "she took us to her bed. he couldn't run, because she was on top of him"
        pr "he didn't stop struggling. of course, it was pointless, but i think it made him less afraid."
        m sadtalk "What... what did she do then?"
        pr "she... touched us."
        pr "she wasn't hitting us at least, but it was... worse"
        pr "she never managed to make him scream more loudly than when she did it for the first time."
        "He pauses."
        pr "of course, she didn't stop there."
        show pback 7 with dissolve
        pr "the next day she called us to her bedroom she did the same."
        pr "and the day after that..."
        pr "after a week it became clear to me that she wouldn't stop it."
        pr "i just wanted to help him..."
        pr "i kept telling him to give up, but he didn't."
        pr "until she hit him again for the first time in a month."
        show pback 8 with dissolve
        pr "he told me: \"Please, just make it stop\". if i hadn't helped him then, i don't think he would have survived any of that."
        pr "suddenly i was in control. i didn't really know what to do at first, but... it wasn't difficult."
        pr "i didn't have to do anything"
        pr "the following hour i didn't make a sound until she was done."
        pr "at first she kept her promise not to hurt me if i stop fighting back."
        pr "but..."
        pr "sometimes she would hit me harder than she hit him, just to see if i would scream."
        show pback 9 with dissolve
        pr "i never did"
        pr "it lasted for four years."
        pr "he would switch every day at 4PM, i would go to her room as i was supposed to, and once she was done i went to sleep."
        pr "after he let me take control once, i stopped remembering what he did during the days."
        pr "so for four years, all i saw and knew was... our mother."
        stop music fadeout 5
        "He pauses."
        hide pback with dissolve
        show hg sadtalk with dissolve
        pr "is something wrong?"
        play music "ost/neutral.ogg" fadein 8
        show hg sad with dissolve
        m serious "I'm fine... I just... didn't expect any of that."
        show hg sadtalk with dissolve
        pr "i'm sorry-"
        show hg pant with dissolve
        pr "i... said too much, didn't i?"
        show hg pain with dissolve
        pr "i... i tried to spare you the details. i apologize if that made you uncomfortable"
        show hg calm with dissolve
        pr "...."
        show hg talk with dissolve
        pr "i should be going now"
        show hg sad with dissolve
        pr "i don't think you'll see me again this week..."
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        hide screen easymeter
        hide screen purplemeter
        "He leaves, and I still can't move from my desk."
        "I thought it couldn't get any worse than what I heard of yesterday... I need to rest..."
        stop music fadeout 5
        "I spend the whole break in my office."
        jump patientchoice
    elif day == 11:
        scene bg mcdesk with dissolve
        "The door to my office flies open."
        play music "ost/james.ogg" fadein 10
        nn "Hello there ~"
        "This must be the third alter I haven't met yet."
        nn "I don't think we've met... I'm James."
        er "And you are..?"
        m talk "I'm [name] Hart, your psychologist."
        er "Of course! Such a pretty face could only belong to someone with a fittingly beautiful name ~"
        show jm smile with dissolve
        "He sits down in front of me. I wasn't expecting this..."
        if easymeter:
            show screen easymeter
            show screen purplemeter
        show jm sidetalk with dissolve
        er "Out of curiousity, how long was I gone for?"
        show jm neutral with dissolve
        "He seems to be incapable of staying in place for even a second."
        show jm siden with dissolve
        m fab "I can't tell, I met you two weeks ago and this is the first time I'm seeing... you."
        show jm regrettalk with dissolve
        er "My mistake! I must've forgotten about you..."
        show jm neutalk with dissolve
        er "So who have you seen so far?"
        show jm neutral with dissolve
        m talk "Both of them. I spoke to the first one five times, and three times to the second."
        show jm sidetalk with dissolve
        er "Oh, it seems that I have an unfair disadvantage, then..."
        show jm neutral with dissolve
        "He rests his hands on my desk and leans in a bit. I'm definitely not used to something like that from neither Tom nor Edward."
        show jm kawaii with dissolve
        er "We have some catching up to do, [name] ~"
        show jm smile with dissolve
        m angry "...Right."
        show jm neutalk with dissolve
        er "What do you think of the others? Pretty boring, eh?"
        show jm neutral with dissolve
        m fabtalk "No, I wouldn't say that..."
        show jm frust with dissolve
        "He's silent for a moment."
        show jm angry with dissolve
        m talk "They were telling me about your past... Could you tell me some more about that?"
        show jm smirk with dissolve
        er "I could tell you all sorts of things... But I don't think that's what you want to hear."
        "Let's get to the point."
        show jm neu with dissolve
        m angry "What's the first thing you remember? Your earliest memory?"
        show jm talk with dissolve
        er "Uhhh... their mother."
        show jm siden with dissolve
        er "I say \"their\" since I've never actually met her."
        show jm neutalk with dissolve
        er "I remember a little before I first took over..."
        show jm neutral with dissolve
        er "It was an afternoon. 4PM."
        show jm angrytalk with dissolve
        er "The second was there."
        show jm neutalk with dissolve
        er "I assume you know the whole story..."
        stop music fadeout 8
        show jm frust with dissolve
        er "She would call him to her bedroom every day at the same time, and, um..."
        show jm talk with dissolve
        er "Well."
        show jm regretsmile with dissolve
        er "I sure am glad that wasn't me..."
        play music "ost/memory.ogg" fadein 10
        show jm neu with dissolve
        er "Anyway, one day she didn't call him."
        show jm sidetalk with dissolve
        show drk 2 with dissolve
        er "So, being the sweet obedient child that he was, he went to her room on his own, thinking she must've just forgotten."
        show pback 10 with dissolve
        er "But when he entered the room he saw her corpse hanging from the ceiling."
        er "When he realized that she'd killed herself, he started crying."
        er "He really was sad about her dying. Don't ask me why."
        er "He fell to the floor and cried until he passed out."
        er "And that's why I came in."
        er "I woke up to see doctors and policemen all around me, with the corpse still there."
        show pback 11 with dissolve
        er "They asked me if I was hurt - of course I wasn't."
        er "For some reason, they already knew about what she did to them."
        er "Someone must have told them, I don't really know..."
        hide drk 2 with dissolve
        hide pback with dissolve
        show jm talk with dissolve
        er "I spent a week in a hospital, \"recovering\"."
        show jm frust with dissolve
        er "They were asking me a lot of things, but I mostly had no memory of what happened - I couldn't answer them even if I cared enough to do so."
        show jm neu with dissolve
        er "Which I didn't."
        show jm sidetalk with dissolve
        er "They thought the shock caused me to, uh... force myself to forget traumatic memories, some bullshit like that."
        stop music fadeout 5
        show jm siden with dissolve
        "He doesn't seem to care much about his past."
        m fabtalk "And you never told anyone the truth about your illness?"
        play music "ost/neutral.ogg" fadein 10
        show jm talk with dissolve
        er "I didn't know I was \"ill\". And even if I did, why would I tell anyone about it?"
        show jm angry with dissolve
        er "I wouldn't want to go back to being some whiny piece of shit who can't do anything on his own."
        m talk "That's a bit harsh, don't you think?"
        show jm siden with dissolve
        er "\"Harsh\"? No, they totally deserve it."
        show jm frust with dissolve
        er "But I guess I never had the experiences they had - maybe that's why they're so pathetic."
        show jm neutral with dissolve
        menu:
            "They're not pathetic":
                show jm gasp with dissolve
                er "Oh?" 
                show jm cute with dissolve
                er "Well, in my opinion they are, and you don't get to decide what I think."
                show jm smile with dissolve
                "He's going to be trouble."
            "And maybe you should shut up":
                show jm gasp with dissolve
                er "Ouch-?"
                show jm frustsmile with dissolve
                er "And maybe I won't."
                show jm cute with dissolve
                er "I don't like women telling me what to do."
                show jm smile with dissolve
                "I don't even have any time to reply to that."
            "They've been through a lot":
                show jm neutalk with dissolve
                er "Oh, I'm sure of that."
                show jm sidetalk with dissolve
                er "I kind of wish I'd seen it - I bet it got pretty intense."
                show jm neutral
                m angry "...."
        stop music fadeout 6
        show jm neutalk with dissolve
        er "So you're a psychologist here?"
        show jm neutral with dissolve
        m talk "That's right."
        show jm happy with dissolve
        er "How is it? Are you getting bored of it yet?"
        play music "ost/james.ogg" fadein 6
        show jm smile with dissolve
        m fabtalk "I don't think I ever will."
        show jm sidesmile with dissolve
        er "Don't tell me your other patients are more fun than me..."
        show jm smirk with dissolve
        menu:
            "I wouldn't say that":
                show jm laugh with dissolve
                er "Ha! I knew it."
                show jm regrettalk with dissolve
                er "All this time, you were just dying for my company..."
                show jm sidesmile with dissolve
                "I open my mouth to deny it."
                show jm cute with dissolve
                er "Oh, spare me the praise, [name] - I've heard it all before."
            "You're full of yourself":
                $PurpleHeart+=1
                show drk with Dissolve(0.75)
                show p 2 with dissolve
                show p 3 with Dissolve(0.55)
                $renpy.pause(0.5, hard = True)
                hide p with Dissolve(0.7)
                hide drk with dissolve
                show jm laugh with dissolve
                er "Ha! I have reasons to be, sweetheart~"
                show jm smile with dissolve
                menu:
                    "Don't call me that":
                        $personal+=1
                        $dominant+=2
                        show jm gasp with dissolve
                        er "Oh, you're a feisty one ~ I love it."
                        show jm sidesmile with dissolve
                        er "Why wouldn't I call you that?"
                        show jm cute with dissolve
                        er "I'll call you whatever I want, princess."
                        "I'm just encouraging him at this point."
                        show jm smile with dissolve
                    "What reasons?":
                        $professional+=1
                        $submissive+=1
                        show jm neutalk with dissolve
                        er "I don't think I need to justify myself to you."
                        show jm cute with dissolve
                        er "Besides, you'll find out soon enough... Don't be impatient."
            "I won't answer that":
                $professional+=1
                show jm neu with dissolve
                "He's silent."
                show jm frust with dissolve
                "I glare at him triumphally - he didn't expect that."
                "He probably just wanted to provoke me."
        stop music fadeout 5
        "We got off-topic... I was asking him about his past."
        show jm neu with dissolve
        m fabtalk "So you have no memory of what your mother's done?"
        play music "ost/neutral.ogg" fadein 10
        show jm talk with dissolve
        er "I don't. I only know it happened, I haven't seen any of it myself."
        show jm frust with dissolve
        "I suppose that's good for him, at least."
        show jm neu with dissolve
        er "Like I said, the first thing I remember is the day she killed herself."
        m serious "Do you know why she committed suicide?"
        show jm sidetalk with dissolve
        er "Do I look like I care? I didn't even know her."
        show jm frust with dissolve
        "That's... surprisingly harsh."
        show jm neutral with dissolve
        m talk "You mentioned someone finding out about the... abuse. Is this why she killed herself? So she wouldn't get caught?"
        show jm neutalk with dissolve
        er "I guess."
        show jm sidetalk with dissolve
        er "You should ask the others about it, they're more invested in what happened than I am."
        show jm angrytalk with dissolve
        er "What's the point of dwelling on the past, anyway?"
        show jm gasp with dissolve
        er "It's better to just forget about it and move on, don't you think?"
        show jm smile with dissolve
        m frust "...."
        show jm siden with dissolve
        "Like I'm one to talk about the past..."
        "I decide to change the topic."
        show jm angry with dissolve
        m fabtalk "What happened to you after that?"
        show jm frust with dissolve
        er "I can't tell you everything, since I was only myself for two weeks after her death."
        show jm neutalk with dissolve
        er "Once everything settled down, I wasn't needed anymore, I guess."
        show jm sidesmile with dissolve
        er "Well, they got adopted quite quickly after that - people must've really pitied me back then."
        show jm talk with dissolve
        er "Since the first time I took over, I've been getting one or two days every two months or so... Sometimes I'd miss half a year."
        show jm frust with dissolve
        "I recall Edward's words from last week..."
        m talk "Edward told me..."
        show jm gasp with dissolve
        er "Which one was it again? I don't bother to keep up with the names."
        show jm neu with dissolve
        "I correct myself quickly."
        m fabtalk "The second told me you usually appear when something needs to be done that the others wouldn't be able to handle. Is that true?"
        show jm sidetalk with dissolve
        er "I would be willing to agree."
        er "I told you they're pathetic compared to me - they get scared of the simplest things, especially that second one."
        show jm smirk with dissolve
        er "Every time that happens, I'm needed immediately. It's hilarious."
        stop music fadeout 5
        show jm cute with dissolve
        "I decide to keep my comments to myself."
        show jm smile with dissolve
        m talk "I think we're running out of time for today."
        play music "ost/james.ogg" fadein 6
        show jm regrettalk with dissolve
        er "Oh, what a pity! If only I could see your face once again..."
        show jm regret with dissolve
        m neutral "You'll be here tomorrow, right?"
        show jm neu with dissolve
        er "I should be."
        show jm laugh with dissolve
        er "If you want to scare me away, you'll have to try harder than that, sweetheart."
        show jm cute with dissolve
        "That's enough for today."
        show jm smirk with dissolve
        m fabtalk "Goodbye, James."
        show jm frust with dissolve
        er "I'll see you tomorrow..?"
        show jm happy with dissolve
        er "...[name]. It's been a pleasure."
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        "He leaves with a smile."
        stop music fadeout 8
        "I've met all three of Tom's identities now... I'll need to get to know them better before I can really help him."
        "If I want them to integrate... it won't be easy, but I should find something they have in common and try to focus on it."
        play music "ost/neutral.ogg" fadein 8
        hide screen easymeter
        hide screen purplemeter
        "Confronting their past is probably important as well."
        "These should be my priorities for now..."
        "...James is going to be trouble. A lot of trouble."
        "I have seriously mixed feelings about him, I'm not sure how to help him..."
        "He seemed so carefree, as if he liked being this way - maybe he does."
        "Maybe it benefits him to be just a once in a month occurance, free of attachments, of responsibility..."
        stop music fadeout 10
        "...and maybe I'm just assuming too much. I'll have to ask him a lot of things tomorrow, if he's still there."
        jump breakchoice
    elif day == 12:
        scene black with dissolve
        "What... was that dream?"
        scene bg mcdesk with dissolve
        show jm smirk with dissolve
        "James enters my office just like yesterday."
        play music "ost/james.ogg" fadein 10
        show jm kawaii with dissolve
        er "Hello, sweetheart ~"
        show jm neu with dissolve
        "I glare at him."
        show jm sidetalk with dissolve
        er "Princess?"
        show jm gasp with dissolve
        er "...darling?"
        show jm angrytalk with dissolve
        er "You must have a soft spot for one of these... everyone does."
        show jm neutral with dissolve
        m talk "\"[name]\" is fine."
        show jm frust with dissolve
        er "...."
        show jm talk with dissolve
        er "Alright, I give up... for now."
        show jm smile with dissolve
        if easymeter:
            show screen easymeter
            show screen purplemeter
        "He takes a seat in front of me."
        "I won't be affected by his shameless flirting."
        show jm sidetalk with dissolve
        er "Ah, it's good to be back..."
        show jm regrettalk with dissolve
        er "I'll probably be gone in a few days, though..."
        show jm cute with dissolve
        er "Such a pity - I'm having the most fun I've had in a while, with you here."
        show jm frust with dissolve
        er "That previous psychologist was a pain - some boring old man..."
        show jm neutral with dissolve
        "He suddenly gets closer to me."
        show jm winkblush with dissolve
        er "Not nearly as interesting as you, [name]."
        show jm smile with dissolve
        m gasp "What do you mean by that?"
        "I'm not used to him being like this... I can see the light from the window behind me reflecting in both of his eyes."
        show jm regrettalk with dissolve
        er "Oh, don't act like you don't know..."
        show jm talk with dissolve
        er "You're smart, confident, and most of all - you seem to enjoy what you're doing."
        show jm sidetalk with dissolve
        er "And that's rare here, from what I know."
        show jm neutral with dissolve
        m fabtalk "You've only been here for a few days, from your point of view..."
        show jm happy with dissolve
        er "And even if you didn't have all these wonderful qualities - you're at least more pleasant to look at than the others."
        stop music fadeout 6
        show jm cute with dissolve
        "...."
        "That's... a very subjective matter which doesn't add much to our conversation."
        play music "ost/neutral.ogg" fadein 10
        show jm gasp with dissolve
        er "You're younger than me, aren't you?"
        show jm neu with dissolve
        "What does that have to do with anything?"
        m talk "Only a year."
        show jm regrettalk with dissolve
        er "Really? I could swear you look 25 to me."
        show jm kawaii with dissolve
        er "That must be thanks to your lovely face."
        show jm talk with dissolve
        er "Though, other than that..."
        show jm siden with dissolve
        "His gaze leaves my eyes."
        show jm neutalk with dissolve
        er "I can see that 28 there."
        show jm neutral with dissolve
        menu:
            "Are you done?":
                show jm cute with dissolve
                er "...of course I am, [name]~"
            "Excuse me?":
                show jm wink with dissolve
                er "Oh, don't mind me, [name]. I was only admiring the feminine aspects of your form."
            "Stop staring at me.":
                $professional+=1
                $dominant+=1
                show jm gasp with dissolve
                er "Why so harsh, [name]? It's not like I'm doing you any harm ~"
        stop music fadeout 8
        show jm smile with dissolve
        "He looks at me again with a playful smile. It feels genuine this time."
        "There's a mischievous spark in his right eye."
        play music "ost/james.ogg" fadein 10
        show jm winkblush with dissolve
        er "You know, I've had many women so far, but none of them have been as stunning as you ~"
        m fab "Do you say that to every woman you meet?"
        show jm gasp with dissolve
        er "No-"
        show jm frust with dissolve
        er "Even if I did, what's wrong with that? It never seemed to bother anyone before."
        show jm smirk with dissolve
        er "It surely didn't stop anyone from falling for it."
        show jm neutalk with dissolve
        er "So believe what you want, sweetheart, but I wouldn't bother with you if I didn't mean any of what I said."
        show jm sidetalk with dissolve
        er "I have standards, after all."
        show jm regrettalk with dissolve
        er "Though I've been kind of lonely recently, I admit..."
        show jm neutalk with dissolve
        er "Last time I was myself, we were already here."
        show jm regret with dissolve
        er "I'm kind of glad that I'm here so rarely, though - nothing interesting ever happens here."
        show jm sidetalk with dissolve
        er "Same places, same boring people..."
        show jm frust with dissolve
        er "Most of the nurses are no fun - and the one whom I'd call remotely my type is always busy with something and running around."
        show jm talk with dissolve
        er "The patients are out of question, since they're always being watched by the staff."
        show jm neutral with dissolve
        "He looks at me with an unreadable expression."
        show jm neutalk with dissolve
        er "So that just leaves you."
        show jm neu with dissolve
        m shock "...me?"
        show jm wink with dissolve
        er "Ha, relax... I'm just having fun while I can."
        m fabtalk "I don't think I share your idea of \"fun\"."
        show jm neutral with dissolve
        m talk "What were you doing the whole time you were fronting, anyway? I don't see you helping the first by pretending to be him like the second did..."
        show jm frustsmile with dissolve
        er "No, not a chance..."
        stop music fadeout 8
        show jm sidetalk with dissolve
        er "The others wouldn't tell you that, but I don't only appear when there's an emergency."
        show jm neutalk with dissolve
        er "Do you think either of them ever had sex even once these past 15 years?"
        show jm neutral with dissolve
        "I... why would I ask myself that?"
        play music "ost/hospital.ogg" fadein 6
        show jm neu with dissolve
        m angrytalk "They've been abused by their own mother for four years - I don't think they would -"
        show jm wink with dissolve
        er "Are you sure about that?"
        show jm neutral with dissolve
        "I'm not sure if I can trust him... he seems to have some ulterior motives."
        stop music fadeout 6
        show jm laugh with dissolve
        er "Luckily, they have me ~ And I don't share their warped views."
        show jm wink with dissolve
        er "In fact - those past 10 years there was barely a night when I slept alone. Well, until we were locked up here."
        show jm frust with dissolve
        er "And the first complains about me... If it wasn't for me, he-"
        play music "ost/tension.wav" fadein 5
        show jm neu with dissolve
        m trigger "Stop. Just stop."
        show jm gasp with dissolve
        er "Huh?"
        m sjw "You weren't there when it happened. You have no idea what it was like."
        show jm angry with dissolve
        er "Do you?"
        m angrytalk "No, but I'm not mocking them while being extremely immature about what happened."
        show jm regret with dissolve
        er "...."
        show jm talk with dissolve
        er "{i}That{/i} is not what I expected from you."
        show jm wink with dissolve
        stop music fadeout 6
        er "Well, time for me to go ~"
        "He gets up and I realize that it's about time to finish for today. Thankfully."
        show jm neutral with dissolve
        "I've learned a lot of things from him today I didn't ask about, but I guess that's just the way it is with him."
        "He does what he wants. And talks a lot."
        hide screen easymeter
        hide screen purplemeter
        show jm siden with dissolve
        show drk with dissolve
        "He's oddly silent when I lead him to the door."
        show jm regrettalk with dissolve
        er "I won't see you the next time we meet... Oh, what a tragic turn of events ~!"
        scene bg mc with dissolve
        "I open my mouth to reply, but freeze before I can even say anything."
        show james
        nt "He kisses my forehead softly."
        nt "...!"
        nt "I'm too shocked to push him away."
        play music "ost/james.ogg" fadein 8
        er "See you in a few weeks, [name] ~"
        nt "He pulls away with a mischievous smile and leaves before I can say anything."
        play sound "doorclose.ogg" fadein 1
        hide james with dissolve
        "What just... happened?"
        "How did I let him do that?"
        "He was gone before I could even realize what was happening... that sly bastard."
        "I'll need to be careful around him next time - not like I'll see him again that soon, but..."
        "It won't be that easy to catch me off-guard next time."
        "I'm his psychologist, not some random girl he can just flirt with."
        "But I know he doesn't care at all - maybe he even likes how wrong this feels to me."
        "Ughh... I want the other two back."
        jump breakchoice
    elif day == 13 or day == 14:
        jump nextday
##########################         
    elif day == 15:
        "Another week at the hospital is starting, and I intend to see Tom again."
        "James told me he wouldn't be here this time, which leaves only two options..."
        scene bg mcdesk with dissolve
        play music "ost/hospital.ogg" fadein 10
        show t neutral with dissolve
        "The door opens to reveal Tom himself."
        m talk "Welcome back. Please, take a seat."
        if easymeter:
            show screen easymeter
            show screen purplemeter
        show t frusttalk with dissolve
        t "Which one was it this time?"
        show t angry with dissolve
        m fab "Both of them."
        show t hurttalk with dissolve
        t "And... did they tell you everything?"
        show t frust with dissolve
        "I nod."
        m frust "You don't have to add anything about your childhood if you don't want to - I already know everything I needed."
        show t sidetalk with dissolve
        t "Thank you, Hart... This was your first time talking to the third one, yes?"
        show t neutral with dissolve
        m fabtalk "That's right."
        show t frusttalk with dissolve
        t "How... was it?"
        show t neutral with dissolve
        m gasp "...interesting..?"
        show t talk with dissolve
        t "That sounds like you had trouble with him."
        show t frusttalk with dissolve
        t "He doesn't appear often, but when he does... he just ruins everything."
        show t neutral with dissolve
        m serious "They both exist for a reason."
        show t sidetalk with dissolve
        t "...I suppose. But that reason stopped existing 15 years ago."
        show t frust with dissolve
        m talk "Did James cause you trouble?"
        stop music fadeout 5
        show t sidetalk with dissolve
        t "Yeah... that's how I was admitted here."
        show t neutral with dissolve
        m serious "What happened?"
        show t talk with dissolve
        t "The trouble with him actually started a lot earlier."
        play music "ost/neutral.ogg" fadein 10
        show t frusttalk with dissolve
        t "I remember getting texts from random girls I've never met, asking me to go out with them."
        show t sad with dissolve
        t "It started maybe 8 years ago... At that time I was aware of having two of these... alters, and was trying to make some sense of them."
        show t angrytalk with dissolve
        t "I started linking events I would miss to each one of them, which gave me a very vague idea of what they're like."
        show t talk with dissolve
        t "I noticed that most of the time I would switch for about two, three days and absolutely nothing noteworthy would happen."
        show t talk with dissolve
        t "It was as if I just slept for these days."
        show t sidetalk with dissolve
        t "And sometimes I would lose one day, but it would be... troublesome."
        show t angry with dissolve
        t "So I came to the conclusion that there must be two of them."
        show t sidetalk with dissolve
        t "But I was only told of how they split here."
        show t neu with dissolve
        m fab "I see."
        show t talk with dissolve
        t "I had enough knowledge of them to link the girls to the third one then."
        show t frusttalk with dissolve
        t "It would be very unlike the second to meet with anyone."
        show t frust with dissolve
        m talk "What do you think he did when he fronted?"
        show t neutalk with dissolve
        t "I never found any signs of his activity... so my guess is that he stayed at home for whole days."
        show t neutral with dissolve
        m fabtalk "What about the third? How did he cause you to be admitted here?"
        show t frusttalk with dissolve
        t "I know of his... activities, based on the consequences I saw myself."
        t "Sometimes I would even wake up next to some girl I didn't recognize."
        show t hurttalk with dissolve
        t "I'm sure it happened to the second a few times as well..."
        show t frust with dissolve
        "Poor Edward... that must've been borderline traumatic for him."
        show t sadtalk with dissolve
        t "It was... very troublesome, but I'm at least thankful he never brought any of them to my house."
        stop music fadeout 5
        show t frusttalk with dissolve
        t "This went on for a while until one girl, uh... accused me of harassment."
        show t neutral with dissolve
        "...oh."
        show t sidetalk with dissolve
        t "She didn't know my name, but they found me the next day anyway - the consequence of having a very characteristic eye color, I assume."
        play music "ost/memory.ogg" fadein 10
        show t angrytalk with dissolve
        t "At first, I had no idea what happened - I knew it must have been the third."
        show t sadtalk with dissolve
        t "The police started to question me, and uh... they realized that the holes in my memory weren't random at all."
        show t angry with dissolve
        t "They also dug up my past, and that along with a confirmation from a psychologist, was enough to conclude I was definitely ill."
        show t sidetalk with dissolve
        t "And that's how I got here."
        show t talk with dissolve
        t "Of course, I lost my job immediately once they learned of my condition."
        show t frust with dissolve
        t "Later on, that girl who accused me confessed to being drunk and not remembering much."
        show t talk with dissolve
        t "So at least by law, I didn't hurt her, since her version was vague at best."
        show t neutral with dissolve
        "Still, she felt harassed... it must've been hard for her, especially since she couldn't be sure what happened."
        show t sadtalk with dissolve
        t "Honestly, I don't think even he could've done something like this."
        show t angrytalk with dissolve
        t "He's done a lot of stupid things, but that's just... wrong."
        show t sadtalk with dissolve
        t "I didn't get to talk to her after that, I barely saw her at all, but..."
        show t hurt with dissolve
        t "For the first time, I felt like I wanted to tell someone about what happened to me."
        show t talk with dissolve
        t "...I don't know, I just wanted to see her reaction."
        show t angrytalk with dissolve
        t "From what she'd said, she really had no idea what she was accusing me of."
        show t patalk with dissolve
        t "I just wanted to tell her that... she has no idea how that feels."
        show t pa with dissolve
        "...Right. There's hardly anything that could compare to what he's gone through."
        show t sidetalk with dissolve
        t "...but I guess it's pointless anyway. Telling her that would achieve nothing."
        show t sadtalk with dissolve
        t "And I would probably just seem like more of a psychopath to her."
        show t frust with dissolve
        m serious "How do you feel now that I know about it?"
        show t neutalk with dissolve
        t "You're not the first... a lot of people knew about my past before you, and the staff here knows about my illness."
        show t frusttalk with dissolve
        t "I don't feel any way in particular about it, it's something that had to be done eventually."
        show t calmtalk with dissolve
        t "Though... I have to admit I'd rather not talk about it if I had the choice."
        show t frust with dissolve
        m sadsmile "I understand. We all have some things we'd rather not share from our past."
        show t neutral with dissolve
        "He looks at me with a hint of curiousity."
        show t gasp with dissolve
        t "Even you, Hart?"
        show t angry with dissolve
        stop music fadeout 6
        m neu "Even me."
        show t neutral with dissolve
        "I feel a bit of sympathy in the way he looks at me."
        show t sidesmile with dissolve
        play sound "page.ogg"
        "I flip through my notes quickly, looking for something to talk about now that he's fallen silent."
        show t neutral with dissolve
        m talk "You know, last time I saw the second, he called you a coward for not telling me what your mother did."
        play music "ost/hospital.ogg" fadein 10
        show t sadtalk with dissolve
        t "He did..?"
        show t hurt with dissolve
        t "...."
        m regrettalk "He said he's always the one who has to do everything that you can't."
        m talk "How do you feel about that?"
        "He sighs."
        show t sadtalk with dissolve
        t "I... I guess I've always had the urge to dump everything onto him."
        show t patalk with dissolve
        t "Back then, with my mother, I..."
        show t hurt with dissolve
        t "I left it all to him."
        show t hurttalk with dissolve
        t "From what I know, what she did to me was just the start - it got a lot worse over time."
        show t frusttalk with dissolve
        t "And I made him go through that for four years, while I didn't remember anything that happened."
        show t pa with dissolve
        m sadtalk "It wasn't your choice - you didn't know what would happen if you gave up."
        show t frusttalk with dissolve
        t "You're right, I didn't - so from my perspective, when I made the choice to give up, it was the best thing to do."
        show t hurttalk with dissolve
        t "It was the only thing I could do."
        show t sad with dissolve
        m angrytalk "Remember that he was created specifically to absorb all those memories. You weren't."
        m serious "He was a necessity at that time. I don't think there was much you could've done."
        show t sadtalk with dissolve
        t "And yet..."
        show t patalk with dissolve
        t "I should've treated him better all those years... I should've been more grateful for what he's done for me."
        show t sadtalk with dissolve
        t "I just wish I could tell him that I'm sorry for what I put him through."
        show t sad with dissolve
        "This is going in the right direction, I feel."
        show t neutral with dissolve
        m neutral "I can tell him that the next time we meet."
        show t gasp with dissolve
        t "You will?"
        show t neu with dissolve
        "I nod."
        m conf "I promise."
        stop music fadeout 6
        show t smile with dissolve
        t "Thank you, Hart... I can tell you're trying your best."
        show t siden with dissolve
        m flirt "That's why I'm here. I think it would really help all three of you to have a better relationship with one another."
        play music "ost/neutral.ogg" fadein 10
        show t neutalk with dissolve
        t "Can I ask you for one more thing?"
        show t neutral with dissolve
        m smile "Of course."
        show t angrytalk with dissolve
        t "Go easy on him. He really doesn't deserve to go through any more shit than what I've already put him through."
        show t angry with dissolve
        m boretalk "I've been doing everything I can to treat him well."
        show t sidetalk with dissolve
        t "Really?"
        show t talk with dissolve
        t "Did he ever say something about that?"
        show t angry with dissolve
        "I think back to the second time I saw Edward, on Friday..."
        m talk "He said I'm good at what I'm doing last week. And that he's glad I want to keep seeing him."
        show t frust with dissolve
        m frusttalk "Our last session was a bit difficult, though..."
        m sadtalk "I had no idea that what happened to you was... this horrible."
        m serious "And having to tell me the details of what happened wasn't easy for Edward..."
        show t sad with dissolve
        m regret "He didn't take it too well."
        m sadtalk "That's probably why I saw James the next day."
        show t hurt with dissolve
        t "...."
        show t angrytalk with dissolve
        t "Try your best not to fuck it up next time - he won't let you know when you do something wrong, so be careful, alright?"
        show t frust with dissolve
        m neutral "I will."
        show t frusttalk with dissolve
        t "Uhhh... isn't it time for me to leave? We've been here for a while today."
        show t neutral with dissolve
        m gasp "Oh, right."
        "I check the time and realize it's almost time for him to go."
        "He stops before he can open the door."
        show t sidetalk with dissolve
        t "I feel... strange today... I think you might see someone else tomorrow."
        show t frust with dissolve
        m conf "I'll see you whenever you're back. Goodbye, Tom."
        show t neutalk with dissolve
        t "Goodbye, Hart."
        hide screen easymeter
        hide screen purplemeter
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        "He leaves."
        "That was... unexpected. I got to see a more sensitive side of Tom, as well as learned more about his past and his relationship with the other two..."
        "I also finally know exactly how he got here."
        "I wonder if I'll see Edward tomorrow... Tom's honesty today may have been his influence."
        stop music fadeout 5
        "I hope I can make him feel comfortable with me again."
        jump breakchoice
    elif day == 16:
        play music "ost/tran.ogg" fadein 6
        scene bg front with dissolve
        "I'm making my way to the hospital."
        "I wonder who I'm about to see... something tells me it's going to be Edward."
        scene bg patients with dissolve
        "I make my way through most of the hallway before stopping near room number XVI."
        "I glance through the door to see Tom. I'm not sure which one of them it is yet."
        "He looks back at me and gives me a faint smile."
        pr "hello."
        "It is Edward, just like I thought."
        pr "do you... need anything?"
        m flirt "No, I was just curious if it was you this time."
        pr "it's me. how... long was i gone for?"
        m talk "It's Tuesday."
        pr "...oh."
        stop music fadeout 6
        pr "thank you"
        pr "give me a few minutes, i- i'll join you soon."
        m conf "Of course."
        "I decide to leave him be and wait for him in my office."
        show bg central with dissolve
        show bg offices with dissolve
        show bg mc with dissolve
        $renpy.pause()
        play sound "knock2.ogg"
        "I hear a quiet knock on the door."
        play music "ost/hospital.ogg" fadein 10
        m smile "Come in, Edward."
        show bg mcdesk with dissolve
        show hg neutral with dissolve
        "He enters my office."
        if easymeter:
            show screen easymeter
            show screen purplemeter
        show hg sadtalk with dissolve
        pr "h-hello, dr.hart..."
        show hg sad with dissolve
        "He takes a seat."
        show hg grief with dissolve
        pr "i... i wanted to apologize... for last time."
        show hg calm with dissolve
        m pity "There's nothing to apologize for. In fact, I should be thanking you."
        show hg shock with dissolve
        pr "...for what?"
        show hg neu with dissolve
        m angry "For telling me everything. You helped me a lot last week."
        show hg calmtalk with dissolve
        pr "...oh."
        show hg calm with dissolve
        "I decide to get to the point - there's a lot I wanted to discuss."
        show hg neu with dissolve
        m fabtalk "I spoke to the first one yesterday. He wanted me to tell you something."
        show hg sadtalk with dissolve
        pr "...me? why would he want to..?"
        show hg sad with dissolve
        m sad "He said he's sorry for putting you through all of that. He didn't know you would have to handle it on your own."
        show hg calm with dissolve
        "He takes a deep breath."
        stop music fadeout 5
        show hg calmtalk with dissolve
        pr "how benevolent of him..."
        show hg pain with dissolve
        pr "...to finally acknowledge me."
        show hg neu with dissolve
        pr "he still treated me like air for the past twenty years, so i don't think an apology is enough."
        play music "ost/neutral.ogg" fadein 10
        show hg talk with dissolve
        pr "but i suppose it's an act of good will from him... i won't be the troublesome one"
        show hg calmtalk with dissolve
        pr "you can tell him i accept his apology - there's no point telling him how i feel about him now."
        show hg neu with dissolve
        m uncom  "He seemed to feel really guilty about it."
        show hg calmtalk with dissolve
        pr "i'm sure he does - if he had felt guilty fifteen years ago, it would have been a bit better, though."
        show hg talk with dissolve
        pr "nevermind that - i'm glad he at least feels remorse now."
        show hg calm with dissolve
        pr "if he wants to cooperate, then i will as well."
        show hg angry with dissolve
        pr "though... the third has yet to make any attempt at contacting us."
        m talk "From what I've seen of him, you may be right."
        show hg gasp with dissolve
        pr "...you met him?"
        "I nod."
        show hg talk with dissolve
        pr "forgive my curiousity... how was it?"
        show hg neu with dissolve
        menu:
            "Interesting":
                show hg calmtalk with dissolve
                pr "oh. if that's so, then... i'm glad."
            "Fun":
                show hg grief with dissolve
                pr "umm... i suppose that's good."
            "Difficult":
                $PurpleHeart+=1
                show hg talk with dissolve
                pr "...oh."
                show hg grief with dissolve
                pr "i'm sorry to hear that"
                show hg sadtalk with dissolve
                pr "i won't cause you any more trouble, i promise."
                show drk with Dissolve(0.75)
                show p 2 with dissolve
                show p 3 with Dissolve(0.55)
                $renpy.pause(0.5, hard = True)
                hide p with Dissolve(0.7)
                hide drk with dissolve
        show hg hostile with dissolve
        m talk "I didn't get a clear answer from him about one thing, though..."
        m talk "What exactly happened before he first appeared?"
        show hg grief with dissolve
        pr "oh..."
        show hg sadtalk with dissolve
        pr "are you... asking our mother's s-suicide?"
        show hg sad with dissolve
        m talk "If I can."
        show hg pain with dissolve
        pr "n-no, i'll tell you..."
        "I hope he won't feel bad about telling me this..."
        stop music fadeout 5
        show hg hostile with dissolve
        m talk "Take your time. It's okay."
        show hg neu with dissolve
        "He nods slowly."
        play music "ost/memory.ogg" fadein 10
        show hg sadtalk with dissolve
        pr "when... i got to her room, and i saw her h-hanging, i was..."
        show hg grief with dissolve
        pr "i was devastated. i didn't know what to do."
        show hg pain with dissolve
        pr "i started crying, i couldn't stand to watch her corpse."
        show hg talk with dissolve
        pr "i... i knew i'd have to do something eventually, that i would have to find a new home and learn to be with other people."
        show hg sadtalk with dissolve
        pr "...and that terrified me."
        show hg grief with dissolve
        pr "i even wondered if i'd be needed at all in the first place, or if i would just... d-die with our mother..."
        "I understand how he feels... But I need to focus on him right now, not me."
        show hg calmtalk with dissolve
        pr "i knew what we needed then - courage."
        show hg pain with dissolve
        pr "i didn't have it, and i don't think the first one was ready to deal with any of that either."
        show hg angry with dissolve
        pr "we... needed someone who wasn't scarred by what our mother did, someone strong enough to take everything that was ahead."
        show hg talk with dissolve
        pr "someone who can adjust to any situation and just... distance themselves from all the pain both of us had endured"
        show hg grief with dissolve
        pr "i... don't think it went exactly as i would've wanted it to"
        show hg talk with dissolve
        pr "but i'm used to that, so i'm at least grateful the third managed to get us through everything."
        show hg calm with dissolve
        m talk "I suppose that's what mattered then."
        show hg grief with dissolve
        pr "the truth is, if it wasn't for the third we'd never move on. he had no memory of what happened to us, so he had nothing to move on from."
        show hg talk with dissolve
        pr "he was new to everything, wanted to experience everything he could - it was something we wouldn't be capable of."
        show hg sad with dissolve
        pr "i think if we hadn't split then, we would have just... died instead."
        "That's how it feels to lose someone close... even if she hurt them so much."
        show hg hostile with dissolve
        m talk "How long after the suicide did you first front again?"
        show hg talk with dissolve
        pr "i think it was... about a month after that."
        show hg calmtalk with dissolve
        pr "when we were adopted."
        show hg smile with dissolve
        pr"...i think the third realized he wouldn't be able to get along with our new parents."
        show hg calmtalk with dissolve
        pr "so i was needed again."
        show hg neu with dissolve
        m talk "How did you feel when you appeared without your mother for the first time?"
        show hg talk with dissolve
        pr "i was... really anxious at first, because i didn't know what to expect."
        show hg sadtalk with dissolve
        pr "but our new parents were good people - they were really nice to us."
        show hg smile with dissolve
        pr "so... i was honestly happy that i got the chance to live a normal life."
        show hg calmtalk with dissolve
        pr "to see people... talk to them..."
        show hg pain with dissolve
        pr "i didn't really know how, but it made me feel less... trapped."
        show hg grief with dissolve
        pr "back when i first split, i was only there when our mother called us. i never got to see anything else."
        show hg calmtalk with dissolve
        pt "...it made me happy to be able to do what i wanted to."
        show hg sadtalk with dissolve
        pr "i didn't do that much, though... i didn't want to cause the others trouble by exposing our illness."
        show hg neutral with dissolve
        stop music fadeout 6
        m talk "I see."
        "I think for a moment..."
        m talk "In the context of these past twenty years, how do you feel about your mother now?"
        show hg calm with dissolve
        "Out of the three of them, he's the one who's been hurt the most by her."
        play music "ost/hospital.ogg" fadein 10
        show hg calmtalk with dissolve
        pr "um..."
        show hg pain with dissolve
        pr "...it's complicated, but i'll try"
        show hg sadtalk with dissolve
        pr "i never hated her for what she's done to us."
        show hg grief with dissolve
        pr "...to me."
        show hg talk with dissolve
        pr "i'm not sure if any of the others told you about it, but she's had a difficult life before i was born."
        show hg grief with dissolve
        pr "our father left her, i don't think they were even in a relationship before that."
        show hg sadtalk with dissolve
        pr "her family was poor, and even if they could've helped, they never had."
        pr "they were disgusted with her after she became pregnant at her age."
        show hg grief with dissolve
        pr "they left her as well. everybody did."
        pr "we never met any of our family."
        show hg sadtalk with dissolve
        pr "even after her suicide, nobody wanted to help."
        show hg pain with dissolve
        pr "and it was all over the news for some time, they had no way of missing it. they recognized her for sure..."
        "I honestly don't remember ever hearing about it. I was thirteen when it happened, though, so it's understandable."
        show hg grief with dissolve
        pr "she was all alone - everyone left her because of us."
        show hg sadtalk with dissolve
        pr "of course we were a burden for her - she was seventeen, she had a whole life ahead of herself."
        show hg grief with dissolve
        pr "and we took that from her."
        m talk "It's not your fault it was like this."
        show hg talk with dissolve
        pr "maybe it wasn't, but from her point of view it was."
        show hg sadtalk with dissolve
        pr "that's why i don't blame her for everything she's done. she had her reasons, and you have to understand that."
        show hg angry with dissolve
        pr "she wasn't evil. she didn't hurt me because it made her happy."
        show hg grief with dissolve
        pr "she hurt me because it eased her own pain."
        show hg pain with dissolve
        pr "she wasn't responsible. nobody was."
        stop music fadeout 6
        show hg sad with dissolve
        "I take a deep breath. Where do I begin..?"
        m talk "You can't deny that she's hurt you."
        play music "ost/neutral.ogg" fadein 8
        show hg talk with dissolve
        pr "she has"
        show hg sad with dissolve
        m talk "Nobody forced her to do it - she wanted to."
        show hg sadtalk with dissolve
        pr "i..."
        show hg grief with dissolve
        pr "i can't deny that she enjoyed it."
        "Just hearing that makes me feel sick."
        show hg calmtalk with dissolve
        pr "my father was the first man she'd ever slept with."
        show hg grief with dissolve
        pr "and the only one she'd ever loved."
        show hg angry with dissolve
        pr "when he left her, she was furious."
        show hg talk with dissolve
        pr "a part of her wanted to find someone else to fill the hole in her heart my father left."
        show hg sadtalk with dissolve
        pr "but she couldn't - she hated men after what he'd done to her."
        show hg grief with dissolve
        pr "that... didn't stop her from wanting them."
        show hg angry with dissolve
        pr "everything that happened pushed her to do what she did. you can't just say she was evil and stop there."
        show hg talk with dissolve
        pr "nobody is evil on their own. it's the circumstances that push them to hurting others."
        show hg pain with dissolve
        pr "my mother was no exception."
        show hg sadtalk with dissolve
        pr "she... she told me that we remind her of our father."
        show hg grief with dissolve
        pr "i think that... a part of her must've loved me, in some way"
        show hg calmtalk with dissolve
        pr "and i loved her too - as a mother."
        show hg talk with dissolve
        pr "i sometimes wish she hadn't had to go through any of that."
        show hg sadtalk with dissolve
        pr "but... she did, and she was all i had."
        show hg pain with dissolve
        "I want to help him, but... I don't know where to start..."
        "He shouldn't love someone like her... someone who's hurt him so much."
        show hg neutral with dissolve
        m talk "Edward, I... I really want to help you live with your past."
        m talk "I can't believe you could've felt that way about her despite everything..."
        show hg talk with dissolve
        pr "i still do."
        show hg calm with dissolve
        m talk "Are you... alright after talking to me today?"
        show hg calmtalk with dissolve
        pr "i should be here tomorrow as well, if that's what you mean."
        show hg hostile with dissolve
        m talk "Oh, thank god... if you ever don't want to tell me something, just say it."
        m talk "Besides, the first one made me promise him I wouldn't make you feel bad like last time."
        show hg gasp with dissolve
        pr "...oh? he did?"
        show hg neu with dissolve
        "I nod."
        show hg calmtalk with dissolve
        pr "he really shouldn't make you promise that... if you don't force me to tell you some things, nobody else will."
        show hg pain with dissolve
        pr "he thinks he can help me that way... it's pointless."
        show hg hostile with dissolve
        m talk "He just wants to make it up to you somehow."
        show hg angry with dissolve
        pr "well... i should go now."
        show hg talk with dissolve
        pr "goodbye, dr.hart"
        hide screen easymeter
        hide screen purplemeter
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        stop music fadeout 5
        "He gets up in silence and leaves."
        jump breakchoice
    elif day == 17:
        scene bg mcdesk with dissolve
        play sound "knock2.ogg"
        play music "ost/neutral.ogg" fadein 10
        "I find myself holding my breath until I hear the sound of Edward knocking on the door."
        show hg neu with dissolve
        m cute "It's good to see you again ~"
        if easymeter:
            show screen easymeter
            show screen purplemeter
        show hg talk with dissolve
        pr "...hello"
        show hg hostile with dissolve
        m talk "How are you feeling today? Are you okay after last time?"
        show hg neutral with dissolve
        "He nods."
        show hg talk with dissolve
        pr "do you have any quesions about yesterday? i'd rather get to the point."
        show hg angry with dissolve
        "He seems tense... I should do what he asks me to."
        show hg hostile with dissolve
        m talk "From your point of view, how did you all manage to lead a normal life for these past 15 years?"
        m fab "Aside of what happened with the third recently, since I take it it wasn't very frequent before."
        show hg calmtalk with dissolve
        pr "you're right."
        show hg talk with dissolve
        pr "james only started to come out a lot about a year ago..."
        show hg grief with dissolve
        pr "i'm sorry if i can't quite place it in time, my memory is a bit blurry..."
        show hg sad with dissolve
        m talk "It's fine. Go on."
        show hg calmtalk with dissolve
        pr "i don't think that much has happened with him since he first emerged..."
        show hg talk with dissolve
        pr "maybe he wasn't really needed for anything for a while, so it was mostly just tom and i."
        show hg neutral with dissolve
        pr "of course, tom being the core meant he's had the most time."
        "I nod."
        m fabtalk "Has anything happened to cause James to start fronting more frequently?"
        show hg talk with dissolve
        pr "actually, yes."
        show hg pain with dissolve
        pr "about a year ago, i think, we... {i}i{/i} started having nightmares about, um... our past."
        show hg sadtalk with dissolve
        pr "and before that we rarely had those, or they... weren't very impactful."
        stop music fadeout 5
        show hg calm with dissolve
        "He pauses for a moment."
        show hg pain with dissolve
        pr "i really apologize for all the stuttering today, i don't know what's gotten into me..."
        show hg hostile with dissolve
        m conf "I don't mind. You can talk at your own pace."
        play music "ost/hospital.ogg" fadein 10
        show hg pain with dissolve
        pr "umm... the point i was trying to make is... we started having these nightmares, and it was really, um... triggering."
        show hg talk with dissolve
        pr "i usually tried to avoid thinking about the past, so we could have a fairly normal life and focus on what's ahead, without looking back at any of that..."
        show hg sadtalk with dissolve
        pr "so seeing it all again, and with so much... realism to it, it felt like... she was actually there. doing all these things"
        show hg pain with dissolve
        pr "both tom and i had these dreams, but... of course, his weren't as bad - they only showed what she did to {i}him."
        show hg grief with dissolve
        pr "i think they really... shook both of us, if that's the right word."
        show hg talk with dissolve
        pr "we started switching in and out a lot more frequently than what we were used to."
        show hg angry with dissolve
        pr "...mostly back and forth between the two of us, but since that didn't work, we needed james again - he didn't have these nightmares."
        show hg calmtalk with dissolve
        pr "so it really wasn't difficult for him to get mixed into that as well, and for a while, he did really well to deal with these dreams."
        show hg grief with dissolve
        pr "there was a time when i actually thought it could work."
        show hg talk with dissolve
        pr "but of course, we weren't really used to more than two of us, and james... well, he never liked to fit in, i think."
        show hg angry with dissolve
        pr "so it became a mess. we never knew who we were switching into and who was before us, we had no communication with each other, and we still don't."
        show hg sadtalk with dissolve
        pr "i think... both tom and james value their time so much, they would never let themselves switch consciously."
        show hg calmtalk with dissolve
        pr "that's probably why it's very rare for us to switch during the day."
        show hg calm with dissolve
        m boretalk "I see..."
        show hg talk with dissolve
        pr "i've heard most people do that, though, so... we must be unique. in some way."
        show hg calm with dissolve
        "It's true that there's a lot of variety among the people with this disorder in particular, due to how complex it is."
        show hg neutral with dissolve
        m serious "So everything regarding your past is triggering for you?"
        show hg talk with dissolve
        pr "generally speaking, yes."
        show hg pain with dissolve
        pr "it's different for every one of us, i definitely react more intensely to, um... intimacy than the rest."
        show hg talk with dissolve
        pr "so it varies, but i don't think i can tell you anything that really triggers james... he doesn't seem to have any, um... fears and such."
        show hg hostile with dissolve
        m angry "And these nightmares were really upsetting for both of you because they reminded you of how you felt with your mother."
        show hg neu with dissolve
        "He nods."
        show hg neutral with dissolve
        m uncom "Is it okay for you to talk about exactly how you felt for these four years every time she forced you into... all of that?"
        stop music fadeout 5
        show hg pale with dissolve
        show hg calm with Dissolve(0.3)
        show hg neutral with Dissolve(0.3)
        pr "it is"
        show hg pain with dissolve
        pr "...."
        show hg sadtalk with dissolve
        pr "i think... it would help if you asked about something specific, i have... too many vivid memories to describe it all on my own."
        show hg grief with dissolve
        play music "ost/neutral.ogg" fadein 10
        "Where should I begin?"
        menu:
            "You never wished for her to be gone?":
                show hg talk with dissolve
                pr "no, never. i never wished her harm, if that's what you meant."
                show hg pain with dissolve
                pr "but i did want it to stop"
            "Were you always capable of waiting it out patiently?":
                show hg calmtalk with dissolve
                pr "i had to. so the vast majority of the time, i had no trouble obeying her."
                show hg pain with dissolve
                pr "i'm not saying that made it any better."
        menu:
            "So she tried to make you break?":
                show hg talk with dissolve
                pr "she absolutely did. it was quite difficult with me, but she learned quickly - i had to adapt even more quickly."
            "Did she ever notice the shift between you and Tom?":
                show hg talk with dissolve
                pr "she did... she thought it was strange how silent we suddenly were."
                show hg calmtalk with dissolve
                pr "it angered her, i think."
        show hg sad with dissolve
        m fab "Did she ever abuse you outside of that one hour or so every day?"
        show hg calmtalk with dissolve
        pr "no, not really..."
        show hg sadtalk with dissolve
        pr "i may be wrong... if you really want to know, you should probably ask tom in person."
        show hg sad with dissolve
        m talk "That's fine."
        "I had one more question in mind..."
        show hg hostile with dissolve
        m serious "How do you feel about these events now, recalling them? Do you ever think about them?"
        stop music fadeout 8
        show hg calm with dissolve
        pr "um..."
        show hg calmtalk with dissolve
        pr "these nightmares we had... were really..."
        show hg pain with dissolve
        pr "thought... provoking."
        show hg angry with dissolve
        pr "despite everything, they forced me to relive a part of that, and i started to recall all of it."
        show hg talk with dissolve
        pr "i realized some things then."
        play music "ost/tension.ogg" fadein 10
        show hg calmtalk with dissolve
        pr "the reason i exist is to take the pain away from tom."
        show hg grief with dissolve
        pr "so, once the pain is gone, along with my mother, i... serve no purpose like this."
        show hg talk with dissolve
        pr "and, um... i started to think that... if our mother was back, i would feel like there's a reason for me to keep living at all."
        show hg sadtalk with dissolve
        pr "i also realized that i... i..."
        show hg grief with dissolve
        pr "a part of me misses her. and everything she used to do to me."
        show mcshock
        "...!"
        "He can't be serious... this is..."
        pr "i just... I sometimes feel like... it would be so much easier to be forced like that again."
        "I don't know what to say."
        "He doesn't stop talking, despite my silence."
        hide mcshock with dissolve
        pr "i don't know how to... i can't... be with people."
        show hg sadtalk with dissolve
        pr "i just want to give up..."
        show hg cry2talk with dissolve
        pr "...but you don't let me... nobody does..."
        show hg cry2 with dissolve
        "He sobs suddenly."
        "I look at him intently, concerned."
        "I don't know what to do!"
        show hg cry2talk with dissolve
        pr "nobody understands what it's like... to have been through all of that..."
        stop music fadeout 3
        show hg cry2 with dissolve
        pr "i... i..."
        show hg scream with dissolve
        pr "{i}I can't go on like this-!"
        show hg cry with dissolve
        "The tone of his voice changes completely."
        play music "ost/emo.ogg" fadein 6
        show hg grief with dissolve
        pr "i'm... so sorry... i don't feel like myself today..."
        m boretalk "That's okay, You'll probably switch soon."
        show hg pain with dissolve
        "He nods."
        show hg calmtalk with dissolve
        pr "i think so."
        show hg grief with dissolve
        pr "but... right now i feel like..."
        show hg sadtalk with dissolve
        pr "...my head hurts... it feels really confusing."
        show hg sad with dissolve
        "He sobs again. He looks like he's about to cry."
        show hg cry2talk with dissolve
        pr "[name]... help me... {i}please"
        show hg cry2 with dissolve
        m confusion "What should I do?"
        show hg cry2talk with dissolve
        pr "i... i... i don't know..."
        pr "i'm giving up... i don't care what you do. just..."
        show hg scream with dissolve
        pr "{cps=6}dO soMEthInG"
        show hg cry with dissolve
        "His voice is shaky."
        show hg cry2talk with dissolve
        pr "don't ask me... just do whatever you want and stop... expecting me to..."
        show hg cry2 with dissolve
        "He lowers his head and sobs again. A tear falls down his pale blue eye."
        "I can't let him cry like this!"
        "He's been through too much in his life for me to let him suffer now."
        "I need to protect him. I'm all he has right now."
        "Without thinking, I reach out to place my hand on his, shaking at the edge of my desk."
        show hg cry with dissolve
        "His eyes are fixated on me."
        "I feel a wave of pure dread wash over me when I see the look in them."
        "...He's afraid of me."
        m serious "Edward... you're safe with me. I would never hurt you."
        show hg cry2 with dissolve
        "I feel his hands becoming slightly more steady, but he's still trembling."
        "God, how many times has he been like this without anyone to help him?"
        "He's not backing away from me, of course he isn't, but I can still see fear in his eyes."
        "I don't think anyone's been this close to him since... his mother."
        "I can't help him if he doesn't trust me... What do I do?"
        menu:
            "Hug him":
                $route = "no"
                stop music fadeout 6
                show drk with dissolve
                "I get up from my chair and bridge the gap between us over my desk, embracing him with all the warmth I can give."
                show hg pale with dissolve
                "He freezes."
                show hg calm with dissolve
                pr "...."
                play music "ost/tension.ogg" fadein 10
                "He's not doing anything to push me away, he's just... still."
                m regrettalk "Edward... what are you so afraid of?"
                show hg pain with dissolve
                pr "...."
                "I hug him more tightly, feeling his trembling body in my arms."
                show hg grief with dissolve
                "I place my hand on his back slowly."
                show hg shock with dissolve
                "He gasps."
                show hg grief with dissolve
                pr "please... stop it..."
                show hg cry2 with dissolve
                "I feel a single tear falling onto my cheek."
                "What other way is there to help him stop fearing this than doing it?"
                "I need him to realize I won't hurt him."
                m sadtalk "I'm not your mother, Edward. You're safe."
                show hg cry with dissolve
                pr "...."
                "He's silent."
                show hg cry2talk with dissolve
                pr "don't... talk to me..."
                show hg cry2 with dissolve
                m regret "...."
                hide drk with dissolve
                "I pull back, away from him."
                show hg dread with dissolve
                "He's glaring at me in silence."
                m sadtalk "I'm sorry. I thought it would help."
                "I really did..."
                show hg grief with dissolve
                pr "...."
                "I feel like a failure..."
                stop music fadeout 5
                show hg sad with dissolve
                m uncom "You may leave for today... thank you for your time."
                play sound "doorclose.ogg" fadein 1
                scene bg mc with dissolve
                "Without a word, he gets up and leaves my office. He looks shaken."
                "I don't have the strength to get up from my chair for the longest time... what have I done..?"
                scene black with dissolve
                pause 2
            "Touch his face":
                "I slowly let go of his hands, making sure to never let him lose sight of what I'm doing, and lean in a bit closer to him."
                show hg dread with dissolve
                "He's holding his breath, glaring at me with wide eyes. When he sees my hand about to touch his face, he shuts them immediately."
                show hg grief with dissolve
                m fabtalk "May I?"
                stop music fadeout 7
                show hg pale with dissolve
                "He stares at me in shock. Obviously, he's not used to being asked for permission."
                "I want him to see how different what I want to do is from what his mother's done."
                play music "ost/ship.ogg" fadein 10
                show hg calm with dissolve
                "He nods slowly and I place my hand on the side of his face, letting my fingertips gently brush against his cheek, still wet with tears."
                "I reach out with my left hand to move his hair a bit to the side so I can finally see both of his eyes."
                show hg neu with dissolve
                "The brown one seems much calmer."
                m conf "Edward... there's nothing to be afraid of."
                show hg calm with dissolve
                "I move my hands a little to touch his cheeks softly, careful not to startle him."
                "He closes his eyes. Does he really... trust me already..?"
                "I slowly move my fingers to touch his face, his hair, eventually placing both of my hands on his shoulders."
                "I hesitate a little before resting my left hand on his bare shoulder."
                show hg hostile with dissolve
                m talk "Is this... okay?"
                show hg neu with dissolve
                "He nods again, this time without hesitation."
                show hg neutral with dissolve
                m neu "...."
                "I think I can go on like this."
                "If I'm given the chance to comfort him, I won't stop here."
                "I get up from my chair. He's watching me without a word."
                show hg hostile with dissolve
                "Making my way over to his side of the desk, I barely have the time to think about what I'm about to do."
                "I'm more than ready, and he seems calm so far."
                show hg neu with dissolve
                "I lean down a little and place my hands on his shoulders again."
                m regrettalk "Can I... hug you?"
                "Regardless, I need to ask."
                show hg shock with dissolve
                pr "hug... me..?"
                show hg blush with dissolve
                "I nod."
                m talk "I won't if you don't want me to."
                if PurpleHeart>17:
                    $HangedShip=True 
                    show hg sadtalk with dissolve
                    pr "no, i-"
                    show hg angry with dissolve
                    pr "you can. you can"
                    show hg hostile with dissolve
                    "He looks up at me, almost pleadingly."
                    m boretalk "Tell me when to stop."
                    "He nods quickly, waiting for me to come closer."
                    show hg neutral with dissolve
                    "I have to admit, I'm quite nervous about this myself, but I won't stop now."
                    show edward 3 with dissolve
                    "I wrap my arms around his neck and slowly lift my legs onto his chair."
                    "Looking at him, I see no signs of fear or anxiety."
                    "Hesitantly, I pull him closer, resting my head on his shoulder."
                    "Now I'm the one who's trembling."
                    "I've never felt so... close to anyone before."
                    "I can feel his heartbeat on my chest."
                    show edward 2 with dissolve
                    "Suddenly, he wraps his arms around me as well, and I tighten my own grip."
                    "I just want him to be close to me like this... I haven't felt this way in such a long time..."
                    m sadtalk "Edward?"
                    m serious "How do you feel?"
                    show edward 3 with dissolve
                    "He's silent for a moment."
                    pr "...different."
                    m neu "In what way?"
                    pr "like you're not going to hurt me."
                    pr "like... you care about me."
                    "I relax a little."
                    m sadsmile "I really care about you, Edward. I won't let anyone hurt you ever again."
                    show edward 2 with dissolve
                    pr "...thank you."
                    "He rests his head on my shoulder and falls silent."
                    "I'm so happy."
                    "To have helped him, made him believe that nobody's going to hurt him, but also because..."
                    "...I care about him. I've wanted this for a while now."
                    "And seeing how much he needed it makes me feel even better."
                    "I want to stay like this. With him."
                    "I don't want to let go..."
                    "I let my hand wander on his back a little before burying it in his long hair. I hope he doesn't mind."
                    m kawaii "I'm so happy to have met you."
                    pr "[name]... you have no idea how much you've done for me."
                    "I touch his face softly and pull back a little to look into his eyes."
                    "I don't know what's gotten into me, but I don't want this to stop."
                    "I don't care if anyone finds out."
                    "I don't even care if I get fired for this as long as I get to stay with him this way."
                    "Of course, nobody among the staff here would approve of this, but... I felt like it's for the best for both of us."
                    "It's the only way I can make him feel happy and at peace with his past."
                    "I stroke his cheek absentmindedly, lost in thought for a moment."
                    show edward 1 with dissolve
                    "I don't realize when my fingertips brush against his parted lips."
                    "He freezes. I can feel his hands withdrawing from my back."
                    pr "i... i'm not ready for this."
                    stop music fadeout 5
                    pr "i'm sorry."
                    scene bg mcdesk with dissolve
                    show hg sad with dissolve
                    "I pull back, startled."
                    m regrettalk "No no, it's fine. I didn't really..."
                    play music "ost/hospital.ogg" fadein 10
                    "I stop myself before I can lie to him. Of course I wanted to..."
                    "God, what am I thinking?"
                    show hg grief with dissolve
                    m talk "It's not your fault, Edward."
                    "I get up and move back to my chair."
                    show hg sadtalk with dissolve
                    pr "just so you know... i won't take any of what i said just now back."
                    show hg calmtalk with dissolve
                    pr "i really... care a lot... about you"
                    show hg talk with dissolve
                    pr "i just... i'm not ready. i'm sorry."
                    show hg hostile with dissolve
                    "I force myself to move back in my chair and go back to being my usual, more composed self."
                    m neu "Well... we're running out of time for today, I think."
                else: ## later you're locked to platonic route
                    stop music fadeout 5
                    show hg sad with dissolve
                    pr "...."
                    show hg grief with dissolve
                    pr "i'm sorry..."
                    show hg sadtalk with dissolve
                    pr "i don't think i can do that right now."
                    play music "ost/hospital.ogg" fadein 10
                    show hg sad with dissolve
                    "I nod and go back to my chair, giving him more space."
                    m talk "I understand."
                    show hg calmtalk with dissolve
                    pr "i'm... i'm not ready for it"
                    show hg sad with dissolve
                    m talk "Don't worry about it."
                    "I look at his face more closely, searching for any signs of tears."
                    m talk "How do you feel now?"
                    show hg talk with dissolve
                    pr "...better."
                    show hg grief with dissolve
                    pr "i... didn't expect you to do any of that..."
                    show hg calmtalk with dissolve
                    pr "i thought you would just... try to calm me down."
                    show hg talk with dissolve
                    pr "but... you helped. i didn't expect that..."
                    show hg neutral with dissolve
                    m talk "Anything you need, Edward. I'm always here to help."
                    show hg smile with dissolve
                    pr "thank you so much..."
                    "...."
                    m talk "We're running out of time for today."
                show hg neu with dissolve
                pr "oh"
                show hg hostile with dissolve
                m talk "But... I'm happy with the progress we've made. We can discuss that\nmore in-depth tomorrow, if you want."
                show hg calm with dissolve
                pr "actually..."
                show hg talk with dissolve
                pr "i think if you talked to us tomorrow, it would be the third."
                show hg calmtalk with dissolve
                pr "i feel like... he's close."
                show hg neutral with dissolve
                "I nod and lead him to the door."
                show hg neu with dissolve
                "I can't stop myself. I touch his face gently before he can leave and look up into his eyes."
                show hg calm with dissolve
                m talk "It's okay. Whenever you're back, we will see each other again."
                show hg smileblush with dissolve
                pr "thank you... [name]"
                play sound "doorclose.ogg" fadein 1
                scene bg mc with dissolve
                stop music fadeout 5
                "He leaves quickly."    
            "Talk to him":
                $professional+=2
                m talk "Edward, please say something..."
                m talk "I want to help you."
                show hg pain with dissolve
                stop music fadeout 5
                pr "please... don't do anything else..."
                show hg grief with dissolve
                pr "...just leave me alone..."
                play music "ost/tension.ogg" fadein 10
                "I withdraw my hand and lean back in my chair, further away from him."
                m talk "Is this better?"
                show hg hostile with dissolve
                "He nods hesitantly."
                show hg sad with dissolve
                pr "...."
                m serious "I don't want to hurt you. I thought you would feel better..."
                show hg grief with dissolve
                m regrettalk "I know what you've been through, and I'm trying my best, but it's... difficult."
                show hg calmtalk with dissolve
                pr "i don't blame you for my problems... i know it's irrational to act like this..."
                show hg calm with dissolve
                m talk "No, you have every right to feel that way. Really."
                m regret  "It's just that... I'm not sure how to help you... so it's my fault."
                show hg sadtalk with dissolve
                pr "i'm sorry for causing you trouble..."
                show hg grief with dissolve
                m sad  "...."
                pr "...."
                stop music fadeout 6
                scene black with dissolve
                "We spend the rest of the session in silence. I don't know what to say."
                "Once the time runs out, he leaves quickly, thanking me, even though I haven't really done anything to help."
                $route = "no"
        hide screen easymeter
        hide screen purplemeter
        jump patientsattack
##########################
    elif day == 18:
        jump breakevent1
    elif day == 19:
        jump breakevent2
    elif day == 20:
        jump tombreakevent
    elif day == 21:
        jump breakevent3
##########################
    elif day == 22:
        jump gmeeting
    elif day == 23:
        jump callhospital
    elif day == 24:
        jump breakend

label wednesdayhanged: ##passing by his room, he's unstable and almost switching
    scene bg mc with dissolve
    "My work for today is over."
    play music "footsteps.ogg" fadein 4
    scene bg central with dissolve
    "What Edward told me today... I wasn't prepared for that."
    "I can see why it was so hard for them to talk about it... maybe I pushed him too much."
    show bg patients with dissolve
    stop music fadeout 3
    "...."
    "XVI. Should I take a look inside..?"
    menu:
        "Yes":
            $PurpleHeart+=1
            play sound "knock2.ogg"
            m uncom "Edward?"
            pr "...dr. hart? did you need something?"
            play music "ost/tran.ogg" fadein 6
            "It's definitely still him."
            m fabtalk "Can I come in? I wanted to check on you before I leave for today."
            pr "...."
            stop music fadeout 6
            pr "of course. come in."
            "He seemed hesitant, probably because he didn't expect me to visit him like that."
            show bg tom with dissolve
            show hg full with dissolve
            m sadtalk "How do you feel?"
            play music "ost/hospital.ogg" fadein 6
            pr "like we're dissociating again."
            m talk "So you'll be switching?"
            "He nods."
            pr "i'll be gone soon."
            pr "i, um... my head hurts. it happens a lot before we switch."
            m sad "...."
            m serious "I'm sorry about today. I know that must have been difficult for you -"
            pt "stop it"
            pr "someone had to tell you."
            m regrettalk "I'm just sorry it had to be you."
            pr "...in the end, it's always me."
            "...."
            pr "you should leave. someone else is really close and i don't think any of us wants you to see that."
            "I get that he might feel uncomfortable with me seeing him switch, especially since it only happens when they're unconscious."
            "I should give him space."
            "...at the same time, I feel like I should say something."
            menu:
                "I'll be waiting for you to be back":
                    $PurpleHeart+=1
                    $personal+=2
                    pr "...."
                    "He looks at me with an unreadable expression before giving me a faint smile."
                    pr "thank you, doctor."
                "It'll be okay":
                    $personal+=1
                    pr "don't worry about me. it won't be the first time this happens."
                    "I suppose he's right."
                "Goodbye":
                    pass
            play sound "doorclose.ogg" fadein 1
            scene bg patients with dissolve
            "I leave their room."
            "Everything that's happened recently only makes me empathize with Edward more. He's been through so much, and it never seems to stop."
            "Even now, he mostly appears when something hard is about to happen, like telling me what happened to them."
            scene bg front with dissolve
            "I try my best to make him feel more comfortable, but it's so difficult, given what we have to talk about."
            "I hope I can at least ease his pain by showing him how much I appreciate what he's doing for this therapy."
            "Without him, I might not have learned anything... it was his appearence that prompted Tom to speak up about his past, after all."
            scene black with Dissolve(1.0)
            "I wonder who I'm about to see tomorrow... Tom? Or the mysterious third alter I haven't met yet?"
        "No":
            "I don't want to disturb them."
            scene black with dissolve
            "I make my way outside and go home."
    jump nextday
label fridayemperor:
    scene bg mc with dissolve
    "My work for today is over."
    "I gather my belongings and leave my office."
    play music "footsteps.ogg" fadein 4
    show bg offices with dissolve
    "I can't get over what James did today... the nerve."
    show bg central with dissolve
    "Still, I have to wonder if that's all there was to it - maybe he really thinks he can \"seduce\" me like that."
    show bg patients with dissolve
    "Whatever ulterior motive he had, I'm not planning to fall for any of it."
    stop music
    show bg with vpunch
    "!!!"
    "I'm almost out of the second floor when I feel a hand on my shoulder."
    show jm full with dissolve
    play music "ost/james.ogg" fadein 5
    er "And where are you going, sweetheart ~?"
    menu:
        "Home.":
            $professional+=1
            er "I assumed that much."
        "Why do you care?":
            $personal+=1
            "He scoffs."
            er "I care about what you're doing, isn't that obvious?"
        "Away from you":
            $PurpleHeart+=1
            "He laughs."
            er "I don't think that's possible."
            er "I might be gone for a while, but I will be back eventually."
    m talk "Is there something you want? Because if not, I should be on my way."
    er "Ouch. It's very cold of you, treating me like that."
    m fab "...?"
    er "Do I need a reason to talk to you? I just figured if I'm still here and so are you, a goodbye is in order."
    m boretalk "I'm pretty sure the last one was quite enough."
    er "You think so?"
    m angry "Listen, whatever you wanted to accomplish by that, it didn't work."
    "He smiles from ear to ear and I feel like I've made a mistake."
    er "I don't accomplish things. They just happen along the way ~"
    "What..?"
    er "~ ~"
    m fabtalk "If you want me to like you more than the others, you should learn a thing or two from them."
    "He looks away from me for a moment. Is he... actually considering that?"
    m talk "Like not attacking me, for example."
    er "Did you feel attacked, darling? I didn't notice ~"
    "I sigh."
    m fab "I should get going. Goodbye, James."
    er "Have a lovely weekend, [name] ~"
    "Gee, thanks... I leave the hospital."
    jump nextday
label tombreakevent:
    scene black with dissolve
    "I still have five days until I can go back to work."
    "...to them."
    "I wonder if anything's happened since the last time I called..."
    "I pick my phone up to call again."
    "I feel like an overprotective mother, but I have to make sure everything is as it should be."
    "I call the reception for the second time."
    gu "Hello? Ms. Hart?"
    "It's the same nurse from last time."
    m fabtalk "I'm just... calling to make sure everything is still okay with my patients."
    gu "Let's see... um, nothing seems unusual..."
    gu "Other than Mr. Richards appearing most commonly as his third alter recently."
    "James... that's unusual."
    "He seemed to be somewhat rare."
    m sadsmile "Thank you, nurse. I'm sorry about... calling like this."
    m frust "...Again."
    m serious "I'm just..."
    gu "Worried about your patients? Anxious to get back to work?"
    gu "It's fine, really. At least some people here take their job seriously."
    m flirt "Thank you again. I'll be back soon."
    "I hang up and feel a wave of relief wash over me."
    "Everything seems to be going well."
    "Now that I think about it..."
    "Switching to James does make sense after what happened the last time I saw them."
    "I wonder if he'll still be there once I'm back..."
    "Come to think of it, I barely spoke to him. I barely even know him."
    "Either way, I'm anxious to get back to work after this break."
    jump janeback2
        