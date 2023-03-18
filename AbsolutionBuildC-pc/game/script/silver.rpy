define wt = Character("William", screen='cinematic', color='#ffffff')

default Moonship = False
default ShadowTalk = False

default moonsharpeknow = False
default moonshadowfused = False
default tellsharpemoondreams=False

default williamw51="calm"
default wanxiety=5
default wshadow=0
default WilliamEnd=""

image moon1 1 = "cg/Moon11.png"
image moon1 2 = "cg/Moon12.png"
image moon1 3 = "cg/Moon13.png"
image moon1 4 = "cg/Moon14.png"
                                  
## SHADOW sprites ##########################
image w sa: ##eye opening
    "sprites/moon/s/a1.png" with Dissolve(1.0)
    pause .3
    "sprites/moon/s/a2.png" with dissolve
    pause .1
    "sprites/moon/s/a3.png" with dissolve
image w sb: ##eye closing
    "sprites/moon/s/a3.png" with Dissolve(0.7)
    pause .2
    "sprites/moon/s/a2.png" with dissolve
    pause .1
    "sprites/moon/s/a1.png" with dissolve    
image w s1 = "sprites/moon/s/1.png"
image w s2 = "sprites/moon/s/2.png"
image w s3 = "sprites/moon/s/3.png"
image w s4 = "sprites/moon/s/4.png"
image w s5 = "sprites/moon/s/5.png"
image es s:
    "sprites/moon/s/e3.png"
    pause 4
    "sprites/moon/s/e1.png"
    pause 0.06
    "sprites/moon/s/e2.png"
    pause 0.06
    "sprites/moon/s/e1.png"
    pause 0.06
    repeat
image w sc1 = "sprites/moon/s/c1.png"
image w sc2 = "sprites/moon/s/c2.png"
image w sc3 = "sprites/moon/s/c3.png"
image w sc4 = "sprites/moon/s/c4.png"
image w sc5 = "sprites/moon/s/c5.png"
image es c:
    "sprites/moon/s/ce3.png"
    pause 4
    "sprites/moon/s/ce1.png"
    pause 0.06
    "sprites/moon/s/ce2.png"
    pause 0.06
    "sprites/moon/s/ce1.png"
    pause 0.06
    repeat

