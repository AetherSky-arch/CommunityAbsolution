default HermitFail = False
default HermitApathyEnd = False
default Hermithonest = 0

default StarHeart=0

default Charlie51=False
default Charlie52=False
default Charlie53=False
default Charlie54=False
default CharlieEnd="bad"

image charlieforest = "cg/CharlieForest.png"

image charlie11 = "cg/Hermit11.png"
image charlie12 = "cg/Hermit12.png"

image bg charlie = "bg/Charlie.png"

image hermitkiss = "cg/CharlieKiss1.png"

image h 2neu = "sprites/hermit/2Neutral.png"
image h 2talk = "sprites/hermit/2Talk.png"
image h 2smile = "sprites/hermit/2Smile.png"
image h 2angry = "sprites/hermit/2Angry.png"
image h 2angrytalk = "sprites/hermit/2AngryTalk.png"
image h 2evil = "sprites/hermit/2Evil.png"
image h 2sad = "sprites/hermit/2Sad.png"
image h 2fool = "sprites/hermit/2Fool.png"
image h 2siden = "sprites/hermit/2Siden.png"
image h 2sidetalk = "sprites/hermit/2SideTalk.png"
image h 2sidesmile = "sprites/hermit/2SideSmile.png"
image h 2frust = "sprites/hermit/2Frust.png"
image h 2frusttalk = "sprites/hermit/2FrustTalk.png"
image h 2frustsmile = "sprites/hermit/2FrustSmile.png"
image h 2calm = "sprites/hermit/2Calm.png"
image h 2calmtalk = "sprites/hermit/2CalmTalk.png"
image h 2pain = "sprites/hermit/2Pain.png"
image h 2paintalk = "sprites/hermit/2PainTalk.png"
image h 2dead = "sprites/hermit/2Dead.png"
image h 2deadtalk = "sprites/hermit/2DeadTalk.png"
image h 2deadsmile = "sprites/hermit/2DeadSmile.png"

image hermitenter = "bg/Hermitenter.png"
image hermittruth = "cg/CharlieTruth.png"

image htc neu = "sprites/hermit/truth/Charlieneu.png"
image htc angry = "sprites/hermit/truth/Charlieangry.png"
image htc freeze = "sprites/hermit/truth/Charliefreeze.png"
image htc sad = "sprites/hermit/truth/Charliesad.png"
image htc side = "sprites/hermit/truth/Charlieside.png"
image htsmile = "sprites/hermit/truth/Charliesmile.png"
image htm neu = "sprites/hermit/truth/MCneu.png"
image htm sad = "sprites/hermit/truth/MCsad.png"
image htm gasp = "sprites/hermit/truth/MCgasp.png"

image ascare="cg/AEvent4.png"

label bluenotes:
    if month == 1:
        if day == 6 or day ==  7 or day == 13 or day == 14 or day > 17:
            jump bluenav
    if nhermit1=="":
        $nhermit1 = renpy.input("Note 1 (max 50 characters):", length = 50)
    else:
        if nhermit2=="":
            $nhermit2 = renpy.input("Note 2 (max 50 characters):", length = 50)
        else:
            if nhermit3=="":
                $nhermit3 = renpy.input("Note 3 (max 50 characters):", length = 50)
            else:
                if nhermit4=="":
                    $nhermit4 = renpy.input("Note 4 (max 50 characters):", length = 50)
                else:
                    if nhermit5=="":
                        $nhermit5 = renpy.input("Note 5 (max 50 characters):", length = 50)
                    else:
                        if nhermit6=="":
                            $nhermit6 = renpy.input("Note 6 (max 50 characters):", length = 50)
                        else:
                            if nhermit7=="":
                                $nhermit7 = renpy.input("Note 7 (max 50 characters):", length = 50)
                            else:
                                if nhermit8=="":
                                    $nhermit8 = renpy.input("Note 8 (max 50 characters):", length = 50)
                                else:
                                    if nhermit9=="":
                                        $nhermit9 = renpy.input("Note 9 (max 50 characters):", length = 50)
                                    else:
                                        if nhermit10=="":
                                            $nhermit10 = renpy.input("Note 10 (max 50 characters):", length = 50)
                                        else:
                                            if nhermit11=="":
                                                $nhermit11 = renpy.input("Note 11 (max 50 characters):", length = 50)
                                            else:
                                                if nhermit12=="":
                                                    $nhermit12 = renpy.input("Note 12 (max 50 characters):", length = 50)
                                                else:
                                                    if nhermit13=="":
                                                        $nhermit13 = renpy.input("Note 13 (max 50 characters):", length = 50)
                                                    else:
                                                        if nhermit14=="":
                                                            $nhermit14 = renpy.input("Note 14 (max 50 characters):", length = 50)
                                                        else:
                                                            if nhermit15=="":
                                                                $nhermit15 = renpy.input("Note 15 (max 50 characters):", length = 50)
                                                            else:
                                                                if nhermit16=="":
                                                                    $nhermit16 = renpy.input("Note 16 (max 50 characters):", length = 50)
                                                                else:
                                                                    if nhermit17=="":
                                                                        $nhermit17 = renpy.input("Note 17 (max 50 characters):", length = 50)
                                                                    else:
                                                                        if nhermit18=="":
                                                                            $nhermit18 = renpy.input("Note 18 (max 50 characters):", length = 50)
                                                                        else:
                                                                            if nhermit19=="":
                                                                                $nhermit19 = renpy.input("Note 19 (max 50 characters):", length = 50)
                                                                            else:
                                                                                if nhermit20=="":
                                                                                    $nhermit20 = renpy.input("Note 10 (max 50 characters):", length = 50)
                                                                                else:
                                                                                    "I've already filled up all my notes."
                                                                                    "Should I rewrite one of my notes?"
                                                                                    menu:
                                                                                        "[nhermit1]":
                                                                                            $nhermit1 = renpy.input("Note 1 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit2]":
                                                                                            $nhermit2 = renpy.input("Note 2 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit3]":
                                                                                            $nhermit3 = renpy.input("Note 3 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit4]":
                                                                                            $nhermit4 = renpy.input("Note 4 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit5]":
                                                                                            $nhermit5 = renpy.input("Note 5 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit6]":
                                                                                            $nhermit6 = renpy.input("Note 6 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit7]":
                                                                                            $nhermit7 = renpy.input("Note 7 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit8]":
                                                                                            $nhermit8 = renpy.input("Note 8 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit9]":
                                                                                            $nhermit9 = renpy.input("Note 9 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit10]":
                                                                                            $nhermit10 = renpy.input("Note 10 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit11]":
                                                                                            $nhermit11 = renpy.input("Note 11 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit12]":
                                                                                            $nhermit12 = renpy.input("Note 12 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit13]":
                                                                                            $nhermit13 = renpy.input("Note 13 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit14]":
                                                                                            $nhermit14 = renpy.input("Note 14 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit15]":
                                                                                            $nhermit15 = renpy.input("Note 15 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit16]":
                                                                                            $nhermit16 = renpy.input("Note 16 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit17]":
                                                                                            $nhermit17 = renpy.input("Note 17 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit18]":
                                                                                            $nhermit18 = renpy.input("Note 18 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit19]":
                                                                                            $nhermit19 = renpy.input("Note 19 (maximum 50 characters):", length = 50)
                                                                                        "[nhermit20]":
                                                                                            $nhermit20 = renpy.input("Note 20 (maximum 50 characters):", length = 50)
                                                                                        "Don't rewrite":
                                                                                            jump breaknav
    "Write another note?"
    menu:
        "Yes":
            jump bluenotes
        "No":
            if route=="blue":
                jump breakreal
            jump breaknav
label bluenav:
scene black with dissolve
pause 1
$firstpatient = "blue"
$sessions += 1
########################## 
if month == 1:
    if day == 8:
        scene black with dissolve
        "I spent the weekend wondering how I could help Charlie recover his memories."
        scene bg mcdesk with dissolve
        show h cute with dissolve
        h "Hello ~"
        play music "ost/sunny.ogg" fadein 8
        if easymeter:
            show screen easymeter
            show screen bluemeter
        show h smile with dissolve
        "He enters my office with a smile. He seems somehow more cheerful than usual."
        m smile "How are you?"
        show h laugh with dissolve
        h "Great! It's so nice of you to keep seeing me every day ~"
        show h cute with dissolve
        m flirt "I'm glad you think so."
        show h sidetalk with dissolve
        h "Do you... not see all of your patients this often?"
        show h bored with dissolve
        m conf "I don't neglect anyone, don't worry."
        show h sad with dissolve
        h "...oh."
        show h tsun with dissolve
        h "...."
        m gasp "So..."
        show h neu with dissolve
        m fab "I thought about what you said on Friday."
        show h gasp with dissolve
        h "And?"
        show h siden with dissolve
        m conf "I think if we both work hard, you can get your memories back."
        show h gasp with dissolve
        h "R... Really..?"
        show h laugh with dissolve
        h "That's great, [name]!"
        show h cute with dissolve
        m angry "...at least some of them. I don't want to promise that much yet."
        show h bored with dissolve
        "He nods, regaining a serious expression."
        show h frusttalk with dissolve
        h "But... you'll help me... right?"
        show h bored with dissolve
        m cute "I'll try my best."
        show h happy with dissolve
        h "That's all that matters, [name] ~"
        show h smile with dissolve
        m frust "...."
        show h sidesmile with dissolve
        m gasp "Could you... tell me about what you think you remember?"
        stop music fadeout 6
        show h frust with dissolve
        h "Ummm...."
        show h talk with dissolve
        h "Like... my childhood?"
        show h bored with dissolve
        m fabtalk "If you want to."
        show h sidetalk with dissolve
        h "Well..."
        play music "ost/tran.ogg" fadein 8
        show h sadtalk with dissolve
        h "I have some memories... They're blurry, though."
        show h sad with dissolve
        m conf "Just tell me about them and we'll try to make some sense of them from there."
        show h neu with dissolve
        "He ponders what I said for a moment before nodding enthusiastically."
        show h frusttalk with dissolve
        h "So, uh... I remember..."
        show h sad with dissolve
        "He hesitates."
        show h talk with dissolve
        h "...a house by the forest. But it must've been on the other side."
        show h bored with dissolve
        m gasp "You mean the city?"
        show h sidetalk with dissolve
        h "Probably."
        show h sadsmile with dissolve
        h "The... the house looks nice."
        show h smile with dissolve
        m flirt "So it's a good memory."
        show h sadtalk with dissolve
        h "If... it's real."
        show h frust with dissolve
        h "...."
        show h talk with dissolve
        h "Do you think it's real, [name]?"
        show h angry with dissolve
        menu:
            "It has to be":
                $personal+=1
                show h gasp with dissolve
                h "You... You think so?"
                show h happy with dissolve
                h "You're right! It has to be real!"
            "What do you think?":
                $BlueHeart+=1
                show drk with Dissolve(0.75)
                show b 1 with dissolve
                show b 2 with Dissolve(1.0)
                $renpy.pause(0.75, hard = True)
                hide b with dissolve
                hide drk with dissolve
                show h sidetalk with dissolve
                h "I mean... it just... came back to me."
                show h frust with dissolve
                h "I've never seen this memory before."
                show h talk with dissolve
                h "I don't know."
            "It's unlikely":
                $professional+=1
                show h neu with dissolve
                h "Oh..."
                show h sadtalk with dissolve
                h "If that's what you think, then... I guess..."
                show h sad with dissolve
                "He seems a bit discouraged."
        show h siden with dissolve
        m fabtalk "Is there anyone with you in that house?"
        show h frust with dissolve
        h "...."
        show h sidetalk with dissolve
        h "I'm... looking at the forest. I don't... recall anyone else."
        show h neu with dissolve
        m talk "What else do you remember?"
        show h talk with dissolve
        h "Ummm... There's this... woman talking to me."
        show h gasp with dissolve
        h "I think she's my mother."
        show h sadsmile with dissolve
        m gasp "Really? What is she like?"
        show h smile with dissolve
        h "She's smiling at me. She... seems proud of me."
        m neu "Do you think she's real?"
        show h sad with dissolve
        stop music fadeout 4
        h "...oh."
        show h talk with dissolve
        h "Are you... saying she's not?"
        show h bored with dissolve
        m fabtalk "No, I'm just asking for your honest opinion."
        play music "ost/hospital.ogg" fadein 6
        show h frusttalk with dissolve
        h "She... She must be real. My parents are real!"
        show h talk with dissolve
        h "[name], I know my parents are good people. They had to be, because they're my parents."
        show h sadtalk with dissolve
        h "And... we lived together in this nice house by the forest, and, and..."
        show h angrytalk with dissolve
        h "...And everything was really great!"
        show h sidetalk with dissolve
        h "And they loved me a lot. They must've."
        show h angry with dissolve
        m fabtalk "Do you remember that as well?"
        show h sadtalk with dissolve
        h "I..."
        stop music fadeout 4
        show h angrytalk with dissolve
        h "Yes! Yes, of course I do!"
        show h frust with dissolve
        h "[name]... Are you..."
        play music "ost/tension.ogg" fadein 6
        show h talk with dissolve
        h "...doubting me?"
        show h angry with dissolve
        "He seems really serious all of a sudden."
        show h sadtalk with dissolve
        h "If... If you don't believe me, I don't have to tell you any of that."
        show h bored with dissolve
        m serious  "I'm sorry. I didn't mean to -"
        stop music fadeout 3
        show h laugh with dissolve
        h "[name]! You didn't actually think I was being serious, did you? Hehe ~"
        show h smile with dissolve
        m neu "...."
        play music "ost/neutral.ogg" fadein 6
        m boretalk "Well..."
        show h cute with dissolve
        m fabtalk "I'm glad you remembered your parents. Somewhat."
        show h happy with dissolve
        h "Yes! It's great, isn't it?"
        show h bored with dissolve
        m talk "Can you tell me anything more about the -"
        "I realize he's not looking at me anymore."
        stop music fadeout 3
        m gasp "Charlie?"
        show h talk with dissolve
        h "...."
        h "The house... by the forest..."
        "Is he remembering something?"
        play music "ost/tension.ogg" fadein 4
        h "The... the forest..."
        show h neu with dissolve
        m serious "What about it, Charlie? What about the forest?"
        h "{i}It..."
        h "...."
        "He goes silent for a while, despite my attempts to make contact with him."
        stop music fadeout 3
        m gasp "Charlie? Can you hear me?"
        show h happy with dissolve
        h "Oh, hi [name] ~"
        show h cute with dissolve
        m fabtalk "Did you... happen to remember anything new?"
        play music "ost/sunny.ogg" fadein 6
        show h gasp with dissolve
        h "What do you mean?"
        "It's probably hopeless... But it is worth noting that something we talked about triggered this."
        "I just can't figure out what he could be remembering and why..."
        show h neu with dissolve
        m talk "...are you okay?"
        show h laugh with dissolve
        h "Of course I am ~"
        show h kawaii with dissolve
        "I don't think I should ask him things he doesn't know. I still can't understand how he doesn't remember all the..."
        "...I don't even know what to call them."
        "I suppose what \"they\" are will remain a mystery for now."
        show h smile with dissolve
        m talk "I'll see you again tomorrow. Have a nice day."
        show h happy with dissolve
        h "You too ~"
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        hide screen easymeter
        hide screen bluemeter
        "He leaves my office."
        "I'm still unsure if I should believe him or not, but I'm glad the memories he told me about are good ones, at least."
        jump breakchoice ### after this day there's the dream with Jane by the forest
    elif day == 9:
        scene bg mcdesk with dissolve
        play music "ost/neutral.ogg" fadein 6
        "Charlie greets me enthusiastically."
        if easymeter:
            show screen easymeter
            show screen bluemeter
        show h laugh with dissolve
        h "I'm so happy to be back here ~~"
        show h cute with dissolve
        m gasp "Why is that?"
        show h happy with dissolve
        h "I waited the whole morning to talk to you again!"
        show h talk with dissolve
        h "I... I had this... epiphany, after what I said yesterday."
        show h smile with dissolve
        m fabtalk "Really?"
        show h frusttalk with dissolve
        h "I thought about... my memories... and my childhood..."
        show h laugh with dissolve
        h "And I thought to myself: \"What about [name]?\"."
        show h smile with dissolve
        m gasp "Huh?"
        show h happy with dissolve
        h "Maybe if I hear about your childhood, it'll trigger some memories of my own!"
        show h cute with dissolve
        m boretalk "...oh."
        "That's an interesting idea..."
        m talk "Do you really think that could help?"
        show h sidetalk with dissolve
        h "I need to know what a childhood is like."
        show h smile with dissolve
        stop music fadeout 5
        m flirt "Alright then."
        "I take a deep breath. Where do I begin..?"
        play music "ost/tran.ogg" fadein 5
        m boretalk "I was born in the outskirts of the city. My family had a house near the..."
        "I hesitate."
        stop music fadeout 2
        m neu "...forest."
        m gasp "...."
        m regrettalk "Charlie..?"
        play music "ost/tension.ogg" fadein 5
        show h gasp with dissolve
        h "Yes? What is it?"
        m frust "Haven't I... told you about this already?"
        show h siden with dissolve
        h "No."
        m talk "Because... that place you described yesterday seems similiar to where I used to live."
        show h gasp with dissolve
        h "!!!"
        show h laugh with dissolve
        h "Oh my god, [name], that's amazing! We must've been neighbors ~"
        show h kawaii with dissolve
        "That's... not really what bothered me."
        stop music fadeout 5
        "Ugh, what was I thinking..? I can't believe he's making more sense than I am for once."
        m neu "I doubt it."
        play music "ost/hospital.ogg" fadein 8
        m fabtalk "I knew all my neighbors, and I'm pretty sure I wouldn't forget you."
        show h sadsmile with dissolve
        h "...oh."
        show h regrettalk with dissolve
        h "If you say so..."
        show h talk with dissolve
        h "What about your family? What were they like?"
        show h neu with dissolve
        m talk "I... lived with my parents and older sister, Jane."
        m "She was four years older than me."
        show h happy with dissolve
        h "Did you two get along?"
        show h smile with dissolve
        "I recall all the adventures we would have together when I was very little..."
        "Before... everything went wrong."
        show h cute with dissolve
        m boresmile "Yes, we did. We were very close, always spent time together."
        show h happy with dissolve
        h "That sounds so good! I wish I had siblings as well ~"
        show h siden with dissolve
        "He pauses for a while."
        show h frusttalk with dissolve
        h "I have this memory..."
        show h sidetalk with dissolve
        h "There's a girl who's taller than me, and another, smaller one."
        show h neu with dissolve
        m gasp "What do they look like?"
        show h sidesmile with dissolve
        h "The older one has red hair. She's looking at me. And the other one... has a blue bow in her hair."
        show h cute with dissolve
        h "She looks happy."
        m fabtalk "Did you only see them in this memory?"
        show h frust with dissolve
        h "...."
        show h sidetalk with dissolve
        h "I'm not sure."
        show h regret with dissolve
        h "There's... so many different people I can faintly recall..."
        m neu "I see."
        stop music fadeout 4
        show h happy with dissolve
        h "Do you still see your sister that often?"
        show h smile with dissolve
        m boretalk "She..."
        m angry "She passed away. A long time ago."
        play music "ost/neutral.ogg" fadein 8
        show h siden with dissolve
        h "...oh."
        show h sadtalk with dissolve
        h "I'm... sorry."
        show h regret with dissolve
        m conf "It's fine, really."
        show h sad with dissolve
        h "I hope my siblings didn't die... That would be horrible."
        m gasp "So you think you had siblings?"
        show h sidesmile with dissolve
        h "Umm... I'd want to."
        show h neu with dissolve
        m regrettalk "Being an only child must be hard... I can't imagine a childhood on my own."
        show h laugh with dissolve
        h "I'm happy for you ~"
        show h cute with dissolve
        m gasp "Huh?"
        show h happy with dissolve
        h "At least you had a loving sister for a bit."
        show h sidesmile with dissolve
        m regret "...."
        "I never thought of it like that."
        "He's right... I should be grateful for Jane."
        "I just... wish it lasted."
        show h gasp with dissolve
        h "So what happened later?"
        show h smile with dissolve
        m frust "Umm..."
        m talk "I wanted to study psychology."
        m uncom "So... I guess I just... spent a lot of time studying."
        m fabtalk "I skipped two years of high school because I was studying ahead of time."
        show h cute with dissolve
        h "Wow, you were really determined ~"
        show h sidesmile with dissolve
        m bored "I guess I was."
        "All to work here... It's paid off, it really has."
        show h smile with dissolve
        m neu "I graduated university two years younger than most of my friends."
        m talk "So I already have a few years of experience as a psychologist."
        show h frust with dissolve
        h "...."
        show h talk with dissolve
        h "Do you think I could've been studying before I got here?"
        show h bored with dissolve
        m frust "Hmm..."
        m talk "Did you like school?"
        show h sidetalk with dissolve
        h "Umm... some of it."
        show h regretsmile with dissolve
        h "I think... I always liked biology the most."
        stop music fadeout 3
        show h frust with dissolve
        "...."
        show h happy with dissolve
        h "That... means I'm smart, right..? Like you!"
        play music "ost/sunny.ogg" fadein 6
        show h sidesmile with dissolve
        m smile "Probably."
        show h laugh with dissolve
        h "Once I'm out of here, [name], I'm going to study just like you did."
        show h frusttalk with dissolve
        h "Or maybe... once I get my memories back, all the knowledge I had will come back to me."
        show h laughblush with dissolve
        h "And I'll be smart again!"
        show h sidesmile with dissolve
        h "...I also won't have to study that way."
        m boretalk "That could happen."
        "I should try not to discourage him. I can't know anything for sure just yet."
        show h gasp with dissolve
        h "Did you have a lot of friends at school?"
        show h smile with dissolve
        m talk "Umm... a couple, yeah."
        show h neu with dissolve
        m boretalk "I always prioritized my work, though."
        stop music fadeout 5
        show h frust with dissolve
        h "...."
        show h sidetalk with dissolve
        h "I remember... a party. With a couple of people my age."
        show h regret with dissolve
        h "It was dark... it's really blurry now."
        "Huh."
        play music "ost/tran.ogg" fadein 6
        show h neu with dissolve
        m frusttalk "Charlie, could I ask you a slightly... more difficult question?"
        show h laugh with dissolve
        h "Ooh, I love a challenge ~! Go ahead."
        show h smile with dissolve
        m talk "Do you think you were always like this? That you always wanted to have a lot of friends?"
        show h siden with dissolve
        h "...."
        show h frusttalk with dissolve
        h "I... can't know that for sure."
        show h siden with dissolve
        h "I don't recall much when it comes to friendship."
        show h neu with dissolve
        m fab "It's possible that your desire to make friends comes from having felt lonely before."
        stop music fadeout 4
        show h gasp with dissolve
        h "Woah... You... You really think so?"
        m talk "That's just a guess, but yeah. It might be the case."
        show h frust with dissolve
        h "...."
        show drk with dissolve
        hide drk with dissolve
        show drk 2 with dissolve
        h "{cps=*2}{i}Might be, might be... does that mean it is?"
        h "{cps=*2}{i}Does she really think that? Is that what [name] thinks?"
        h "{cps=*2}{i}...is that what [name] thinks about me?"
        hide drk with hpunch
        show h neu with dissolve
        "Ugh, I feel sick. What just happened?"
        play music "ost/tension.ogg" fadein 6
        "I think it's just a headache. I look at Charlie again, hoping this hasn't interrupted our session."
        m gasp "I'm sorry, I don't know what that was. What did you say just now?"
        show h gasp with dissolve
        h "What did I what?"
        m frust "You... you said..."
        show h cute with dissolve
        h "I didn't say anything, [name] ~"
        "I bite my lip in frustration."
        show h sidesmile with dissolve
        "Either he's lying, or I'm..."
        "...hearing things."
        "I didn't get much sleep today."
        stop music fadeout 4
        show h sadtalk with dissolve
        h "You look tired, [name]. Are you okay?"
        show h sadsmile with dissolve
        "I nod."
        show h smile with dissolve
        m cute "Don't worry about me. I have the whole break to rest."
        show h laugh with dissolve
        h "Oh yeah, we're running out of time. I'll see you tomorrow, [name] ~"
        show h cute with dissolve
        m conf "Goodbye, Charlie."
        hide screen easymeter
        hide screen bluemeter
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        "He leaves. What was that just now..?"
        jump breakchoice
    elif day == 10:
        scene bg mc with dissolve
        play music "ost/neutral.ogg" fadein 7
        "Charlie is back. I wonder if he remembers anything new..."
        show bg mcdesk with dissolve
        show h laugh with dissolve
        h "Hello ~!"
        if easymeter:
            show screen easymeter
            show screen bluemeter
        show h smile with dissolve
        m flirt "How are you today?"
        show h sidetalk with dissolve
        h "I... tried to remember some more things..."
        show h siden with dissolve
        m gasp "And?"
        show h regrettalk with dissolve
        h "...nothing."
        show h sad with dissolve
        "...oh."
        m talk "Don't get discouraged. I'm sure you -"
        show h happy with dissolve
        h "But I have a different idea!"
        show h cute with dissolve
        m fab "What is it?"
        show h frusttalk with dissolve
        h "So... I have a lot of dreams."
        stop music fadeout 6
        show h regretsmile with dissolve
        h "Most of them... Don't make much sense, but some... feel real."
        show h neu with dissolve
        m frusttalk "Are you saying your memories may be coming back to you as dreams?"
        show h happy with dissolve
        h "Yes!"
        show h cute with dissolve
        play music "ost/emo.ogg" fadein 6
        "That's... an interesting idea."
        show h neu with dissolve
        m angrytalk "And what do you see in these dreams?" 
        show h frusttalk with dissolve
        h "Umm... most of the times I'm in some... forest."
        show h siden with dissolve
        m gasp "A forest? How did you get there?"
        show h regret with dissolve
        h "I don't... know."
        show h regrettalk with dissolve
        h "I just remember it seeming like... an eternity."
        show h regret with dissolve
        m angry "What do you mean?"
        show h sadtalk with dissolve
        h "I'm... walking through it, but... it never ends."
        show h talk with dissolve
        h "And is's always the same trees, the same place... I feel like I'm going in circles."
        show h regret with dissolve
        "Hmm... Going in circles..?"
        stop music fadeout 4
        m talk "Do you think this forest represents something?"
        show h gasp with dissolve
        h "Huh?"
        play music "ost/tension.ogg" fadein 6
        show h angrytalk with dissolve
        h "Why should it represent something? It's real, I {i}know{/i} it's real!"
        show h frust with dissolve
        "I back away a little. For some reason, he seems absolutely convinced it's real."
        show h happy with dissolve
        h "[name], I know how to get my memories back now!"
        show h laugh with dissolve
        h "I just have to trust these dreams! I've been seeing my whole life in them for the past year and never realized it's all real!"
        show h cute with dissolve
        "I can't help but be skeptical about this..."
        stop music fadeout 5
        show h smile with dissolve
        m talk "Have you ever seen any memories, other than this forest, in dreams?"
        show h laugh with dissolve
        h "Yes, lots of them! It's so amazing, [name], I finally know everything ~!"
        play music "ost/hospital.ogg" fadein 6
        show h sidesmile with dissolve
        m boretalk "So from your dreams, what can you tell me about how you got here?"
        show h siden with dissolve
        h "...."
        show h sad with dissolve
        h "...oh."
        show h regrettalk with dissolve
        h "I... didn't think about that..."
        show h angry with dissolve
        h "But the forest is real! I can prove it!"
        m gasp "How?"
        show h happy with dissolve
        h "I'll draw it! I just need some paper."
        show h evil with dissolve
        "I'm not sure if drawing it makes it any more believable, but this might be interesting."
        "Besides, how could I say no?"
        show h smile with dissolve
        m flirt "Give me a moment. I'll fetch everything from office IV."
        show h laugh with dissolve
        h "Wow, you really believed me ~ I'm so happy now ~!"
        scene bg officeiv with dissolve
        "I take everything he needs from the office next to mine, reserved for group activities and come back to my office."
        scene bg mcdesk with dissolve 
        m cute "There you go."
        show h frust with dissolve
        stop music fadeout 8
        "He starts drawing enthusiastically."
        "For a while, all of his attention is focused exclusively on the paper."
        "I can barely see what he's drawing, with how quickly his hands are moving."
        show h siden with dissolve
        "A while later, he stops suddenly and looks at the sketch."
        show h talk with dissolve
        h "Looks about right. Here."
        play music "ost/emo.ogg" fadein 6
        show charlieforest with dissolve
        "Huh. It's a forest, but there's something unsettling about it."
        m no "Well..."
        "He shoves the drawing in my face."
        h "...Well?"
        m "It looks... like a forest."
        h "And..?"
        m "I mean... I can't tell if it's real or not."
        h "Why?"
        h "You just... don't want to believe me."
        stop music fadeout 5
        m "No, it's not that! I simply don't think I have enough proof to... believe you, I guess."
        h "...."
        show h frust with dissolve
        h "If you trusted me, you'd believe me..."
        play music "ost/tension.ogg" fadein 6
        hide charlieforest with dissolve
        m regret "...."
        m angrytalk "Charlie, I'm sorry. I'm trying to look at it from different perspectives, maybe -"
        show h angrytalk with dissolve
        h "Why is it so hard to look at it from mine?"
        show h angry with dissolve
        menu:
            "Because you're different":
                show h regrettalk with dissolve
                h "I... I know, [name]."
            "Because I wasn't trying to":
                show h sadtalk with dissolve
                h "Why?"
                show h regrettalk with dissolve
                h "Why does nobody try to see things the way I do?"
                show h angrytalk with dissolve
                h "Why do I always have to-"
            "Because it's difficult":
                show h regrettalk with dissolve
                h "If it were easy, I wouldn't be here..."
        stop music fadeout 5
        show h regretsmile with dissolve
        h "...."
        show h laugh with dissolve
        h "What am I saying? You're doing your best, of course you are ~"
        play music "ost/mc.ogg" fadein 8
        show h cute with dissolve
        "I wish I had that much faith in myself..."
        show h smile with dissolve
        m conf "I will do anything I can to help you, Charlie. I promise."
        show h kek with dissolve
        h "Oh, there's no need to promise that - I know you will."
        show h kawaii with dissolve
        "I smile at him. I'm still amazed by how quickly he moves on from his doubts."
        "It's almost like..."
        "No. That's not possible. Not Charlie."
        "...."
        show h regrettalk with dissolve
        h "What's wrong, [name]? Did I say something..?"
        show h sadsmile with dissolve
        m boresmile "I'm fine. I was just thinking about that drawing of yours."
        show h gasp with dissolve
        h "Oh?"
        show h cute with dissolve
        m cute "It's very pretty. You must be talented."
        show h kek with dissolve
        h "Hehe ~"
        show h laugh with dissolve
        h "That's so nice of you to say, [name] ~"
        show h sideblush with dissolve
        stop music fadeout 5
        "Yeah, there's no way Charlie could be like that. I'm overthinking this."
        m talk "It looks like we're out of time. I'll see you tomorrow, Charlie."
        play music "ost/tran.ogg" fadein 5
        show h blush with dissolve
        h "Goodbye ~"
        hide screen easymeter
        hide screen bluemeter
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        "I'm still a little concerned about what he said..."
        "That I don't trust him. That if I did, I would've believed him."
        "No, I can't believe his every word. No matter how much I want to trust him, there are things he doesn't know."
        "And despite how much he believes in his own version, I have to be careful."
        "...even if it means he might feel betrayed."
        jump breakchoice
    elif day == 11:
        scene bg mc with dissolve
        "...."
        play music "ost/neutral.ogg" fadein 7
        "I'm waiting for Charlie in my office."
        play sound "knock.ogg" 
        m neu "Come in."
        show jl neutral with dissolve
        "...oh."
        m gasp "Is something wrong?"
        show jl calmtalk with dissolve
        jl "Yeah, your patient isn't feeling well. Doesn't want to leave his room."
        show jl talk with dissolve
        jl "You might want to check IX out."
        play sound "doorclose.ogg" fadein 1
        hide jl with dissolve
        "She leaves without another word."
        "Charlie, refusing to leave his room..? That doesn't sound right."
        "Something must be very wrong if Charlie, of all people, doesn't want to talk to me."
        "I... I have to act! I don't think I need any of my things, so I leave my office in a hurry."
        "This is an emergency, after all."
        scene bg patients with dissolve
        stop music fadeout 4
        "I approach Charlie's room carefully."
        scene black with dissolve
        m confusion "Charlie? Are you okay?"
        "Without further ado, I open the door."
        play sound "ost/jump.ogg"
        scene bg charlie with hpunch
        "!!!"
        "He's {i}gone -!"
        "{cps=2}. . ."
        "Oh wait. He's right here."
        play music "ost/hospital.ogg" fadein 8
        "He's sitting on the floor next to the door, right next to me."
        "I've never seen him like this... he looks depressed."
        m freeze "Charlie?"
        "Still no response."
        "I sit on the floor next to him, not too close - I don't want to invade his personal space, but I need him to notice me."
        m fabtalk "Hey, it's me, [name]."
        if easymeter:
            show screen easymeter
            show screen bluemeter
        show charlie11 with Dissolve(1.0)
        "I realize he likely knows I'm here, but for some reason doesn't want to say anything."
        "That's new..."
        "I think back to the dream I had yesterday..."
        "That must've been him... he looked so much different, though."
        "Younger, definitely. The two people I heard must've been his parents."
        stop music fadeout 5
        "Why did I have this dream now..? And why did it feel so... accurate?"
        m sadtalk "What happened?"
        h "...."
        play music "ost/tension.ogg" fadein 5
        show charlie12 with dissolve
        h "I was wrong."
        m talk "About what?"
        h "About... my parents."
        m frust "What do you mean? Did you remember anything new?"
        "He nods slowly."
        h "They... they didn't really love me."
        m wut "!!!"
        m trigger "Did you see them in a dream?"
        h "I did. It was real."
        m regrettalk "Can you tell me about this dream?"
        h "...."
        h "They just... kept yelling at me. And saying that..."
        hide charlie12 with dissolve
        h "...They're disappointed with me."
        menu:
            "I'm so sorry to hear that...":
                $personal+=2
                "He's silent."
            "How do you know it's real?":
                $professional+=2
                h "What?"
                h "I just do, [name]!"
        m talk "I had a similar dream last night."
        h "Huh?"
        "If he believes that these dreams are real, maybe telling him about mine can help."
        m angry "I saw you. Except you were younger. And it was through your mother's eyes."
        show charlie12 with dissolve
        h "Really? [name], you really aren't lying to me?"
        m trigger "No, why would I?"
        h "...."
        h "Was my father there as well?"
        m frusttalk "He was, but I couldn't see him."
        h "What about me?"
        m regret "You were sitting in your room, ignoring them."
        h "I wasn't!"
        m gasp "H-Huh?"
        stop music fadeout 6
        h "You saw the same thing I did, but from a different point of view."
        "...oh."
        "Okay, wow... I wouldn't have thought of that."
        "Still..."
        m angry "That's impossible."
        h "Does it matter?"
        m freeze "But... I don't have these memories... How did I -?"
        h "You're overcomplicating it."
        play music "ost/emo.ogg" fadein 8
        m boretalk "I was just trying to understand."
        h "Why..? You don't have to understand."
        m sad "...."
        "Maybe he's right and I'm overthinking a simple dream, but... he sounds so harsh today. So much... different."
        m talk "Charlie?"
        h "Yes?"
        m angry "Your parents loved you. I felt that."
        h "...."
        "I'm not sure what I believe at this point, but I want to convince him."
        h "Then why were they yelling at me?"
        m sadtalk "You haven't talked to them in a week, they were worried about you!"
        h "They were..?"
        h "I didn't notice."
        m regrettalk "Charlie, something was seriously wrong. They really wanted to help you."
        h "...."
        hide charlie12 with dissolve
        "He hides his face from me even further."
        "It seems he doesn't want to talk to me."
        menu:
            "Try to convince him":
                $professional+=1
                m frust "Charlie, I really think they meant well."
                m boretalk "Maybe... the circumstances were difficult and you weren't allowing them to help."
                h "...."
                m sad "Charlie, please, just listen to me."
                show charlie12 with dissolve
                stop music fadeout 5
                "...."
                "He's stubborn."
                "I stay with him for a while, trying to talk to him, but I don't think there's much I can do."
                $HermitFail=True    
            "Move a little closer":
                $personal+=2
                $BlueHeart+=1
                "I hesitantly move closer to him on the floor."
                m sadtalk "Charlie... Why won't you talk to me?"
                h "...."
                "It seems it's getting harder for him to ignore me."
                show drk with Dissolve(0.75)
                show b 1 with dissolve
                show b 2 with Dissolve(1.0)
                $renpy.pause(0.75, hard = True)
                hide b with dissolve
                hide drk with dissolve
                stop music fadeout 5
                menu:
                    "Keep talking":
                        $professional+=1
                        m regrettalk "I'm sorry you felt that way, but I really think what you saw was incomplete."
                        m conf "Your parents meant well, I'm sure of it."
                        "He seems to suddenly realize I got closer to him."
                        h "You... You really think so?"
                        "I nod."
                        show charlie12 with dissolve
                        play music "ost/hospital.ogg" fadein 5
                        h "...Fine."
                        h "I'll believe you for now, [name]."
                        m smile "Thank you ~"
                        h "Get out now. I'll talk to you tomorrow, but get out."
                        "A little startled, I leave his room."
                    "Get closer":
                        $BlueHeart+=2
                        show charlie12 with dissolve
                        h "...huh?"
                        h "You... You're touching me, [name]."
                        "My shoulder is touching his arm."
                        m freeze "I'm so sorry, I just wanted to-"
                        play music "ost/ship.ogg" fadein 6
                        h "Wait. It's fine that way."
                        show drk with Dissolve(0.75)
                        show b 1 with dissolve
                        show b 2 with Dissolve(1.0)
                        $renpy.pause(0.75, hard = True)
                        hide b with dissolve
                        hide drk with dissolve
                        m neu "...."
                        "Focus, [name]. Change the topic."
                        m sadtalk "Do you believe me when I say that your parents meant well? I really saw how concerned your mother was about you..."
                        hide charlie12 with dissolve
                        h "...."
                        h "I'll believe you, [name]."
                        h "I have to believe something."
                        "He sounds somewhat indifferent, but it's better than silence."
                        m smile "Thank you."
                        "I glance at him and suddenly feel somewhat self-conscious."
                        m frust "Um... I should be leaving for now."
                        show charlie12 with dissolve
                        h "...okay."
                        "I give him a small smile before getting up."
            "Leave him be":
                stop music fadeout 5
                m talk "I'll see you tomorrow. I hope we can talk then."
                $HermitFail = True
        hide screen easymeter
        hide screen bluemeter
        play sound "doorclose.ogg" fadein 1
        scene bg patients with dissolve
        "Charlie acted so strangely today... I tried my best."
        jump breakchoice
    elif day == 12:
        if HermitFail:
            scene bg mc with dissolve
            "I was told by the nurses that Charie really doesn't want to talk to me again."
            "Maybe he needs some space..."
            $route="no"
            jump patientsattack
        else:
            scene bg mcdesk with dissolve
            play music "ost/sunny.ogg" fadein 6
            show h smile with dissolve
            if easymeter:
                show screen easymeter
                show screen bluemeter
            h "Hi."
            m cute "Hello again ~"
            m smile "I'm really glad you wanted to talk to me today."
            scene bg mcdesk with dissolve
            show h siden with dissolve
            h "...."
            "He takes a seat in silence."
            "I wonder if that dream is what affected him so much..."
            show h frust with dissolve
            m talk "How do you feel today?"
            stop music fadeout 5
            show h frusttalk with dissolve
            h "I told you yesterday..."
            show h angry with dissolve
            h "How am I supposed to feel after what happened?"
            m serious "But... you believed me, right?"
            play music "ost/emo.ogg" fadein 6
            show h neu with dissolve
            "He nods."
            m regret "And yet you doubt it?"
            show h sidetalk with dissolve
            h "I do."
            show h frust with dissolve
            m sad "And it makes you feel uneasy?"
            show h sidetalk with dissolve
            h "That's... putting it lightly, [name]."  
            show h regrettalk with dissolve
            h "I... I really thought they loved me... that they were happy with me..."
            show h frust with dissolve
            h "I thought I... knew that, at least."
            show h talk with dissolve
            h "But... now that I saw them in this dream, it makes me question everything again."
            show h angrytalk with dissolve
            h "I... I still don't know anything, [name]. I want to know!"
            show h regret with dissolve
            m frust "I understand. But doesn't knowing what you saw and accepting it as the truth make it better?"
            show h angrytalk with dissolve
            h "No!"
            show h frusttalk with dissolve
            h "I can't know anything for sure... It just made everything worse!"
            show h frust with dissolve
            m sad "I'm sorry."
            show h cute with dissolve
            h "Thanks, [name]. I'm also sorry."
            show h smile with dissolve
            m gasp "Huh?"
            show h regrettalk with dissolve
            h "About... yesterday. And about ignoring you."
            show h sidesmile with dissolve
            m fabtalk "So you were ignoring me on purpose?"
            show h talk with dissolve
            h "Yes."
            show h sidetalk with dissolve
            h "I'm not sure why, but... my initial response to that dream was to just... cut off, I guess."
            show h frust with dissolve
            m neu "Strange, given that it's what you were doing in my dream, as well."
            show h gasp with dissolve
            h "Really?"
            show h neu with dissolve
            m fab "Even the way you were sitting was... similar."
            show h talk with dissolve
            h "But... didn't you say I shouldn't believe everything I see in dreams?"
            show h bored with dissolve
            "...."
            stop music fadeout 5
            "He's right. But... I feel like I should ask him about these dreams..."
            "This might get nonsensical very quickly."
            menu:
                "So that dream influenced the way you acted last time?":
                    $BlueHeart+=1
                    show h sidetalk with dissolve
                    h "...What do you mean?"
                    show h neu with dissolve
                    m regrettalk "You were really quiet yesterday, and that's never happened before."
                    show h regret with dissolve
                    h "...oh."
                    show h sidetalk with dissolve
                    h "I guess..."
                    show h frust with dissolve
                    h "I just... reacted to being yelled at that way."
                    show drk with Dissolve(0.75)
                    show b 1 with dissolve
                    show b 2 with Dissolve(1.0)
                    $renpy.pause(0.75, hard = True)
                    hide b with dissolve
                    hide drk with dissolve
                "Moving on...":
                    pass
            m talk "Do you feel like you'll keep having these dreams now? Or was it just a one-time thing?"
            show h sidetalk with dissolve
            h "I'm not sure..."
            h "I..."
            play music "ost/tension.ogg" fadein 6
            show h frust with dissolve
            "He bites his lip."
            m gasp "Is something wrong?"
            show h sadtalk with dissolve
            h "I don't... want to keep having these dreams... If they're like this."
            show h frust with dissolve
            h "...."
            show h regrettalk with dissolve
            h "That wasn't a nice thing to remember, [name]..."
            show h regret with dissolve
            m angry "I know it may seem pointless now, but if you still want to regain your memories, this might be your only hope, Charlie."
            show h gasp with dissolve
            h "You... think so?"
            show h surp with dissolve
            m boresmile "You're starting to recall what really happened."
            m talk "Your past may not be as you'd want it to be, but it's what shaped you as a person and what lead you to where you are today."
            show h bored with dissolve
            m smile "There's nothing to be afraid of - the person you were in that dream is still you, and you have to accept it if you want to recall everything."
            show h siden with dissolve
            h "...."
            m bored "You said you talk to everyone here."
            show h neu with dissolve
            "He nods."
            stop music fadeout 5
            m gasp "Have you asked any of the patients about their past?"
            show h sidetalk with dissolve
            h "Not really."
            show h bored with dissolve
            m sadsmile "I can assure you, everyone here deals with a lot. You're not the only one wishing your past was just a bit happier."
            play music "ost/hospital.ogg" fadein 6
            m frusttalk "But all these people... they know they need what they've been through."
            m smile "They need to understand what happened and why it happened to them, so they can get better."
            m sad "If you reject your past, and you refuse to remember, you'll never leave this place."
            show h gasp with dissolve
            h "...!"
            show h surp with dissolve
            m angry "I'll do anything I can to help you, but {i}you{/i} have to remember. You have to want to remember."
            show h siden with dissolve
            h "...."
            m talk "Do you want to remember everything, Charlie?"
            stop music fadeout 5
            show h frusttalk with dissolve
            h "I..."
            show h frust with dissolve
            h "I don't know..."
            show h regrettalk with dissolve
            h "I don't... {i}know..."
            play music "ost/fight.ogg" fadein 10
            show h angrytalk with dissolve
            h "I don't know anything anymore, [name]! I hate it!"
            show h sad with dissolve
            m frust "...."
            menu:
                "I'm sorry":
                    $personal+=1
                    show h neu with dissolve
                    h "...."
                    stop music fadeout 4
                    show h regret with dissolve
                    "He falls silent."
                    show h regretsmile with dissolve
                    h "You're right, [name]. I have no idea what came over me."
                    show h cute with dissolve
                    "He gives me a somewhat forced smile before getting up."
                    show h smile with dissolve
                    h "...bye."
                    play sound "doorclose.ogg" fadein 1
                    scene bg mc with dissolve
                    "He leaves. I don't... think he was in the mood to talk, anyway."
                    hide screen easymeter
                    hide screen bluemeter
                    $route="no"
                    jump patientsattack
                "That's why you have to remember":
                    $professional+=1
                    $BlueHeart+=1
                    show drk with Dissolve(0.75)
                    show b 1 with dissolve
                    show b 2 with Dissolve(1.0)
                    $renpy.pause(0.75, hard = True)
                    hide b with dissolve
                    hide drk with dissolve
                    show h regrettalk with dissolve
                    h "I... I don't want to..."
                    show h frust with dissolve
                    m fab "Why is that?"  
                    show h sidetalk with dissolve
                    h "Because..."
                    show h sadtalk with dissolve
                    h "I may not... like the person I was in these memories."
                    show h sad with dissolve
                    m talk "What do you mean? It's still you."
                    show h regret with dissolve
                    h "...."
                    show h regrettalk with dissolve
                    h "What if I... did some things... I shouldn't have?"
                    show h frust with dissolve
                    m boretalk "Is that what you're afraid of?"
                    show h regret with dissolve
                    "He nods hesitantly."
                    show h regrettalk with dissolve
                    h "Some people here... have done some really bad things..."
                    show h sad with dissolve
                    h "I don't want to be one of them."
                "I'm trying to help you":
                    $wrong+=1
                    stop music fadeout 5
                    show h surp with hpunch
                    m sjw "Don't you understand? It's the only way!"
                    show h regret with dissolve
                    h "...."
                    "He's oddly silent."
                    play music "ost/tension.ogg" fadein 5
                    m angry "Charlie, I'm only doing what's best for you."
                    show h frust with dissolve
                    m boretalk "I know it may not seem that way, but I'm really trying to help."
                    h "...."
                    m neu"...."
                    show h siden with dissolve
                    "He's ignoring me completely, just like yesterday."
                    m regret "If you don't want to talk, maybe we both need a break."
                    m talk "I'll see you on Monday."
                    play sound "doorclose.ogg" fadein 1
                    scene bg mc with dissolve
                    hide screen easymeter
                    hide screen bluemeter
                    "He leaves."
                    $route="no"
                    jump patientsattack
            menu:
                "They're no different than you and I":
                    $professional+=1
                    m angry "They're all dealing with problems of their own."
                    show h sidetalk with dissolve
                    h "...I know."
                    show h siden with dissolve
                    "He falls silent."
                    stop music fadeout 6
                    m talk "Charlie, whatever your past is like, it doesn't change anything."
                    m boretalk "I wouldn't apply for this job in the first place if I were discouraged so easily."
                    play music "ost/hospital.ogg" fadein 6
                    show h sadsmile with dissolve
                    h "Thanks, [name]..."
                    show h talk with dissolve
                    h "Sorry about that."
                    show h kawaii with dissolve
                    h "I'm fine now ~"
                    m neu "...."
                    show h smile with dissolve
                    m talk "I'm glad you are."
                    show h sidetalk with dissolve
                    h "I should... get going, though."
                    show h cute with dissolve
                    h "I'll see you tomorrow."
                    m freeze "...On Monday."
                    show h laugh with dissolve
                    h "Right! Bye ~"
                    play sound "doorclose.ogg" fadein 1
                    scene bg mc with dissolve
                    hide screen easymeter
                    hide screen bluemeter
                    "He leaves in a hurry. I'm not sure why."
                    $route="no"
                    jump patientsattack
                "You can't change for the worse if you remember your past":
                    stop music fadeout 5
                    show h gasp with dissolve
                    h "Are you... sure about that?"
                    show h neu with dissolve
                    m conf "You can only feel better, trust me."
                    m flirt "And you'll be able to understand yourself more afterwards."
                    play music "ost/sunny.ogg" fadein 6
                    show h sidesmile with dissolve
                    h "You think so?"
                    show h smile with dissolve
                    m cute "I'm sure of it."
                    show h laugh with dissolve
                    h "That sounds great, [name]!"
                    show h sidetalk with dissolve
                    h "But..."
                    show h talk with dissolve
                    h "How can I get my real memories back?"
                    show h smile with dissolve
                    m smile "They should come with time in some form."
                    show h cute with dissolve
                    h "Oh, right. That... makes me feel hopeful."
                    show h laughblush with dissolve
                    h "Thank you so much, [name] ~"
                    play sound "doorclose.ogg" fadein 1
                    scene bg mc with dissolve
                    "He leaves my office with a smile. I'm glad he at least feels better now."
                    hide screen easymeter
                    hide screen bluemeter
                    $route="no"
                    jump patientsattack
                "It won't change how I feel about you":
                    $personal+=2
                    show h neu with dissolve
                    "That... came out of nowhere."
                    stop music fadeout 6
                    m confusion "I meant that... even if your past turns out to be something you're not exactly proud of, it doesn't matter to me."
                    m frusttalk "I wouldn't give up on you over something like that."
                    h "...."
                    "He's eerily silent."
                    show h frust with dissolve
                    m sad "Is something... wrong?"
                    play music "ost/hermittense.ogg" fadein 10
                    show h regrettalk with dissolve
                    h "I... I don't... know..?"
                    show h frust with dissolve
                    h "I feel... strange."
                    show h regret with dissolve
                    h "Like... I'm not really... here."
                    m gasp "What do you mean?"
                    show h sadtalk with dissolve
                    h "Can... can you hear me, [name]...?" ##voiced
                    show h frusttalk with dissolve
                    h "I... can't tell anymore..."
                    show h regret with dissolve
                    m trigger "Charlie, what's wrong?"
                    show h dead with dissolve
                    "He's not looking at me... like I'm not really there..."
                    show h deadtalk with dissolve
                    h "[name], you're real... You're real."
                    m freeze "Huh?"
                    show h sidetalk with dissolve
                    h "Unless... you aren't."
                    show h dead with dissolve
                    "I don't know what to do."
                    menu:
                        "I have to help him!":
                            $personal+=1
                            "I'm done being helpless. I need to act."
                        "Charlie, listen to me.":
                            m talk "I'm here. And I'm real, we both are."
                            show h dead with dissolve
                            h "[name]... You don't know anything either."
                            "I... I need to do something."
                        "{color=#5185ff}Stay silent":
                            $professional+=1
                            "I decide to wait it out. He doesn't say a single word for a while."
                            show h sidetalk with dissolve
                            h "I... I should be leaving, Dr. Hart."
                            show h bored with dissolve
                            m shock "Huh?"
                            show h frust with dissolve
                            h "...."
                            play sound "doorclose.ogg" fadein 1
                            scene bg mc with dissolve
                            hide screen easymeter
                            hide screen bluemeter
                            "He leaves my office."
                            $route="no"
                            jump patientsattack
                    "I get up from my chair in one decisive motion."
                    m confusion "Charlie, I-"
                    show h surp with dissolve
                    "Suddenly, he hides his face in his hands. What's happening to him..?"
                    show h deadtalk with dissolve
                    h "Forest... in the forest..."
                    show h dead with dissolve
                    "Huh?"
                    show h deadtalk with dissolve
                    h "It's dark... {i}it's so dark..."
                    show h dead with dissolve
                    m sadtalk "Charlie..?"
                    show h sadtalk with dissolve
                    h "Alone, so alone... {i}always so alone!"
                    "Could... that mean... he's seeing some old memories of this forest he keeps talking about?"
                    show h dead with dissolve
                    "Why now?"
                    show h deadtalk with dissolve
                    h "And... and..."
                    show h regrettalk with dissolve
                    h "{i}...Her."
                    stop music fadeout 6
                    show h dead with dissolve
                    "He's shaking. I'm not sure what's happening, but it doesn't look good."
                    m angry "Charlie."
                    "I reach out to him."
                    m talk "Charlie, listen to -"
                    scene black with Dissolve(0.2)
                    scene hermitkiss with Dissolve(0.8)
                    $renpy.pause()
                    m no "!!!"
                    "Before I can finish, he gets up and closes the distance between us faster than I thought possible."
                    "He... {i}He's kissing me..?"
                    play music "ost/emo.ogg" fadein 6
                    "My mind goes blank in an instant."
                    "Is this... really happening..?"
                    "I... somehow can't bring myself to push him away."
                    "...Not until I understand what the hell he's doing and why."
                    "Is he doing it out of anger? Is he trying to scare me away..?"
                    "No, that's not it... It's not like him at all."
                    "The way he's kissing me, it feels... desperate, more than anything."
                    "I'm still frozen in place since the moment he bridged the gap between us."
                    "I... thought I had everything under control."
                    "The air above my desk always felt like a barrier of sorts - between me and whatever was happening to my patients."
                    "But... now he's violated it. There's no neutral space seperating us anymore."
                    "And... it makes me feel..."
                    "...like my control is slipping away."
                    stop music fadeout 6
                    show hermitkiss with hpunch
                    "That's not the way it's supposed to be!"
                    scene black with Dissolve(1.0)
                    "I finally place my hand on his shoulder and push him away gently."
                    "I look him in the eye carefully... he doesn't look quite like himself."
                    play music "ost/tension.ogg" fadein 8
                    m "Charlie, what are you doing?"
                    h "...."
                    "He looks almost delirious..."
                    h "I... wanted you to stop talking."
                    "I'm at a loss of words. Why would he do something like that..?"
                    scene bg mcdesk with dissolve
                    "Suddenly, he smiles. Something is so different about him right now..."
                    show h 2neu with dissolve
                    "He sits down again, and so do I."
                    m tsun "...."
                    stop music fadeout 6
                    m confusion "Could you please explain why you did what you just did?"
                    show h 2sidetalk with dissolve
                    h "I already explained myself."
                    show h 2siden with dissolve
                    "I'm a little taken aback by everything that's happening."
                    show h 2angry with dissolve
                    m sjw "And you believe it was appropriate, given the situation you were in?"
                    show h 2talk with dissolve
                    h "Obviously."
                    show h 2siden with dissolve
                    play music "ost/neutral.ogg" fadein 6
                    "Not that I'm mad at him, of course he's not in the state to be held accountable for his actions, but..."
                    "Some explanation would be nice."
                    "My control of the situation was violated and I need to know why."
                    show h 2neu with dissolve
                    m angrytalk "Charlie, do you realize the consequences of what you've just done?"
                    show h 2frusttalk with dissolve
                    h "What? It's not like I hurt you or anything."
                    show h 2siden with dissolve
                    "I... would never have expected something like that from him."
                    m talk "I didn't allow you to do that."
                    show h 2calmtalk with dissolve
                    h "You didn't seem all that angry about it a moment ago."
                    show h 2neu with dissolve
                    "I... I can't believe I have to justify myself like that."
                    m fabtalk "What happened before you... did that?"
                    stop music fadeout 5
                    show h 2sidetalk with dissolve
                    h "Huh?"
                    show h 2neu with dissolve
                    m frusttalk "You said some pretty strange things."
                    show h 2frustsmile with dissolve
                    h "Are you sure you're not the one who needs help here?"
                    play music "ost/hospital.ogg" fadein 6
                    show h 2angry with dissolve
                    h "I never said anything like that."
                    "What..?"
                    show h 2talk with dissolve
                    h "Time for your break, Doctor. See you on Monday."
                    show h 2neu with dissolve
                    m sjw "Wait -"
                    play sound "doorclose.ogg" fadein 1
                    scene bg mc with dissolve
                    hide screen easymeter
                    hide screen bluemeter
                    "He leaves, and I can't bring myself to move from my chair."
                    "What the hell was that..?"
                    "First it seemed like his memories may be coming back, then he kisses me out of nowhere, and just now..."
                    "He was acting like a completely different person."
                    "I'm so confused..."
            jump breakchoice
    elif day == 13:
        scene black with dissolve
        pause 1
        nt "What... was that dream?"
        play music "ost/emo.ogg" fadein 6
        nt "That girl... I recognized her. I knew her."
        show bg mcbed with dissolve
        nt "I... can't remember her face..."
        nt "How did I recognize her?"
        if HermitApathyEnd:
            nt "Something about her seemed wrong."
            nt "I couldn't agree to whatever it was she suggested."
        else:
            nt "For some reason, I chose to make a deal with her in that dream."
        nt "In the end, it's not like I had control over what I did."
        nt "It was just a dream."
        nt "...."
        nt "...right?"
        jump nextday
    elif day ==  14:
        jump nextday
##########################         
    elif day == 15:
        scene bg mc with dissolve
        "Charlie enters my office."
        "I wonder if I should ask him about last Friday... maybe it would be better to just drop it."
        m talk "Good morning."
        if easymeter:
            show screen easymeter
            show screen bluemeter
        play music "ost/sunny.ogg" fadein 7
        h "Hello ~!"
        show bg mcdesk with dissolve
        show h neu with dissolve
        "He sits down. He seems to be back to normal from whatever happened last time."
        m smile "How are you today, Charlie?"
        show h bored with dissolve
        h "...."
        show h laugh with dissolve
        h "Oh, sorry! I was a little... confused for a moment ~"
        show h smile with dissolve
        h "I'm fine, I'm fine."
        show h cute with dissolve
        m neu "...."
        menu:
            "Are you sure everything is okay?":
                $professional+=1
                show h smile with dissolve
                "He nods enthusiastically."
                show h sadtalk with dissolve
                h "Is something bothering you, [name]?"
                show h regret with dissolve
                "He seems completely oblivious to my concerns."
            "I'm glad to see you again ~":
                $personal+=1
                show h kawaii with dissolve
                h "~~"
        menu:
            "Have your memories come back?":
                show h gasp with dissolve
                h "What..? My memories?"
                show h sidetalk with dissolve
                h "Why would they come back?"
                show h neu with dissolve
                m neu "...."
                m frusttalk "I... thought you remembered some things... On Friday."
                stop music fadeout 8
                show h surp with dissolve
                h "On... Friday?"
                show h sad with dissolve
                h "...."
                m gasp "What's wrong..?"
                show h regrettalk with dissolve
                h "[name], nothing like that happened last Friday."
                show h bored with dissolve
                m wut "What do you... mean?"
            "You were acting strange last time":
                show h gasp with dissolve
                h "Strange? How so?"
                show h smile with dissolve
                m neu "...."
                m frusttalk "It... looked like your memories came back for a moment, and after that..."
                stop music fadeout 8
                show h neu with dissolve
                m sadtalk "You seemed like a completely different person."
                show h regrettalk with dissolve
                h "Are you sure that... really happened?"
                show h bored with dissolve
                m gasp "Huh?"
                m sjw "No, that was last Friday. They even moved you to XXI temporarily!"
        show h kek with dissolve
        h "You must be imagining things, [name] ~"
        show h gasp with dissolve
        h "Maybe it was all a dream, but it looked so real you thought it actually happened!"
        show h laugh with dissolve
        h "It happens to me all the time ~"
        show h cute with dissolve
        m wut "What..?"
        m angrytalk "Charlie, you remember this, right? Stop trying to -"
        play music "ost/tension.ogg" fadein 6
        show h neu with dissolve
        h "No."
        m freeze "...?"
        show h talk with dissolve
        h "I don't remember it, [name]."
        show h sidesmile with dissolve
        h "Are you really sure I did all of these things?"
        show h smile with dissolve
        m neu "...."
        "I'm dumbfounded for a moment."
        "Could he really have... lost his recent memories like that?"
        "...Or am I going insane?"
        "No, I'm sure it happened."
        "I decide to clarify some things."
        m angrytalk "Last week, we were going over what you thought you remember about your past."
        show h sidetalk with dissolve
        h "We were..?"
        show h neu with dissolve
        m talk "You had a dream about something you believed to be a memory of your parents."
        h "...."
        show h kek with dissolve
        h "I'm sorry, [name]. I don't think I understand."
        show h sidesmile with dissolve
        m serious "So you don't remember having that dream?"
        show h gasp with dissolve
        h "What dream? [name], I'm telling you I never had a dream like that."
        show h surp with dissolve
        m frust "...."
        "I'm second-guessing my own memories... even though I know it's far more likely that he's forgotten it."
        show h neu with dissolve
        m talk "So... what's the last session with me you remember?"
        show h frust with dissolve
        h "Ummm..."
        show h sidetalk with dissolve
        h "I think we talked about... my psychiatrist..?"
        show h cute with dissolve
        stop music fadeout 6
        "...."
        "That was over a week ago."
        "So he forgot all of last week, just like that..? Why?"
        show h gasp with dissolve
        h "What's the matter, [name] ~?"
        show h smile with dissolve
        play music "ost/neutral.ogg" fadein 6
        menu:
            "Change the topic":
                $personal+=1
                "I try to come up with something reasonable to ask him..."
                "No, there's no point."
                show h surp with dissolve
                m angry "Charlie, I'm sorry, but we really need to talk about it."
                show h neu with dissolve
                m uncom "I can't overlook you losing your memory of half our sessions."
                show h gasp with dissolve
                h "Why?"
            "Keep asking him":
                $professional+=1
                m angry "You've lost your memory again. A whole week."
                show h sidetalk with dissolve
                h "How can you be sure of that, [name]?"
                show h neu with dissolve
                m frusttalk "You can't recall things that clearly happened."
                show h regret with dissolve
                h "...."
                show h sadtalk with dissolve
                h "[name], I don't want to fight you..."
                show h siden with dissolve
                m regret "...."
        show h neu with dissolve
        m angry "You told me you wanted to regain your memories."
        show h bored with dissolve
        m talk "And now that you've lost them again, it's my duty to tell you what happened."
        m trigger "You may believe me or not, but my responsibility is to at least try."
        stop music fadeout 5
        show h regrettalk with dissolve
        h "[name]..."
        show h sadtalk with dissolve
        h "Why are you angry?"        
        show h sad with dissolve
        play music "ost/emo.ogg" fadein 6
        m confusion "What do you mean? I'm not angry."
        show h frusttalk with dissolve
        h "Then... why are you yelling at me?"
        show h regret with dissolve
        h "If I really forgot something, it's not..."
        show h sadtalk with dissolve
        h "It's not my fault, [name]."
        show h sad with dissolve
        m frusttalk "No, I didn't say it was your fault, I..."
        "The look in his eyes makes me lose my trail of thought."
        stop music fadeout 5
        "I don't want him to think I blame him for this... how could I?"
        "It's obviously beyond his control, and he should be helped."
        play music "ost/hospital.ogg" fadein 6
        m regrettalk "Charlie. I'm so sorry you felt that way."
        show h frust with dissolve
        m fabtalk "I could never be mad at you, do you understand?"
        show h neu with dissolve
        "He nods slowly."
        m talk "Look, it's unfortunate that you lost your memories again, but it's not the end of the world."
        show h gasp with dissolve
        h "It's not?"
        show h surp with dissolve
        m conf "Maybe they'll come back soon. And maybe it can help us understand what happened last time when you lost your memories."
        show h sidetalk with dissolve
        h "You think so?"
        show h neu with dissolve
        m flirt "And until they come back... nothing changes."
        show h gasp with dissolve
        h "Nothing?"
        show h surp with dissolve
        m smile "Nothing."
        show h laugh with dissolve
        stop music fadeout 6
        h "I'm so happy, [name] ~"
        show h regretsmile with dissolve
        h "When you said I lost a whole week, I was so scared..."
        show h regret with dissolve
        m fabtalk "Scared of what?"
        play music "ost/tran.ogg" fadein 8
        show h sidetalk with dissolve
        h "Scared that... something happened last week. To me."
        show h frusttalk with dissolve
        h "That... maybe I had some accident, or... I don't know anymore..."
        show h bored with dissolve
        m flirt "Nothing like that happened. We only talked about what you remembered from before you got here."
        show h gasp with dissolve
        h "Oh. We were recovering memories?"
        show h neu with dissolve
        m regrettalk "Well, we weren't... very successful, but I learned a few things."
        show h regretsmile with dissolve
        h "I... feel like you know things I don't. It's scary."
        show h sadsmile with dissolve
        m smile "Don't worry about it. We'll take it slow, okay?"
        show h cute with dissolve
        "He nods enthusiastically. At least he's back to his normal self."
        m talk "But that's for tomorrow. I think we're out of time."
        show h happy with dissolve
        h "Thank you, [name]... You must really believe in me ~"
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        hide screen easymeter
        hide screen bluemeter
        "I'm glad he's okay, at least."
        "Though it bothers me... how could he have lost his memories again just like that?"
        "Did he just repress them? Maybe he was upset after what happened last time, and he..."
        "Well, I can't be sure. Let's hope he regains his memories soon."
        pause 1
        jump charliestar2
    elif day == 16:
        scene bg mc with dissolve
        play music "ost/neutral.ogg" fadein 7
        "I'm waiting for Charlie in my office."
        "...."
        "What should I do today..? I thought I should just tell him what happened last week, but..."
        "...maybe that triggered something in him. Something that caused him to forget the whole week."
        "I don't know what I should avoid with him... I feel completely lost."
        show bg sun with dissolve
        "Why are his memories gone? And are they really all gone, or has he repressed them somehow?"
        "Maybe he doesn't want to remember..."
        "With all of this going on, I can't help but wonder..."
        "...do {i}I{/i} want to remember last week?"
        "A part of me thinks we should start over. Try again to solve this mess that is his memories."
        "...."
        menu:
            "It's good I got another chance at this":
                "Maybe I took the wrong path last week... maybe it's for the best."
                "I wanted to solve this too quickly. We both need time. We need to trust each other before jumping into this."
                "I'll do it right this time. I have to."
            "He should remember it":
                "All this time, he wanted to regain his memories..."
                "And I intend to help him do it. No matter what happens in the process."
            "I can't believe I lost a week of work":
                "No matter how I look at it, it's still a whole week of wasted sessions."
                "All I can do now is hope that I can use what I learned to help him."
                "There must be something I can salvage from last week... right?"
        play sound "knock2.ogg"
        show bg mc with dissolve
        h "[name]? Are you... are you busy?"
        if easymeter:
            show screen easymeter
            show screen bluemeter
        "I turn around to notice Charlie already in my office."
        m gasp "Oh, not at all."
        "I take a seat by my desk."
        m cute "Please, sit down."
        scene bg mcdesk with dissolve
        show h neu with dissolve
        m neu "...."
        show h cute with dissolve
        h "...."
        "What's going on..? For the first time in a long time, I have no idea how to start."
        "Maybe... I should just ask him."
        stop music fadeout 6
        show h smile with dissolve
        m fabtalk "Is there anything you'd like to talk about, Charlie?"
        show h gasp with dissolve
        h "Like what?"
        show h smile with dissolve
        m smile "Anything, really. Whatever is on your mind."
        show h frust with dissolve
        h "Ummm..."
        play music "ost/sunny.ogg" fadein 6
        show h happy with dissolve
        h "Well, I bumped into my favourite nurse the other day."
        show h neu with dissolve
        m flirt "And who's that?"
        show h  with dissolve
        show h gasp with dissolve
        h "Sue. Do you know her?"
        show h bored with dissolve
        if SunLink>0:
            m cute "Yes."
        else:
            m frusttalk "No, I don't think so."
        show h laugh with dissolve
        h "We're friends. She's really great ~"
        show h sidesmile with dissolve
        m fabtalk "So what happened?"
        show h kek with dissolve
        h "What was supposed to happen?"
        show h cute with dissolve
        m talk "Well, you were telling me how you bumped into her one time."
        show h gasp with dissolve
        h "Oh. I did."
        show h neu with dissolve
        stop music fadeout 5
        m neu "...."
        show h cute with dissolve
        h "...."
        "I think that was it."
        menu:
            "Last week...":
                $Hermithonest+=1
                m fabtalk "Would you like to talk about what happened last week?"
                show h frust with dissolve
                h "Ummm..."
                show h sadtalk with dissolve
                play music "ost/hospital.ogg" fadein 6
                h "Do we have to?"
                show h angry with dissolve
                m gasp "What do you mean?"
                show h regrettalk with dissolve
                h "Um... wouldn't it be better to just... talk about something else?"
                show h frust with dissolve
                m talk "Why do you say that?"
                show h sad with dissolve
                h "You looked... sad. When you mentioned last week yesterday. I don't want you to be sad."
                show h regret with dissolve
                "Is... that why he doesn't want to talk about last week?"
                "It wasn't that upsetting... and I shouldn't keep all of it from him."
            "You seem to be in high spirits":
                show h laughblush with dissolve
                h "Why wouldn't I be?"
                show h sidesmile with dissolve
                h "It's a pretty day ~"
                "He seems to be back to the way he was last week... it's comforting, in a way."
                play music "ost/hospital.ogg" fadein 6
                m smile "I'm so glad you're okay."
                show h gasp with dissolve
                h "Huh?"
                show h neu with dissolve
                m serious "I was worried about you yesterday..."
                show h sidetalk with dissolve
                h "Because I lost my memories?"
                show h siden with dissolve
                "I nod."
                show h bored with dissolve
                m regret "I feel like I owe you an explanation, at least."
        m angry "I'll keep it brief, but you should know what happened."
        m gasp "Is that okay?"
        show h regrettalk with dissolve
        h "I... think so? I don't know what you're about to say, but..."
        stop music fadeout 5
        show h cute with dissolve
        h "I trust you, [name]."
        "I smile. It makes me so happy to know that he trusts me."
        show h smile with dissolve
        m bored "Well..."
        play music "ost/memory.ogg" fadein 8
        show h neu with dissolve
        m talk "First, I asked you about your childhood."
        show h bored with dissolve
        m conf "You mentioned a house by the forest and a woman you thought to be your mother."
        "I pause to look at him, puzzled."
        "Can he still remember it? Or has he forgotten his recovered memories as well..?"
        show h neu with dissolve
        m gasp "Does any of that ring a bell?"
        show h regrettalk with dissolve
        h "Ummm... I..."
        show h frust with dissolve
        h "I don't remember talking about it to anyone, but..."
        show h talk with dissolve
        h "Yeah, I think I know that."
        show h siden with dissolve
        h "The... the woman. I know her face."
        "So he hasn't forgotten. That's good."
        show h smile with dissolve
        m boretalk "Then you asked me about my childhood."
        show h gasp with dissolve
        h "I did?"
        stop music fadeout 5
        show h surp with dissolve
        m fab "You said it might help you remember yours by comparison."
        show h regrettalk with dissolve
        h "Did... did it work?"
        show h bored with dissolve
        m talk "Not really, no."
        show h kek with dissolve
        h "...oh."
        play music "ost/sunny.ogg" fadein 6
        show h laugh with dissolve
        h "I'm sorry, [name]... I must have really bad ideas..."
        show h regretsmile with dissolve
        menu:
            "It was an interesting one":
                $BlueHeart+=1
                show h gasp with dissolve
                h "Really? But... it didn't work."
                show h surp with dissolve
                m cute "I thought it was worth a try, that's something."
                show h cute with dissolve
                h "Thank you, [name] ~"
                show drk with Dissolve(0.75)
                show b 1 with dissolve
                show b 2 with Dissolve(1.0)
                $renpy.pause(0.75, hard = True)
                hide b with dissolve
                hide drk with dissolve
            "What makes you say that?":
                show h frust with dissolve
                h "Well... it didn't work."
                m conf "That doesn't make it bad."
                show h sidesmile with dissolve
                "He smiles."
                h "You're right, [name]."
            "I'm sorry":
                show h laugh with dissolve
                h "For what?"
                "He laughs."
                show h sidesmile with dissolve
                h "Don't be silly, [name] ~"
        stop music fadeout 6
        show h gasp with dissolve
        h "So what happened then?"
        show h neu with dissolve
        "I pause to think about last Wednesday."
        "Should I mention him drawing the forest? It seems important, but..."
        play music "ost/tension.ogg" fadein 8
        "What if it triggers something in him? Something... like last Friday."
        menu:
            "You drew a forest":
                $Hermithonest+=1
                show h bored with dissolve
                m talk "You... said you often have dreams that feel \"real\"."
                m boretalk "And that in these dreams, you're in a forest."
                m regret "There's no way out, so you're lost, wandering around blindly."
                m talk "You said that these dreams feel like memories."
                show h regret with dissolve
                h "...."
                show h frusttalk with dissolve
                h "I... keep seeing this forest, but..."
                show h sadtalk with dissolve
                h "[name], I don't know what it means."
                show h regretsmile with dissolve
                h "It... it might just be a dream."
                show h regrettalk with dissolve
                h "I don't... know anymore..."
                show h frust with dissolve
                "Last week, he was so convinced it was real... what happened?"
                m neu "You drew this... forest."
                menu:
                    "Show him the drawing":
                        $Hermithonest+=1
                        m fab "I think you should see it."
                        show h neu with dissolve
                        "He watches me in silence while I reach down to get the drawing."
                        "Of course I kept it - right next to his file."
                        m boresmile "There it is."
                        "I pass him the sketch on my desk."
                        show h siden with dissolve
                        "He looks at it with an unreadable expression for a while."
                        "I can't help but wonder what is going through his head right now."
                        stop music fadeout 6
                        show h kek with dissolve
                        h "It's... a nice drawing. I think."
                        show h sadsmile with dissolve
                        m cute "It is."
                        m boretalk "You don't remember drawing this?"
                        show h talk with dissolve
                        h "No."
                    "Don't":
                        stop music fadeout 6
                        show h bored with dissolve
                        m regret "It looked... a little unsettling."
                        show h sidetalk with dissolve
                        h "...okay."
                        show h frust with dissolve 
                        m gasp "You don't remember it?"
                        show h talk with dissolve
                        h "No."
            "We talked about school and friends":
                show h neu with dissolve
                m talk "I tried to get you to talk about anything you might remember from the time you were a teenager."
                m bored "You liked biology the most at school, but couldn't remember anything other than that."
                show h laughblush with dissolve
                h "Biology was the best ~"
                show h smile with dissolve
                m angry "I asked about your friends because I theorized that you may have felt lonely at some point and it's why you want to befriend everyone here."
                show h sidetalk with dissolve
                h "...I see."
                show h talk with dissolve
                stop music fadeout 6
                h "Do you still think it's what happened? I-I mean, me having felt lonely?"
                show h neu with dissolve
                m fabtalk "It was just a theory, but I think it's possible."
                show h sidetalk with dissolve
                h "...okay."
        show h bored with dissolve
        play music "ost/hospital.ogg" fadein 8
        m frusttalk "Then..."
        "I wonder how I should explain what happened on Thursday..."
        menu:
            "We had weird dreams":
                $Hermithonest+=1
                show h gasp with dissolve
                h "About what?"
                show h surp with dissolve
                "Of course he doesn't question it."
                m talk "About your parents."
                show h neu with dissolve
                m frust "In my dream, they seemed worried, and in yours - angry."
                m regrettalk "You thought it meant that they didn't love you."
            "You felt depressed":
                show h gasp with dissolve
                h "Why?"
                show h neu with dissolve
                m regrettalk "You said you had a dream about your parents. That they seemed disappointed in you."
                m talk "And that it must've been a real memory."
        show h talk with dissolve
        h "And... you believed me?"
        show h bored with dissolve
        menu:
            "Yes":
                $BlueHeart+=1
                m flirt "Of course I did, Charlie."
                show h smile with dissolve
                m smile "I trust you."
                show h kawaii with dissolve
                h "~ ~"
                show h laugh with dissolve
                h "I'm so lucky to have a psychologist as great as you ~"
                show drk with Dissolve(0.75)
                show b 1 with dissolve
                show b 2 with Dissolve(1.0)
                $renpy.pause(0.75, hard = True)
                hide b with dissolve
                hide drk with dissolve
                show h cute with dissolve
                "Did I... lie to him..?"
            "No":
                $BlueHeart+=2
                show drk with Dissolve(0.75)
                show b 1 with dissolve
                show b 2 with Dissolve(1.0)
                $renpy.pause(0.75, hard = True)
                hide b with dissolve
                hide drk with dissolve
                m boretalk "I didn't have a way of knowing if it was real."
                show h cute with dissolve
                h "You're smart, [name]. And you're right."
                show h sadsmile with dissolve
                h "You shouldn't believe everything people say."
                "What..? What's that supposed to mean?"
        show h neu with dissolve
        m talk "Then, on Friday, you came to my office again."
        m regret "But... you were acting kind of... unusual."
        stop music fadeout 5
        show h sidetalk with dissolve
        h "How so?"
        show h frust with dissolve
        "How much should I say..?"
        "I don't think last Friday was very pleasant for either of us."
        play music "ost/memory.ogg" fadein 6
        menu:
            "You remembered something":
                $Hermithonest+=1
                show h bored with dissolve
                m sad "You were just... out of it."
                m talk "You talked about a forest, a... A girl, you mentioned a girl."
                show h neu with dissolve
                m frust "It looked like you remembered something. And... it probably wasn't pleasant."
                show h regret with dissolve
                m regrettalk "I'm sorry."
            "I think you were having a bad day":
                show h surp with dissolve
                h "Oh."
                show h laugh with dissolve
                h "I'm fine now ~"
                show h smile with dissolve
                m neu "It was... kind of jarring, actually."
        show h gasp with dissolve
        h "Is that why they put me in XXI after that?"
        show h surp with dissolve
        m gasp "You... remember that?"
        show h kawaii with dissolve
        h "You told me ~"
        show h sidesmile with dissolve
        h "And... so did my psychiatrist. After you did."
        show h talk with dissolve
        h "But I don't recall being in XXI. Ever."
        show h neu with dissolve
        "All things considered, maybe it's for the best."
        stop music fadeout 6
        m sadsmile "I doubt it would've been a good memory."
        show h laugh with dissolve
        h "Yeah. That means I only remember the nice things ~"
        show h kawaii with dissolve
        if Hermithonest>3:
            "Wait."
            "...."
            play music "ost/emo.ogg" fadein 6
            "That's it! That must be why he forgot last week."
            "He didn't sustain any kind of brain trauma, he just repressed it."
            "He must have."
            show h smile with dissolve
            m fab "Charlie?"
            show h cute with dissolve
            h "Hmm ~?"
            m angry "Based on what I said, would you say that last week was unpleasant?"
            show h bored with dissolve
            h "...."
            show h frusttalk with dissolve
            stop music fadeout 5
            h "Ummm... let me think..."
            show h frust with dissolve
            "He's silent for a bit. I can't blame him - I would need a while to process all of that as well."
            show h talk with dissolve
            h "No."
            show h neu with dissolve
            m trigger "No?"
            play music "ost/sunny.ogg" fadein 5
            show h sideblush with dissolve
            h "How could it not be nice to spend time with you, [name]?"
            show h laugh with dissolve
            h "I'm only sad that I don't remember it, it must've been great ~"
            show h sidesmile with dissolve
            "I'm... somewhat surprised, but... well, I guess Charlie will always be Charlie."
            m boresmile "I'm glad you know what happened now. I'd hate to keep you in the dark about something like this."
            show h cute with dissolve
            h "It was fun ~"
        else:
            play music "ost/sunny.ogg" fadein 5
            "I smile at him. I still can't grasp how he can squeeze this much optimism out of everything that's going on."
        m fabtalk "Well, I think we're running out of time for today."
        show h gasp with dissolve
        h "Already?"
        show h neu with dissolve
        m neu "I think so."
        m flirt "If there's something you want to say, we can stay here for a bit longer."
        show h bored with dissolve
        "I look at him analytically for a moment... maybe he just doesn't want to leave yet."
        m angry "I don't mind, we have time."
        show h surp with dissolve
        h "...."
        "I never know what to expect when he's silent like this."
        show h laugh with dissolve
        h "[name], [name], you really- That's too kind ~"
        show h cute with dissolve
        m gasp "Why? It's not like it's a problem."
        show h kek with dissolve
        h "Umm... I meant-"
        show h tsun with dissolve
        "He trips over his words and pauses to get a grip."
        show h laugh with dissolve
        h "I don't think I'll remember anything this quickly, [name]."
        show h sidetalk with dissolve
        h "Give me some time, tomorrow I should know some more."
        show h laughblush with dissolve
        h "I... need to think about it. I'm so slow, sorry ~!"
        show h cute with dissolve
        "He laughs."
        show h smile with dissolve
        m smile "No, I understand. Take all the time you need."
        show h laugh with dissolve
        h "Thank you ~"
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        hide screen easymeter
        hide screen bluemeter
        "He leaves my office with a smile."
        "...."
        "Is it just me, or was he a little... odd just now?"
        "It's Charlie, so \"odd\" is somewhat expected, but..."
        "I guess he must still be a little shaken after losing his memory - who wouldn't be?"
        if Hermithonest>3:
            "I tried to be as honest as possible and tell him what happened."
            "He should know the truth, even if it's not exactly a nice thing to hear."
            "I can't keep what happened from him."
        else:
            "And because he's still recovering, I shouldn't overwhelm him with too much information at once."
            "We have time, and I'll tell him everything he needs to know eventually."
        jump breakchoice
    elif day == 17: 
        if HermitApathyEnd: ## Apathy ending
            scene bg mcdesk with dissolve
            play music "ost/sunny.ogg" fadein 8
            show h happy with dissolve
            h "Hello ~"
            if easymeter:
                show screen easymeter
                show screen bluemeter
            show h kawaii with dissolve
            h "It's so good to see you again, [name] ~"
            m flirt "It's good to see you, too."
            show h sidesmile with dissolve
            "I wait for him to settle down before addressing the main issue."
            m gasp "Did you manage to remember anything since yesterday?"
            show h gasp with dissolve
            h "What?"
            show h sidetalk with dissolve
            h "Oh, you mean last week?"
            show h frust with dissolve
            h "Umm..."
            show h siden with dissolve
            h "...."
            show h bored with dissolve
            h "No."
            "I suppose I couldn't expect him to recover his memories in one day."
            "It was worth a try, though."
            show h kek with dissolve
            h "I'm sorry, [name]! I know you... cared a lot about that."
            show h sadsmile with dissolve
            m talk "No, it's okay. It's fine."
            m cute "You need to take your time."
            show h kawaii with dissolve
            h "~~"
            stop music fadeout 5
            show h sidesmile with dissolve
            "He looks around the room, distracted, before looking at me again."
            show h gasp with dissolve
            h "[name]?"
            show h talk with dissolve
            h "Does that... mean we'll keep talking until I remember it?"
            show h angry with dissolve
            play music "ost/hospital.ogg" fadein 6
            m fab "What do you mean?"
            show h sidetalk with dissolve
            h "I... I was wondering about what we're going to do now... our sessions."
            show h neu with dissolve
            m conf "Don't worry about that. There's always something to talk about."
            show h laugh with dissolve
            h "That's great ~"
            show h smile with dissolve
            m gasp "Were you... worried that I'd stop seeing you until you recover your memories?"
            show h regrettalk with dissolve
            h "That... would've been sad."
            show h frust with dissolve
            m serious "No, there's no way I would've done something like that."
            m smile "Nothing changes with our sessions, regardless of what you remember."
            show h neu with dissolve
            m flirt "I'm your psychologist, and I'll keep seeing you every day. That's not changing."
            show h laughblush with dissolve
            h "I'm so happy, [name] ~~"
            stop music fadeout 6
            show h cute with dissolve
            h "Thank you ~"
            show h smile with dissolve
            m regrettalk "It's not your fault that you lost your memory, Charlie... Nobody knows why it happened yet, but you didn't want it."
            play music "ost/tran.ogg" fadein 6
            show h neu with dissolve
            m talk "Nobody blames you for it, and you shouldn't as well."
            show h regrettalk with dissolve
            h "I... felt like I've done something... wrong."
            show h laugh with dissolve
            h "I'm sorry, [name], I'm such a mess sometimes, hehe ~"
            show h sideblush with dissolve
            m cute "It's okay. I'll wait."
            show h smile with dissolve
            m conf "And if you don't recover your memories, we'll just resume our sessions normally."
            m talk "We'll try to talk about your past, about the things you see and hear... we have a lot to talk about."
            show h laugh with dissolve
            h "That sounds great, [name] ~"
            show h cute with dissolve
            "We spend the rest of the session discussing the things he remembers from his past."
            play sound "doorclose.ogg" fadein 1
            scene bg mc with dissolve
            hide screen easymeter
            hide screen bluemeter
            "Charlie seems to be back to his usual, cheerful self for good."
            "I... can't say I'm not relieved to see him like this."
            $route="no"
            jump patientsattack
        else:
            if Hermitloop==0:
                jump backintheforest
            elif Hermitloop==1:
                jump backintheforest2
            else:
                scene black with dissolve
                nt "What... was that dream?"
                nn "{i}Wake up, [name]."
                scene black with vpunch
                nt "!!!"
                nt "I know this voice!"
                nn "{i}You should be thanking me ~"
                nt "I open my eyes."
                nt "I'm actually awake this time."
                nt "...I think."
                play music "ost/emo.ogg" fadein 6
                scene bg front with dissolve
                "I get ready and make my way to work."
                show bg greet with dissolve
                "...."
                "I wasn't {i}myself{/i} in that dream. I was Charlie."
                show bg central with dissolve
                "Just what is going on here..? First, that crazy dream from last Friday, now this?"
                "I feel like these nightmares are getting weirder and weirder the longer I work with Charlie."
                show bg mc with dissolve
                stop music fadeout 4
                "I'm waiting for him in my office."
                play sound "knock.ogg"
                pause 1
                m fabtalk "Come in. It's open."
                play sound "doorclose.ogg" fadein 1
                show hermitenter with dissolve
                if easymeter:
                     show screen easymeter
                     show screen bluemeter
                "He opens and closes the door slowly."
                play music "ost/tension.ogg" fadein 6
                "Something seems... odd about him."
                "He doesn't move and looks at me with wide eyes."
                "...it reminds me of my first session with William, actually."
                "I walk up to him, concerned."
                stop music fadeout 6
                m confusion "Charlie? Is everything okay?"
                h "I..."
                "He draws a shaky breath before doing the last thing I could've expected."
                scene black with Dissolve(0.2)
                play music "ost/hermittense.ogg" fadein 10
                scene hermittruth with dissolve
                $renpy.pause()
                m no "Ch-Charlie?"
                h "I saw it. I saw it again."
                h "The- the forest. I was in it."
                h "Please don't leave me now, [name]!"
                h "I- I can explain everything, just don't- {i}Don't leave me alone -"
                "What..?"
                m "I don't... I don't understand."
                h "Please. Just listen to me."
                show htm neu with dissolve
                "His voice is breaking. I've never seen him in such a panic."
                "I stay silent, urging him to continue."
                h "...."
                "He looks relieved that I want to listen to him. Why wouldn't I?"
                show htc sad with dissolve
                show htsmile with dissolve
                h "Thank you... Thank you."
                h "I- I don't know what I'd do... if it weren't for you."
                hide htsmile with dissolve
                h "And... and I'm sorry. For all of this."
                h "I thought that... it was for the best."
                show htc side with dissolve
                h "...."
                h "It wasn't."
                show htc neu with dissolve
                h "...[name]?"
                m "Yes?"
                h "How... how long have you been keeping this from me?"
                "What is he talking about..?"
                "Does this have something to do with that dream I had?"
                menu:
                    "I had a dream last night":
                        show htc freeze with dissolve
                        h "You... I... {i}my dream."
                        h "You had my dream."
                        h "Why?"
                        menu:
                            "She showed it to me":
                                h "No, it... it makes no sense..."
                                h "Why would she?"
                                show htm gasp with dissolve
                                "He tightens his grip on my arms. It's... starting to hurt."
                                menu:
                                    "We made a deal":
                                        h "A... a deal?"
                                        h "She... she's turned you against me, hasn't she?"
                                        show htc angry with dissolve
                                        h "How could you?!"
                                        menu:
                                            "We're working together":
                                                show htc freeze with dissolve
                                                h "You... but you -"
                                                h "You asked me about her. You pretended not to know who she is."
                                                show htc angry with dissolve
                                                h "...You made me sound crazy for seeing her!"
                                                h "You lied to me from the start, you made a deal with her to drive me insane, is that it?"
                                                h "You're all sick! You- You just want to use me!"
                                                jump hermitpanic
                                            "She said it would help you":
                                                show htc freeze with dissolve
                                                h "Help... me?"
                                                h "How?"
                                                show htc sad with dissolve
                                                m "I- I don't know! That's all she said."
                                                show htc sad with dissolve
                                                h "And... you believed her..? You don't... trust me at all, [name]."
                                                menu:
                                                    "I do":
                                                        h "I... [name], I want to believe you..."
                                                        show htc neu with dissolve
                                                        h "B-But... I can't."
                                                        jump hermitfail
                                                    "It was a dream":
                                                        show htc angry with dissolve
                                                        h "That makes no difference!"
                                                        menu:
                                                            "I didn't know it would affect anything":
                                                                show htc neu with dissolve
                                                                "He steps away from me suddenly."
                                                                show htc side with dissolve
                                                                h "You're right. You had no way of knowing."
                                                                show htc neu with dissolve
                                                                h "Because you didn't believe me when I told you it could."
                                                                jump hermitfail
                                                            "I shouldn't believe everything people say":
                                                                show htc neu with dissolve
                                                                h "...."
                                                                show htc side with dissolve
                                                                h "You're absolutely right."
                                                                show htsmile with dissolve
                                                                h "I... I told you my dreams were special, and you didn't listen. Because you're smarter than that."
                                                                jump hermitmore
                                                    "I need all the help I can get":
                                                        show htc angry with dissolve
                                                        h "Why? Because I'm too messed up for one person?!"
                                                        h "[name], you have no idea how hard it is to have to constantly please everyone!"
                                                        show htc freeze with dissolve
                                                        h "...."
                                                        "Is... is that how he really feels..?"
                                                        jump hermitslip
                                            "I didn't know what I was doing":
                                                show htc neu with dissolve
                                                h "...."
                                                h "[name], [name]... Why do you make this so hard..?"
                                                if Hermithonest>3:
                                                    show htsmile with dissolve
                                                    h "I... I'll believe you. One last time."
                                                    jump hermitmore
                                                else:
                                                    h "I can't trust someone who keeps lying to me."
                                                    jump hermitfail                                        
                                    "She betrayed you":
                                        show htc freeze with dissolve
                                        h "She... no..."
                                        show htm neu with dissolve
                                        h "...she would never."
                                        h "[name], why do you do this to me?"
                                        show htc sad with dissolve
                                        h "Why make me choose between the two of you?"
                                        menu:
                                            "She's not real":
                                                show htc freeze with dissolve
                                                h "Not... real..?"
                                                h "She's... she's as real as you or me."
                                                h "If I assume she isn't real, then..."
                                                h "What is? [name], what even is reality?"
                                                h "...."
                                                jump hermitpanic                                                
                                            "I'm the one trying to help you":
                                                show htc freeze with dissolve
                                                h "Why should I believe that..? [name], I don't know what to believe."
                                                if Hermithonest>3:
                                                    show htc side with dissolve
                                                    h "I... want to believe you..."
                                                    h "...."
                                                    show htc neu with dissolve
                                                    show htsmile with dissolve
                                                    h "[name], I trust you. Just tell me the truth."
                                                    jump hermitmore
                                                else:
                                                    h "...."
                                                    show htc neu with dissolve
                                                    h "No, I know."
                                                    h "I know not to believe someone who's lied to me before."
                                                    show htc angry with dissolve
                                                    h "You lied to my face without hesitation yesterday, how can I know you won't do it again?"
                                                    m "What?"
                                                    show htc freeze with dissolve
                                                    h "...."
                                                    jump hermitslip
                                            "She's manipulating you":
                                                show htc angry with dissolve
                                                h "How? By telling me that you've been lying to me this whole time?"
                                                show htm gasp with dissolve
                                                h "That you knew who I am and still made me pretend? To laugh at my stupidity?!"
                                                m "What?"
                                                show htc freeze with dissolve
                                                h "...."
                                                jump hermitslip                                            
                                    "It's not my fault":
                                        h "I... [name], I want to believe you..."
                                        show htc neu with dissolve
                                        h "B-But... I can't."
                                        jump hermitfail
                            "I'm in your head":
                                "He takes a step back, terrified."
                                h "You... {i}you..."
                                show htc angry with dissolve
                                h "Of course you are! You were from the beginning, that's why I trusted you so easily!"
                                show htc neu with dissolve
                                h "...."
                                show htc freeze with dissolve
                                h "[name]..."
                                show htm gasp with dissolve
                                h "Are you even real?"
                                menu:
                                    "Yes":
                                        h "No... no, I don't believe you... you can't be."
                                    "No":
                                        h "You're not... no, why did I ever think you were..?"
                                jump hermitpanic
                            "I don't know":
                                jump hermitfail
                    "I don't know what you're talking about":
                        jump hermitfail
    elif day == 18:
        scene bg mc with dissolve
        play music "ost/neutral.ogg" fadein 8
        "I'm waiting in my office, looking through my notes about Charlie."
        "All these facts... things I've noticed, things I felt observant for picking up on..."
        "...things I thought I knew about him."
        "How... how do I even treat him at this point?"
        "Do I just... discard everything I've learned and act like we've just met?"
        play sound "knock.ogg" fadein 1
        m fab "Come in, please."
        play sound "doorclose.ogg" fadein 1
        if easymeter:
            show screen easymeter
            show screen bluemeter
        "He opens the door and approaches my desk."
        h "...hello, [name]."
        show bg mcdesk with dissolve
        show h 2neu with dissolve
        "Already, his behavior feels very different."
        m neu "So."
        m boretalk "...I'm not sure where to begin."
        show h 2frusttalk with dissolve
        h "That {i}is{/i} a problem."
        show h 2siden with dissolve
        m angry "Yesterday, you said you're not the person I thought you were."
        show h 2talk with dissolve
        h "I'm not."
        show h 2neu with dissolve
        m fabtalk "So who are you?"
        show h 2sidetalk with dissolve
        h "Huh?"
        stop music fadeout 5
        show h 2neu with dissolve
        m neu "Focus on who you are, not who you are not."
        show h 2frust with dissolve
        h "...."
        show h 2sidetalk with dissolve
        h "I don't remember."
        show h 2siden with dissolve
        m serious "Then who are you now?"
        show h 2talk with dissolve
        play music "ost/hospital.ogg" fadein 8
        h "I'm... someone now?"
        show h 2frusttalk with dissolve
        h "Someone else than I was before?"
        show h 2frust with dissolve
        m conf "People change. Especially when they start from a blank slate again, like you did here."
        show h 2talk with dissolve
        h "When I first got here, I didn't remember anything."
        show h 2siden with dissolve
        h "I... felt like I should have something I knew, but... I didn't."
        m fab "You knew your first name."
        show h 2neu with dissolve
        h "Oh."
        show h 2sidesmile with dissolve
        h "I forgot that's not common knowledge as well."
        show h 2talk with dissolve
        h "\"Charlie\" is not my real name. I don't know what is."
        show h 2neu with dissolve
        "...."
        menu:
            "Why \"Charlie\"?":
                show h 2talk with dissolve
                h "My psychiatrist let me borrow his until I know what mine is."
                show h 2neu with dissolve
                m trigger "But... it's in your file as a first name."
                show h 2sidetalk with dissolve
                h "He thought we should keep the origin of the name between us."
                show h 2sidesmile with dissolve
                h "The official version of events is that I remembered it during a session."
            "Why would you make up a name?":
                show h 2talk with dissolve
                h "If it's in my file, the staff can call me that."
                show h 2sidetalk with dissolve
                h "And... I hated being nameless. It's not a good feeling."
        show h 2neu with dissolve
        m boretalk "Either way, you must have wanted a name quite badly."
        show h 2talk with dissolve
        h "I was nameless for one day, and that was one day too many."
        show h 2siden with dissolve
        m fabtalk "How do you feel now when people call you \"Charlie\"? Does it feel like they're addressing you?"
        m talk "Or someone else who stands between the real you and the outside world?"
        stop music fadeout 6
        h "...."
        show h 2frusttalk with dissolve
        h "The name, it stuck to the identity I made myself. I don't know about \"the real me\"."
        show h 2neu with dissolve
        m neu "I understand."
        "So it is, essentially, a persona. And it needed a name."
        play music "ost/memory.ogg" fadein 8
        m frusttalk "You say you \"made yourself an identity\". Why?"
        show h 2sidetalk with dissolve
        h "At the beginning, I... I didn't know how to act."
        show h 2frust with dissolve
        h "I noticed that... the nurses seem to act nicer to the patients who were friendly to them, but not forceful."
        show h 2neu with dissolve
        h "So... I watched the patients. The nurses. Everyone."
        show h 2sidetalk with dissolve
        h "I... I tried to understand what it is that makes people... like other people."
        show h 2siden with dissolve
        menu:
            "Is that why you asked me what kind of people I like?":
                show h 2neu with dissolve
                m neu "It was during one of our first sessions."
                show h 2sidesmile with dissolve
                h "I tried to understand you. So I could adjust to what you like."
                show h 2neu with dissolve
                m gasp "Why?"
                show h 2sidetalk with dissolve
                h "I... wanted you to like me. To... think I'm the most approachable of your patients."
                show h 2talk with dissolve
                h "...the nicest one."
                show h 2frust with dissolve
                h "I don't know who the others are, but I think it worked."
                show h 2neu with dissolve
                m fabtalk "Well, I've been seeing you every day. Congratulations."
            "Why go through all this trouble?":
                $BlueHeart+=1
                show drk with Dissolve(0.75)
                show b 1 with dissolve
                show b 2 with Dissolve(1.0)
                $renpy.pause(0.75, hard = True)
                hide b with dissolve
                hide drk with dissolve
                show h 2sidetalk with dissolve
                h "I... I don't want to be alone."
                show h 2angry with dissolve
                h "That's really it. I don't know why, but... I know I can't stand it."
                show h 2neu with dissolve
                m frusttalk "Do you think it might have something to do with your memories?"
        show h 2siden with dissolve
        h "...."
        show h 2talk with dissolve
        h "[name], I lied to you."
        show h 2sidetalk with dissolve
        h "The pieces of memories that I have... they aren't happy."
        show h 2frust with dissolve
        h "I couldn't remember anything that happened, but thinking about my past made me... sad."
        show h 2talk with dissolve
        h "The first few days here, I felt... hollow."
        show h 2siden with dissolve
        h "And... I didn't know what else to do. How to fix it."
        m talk "So you remember more than you told me?"
        show h 2talk with dissolve
        h "Yes."
        show h 2neu with dissolve
        m serious "Why did you only tell me about the happy things?"
        show h 2frusttalk with dissolve
        h "Because that's what I wanted to remember. I don't... want to think about the bad things."
        show h 2siden with dissolve
        h "And Charlie, he... didn't seem like someone to have bad memories. Nobody would believe that I'm this happy with memories like that."
        show h 2sidetalk with dissolve
        h "But... they keep coming back. Another lie, [name] - they've been coming back. In pieces."
        show h 2frust with dissolve
        h "It's slow, but... they are."
        m angry "What do you remember?"
        show h 2talk with dissolve
        h "Nothing clear, but..."
        show h 2sidetalk with dissolve
        h "My life was a mess."
        show h 2neu with dissolve
        h "At some point, I stopped talking to my parents."
        show h 2sidetalk with dissolve
        h "I would spend whole days away from home, I have no idea where."
        show h 2talk with dissolve
        h "Eventually, I cut ties with my family and never saw them again."
        h "It's a blur after that."
        show h 2neu with dissolve
        m smile "That's already a lot. You might be able to piece it together at this rate."
        show h 2sidetalk with dissolve
        h "I don't... want to try."
        show h 2talk with dissolve
        h "The truth is, I don't want to remember anything. If it's like this."
        show h 2neu with dissolve
        m boretalk "Maybe if you learned why it happened, you would forgive yourself."
        show h 2talk with dissolve
        h "For what?"
        show h 2siden with dissolve
        m angry "Leaving your parents. That's what bothers you, isn't it?"
        stop music fadeout 6
        show h 2frusttalk with dissolve
        h "What bothers me, [name], is the emptiness. The lack of joy, of anything."
        show h 2sidetalk with dissolve
        h "I didn't feel anything at that time. I had nobody to talk to."
        show h 2talk with dissolve
        h "I don't want to go back to that."
        show h 2neu with dissolve
        m bored "I understand."
        play music "ost/tension.ogg" fadein 6
        show h 2frusttalk with dissolve
        h "Do you, [name]? I don't think you do."
        show h 2angrytalk with dissolve
        h "Do you even want to listen to me go on about this? If you don't understand a thing, just shut up and listen to me."
        show h 2angry with dissolve
        h "...."
        menu:
            "Go on":
                stop music fadeout 4
            "Excuse me?":
                stop music fadeout 4
                show h 2talk with dissolve
                h "You told me to be honest. That's exactly what I'm doing."
            "I want to listen":
                stop music fadeout 6
                $BlueHeart+=1
                show h 2smile with dissolve
                h "Thank you, [name]."
                show h 2talk with dissolve
                h "That was unnecessary. I'm... out of focus today, I'm not sure how to act."
                show h 2neu with dissolve
                show drk with Dissolve(0.75)
                show b 1 with dissolve
                show b 2 with Dissolve(1.0)
                $renpy.pause(0.75, hard = True)
                hide b with dissolve
                hide drk with dissolve
                m fab "Go on, it's fine."
        show h 2sidetalk with dissolve
        h "Since everyone was so willing to believe that after a year, I remember nothing, I..."
        show h 2talk with dissolve
        h "Decided to do it again."
        play music "ost/emo.ogg" fadein 6
        show h 2neu with dissolve
        m trigger "What?"
        show h 2talk with dissolve
        h "I told you I lost my memories of last week. I lied."
        show h 2siden with dissolve
        "...."
        m regrettalk "Why would you fake another amnesia?"
        show h 2sidesmile with dissolve
        h "Because you fell for it."
        "Undoubtedly, I did. I'm not proud of that, but how was I supposed to know?"
        show h 2neu with dissolve
        m angry "But... what's the point of erasing last week?"
        show h 2frusttalk with dissolve
        h "I... acted impulsively. I was out of control, I don't know what happened to me."
        show h 2sidetalk with dissolve
        h "I realized after the fact that I shouldn't have ignored you on Thursday."
        h "And I shouldn't have kissed you on Friday."
        show h 2talk with dissolve
        h "Both of these days made you reconsider what you thought about me."
        show h 2sidetalk with dissolve
        h "So you threatened to expose me if I slipped again."
        show h 2evil with dissolve
        h "I thought I'd lost, but then I remembered that I have one advantage over you."
        menu:
            "Being a patient, not a psychologist":
                show h 2sidesmile with dissolve
                h "Wrong."
                show h 2talk with dissolve
                h "The advantage is that people think I'm insane."
            "Being considered unstable and delusional":
                $BlueHeart+=2
                show drk with Dissolve(0.75)
                show b 1 with dissolve
                show b 2 with Dissolve(1.0)
                $renpy.pause(0.75, hard = True)
                hide b with dissolve
                hide drk with dissolve
                show h 2smile with dissolve
                h "Exactly."
            "Having been here for over a year":
                show h 2sidesmile with dissolve
                h "Wrong."
                show h 2talk with dissolve
                h "The advantage is that people think I'm insane."
        show h 2neu with dissolve
        m talk "I have two questions at this point."
        show h 2talk with dissolve
        h "Ask."
        show h 2siden with dissolve
        m boretalk "When you said you realized you shouldn't have done something, I thought you meant it on a moral level."
        m frust "But the way you said it, it doesn't sound that way."
        show h 2talk with dissolve
        h "I made mistakes last week."
        show h 2sidetalk with dissolve
        h "And... no, I haven't really grasped morality just yet."
        show h 2frust with dissolve
        stop music fadeout 6
        h "It's a tricky thing - I know what people would consider right or wrong most of the time, but..."
        m talk "You don't feel guilt?"
        show h 2neu with dissolve
        h "No. I don't think so."
        "He's turning out to be a completely different person that I thought him to be."
        play music "ost/hospital.ogg" fadein 7
        m uncom "My second question is: are you actually schizophrenic?"
        show h 2sidesmile with dissolve
        "He laughs, but it's different than the kind I usually hear."
        show h 2smile with dissolve
        h "No, that is fair. Do I fake the delusions, the voices, the dreams, all of that?"
        show h 2talk with dissolve
        h "I don't. I don't even exaggerate them."
        show h 2sidetalk with dissolve
        h "I can't quite... control myself when these happen. It's a panic. Sometimes I don't even remember what happened when I was like that."
        show h 2talk with dissolve
        h "The only thing I do fake is my ability to understand the situation."
        show h 2sidesmile with dissolve
        h "Every time I didn't understand a question, didn't know you were there, anything like that - that's an act."
        show h 2paintalk with dissolve
        h "I'm not {i}that{/i} unstable. Or stupid."
        show h 2neu with dissolve
        m serious "If you went through so much trouble to establish that elaborate persona, why tell me all of this now?"
        show h 2talk with dissolve
        h "Well, she tricked me into telling you."
        show h 2sidetalk with dissolve
        h "I... I freaked out. I wasn't thinking straight."
        show h 2calmtalk with dissolve
        h "I didn't know what I did wrong, and... well, my panic's what really exposed me."
        show h 2neu with dissolve
        m talk "By \"she\" you mean the girl in black?"
        show h 2calm with dissolve
        "He nods."
        show h 2neu with dissolve
        m fab "So she wasn't a lie?"
        show h 2talk with dissolve
        h "Everything I said I see was the truth."
        show h 2neu with dissolve
        m angrytalk "What about the forest?"
        show h 2calmtalk with dissolve
        h "It's... a memory."
        show h 2neu with dissolve
        m talk "Are you sure?"
        show h 2sidetalk with dissolve
        h "It's vivid. Much more so than the others."
        show h 2frust with dissolve
        h "I tried to be diplomatic about it before because I know you didn't like me being stubborn, but..."
        m frust "I didn't -"
        stop music fadeout 5
        show h 2talk with dissolve
        h "Now that we're being honest, it's not a dream. It happened."
        show h 2angry with dissolve
        m boretalk "Let's say you're right and it really happened."
        show h 2neu with dissolve
        m angry "Why are you there?"
        show h 2dead with dissolve
        h "...."
        "I'm not sure what he's looking at."
        show h 2deadtalk with dissolve
        h "{i}\"She led me here\"."
        show h 2sidetalk with dissolve
        h "That's all I remember."
        show h 2siden with dissolve
        m trigger "Is that referring to that girl in black?"
        show h 2talk with dissolve
        play music "ost/neutral.ogg" fadein 6
        h "I think so. She has some connection to the forest."
        show h 2neu with dissolve
        m fabtalk "Well, Charlie -"
        "I pause."
        m talk "Should I call you that at this point?"
        show h 2sidesmile with dissolve
        h "Why not? It would be weird to change it now."
        show h 2neu with dissolve
        m fabtalk "I think we have a lot to discuss during our next few sessions."
        show h 2talk with dissolve
        h "You'll keep seeing me?"
        show h 2angry with dissolve
        m conf "Of course. I still want to help you."
        show h 2sidetalk with dissolve
        h "I... didn't expect that."
        show h 2neu with dissolve
        m talk "At least now you can be honest with me. You don't have to hide behind this mask anymore."
        show h 2siden with dissolve
        h "It's nice to be able to talk to someone honestly."
        show h 2neu with dissolve
        m flirt "I'm glad you feel that way. I'll see you tomorrow."
        show h 2calmtalk with dissolve
        h "Goodbye, [name]."
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        hide screen easymeter
        hide screen bluemeter
        "He leaves my office and I smile to myself."
        "That wasn't half as bad as I thought."
        "He trusts me now. He knows he can be honest with me."
        "If that's what took me two weeks to achieve, then hell, it was worth it."
        jump patientsattack
    elif day == 19:
        jump breakevent1
    elif day == 20:
        jump breakevent2
    elif day ==  21:
        jump breakevent3
##########################        
    elif day == 22:
        scene bg mcliving with dissolve
        if SunLink>0 and social>0 and social<17:
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
        elif social==17:
            "I invited Dr. Young to come to my house today."
            "But... I still have a lot of time left until the afternoon."
            "In the end, I decided to open a book I never had the time for, so there's that."
            scene black with dissolve
            $renpy.pause()
            play sound "knock.ogg"
            scene black with hpunch
            "Oh! That must be him."
            "I get up to open the door."
            $renpy.pause()
            play music "ost/ascare.ogg"
            show ascare with hpunch
            pause 0.3
            play sound "ost/ascare.ogg"
            show ascare with vpunch
            pause 0.3
            show ascare with hpunch
            scene black with vpunch
            stop music
            m wut "...!"
            nt "Who -"
            show mcshock with dissolve
            $renpy.pause()
            "There... {i}there's nobody at the door{/i}..."
            "{i}It's fine. It was nothing."
            $renpy.pause()
            "Nothing... at all."
            scene black with dissolve
            "God, all this stress is taking a toll on me."
            $renpy.pause()
            scene bg mcliving with dissolve
            "Another half hour passes with me puzzled over what the hell was behind my door before I hear another knock on the door."
            scene black with dissolve
            "This time it's actually who I was expecting."
            jump youngvisit
        else:
            "I spend the first half of the day reading. I never had it in me to open this book before, but..."
            show drk with dissolve
            "It was Jane's. I got it along with a box full of her stuff. I'm not sure why I ever kept any of it."
            play music "ost/jane.ogg" fadein 8
            "{i}\"From the Moon to the Sun: A beginner's guide to tarot readings\"{/i}. On the cover is an elaborate, stylized illustration of the sky."
            "I still remember when she first got her deck. She was so excited."
            "I was never into the occult, but the joy she got out of that... I wouldn't dream of taking that away from her."
            "Suddenly, old memories are flooding back."
            scene black with dissolve
            $renpy.pause()
            nm "Oooh? What are you doing?"
            j "Me? Just setting up."
            nm "What is it? Can I see?"
            j "Sure. Just don't sit on them, dork."
            show janetarot with Dissolve(1.0)
            nt "I pointed to one of the cards."
            nm "What's that? Who's this lady?"
            j "That's the Empress."
            nt "She looked at me, curious."
            j "Why did you ask about her?"
            nm "Dunno. She looks nice."
            j "Huh."
            nm "What?"
            nt "She smiled a little, skimming the pages of her book."
            j "{i}...Nothing."
            nm "You can't do that!"
            j "What am I doing?"
            nm "You're making fun of me! What's so interesting about that queen lady?"
            j "Empress... lady."
            nt "She picked up the Empress card and looked back at me a moment later."
            j "Well... it means you... Hmm..."
            j "That's what we have the book for, right? Don't worry, I'm gonna be an expert at this soon."
            nm "Mom isn't gonna believe you either way. She thinks it's just a game."
            j "...."
            nt "I noticed she was clutching another card in her hands that I hadn't seen before."
            nm "What's that? You're gonna tear it if you're not careful, that's what you said."
            j "Oh? Right..."
            nt "She turned the card in her hand."
            j "That's the Hanged Man."
            nt "I shivered at the thought of a \"hanged man\"."
            nm "Is he okay?"
            j "He's still alive... I guess."
            play sound "knock.ogg"
            stop music
            scene black with hpunch
            "Oh..? Was that a knock?"
            "Who could that be..?"
            "I haven't made plans to meet anyone, have I..?"
            "Either way, I should probably open the door to check."
            "I close the book and put it down safely on the couch before standing up."
            "I guess I need to check the door."
            $renpy.pause()
            play music "ost/ascare.ogg"
            show ascare with hpunch
            pause 0.3
            play sound "ost/ascare.ogg"
            show ascare with vpunch
            pause 0.3
            show ascare with hpunch
            scene black with vpunch
            stop music 
            m wut "...!"
            nt "Who -"
            show mcshock with dissolve
            $renpy.pause()
            "There... {i}there's nobody at the door{/i}..."
            "{i}It's fine. It was nothing."
            $renpy.pause()
            "Nothing... at all."
            scene black with dissolve
            $renpy.pause()
            scene bg mclivingnight with dissolve
            "If... if it was nothing, then..."
            "Why did I hear a knock on my door?"
        jump nextday
    elif day == 23:
        jump nextday
    elif day == 24:
        scene bg mcliving with dissolve
        "It's a nice day today."
        play music "ost/tran.ogg" fadein 6
        "Since I don't have much to do, I decide to take a walk and enjoy the sun."
        show bg sun with dissolve
        "The cool breeze feels refreshing after being holed up in my house for so long."
        "I don't know why this never occured to me before. I should have gone out earlier."
        "Well, better late than never."
        stop music fadeout 3
        "I approach the edge of the forest that stretches for what feels like infinity."
        show bg darkforest with dissolve
        $renpy.pause()
        "...."
        play music "ost/jane.ogg" fadein 6
        "Jane."
        "This is the same forest that Jane would go to."
        "And... the one she went to right before..."
        "...these dreams are making me rethink things I thought I had already forgotten."
        "I sit down on the grass and look into the neverending darkness."
        "Could the forest that Charlie kept talking about have been the same place?"
        "It seems likely."
        "What's drawing people there..?"
        "Jane only ever told me that she wanted to be alone."
        "Is that why... {w}I am here now as well?"
        "What do I want to be alone with?"
        "I think... I feel overwhelmed."
        "Charlie not being Charlie, these dreams of Jane..."
        "Everything seems to connect in my head even though it shouldn't."
        "There's no connection between Jane and Charlie other than this forest."
        "Maybe... maybe Charlie was similar to Jane when he was younger."
        "Maybe he wanted to be alone."
        show drk with dissolve
        "But... if he wants to be alone, why is he so attached to me?"
        "He wanted me to like him. He seems lonely, not like someone who {i}wants{/i} to be alone."
        stop music fadeout 4
        "...."
        "People change. I know I've changed."
        "Until he recovers more of his memories, I can't make judgements about his past."
        "...let's hope he doesn't lose any memories again once I'm back."
        scene black with dissolve
        "I go back to my house thinking about Charlie."
        "...and Jane."
        jump janesuicide
    elif day == 25:
        jump breakend
label charliestar: ## Dr. Young comes to talk about Charlie
    scene bg mc with dissolve
    play music "ost/tran.ogg" fadein 5
    "I'm just gathering my things to leave work for today."
    "Today's session with Charlie was... odd. How he insisted that forest was real."
    "Maybe it was, but what does it have to do with him and his memories?"
    "...And how can I know anything for sure at this point?"
    stop music fadeout 4
    play sound "knock.ogg"
    "Who could that be?"
    "I open the door to see..."
    show s neutral with dissolve
    play music "ost/hospital.ogg" fadein 6
    if StarLink>0:
        m cute "Dr. Young. What a pleasant surprise."
        show s calmsmile with dissolve
        s "It's good to see you again, Ms. Hart."
        show s smile with dissolve
        m talk "What brings you here? I imagine it's something urgent."
    else:
        "That's a new face."
        show s calmsmile with dissolve
        s "I apologize for the intrusion. I am Dr. Young, Charlie's psychiatrist."
        $star="Dr. Young"
        show s smile with dissolve
        m gasp "Oh."
    show s sadtalk with dissolve
    s "I'm here to talk about my patient. He's been acting a little... unusual recently."
    show s talk with dissolve
    s "I was hoping you could shed some light on why that is."
    show s neu with dissolve
    m fabtalk "I can try. Please, take a seat."
    show s neutalk with dissolve
    s "So, Charlie... He seems very enthusiastic about you, so you must be doing well."
    show s neutral with dissolve
    m gasp "He said something about me?"
    show s calmsmile with dissolve
    if StarLink>0:
        s "Yes, quite a bit, actually."
    else:
        s "Yes, he's very eager to talk about you - I was actually hoping to meet you at some point."
    show s smile with dissolve
    m boretalk "This is only my second week of working with him, but he does seem very friendly, at least compared to my other patients."
    show s talk with dissolve
    s "That, he definitely is. Which brings me to why I came here today."
    show s calmtalk with dissolve
    s "He has been slightly... melancholic recently. He seems... tired, strangely enough."
    show s neutalk with dissolve
    s "Has he been acting unusually during your sessions as well?"
    show s neutral with dissolve
    menu:
        "He has":
            show s gasp with dissolve
            s "What happened?"
            show s sad with dissolve
            m serious "Just today, he seemed very... on edge."
            show s neutalk with dissolve
            s "Why was that?"
        "Not that I've noticed":
            m frusttalk "No, he seemed normal for the most part..."
            show s neutalk with dissolve
            s "He did?"
            show s neu with dissolve
            m talk "Actually... something strange came up today."
    show s neutral with dissolve
    m fab "You see, I've been trying to help him regain his lost memories from before he got here."
    show s talk with dissolve
    s "And how is that going? As far as I know, he's only recovered very small parts of them."
    show s neu with dissolve
    m talk "I've been asking him about what he thinks he remembers - his childhood, whatever else he can come up with..."
    m frusttalk "And he's really fixated on the idea of this forest... he's absolutely convinced he must've been there at some point."
    show s neutral with dissolve
    m serious "I... try not to jump to concusions, so naturally I am a little..."
    show s calmsmile with dissolve
    s "Skeptical?"
    show s smirk with dissolve
    m neu "Yes. And... he seems to interpret that as my lack of trust."
    show s paintalk with dissolve
    s "Oh. I am very sorry to hear that."
    show s sad with dissolve
    m talk "I think I can handle it. He seemed to change his mind about it quite quickly."
    show s neutalk with dissolve
    s "So he didn't seem bothered by it by the end of the session?"
    show s neutral with dissolve
    m fab "No."
    show s calmtalk with dissolve
    s "That still doesn't quite explain his behavior in my office... Do you have any ideas for how to explain that?"
    show s neu with dissolve
    menu:
        "He cares about my sessions more":
            $personal+=1
            show s neutalk with dissolve
            s "Certainly, that is a possibility."
            show s calmtalk with dissolve
            s "He might be more interested in you as a person - you are new in his life, after all."
            show s neutral with dissolve
            m talk "Maybe he tried harder to act friendly around me because he wants me to like him more."
        "He's tired in the afternoons":
            $wrong+=1
            show s neutalk with dissolve
            s "Well, I wouldn't say that's impossible, but..."
            show s calmsmile with dissolve
            s "It seems unlikely, given that he's never had problems like this before."
            show s neu with dissolve
            s "And there's no reason why medicine would affect him that way."
            show s neutalk with dissolve
            s "Now that I think about it... there is one probable cause."
            show s smirk with dissolve
            s "He might act more cheerful around you to make a better impression on you."
        "He's more comfortable around you":
            $empathy+=1
            show s calmtalk with dissolve
            s "Quite possibly, yes. We've been working together for about a year now."
            show s smile with dissolve
            s "I wouldn't put it past him to be more cheerful around people he's met more recently."
        "I have no idea":
            show s calmtalk with dissolve
            s "Well, one thing is for certain - this is personal on his part."
            show s smirk with dissolve
            s "If I were to guess, I would say he's trying harder to make a good impression on you than me."
    m fabtalk "He does seem to care a lot about what other people think about him."
    show s neutalk with dissolve
    s "Yes, that's what I was thinking about."
    show s talk with dissolve
    s "He might be hiding some things from you, as a result of trying to act... well, more likable around you."
    show s pain with dissolve
    s "And... I'm afraid only I am allowed to see these things, despite your best efforts."
    show s neutral with dissolve
    m boretalk "It's possible, but..."
    m talk "Maybe there's a better explanation."
    show s neu with dissolve
    m frusttalk "I... I don't believe that he's holding things back from me. He seems so genuine when I talk to him."
    show s calmtalk with dissolve
    s "I, too, want to see the best in him - he's been my patient for a long time, and I can't say I haven't grown fond of him over time."
    show s pain with dissolve
    "He sighs."
    show s cute with dissolve
    s "I shouldn't take up too much of your time - I'm sure you're anxious to get home at this hour."
    show s smile with dissolve
    m smile "Thank you for informing me, Dr. Young. I'll keep this in mind."
    show s calmsmile with dissolve
    s "I felt it was my duty to discuss this with you. I believe we should cooperate on this - it's the only way we can help Charlie."
    show s smirk with dissolve
    m talk "I like the idea of working together and exchanging information."
    m fabtalk "If I ever encounter something unusual with Charlie, I'll make sure to inform you."
    show s smile with dissolve
    s "Thank you, Ms. Hart."
    play sound "doorclose.ogg" fadein 1
    scene black with dissolve
    "He leaves my office."
    jump afterwork        
label blueafterkiss:
    scene bg mcdark with dissolve
    play music "ost/hospital.ogg" fadein 10
    "The more I think about it, the more bizzare today's events seem to me."
    "Charlie... wasn't himself at all."
    "He acted so... cold and indifferent at the end of our session."
    "...What am I supposed to believe?"
    "Was that the effect of his memories coming back so suddenly?"
    "Could they have really come back, then..?"
    "He was talking about the forest he kept mentioning before... it may be one of the things he remembered."
    "Maybe it was a real memory, then... Or maybe the forest is only imaginary, a strange attempt at rationalizing his situation."
    "I promised him I would help him get his memories back... Has my job been done this quickly?"
    scene bg centralsun with dissolve
    "I'm left with so many new questions today, and no answers..."
    "I suppose it's just the way it is with Charlie."
    "...I cringe a bit at the memory of his kiss... what was that?"
    "I still have no idea why he did it."
    "It makes me feel... somewhat violated."
    "But I won't get discouraged. I promised I would help him, and I will."
    scene bg patients with dissolve
    "I wonder if he's still acting so unlike himself..."
    "I glance inside his room."
    gu "Don't bother, Hart. He's not there."
    show jl neutral with dissolve
    "I turn around to face a familiar nurse."
    show jl neutalk with dissolve
    jl "I hear they moved him to XXI temporarily. Just a safety measure."
    show jl neu with dissolve
    m shock "Huh? What happened?"
    show jl calmtalk with dissolve
    jl "They said he was acting very unusual. They were worried about him, given what he's normally like."
    show jl angry with dissolve
    m trigger "Can I see him?"
    show jl calm with dissolve
    jl "There's no need. He'll be fine."
    stop music fadeout 6
    m talk "Have you informed Dr. Young?"
    show jl neutalk with dissolve
    jl "'Course we have. We have this under control."
    show jl talk with dissolve
    jl "Go home, Hart. Enjoy your weekend, unlike me."
    scene bg sunset with dissolve
    "I make my way outside, seeing there's not much I could've done."
    jump alicehylophobia
    
label charliestar2:
    scene bg mc with dissolve
    "I'm sitting in my office, looking through my notes."
    "I don't feel like walking around, talking to anyone, I..."
    "...I need a break."
    play sound "knock.ogg"
    "Oh? Who's that?"
    m gasp "Coming!"
    play music "ost/tran.ogg" fadein 6
    show s neutral with dissolve
    "I open the door and let Dr. Young in."
    show s sad with dissolve
    s "I'm sorry to bother you during your break, Ms. Hart, but..."
    m regrettalk "It's about Charlie, isn't it?"
    show s neu with dissolve
    s "It is. Have you spoken to him today?"
    m serious "He just left. I'm as surprised as you are, Doctor."
    show s neutalk with dissolve
    s "Well, when it comes to Charlie, I've learned there is no such thing as a surprise anymore, but..."
    show s talk with dissolve
    s "Still, to recover so quickly after what happened on Friday?"
    show s neutral with dissolve
    m neu "Oh."
    show s neutalk with dissolve
    s "I saw him on Sunday and he was acting as if nothing happened."
    show s smile with dissolve
    m talk "Doctor, I really think you should talk to him."
    show s neu with dissolve
    m regrettalk "He... he claims to have lost his memories again. Of last week."
    show s gasp with dissolve
    s "You can't be serious."
    show s angry with dissolve
    m angry "He told me so today."
    show s pain with dissolve
    s "...."
    m gasp "Has this ever happened since he's here? Could it be something they gave him on Friday?"
    show s talk with dissolve
    s "No no, I was there on Friday - I can assure you, he wasn't harmed in any way."
    show s paintalk with dissolve
    s "But this... this has never happened since I met him. I... I didn't think it was possible..."
    show s sad with dissolve
    m angry "So you have no idea what could have caused it?"
    show s calmtalk with dissolve
    s "No. Regrettably, I think you should know more than I do about it."
    show s angry with dissolve
    s "Memory loss like that isn't something that just happens. Not in his state."
    m talk "I know."
    show s talk with dissolve
    s "I think Dr. Sharpe needs to know about this. And the whole staff, actually."
    show s neutral with dissolve
    m fabtalk "Could you inform them? I'm... still trying to piece this together."
    show s calmtalk with dissolve
    s "Of course. I'll do it right away, Ms. Hart."
    show s smirk with dissolve
    m conf "Thank you."
    show s neu with dissolve
    "He walks up to the door to leave, but looks back at me."
    show s talk with dissolve
    s "You look tired. You shouldn't exhaust yourself over this."
    show s neutral with dissolve
    menu:
        "I'm responsible for this":
            show s calmtalk with dissolve
            s "No, you aren't. None of us are."
            show s sad with dissolve
            s "Whatever caused Charlie to be this way is responsible. You can't blame yourself for this."
        "Charlie is my patient":
            show s sadsmile with dissolve
            s "Just as much as he is mine. I'll do what I can to support you."
            show s neutalk with dissolve
            s "But for now, you should relax - nobody here blames you for anything."
            show s smile with dissolve
        "You're right":
            pass
    m boresmile "You're right. Thank you for the help."
    show s cute with dissolve
    s "No problem. I'll see you again soon."
    if StarLink==0:
        $StarLink=1
        show s neutalk with dissolve
        s "Oh, and if you ever want to talk... about anything, really, my office is VII. Feel free to come anytime."
        show s smile with dissolve
        "It might be good to talk to him sometime... he seems to have been here for a while."
        "And on top of that, he's been really kind and helpful... I could use a friend."
    play sound "doorclose.ogg" fadein 1
    hide s with dissolve
    "He leaves."
    "I'm glad I have his support... I feel like I can trust him with this."
    jump patientchoice

label hermitfail: ##doesn't trust MC, bad end
    show htc neu with dissolve
    h "[name]. I've tried so hard to trust you this whole time."
    show htc sad with dissolve
    h "I... I was willing to believe anything you say."
    show htc sad with dissolve
    h "But you just keep lying to me... It hurts."
    h "...."
    show htc side with dissolve
    "He looks away from me in silence."
    "I still have no idea what he's accusing me of."
    show htc angry with dissolve
    h "How am I supposed to believe someone who lies to my face and pretends to be the victim?"
    show htm gasp with dissolve
    h "[name], you're a manipulative, dirty traitor. I just wish I'd seen that earlier."
    m "Charlie -"
    show htc neu with dissolve
    h "I don't care what lies you're waiting to spout. I don't want to see you ever again."
    stop music fadeout 6
    scene black with dissolve
    play sound "doorclose.ogg" fadein 1
    scene mc with dissolve
    hide screen easymeter
    hide screen bluemeter
    "He just left."
    "What... was that?"
    "He accused me of something, but gave me no time to defend myself."
    "How was I supposed to know what he meant? This is all just a big misunderstanding..."
    "What do I do?"
    menu:
        "Chase after him":
            play music "ost/tension.ogg" fadein 6
            play sound "doorclose.ogg" fadein 1
            scene bg offices with dissolve
            "I slam the door to my office shut behind me."
            m trigger "Charlie?"
            "He's not here. He must've gone back to his room."
            scene bg central with dissolve
            "I look around, but he's definitely not anywhere near."
            scene bg patients with dissolve
            "His room is... IX, right?"
            "I hurry down the hallway towards the stairs. His room is somewhere near the end..."
            m shock "Charlie? Charlie..?"
            stop music fadeout 4
            "I find his room and open the door."
            show bg charlie with dissolve
            "He's gone. This time, he's really gone."
            "Where is he..?"
            gu "Do you need help, Dr. Hart?"
            play music "ost/emo.ogg" fadein 6
            show su sad:
                ypos 0.1
                xpos 0.35
            with dissolve
            if SunLink>0:
                m gasp "Sue? What are you doing here?"
                show su talk with dissolve
                sue "Just checking the rooms, making sure everyone is where they're supposed to be."
                show su neu with dissolve
                m sadtalk "Charlie, he... he just left my office during a session."
                m angry "I think there's been a misunderstanding, I have to find him and tell him what really happened."
                show su sadtalk with dissolve
                sue "Poor Charlie... I've seen that happen a lot recently."
                show su sad with dissolve
                m freeze "Huh?"
                show su talk with dissolve
                sue "He looks like a shadow of his usual self recently. I don't know what happened."
                show su neu with dissolve
                sue "The last few times, I found him in Office IV. You should look there."
                m fabtalk "He... he does that?"
                show su sadtalk with dissolve
                sue "You had no idea..? [name], he's been depressed for a week now."
                show su sad with dissolve
                sue "I don't know what happened, but you should."
                show su sadsmile with dissolve
                sue "Come on, chase after him. Good luck."
            else:
                "I turn around to face a familiar nurse."
                show su gasp with dissolve
                gu "Is something wrong?"
                show su neutral with dissolve
                m sadtalk "Charlie, he... he just left my office during a session. I-I have to find him. Quickly."
                show su sadtalk with dissolve
                gu "Look in Office IV. I've seen him there on breaks a few times."
            scene bg patients with dissolve
            m sadsmile "Thank you."
            "I leave the patients' rooms hallway."
            show bg central with dissolve
            show bg offices with dissolve
            play sound "knock.ogg"
            m fabtalk "Charlie? Are you there?"
            h "Get lost."
            play sound "doorclose.ogg" fadein 1
            scene bg officeiv with dissolve
            "I open the door."
            show h full with dissolve
            m sadtalk "Charlie, I'm sorry you feel betrayed, but there's been a misunderstanding."
            m talk "I have no idea what you were accusing me of, but I can guarantee that all I've done was what I believed to be right and helpful."
            h "[name]. I won't believe you anymore. Whatever you say."
            "He falls silent and doesn't say a word for a while."
            "I don't think I can do any good here... Only harm."
            m sad "I'm sorry, Charlie."
            play sound "doorclose.ogg" fadein 1
            scene bg offices with dissolve
            "I... I guess this is it. I've tried my best. I really did."
            "What do I do..?"
            "Clearly, Charlie would be better off with a different psychologist..."
            stop music fadeout 5
            "No, why am I still clinging to the hope that things will be normal again? He {i}needs{/i} a different psychologist."
            play sound "knock.ogg" fadein 1
            "I knock on the door to Dr. Sharpe's office."
            d "Come in."
        "Report this to Dr. Sharpe":
            "No, chasing after him now would only do us both harm."
            "It's clear that he doesn't want to talk to me and needs a new psychologist. Someone he can trust."
            "I... I'm no longer the right person for this. I can't help him."
            play music "ost/hospital.ogg" fadein 5
            show bg offices with dissolve
            play sound "knock2.ogg"
            "I knock and enter his office."
            show bg doctor with dissolve
            show d neu with dissolve
            "I open my mouth to say something, but realize we're not alone."
            w "...."
            show d talk with dissolve
            d "Ms. Hart."
            show d frust with dissolve
            m fabtalk "I, umm -"
            show d sidetalk with dissolve
            d "Unless it is a matter that cannot wait, please come back in 10 minutes."
            show d neutral with dissolve
            m boretalk "Of course. I'm sorry."
            play sound "doorclose.ogg" fadein 1
            scene bg offices with dissolve
            show bg mc with dissolve
            "I wait in my office. What was I thinking, just walking in there like that?"
            stop music fadeout 5
            "...."
            $renpy.pause()
            show bg offices with dissolve
            play sound "knock.ogg"
            "I think he should be free by now."
            d "Yes, you may come in now, Ms. Hart."            
        "Give him time":
            $route="no"
            "No, it's too early to tell what I should do."
            "I think Charlie needs his space. Once this all calms down, I'll explain what really happened."
            jump patientsattack
    play sound "doorclose.ogg" fadein 1
    show bg doctor with dissolve
    play music "ost/hier.ogg" fadein 6
    show d neutral with dissolve
    m sad "I apologize for barging in like this, but..."
    m boretalk "One of my patients, Charlie, he..."
    show d cold with dissolve
    m frust "I... don't think I should keep working with him."
    show d neutalk with dissolve
    d "And what makes you say that?"
    show d neu with dissolve
    m angry "We had a... misunderstanding. He didn't even allow me to explain what happened, and then he..."
    m talk "He left my office. In the middle of a session."
    show d neutral with dissolve
    m fabtalk "He said he doesn't want to hear anything I have to say anymore."
    show d frust with dissolve
    d "...."
    show d sidetalk with dissolve
    d "And you want him transferred to a different psychologist?"
    show d neu with dissolve
    m neu "Yes. I think it's what is best for him right now."
    show d talk with dissolve
    d "It can be arranged, but... are you really sure?"
    show d cold with dissolve
    menu:
        "Yes":
            m angry "I wouldn't come here if I weren't out of options."
            show d sidetalk with dissolve
            d "That {i}is{/i} fair."
            show d calmtalk with dissolve
            d "Then... he is not your patient anymore as of now. I will take care of the paperwork."
            show d neu with dissolve
            m boresmile "Thank you, Doctor."
            show d talk with dissolve
            d "It needs to be done sometimes, you are not the first psychologist to request a transfer."
            show d sidetalk with dissolve
            d "...and definitely not the last."
            show d frust with dissolve
            "He pulls out a file from the drawer to my left."
            show d calmtalk with dissolve
            d "There it is."
            show d calm with dissolve
            m neu "...."
            show d neutalk with dissolve
            d "Ms. Hart? Is something wrong?"
            show d neutral with dissolve
            m fabtalk "No, I was just... wondering if I'm needed here for anything."
            show d sidetalk with dissolve
            d "You may leave."
            show d calm with dissolve
            stop music fadeout 5
            m gasp "Oh."
            show d siden with dissolve
            m talk "I... I'll just resume my work, then."
            show d neu with dissolve
            "He glances at me."
            show d talk with dissolve
            d "I do not recall excusing you from it because of this."
            show d siden with dissolve
            "Right."
            play sound "doorclose.ogg" fadein 1
            scene bg mc with dissolve
            "I see one more patient before my work for today is over."
            play music "ost/emo.ogg" fadein 6
            show bg frontsun with dissolve
            "...."
            "Charlie..."
            "I just left him. I didn't even look back."
            "No, it was for the best... He wouldn't cooperate with me."
            "Charlie, not cooperating... what the hell happened to him?"
            "Just yesterday, he was acting like he always does..."
            "...."
            stop music fadeout 5
            "All I know is that something bad happened to him. And it's my fault."
            scene black with Dissolve(1.0)
            "Charlie was my responsibility. And I failed him."
            "What the hell have I done?"
            $renpy.pause(2,hard=True)
            return
        "No":
            show d neu with dissolve
            m talk "I... No, maybe he needs another day to think about it..."
            m fabtalk "If he doesn't want to talk tomorrow, I'll come back to ask for a transfer."
            show d neutral with dissolve
            m gasp "Is that possible?"
            show d calmtalk with dissolve
            d "Very much so. I wish you the best of luck."
            stop music fadeout 5
            play sound "doorclose.ogg" fadein 1
            scene bg offices with dissolve
            "Right. Back to work."
            "...."
            scene bg frontsun with dissolve
            "One more session later, I feel like I've done something really horrible down the line."
            "Where did I go wrong..?"
            "...there's no way to fix it now... is there?"
            jump apathyending
label hermitpanic: ##panics, bad end
    scene black with Dissolve(1.0)
    "His breath is shaky when he steps away from me, backing up into the corner."
    "I... I've never seen him like this."
    "I have no idea what to do."
    stop music fadeout 3
    scene bg mcdark with dissolve
    m trigger "Charlie, listen to me -"
    h "Shut up!"
    play music "ost/fight.ogg" fadein 10
    "He looks around the room frantically with wide eyes before covering them with both hands and shaking his head."
    h "You're not real. Both of you."
    h "None of this is!"
    h "This... this hospital, the patients, the staff - you're all in my head!"
    m sadtalk "Charlie, please -"
    h "I... {cps=5}I never left the forest."
    "He looks around again and lets out a laugh."
    h "I- I remember now... I know who I am."
    h "I know why I'm here."
    "He looks up suddenly, searching for something I can't see."
    h "And you're not taking that away from me!"
    "I don't think he can even see me at this point."
    "That, or he stopped believing I'm real and is ignoring me."
    h "...."
    "He freezes. His eyes go wide again."
    h "I... I never left."
    h "I can't... leave."
    h "...I'll never leave."
    m angry "Charlie, you're not in the forest. This is the hospital."
    m conf "You're safe."
    h "I... {i}I'll never leave!"
    "He hides his face in his hands and drops down to the floor, screaming."
    h "Someone..! {i}Anyone, please..!"
    h "I... I'm going to die here."
    "I approach him slowly."
    m neu "Charlie? Can you hear me?"
    h "...."
    "He's shaking. I have to help him."
    "I sit down on the floor next to him."
    m talk "Charlie? Please, talk to me."
    h "...there's nobody there."
    h "I'm all alone here."
    m fab "You're not. I'm here."
    h "{i}Get away from me!"
    "He hides his face in his hands again. I just made it worse."
    "I get up and take a step back. I have to call help."
    m confusion "I'm so sorry."
    hide screen easymeter
    hide screen bluemeter
    stop music fadeout 6
    scene black with dissolve
    "I open the door and ask a nearby nurse for help. She comes back with two more soon and they take him away."
    "To XXI, they say. He'll be safer there, they say."
    "...."
    "What have I done..?"
    $renpy.pause(2,hard=True)
    return
label hermitslip: ##he realizes MC doesn't know anything and is scared, option to get a good end
    show htc freeze with dissolve
    "He takes a step back, and then another."
    show htm gasp with dissolve
    "What... just happened?"
    h "[name]..?"
    "His voice is shaky and uncertain again."
    show htm sad with dissolve
    m "Charlie, I don't understand. Please, talk to me."
    h "...."
    "He looks terrified. What is this about?"
    h "[name], you... you didn't... know?"
    m "Know what?"
    show htc side with dissolve
    h "You really... didn't know?"
    h "...."
    h "She... she lied to me..?"
    show htm neu with dissolve
    menu:
        "She told you I knew":
            show htc freeze with dissolve
            h "In... in my dream."
            h "Why... why did she... lie to me?"
            m "Because she wanted this to happen."
            h "...."
        "Yes, she did":
            if Hermithonest>3:
                show htc neu with dissolve
                h "And... you didn't. You don't lie to me."
                show htm sad with dissolve
                m "I never lied to you. I only want to help you, Charlie."
                h "[name]... I'll believe you. Just once."
                jump hermitmore
            else:
                h "...."
                show htc side with dissolve
                h "You both did."
                m "What..?"
                show htc neu with dissolve
                h "Yesterday. You didn't want to tell me the truth."
                show htm gasp with dissolve
                m "..!"
                "Does he... remember last week now?"
                m sadtalk "Charlie, wait -"
                jump hermitfail
        "{color=#5185ff}Stay silent":
            h "...."
            show htc sad with dissolve
            h "No, how... how can I know you don't lie as well..?"
            jump hermitpanic
    stop music fadeout 6
    show htc neu with dissolve
    h "She... wanted me to be angry. So I would stop trusting you."
    m "Why do you think she wanted that?"
    "If some part of him wanted this, I need to know why."
    show htc side with dissolve
    h "...."
    show htc sad with dissolve
    h "...I don't know."
    play music "ost/hospital.ogg" fadein 6
    show htm sad with dissolve
    m "Charlie, whatever it is that she told you I know, I don't hold it against you."
    m "Every patient hides some things - it's okay to feel like you can't tell me, at least not yet."
    show htc side with dissolve
    h "I... I didn't want to tell you."
    show htm neu with dissolve
    m "That's okay. You can take your time."
    "That moment right before he realized I don't know... was that what he was hiding from me?"
    "No, I'll know what it was about if he chooses to tell me. I've always been too impatient with secrets."
    h "...."
    h "[name]?"
    show htc side with dissolve
    h "At... this point... it wouldn't make sense to go back to that, right?"
    m "Going back to what?"
    show htc sad with dissolve
    h "Hiding it from you. You... you wouldn't believe me now."
    stop music fadeout 5
    show htm sad with dissolve
    m "If you want to tell me now, you can. I promise I won't judge you for it, whatever it is."
    show htc neu with dissolve
    h "Promise?"
    show htm neu with dissolve
    m "I promise."
    "He takes a deep breath."
    play music "ost/emo.ogg" fadein 6
    h "I... wasn't acting like myself. At all."
    m "Yes, you've been a bit strange this week, I admit..."
    show htc side with dissolve
    h "No. The whole time."
    show htm gasp with dissolve
    m "...."
    show htc neu with dissolve
    h "Since we met. Since I got here, really."
    m "What do you mean, you weren't acting like yourself?"
    show htc side with dissolve
    h "I'm not friendly. I'm not cheerful. I don't like people."
    m "...."
    h "I just... I don't want to be alone. It makes me depressed."
    stop music fadeout 5
    show htc neu with dissolve
    "He leans in a bit to look into my shocked eyes."
    h "Are you okay, [name]..?"
    h "I thought it was obvious at this point."
    play music "ost/tension.ogg" fadein 6
    show htm sad with dissolve
    m "It... it wasn't."
    m "I'll... need a bit of time. To process that."
    m "Sorry."
    show htsmile with dissolve
    "He smiles, but it's different than the kind I'm used to. It's a bitter kind of smile, but a genuine one."
    h "No, it's fine. I have one more thing to say."
    m "What is it?"
    hide htsmile with dissolve
    h "I lied to you on Monday."
    show htm gasp with dissolve
    h "I didn't lose my memories of last week. I remember all of it."
    "...."
    "I... I don't know what to say."
    "He looks at me in silence for a moment before stepping away from me and approaching the door."
    scene black with dissolve
    stop music fadeout 6
    h "I'll just... be on my way, yeah?"
    h "Oh, do me a favor and don't tell my psychiatrist - he won't take it well."
    play sound "doorclose.ogg" fadein 1
    play music "ost/neutral.ogg" fadein 6
    hide screen easymeter
    hide screen bluemeter
    scene bg mc with dissolve
    "Everything I thought I knew about Charlie shattered just now."
    "Who... who even is he? Is there anything I know for sure about him?"
    "...."
    "I have so many questions for tomorrow."
    jump breakchoice
label hermitmore:
    stop music fadeout 6
    show htc neu with dissolve
    hide htsmile with dissolve
    m "Charlie, please listen to me."
    show htm sad with dissolve
    m "I had a dream last night where that girl told you that {i}\"I already know everything\"."
    play music "ost/hospital.ogg" fadein 6
    m "And you have to believe me that I have no idea what she meant."
    m "If there's something you haven't told me, I don't hold it against you."
    m "It's perfectly normal for a patient not to want to talk about some things."
    m "Take your time. You can tell me if you think it can help you, but you don't have to."
    m "There are things I don't need to know about you, just like there are things you don't need to know about me."
    m "I just want us to trust each other... And Charlie, I trust you. No matter what this is about."
    h "...."
    stop music fadeout 5
    show htc freeze with dissolve
    h "So... she really lied to me..?"
    show htm neu with dissolve
    m "I think so."
    h "Why? To... get me to stop trusting you?"
    show htc neu with dissolve
    h "...."
    play music "ost/emo.ogg" fadein 6
    h "[name], did you notice?"
    show htm gasp with dissolve
    m "Notice what?"
    show htsmile with dissolve
    h "You should already suspect what she was referring to."
    "How..? Based on what?"
    menu:
        "Something he said":
            m "Did... did you say something..?"
            m "I'm sorry, I was focused on -"
            h "No. But I'll tell you."
        "Something I said":
            m "Did I... already say it?"
            h "No. But I'll tell you."
        "How he acts":
            $BlueHeart+=2
            m "You're different."
            "He smiles."
            "It's different than any of his previous smiles... more genuine."
            h "I knew you would notice."
    h "[name], I'm being honest for the first time since we've met."
    m "What..?"
    "His smile widens."
    h "I never thought I'd have to tell you, but..."
    h "She ruined it. So there's no point hiding it anymore."
    h "Honestly, I- I never thought I'd tell this to anyone."
    h "The lie was too perfect... wasn't it?"
    m "What are you talking about? Sorry, I don't -"
    stop music
    h "Everything. Everything was a lie."
    "...."
    hide htsmile with dissolve
    h "...."
    play music "ost/tension.ogg" fadein 7
    h "...now that I see that look in your eye, I'm starting to think I shouldn't have told you."
    h "Are... are you going to leave me now?"
    show htm neu with dissolve
    m "No, of course not! Why would I?"
    show htc sad with dissolve
    show htsmile with dissolve
    h "I thought you'd be mad at me for that. I'm sorry, I'm still not quite... there, as far as telling people's feelings goes."
    m "I'm still not sure what you lied to me about, exactly."
    show htc side with dissolve
    h "Oh, right."
    hide htsmile with dissolve
    h "Uh... myself, I guess."
    show htc neu with dissolve
    h "I'm not the person you thought I was. I... I don't act like a child. I'm not friendly or cheerful."
    show htm gasp with dissolve
    h "I don't like people. I just need them so I don't feel alone."
    h "So... that's why I act the way I do."
    h "I... wanted you to pick me. Out of all of your patients."
    stop music fadeout 6
    m "...."
    show htsmile with dissolve
    h "[name]? Are you even there? Or did you just leave your body, like, fifteen minutes ago?"
    show htm sad with dissolve
    m "No, I'm here. I, um..."
    hide htsmile with dissolve
    h "I think I should let that sink in... Yeah, I'll be going."
    scene black with dissolve
    "He steps away from me and approaches the door."
    h "See you tomorrow, [name]."
    "He pauses before opening the door."
    h "Oh, do me a favor and don't tell my psychiatrist - he won't take it well."
    play sound "doorclose.ogg" fadein 1
    play music "ost/neutral.ogg" fadein 5
    hide screen easymeter
    hide screen bluemeter
    scene bg mc with dissolve
    "And just like that, he leaves."
    "Everything I thought I knew about Charlie shattered just now."
    "Who... who even is he? Is there anything I know for sure about him?"
    "...."
    "I have so many questions for tomorrow."
    jump breakchoice
    
label youngvisit:
    $sanity+=5
    $empathy+=5
    "Dr. Young enters my house."
    play sound "doorclose.ogg" fadein 1
    show s cute with dissolve
    s "Hello, Ms. Hart."
    play music "ost/hospital.wav" fadein 6
    m laugh "It's so good to see you ~ Please, come in."
    show s smile with dissolve
    "He takes a seat on my sofa and I follow him."
    show s talk with dissolve
    s "How are you doing, Ms. Hart? Any better?"
    show s neutral with dissolve
    m conf "I'm okay. Just... resting. Recovering."
    show s calmtalk with dissolve
    s "That's good. Hopefully you will be alright by the time you are to return to work."
    show s sadsmile with dissolve
    m smile "Yeah, I think I should be okay."
    show s calmsmile with dissolve
    s "Good, that's good to hear..."
    "I smile. I feel like he was genuinely worried about me."
    show s neu with dissolve
    m fab "How has the hospital been since the attack? Has anything changed?"
    stop music fadeout 4
    show s neutalk with dissolve
    s "Surprisingly little. It seems as though not even a police investigation was conducted."
    show s angry with dissolve
    m gasp "Wait, really?"
    show s calmtalk with dissolve
    s "I haven't seen any policemen on hospital grounds."
    play music "ost/emo.wav" fadein 6
    show s talk with dissolve
    s "I assume that there must be some kind of agreement that lets the hospital handle affairs like that privately."
    show s angry with dissolve
    s "Though... I would rather see the matter resolved officially - you were injured and an incident like that shouldn't be swept under the figurative rug."
    m sad "...."
    m talk "Wasn't an internal investigation being held?"
    show s paintalk with dissolve
    s "There's only so much that a group of guards, doctors and nurses can find out on their own."
    show s calm with dissolve
    s "After all, the police exists for a reason..."
    show s angry with dissolve
    m angry "Why would the hospital want to handle something like that on its own?"
    show s calmtalk with dissolve
    s "Officially... they prefer not to have police bother the patients and disrupt hospital life."
    show s neu with dissolve
    s "And I'm certain there's some truth to that."
    m confusion "You don't believe it?"
    show s talk with dissolve
    s "Not fully. For the staff to want to handle something like this privately, it feels like there must be something they are trying to hide."
    show s neutral with dissolve
    "I lean in, gripping my knees with my hands, before I lower my voice."
    m sadtalk "{i}Do you... really think they have something to hide?"
    show s sadsmile with dissolve
    "The look on his face is one of both sympathy and sorrow."
    show s paintalk with dissolve
    s "I think the chances are higher than I would like."
    show s pain with dissolve
    "I look down at the floor. Is it really possible that something is going very wrong..?"
    "That... the attack was only the beginning..?"
    menu:
        "I don't want to lose hope":
            $side+=10
            show s angry with dissolve
            m regret "Even... even if something is going on, I would rather not think about it."
            show s sad with dissolve
            m sad "Things have been hard for me since I started working here... I don't mean to complain -"
            show s pain with dissolve
            s "It's perfectly understandable. I'm sorry for bringing it up."
            m sadsmile "No, I get it. You're concerned about the staff and the patients, but I'm... I don't think I can take it."
        "I believe you":
            $empathy+=1
            $side-=10
            $StarHeart+=1
            show s angry with dissolve
            m angrytalk "If something really is wrong at the hospital, I need to know."
            m sadtalk "I need to protect my patients, my friends..."
            show s sad with dissolve
            m neu "Please let me know if you learn anything more."
            show s talk with dissolve
            s "I will, Ms. Hart."
    show s neutral with dissolve
    stop music fadeout 5
    "I've been meaning to bring up the topic of Charlie with him..."
    "What I've learned about him. What I falsely believed."
    "But he asked me not to tell Dr. Young... maybe I should hold off on that until I have more information."
    "Since the silence is getting awkward, I decide to ask:"
    play music "ost/tran.wav" fadein 6
    show s neu with dissolve
    m fabtalk "Would you like some coffee?"
    show s calmsmile with dissolve
    s "If that's possible, yes. I've had a long day at work."
    show s smirk with dissolve
    m cute "Sure. It won't take long."
    "I get up and head to the kitchen."
    scene black with dissolve
    "After a few minutes, I return with the coffee."
    scene bg mcliving with dissolve
    show s cute with dissolve
    s "Thank you, Ms. Hart."
    show s smile with dissolve
    m smile "No problem. I got some, too."
    "I sit down again and steal a glance at him."
    "I'm puzzled... why exactly did he want to visit me?"
    stop music fadeout 5
    "Is this about Charlie..? There isn't much to talk about, as he seems to be doing fine..."
    "So is this just... a personal visit? {w}Does he have an interest in me that... may not be entirely professional?"
    "I assumed we were meeting as friends, but is that really why he came?"
    show s sadtalk with dissolve
    s "Is something bothering you?"
    play music "ost/ship.wav" fadein 5
    show s calm with dissolve
    "He seems to lose his composure for a moment before sitting up straight again."
    show s talk with dissolve
    s "I apologize, that may have been too intrusive of me to ask."
    show s sad with dissolve
    "This might be a good time to inquire about this... or is it..?"
    menu:
        "I'm fine":
            m neu "I'm alright, thank you."
            show s neu with dissolve
            s "I see."
            show s calmsmile with dissolve
            "He seems to have become much calmer."
            show s calmtalk with dissolve
            s "Either way, it seemed reasonable to ask. After everything that you've been through."
            show s smile with dissolve
            "I smile."
            m sadsmile "Thank you for being considerate, Doctor."
        "What makes you think that?":
            show s gasp with dissolve
            s "Oh, I-"
            show s neutral with dissolve
            "He pauses, closes his mouth and looks around the room aimlessly."
            show s neutalk with dissolve
            s "Well, after everything that happened, I would think it appropriate to ensure that you're alright."
            show s talk with dissolve
            s "...Emotionally, that is."
            if StarLink>2:
                $StarHeart+=1
                show s calm with dissolve
                "The silence is heavy."
                show s calmtalk with dissolve
                s "Is... {w}Is it really so strange to inquire about the well-being of someone I care about?"
                m freeze "...."
                m regrettalk "It's not. I was just... confused."
                s "Confused as to what?"
                m confusion "How you... felt?"
                s "...Oh. So that's why."
                "I seem to have made him anxious."
                s "I'm afraid I offer no surprises in that regard. You are a dear friend to me, despite how recently we've met."
                m flirt "I appreciate it. And... I feel the same way about you."
                "He smiles."
                s "It's... surprisingly rewarding, knowing that there's no inbalance in that regard."
                s "Thank you, Ms. Hart."
            else:
                show s smile with dissolve
                s "But now I see that it was a silly question. You seem to be doing well."
                m neu "I am."
                "...."
                "It seems that it was a pointless thing to ask. But if there really is something going on, I'm sure I'll learn eventually."
    scene black with dissolve
    "We keep talking until the sky goes pitch black outside."
    "If there's anything I'm certain of at this point, it's that Dr. Young is a good friend."
    "I trust him, more than I ever trusted Charlie. I hope there are no more surprises ahead of me to change my mind."
    jump nextday