label silvernotes:
    if month == 1:
        if day == 6 or day ==  7 or day == 13 or day == 14 or day > 17:
            jump silvernav
    if nmoon1=="":
        $nmoon1 = renpy.input("Note 1 (max 50 characters):", length = 50)
    else:
        if nmoon2=="":
            $nmoon2 = renpy.input("Note 2 (max 50 characters):", length = 50)
        else:
            if nmoon3=="":
                $nmoon3 = renpy.input("Note 3 (max 50 characters):", length = 50)
            else:
                if nmoon4=="":
                    $nmoon4 = renpy.input("Note 4 (max 50 characters):", length = 50)
                else:
                    if nmoon5=="":
                        $nmoon5 = renpy.input("Note 5 (max 50 characters):", length = 50)
                    else:
                        if nmoon6=="":
                            $nmoon6 = renpy.input("Note 6 (max 50 characters):", length = 50)
                        else:
                            if nmoon7=="":
                                $nmoon7 = renpy.input("Note 7 (max 50 characters):", length = 50)
                            else:
                                if nmoon8=="":
                                    $nmoon8 = renpy.input("Note 8 (max 50 characters):", length = 50)
                                else:
                                    if nmoon9=="":
                                        $nmoon9 = renpy.input("Note 9 (max 50 characters):", length = 50)
                                    else:
                                        if nmoon10=="":
                                            $nmoon10 = renpy.input("Note 10 (max 50 characters):", length = 50)
                                        else:
                                            if nmoon11=="":
                                                $nmoon11 = renpy.input("Note 11 (max 50 characters):", length = 50)
                                            else:
                                                if nmoon12=="":
                                                    $nmoon12 = renpy.input("Note 12 (max 50 characters):", length = 50)
                                                else:
                                                    if nmoon13=="":
                                                        $nmoon13 = renpy.input("Note 13 (max 50 characters):", length = 50)
                                                    else:
                                                        if nmoon14=="":
                                                            $nmoon14 = renpy.input("Note 14 (max 50 characters):", length = 50)
                                                        else:
                                                            if nmoon15=="":
                                                                $nmoon15 = renpy.input("Note 15 (max 50 characters):", length = 50)
                                                            else:
                                                                if nmoon16=="":
                                                                    $nmoon16 = renpy.input("Note 16 (max 50 characters):", length = 50)
                                                                else:
                                                                    if nmoon17=="":
                                                                        $nmoon17 = renpy.input("Note 17 (max 50 characters):", length = 50)
                                                                    else:
                                                                        if nmoon18=="":
                                                                            $nmoon18 = renpy.input("Note 18 (max 50 characters):", length = 50)
                                                                        else:
                                                                            if nmoon19=="":
                                                                                $nmoon19 = renpy.input("Note 19 (max 50 characters):", length = 50)
                                                                            else:
                                                                                if nmoon20=="":
                                                                                    $nmoon20 = renpy.input("Note 10 (max 50 characters):", length = 50)
                                                                                else:
                                                                                    "I've already filled up all my notes."
                                                                                    "Should I rewrite one of my notes?"
                                                                                    menu:
                                                                                        "[nmoon1]":
                                                                                            $nmoon1 = renpy.input("Note 1 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon2]":
                                                                                            $nmoon2 = renpy.input("Note 2 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon3]":
                                                                                            $nmoon3 = renpy.input("Note 3 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon4]":
                                                                                            $nmoon4 = renpy.input("Note 4 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon5]":
                                                                                            $nmoon5 = renpy.input("Note 5 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon6]":
                                                                                            $nmoon6 = renpy.input("Note 6 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon7]":
                                                                                            $nmoon7 = renpy.input("Note 7 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon8]":
                                                                                            $nmoon8 = renpy.input("Note 8 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon9]":
                                                                                            $nmoon9 = renpy.input("Note 9 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon10]":
                                                                                            $nmoon10 = renpy.input("Note 10 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon11]":
                                                                                            $nmoon11 = renpy.input("Note 11 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon12]":
                                                                                            $nmoon12 = renpy.input("Note 12 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon13]":
                                                                                            $nmoon13 = renpy.input("Note 13 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon14]":
                                                                                            $nmoon14 = renpy.input("Note 14 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon15]":
                                                                                            $nmoon15 = renpy.input("Note 15 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon16]":
                                                                                            $nmoon16 = renpy.input("Note 16 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon17]":
                                                                                            $nmoon17 = renpy.input("Note 17 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon18]":
                                                                                            $nmoon18 = renpy.input("Note 18 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon19]":
                                                                                            $nmoon19 = renpy.input("Note 19 (maximum 50 characters):", length = 50)
                                                                                        "[nmoon20]":
                                                                                            $nmoon20 = renpy.input("Note 20 (maximum 50 characters):", length = 50)
                                                                                        "Don't rewrite":
                                                                                            jump breaknav
    "Write another note?"
    menu:
        "Yes":
            jump silvernotes
        "No":
            if route=="silver":
                jump breakreal
            jump breaknav

label silvernav:
scene black with dissolve
pause 1
$firstpatient = "silver"
$sessions += 1
########################## 
if month == 1:
    if day == 8:
        scene bg mcdesk with dissolve
        if easymeter:
            show screen easymeter
            show screen silvermeter
        play music "ost/hospital.ogg" fadein 6
        m talk "I promised I wouldn't leave you now."
        show w frust with dissolve
        w "...."
        show w frusttalk with dissolve
        w "I can't stop you..."
        show w talk with dissolve
        w "If you don't care about my warnings, then so be it."
        show w neutral with dissolve
        m flirt "How was the weekend? Did you make up your mind about sharing your past with me?"
        show w frusttalk with dissolve
        stop music fadeout 5
        w "I guess it can't be avoided..."
        show w talk with dissolve
        w "I should start from the beginning."
        show w neutral with dissolve
        m fabtalk "Go on, please."
        show sback 1 with dissolve
        play music "ost/memory.ogg" fadein 10
        w "My parents died in a car accident when I was 5."
        w "I don't remember them well, neither the crash itself."
        w "All I know is that I survived without any injuries."
        w "...And they didn't."
        w "I was... a bit troublesome afterwards, since I didn't have any close relatives."
        w "At least, that's what I thought."
        w "It turned out my father had an older brother with whom he didn't get along very well."
        w "They hadn't met for years at least before my father's death."
        w "Once he was found, the obvious choice was for me to be raised by him, along with his two daughters."
        w "I... don't think he was very happy to have another child to take care of, especially one that wasn't his own."
        w "But he agreed in the end."
        w "My cousins eventually started treating me like a brother, but for him... I think I was always the odd one out, in a way."
        w "He tended to be more strict with me than he was with his own children. I... suppose either way I should be grateful he even agreed to take care of me."
        w "He'd always... make sure I appreciated that. He often said that if it wasn't for him, I'd be miserable."
        w "I guess he was right."
        m talk "Maybe he was, but he shouldn't have used something you didn't have control over against you."
        stop music fadeout 5
        m fabtalk "It seems unfair to use the death of your parents as an argument against you."
        show w talk with dissolve
        hide sback with dissolve
        w "Well, that's the way I was raised, so I never questioned it."
        show w frust with dissolve
        w "...."
        show w talk with dissolve
        w "Um... You distracted me. What was I talking about?"
        show w neutral with dissolve
        m "Your uncle."
        show w siden with dissolve
        w "Right."
        play music "ost/memory.ogg" fadein 10
        show sback 2 with dissolve
        w "...I don't really have much to say about him..."
        m neu "How would you describe him overall?"
        w "Um... strict. A bit cold."
        w "He never really showed any appreciation for what I did right, but always made sure to notice when I failed."
        w "I... guess authoritarian might be a good word."
        m talk "I see."
        w "Compared to the other children my age, I'd say he had more influence over us than most parents."
        w "He liked to know where we were and what we were doing at all times."
        w "But in his mind, he was doing good. He wouldn't let anything bad happen to us... His daughters, mostly."
        w "I think he really loved both of them."
        m serious "And what about you?"
        w "...."
        w "I... don't know..."
        w "I've always wanted to believe that he cared about me as well."
        m angry "You wanted to? And how do you really feel?"
        w "I... I don't think anyone's ever cared. About me."
        w "I used to think to myself sometimes - \"If I died right now, would anyone even cry?\"."
        w "For the past 10 years or so I've known the answer."
        w "But... before that..."
        w "...there was only one person who ever cared. At least, there was a time when I really believed she did."
        show sback 3 with dissolve 
        w "Marie, my cousin. She was two years older than me."
        w "She was the only one who ever made me feel like... I mattered to anyone."
        w "She could always tell what was bothering me."
        w "She was so determined to make me feel like a part of the family that... she almost succeeded."
        w "In return, I helped her take care of her sister when she was too busy to look after her."
        w "Ann was just three years younger than me, but she always seemed a lot smaller than that."
        w "Regardless, everyone loved her - she was always so bright and enthusiastic, it was hard to dislike her."
        w "Marie, on the other hand... we were a lot closer, I think."
        w "She was the only one who understood me. We had no secrets from each other."
        w "To an extent, she was like a mother to me - and she embraced that."
        w "I never asked her to be that way for me, but... I think she just saw that... it was what I needed the most."
        w "Strangely, it worked out perfectly."
        w "To me, she was like a bottomless well of patience and strength."
        w "I have no idea where she got all of that... it was like she was never tired of me."
        w "Whenever my uncle would cross a line, she was there to protect me."
        w "He listened to her, he trusted her."
        w "And she was always on my side."
        "He's silent for a moment."
        hide sback with dissolve
        stop music fadeout 5
        show w regrettalk with dissolve
        w "I think... I really..." 
        show w paintalk with dissolve
        w "...miss having someone like her."
        play music "ost/hospital.ogg" fadein 8
        show w pain with dissolve
        m serious "William... There's nothing wrong with wanting to have someone care about you."
        show w sadtalk with dissolve
        w "But... I should be the one to do that for others..."
        show w regrettalk with dissolve
        w "I... I hate being so helpless."
        show w paintalk with dissolve
        w "Like I can't do anything on my own."
        show w sad with dissolve
        menu:
            "It's just the way it is":
                show w regrettalk with dissolve
                w "I know... I can't change it."
            "Your relationship with Marie was mutual":
                $SilverHeart+=1
                show w shock with dissolve
                w "W-What?"
                show drk with Dissolve(0.75)
                show s 1 with dissolve
                show s 2 with Dissolve(1.0) 
                $renpy.pause(0.75, hard = True)
                hide s with dissolve
                hide drk with dissolve
                show w regrettalk with dissolve
                w "But... I didn't do anything to repay her for any of it..."
                show w sad with dissolve
                m pity "You didn't have to."
                show w fear with dissolve
                m neu "Where do you think she got all that strength from?"
                show w frust with dissolve
                m fabtalk "You were the reason she was able to help people like she did."
                show w regrettalk with dissolve
                w "How..? No, I would have known if that was the case..."
                show w angrytalk with dissolve
                w "...you're wrong. I was useless to her."
                show w regrettalk with dissolve
                w "Just like I am to everyone else..."
            "You're not helpless":
                $personal+=1
                show w sadtalk with dissolve
                w "I've been nothing but a disappointment to everyone my whole life."
                show w regrettalk with dissolve
                w "If that's not helpless, then I don't know what is."
        stop music fadeout 4
        show w regret with dissolve
        w "...."
        show w tense with dissolve
        m "Did your relationship with Marie cause your illness to develop?"
        play music "ost/neutral.ogg" fadein 6
        show w tensetalk with dissolve
        w "Well... things got out of hand afterwards."
        show w frusttalk with dissolve
        w "I started getting kind of... self-conscious about spending time with my cousins."
        show w regrettalk with dissolve
        w "They were just too nice to me for their own good, I think..."
        show w regret with dissolve
        m fabtalk "What do you mean?"
        show w tense with dissolve
        w "...."
        show w tensetalk with dissolve
        w "I don't know how to put it..."
        show w frusttalk with dissolve
        w "I think... I've gotten too attached to them... Especially to Marie."
        show w regrettalk with dissolve
        w "She... she was the closest person to me at that time."
        show w sadtalk with dissolve
        w "I don't think anyone's ever been like this for me after her."
        show w sad with dissolve
        m neutral "I see."
        m serious "Did she not care about you as much as you thought in the end?"
        show w regrettalk with dissolve
        w "No, it's just that... It was... a lot more complex."
        show w frusttalk with dissolve
        w "She didn't... do anything wrong."
        show w tensetalk with dissolve
        w "...I was the one who failed."
        show w talk with dissolve
        w "If... you don't mind, I think we're running out of time. I'd rather not talk about this now."
        show w neutral with dissolve
        m flirt "You'll have to tell me tomorrow, then. I'll be waiting."
        show w talk with dissolve
        w "Perfect. I'll see you tomorrow."
        hide screen easymeter
        hide screen silvermeter
        stop music fadeout 5
        hide w with dissolve
        "He leaves in a hurry."
        jump breakchoice
    elif day == 9:
        play music "ost/neutral.ogg" fadein 6
        scene bg mcdesk with dissolve
        show w neutral with dissolve
        if easymeter:
            show screen easymeter
            show screen silvermeter
        m fabtalk "Are you ready to talk about how your illness began to develop?"
        show w frusttalk with dissolve
        w "There's no reason to procrastinate any further now either way."
        show w neutral with dissolve
        "He's probably right."
        m talk "I'm listening. I'll understand if you don't tell me all the details - I just need to know what happened."
        show w pain with dissolve
        "He nods."
        stop music fadeout 4
        show w talk with dissolve
        w "Then..."
        show w regrettalk with dissolve
        w "I should start from Marie."
        show sback 3 with dissolve
        play music "ost/memory.ogg" fadein 6
        w "It's not that we grew distant by any means... On the contrary, we would only become closer as time passed."
        w "And... I think... we reached a point where I couldn't take it anymore."
        m fabtalk "Why was that?"
        w "I... I started questioning... how I actually felt about her."
        m gasp "Meaning..?"
        w "She was too kind for me, and I was..."
        show sback 4 with dissolve
        w "Weak."
        w "So weak that I couldn't even respect her as I should have."
        m serious "Did you hurt her in some way? Or was she offended by something you did?"
        w "She... she had no idea."
        m uncom "How exactly did you disrespect her then?"
        w "I... I considered things I should never have considered. Things that... a normal person would never dare to try..."
        m talk "I see."
        m fabtalk "Did she find out in the end?"
        w "She... did. Just not the way I would've wanted her to."
        w "It wouldn't leave me alone, so I decided to tell her once I was ready to move out."
        w "...so she wouldn't have to look me in the eyes every day knowing how pathetic and disgusting I really was."
        hide sback with dissolve
        stop music fadeout 6
        show w regret with dissolve
        m angry "You're not like that."
        show w talk with dissolve
        w "How can you say it with such confidence?"
        play music "ost/hospital.ogg" fadein 6
        show w regretsmile with dissolve
        w "You sound almost like you mean it..."
        show w regret with dissolve
        "Except I do."
        "But I suppose I should hear him out before I draw any conclusions."
        show w neutral with dissolve
        stop music fadeout 5
        m fabtalk "So you didn't get to tell her the truth?"
        show w talk with dissolve
        w "That's right."
        show sback 4 with dissolve
        play music "ost/memory.ogg" fadein 6
        w "My... my uncle thought that... I really thought about both Ann and Marie like that."
        w "I think he must have asked them about me a lot... I guess he was a bit overprotective."
        w "Either way, once he drew that conclusion, he was sure I was a threat to them in some way and that he shouldn't let us be friends anymore."
        w "He forbid me to spend time with either of them on my own. The only chance I had to see them was when he was around, as well."
        show sback 5 with dissolve
        w "He knew everything."
        w "Everything I did, everything I said... And he never hesitated to take advantage of it."
        m serious "So you never felt comfortable at home?"
        w "Not really. At home, school, it didn't matter - he knew."
        w "I was 15 when he found out. The next three years were... I..."
        w "I felt like he was watching me the whole time."
        w "Everywhere I went, he was there, judging every single thing."
        w "Eventually, I started seeing him in places he had no right to be."
        w "...even if... he wasn't actually there."
        w "But it felt too real... I-I knew it wasn't, but..."
        w "Needless to say, I was paranoid. That was the time when I started becoming oddly aware of the things I couldn't see."
        w "I felt like... even if I couldn't see him, he was still somewhere, behind me, hiding, waiting for me to believe I'm alone and do something stupid so he could punish me for it."
        show w regrettalk with dissolve
        stop music fadeout 3
        hide sback with dissolve
        w "...I know how ridiculous that must sound."
        show w regret with dissolve
        m shock "No no, I wasn't thinking that at all."
        play music "ost/neutral.ogg" fadein 10
        "He smiles weakly."
        show w regretsmile with dissolve
        w "No matter what you think, you won't understand it unless you've been through something like that yourself."
        show w regrettalk with dissolve
        w "Which you probably weren't."
        show w tense with dissolve
        m serious "I'm sure some people here can relate to that, though."
        show w frusttalk with dissolve
        w "Yeah, maybe..."
        show w sidetalk with dissolve
        w "Still, that's not really something to bond over."
        show w talk with dissolve
        w "I'd rather stay as far away as possible from people like me."
        show w neutral with dissolve
        m regret "I see."
        m serious "Do you still see things like that?"
        show w regretsmile with dissolve
        w "Heh, I wish..."
        show w talk with dissolve
        w "I see a lot more than him."
        show w sidetalk with dissolve
        w "In fact, I barely even think about him or my cousins these days. You could say I've moved on."
        show w siden with dissolve
        m gasp "So what do you see nowadays?"
        show w frusttalk with dissolve
        w "Um... it's hard to describe..."
        show w frust with dissolve
        w "It's not... anything in particular."
        show w tense with dissolve
        w "But I don't just see things. I hear people. Voices. Somewhere around me, but always out of sight."
        show w tensetalk with dissolve
        w "I... I sometimes... feel things as well."
        show w regrettalk with dissolve
        w "No matter what I do, they don't go away."
        show w pain with dissolve
        m neu "Does that happen often?"
        show w paintalk with dissolve
        w "Almost... every day."
        show w tensetalk with dissolve
        w "Sometimes it's too much and causes me another attack. But they're not always connected."
        show w talk with dissolve
        w "...Most of the time, I can contain myself, though."
        show w frust with dissolve
        m regret "I'm... so sorry..."
        show w angry with dissolve
        w "Your pity won't do me any good."
        show w sidetalk with dissolve
        w "Though I suppose I need to rely on you with this more than anyone."
        show w regrettalk with dissolve
        w "My psychiatrist's been doing his best for the past two years, but even medicine stopped helping after a while."
        show w frusttalk with dissolve
        w "I think I've, uh... gained resistance to that over time."
        show w tense with dissolve
        m pity "I'll do my best, I promise."
        show w frust with dissolve
        stop music fadeout 4
        w "...."
        m fabtalk "So your uncle told Marie about how he thought you felt about her?"
        show sback 3 with dissolve
        play music "ost/memory.ogg" fadein 6
        w "He did. In the most indelicate manner possible."
        m "What was her reaction?"
        w "At first, she was shocked, she begged me to deny it... but I couldn't."
        show sback 4 with dissolve
        w "It was the truth. Somewhere at the back of my mind there was a dark place I had no control over. It's always been there."
        w "But those thoughts were still mine. So I couldn't deny it when she asked me to."
        m talk "Where do you think this dark place came from?"
        w "My guess would be... my parents' death?"
        w "I really don't know, but it's the only way this can make sense."
        w "There's something about an event you had no way to prevent killing the only two people who ever cared about you that makes you start to question if you really have control over anything at all."
        stop music fadeout 5
        w "So... I think that's why it was created."
        "That's... surprisingly in-depth."
        hide sback with dissolve
        m regrettalk "Did your relatives know about that part of you?"
        play music "ost/hospital.ogg" fadein 6
        show w regrettalk with dissolve
        w "...no."
        show w talk with dissolve
        w "I haven't told anyone about it until I got here."
        show w tense with dissolve
        m serious "So they had no option other than to blame you, right?"
        show w frusttalk with dissolve
        w "Even if they knew, it would be only right to blame me. I'm still responsible for whatever's created there, whether I chose to create it or not."
        stop music fadeout 4
        show w angrytalk with dissolve
        w "I'm the only one at fault here, [name]. Don't decieve yourself."
        show sback 6 with dissolve
        play music "ost/memory.ogg" fadein 8
        m talk "So Marie stopped trusting you after that?"
        w "I... never got to ask her directly, but I assume she did."
        w "I feel like even if my uncle allowed me to keep spending time with them, she wouldn't want to."
        w "She looked like she was... afraid of me whenever I talked to her."
        w "It... it hurt, but I understood why she felt that way."
        m fabtalk "What about Ann?"
        w "She was way too young and innocent to understand what happened. She was just 12 when my uncle told Marie about me."
        w "But she didn't have to know. Marie protected her from me, just like she'd protected me from my uncle."
        w "She really thought I could hurt them... and I couldn't help but believe her. I never stopped trusting her, after all."
        m shock "But... you never actually wanted to hurt them, right?"
        w "I... I don't know anymore..."
        w "I wish I could just say I didn't, but it's not that simple."
        m talk "When did you move out?"
        scene black with Dissolve(0.8)
        w "I was basically kicked out when I turned 18. I was on my own since then."
        m fabtalk "I see. It must've been rough."
        w "Actually, I was kind of glad I got out of that house. It was... difficult, these last three years."
        "I nod."
        m gasp "And you've never seen your relatives again after that?"
        w "Never."
        stop music fadeout 5
        w "I don't think they'd want to see me, either way..."
        scene bg mcdesk with dissolve
        show w regret with dissolve
        m pity "It's been 8 years. People change."
        play music "ost/neutral.ogg" fadein 8
        show w tensetalk with dissolve
        w "I can't know that for sure, so I'd rather not risk it."
        show w regret with dissolve
        m fabtalk "Risk what exactly?"
        show w tense with dissolve
        w "Going back to that house... I feel like... it might be too much for me."
        show w frust with dissolve
        m talk "If that's how you feel, I understand."
        show w sidetalk with dissolve
        w "It may not seem like it, but for the majority of the time before I got here, I was making some progress."
        show w regrettalk with dissolve
        w "And... I fear that it would all return to how it was before if I saw them again."
        show w frusttalk with dissolve
        w "I'm... far from being stable enough to be able to confront any of that."
        show w tense with dissolve
        m conf "I get it."
        show w siden with dissolve
        m fabtalk "We're running out of time for today, so if that's all you had to say, you can go."
        stop music fadeout 3
        show w tense with dissolve
        "He glances at me."
        show w tensetalk with dissolve
        w "[name]...?"
        show w frust with dissolve
        m neu "Yes?"
        play music "ost/hospital.ogg" fadein 6
        show w talk with dissolve
        w "Do you actually still believe I'm a good person? Even after everything I said?"
        show w tense with dissolve
        menu:
            "I'll always believe that":
                $personal+=1
                $SilverHeart+=1
                show w regretsmile with dissolve
                w "I... can't understand, but... all I can do is accept it."
                show w smile with dissolve
                w "Thank you for believing in me so much."
                show drk with Dissolve(0.75)
                show s 1 with dissolve
                show s 2 with Dissolve(1.0) 
                $renpy.pause(0.75, hard = True)
                hide s with dissolve
                hide drk with dissolve
            "So far I do":
                $personal+=1
                show w sidetalk with dissolve
                w "I see."
            "It doesn't matter":
                $professional+=2
                show w neutral with dissolve
                m "As your psychologist, it's my duty to help, no matter what I think of you."
                show w siden with dissolve
                m "I don't think it would be very professional to share these kind of opinions with you."
                show w sidetalk with dissolve
                w "I see."
        show w frust with dissolve
        w "...."
        show w talk with dissolve
        w "Regardless of what you think right now, tomorrow I should tell you about what happened two years ago."
        show w regrettalk with dissolve
        w "You'll probably change your mind about me after that."
        show w tense with dissolve
        m "I'll judge everything I hear tomorrow carefully, then. I plan to be as unbiased as possible."
        show w sidetalk with dissolve
        w "...goodbye, Dr. Hart."
        stop music fadeout 5
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        hide screen easymeter
        hide screen silvermeter
        "He leaves."
        jump breakchoice
    elif day == 10:
        scene bg mc with dissolve
        play music "ost/neutral.ogg" fadein 8
        "I'm about to see William again today."
        "Yesterday, he told me he would talk about what happened two years ago the next time we'd meet."
        "Is he really going to tell me everything so soon..?"
        "He seemed very reluctant to do so last week..."
        "I hope it's not too much trouble for him."
        "But I guess if he agreed, he knows that he can handle it."
        scene bg mcdesk with dissolve
        show w talk with dissolve
        w "Good morning, Dr. Hart."
        if easymeter:
            show screen easymeter
            show screen silvermeter
        show w frust with dissolve
        "His voice sounds more quiet than usual. The tension of what is about to happen seems to be hanging in the air."
        m flirt "Hello, William. There's no reason to be anxious right now. Please, take a seat."
        show w neutral with dissolve
        "He reluctantly complies, though it's clear to me he would rather be anywhere else right now."
        show w frusttalk with dissolve
        stop music fadeout 4
        w "So..."
        show w regrettalk with dissolve
        w "...I should just start talking, shouldn't I?"
        ##Translation idea: William używa dużo question tagów. Po polsku zastąpiłabym je po prostu ",tak?" xddd
        show w tense with dissolve
        m fabtalk "If that's possible."
        play music "ost/memory.ogg" fadein 6
        scene black with dissolve
        w "Once my uncle kicked me out of his house, it didn't take me long to get used to living on my own."
        w "Theoretically, everything was going well except for..."
        scene sback 7 with dissolve
        w "...my illness. It just kept getting worse over time, even though I was never exposed to that much stress or anything that would affect me this way."
        w "It just... developed on its own."
        w "That's when I started having attacks. At first, they only happened about once per month."
        w "The things I would see got a lot more... intense, as well."
        w "My dreams were so horrible at that time that I couldn't bring myself to sleep."
        w "Eventually, I couldn't last an hour without getting anxious in some manner."
        stop music fadeout 5
        w "And I guess... that's roughly how these six years passed."
        scene bg mcdesk with dissolve
        show w neutral with dissolve
        m angry "Did it get better after you got here?"
        play music "ost/neutral.ogg" fadein 6
        show w talk with dissolve
        w "Not really." 
        show w regretsmile with dissolve
        w "Still, knowing the staff is supposed to make sure nothing bad happens is... a little calming, at least."
        show w calm with dissolve
        m smile "I'm glad to help."
        show w frust with dissolve
        w "...."
        show w regrettalk with dissolve
        w "I...I suppose you help a little, as well..." 
        show w tense with dissolve
        m fabtalk "I should probably get to the point." 
        show w fear with dissolve
        "I lean in a bit to look him straight in the eye." 
        show w tense with dissolve
        m talk "What did you do two years ago?" 
        show w frust with dissolve
        stop music fadeout 3
        w "...." 
        show w regrettalk with dissolve
        w "...right. I'll talk, let me just... think about where to start..." 
        show w tense with dissolve
        m conf "Sure. Take your time." 
        show w frusttalk with dissolve
        play music "ost/memory.ogg" fadein 8
        w "Y-You see, I... didn't have many friends after I stopped living with my family." 
        show w regretsmile with dissolve
        w "I stopped caring about people, to an extent." 
        show w regret with dissolve
        w "You could say I had too many problems on my own to deal with others'."
        scene sback 8 with dissolve
        w "But, uh... there were a few people who seemed very set on befriending me."
        w "I didn't want to say no, so we started hanging out occassionally."
        w "I won't name names - I'd prefer them to remain annonymous."
        m talk "No problem."
        w "Most of the time, it was... bearable. I was really careful to never let them see me anxious."
        w "That meant I grew a habit of avoiding them in stressful situations, which made them think I didn't really care about them."
        m gasp "Why didn't you tell them the truth?"
        w "W-What? The truth..?"
        m fabtalk "What were you afraid of? That they wouldn't understand?"
        stop music fadeout 5
        w "I... I always just assumed I shouldn't tell them. I don't think I need to justify that."
        scene mcdesk with dissolve
        show w neutral with dissolve
        m angry "...." 
        play music "ost/tension.ogg" fadein 6
        show w talk with dissolve
        w "[name]. Tell me something." 
        show w tensetalk with dissolve
        w "If you were like me, would you ever tell anyone?" 
        show w sadtalk with dissolve
        w "Tell them that you're afraid of god knows what, so afraid that you can't last a night on your own without having an attack, that you see things that aren't there, things they wouldn't even be able to imagine, that you live in fear and don't even know of what?"
        show w pain with dissolve
        menu:
            "I would tell them the truth": 
                show w frusttalk with dissolve
                w "Hmph. Obviously, you don't understand..." 
                show w tensetalk with dissolve
                w "And you dare mock me for not wanting to tell anyone..?" 
                show w pain with dissolve
                m regret "I'm not mocking you."
            "I wouldn't tell anyone as well": 
                show w regretsmile with dissolve
                w "...thank you. At least you understand that."
            "I would pick friends who could understand": 
                show w regret with dissolve
                w "...." 
                show w tensetalk with dissolve
                w "...nobody could." 
                show w frusttalk with dissolve
                w "I wouldn't trust anyone with that kind of knowledge."
        stop music fadeout 4
        show w frusttalk with dissolve
        w "Either way, things were going alright most of the time."
        show sback 8 with dissolve
        play music "ost/memory.ogg" fadein 8
        w "My best friend and his friend from high school got together since the three of us ended up hanging out so much."
        m fabtalk "Were you happy for them?"
        w "Why wouldn't I be?"
        w "...are you implying I was jealous of them?"
        m gasp "Were you..?"
        w "No, of course not! I would never imagine myself in a relationship with someone."
        m talk "Why is that?"
        w "I... I would have to tell them the truth then..."
        m fabtalk "I see."
        w "Besides, there was nobody I cared for that much. It would be a waste of my time and effort. And anxiety."
        "...."
        m "Are your friends connected to what happened two years ago?"
        w "...yes. Y-yes they are."
        show drk with dissolve
        w "It was New Year's Eve. It was just the three of us at my friend's house."
        w "It was already kind of late..."
        w "His girlfriend seemed nervous about something the whole time. I asked her what's wrong, and she..."
        w "She told us that she's met someone new and they need to break up."
        show sback 91 with dissolve
        hide drk with dissolve
        w "He, um... didn't take it too well. He started yelling at her."
        w "Called her a slut."
        w "She started crying."
        w "At first, I thought I shouldn't intervene, but she was my friend as well and he was getting way too aggressive."
        show sback 92 with dissolve
        w "So I stepped in and told him to leave her alone."
        w "He seemed surprised that I reacted that way and asked me why the hell am I suddenly on her side."
        w "I told him that that was enough and he should stop accusing her."
        w "He... he got really angry."
        show sback 93 with dissolve
        w "We both ended up yelling at each other over her."
        w "And I normally pretty much never raise my voice. I never liked fighting people."
        w "It, um... escalated."
        w "I... I suppose it's not very surprising, but he was a lot stronger than me."
        w "I didn't notice when we moved into another room. It was a narrow hallway leading up to stairs that led to the floor below us."
        w "I... I shouldn't prolonged my excuses anymore."
        w "He fell down. I was the one who pushed him."
        show sback 10 with dissolve
        w "I watched him fall down the stairs and break his neck."
        w "I didn't do anything to help him. I just froze. I couldn't move an inch."
        w "I couldn't believe he was really dead... that I'd just killed him."
        w "The girl fainted. I was alone."
        w "...I panicked, I didn't know what to do..."
        w "I... I... I just killed someone. My own friend."
        w "What kind of a monster does that..?"
        m "It was an accident, wasn't it, though?"
        w "I don't... know..."
        stop music fadeout 5
        w "I wish it was."
        hide sback with dissolve 
        show w tensetalk with dissolve
        w "I'm a murderer, [name]." 
        show w frusttalk with dissolve
        w "And there's nothing you can do to fix that." 
        play music "ost/tension.ogg" fadein 6
        show w pain with dissolve
        "I'm speechless. I need a moment to recollect myself." 
        show w tensetalk with dissolve
        w "S-See? It didn't take long to convince you. You won't ever want to help me again... nobody would."
        show w fear with dissolve
        "His breath becomes uneven. It's like I can hear the anxiety in his voice."
        "He's looking in my direction, but not at me."
        show w shock with dissolve
        w "I... I killed him, [name]... I really killed him..." 
        show w paintalk with dissolve
        w "I don't deserve your pity-" 
        show w dread with dissolve
        "His voice breaks. He looks like he's about to either faint or die of a heart attack."
        "I need to do something."
        menu:
            "I'm not giving up on you.": 
                show w pain with dissolve
                w "...." 
                show w dis with dissolve
                w "{i}She's lying..." 
                stop music fadeout 6
                show w dread with dissolve
                m sadtalk "William. I never lied to you." 
                show w paintalk with dissolve
                w "No, that's not possible..."
                show w pain with dissolve
            "Even you deserve my help": 
                show w paintalk with dissolve
                w "No..." 
                stop music fadeout 5
                show w dis with dissolve
                w "You can't..." 
                show w fear with dissolve
                w "I won't let you..."
            "I don't care about what you did": 
                show w wrong with dissolve
                w "W-What?" 
                show w crit with dissolve
                "He looks straight at me this time." 
                stop music fadeout 5
                m angry "That's right. I'll save you no matter what." 
                show w dis with dissolve
                w "You... you can't..."
                show w dread with dissolve
        "It's just getting worse the more he denies my help." 
        play music "ost/emo.ogg" fadein 8
        show w dis with dissolve
        w "I... I'm going to die here." 
        show w broketalk with dissolve
        w "You should just kill me, [name]. You'll save us both pain."
        show w broke with dissolve
        m sjw "No! I can't allow that."
        show w scream with dissolve
        w "Why...? Why do you make me suffer like this..?"
        show w cry with dissolve
        menu:
            "Because I care about you":
                $SilverHeart+=1
                $personal+=2
                show w dis with dissolve
                w "E... W-What did you say..?"
                show drk with Dissolve(0.75)
                show s 1 with dissolve
                show s 2 with Dissolve(1.0) 
                $renpy.pause(0.75, hard = True)
                hide s with dissolve
                hide drk with dissolve
                show w crit with dissolve
                m uncom "I care about you. I don't want you to remain here and suffer."
                show w broketalk with dissolve
                w "You... you can't say that... don't..."
                show w scream with dissolve
                w "Just leave me alone!"
            "Because I can't hurt you":
                show w broketalk with dissolve
                w "Being here with you is painful enough on its own..."
                show w broke with dissolve
                m regrettalk "I'm sorry."
                show w dis with dissolve
                w "Wait, don't be... you... you've done nothing wrong."
                show w broketalk with dissolve
                w "I'm the only one who can be blamed right now..."
                show w cry with dissolve
                w "...."
                show w scream with dissolve
                w "I can't do this anymore, [name]..."
            "Because it's necessary":
                $professional+=1
                show w broketalk with dissolve
                w "Y-You're right..."
                show w scream with dissolve
                w "...I was always supposed to suffer."
        show w dread with dissolve
        "I feel like I need to comfort him somehow."
        menu:
            "Hug him":
                $personal+=3
                "I get up and wrap my arms around him. He's trembling."
                show w dis with dissolve
                w "?!"
                if SilverHeart>15: 
                    show w broketalk with dissolve 
                    w "[name]..."
                show w crit with dissolve
                w "N-No."
                scene bg mc with vpunch
                w "{i}{cps=*3}GET AWAY FROM ME!"
                "He pushed me away. Ouch. I didn't expect him to have that kind of strength."
                w "...."
                "He's staring at me, his eyes wide."
                w "Are... you... okay?"
                "I get up."
                scene bg mcdesk with dissolve
                show w fear with dissolve
                m fabtalk "It's fine."
                show w wrong with dissolve
                w "No, it's not. Don't ever approach me like that again. I- I could've hurt you."
                show w frust with dissolve
                m regrettalk "I'm sorry. I wanted to help."
                show w broke with dissolve
                w "...."
                show w sadtalk with dissolve
                w "Just ask what you have to ask and let me out of here."
                show w regret with dissolve
                m regret "...."
            "Reach out to him":
                $SilverHeart+=3
                m angry "William. I don't want you to be in pain any longer."
                show w broke with dissolve
                "I hold out both my hands to him over my desk."
                stop music fadeout 5
                m serious "Please... you just have to let me help."
                show w tense with dissolve
                "He glances at me, unsure of what to do. I smile patiently. We have time."
                play music "ost/ship.ogg" fadein 6
                show w regret with dissolve
                "Hesitantly, he places his hands in mine."
                "They're shaking, but that's okay."
                "I move my fingers slowly on his skin."
                show w pain with dissolve
                w "...."
                show w paintalk with dissolve
                w "[name]... You shouldn't be so kind to me."
                show drk with Dissolve(0.75)
                show s 1 with dissolve
                show s 2 with Dissolve(1.0) 
                $renpy.pause(0.75, hard = True)
                hide s with dissolve
                hide drk with dissolve
                show w broke with dissolve
                m pity "Why?"
                "I lower my voice not to make him any more anxious."
                show w sadtalk with dissolve
                w "I don't... deserve your help."
                show w sad with dissolve
                m conf "Of course you do. Everybody does."
                show w broketalk with dissolve
                w "I killed someone, [name]. I should be dead by now."
                show w cry with dissolve
                m serious "Don't say that. You won't do anyone any good by dying."
                show w paintalk with dissolve
                w "...I would argue."
                show w pain with dissolve
                m conf "I need you to calm down first."
                show w sidetalk with dissolve
                w "I {i}am{/i} calm."
                show w neutral with dissolve
                m gasp "Are you?"
                "He nods."
                m fabtalk "Then..."
                show w regret with dissolve
                "I let go of his hands, trying not to invade his personal space any more than needed."
            "You need to calm down":
                $professional +=2
                show w broke with dissolve
                w "...right."
                show w frusttalk with dissolve
                w "I won't inconvienience you any longer."
                show w calm with dissolve
                "...."
                show w neutral with dissolve
                w "I'm calm now. What do you want from me?"
        stop music fadeout 4
        m talk "What happened after your friend's death?"  
        w "I... wasn't thinking straight."
        show sback 10 with dissolve
        play music "ost/memory.ogg" fadein 8
        w "I asked myself: \"now that I'm a murderer, what would a murderer do?\"."
        w "I hid the corpse in the basement and locked it so nobody would find it there."
        w "I barely had the time to get rid of all the blood before  his girlfriend woke up."
        w "Something was telling me to run, and I didn't question it."
        w "Once she woke up, there was no trace of the corpse - or of me."
        show sback 11 with dissolve
        w "I hid the entire next week. Barely ate or slept."
        w "My illness had never affected me more than it did over that one week."
        w "I was... alone with these... voices."
        m uncom "What were they telling you?"
        w "That I..."
        w "I... I wanted to kill him the whole time. That I was a horrible person from the start and that I should die."
        w "I really... wanted to..."
        w "But I didn't have the courage to really kill myself."
        w "The thought of hurting myself terrified me."
        w "I... I'm pathetic, aren't I?"
        m angrytalk "You're not. You should be glad you didn't have the courage to do it."
        w "Why? What good did it do to anyone?"
        m conf "You're alive. That's what matters."
        w "...."
        w "Either way, after that one week I decided I'm being a coward for hiding and decided to confess everything to the police."
        w "It turned out they somehow couldn't find the corpse for the whole week... I saw a couple of missing person posters hanging around the city."
        w "It felt... horrible, looking at them and knowing that I'm responsible."
        w "I told them everything that happened and begged them to arrest me for it."
        w "They managed to confirm all I said, but didn't want to consider it murder."
        w "It felt like they were mocking me..."
        w "It wasn't easy to go there and tell them the truth, and yet they weren't even taking me seriously."
        w "Well, eventually they sent me here."
        w "And that's... how I ended up where I am now, I guess."
        w "Still, even if they didn't consider me guilty..."
        w "They had no idea what goes on inside my head. Didn't know how guilty I really was of everything."
        m serious "Do you really believe that you wanted to kill him?"
        stop music fadeout 5
        w "I... a part of me wanted to. But... if it's a part of me, then... {i}I{/i} wanted to kill him as well."
        "There's so much wrong with that logic... but I don't think I have the time to address everything today."
        play music "ost/neutral.ogg" fadein 6
        show w siden with dissolve
        hide sback with dissolve
        "I check the time. My break just started."
        m talk "We can continue this tomorrow. Thank you for telling me the truth."
        show w talk with dissolve
        w "You... you're welcome. I should go."
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        hide screen easymeter
        hide screen silvermeter
        "He leaves in a hurry."
        "...."
        stop music fadeout 4
        "Can I really consider him a murderer after everything he's told me...?"
        jump breakchoice
    elif day == 11:
        scene bg offices with dissolve
        play music "ost/neutral.ogg" fadein 6
        show w full with dissolve
        m gasp "Oh, you're early today?"
        w "Actually, you're late."
        m fabtalk "...sorry about that."
        "I struggle to find the keys to my office in my bag and unlock the door."
        m talk "Come in."
        if easymeter:
            show screen easymeter
            show screen silvermeter
        scene bg mcdesk with dissolve
        m fabtalk "So..."
        m serious "Last time you told me about... your friend's death."
        stop music fadeout 4
        show w regret with dissolve
        "He looks away from me. I can tell it's difficult for him to talk about it."
        m neu "Hey, I still want to help you. I'm not giving up that easily."
        play music "ost/hospital.ogg" fadein 10
        show w tensetalk with dissolve
        w "...you should."
        show w sidetalk with dissolve
        w "But, if you insist... I think you're missing some information."
        show w siden with dissolve
        m fabtalk "Meaning..?"
        show w talk with dissolve
        w "Ask away."
        show w frust with dissolve
        "I guess I should start where we left off last time."
        show w tense with dissolve
        m talk "What happened after you got here? How did you feel about this place at first?"
        show w talk with dissolve
        w "I was... surprised."
        show w frusttalk with dissolve
        w "I expected it to be a lot worse, to be honest."
        show w frust with dissolve
        m conf "I think a lot of people felt that way at first."
        show w sidetalk with dissolve
        w "I didn't really intend to end up here, but it was still a lot better for me than freedom."
        show w siden with dissolve
        m fabtalk "I see. So you were telling the truth last week when you said it was your choice to be here."
        show w frusttalk with dissolve
        w "I... I meant that if I hadn't gone to the police two years ago, I wouldn't have ended up here."
        show w talk with dissolve
        w "So in a way, it's the truth."
        show w frusttalk with dissolve
        w "I still want to remain here, and that's my choice only."
        show w frust with dissolve
        m talk "You have a room on your own, right?"
        stop music fadeout 5
        show w neutral with dissolve
        "He nods."
        show w talk with dissolve
        w "Always had. Thankfully."
        show w neutral with dissolve
        m fabtalk "XIX, if I remember well?"
        play music "ost/neutral.ogg" fadein 6
        show w frusttalk with dissolve
        w "That's right."
        show w frust with dissolve
        m talk "How many psychologists have you had so far?"
        show w talk with dissolve
        w "Up to... six? I'm not sure."
        show w frusttalk with dissolve
        w "Most of them were quite... unmemorable, though."
        show w siden with dissolve
        m "I see."
        if moonsharpeknow:
            m fabtalk "Your psychiatrist is Dr. Sharpe, right?"
            show w talk with dissolve
            w "That's right. I was never reassigned."
            show w neutral with dissolve
            m talk "How do you feel about working with him?"
        else:
            m fabtalk "What about psychiatrists?"
            show w talk with dissolve
            w "It's been consistent. I'm assigned to Dr. Sharpe."
            show w neutral with dissolve
            "Oh."
            show w sidetalk with dissolve
            w "What's that look supposed to mean? He's your boss, isn't he?"
            show w neutral with dissolve
            "I nod."
        show w frusttalk with dissolve
        w "I mean... he's fine. He's very, um... professional."
        show w frust with dissolve
        "I bet."
        show w talk with dissolve
        w "I think he gets things done more efficiently than the others. It's just faster."
        show w neutral with dissolve
        m gasp "What do you mean?"
        show w frustsmile with dissolve
        w "He's made it quite clear from the start that it's not his job to have long talks with me - that's what you're here for."
        show w sidetalk with dissolve
        w "From my experience, the only time you can have a longer conversation with him is when there's something wrong with the medicine you're taking."
        show w talk with dissolve
        w "But it works out for me. It's not like I'm dying for some company and would like to sit there for three hours straight."
        show w neutral with dissolve
        stop music fadeout 4
        if moonsharpeknow:
            m conf "The important thing is that you two get along."
            play music "ost/tension.ogg" fadein 5
            show w shock with dissolve
            w "What do you mean..?"
            show w fear with dissolve
            "Did I... say something wrong?"
            m talk "I spoke to him about you yesterday. He was very helpful."
            show w tensetalk with dissolve
            w "You... did?"
            show w tense with dissolve
            stop music fadeout 5
            m fabtalk "Based on what he said, I would assume you feel quite comfortable around him. It's a good thing, isn't it?"
            show w paintalk with dissolve
            w "I... I suppose."
        else:    
            m talk "Alright then. I would expect him to be like that, actually."
        m fabtalk "Did it take you a long time to get accustomed to living here?"
        play music "ost/memory.ogg" fadein 8
        show w regrettalk with dissolve
        w "At first, I thought it would be best to kind of... distance myself from everything."
        show w frusttalk with dissolve
        w "I knew I would be here for a long time, and I definitely didn't plan to enjoy it, so I wanted to make it as monotone as possible."
        show w tensetalk with dissolve
        w "But, um... with all these new situations and people, I couldn't really... stay perfectly calm here, if that makes sense."
        show w frust with dissolve
        w "...."
        show w talk with dissolve
        w "It was my third day here. I was on my way to my psychologist's office. I think I was there early."
        show w tensetalk with dissolve 
        w "And, in that hallway connecting the offices, I saw... um..."
        show w sidetalk with dissolve
        w "Do you happen to know the one from room XV? He's always tied up, I heard he's been here for a while..."
        show w tense with dissolve
        stop music fadeout 4
        m gasp "You mean Michael? He's one of my patients."
        show w fear with dissolve
        "His eyes go wide."
        play music "ost/tension.ogg" fadein 5
        show w gasp with dissolve
        w "Holy fuck, you have him as well?!"
        show w fear with dissolve
        m neu "I do."
        show w frust with dissolve
        w "Umm..."
        show w tensetalk with dissolve
        w "Is he, like... aggressive?"
        show w tense with dissolve
        m uncom "As far as I know, he's only attacked the staff once, but that was before he was, uh... restrained."
        show w neutral with dissolve
        m serious "But he's never really acted violently towards me."
        show w frusttalk with dissolve
        stop music fadeout 4
        w "I see..."
        show w frust with dissolve
        m talk "He's been here for three years, by the way."
        show w regrettalk with dissolve
        play music "ost/neutral.ogg" fadein 6
        w "I... feel kind of bad about asking like this, but the guy has... a bit of a reputation here."
        show w tense with dissolve
        m regret "It's hard not to, in his state."
        show w shock with dissolve
        w "Wait, what illness does he actually have?"
        show w neutral with dissolve
        m talk "Obsessive-compulsive disorder. It's an anxiety disorder, just like yours."
        show w yuri with dissolve
        w "I don't see many similarities, to be honest."
        show w frust with dissolve
        m fabtalk "His case isn't the most typical, I guess."
        show w tense with dissolve
        m conf "Besides, you'd have to know him better to notice these things."
        show w regrettalk with dissolve
        stop music fadeout 5
        w "...yeah."
        show w talk with dissolve
        w "Well, the first time I saw him, I... pretty much froze."
        show w tensetalk with dissolve
        play music "ost/memory.ogg" fadein 6
        w "That was probably one of the first times I thought to myself: \"Should I {i}really{/i} be here..?\"."
        show w frusttalk with dissolve
        w "Seriously, that's just... uncomfortable to look at."
        show w frust with dissolve
        m pity "It can be a bit intimidating at first."
        show w neutral with dissolve
        m sadsmile "I'm speaking from experience here."
        show w tensetalk with dissolve
        w "He, um... started talking to me. And I kind of wanted to run away."
        show w frusttalk with dissolve
        w "So... that was probably one of the worse experiences I've had here."
        show w regrettalk with dissolve
        w "Disregarding the attacks and such, I mean."
        show w frusttalk with dissolve
        w "It took me a while to get used to some of the other patients."
        show w tensetalk with dissolve
        w "Not to sound offensive towards anyone, but I was already used to living with what I had on my own, and seeing other people with all sorts of problems,"
        show w regrettalk with dissolve
        w "...Most of which seemed way more serious than mine felt a bit... overwhelming."
        show w tense with dissolve
        stop music fadeout 5
        m conf "I get it."
        m fabtalk "How did your illness react to living here? Did it get better?"
        show w regrettalk with dissolve
        play music "ost/hospital.ogg" fadein 6
        w "Right after I got here, I was still... in the state I was right after I... I..."
        show w tense with dissolve
        m angry "I know."
        show w frust with dissolve
        m serious "Did you still have these suicidal thoughts here?"
        show w sidetalk with dissolve
        w "I mean... I've... had them for the past 10 years quite consistently, but..."
        show w tensetalk with dissolve
        stop music fadeout 5
        w "Yes. They were... much more intense than usual."
        show w frusttalk with dissolve
        w "I... I had a lot of dreams at that time where... I was actually in prison."
        show w regrettalk with dissolve
        w "And, um... they were going to kill me... For what I've done."
        play music "ost/tension.ogg" fadein 10
        show w paintalk with dissolve
        w "I thought that... if it's going to be like this, it would be better if I just ended it."
        show w frusttalk with dissolve
        w "But... obviously, that's impossible here."
        show w regrettalk with dissolve
        w "So I just waited."
        show w regret with dissolve
        w "...waited for someone to come end it."
        show w tensetalk with dissolve
        w "But nobody came."
        show w paintalk with dissolve
        w "So I had to suffer for two years with no hope of it ever ending."
        show w regrettalk with dissolve
        w "It's torture, [name]. I hate this."
        show w frust with dissolve
        w "But... I know it has to the that way."
        stop music fadeout 4
        m serious "Why? Why do you have to suffer?"
        show w paintalk with dissolve
        w "B-Because..."
        show w dis with dissolve
        play music "ost/fight.ogg" fadein 15
        w "{i}{cps=*3}I wanted to kill him!{/i} {cps=*1}I-I would do it again if I were given the chance to."
        show w dread with dissolve
        m uncom "But you said it was an accident..."
        show w regrettalk with dissolve
        w "I thought it was."
        show w neutral with dissolve
        "He leans in, getting closer to me. I... wouldn't have expected that of him."
        show w frusttalk with dissolve
        w "[name], the truth is, I... that part of me I mentioned earlier..."
        show w regrettalk with dissolve
        w "It just kept telling me that... I was a murderer. That if I could, I would've killed him even if we hadn't fought."
        show w paintalk with dissolve
        w "That I would've killed everyone."
        show w dis with dissolve
        w "...who am I supposed to believe?"
        show w pain with dissolve
        w "I don't know anymore..."
        show w regrettalk with dissolve
        w "But what I did after his death..."
        show w frusttalk with dissolve
        w "That wasn't what any normal person would have done."
        show w dis with dissolve
        w "Anyone else would've called for help, tried to save him somehow..."
        show w paintalk with dissolve
        w "And I? I hid."
        show w dis with dissolve
        w "If I had wanted to, I could've gotten away with it and he would be considered missing until everyone would forget about him."
        show w sadtalk with dissolve
        w "Can't you see it, [name]?"
        show w pain with dissolve
        w "I have the potential to become a monster. And the worst thing is that I would enjoy it."
        "I'm confused."
        show w tense with dissolve
        stop music fadeout 5
        m serious "But... you regret what you've done. You're not like that."
        show w paintalk with dissolve
        w "How do you know what I'm like?"
        show w tensetalk with dissolve
        play music "ost/tension.ogg" fadein 6
        w "I'm only half what you know, and other half is... all of that."
        show w regret with dissolve
        "I refuse to believe he's really a bad person."
        "It must be his illness and guilt pushing him to think like that... or something."
        "I have no idea what happened there, but I know I can't let him think that way."
        m uncom "William... you've never hurt anyone on purpose. You're not evil."
        show w pain with dissolve
        m angrytalk "And you're definitely not a murderer."
        show w dis with dissolve
        w "How can you know that for sure?"
        show w regret with dissolve
        m angry "You'd never do something like that."
        show w dread with dissolve
        m serious "Look at yourself - look at the amount of pain it cost you to cause his death, even if it was by accident."
        show w pain with dissolve
        m "You don't want this. You said you could never let it happen again."
        show w regrettalk with dissolve
        w "I..."
        show w frusttalk with dissolve
        w "...You wouldn't understand."
        show w regret with dissolve
        w "I'm... so afraid, [name]."
        show w regrettalk with dissolve
        w "I fear that... one day, I may not have a choice."
        show w sadtalk with dissolve
        w "I'm going to hurt someone else. I just... I feel it."
        show w regrettalk with dissolve
        w "...and they'll never forgive me for it."
        show w sad with dissolve
        m sadtalk "William..."
        show moon1 1 with Dissolve(1.0)
        "...."
        "I didn't notice that before, but I got way closer to him than what I'm used to."
        "He's always been bothered by me invading his personal space, but now..?"
        "He doesn't seem to have noticed it yet."
        "Either way, it would be smart to move away a bit so I don't make him uncomfortable."
        show moon1 4 with dissolve
        w "{i}!!!"
        stop music fadeout 5
        "He seems to have just noticed how close I am."
        w "{i}{cps=*3}What... are you doing?"
        m no "I'm sorry, I didn't mean to-"
        if SilverHeart>=18:
            play music "ost/ship.ogg" fadein 8
            show moon1 2 with dissolve
            w "...it's fine."
            "Is it really..? That's... uncharacteristic of him."
            w "{cps=*3}I-I mean if you want to, then..."
            "He pauses abruptly."
            show moon1 1 with dissolve 
            w "[name]? You really... aren't bothered by it?"
            w "I... said you can get away from me if you want to. {cps=*2}I'm not... pressuring you, am I..?"
            menu:
                "You're not":
                    $personal +=1
                    w "O-Oh... that's good..."
                    "I move away from him with a neutral expression."
                    hide moon1 with Dissolve(1.0)
                    show w tense with dissolve
                "Move away from him":
                    $professional+=1
                    "I move away from him before I can make him any more nervous."
                    hide moon1 with Dissolve(1.0)
                    show w tense with dissolve
                "Keep looking at him":
                    $SilverHeart+=1
                    w "I... um..."
                    show moon1 2 with dissolve
                    w "I'm not sure what you're..."
                    "He falls silent again."
                    "He's at a loss of words."
                    show drk with Dissolve(0.75)
                    show s 1 with dissolve
                    show s 2 with Dissolve(1.0) 
                    $renpy.pause(0.75, hard = True)
                    hide s with dissolve
                    hide drk with dissolve
                    menu:
                        "Touch him":
                            $personal+=2
                            $SilverHeart+=2
                            $Moonship=True
                            "I hold out my hand hesitantly."
                            m "May I..?"
                            "He's not looking at me, but there's a sense of urgency to his expression."
                            "I could be messing this up, but I trust my instinct."
                            "I lay my hand on his cheek carefully."
                            show moon1 3 with dissolve
                            w "...."
                            m "It's okay. You're safe here."
                            m "You won't hurt anyone else."
                            w "...."
                            show moon1 2 with dissolve
                            w "...thank you, [name]."
                            show drk with Dissolve(0.75)
                            show s 1 with dissolve
                            show s 2 with Dissolve(1.0) 
                            $renpy.pause(0.75, hard = True)
                            hide s with dissolve
                            hide drk with dissolve
                            w "I... didn't feel it was proper to ask you for this, but..."
                            show moon1 1 with dissolve
                            w "You knew, didn't you?"
                            w "You always know."
                            hide moon1 with dissolve
                            show w smile with dissolve
                        "Move away":
                            "That's enough. I don't want to make him uncomfortable."
                            "I retreat carefully."
                            hide moon1 with dissolve
                            show w regret with dissolve
            stop music fadeout 5
            w "...."
            show w regrettalk with dissolve
            w "I should... be going now. Thank you for listening to me, Dr. Hart."
            hide screen easymeter
            hide screen silvermeter
            play sound "doorclose.ogg" fadein 1
            scene bg mc with dissolve
            "He leaves quickly. I'm not sure what just happened."
        else:
            play music "ost/tension.ogg" fadein 5
            w "{i}{cps=*3}G-Get away from me!"
            "I retreat as quickly as I can."
            hide moon1 with dissolve
            show w frust with dissolve
            "Oh god... I think I just made it awkward..."
            "...this is the moment when I would probably swear if I could."
            "Well... judging by his reaction, I don't think he wants to talk to me anymore."
            "Let's not make this any worse."
            show w tense with dissolve
            m uncom "You... You may go. I'll see you tomorrow."
            play sound "doorclose.ogg" fadein 1
            scene bg mc with dissolve
            hide screen easymeter
            hide screen silvermeter
            "He leaves without a word."
            "I messed up a bit, but... I guess tomorrow is another day."
        jump breakchoice
    elif day == 12:
        if Moonship:
            scene black with dissolve
            "What... was that dream..?"
            if sanity<50:
                "I feel... dizzy today... My head hurts."
                "Something about that dream unsettled me."
            else:
                "...."
                "It doesn't matter. It was just a nightmare."
            play music "footsteps.ogg" fadein 6
            scene bg patients with dissolve
            "I'm making my way through the patients' rooms hallway."
            show bg patientsnight
            $renpy.pause()
            show bg patients with dissolve
            "What...?"
            "No, I'm not dreaming. I must be tired."
            scene bg offices with dissolve
            "I reach my office at last. Let's get to work."
        if easymeter:
            show screen easymeter
            show screen silvermeter
        scene bg mcdesk with dissolve
        play music "ost/neutral.ogg" fadein 10
        m smile "Good morning, William."
        show w frust with dissolve
        w "...."
        "He doesn't seem to be in the mood to talk today."
        m serious "Is something wrong?"
        show w frusttalk with dissolve
        w "...it's nothing."
        show w tense with dissolve
        m talk "Alright then..."
        m fabtalk "Is there anything you'd want to talk about..?"
        if Moonship:
            stop music fadeout 4
            show w neutral with dissolve
            "He glances at me for a moment."
            show w talk with dissolve
            w "You look exhausted."
            show w neutral with dissolve
            play music "ost/hospital.ogg" fadein 6
            m shock "H-huh?"
            show w frusttalk with dissolve
            w "Seriously, did you sleep at all last night..?"
            show w neutral with dissolve
            m uncom "Umm... To be honest, I am a little tired..."
            m boretalk "I had this weird dream last night..."
            show w tensetalk with dissolve
            w "A-A dream? What was it about?"
            show w sidetalk with dissolve
            w "...if I may ask."
            show w neutral with dissolve
            stop music fadeout 3
            "I try to recall the dream..."
            scene bg greetnight
            scene bg centralnight
            pause 1
            play music "ost/tension.ogg" fadein 8
            scene bg mcdesk with dissolve
            m fabtalk "I was... in the hospital... It was nighttime."
            show w tensetalk with dissolve
            w "...Was the moon full?"
            show w tense with dissolve
            m gasp "I... think so?"
            show w frusttalk with dissolve
            w "Shit... This isn't good."
            show w frust with dissolve
            "I'm confused."
            show w neutral with dissolve
            m serious "What's wrong?"
            show w angrytalk with dissolve
            w "I also had that dream last night."
            show w angry with dissolve
            m angry "Is... is that possible?"
            show w sidetalk with dissolve
            w "I've read about it, but it's never happened to me before."
            show w tensetalk with dissolve
            w "You can believe it or not, but for me it matters. What did you see in that dream?"
            show w angry with dissolve
            w "Where exactly were you?"
            show w tense with dissolve
            m fab "It started in the reception, I went upstairs to where my office is, and then..."
            m talk "The patients' rooms."
            show w talk with dissolve
            w "Were you in any room in particular?"
            show w neutral with dissolve
            m uncom "Umm... XIX..?"
            "Wait, that's..."
            show w frusttalk with dissolve
            w "...my room."
            show drk with dissolve
            show w talk with dissolve
            w "I was also there in my dream."
            show w frust with dissolve
            "I saw... someone in that dream..."
            show mirrorcg2 with dissolve
            show mirrorcg4 with dissolve
            show mirrorcg3 with dissolve
            hide mirrorcg3 with dissolve
            "!!!"
            show w tense with dissolve
            "Was that him?"
            hide drk with dissolve
            hide mirrorcg2 with dissolve
            hide mirrorcg4 with dissolve
            show w angrytalk with dissolve
            w "In my dream, I wasn't alone. Were you?"
            show w tense with dissolve
            m angry "There was someone else... I couldn't see their face. It was just... a shadow."
            show w fear with dissolve
            w "A... {i}shadow?"
            m fabtalk "Yeah, like a dark silhouette."
            show w frusttalk with dissolve
            w "Did it do anything?"
            show w tense with dissolve
            "...."
            m talk "It, um... approached me."
            show w tensetalk with dissolve
            w "Did it seem like it wanted to hurt you?"
            show w tense with dissolve
            "I think back to the dream... I felt threatened by that figure for some reason."
            stop music fadeout 8
            m talk "It... did."
            show w regret with dissolve
            "He's really anxious. But why..?"
            m talk "What does it mean? Did you see it as well in your dream?"
            show w tensetalk with dissolve
            w "...No. I only saw..."
            show w frust with dissolve
            play music "ost/hospital.ogg" fadein 6
            w "You."
            show w talk with dissolve
            w "I was standing in front of a mirror. You were on the other side."
            show w tense with dissolve
            "This... This is weird."
            m neu "I saw a mirror as well. That figure was on the other side."
            show w regret with dissolve
            w "...."
            show w paintalk with dissolve
            w "How could this happen..?"
            show w tensetalk with dissolve
            w "Do you get it already, [name]?"
            show w frusttalk with dissolve
            w "That wasn't me in your dream."
            show w regrettalk with dissolve
            w "It was... something else."
            show w sadtalk with dissolve
            stop music fadeout 4
            w "That part of my mind I told you about last time."
            show w regrettalk with dissolve
            w "The one that... wanted to hurt Marie. Kill my friends."
            play music "ost/tension.ogg" fadein 8
            show w tense with dissolve
            w "I... I think you need to know the truth now."
            show w regrettalk with dissolve
            w "I never found a more accurate psychological term to describe it than...\na shadow."
            show w regret with dissolve
            "A \"shadow\"? I think back to the last time I've heard that word used in this particular context..."
            show w tense with dissolve
            m fab "So it's a part of your personality that was created by you subconsciously..."
            show w neutral with dissolve
            "He nods."
            show w tense with dissolve
            m gasp "...as the polar opposite to what you consciously want to be like?"
            show w frusttalk with dissolve
            w "Right."
            show w frust with dissolve
            m uncom "And it's created from feelings you don't want to have?"
            show w regrettalk with dissolve
            w "That's... yes, that's putting it very directly."
            show w regret with dissolve
            m conf "Well, at least now I know what I'm working with."
            show w tensetalk with dissolve
            w "And... you're not even bothered by me having that?"
            show w tense with dissolve
            m fab "No, it seems to fit what I knew of you so far."
            show w frust with dissolve
            m gasp "Better yet, it's not an illness or something to be particularly concerned about..."
            m serious "...most of the times. I mean... everyone has it."
            show w regrettalk with dissolve
            w "I... Mine is difficult, I swear. It won't be that simple."
            show w tense with dissolve
            m talk "When did it first appear?"
            show w frusttalk with dissolve
            w "Maybe... 12 years ago? 13?"
            show w frust with dissolve
            m fabtalk "Alright. You said your parents' death could've affected it, though."
            show w talk with dissolve
            w "I guess it had room to grow since then, if that makes sense."
            show w neutral with dissolve
            m talk "Sure. So the first instance of it being troublesome was with Marie?"
            stop music fadeout 4
            show w sidetalk with dissolve
            w "Yes."
            show w tense with dissolve
            m neu "Could you describe the feelings that went into it in more detail?"
            play music "ost/emo.ogg" fadein 8
            show w sidetalk with dissolve
            w "I... {i}I..."
            show w dis with dissolve
            w "{i}!!!"
            show w hiden with Dissolve(1.0)
            w "{i}I can't-"
            w "{i}I'm... so sorry..."
            show w pain with dissolve
            "He pauses to calm down. His voice returns to normal."
            show w paintalk with dissolve
            w "I just... I can't talk about it, I really can't..."
            show w frust with dissolve
            m pity "That's okay."
            show w tense with dissolve
            m talk "So... can you tell me how it looks to you?"
            show w regrettalk with dissolve
            w "It's... it's not human."
            show w angrytalk with dissolve
            w "It's hideous. Terrifying."
            show w frusttalk with dissolve
            w "But... it doesn't have some appearance I can recall right now."
            show w tensetalk with dissolve
            w "Sometimes it looks like me, sometimes completely different."
            show w tense with dissolve
            m fabtalk "Does it talk to you?"
            show w tense with dissolve
            w "Constantly. Whenever it has anything to feed off of, that is."
            show w regrettalk with dissolve
            w "These past two years, I barely remember it disappearing."
            show w regret with dissolve
            m serious "When does it go away?"
            show w calm with dissolve
            w "...When I'm happy."
            show w sidetalk with dissolve
            w "And that barely ever happens."
            show w siden with dissolve
            "...."
            "I feel sorry for him."
            show w paintalk with dissolve
            w "Whenever I have any doubts about what to do, it's there to convince me to do the thing I least want."
            show w tensetalk with dissolve
            w "It... it whispers the thoughts I never wanted to have at the back of my mind."
            show w frust with dissolve
            m talk "Can you find any recent examples?"
            show w frusttalk with dissolve
            w "Yesterday... it..."
            show w tensetalk with dissolve
            w "It told me how pathetic I was for..."
            show w regrettalk with dissolve
            w "...not... wanting you to go away..."
            show w broke with dissolve
            m sadtalk "William..."
            show w scream with dissolve
            w "I-I know it's pathetic, [name]."
            show w broketalk with dissolve
            w "I know that I'm desperate. But I'm really going to break if I hear it from you."
            show w broke with dissolve
            m angry "William, you're wrong. I'd never think of you that way."
            show w scream with dissolve
            w "You... You're lying, you must be lying..."
            show w broketalk with dissolve
            w "I... I was responsible for what happened yesterday. I was the one who didn't move away when I should have." 
            show w cry with dissolve
            w "It's my fault... you wouldn't have done it if you hadn't thought I wanted you to."
            "God dammit, I have the urge to do something stupid I would regret just to convince him."
            show w broke with dissolve
            "Instead, I get a little closer to him, not as close as yesterday, and say:"
            m talk "I didn't want to move away, and that's why I didn't. You're not to blame here."
            show w fear with dissolve
            "He turns pale at my words."
            show w dis with dissolve
            w "You... You didn't..?"
            show w scream with dissolve
            w "No, no... why did you say that?"
            show w broke with dissolve
            w "{i}!!!"
            show w hiden with Dissolve(1.0)
            w "It's... I shouldn't... I really shouldn't be allowed to hear you say such things."
            stop music fadeout 4
            m uncom "Why?"
            show w broketalk with Dissolve(1.0)
            w "B-Because... it's becoming attached to you."
            show w dread with dissolve
            m gasp "What is?"
            play music "ost/tension.ogg" fadein 8
            show w regrettalk with dissolve
            w "My... shadow."
            show w paintalk with dissolve
            w "It's best if it ignores you..."
            show w regrettalk with dissolve
            w "That way, you'll be... you'll be safe."
            show w tensetalk with dissolve
            w "The more it says about you, the more focused it is on you."
            show w tense with dissolve
            m serious "What did it say about me just now?"
            show w tsun with dissolve
            w "...."
            show w frusttalk with dissolve
            w "You... you shouldn't know."
            show w frust with dissolve
            m regrettalk "William, please..."
            show w dis with dissolve
            w "{i}I can't tell you!"
            show w hiden with Dissolve(1.0)
            w "You... {i}you would hate me if you knew..."
            m angry "I wouldn't."
            show w broketalk with Dissolve(1.0)
            w "[name], you have no idea..."
            show w tense with dissolve
            "He's not going to tell me."
            m talk "Whatever it is, I can take it."
            show w sidetalk with dissolve
            w "I... I doubt it."
            show w frust with dissolve
            m angrytalk "William. Listen to me."
            "I look straight at him."
            show w tense with dissolve
            m serious "Whatever these feelings are, they're yours."
            show w regrettalk with dissolve
            w "I... I know..."
            show w regret with dissolve
            m frust "They can't be that horrible if they came from you."
            m talk "It's not like it's some... foreign entity that's just pure evil."
            show w sidesmile with dissolve
            w "Heh, actually..."
            show w calm with dissolve
            w "The pure evil part fits."
            show w pain with dissolve
            m "It comes from a human mind. It has traits of a person."
            show w siden with dissolve
            m angry "So it can't be just evil."
            show w frusttalk with dissolve
            w "It is. You haven't seen it."
            show w tense with dissolve
            m talk "I want to, then."
            show w dis with dissolve
            w "Wh-What?!"
            show w sadtalk with dissolve
            w "You... you really... want to see it in person?"
            show w tense with dissolve
            "Wait, what?"
            show w frusttalk with dissolve
            w "Remember how... I told you I was scared I may not have a choice someday?"
            show w regrettalk with dissolve
            w "I fear that... if there's no hope left for me, and I'm... in a lot of pain... I might..."
            show w broke with dissolve
            w "It might... take control."
            show w tensetalk with dissolve
            w "{i}Then{/i} I'd become a monster."
            show w sadtalk with dissolve
            w "I would hurt and kill without remorse."
            show w broketalk with dissolve
            w "Everything I am now would die."
            stop music fadeout 4
            show w regrettalk with dissolve
            w "That's why... I would rather kill myself before I lose the choice to."
            show w pain with dissolve
            m regret "...."
            play music "ost/neutral.ogg" fadein 8
            show w sadtalk with dissolve
            w "If you're really sure, I could... do exactly what it's telling me to for some time, so... you can ask it things I can't tell you."
            show w regrettalk with dissolve 
            w "It... it knows my every thought, and has no reason to lie or avoid answering."
            show w tensetalk with dissolve
            w "I would only stop it if it tried to hurt you, or if you decided you've learned enough."
            show w tense with dissolve
            m uncom "Are you... capable of that?"
            show w sidetalk with dissolve
            w "I've never done it consciously, but even it thinks it's possible."
            show w neutral with dissolve
            m talk "And you're sure you could come back when I ask you to?"
            show w sidetalk with dissolve
            w "I won't be gone in the first place, so it should be fine."
            show w frust with dissolve
            m serious "Are you really comfortable trying something like that?"
            show w talk with dissolve
            w "If it's necessary, I will."
            show w neutral with dissolve
            stop music fadeout 4
            m boretalk "Then..."
            menu:
                "I want to see it":
                    show w sadtalk with dissolve
                    w "Are you sure?"
                    show w sad with dissolve
                    menu:
                        "Yes":
                            $ShadowTalk=True
                            play music "ost/hospital.ogg" fadein 6
                            show w sidetalk with dissolve
                            w "Then... It'll be here on Monday."
                            show w talk with dissolve
                            w "I will set it free in the morning before I go see you."
                            show w frust with dissolve
                            w "Don't worry, I'll force it to come here and talk to you."
                            show w tensetalk with dissolve
                            w "And if you need another day to talk to it, it will stay in control for the night and come here again."
                            show w talk with dissolve
                            w "Once you'll have learned everything, tell it to leave."
                            show w frust with dissolve
                            w "I should be back soon after that."
                            show w tense with dissolve
                            m neu "I understand."
                        "No":
                            play music "ost/neutral.ogg" fadein 6
                            show w sidesmile with dissolve
                            w "That's fine. Maybe once we're both... more prepared."
                "Let's not try that":
                    play music "ost/neutral.ogg" fadein 6
                    show w frust with dissolve
                    m uncom "I mean, you could say something you'd regret, or..."
                    show w sidetalk with dissolve
                    w "Yeah, right... Well, I was just asking."
                    show w sadsmile with dissolve
                    w "To be honest, I wasn't prepared to try that, either..."
            show w siden with dissolve
            "We're short on time."
            show w neutral with dissolve
            m sadsmile "Thank you for telling me about all of that..."
            show w frust with dissolve
            m fabtalk "I'll try to research shadows over the weekend, and hopefully this'll be getting somewhere next week."
            show w neutral with dissolve
            "He nods."
            show w sidetalk with dissolve
            w "I'll see you on Monday, then."
            stop music fadeout 5
            hide screen easymeter
            hide screen silvermeter
            if ShadowTalk:
                show w regretsmile with dissolve
                w "...or not."
            show w neutral with dissolve
            "He leaves in a hurry."
            jump breakchoice
        else:
            show w frusttalk with dissolve
            w "Umm..."
            show w sidetalk with dissolve
            w "Not really..."
            if SilverHeart>=18: ##czyli jej nie odepchnął
                show w siden with dissolve
                "It seems that he won't say much today."
                "It might be due to what happened yesterday..."
                "Strangely, he didn't seem bothered then, but... he might be now."
            else:
                show w frust with dissolve
                "He must still be uncomfortable after what happened yesterday... I really messed up."
                m uncom "I'm sorry about last time."
                show w fear with dissolve
                w "Huh?"
                show w regrettalk with dissolve
                w "There's... nothing to be sorry for."
                show w frusttalk with dissolve
                w "I probably overreacted... I apologize."
                show w neutral with dissolve
                m angry "It won't happen again."
                show w sidetalk with dissolve
                w "Thank you..."
                show w siden with dissolve
                "He still doesn't seem very eager to talk to me, but at least I made it clear that I didn't mean it."
            m serious "Can I ask you about something you said last time?"
            show w talk with dissolve
            w "About what exactly?"
            stop music fadeout 5
            show w neutral with dissolve
            m fabtalk "You mentioned... having a part of you that kept telling you that you wanted to kill your friend. That... you wanted to hurt people."
            show w regret with dissolve
            w "...."
            play music "ost/hospital.ogg" fadein 6
            show w frusttalk with dissolve
            w "...that's right."
            show w frust with dissolve
            m gasp "Could you tell me some more about this part of you?"
            "I feel like that's the issue that needs adressing the most."
            show w talk with dissolve
            w "It's... I don't really know what to say..."
            show w regret with dissolve
            m regrettalk "Why are you so afraid of it, William..?"
            show w regrettalk with dissolve
            w "You wouldn't... you wouldn't understand..."
            stop music fadeout 5
            show w tense with dissolve
            m serious "How do you know? Haven't I done a good job understanding things so far?"
            show w sidetalk with dissolve
            w "Actually..."
            if SilverHeart>=10:
                show w frusttalk with dissolve
                w "Most of the time, you handled yourself... I guess..."
                show w regrettalk with dissolve
                play music "ost/tension.ogg" fadein 6
                w "But... when you failed, you... that really... hurt."
                show w paintalk with dissolve
                w "Just yesterday, I was willing to tell you everything... I really could've trusted you..."
                show w broketalk with dissolve
                w "But you... you just showed me how little you understand. And it hurts a lot more knowing I..."
                show w dis with dissolve
                w "...I really believed you could help me."
                show w dread with dissolve
                m sjw "I can!"
                show w paintalk with dissolve
                w "...No. I don't trust you anymore."
            else:
                play music "ost/tension.ogg" fadein 6
                show w frusttalk with dissolve
                w "...You haven't. You don't understand at all."
                show w frust with dissolve
                "...What?"
                "But... I've done everything right, haven't I..?"
                m gasp "Isn't that a bit-"
                show w angrytalk with dissolve
                w "No. It's how I feel."
                show w sidetalk with dissolve
                w "And if you really care so much about what I think, you should give up."
            show w talk with dissolve
            w "All you can do right now is try not to mess it up even more."
            show w frusttalk with dissolve
            w "I have no way to force you to give up, but I won't let you any closer..."
            stop music fadeout 4
            show w angry with dissolve
            w "I won't let you \"save\" me like you wanted to."
            show w regrettalk with dissolve
            w "Of course, you're determined, so I know you'll keep seeing me."
            play music "ost/emo.ogg" fadein 10
            show w talk with dissolve
            w "You'll end up the way all my previous psychologists did - doing absolutely nothing to help."
            show w neutral with dissolve
            "All this time, I thought that... his previous psychologists were doing a bad job..."
            "Now I see that... I'm no better."
            "He really can't be helped like this... And I believed I was different."
            "That I would save him. I don't think I can anymore..."
            show w siden with dissolve
            m angry "You're right. You can't stop me from trying."
            "We still have a lot of time, but I think this is all I need to say."
            show w neutral with dissolve
            m uncom "I will see you again on Monday."
            scene bg mc with dissolve
            "He gets up to leave."
            m regrettalk "Take... take care of yourself, William."
            w "It's over, Dr. Hart. Don't bother."
            hide screen easymeter
            hide screen silvermeter
            play sound "doorclose.ogg" fadein 1
            "The door closes behind him."
            "I... I can't believe he really rejected my help... after everything we... {i}I{/i} did for him..."
            scene black with Dissolve(1.5)
            "I've failed. I really have."
            "I spend the break in my office and pick a random patient for my second session just so I can focus on anything that isn't William."
            "At least... at least the others are willing to talk..."
            stop music fadeout 4
            "...That doesn't help at all."
            "William... William, come back... He won't last long without help..."
            scene bg central with dissolve
            play music "ost/tension.ogg" fadein 6
            "I'm on my way out of the hospital. This day was... I still can't believe he rejected my help just like that..."
            scene bg patients with dissolve
            "Something pulls me to the door of his room. I need to see him again, at least."
            m serious "William? Are you there?"
            "No response."
            "I can't bear to be here anymore. I walk away quickly."
            nn "Hey, [name]! [name]!"
            stop music fadeout 4
            "I hear a familiar voice calling my name suddenly. I stop."
            m gasp "Michael?"
            show bg closeXV2 with dissolve
            play music "ost/hospital.ogg" fadein 8
            "He's staring at me intently. I approach the door to his room."
            "It takes me a bit to realize I'm seeing him free for the first time."
            dv "What's gotten into Moore today? He seems... more depressed than usual."
            "For whatever reason, I feel like I can tell him the truth."
            "...Maybe it's because I desperately need to talk to someone about it."
            m regrettalk "I... I failed. It's my fault."
            dv "...what did you do?"
            "He sounds surprisingly serious."
            m sadtalk "It's just that... he doesn't seem to trust me anymore."
            dv "Oh... That must be tough."
            dv "But hey, don't worry about it too much - he does that sometimes."
            m confusion "What?"
            dv "I mean, I don't know him all that well, but I don't think it's permanent."
            dv "...Unless you've really fucked up."
            m sadsmile "No, I... I don't think it's that bad..."
            dv "Give him some time. He should come back to his senses in a couple of days."
            menu:
                "Alright, thanks":
                    pass
                "How do you know all that?":
                    dv "Do you think I have anything better to do here than watch people?"
                    dv "Especially since he's been here for the second longest time."
                    "Right... they've both been here for a while..."
                    dv "So I pride myself on knowing a lot of things. About the staff as well."
                    "I suppose he needs something to occupy himself with."
                    m boretalk "If that's so, then..."
            m smile "Thank you, Michael. Looks like I can't lose hope for him yet."
            dv "Definitely. He seems like he's going to take a while."
            "I leave the hospital with a smile. Maybe I shouldn't overreact yet."
            jump nextday
    elif day == 13 or day == 14:
        jump nextday
##########################         
    elif day == 15:
        if ShadowTalk:
            define wn = Character("William..?", color='#ffffff')
            define sh = Character("Shadow", color='#ffffff')
            ##Meeting the Shadow p.1
            scene bg mc with dissolve
            "I'm waiting in my office."
            "I have to admit, I am a little nervous... I don't know what to expect, but at least I have a couple of questions prepared."
            "Let's see how it goes."
            "The door to my office opens..."
            show bg mcdesk with dissolve
            show w smile with dissolve
            w "Hello."
            m fab "...good morning. How are you today?"
            show w sidetalk with dissolve
            w "I..."
            show w crazy with dissolve
            wn "...."
            show w pain with dissolve
            wn "...."
            show w frust with dissolve
            wn "I apologize for the inconvenience. We seem to be alone already."
            show w talk with dissolve
            wn "Allow me to introduce myself more properly, then."
            hide w with dissolve
            show bg mcdeskdark with dissolve
            show w sa with dissolve
            $renpy.pause(2.3,hard=True)
            show w s1 with dissolve
            show es s
            sh "{b}I am the shadow. His true self."
            sh "{b}It is a pleasure to see you in person at last, Ms. Hart."
            play music "ost/shadow.ogg" fadein 10
            show w s2 with dissolve
            "...."
            "Focus, [name]..."
            m fabtalk "I don't think the enthusiasm is mutual."
            show w s4 with dissolve
            sh "{b}Is it? Judging by how quickly you agreed to see me, one could even say you were... {i}very{/i} enthusiastic about it."
            show w s2 with dissolve
            sh "{b}Or am I wrong?"
            sh "{b}Pardon me, then. From his point of view, it certainly seemed so."
            "He seems a lot more talkative than William, but I have questions to ask. I won't let him distract me."
            m "I had some questions for you."
            show w s4 with dissolve
            sh "{b}Of course."
            show w s3 with dissolve
            m talk "Since when did you exist in William's mind? If that's not too indelicate to ask."
            "I'm used to interacting with people, not... psychological structures in people's minds."
            show w s1 with dissolve
            sh "{b}Heh, like that could affect me..."
            show w s4 with dissolve
            sh "{b}You're being a lot more \"delicate\" than you need to be."
            show w s3 with dissolve
            sh "{b}[name], I don't feel anything. You can't hurt me."
            show w s4 with dissolve
            sh "{b}Since I don't \"exist\" all that much."
            show w s2 with dissolve
            "Let's try a different approach then..."
            m neu "Do you have memories?"
            show w s4 with dissolve
            sh "{b}I know what he knows. I don't have seperate memories."
            show w s5 with dissolve
            sh "{b}It would be quite strange for something that doesn't really exist to have memories, don't you think?"
            show w s2 with dissolve
            "...."
            sh "{b}Perhaps a smarter question would be: \"When did {i}he{/i} start to acknowledge me?\"."
            show w s4 with dissolve
            sh "{b}But you already know the answer to that, so your whole question was utterly pointless."
            show w s2 with dissolve
            "...."
            "I'm starting to be annoyed by his all-knowing attitude, but I remain calm."
            m fabtalk "Let me try to ask something more direct then - who are you?"
            m angry "Maybe a simpler question will be easier for you to comprehend."
            show w s1 with dissolve
            "He smiles. I think he's enjoying this."
            show w s4 with dissolve
            sh "{b}See? Now you're starting to get better at it. I can't believe you got this far with him without being able to properly ask questions."
            show w s3 with dissolve
            sh "{b}Then again, he wouldn't care much either way. He would need to have standards for that."
            show w s4 with dissolve
            sh "{b}I am him, and he is me. We're like two sides of the same coin, Ms. Hart."
            sh "{b}He can't exist without me, and vice versa."
            show w s2 with dissolve
            sh "{b}One of us has to be in control, of course, but that doesn't erase the other one."
            m angrytalk"How much in control are you really right now?"
            show w s4 with dissolve
            sh "{b}As much as I'm allowed to."
            show w s3 with dissolve
            sh "{b}He wouldn't let me act completely on my own."
            show w s4 with dissolve
            sh "{b}So you should be safe..."
            show w s1 with dissolve
            sh "{b}For now."
            m uncom "What exactly did he do to make you appear?"
            show w s4 with dissolve
            sh "{b}That look in your eyes... You think it must have been difficult to change so much in an instant. That he's suffering right now."
            show w s1 with dissolve
            sh "{b}The truth is, it's not difficult to give up. Especially for him."
            show w s4 with dissolve
            sh "{b}You still believe he's a good person... that he really doesn't want any of this?"
            show w s3 with dissolve
            sh "{b}It's not difficult at all to let these feelings take over. After all, they are too strong for him to block them forever."
            show w s4 with dissolve
            sh "{b}All he had to do was admit how much he's lying to himself. And that doesn't hurt him."
            show w s2 with dissolve
            m gasp "What feelings are you talking about? The ones that you came from?"
            sh "{b}It's painfully simple, Ms. Hart. So simple he never wanted to admit it."
            show w s4 with dissolve
            sh "{b}I am hatred. Rage."
            show w s1 with dissolve
            sh "{b}And look at me now - I only grew so relevant because of the amounts of them he feels but doesn't want to."
            show w s2 with dissolve
            sh "{b}Over time, I also became everything he simply doesn't consider \"right\"."
            sh "{b}...At least, that's his view."
            show w s4 with dissolve
            sh "{b}I've grown, Ms. Hart. All those years ago I was only a single emotion he couldn't contain any other way."
            show w s1 with dissolve
            sh "{b}And now? You could even say I'm a human being on my own."
            show w s3 with dissolve
            sh "{b}Although that's highly debatable, from my point of view, I exist as much as everything else."
            show w s5 with dissolve
            sh "{b}If I said that you don't exist, would you disappear?"
            show w s4 with dissolve
            sh "{b}I don't think so."
            show w s1 with dissolve
            sh "{b}If that's not funny enough, I believe in reality. If I didn't, that would mean I only started existing once I entered your office."
            show w s2 with dissolve
            sh "{b}\"Existing\" only for one person doesn't seem like much, though..."
            m talk "Is he listening to us right now? Will he remember all of this?"
            show w s3 with dissolve
            sh "{b}He's there, but very faintly."
            show w s4 with dissolve
            sh "{b}I can't predict whether he chooses to remember this or not."
            show w s2 with dissolve
            m serious "What would you do if you were free right now?"
            show w s1 with dissolve
            sh "{b}I don't think you would want to listen to the details..."
            show w s4 with dissolve
            sh "{b}You're a fragile one, aren't you? \"Sensitive\", that's what you'd call it."
            show w s1 with dissolve
            "I'm seeing a certain parallel to how William refuses to tell me somethings claiming that I wouldn't understand."
            "...They really are two sides of the same coin. It's just that the similarities are quite hard to spot."
            show w s4 with dissolve
            sh "{b}If I were free right now, it wouldn't be very pleasant for you, I assure you."
            show w s3 with dissolve
            sh "{b}Oh? He seems to be struggling. He must really not want you to know that."
            "He tilts his head back a bit and looks somewhere to the side."
            show w s1 with dissolve
            sh "{b}How delightful."
            show w s4 with dissolve
            sh "{b}Listen, [name]."
            hide es s
            hide w with dissolve
            show bg mcdark with dissolve
            show w sc2 with dissolve
            show es c 
            "He places his hand at the back of my head and pulls me closer. Way too close."
            show w sc4 with dissolve
            sh "{b}One day, these feelings may be too much for him."
            sh "{b}Once he loses hope, he'll lose his \"humanity\" as well."
            show w sc2 with dissolve
            sh "{b}That day, I'll be freed."
            show w sc1 with dissolve
            sh "{b}And you can be sure I won't forget about you then."
            menu:
                "That will never happen":
                    sh "{b}Go ahead, keep trying to deceive yourself."
                    show w sc4 with dissolve
                    sh "{b}Keep building yourself a wall of false hope. It won't save you when the time comes."
                "You can't hurt me":
                    "He laughs."
                    show w sc4 with dissolve
                    sh "{b}Do you really think that's all I'm capable of?"
                    show w sc3 with dissolve
                    sh "{b}He's still trying to stop me from tearing you apart."
                    show w sc1 with dissolve
                    sh "{b}But he won't last long."
                "What will you do?":
                    show w sc4 with dissolve
                    sh "{b}You really are curious, aren't you?"
                    show w sc1 with dissolve
                    sh "{b}I like that."
                    show w sc2 with dissolve
                    sh "{b}I'll tell you once you're ready... Or maybe you'll get to see it for yourself."
                    show w sc1 with dissolve
                    sh "{b}It won't be long before I can do anything I want to you."
            show w sc4 with dissolve
            sh "{b}At this rate, I'm giving him less than half a year before he gives up completely."
            sh "{b}You're blind if you think you can stop it."
            show w sc1 with dissolve
            sh "{b}He's so close now... These really are his last attempts at stopping me."
            show w sc4 with dissolve
            sh "{b}Why do you think he's so desperate to let you help him?"
            show w sc3 with dissolve
            sh "{b}He knows it's coming. So he's doing everything he can to stop it."
            show w sc4 with dissolve
            sh "{b}It's pathetic, really..."
            show w sc2 with dissolve
            sh "{b}Like you can do anything to stop me, with your patient smiles and words of encouragement. You're nothing, [name]."
            show w sc3 with dissolve
            sh "{b}You're worthless, just like him."
            show w sc4 with dissolve
            sh "{b}That's why you'll never be strong enough to stop me from taking over."
            show w sc2 with dissolve
            menu:
                "I'm not worthless":
                    $personal+=2
                    $wrong+=1
                    m angrytalk "I'm stronger than you, and so is he."
                    m sjw "I'm going to save him and you have no right to question it."
                    show w sc4 with dissolve
                    sh "{b}So self-centered... \"I'm going to save him\"... in the end, it's all about you."
                    show w sc3 with dissolve
                    m serious "That's not what I-"
                    show w sc1 with dissolve
                    sh "{b}Ouch, touchy subject, isn't it? I apologize if that hurt your feelings, Ms. Hart."
                    scene bg mcdeskdark with dissolve
                    show w s3 with dissolve
                    show es s
                "He's not worthless":
                    m talk "He can fight back on his own. I just need him to realize that."
                    show w sc1 with dissolve
                    sh "{b}Heh, good luck-"
                    show w sc3 with dissolve
                    m neu "Silence."
                    m angrytalk "I won't let you call him worthless."
                    show w sc2 with dissolve
                    m angry "It takes a lot more strength to keep trying to do what's right than to give up and think that makes you any better."
                    m fabtalk "You're just too weak to take action, so you act like it's better to do nothing."
                    scene bg mcdeskdark with dissolve
                    show w s3 with dissolve
                    show es s
                "You're the worthless one":
                    scene bg mcdeskdark with dissolve
                    show w s3 with dissolve
                    show es s
                    "I struggle out of his grip and get away from him."
                    m talk "You think I care for your bullshit?"
                    m neutral "I have no reason to believe you. You're just spouting lies like an immature child because you think you're beyond consequences."
                    m angry "Truly, you are the pathetic one. You don't even \"exist enough\" to take responsibility for your actions."
                    m fabtalk "Someone like you has no right to lecture me."
                "Even if he'll give up eventually, I'll keep trying":
                    m "The least I can do is try."
                    m "If I gave up, I would be as pathetic as you."
                    show w sc4 with dissolve
                    sh "{b}Does it really matter if you \"try\"?"
                    show w sc2 with dissolve
                    sh "{b}Do you think he'd want you to prolong his suffering just for the sake of your own integrity?"
                    show w sc1 with dissolve
                    sh "{b}He doesn't care about how you feel. And soon, he won't care about anything at all."
                    "He pulls away from me."
                    scene bg mcdeskdark with dissolve
                    show w s3 with dissolve
                    show es s
            sh "{b}...."
            show w s2 with dissolve
            sh "{b}You may have very little understanding of your situation, but you're still going to fight back."
            show w s4 with dissolve
            sh "{b}I have to say, I appreciate women who don't break easily."
            show w s1 with dissolve
            sh "{b}Otherwise, what fun would there be in getting them to give up?"
            sh "{b}Seeing all hope disappear from your eyes when you realize it's too late to stop me... it would certainly be amusing."
            show w s4 with dissolve
            sh "{b}But alas, our time has run out... I will see you again tomorrow."
            show w s2 with dissolve
            m angrytalk "Wait-"
            show w s1 with dissolve
            sh "{b}What is it? Do you not want me to leave?"
            m fabtalk "No. But I decide whether I want to see you again or not."
            show w s4 with dissolve
            sh "{b}What do you want, then?"
            show w s3 with dissolve
            "I get up."
            m talk "I still have things to ask you, so I would like you to be back here tomorrow."
            m fab "Goodbye for now."
            show w s2 with dissolve
            "He nods slowly. I can tell he's mocking my attempts at controlling the situation."
            show w s1 with dissolve
            stop music fadeout 6
            sh "{b}Of course, Ms. Hart."
            play sound "doorclose.ogg" fadein 1
            scene bg mc with dissolve
            "He leaves. I wonder if he'll turn back into William for the rest of the day or not..."
            "I hope I really can bring him back when I'm done with... whatever that thing is."
            "...That was stressful. I need to be more prepared tomorrow... I wasn't expecting any of this."
            "Ugh, that was uncomfortable... I need to do something relaxing over my break or I'll go crazy."
            jump breakchoice
        elif Moonship:
            scene bg mc with dissolve
            "William enters my office."
            play music "ost/neutral.ogg" fadein 8
            w "Good morning, Dr. Hart."
            if easymeter:
                show screen easymeter
                show screen silvermeter
            m cute "It's good to see you again ~"
            "I wait for him to sit down."
            scene bg mcdesk with dissolve
            show w tense with dissolve
            m talk "How was the weekend?"
            show w frusttalk with dissolve
            w "I've been thinking a lot..."
            show w tensetalk with dissolve
            w "About what's best for everyone."
            show w frust with dissolve
            m gasp "Huh? What does that mean?"
            show w regrettalk with dissolve
            w "I shouldn't have offered to let you talk to it. I'm sorry."
            show w regret with dissolve
            m fabtalk "Why do you think that?"
            show w tensetalk with dissolve
            w "You wouldn't get anything out of it other than stress."
            show w paintalk with dissolve
            w "And... I'd feel bad about the things it could tell you."
            show w siden with dissolve
            w "...."
            show w talk with dissolve
            w "That would just be counterproductive."
            show w neutral with dissolve
            stop music fadeout 6
            m neu "I see."
            m boretalk "You didn't look convinced when you suggested it, and I knew I shouldn't pressure you."
            play music "ost/tran.ogg" fadein 8
            show w calmsmile with dissolve
            w "Thank you."
            show w talk with dissolve
            w "Really, you would only only get more questions than answers from it."
            show w frusttalk with dissolve
            w "It would take another session to right all the wrongs in what it would've said."
            show w tense with dissolve
            m talk "You know it better than I do, so I trust you."
            m conf "There's no reason to justify yourself."
            show w regretsmile with dissolve
            w "...I can't thank you enough for understanding, Dr. Hart."
            show w siden with dissolve
            m fabtalk "I take it none of your previous psychologists had the chance to interact with it?"
            show w talk with dissolve
            w "I never offered it for everyone."
            show w neutral with dissolve
            menu:
                "Why is that?":
                    show w sidetalk with dissolve
                    w "I never trusted my previous psychologists enough."
                    show w frust with dissolve
                    "If that was a sign of trust, maybe I should've..?"
                    show w neutral with dissolve
                    m regret "...."
                    show w tensetalk with dissolve
                    w "Umm... wait, that's not what I meant."
                    show w frusttalk with dissolve
                    w "You shouldn't agree to something like that."
                    show w paintalk with dissolve
                    w "...trust is just the amount of nonsense I spout around someone."
                    show w calm with dissolve
                    w "Sorry about misleading you before."
                "You never even considered it?":
                    show w angry with dissolve
                    w "No."
                    show w talk with dissolve
                    w "Why do you ask?"
                    show w neutral with dissolve
                    m fab "I was just... curious."
                    show w siden with dissolve
                    "Just how much does he trust me, then..?"
                    "I must be somewhat special if he even suggested something like that."
            show w neutral with dissolve
            m frust "Umm..."
            "I wonder how to put it..."
            show w tense with dissolve
            m smile "Regardless of why you brought it up in the first place, thank you."
            show w fear with dissolve
            w "Huh?"
            show w neutral with dissolve
            m cute "That means you trust me, right? Trust is important ~"
            show w regrettalk with dissolve
            w "I... I suppose."
            stop music fadeout 6
            show w tense with dissolve
            m conf "Hey, it's alright. I think we're going in the right direction here."
            show w sadtalk with dissolve
            w "Towards... what, exactly?"
            show w sad with dissolve
            m fabtalk "You leaving this place. That's what I'm here for, isn't it?"
            play music "ost/tension.ogg" fadein 8
            show w regrettalk with dissolve
            w "I don't... know."
            show w tensetalk with dissolve
            w "I don't like the thought of that, Dr. Hart."
            show w tense with dissolve
            m gasp "Why is that?"
            show w frust with dissolve
            w "...."
            show w paintalk with dissolve
            w "It's because of... {i}that thing."
            show w sad with dissolve
            m talk "You mean your shadow?"
            show w tensetalk with dissolve
            w "That's right."
            show w tense with dissolve
            m angry "If that's the problem, how do I fix it?"
            show w regrettalk with dissolve
            w "You can't. You can't fix it."
            show w paintalk with dissolve
            w "Seeing it would only make things worse."
            show w frusttalk with dissolve
            w "It would be better for you to... stop trying to make it disappear."
            show w pain with dissolve
            menu:
                "As you wish":
                    show w gasp with dissolve
                    w "Wh... What?"
                    show w dis with dissolve
                    stop music fadeout 6
                    w "Do you really... mean that?"
                    show w fear with dissolve
                    m regrettalk "If it makes you happy, I can stop asking you about it."
                    show w sidetalk with dissolve
                    w "And... I'd get a new psychologist again?"
                    show w neutral with dissolve
                    play music "ost/hospital.ogg" fadein 8
                    m angry "No. I'd stay and make sure you're not getting any worse."
                    show w frust with dissolve
                    w "That's..."
                    show w regrettalk with dissolve
                    w "That's too kind for someone like me, [name]."
                    show w tensetalk with dissolve
                    w "You shouldn't... keep seeing me, if it's going to be like that."
                    show w paintalk with dissolve
                    w "You have other patients. They need you more."
                "What then?":
                    show w talk with dissolve
                    stop music fadeout 5
                    w "Then?"
                    show w siden with dissolve
                    "He pauses."
                    show w paintalk with dissolve
                    w "Nothing. It would go back to the way it was before we met."
                    show w calm with dissolve
                    m frust "...."
                    show w neutral with dissolve
                    play music "ost/tension.ogg" fadein 8
                    m angrytalk "No! I can't let this go on!"
                    show w tense with dissolve
                    m sad "William, please... There has to be a way for me to help."
                    show w tensetalk with dissolve
                    w "There isn't."
                    show w paintalk with dissolve
                    w "I'm sorry, [name] - it's impossible."
                    show w tense with dissolve
                    m serious "If... I really can't help, I'll ask for you to be reassigned."
                    m regret "Maybe... I've gotten too attached to help."
                    show w dis with dissolve
                    w "Attached? To... me?"
                    show w fear with dissolve
                    "I nod."
                    show w regret with dissolve
                    w "...."
                    show w broketalk with dissolve
                    w "I'm so sorry, [name]."
                    show w sad with dissolve
                    w "You shouldn't waste your time on me."
                    show w regrettalk with dissolve
                    w "I'm not worth any of that."
                "But it's making you suffer!":
                    stop music fadeout 4
                    $SilverHeart+=1
                    show drk with Dissolve(0.75)
                    show s 1 with dissolve
                    show s 2 with Dissolve(1.0) 
                    $renpy.pause(0.75, hard = True)
                    hide s with dissolve
                    hide drk with dissolve
                    show w angrytalk with dissolve
                    w "And you can't do anything about it, so just stop already."
                    show w frust with dissolve
                    play music "ost/tension.ogg" fadein 8
                    m angrytalk "No! I can't let this go on!"
                    m sad "William, please... There has to be a way for me to help."
                    show w talk with dissolve
                    w "There isn't."
                    show w regrettalk with dissolve
                    w "I'm sorry, [name] - it's impossible."
                    show w tense with dissolve
                    m serious "If... I really can't help, I'll ask for you to be reassigned."
                    m regret "Maybe... I've gotten too attached to help."
                    show w dis with dissolve
                    w "Attached? To... me?"
                    show w fear with dissolve
                    "I nod."
                    show w regret with dissolve
                    w "...."
                    show w broketalk with dissolve
                    w "I'm so sorry, [name]."
                    show w sad with dissolve
                    w "You shouldn't waste your time on me."
                    show w regrettalk with dissolve
                    w "I'm not worth any of that."
            show w pain with dissolve
            stop music fadeout 5
            "I don't know what to do."
            show w tense with dissolve
            m regrettalk "What do you want, William?"
            m angry "You know I'll at least try if you tell me."
            show w frust with dissolve
            play music "ost/neutral.ogg" fadein 6
            w "...."
            show w regrettalk with dissolve
            w "I... I don't..."
            show w pain with dissolve
            w "...."
            show w tense with dissolve
            m sad "Be honest. Please."
            show w gasp with dissolve
            w "...."
            show w regrettalk with dissolve
            w "Do I... have to?"
            show w tense with dissolve
            m boretalk "For me?"
            show w neutral with dissolve
            stop music fadeout 5
            w "...."
            show w talk with dissolve
            w "I don't... want you to leave."
            show w siden with dissolve
            "I thought so."
            play music "ost/hospital.ogg" fadein 6
            show w frusttalk with dissolve
            w "But... I know that's too much to ask. Since there's nothing you can do to help, and..."
            show w tense with dissolve
            m angry "Would that make you happy?"
            show w paintalk with dissolve
            w "...No. Knowing you're doing that for me... would be overwhelming."
            show w sadtalk with dissolve
            w "I don't want to be a waste of your time and commitment."
            show w regrettalk with dissolve
            w "And... I hate the thought of you focusing on me, instead of helping the others."
            show w tense with dissolve
            m regrettalk "Then... you really want me to reassign you to a different psychologist?"
            show w frusttalk with dissolve
            w "That would be... for the best..."
            show w broke with dissolve
            w "...."
            "Should I really let him go?"
            "I know he's asking me to, but would that really benefit anyone?"
            "I'd feel bad for leaving him like that..."
            "...but if another psychologist can help him, I can't let my feelings sway me."
            menu:
                "Do as he says":
                    stop music fadeout 6
                    m sadtalk "Are you really sure I can't help?"
                    show w cry with dissolve
                    w "I... I am."
                    show w broke with dissolve
                    "God, do I really have the heart to leave him now..?"
                    play music "ost/tran.ogg" fadein 8
                    m talk "I'll ask Dr. Sharpe to have you reassigned today after work."
                    m serious "Is that okay?"
                    show w broketalk with dissolve
                    w "It's... what I wanted."
                    show w regret with dissolve
                    m bored "...."
                    "I feel like he wants to leave."
                    "I can't blame him. I'm a little shaken right now, as well."
                    show w tense with dissolve
                    m talk "Should we call it a day? If we've already decided..."
                    show w talk with dissolve
                    w "Yes. I think it's for the best."
                    scene bg mc with dissolve
                    show w full with dissolve
                    stop music fadeout 6
                    "I get up and lead him to the door slowly."
                    "This really is the last time I'll see him here..."
                    play music "ost/hospital.ogg" fadein 6
                    m sadtalk "Thank you for... all the progress we've made."
                    m regret "I hope your next psychologist will continue what I've started."
                    w "I should be thanking you, Dr. Hart, for... believing in me."
                    "His voice breaks."
                    w "I- I'm sorry- I can't... do the right thing for once."
                    w "I should go... before you start regretting this."
                    "If this really is the last time..."
                    m gasp "William. Wait..."
                    "I know I shouldn't, but I can't stop myself."
                    "I grab his hand to stop him from leaving."
                    m regrettalk "I... I don't know what to say, but..."
                    m sadtalk "I'll miss you."
                    stop music fadeout 5
                    "He looks at me, unsure of what to make of what I just said."
                    w "[name]...? What do you -"
                    hide w with dissolve
                    show drk with dissolve
                    play music "ost/ship.ogg" fadein 6
                    "I wrap my arms around him before he can even finish. Screw it."
                    w "{i}...!"
                    m neu "I mean it. I just wanted to let you know."
                    "He seems tense, but doesn't move away or do anything to push me away."
                    m sadsmile "I still believe in you."
                    "I hesitantly lay my head on his shoulder. I can feel his soft hair brushing against my face."
                    w "...."
                    "He touches my head for a moment before slowly placing his hands on my back. I relax a little."
                    w "I don't know why you would want to do something like this, but..."
                    w "Thank you. I... I appreciate it."
                    "I smile to myself. At least I could make him a little happier."
                    stop music fadeout 5
                    m serious "If you ever change your mind, I -"
                    w "I won't."
                    hide drk with dissolve
                    show w full with dissolve
                    hide screen easymeter
                    hide screen silvermeter
                    "He steps away from my suddenly and looks at me without any hint of emotion."
                    w "Goodbye, Dr. Hart."
                    m regret "...goodbye, William."
                    play sound "doorclose.ogg" fadein 1
                    hide w with dissolve
                    "I watch him leave my office for the last time."
                "Refuse":
                    stop music fadeout 6
                    m angrytalk "I... I can't leave you. Not when it's like this."
                    show w sadtalk with dissolve
                    w "No..."
                    show w scream with dissolve
                    play music "ost/tension.ogg" fadein 6
                    w "[name], don't do this to me..."
                    show w broke with dissolve
                    w "We both know... you're just prolonging my suffering..."
                    show w pain with dissolve
                    m scream "I can't... make this choice -!"
                    show w tensetalk with dissolve
                    stop music fadeout 5
                    w "You don't have to."
                    show w neutral with dissolve
                    "He stands up suddenly."
                    play music "ost/neutral.ogg" fadein 6
                    show w sidetalk with dissolve
                    w "I'll explain everything to Dr. Sharpe personally."
                    show w calm with dissolve
                    w "Thank you for your efforts, Dr. Hart."
                    play sound "doorclose.ogg" fadein 1
                    hide screen easymeter
                    hide screen silvermeter
                    scene bg mc with dissolve
                    "He leaves without another word."
                    "I... don't think I should chase after him."
            "I couldn't have done anything differently... right?"
            $route="no"
            jump patientsattack
        else:
            scene bg mc with dissolve
            if easymeter:
                show screen easymeter
                show screen silvermeter
            "Despite everything, I want to keep seeing him today."
            "I feel like there's still hope for him."
            scene bg mcdesk with dissolve
            show w siden with dissolve
            "He enters my office without a word."
            "That's uncharacteristic of him..."
            m fab "William?"
            show w talk with dissolve
            w "What?"
            show w neutral with dissolve
            m neu "...Are you okay?"
            show w sidesmile with dissolve
            w "Do I seem okay?"
            "...He doesn't, to be honest."
            m uncom "Umm... how are you feeling today? I know the weekend must've been-"
            show w talk with dissolve
            w "Do you really want to know?"
            show w neutral with dissolve
            m angry "Of course I do."
            show w sidetalk with dissolve
            w "I feel nothing. Absolutely nothing."
            show w siden with dissolve
            "...."
            m serious "Since when?"
            show w sidetalk with dissolve
            w "Since Friday."
            show w siden with dissolve
            m talk "Do you really... not want to talk to me like you used to?"
            m confusion "If you gave me another chance, I could-"
            show w talk with dissolve
            w "It's pointless. Can't you see?"
            show w calm with dissolve
            w "There's nothing you can do anymore. Just leave me be."
            show w calm with dissolve
            m sjw "I won't!"
            show w neutral with dissolve
            w "You won't have a choice soon."
            show w frusttalk with dissolve
            w "I'll be gone before you know it."
            show w calmsmile with dissolve
            "!!!"
            m angrytalk "Don't say that!"
            show w talk with dissolve
            w "Why? Are you too sensitive to even hear me talk about it?"
            show w frustsmile with dissolve
            w "You really are pathetic, [name]. So pathetic I can't believe I ever trusted you."
            show w calm with dissolve
            "This can't be how he really feels... what's happened to him?"
            m sadtalk "What's wrong, William?"
            show w angrytalk with dissolve
            w "\"What's wrong?\"? Is that a joke?"
            show w talk with dissolve
            w "Isn't it obvious? You can't help me, [name]. Nobody can."
            show w paintalk with dissolve
            w "It really isn't personal. I wouldn't want to hurt your precious feelings."
            show w angrytalk with dissolve
            w "You think you're in pain right now? That I did something horrible because I rejected your help?"
            show w calm with dissolve
            w "You can't be serious... You are the last person to ever let me down, and you think you're the victim?"
            show w frust with dissolve
            w "Don't lie to me - I know that's what you think. You're just worried about failing."
            show w paintalk with dissolve
            w "You don't even care if I die here. You said all those lies just to make me trust you..."
            show w angry with dissolve
            m sjw "That's not true! You know it's not true, you trusted me..."
            show w talk with dissolve
            w "And I was wrong."
            show w siden with dissolve
            m confusion "...."
            "...I want to cry. What have I done to lose his trust?"
            m regrettalk "William... Are you really sure you can't trust me again?"
            show w angrytalk with dissolve
            w "Look at yourself. You don't look like you can help anyone."
            show w sidetalk with dissolve
            w "...Especially me."
            show w frust with dissolve
            "...."
            show w talk with dissolve
            w "This is the last time I'll ever talk to you here. Don't even bother trying tomorrow."
            show w neutral with dissolve
            "He falls silent and I have no words left to say."
            "I wait a while before letting him go."
            "I suppose this is a goodbye."
            scene black with dissolve
            hide screen easymeter
            hide screen silvermeter
            "I spend the break in my office again and pick a random patient for my second session."
            "...Again."
            "Why am I still here?"
            $SilverRouteBroken=True
            jump nextday
    elif day == 16:
        if ShadowTalk:
            scene black with dissolve
            "I had another weird nightmare..."
            "Could it be because of the shadow?"
            play music "ost/tension.ogg" fadein 6
            scene bg patients with dissolve
            "I don't want to look at him. I just want to ask him the rest of my questions and be done with it."
            "A cold chill runs down my spine suddenly. I feel like he's watching me."
            scene bg central with dissolve
            "I can't begin to imagine how I plan to deal with this... {i}thing."
            "Before yesterday, I was sure William was just worrying too much... but..."
            "How the hell do I make this thing disappear?"
            "If it got to the point where my shadow almost acted as a seperate person, I don't think I would have the strength to accept it as a part of me."
            "It seems so much simpler than a split personality, but this one is unlike anything I've ever seen before."
            scene bg offices with dissolve
            "I glance at the door to Dr. Sharpe's office."
            "I doubt he even suspects this thing's existence."
            scene bg mc with dissolve
            "I take a deep breath. I can start whenever I'm ready."
            $renpy.pause()
            scene bg mcdesk with dissolve
            "This time he doesn't even bother to look like William when he enters my office."
            show bg mcdeskdark with dissolve
            show w s1 with dissolve
            play music "ost/shadow.ogg" fadein 6
            show es s 
            sh "{b}Hello again."
            m angry "I would say it's good to see you again, but I don't like lying."
            show w s4 with dissolve
            sh "{b}Oh, how \"good\" of you. Is that what you call morality?"
            show w s2 with dissolve
            m fab "What do you know about morality? Do you consider yourself evil?"
            m talk "William seems to believe you are."
            show w s4 with dissolve
            sh "{b}And do you consider yourself \"good\"?"
            show w s3 with dissolve
            m angry "You're reflecting the question. What I believe is none of your business."
            show w s4 with dissolve
            sh "{b}And what do you believe in?"
            sh "{b}\"Believing\" is a very human thing to do."
            show w s2 with dissolve
            m fabtalk "That's probably why you can't understand it."
            show w s4 with dissolve
            sh "{b}Are you saying I'm not human?"
            show w s3 with dissolve
            m talk "Are you?"
            show w s4 with dissolve
            sh "{b}That depends on your definition. What is a human being?"
            show w s2 with dissolve
            menu:
                "A human is someone who knows they exist":
                    show w s1 with dissolve
                    sh "{b}I know we both exist. Then I am human as well."
                "A human is someone who thinks and affects the world around them":
                    show w s4 with dissolve
                    sh "{b}I think and right now, I'm affecting you..."
                    show w s2 with dissolve
                    m fab "Don't flatter yourself."
                    show w s4 with dissolve
                    sh "{b}...So right not I am human."
                "Save the pointless questions for someone who has too much time to spare":
                    show w s1 with dissolve
                    sh "{b}Very well."
                    show w s4 with dissolve
                    sh "{b}I see you lack the ability to even define what you are."
            show w s2 with dissolve
            m talk "I had questions for you."
            show w s4 with dissolve
            sh "{b}Start then. We both know why we're here."
            show w s2 with dissolve
            m fabtalk "William said you're responsible for the thoughts he doesn't want to have. Why?"
            show w s1 with dissolve
            sh "{b}You don't get it at all, do you?"
            show w s4 with dissolve
            sh "{b}No matter how hard he may try to get rid of me, he can't stop himself from doubting every slightly more optimistic thought that occurs to him."
            sh "{b}And when he feels doubt, he blames me."
            show w s1 with dissolve
            sh "{b}After all... it's easier to blame everything on something he claims not to have control over than to admit he's just meant to think this way."
            show w s3 with dissolve
            sh "{b}This is why I exist. I'm a way of hiding everything he doesn't like about himself under one name."
            show w s4 with dissolve
            sh "{b}If he couldn't do that, everything he believes about himself would shatter."
            show w s2 with dissolve
            m serious "...William said that it's better if you don't think about me at all. That... it wouldn't be good for you to focus on me."
            m talk "What did he mean by that?"
            show w s4 with dissolve
            sh "{b}You really don't realize it yet?"
            sh "{b}Let me tell you about the last time I was interested in someone more than the others."
            show w s1 with dissolve
            sh "{b}Marie. She was really pretty."
            show w s3 with dissolve
            sh "{b}...At least, that's what he thought."
            m fabtalk "Can you actually develop feelings for someone he's not attached to?"
            show w s4 with dissolve
            sh "{b}I don't \"feel\" anything. I can't care about anyone."
            show w s2 with dissolve
            sh "{b}He's the one who cares. I'm just a reflection of these feelings."
            m talk "What about Marie?"
            show w s1 with dissolve
            sh "{b}Ah, Marie... she cared a lot. I could see it in her eyes when she'd look at him."
            show w s4 with dissolve
            sh "{b}Actually..."
            sh "{b}Do you know why it was so easy for him to let you help him?"
            show w s1 with dissolve
            sh "{b}You remind him of her."
            show w s3 with dissolve
            sh "{b}Same eyes, same hair color, same... attitude."
            show w s4 with dissolve
            sh "{b}You're almost as desperate to help him as she was."
            show w s2 with dissolve
            sh "{b}...but I digress."
            show w s4 with dissolve
            sh "{b}He told you he started \"questioning his feelings for her\". That's putting it very mildly, typical for him."
            show w s1 with dissolve
            sh "{b}Let me tell you where I came from."
            show w s2 with dissolve
            sh "{b}He wanted her. More than anyone else."
            show w s4 with dissolve
            sh "{b}She was just too kind, too beautiful... too perfect."
            sh "{b}He craved to destroy it all, just because he hated himself so much."
            show w s1 with dissolve
            sh "{b}You can imagine that with his sense of morality, the thought of fucking his own cousin didn't seem very \"right\"."
            show w s4 with dissolve
            sh "{b}...Where are my manners? Pardon my language, there's no better way to describe it."
            show w s3 with dissolve
            m uncom "...."
            show w s4 with dissolve
            sh "{b}What is is? Are you too \"sensitive\" to keep listening to this?"
            show w s1 with dissolve
            sh "{b}You were the one who asked to see me. And I'm just starting to have fun."
            show w s3 with dissolve
            sh "{b}That's why I exist. Because of her."
            show w s4 with dissolve
            sh "{b}He would never tell you that, but he wanted to hate her after she found out."
            sh "{b}He hated his family. He hated everyone."
            show w s2 with dissolve
            sh "{b}But he still hates himself the most. That's why he couldn't let you help himself."
            show w s1 with dissolve
            sh "{b}Oh, he's desperate, he really is..."
            m uncom "Does he... hate me as well?"
            show w s4 with dissolve
            sh "{b}He? Why would he hate you?"
            show w s3 with dissolve
            m neu "Do you hate me, then?"
            show w s4 with dissolve
            sh "{b}I have no reason to hate you, or feel any other way about you."
            show w s1 with dissolve
            sh "{b}That doesn't mean I wouldn't want to watch you suffer, though."
            m serious "So what does it mean if you focus on me?"
            scene bg mcdark with dissolve
            show w sc3 with dissolve
            show es c
            "He leans in, getting uncomfortably close to me again."
            show w sc4 with dissolve
            sh "{b}Don't you realize it, [name]?"
            sh "{b}Are you really clueless and innocent enough not to understand it?"
            show w sc3 with dissolve
            sh "{b}I am not just hatred..."
            "I can feel his breath on my ear. I can't find the strength to push him away."
            show w sc4 with dissolve
            sh "{b}I am lust."
            sh "{b}I am everything he doesn't want to admit lurks within him."
            show w sc2 with dissolve
            sh "{b}And you... you affect him more than anyone else right now."
            show w sc3 with dissolve
            stop music fadeout 6
            sh "{b}He would likely die before doing this, but..."
            hide es c
            hide w sc3 with dissolve
            show mcshock
            "He gets even closer and places his hand firmly on my shoulder."
            m no "{i}!!!"
            "I feel his lips on my neck."
            sh "{b}...he wants it. That and much more."
            scene bg mcdeskdark
            show w s5 with hpunch
            show es s
            "I regain reason suddenly and push him away with a force that makes him stumble back in his chair."
            show w s1 with dissolve
            play music "ost/shadow.ogg" fadein 6
            "He laughs."
            show w s4 with dissolve
            sh "{b}Oh, you have no idea what you've just done."
            show w s2 with dissolve
            sh "{b}You're only making it worse by pushing me away."
            m sjw "W-What? Don't play games with me, what do you mean?"
            show w s4 with dissolve
            sh "{b}So you really want to know? How unfortunate for him..."
            show w s3 with dissolve
            sh "{b}He doesn't want to hurt you. Unlike me, he doesn't really want to hurt anyone."
            show w s2 with dissolve
            sh "{b}But... if it was the other way around..."
            show w s4 with dissolve
            sh "{b}He wouldn't stop you."
            show w s3 with dissolve
            sh "{b}I suppose if you feel powerless your whole life, you grow to enjoy it."
            m shock "E-Excuse me?"
            show w s1 with dissolve
            sh "{b}If he could, he would beg you to do it again. And I'm supposed to be the sick one..."
            "I don't know what to make of what I just learned."
            m serious"When you said you would hurt me if you could yesterday, did you mean... um..."
            "I can't force myself to say that."
            show w s4 with dissolve
            sh "{b}...Are you asking me if I would want to-"
            show w s3 with dissolve
            m wut "Yes."
            show w s1 with dissolve
            sh "{b}Of course I would, [name]."
            m talk "Because you would enjoy it, or only to hurt William?"
            show w s4 with dissolve
            sh "{b}...Both."
            show w s1 with dissolve
            sh "{b}I can't imagine anything that could hurt him more than that, but... I dare say I would enjoy it as well."
            sh "{b}...Seeing you in fear of what I'm about to do to you..."
            sh "{b}I would go into detail about it, but it all depends on the circumstances, which I can't predict. I'm not all-knowing, after all."
            show w s3 with dissolve
            "...."
            m angrytalk "He wouldn't let you hurt me."
            show w s4 with dissolve
            sh "{b}You think so? Then why didn't he stop me just now?"
            show w s2 with dissolve
            m shock "B-Because..."
            show w s1 with dissolve
            sh "{b}This is just great. You can't even justify that."
            show w s2 with dissolve
            sh "{b}I wonder what would happen if I did something more... violent. Would you just give up defending him?"
            show w s4 with dissolve
            sh "{b}I didn't expect you to break so easily... You disappoint me."
            show w s3 with dissolve
            sh "{b}...."
            show w s1 with dissolve
            sh "{b}How could I forget? You had another dream last night, didn't you?"
            "I nod."
            show w s4 with dissolve
            sh "{b}Yes... I remember..."
            show w s1 with dissolve
            sh "{b}I was there, too."
            show w s4 with dissolve
            sh "{b}Do you know what that means?"
            show w s2 with dissolve
            m frust "...."
            show w s4 with dissolve
            sh "{b}Think, [name]. What do you think he was so afraid of after last time?"
            show w s3 with dissolve
            "The realization hits me suddenly."
            m shock "You... You can affect my dreams..."
            show w s4 with dissolve
            sh "{b}And do you know what that means, [name]?"
            show w s3 with dissolve
            sh "{b}He never told you why the nightmares that haunt him terrify him so much."
            show w s2 with dissolve
            sh "{b}It's because in his dreams, I'm the one in control. I always am."
            show w s1 with dissolve
            sh "{b}And he can't do anything but watch."
            sh "{b}He does things he never would do on his own in these dreams."
            show w s4 with dissolve
            sh "{b}That's why he hates these dreams so much - because he wakes up not knowing if he didn't actually enjoy some of it."
            sh "{b}You know what that means for you?"
            show w s1 with dissolve
            sh "{b}If I end up in your dream somehow... You better run."
            m serious "Is that even possible?"
            show w s4 with dissolve
            sh "{b}Well... I've been growing stronger recently."
            sh "{b}And I've been getting closer to you with every dream... Who knows?"
            show w s1 with dissolve
            sh "{b}You look upset. You're scared?"
            m angrytalk "No. I'm more worried about William."
            show w s4 with dissolve
            sh "{b}I don't understand... Why do you want so desperately to help him?"
            show w s2 with dissolve
            sh "{b}He can't do anything to for you in return, and you'd get paid regardless of your progress with him."
            show w s4 with dissolve
            sh "{b}So why risk your life and your happiness to help someone who can't even appreciate it?"
            show w s3 with dissolve
            sh "{b}What reason is there in this? It's pointless."
            m fabtalk "It's not."
            show w s4 with dissolve
            sh "{b}Then why?"
            show w s2 with dissolve
            menu:
                "Because I care about him":
                    $personal+=2
                    show w s3 with dissolve
                    sh "{b}You \"care\" about him."
                    show w s1 with dissolve
                    sh "{b}...how interesting."
                    show w s4 with dissolve
                    sh "{b}And why do you care?"
                    sh "{b}Why do you care what happens to him?"
                    show w s2 with dissolve
                    sh "{b}He's just another meaningless human being in your path."
                    sh "{b}You could just..."
                "Because I need to help him":
                    $personal+=1
                    show w s4 with dissolve
                    sh "{b}You \"need to\"?"
                    show w s5 with dissolve
                    sh "{b}That's certainly an odd way to put it."
                    show w s2 with dissolve
                    sh "{b}Unless..."
                "I have no reason to tell you that":
                    $professional+=2
                    show w s4 with dissolve
                    sh "{b}Hmph! Such arrogance."
                    show w s2 with dissolve
                    sh "{b}I'm being honest here, answering your questions, and you pay me back with that..."
                    show w s4 with dissolve
                    sh "{b}So be it. I'll know it either way."
                    show w s2 with dissolve
                    sh "{b}Let's see... The only reason for you to help him would be..."
            show w s4 with dissolve
            sh "{b}Ah! Of course, how could I forget?"
            show w s1 with dissolve
            sh "{b}It's guilt. You're repaying someone else for failing them."
            show w s3 with dissolve
            sh "{b}Am I right?"
            m regret "...."
            show w s1 with dissolve
            sh "{b}Of course I am."
            show w s4 with dissolve
            sh "{b}It's the only reason why you'd ever help him so selflessly. It's so painfully human, too..."
            show w s1 with dissolve
            sh "{b}So he's not even the reason why you want so desperately to help him... Oh, he would be devastated if he knew..."
            m angrytalk "That's not true. I'm doing this because I want him to be happy."
            m sjw "And you can't stop me!"
            show w s3 with dissolve
            "I barely keep myself from slamming my hands on the desk."
            "He's my real enemy. I have every right to hate him for what he's done to William."
            m angry "Now..."
            show w s2 with dissolve
            "I look at him and regain a neutral expression."
            stop music fadeout 5
            m fabtalk "With all due respect..."
            m angrytalk "{i}BEGONE."
            show w s3 with dissolve
            sh "{b}...."
            play music "ost/tension.ogg" fadein 6
            show w s4 with dissolve
            sh "{b}Before I do that... Don't you have anything else to ask?"
            show w s2 with dissolve
            m talk "No. I know everything I need from you."
            "He didn't disappear like he should have... what's wrong?"
            "I can't panic right now, I can't lose control over him..."
            show w s4 with dissolve
            sh "{b}Then let me tell you something."
            show w s2 with dissolve
            sh "{b}If I somehow ended up hurting you..."
            show w s4 with dissolve
            sh "{b}The pain would be too much for him. It would drive him to kill himself."
            show w s3 with dissolve
            sh "{b}Don't listen to him if he denies it - he wouldn't last a second if he had to look at you after that."
            show w s2 with dissolve
            sh "{b}He would rather die if that happened."
            sh "{b}...."
            show w s4 with dissolve
            sh "{b}That's all I had to say."
            show w s1 with dissolve
            stop music fadeout 5
            sh "{b}Farewell, for now."
            hide es s with dissolve
            show w sb with dissolve
            $renpy.pause(2,hard=True)
            show bg mcdesk with dissolve
            show w calm with dissolve
            "He's back..?"
            show w pain with dissolve
            "It's like he's just starting to remember what happened..."
            play music "ost/tension.ogg" fadein 4
            show w shock with dissolve
            w "{i}[name]-?"
            show w fear with dissolve
            m uncom "Are you okay?"
            w "....."
            play sound "doorclose.ogg" fadein 1
            scene mc with dissolve
            "He runs away without a word."
            "I... think he needs time to process what just happened."
            "So do I, to be honest."
            jump breakchoice
        else:
            scene bg mcdark with dissolve
            "William stays true to his word from yesterday."
            "He barely says anything the whole session."
            "I'm starting to doubt if there's even a point to this anymore... if he's not willing to talk to me."
            jump nextday
    elif day == 17:
        if ShadowTalk:
            scene bg mc with dissolve
            if easymeter:
                show screen easymeter
                show screen silvermeter
            play sound "knock2.ogg"
            play music "ost/tension.ogg" fadein 6
            "I hear a knock on my door."
            m fabtalk "Come in."
            w "Can I... not..?"
            m conf "There's nothing to be afraid of. You can enter."
            "He opens the door hesitantly and sits by my desk."
            scene bg mcdesk with dissolve
            show w regret with dissolve
            stop music fadeout 5
            "I'm so glad to actually see him today and not... {i}that thing."
            m talk "It's been a while."
            play music "ost/hospital.ogg" fadein 6
            m conf "I missed you."
            show w shock with dissolve
            w "You... you missed... me?"
            show w fear with dissolve
            m sadsmile "For the past two days, I only talked to... him. And that wasn't very pleasant."
            show w frusttalk with dissolve
            w "...Oh."
            show w regrettalk with dissolve
            w "I... I really don't know what to say about what happened..."
            show w sadtalk with dissolve
            w "I'd rather just forget these last two days..."
            show w regret with dissolve
            m talk "I get it."
            m conf "Well, at least now that's over and we won't have to mention most of what he said again."
            show w frust with dissolve
            w "...."
            show w frusttalk with dissolve
            w "...No."
            show w tensetalk with dissolve
            w "I have to say something... It won't leave me alone."
            stop music fadeout 5
            show w regrettalk with dissolve
            w "I apologize if... he said or did anything to hurt you... I'm really sorry."
            show w pain with dissolve
            menu:
                "It's okay":
                    $SilverHeart+=1
                    show drk with Dissolve(0.75)
                    show s 1 with dissolve
                    show s 2 with Dissolve(1.0) 
                    $renpy.pause(0.75, hard = True)
                    hide s with dissolve
                    hide drk with dissolve
                    show w sadtalk with dissolve
                    w "Are... you sure of it?"
                    show w regret with dissolve
                    m conf "Absolutely. I get that it's not your fault."
                "Are you?":
                    show w regrettalk with dissolve
                    w "I... I..."
                    show w tensetalk with dissolve
                    w "I couldn't do anything to stop him, I swear."
                    show w pain with dissolve
                    m confusion "...."
                    "Regardless of what they both say, I decide to keep everything that happens in mind."
            play music "ost/tension.ogg" fadein 6
            show w paintalk with dissolve
            w "It's... I'm sorry, it's just that..."
            show w angry with dissolve
            w "That didn't go as I thought it would."
            show w regrettalk with dissolve
            w "And... I had trouble pulling him back yesterday... that's not how it was supposed to be."
            show w paintalk with dissolve
            w "I... I know that failed, I'm so sorry..."
            show w hiden with Dissolve(1.0)
            "He hides his face in his hands."
            m sad "...."
            "I need to help."
            m confusion "William..."
            "I try to reach out to him, but he only moves further away from me."
            w "D-Don't..."
            w "Get away from me. You heard what he said."
            "It seems he won't let me help."
            m serious "I'm sorry, but I have to ask you somethings... just to clarify what I've heard."
            show w sad with Dissolve(1.0)
            "He looks at me hesitantly. There's so much pain in his eyes..."
            "It's like he's a completely different person than the one I just talked to yesterday."
            m talk "Can I believe everything he said?"
            show w frusttalk with dissolve
            w "He... he might've said some things just to scare you, but... he has no reason to lie to you."
            show w tensetalk with dissolve
            w "I can't hear his thoughts, I'm not even sure if he has any, so I can't tell."
            stop music fadeout 4
            show w talk with dissolve
            w "I don't think he did, though."
            show w regret with dissolve
            w "...."
            play music "ost/neutral.ogg" fadein 8
            show w regrettalk with dissolve
            w "You... you can ask me about specific things he said, then I might be able to help."
            show w regret with dissolve
            m fab "How did the switching into him occur? Did it take a while?"
            show w talk with dissolve
            w "A little, yes. I had to really focus for a moment."
            show w regrettalk with dissolve
            w "Once he was free, it... was a lot easier."
            show w tense with dissolve
            m neu "I see."
            m fabtalk "How conscious were you of everything that happened?"
            show w tensetalk with dissolve
            w "At the time, I saw and heard everything."
            show w frusttalk with dissolve
            w "I think now I'm... trying to forget that."
            show w sidetalk with dissolve
            w "It's a little blurry."
            show w siden with dissolve
            m talk "How did you feel after you were back?"
            show w frusttalk with dissolve
            w "Horrible. Once I started to realize everything I've said and done..."
            show w tensetalk with dissolve
            w "I spent the entire afternoon getting myself to calm down. I still haven't."
            show w frust with dissolve
            m regrettalk "I'm sorry if it caused you to feel that way..."
            show w angrytalk with dissolve
            w "Stop it. I'm the one who failed you."
            show w paintalk with dissolve
            w "You should be yelling at me right now, not apologizing to me."
            show w pain with dissolve
            m angry "I don't want to yell at you... I have no reason to."
            show w frust with dissolve
            w "...."
            m serious "How do you feel?"
            show w frusttalk with dissolve
            w "Should I be honest?"
            show w tense with dissolve
            "I nod."
            show w talk with dissolve
            w "Like my heart is being continously stabbed for the past two hours or so."
            show w sidetalk with dissolve
            w "And before you ask, there's nothing you can do about it."
            show w paintalk with dissolve
            w "I asked for this by letting you see him."
            show w regret with dissolve
            m regret "...."
            "I... don't know what to do."
            show w talk with dissolve
            w "You had things to ask. Don't bother trying to make me feel better and get to the point."
            show w neutral with dissolve
            stop music fadeout 5
            m talk "Is what he said about your cousins true?"
            show w regret with dissolve
            w "...."
            show w paintalk with dissolve
            w "Yes."
            show w tense with dissolve
            m neu "And the feelings he was created from?"
            show w talk with dissolve
            w "Yes."
            show w neutral with dissolve
            play music "ost/tension.ogg" fadein 8
            m uncom "Is it true that... you hate yourself?"
            show w regrettalk with dissolve
            w "Y-Yes."
            show w regret with dissolve
            m angry "Do you hate {i}me{/i}?"
            show w wrong with dissolve
            w "No!"
            show w tense with dissolve
            m serious "Was he lying about... what it means that it's focused on me?"
            show w pain with dissolve
            w "...."
            show w paintalk with dissolve
            w "...no."
            show w regret with dissolve
            m angry "William. Look at me."
            show w tense with dissolve
            m fabtalk "Do I really remind you of Marie?"
            show w fear with dissolve
            w "...."
            show w tensetalk with dissolve
            w "You... You do."
            show w regrettalk with dissolve
            w "I... I'm sorry, but you really are similar."
            show w regret with dissolve
            m smile "There's nothing to be sorry for. I'm glad it helped you to trust me."
            show w tensetalk with dissolve
            w "You shouldn't be thankful for that."
            show w sadtalk with dissolve
            w "[name], I could've hurt you yesterday."
            show w frusttalk with dissolve
            w "Why didn't you stop me?"
            show w pain with dissolve
            m confusion "I did."
            show w regrettalk with dissolve
            w "But... it was already after... I..."
            show w tsun with dissolve
            w "He wasn't supposed to act that way."
            show w frusttalk with dissolve
            w "You waited. You could've done something sooner."
            show w sadtalk with dissolve
            w "Why? Why did you wait?"
            show w sad with dissolve
            menu:
                "I was surprised":
                    show w neutral with dissolve
                    w "...."
                    show w regrettalk with dissolve
                    w "I'm sorry, I know I shouldn't blame you for this..."
                    show w hiden with Dissolve(1.0)
                    w "God, I'm doing it again... I'm blaming you for something that isn't your fault..."
                "I was scared":
                    $personal+=1
                    show w shock with dissolve
                    w "You..."
                    show w regrettalk with dissolve
                    w "I'm so sorry..."
                    show w angry with dissolve
                    w "I won't let him near you again, I promise."
                    show w regrettalk with dissolve
                    w "But for your own good, you should just avoid me."
                "I was curious":
                    $personal +=2
                    show w tensetalk with dissolve
                    w "And... was that what you expected?"
                    show w tense with dissolve
                    m neu "Not quite. It was... a lot bolder than I expected."
                    show w frust with dissolve
                    w "...."
                    show w angrytalk with dissolve
                    w "Don't ever do something like that out of curiousity..."
            show w neutral with dissolve
            "He glances at my neck briefly."
            show w tensetalk with dissolve
            w "Did... did it hurt?"
            show w regret with dissolve
            "I think back to yesterday..."
            show w tense with dissolve
            m talk "Not really. If anything, it was the shock."
            stop music fadeout 5
            show w regrettalk with dissolve
            w "...I see."
            show w regret with dissolve
            m serious "Hey, don't blame yourself. It's not like {i}you{/i} did it."
            w "...."
            show w pain with dissolve
            m neu "What is it?"
            play music "ost/hospital.ogg" fadein 6
            show w shock with dissolve
            w "N-Nothing."
            show w regret with dissolve
            "I decide to change the subject." 
            m frusttalk "He said something strange yesterday... I'm not sure if I understood it correctly..."
            show w talk with dissolve
            w "Ask then."
            show w neutral with dissolve
            menu:
                "How did you feel when I pushed you away?":
                    show w scaredblush with dissolve
                    w "I..."
                    show w disblush with dissolve
                    w "What kind of question is that?"
                    show w fear with dissolve
                    m neu "I just wanted to clarify."
                    show w frusttalk with dissolve
                    w "I... I refuse to answer that."
                    show w frust with dissolve
                "He said: \"If you feel powerless your whole life, you start to enjoy it\"":
                    show w dis with dissolve
                    w "He... He said that?"
                    show w fear with dissolve
                    m talk "What should I make of that?"
                    show w regret with dissolve
                    w "He... He's probably right."
                "...Are you a masochist?":
                    show w shock with dissolve
                    w "...!"
                    show w disblush with dissolve
                    w "I... I won't answer that."
                    show w frust with dissolve
                    "That sounds like a yes to me."
            m angrytalk "Regardless of how you feel about that, I need to know - have you ever purposely harmed yourself?"
            show w wrong with dissolve
            w "No, of course not-! I would never..."
            show w frust with dissolve
            w "Umm..."
            show w regrettalk with dissolve
            w "T-To be honest, the thought of hurting myself physically... scares me."
            show w tense with dissolve
            "I'm... somewhat relieved."
            m talk "As it should."
            show w neutral with dissolve
            m conf "As long as you don't harm anyone because of it, I don't see a problem."
            show w shock with dissolve
            w "You... You don't?"
            show w fear with dissolve
            m neu "I mean... it's not like it matters from my point of view."
            show w tsun with dissolve
            w "O-Oh..."
            show w smile with dissolve
            w "Thank you."
            show w frusttalk with dissolve
            w "I... never wanted to talk about it to anyone since..."
            show w tensetalk with dissolve
            w "I thought it was..."
            show w regrettalk with dissolve
            w "...pathetic."
            show w regret with dissolve
            "I can see why he would think that, given what he's like."
            m gasp "Would you call your shadow sadistic?"
            show w talk with dissolve
            w "definitely."
            show w neutral with dissolve
            m fabtalk "So it's as he said - you're like two sides of the same coin."
            stop music fadeout 5
            show w regrettalk with dissolve
            w "...maybe."
            show w frust with dissolve
            m talk "There's one more thing, William."
            show w talk with dissolve
            w "What is it?"
            show w tense with dissolve
            play music "ost/tension.ogg" fadein 8
            m regrettalk "I... had another dream with him in it. And this time... he seemed closer."
            show w shock with dissolve
            w "What... What happened?"
            show w fear with dissolve
            "I tell him about my dream."
            show w tensetalk with dissolve
            w "He... He pulled you back into the water?"
            show w tense with dissolve
            m neutral "That's right."
            show w talk with dissolve
            w "And you drowned?"
            show w frust with dissolve
            m uncom "I'm not sure."
            show w regrettalk with dissolve
            w "That's... one dream could've been a coincidence, but this..."
            show w tensetalk with dissolve
            w "You... You're on your own, [name]."
            show w regrettalk with dissolve
            w "There's nothing I can do to stop him like this." 
            show w sadtalk with dissolve
            w "I'm sorry, but I can't protect you from him."
            show w sad with dissolve
            m frust "...Right."
            show w frusttalk with dissolve
            w "I... I knew I shouldn't have let you talk to him..."
            show w paintalk with dissolve
            w "Now there's really nothing either of us can do."
            show w pain with dissolve
            "Well that's reassuring..."
            m serious "Do you think he's actually capable of physically being in my dream?"
            show w talk with dissolve
            w "Judging by last week alone, he could be."
            show w frust with dissolve
            m sad "Would you really be unable to stop him if he ever... tried to hurt me?"
            show w regrettalk with dissolve
            w "I'm afraid I would be."
            show w sad with dissolve
            m regrettalk "And... is he really as close to taking over permanently as he said he is?"
            stop music fadeout 4
            show w sadtalk with dissolve
            w "I... I didn't want to tell you that, [name]... didn't want to worry you, but... I think so."
            show w regrettalk with dissolve
            w "I've feared it would come eventually, but... I wasn't prepared for it to be this soon."
            show w broke with dissolve
            play music "ost/emo.ogg" fadein 8
            m sadtalk "Is there really nothing that can stop him?"
            show w tense with dissolve
            w "I... I don't..."
            show w paintalk with dissolve
            w "No. There isn't."
            show w regret with dissolve
            m sjw "There must be a way."
            show w pain with dissolve
            m sad "Please, the most important thing is not to lose hope. You have to give me time to at least try."
            m angrytalk "I won't give up, I swear."
            stop music fadeout 4
            show w tensetalk with dissolve
            w "Is that... a promise?"
            show w frust with dissolve
            m conf "If it has to be, then yes. I promise."
            play music "ost/hospital.ogg" fadein 5
            show w regretsmile with dissolve
            w "That... I know it's irrational, but somehow that makes me hopeful."
            show w smile with dissolve
            w "...thank you for everything, [name]."
            show w sidetalk with dissolve
            w "I should go now. It's almost time for your break."
            show w neutral with dissolve
            m "I'll see you tomorrow, William. Take care of yourself."
            hide screen easymeter
            hide screen silvermeter
            play sound "doorclose.ogg" fadein 1
            scene bg mc with dissolve
            "He nods and leaves."
            jump patientsattack
        else:
            $SilverRouteBroken=True
            scene bg mcdark with dissolve
            "This is our third session this week, and he still haven't said anything."
            "He really doesn't want to cooperate... what should I do?"
        jump patientsattack
    elif day == 18:
        jump breakevent1
    elif day== 19:
        jump breakevent2
    elif day == 20:
        scene black with dissolve
        "...."
        scene bg mcbed with Dissolve(1.0)
        "I just had another dream about the shadow."
        "William's warned me of this... should I be worried?"
        scene black with dissolve
        nt "Wait... what was that at the end of the dream? A glowing pair of eyes..."
        nt "Was it the shadow? Does that mean I'll have another dream with him in it..?"
        play music "ost/emo.ogg" fadein 5
        scene bg mcliving with Dissolve(1.0)
        "I think back to the last time I talked to... that thing."
        "That was probably the most uncomfortable I've ever been."
        "I'm not sure what would happen if I were to meet him in person again."
        "I can't help but worry about it, even though it's just a nightmare."
        scene bg mclivingnight with Dissolve(1.0)
        "I still have a week until the end of my break."
        "I want to see William again..."
        "I'm worried about him, despite what that nurse told me when I called the hospital yesterday."
        play music "ost/ring.ogg"
        "Huh?"
        "Could it be from the hospital?"
        play music "ost/hospital.ogg" fadein 6
        "I pick up quickly."
        m gasp "Hello?"
        gu "{i}I'm so sorry to bother you on your break, Ms. Hart, but I have an important message to relay."
        m serious "About my patients?"
        stop music fadeout 5
        gu "{i}About William Moore."
        m shock "Wh-What happened?"
        play music "ost/tension.ogg" fadein 6
        gu "{i}He's gotten particularly... anxious today."
        m serious "Does anyone know what may have caused it?"
        gu "{i}I'm afraid not."
        m angrytalk "Has anyone tried to ask him about it?"
        gu "{i}Of course we have! But all attempts at talking to him were complete failures. He simply refuses to explain anything."
        "I remember him saying he doesn't like being bothered by the staff... that it only makes him anxious."
        "Maybe... if they left him alone, he would feel calmer... but then he could be hurt in some way without supervision."
        stop music fadeout 5
        "It's risky... what do I do..?"
        menu:
            "You should keep watching out for him":
                m angrytalk "Be especially careful. He might do something he'd regret if you stop watching him."
            "You should leave him be":
                gu "{i}Huh? Are you... sure, Ms. Hart?"
                m angry "I've spoken to him about it. Being watched only makes him more anxious."
                gu "{i}I... see."
        play music "ost/tran.ogg" fadein 6
        gu "{i}I'll let the others know. Thank you very much, Ms. Hart."
        show drk with dissolve
        nt "I hang up and think to myself..."
        nt "Was this really the right choice?"
        nt "He might still be in danger..."
        nt "I wonder what caused him to act that way. He doesn't seem to get this anxious without a reason..."
        nt "Could it be... his shadow? What if it's closer than I previously thought?"
        stop music fadeout 6
        scene black with Dissolve(1.0)
        nt "What if... it's really about to take over?"
        nt "The worst thing is that I can do nothing but watch it happen..."
        jump fullmoon
    elif day == 21:
        if moonshadowfused:
            jump nextday
        jump fullmoonmorning
## week IV ###############
    elif day == 22:
        if moonshadowfused:
            pass
        else:
            jump breakevent3
    elif day == 23:
        if moonshadowfused:
            jump nextday
        jump gmeeting
    elif day == 24:
        if moonshadowfused:
            jump nextday
        jump callhospital
    elif day==25:
        if moonshadowfused:
            jump nextday
        jump breakend
    elif day == 26:
        jump nextday
    elif day == 27:
        jump nextday
    elif day == 28:
        jump nextday
## week V ################ 
    elif day == 29:
        if moonshadowfused: ##rare bad ending
            scene black with dissolve
            nt "I can finally go back to work today."
            nt "These past few days have been such a blur... nothing happened."
            nt "No calls from the hospital, no news... maybe that nightmare really was just that - a nightmare."
            play music "ost/hospital.ogg" fadein 6
            scene bg front with dissolve
            "The air feels cold today. I hurry inside."
            show bg mcdark with dissolve
            show bg mc with dissolve
            "Alright, time to see William and prove this was just a bad dream."
            "There's no way the staff would let something like that slide - no updates means no bad news."
            play sound "doorclose.ogg" fadein 1
            show bg mcdesk with dissolve
            show w neutral with dissolve
            stop music fadeout 5
            m conf "It's so good to see you again, William."
            show w sidesmile with dissolve
            w "I'm glad you're safe."
            m gasp "Huh?"
            show w frusttalk with dissolve
            w "After all..."
            show w shadowend
            w "{b}Pushing you out of his mind like that could've killed you."
            play music "ost/shadowA.ogg" fadein 3
            m wut "!!!"
            scene black with vpunch
            "I jump up from my chair and retreat until my back hits the wall."
            m fear "You... {i}you're not... real..."
            m scream "You can't be!"
            show w sa with dissolve
            $renpy.pause(2,hard=True)
            sh "{b}Hello, [name]."
            pause 1
            stop music
            scene black
            $renpy.pause(3,hard=True)
            $renpy.quit()
label moonaftertalk:
    play music "ost/hospital.ogg" fadein 10
    scene bg offices with dissolve
    "I decide to check on William one last time before I interact with his shadow next week."
    "Honestly, it shouldn't be much different from him, but seeing how anxious he is because of it, I feel responsible."
    scene bg central with dissolve
    "I've never talked to him after work, but the situation seems to call for it."
    scene bg patients with dissolve
    "I approach the door to his room."
    scene bg closeXIX2 with dissolve
    m uncom "William?"
    w "What are you doing here?"
    m talk "I just wanted to make sure you're okay."
    w "...."
    w "You really feel responsible, don't you?"
    w "I'll be fine. I've been through worse."
    m serious "If... if you ever don't want to answer something, just turn back, okay?"
    w "I... don't think that would make much sense."
    w "I'm going to free it exactly so it can answer the things I can't."
    w "It won't be pretty."
    w "It's going to be disgustingly, brutally honest... and I'll hate it."
    w "But that's how it has to be."
    w "That's all. You should get going before I start regretting this..."
    scene bg patients with dissolve
    "I do as he says. I suppose this is a goodbye for now."
    jump nextday
label shadowaftertalk:
    scene bg offices with dissolve
    "I lock my office for the day and head home."
    scene bg patients with dissolve
    play music "ost/tension.ogg" fadein 6
    sh "Leaving already?"
    scene bg closeXIX with dissolve
    m fabtalk "It's been over four hours."
    sh "Really? I must have no sense of time, then..."
    "I look at him through the door to his room."
    "He looks just like William again and I hate it."
    "...Except for the eyes. That's the only thing giving him away."
    "They look... dead. Emotionless. Just like how his voice changed ever so slightly."
    "I guess that's to be expected."
    m angry "If you don't mind, I should be leaving now. I'll see you again tomorrow."
    sh "I can't wait, Ms. Hart. I haven't had this much fun in a while."
    scene bg patients with dissolve
    stop music fadeout 5
    "I move away from the door quickly."
    "There's something about interacting with him that makes my skin crawl..."
    scene black with dissolve
    "I make my way outside and go home at last."
    "I'm tired..."
    jump moonlight
label moonmidgameroutefail:
    m talk "I... I apologize if this is sudden, Doctor, but I have something to say."
    show d neu with dissolve
    "He looks somewhat surprised."
    show d talk with dissolve
    d "Of course, Ms. Hart. What is it?"
    show d cold with dissolve
    "I take  a deep breath. I... I know this is wrong, but..."
    "...I don't think I can take this anymore."
    m regret "I..."
    show d neu with dissolve
    m angrytalk "I quit."
    show d sad with dissolve
    d "...."
    show d regrettalk with dissolve
    d "...oh."
    show d frust with dissolve
    d "I... I understand that today's events may have been... difficult for you, but..."
    show d sad with dissolve
    m uncom "It's not about that. I... I failed."
    show d talk with dissolve
    d "Is it about your patients?"
    show d cold with dissolve
    m regret "One of them."
    m sadtalk "I... think I ruined my relationship with William Moore. He won't talk to me anymore."
    show d sadtalk with dissolve
    d "When did he stop cooperating?"
    show d frust with dissolve
    m regrettalk "Last Friday. He said... he shouldn't have trusted me at all."
    show d regret with dissolve
    d "...."
    show d talk with dissolve
    d "I know he can be a little... difficult. William is a very sensitive patient."
    show d sadtalk with dissolve
    d "You should not blame yourself for this. But... it really is as you say..."
    show d frust with dissolve
    "He hesitates."
    show d coldtalk with dissolve
    d "Are you sure you do not want to keep working here? I can assign a different patient to you in his place."
    show d cold with dissolve
    "It's... irrational, but... I don't think I could handle staying here, having to look him in the eyes and know how much I've failed him."
    m sad "No. I don't think I can keep working here... After what happened."
    show d regret with dissolve
    d "I am terribly sorry for everything that happened. It is very unfortunate to hear you want to quit so soon."
    show d talk with dissolve
    d "But... you should have told me before. If you asked me for help last Friday, maybe it would be different now."
    show d neu with dissolve
    "...."
    "That didn't even occur to me."
    show d neutral with dissolve
    m frusttalk "I'm sorry. I know I should've done something about it sooner..."
    show d sad with dissolve
    d "No, you are not to blame, Ms. Hart. I know it must have been difficult for you."
    show d sidetalk with dissolve
    d "And... that such delicate matters are hard to discuss sometimes."
    show d frust with dissolve
    "He's right."
    show d frusttalk with dissolve
    d "William did seem a little... different, the last time I saw him here."
    show d regret with dissolve
    d "I... did not think to draw any conclusions based on his behavior. With a patient like him, it is difficult to predict what exactly causes him anxiety."
    show d talk with dissolve
    d "Regardless, I feel personally responsible for everything that happened to you recently."
    show d coldtalk with dissolve
    d "If you want to quit because of it, I will not stop you."
    show d neutral with dissolve
    m regret "...."
    m pity "Thank you, Doctor. It's very considerate of you."
    show d grieftalk with dissolve
    d "There is no need to thank me."
    show d neutalk with dissolve
    d "If you are really sure, I will make sure William gets all the help he needs after you leave."
    show d sidetalk with dissolve
    d "He may claim he regrets trusting you now, but it could still affect him negatively to see you leave the hospital."
    show d frust with dissolve
    m regret "...."
    "I feel increasingly that this is my fault."
    m serious "Is there... anything I can do to help? I don't think he wants to see me right now, but..."
    show d cold with dissolve
    "He looks at me for a moment in silence, studying me."
    show d neutalk with dissolve
    d "Ms. Hart?"
    show d neutral with dissolve
    m gasp "Yes?"
    show d sidetalk with dissolve
    d "Could you answer one question before you leave..?"
    show d frust with dissolve
    m talk "Of course."
    show d coldtalk with dissolve
    d "Were you two... close?"
    show d neutral with dissolve
    m shock "...."
    menu:
        "Yes":
            $personal+=2
            m regrettalk "Yes, we were."
            show d cold with dissolve
            m sad "But... I don't think we are anymore."
            show d regret with dissolve
            d "...."
            show d grieftalk with dissolve
            d "I am very sorry to hear that."
            show d sadtalk with dissolve
            d "These past few days must have been horrible for you. The pain of losing someone close to you is something very few can handle."
            show d foc with dissolve
            d "...."
            show d regrettalk with dissolve
            d "If you want, I can let you see him for one last time before you leave."
            show d foctalk with dissolve
            d "Maybe hearing that you want to leave will make him more willing to talk."
            show d sadtalk with dissolve
            d "...Do you want to say goodbye to him?"
            show d neutral with dissolve
            "I wouldn't have expected him to be this... compassionate about it."
            "Do I really want to see William again..?"
            "This may not be the best time, but I remind myself I'll never see him after this."
            menu:
                "I want to see him":
                    show d sad with dissolve
                    m sadtalk "If that's possible."
                    show d talk with dissolve
                    d "Whatever you wish for, Ms. Hart. I hope this is enough of an apology for what happened today."
                    show d frust with dissolve
                    m regret "...."
                    show d regrettalk with dissolve
                    d "Are you in the state to walk yet?"
                    show d cold with dissolve
                    m uncom "I think so..."
                    "I get up and we leave his office."
                    show bg offices with dissolve
                    show d regret with dissolve
                    d "...."
                    "He's eerily silent. It probably isn't the most typical situation to be in, anyway."
                    show d cold with dissolve
                    m sad "I'm sorry to bother you with that request..."
                    show d frusttalk with dissolve
                    d "It really is all I can do for you, Ms. Hart."
                    scene black with dissolve
                    "I remember to take the things I've left in my office..."
                    scene bg mc with dissolve
                    "...."
                    scene bg offices with dissolve
                    show d talk with dissolve
                    d "Are you ready to leave?"
                    show d neutral with dissolve
                    "I nod."
                    show bg central with dissolve
                    show d sidetalk with dissolve
                    d "I will not disturb you, Ms. Hart. I know it must be difficult as it is for you."
                    show d neu with dissolve
                    m boresmile "Thank you."
                    show bg patients with dissolve
                    show d talk with dissolve
                    d "This is it... Do you want me to tell him you are leaving?"
                    show d neutral with dissolve
                    m angry "I think I'd rather do it on my own."
                    show d neutalk with dissolve
                    d "I see."
                    hide d with dissolve
                    "He leaves me be, but remains at a distance from which he can see me in case I need anything from him."
                    scene bg closeXIX with Dissolve(1)
                    m serious "William..?"
                    m regrettalk "It's... It's me, [name]..."
                    "...."
                    m angry "I'm... quitting my job. I just thought I should... let you know."
                    "I preparing to hear no response again, but he suddenly approaches the door and I can see him again."
                    show bg closeXIX2 with dissolve
                    "I look up at him through the glass."
                    w "What did you say..?"
                    m regret "I'm leaving, William. I can't keep working here."
                    w "Because of me...?"
                    m sadtalk "Yes."
                    w "...."
                    "He looks away from me."
                    w "Why would you... do that?"
                    m regret "You... You wanted me to leave you be, didn't you..?"
                    w "{i}No!"
                    w "I... I never thought you would... really leave..."
                    "His breath tells me it's getting worse."
                    "I glance at Dr. Sharpe before looking back at William."
                    m serious "Can I come in?"
                    w "...no."
                    w "I shouldn't... be in one room with you right now..."
                    m sadtalk "William, I'm sorry..."
                    w "{i}Stop it."
                    w "Just... stop. {i}Don't make this any worse."
                    w "...."
                    "I don't know what to say to him, but... I don't want to leave him like that."
                    m serious "Should I leave you be..?"
                    w "...yes. You shouldn't keep talking to me."
                    m sad "...."
                    "I want to ask him something, but I remind myself this isn't one of our sessions."
                    "I'll never see him again. And yet... he just wants me to leave."
                    m regrettalk "William, I... I really-"
                    w "Don't say anything. Just go."
                    m shock "But-"
                    w "{i}Leave. Me. {b}Alone."
                    "...."
                    m sadtalk "Goodbye, William. I'm sorry it had to be that way."
                    stop music fadeout 4
                    "I step away from the door. This is the last time he'll ever tell me to leave him be."
                    scene black with Dissolve(1.0)
                    "I'll really never... see him again."
                    jump moonmidgamedeath
                "I'd rather not":
                    show d calmtalk with dissolve
                    d "I understand."
                    show d talk with dissolve
                    d "You are free to leave, Ms. Hart. I will settle the formalities later."
                    stop music fadeout 6
                    show d neutral with dissolve
                    m boresmile "Thank you."
                    show d regret with dissolve
                    m sadtalk "I'm sorry it had to be that way."
                    "I don't know what I'm going to do now..."
                    jump apathyending 
        "No":
            $professional+=2
            "What kind of question is that..?"
            "Even if I knew how to answer it, I wouldn't tell him."
            "Why would he want to know such a thing?"
            show d cold with dissolve
            m fabtalk "We weren't. I don't think it would be very professional, either way."
            show d calmtalk with dissolve
            d "I see."
            show d neutalk with dissolve
            d "If it was nothing personal, it may be easier for him to move on."
    show d coldtalk with dissolve
    d "We will do our best, I promise."
    show d frusttalk with dissolve
    d "I know it may be... alarming, to say the least, to see him in the state he must be in right now, but everything should be under control."
    show d neutalk with dissolve
    d "I will assign him to one of the other psychologists immidiately and personally see him after you leave."
    show d foc with dissolve
    d "If his state really is so severe, I will ensure he cannot hurt himself in any way."
    show d cold with dissolve
    m smile "Thank you, Doctor."
    show d talk with dissolve
    d "It is my duty. Thank you for bringing this to my attention... It only pains me to hear you want to leave because of it."
    scene black with dissolve
    "The formalities didn't take long and I was soon released from the hospital."
    "For good, this time..."
    "I look back at the large building... I'll never see it again."
    jump apathyending
label moonmidgamedeath:
    scene black with dissolve
    pause 2
    "..."
    "....."
    "I deserve this."
    "{i}I deserve all of this."
    #sfx
    show blood with hpunch
    "...."
    "It's over..."
    scene black with Dissolve(3.0)
    "{i}...finally."
    $renpy.pause(4, hard=True)
    $renpy.quit()

label afterfullmoon:
    scene black with vpunch
    play music "ost/fight.ogg" fadein 3
    nt "I wake up with a gasp."
    scene bg mcbednight with Dissolve(1.0)
    nt "I'm fine. I'm safe now."
    nt "It was just a nightmare..."
    nt "But... William... said the previous ones happened to him as well..."
    nt "And... the shadow said he saw everything."
    nt "So... did it... {i}really happen..?"
    stop music fadeout 5
    nt "I can't even begin to think of the consequences of that dream, if William saw it as well. It would be..."
    play music "ost/emo.ogg" fadein 6
    nt "It would destroy him."
    nt "Oh god... if this was real, I'm in serious trouble."
    nt "I get up from my bed."
    nt "Ouch-"
    nt "My legs hurt. It's almost like someone really..."
    scene black with Dissolve(1.0)
    nt "Ugh, just reminding myself of that nightmare gives me chills."
    nt "It felt... way too real."
    nt "I can't erase the memory of his face when he was looking down at me from my mind."
    nt "That... that was... traumatizing. I think."
    nt "Especially because... it was him."
    nt"Or at least he had his face when he did all these things to me."
    stop music fadeout 4
    nt "Ugh -"
    nt "I force myself to stop thinking about it until I get back to the hospital."
    nt "I just want to sleep..."
    pause 1
    jump nextday
label fullmoonmorning:
    scene bg mcbed with Dissolve(1.0)
    "...."
    "{i}William."
    play music "ost/tension.ogg" fadein 6
    "The memories of last night's dream are flooding back all at once."
    "...All I can do now is hope it was just that - a dream."
    "There's still a small chance it wasn't like the previous nightmares - that he didn't actually see any of that."
    "Whatever happened, I would much rather live with what I saw on my own than have to deal with the consequences."
    scene bg mcliving with dissolve
    "It... it might be too late to help him now."
    stop music fadeout 5
    "Should I... call the hospital again..?"
    menu:
        "Call them":
            "I pick the number of the reception and call."
            "If I'm wrong, and I better be, they'll just think I'm a little overprotective."
            "And maybe I am, but I have to know."
            gu "Hello, Ms. Hart."
            m serious "Good morning. I know it may be sudden, but is everything okay with my patients?"
            m regrettalk "I... have a feeling something bad may have happened."
            gu "What do you mean?"
            m neu "I -"
            gu "One moment, please."
            play music "ost/tension.ogg" fadein 4
            "I hear some commotion on the other side. I can barely make out the nurse's voice."
            gu "What? Where?"
            gu "...."
            gu "Ms. Hart? Are you still there?"
            m confusion "What's going on there?"
            gu "I... I think there's something wrong with one of your patients."
            gu "I'm really sorry, I have to leave - we have this under control, Ms. Hart."
            "She hangs up abruptly and my face goes pale at the realization of what this means."
            "{i}He saw it. He saw all of it."
            "Or at least, as much as the shadow needed him to see."
            stop music fadeout 5
            "I... want to be wrong so badly, but... if something happened to him {i}today{/i}, I... can't help assuming it was that dream."
            "{i}Oh god...{/i} How can I ever make this right..?"
        "Don't":
            "I'll know once I'm back to work."
            "There's no reason to worry about something I can't fix."
            if moonsharpeknow:
                "If I had a way of contacting Dr. Sharpe directly, maybe I would be more willing to call."
    play music "ost/emo.ogg" fadein 6
    "I slump down to the couch and close my eyes."
    show drk 2 with Dissolve(1.0)
    nt "I had no doubt it would be difficult, but now..?"
    nt "I fear it's only getting worse since I started seeing him."
    nt "Sure, he opened up a lot in a rather short time - and he's been here for two years, so it's a huge step."
    hide drk with Dissolve(1.0)
    "But... what if I'm only hurting him in the process? What exactly is getting him to trust me going to accomplish?"
    "If I fail now, he'll never trust any other therapist again."
    "Or anyone at all, for that matter."
    "I hope to god Sharpe can handle whatever is going on right now."
    "...I can't lose him. I can't let him suffer because of me."
    "I just have to get back to work before something horrible can happen."
    jump janeback2
    