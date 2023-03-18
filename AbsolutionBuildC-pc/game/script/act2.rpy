define lil = Character("Lily", color='#ffffff', voice_tag="lily")
define my = Character("Maya", color='#ffffff', voice_tag="maya")
define kat = Character("Katya", color='#ffffff')
define sai = Character("Saika", color='#ffffff')
define ver = Character("Veronica", color='#ffffff')
define jsp = Character("Jasper", color='#ffffff')
##action SetCharacterVolume("maya", 0.6)

define a = Character("Alice", color='#ffffff')
define an = Character("Alice", color='#ffffff', screen="cinematic")

default visitkitchen=0
default w4michaelsue=False

default gameon=False
default side=0
default LawSide = False ## if true, the chaos ending is blocked and you support Sharpe
default ChaosSide = False ## if true, the law ending is blocked and you support \"G\"
default Alice=False
default NoDeal=False
default alicedraw=0

image attackers = "sprites/attackers.png"
image bg mcliving = "bg/Living.png"
image bg mclivingnight="bg/LivingNight.png"
image bg mcbed = "bg/MCbed.png"
image bg mcbednight="bg/MCbedNight.png"
image bg mcphone = "bg/MCphone.png"
image bg mcphone2 = "bg/MCphone2.png"
image bg mckitchen = "bg/MCKitchen.png"

image gback 1 = "cg/g1.png"
image gback 2 = "cg/g2.png"
image gback 3 = "cg/g3.png"
image gback 4 = "cg/g4.png"

image g neutral = "sprites/justice/Neutral.png"
image g talk = "sprites/justice/Talk.png"
image g smirk = "sprites/justice/Smirk.png"

image g neu = "sprites/justice/Neu.png"
image g neutalk = "sprites/justice/NeuTalk.png"
image g smile = "sprites/justice/Smile.png"

image g sad = "sprites/justice/Sad.png"
image g sadtalk = "sprites/justice/SadTalk.png"
image g sadsmile = "sprites/justice/SadSmile.png"

image g calm = "sprites/justice/Calm.png"
image g calmtalk = "sprites/justice/CalmTalk.png"
image g calmsmile = "sprites/justice/CalmSmile.png"

image g frust = "sprites/justice/Frust.png"
image g frusttalk = "sprites/justice/FrustTalk.png"
image g frustsmile = "sprites/justice/FrustSmile.png"

image g regret = "sprites/justice/Regret.png"
image g regrettalk = "sprites/justice/RegretTalk.png"
image g regretsmile = "sprites/justice/RegretSmile.png"

image bg darkforest = "bg/DarkForest.png"

image monitor="bg/g/Monitor.png"
image goff = "bg/g/Off.png"
image gdrawer = "bg/g/drawer.png"

image cam1="bg/g/1.png"
image cam2="bg/g/2.png"
image cam3="bg/g/3.png"
image cam5="bg/g/5.png"
image cam6="bg/g/6.png"
image cam7="bg/g/7.png"
image cam8="bg/g/8.png"
image cam9="bg/g/9.png"
image verror = "bg/g/verror.png"

image bg gpat:
    "bg/g/patients.png" 
    pause 0.1
    "bg/g/patients2.png"
    pause 0.1
    repeat
image bg gcaf:
    "bg/g/cafeteria.png" 
    pause 0.1
    "bg/g/cafeteria2.png"
    pause 0.1
    repeat
image bg gcafp:
    "bg/g/cafeteriap.png" 
    pause 0.1
    "bg/g/cafeteriap2.png"
    pause 0.1
    repeat
image bg gcafc:
    "bg/g/cafeteriac.png" 
    pause 0.1
    "bg/g/cafeteriac2.png"
    pause 0.1
    repeat
image bg grec:
    "bg/g/reception.png" 
    pause 0.1
    "bg/g/reception2.png"
    pause 0.1
    repeat
image bg gout:
    "bg/g/outside.png" 
    pause 0.1
    "bg/g/outside2.png"
    pause 0.1
    repeat
image bg ghall:
    "bg/g/hallway.png" 
    pause 0.1
    "bg/g/hallway2.png"
    pause 0.1
    repeat
image bg gpsych:
    "bg/g/psychologists.png" 
    pause 0.1
    "bg/g/psychologists2.png"
    pause 0.1
    repeat
image bg gcentr:
    "bg/g/central.png" 
    pause 0.1
    "bg/g/central2.png"
    pause 0.1
    repeat
image bg gthird:
    "bg/g/third.png"
    pause 0.1
    "bg/g/third2.png"
    pause 0.1
    "bg/g/third.png"
    pause 0.1
    "bg/g/third2.png"
    pause 0.1
    "bg/g/black.png" with dissolve
    pause 0.1
    "bg/g/black2.png" 
    pause 0.1
    "bg/g/black.png"
    pause 0.1
    "bg/g/third2.png" with dissolve
    repeat
image bg gface:
    "bg/g/face.png" 
    pause 0.1
    "bg/g/face2.png"
    pause 0.1
    repeat 
image bg gbl:
    "bg/g/black.png" 
    pause 0.1
    "bg/g/black2.png"
    pause 0.1
    repeat

image flashlight = "bg/g/flashlight.png"    
image alicerun:
    "bg/g/arun1.png"
    pause 0.1
    "bg/g/arun2.png"
    pause 0.1
    "bg/g/arun3.png"
    pause 0.1
    "bg/g/arun2.png"
    pause 0.1
    repeat

label patientsattack:
    scene black with dissolve
    scene bg offices with dissolve
    play music "footsteps.ogg" fadein 3
    "I decide to take a walk around the hospital on my break."
    if route == "blue" or route == "purple":
        "I feel like I need a breath of fresh air after what just happened."
    scene bg central with dissolve
    "...."
    "The hospital seems oddly quiet right now..."
    stop music fadeout 2
    scene bg patients with dissolve
    play music "ost/tension.ogg"
    "...huh?"
    play sound "ost/jump.ogg"
    show attackers with hpunch
    nt "Three patients approach me suddenly. I don't recognize any of them."
    nt "Where did they come from..?"
    nt "They're staring at me in eerie silence."
    nt "...Something feels very wrong."
    nt "I take a step back, away from them, but they only follow me, nearly cornering me to a wall."
    nt "I could try running, but it doesn't seem very smart and I would feel bad about leaving them like that when they might need my help."
    nm "Um... excuse me, do you need any help?"
    nn "Ughh? Help -?"
    stop music fadeout 4
    nm "Why are you here? I'm a psychologist, I can guide you-"
    play music "ost/fight.ogg"
    show drk with vpunch
    nn "She's one of them!"
    nn "To hell with the doctors!"
    nt "I back away from them, too shocked to say anything."
    nt "I'm trapped."
    nt "I can't run."
    nm "Please, I can explain -!"
    show punchblood with hpunch
    hide punchblood with dissolve
    nt "I get punched in the jaw."
    nn "We won't fall for your excuses anymore!"
    ##sfx
    show punchblood with hpunch
    hide punchblood with dissolve
    show drk 2 with dissolve
    nn "All of you are liars!"
    nn "You just want to use us!"
    ##sfx
    show bg patientsblur with dissolve
    ##sfx
    scene mcblood
    nt "I can barely see anything... My knees are weak, I nearly fall to the ground from the strength of their hits."
    nt "Why are they doing this..? Everyone's doing their best to help them..."
    nt "So why would they mistrust the doctors so much..?"
    nt "My only option is to beg for help and hope someone hears it."
    stop music fadeout 7
    nm "SOMEBODY HELP! Please..."
    scene black with Dissolve (4.0)
    nt "I can't hear anything."
    nt "I can't feel anything."
    nt "I close my eyes and give up."
    $renpy.pause(5,hard=True)
    nn "Oh my god, are you okay?!"
    nn "Hang in there!"
    nt "Someone is next to me. The patients are gone."
    show bg patients with Dissolve(1.0)
    "I open my eyes to see two nurses I recognize."
    $social=0
    show jl neutral:
        xpos -0.2
    with dissolve
    show su sadtalk:
        xpos 0.2
    with dissolve
    jl "Hey, can you hear me? You don't look too good."
    if route == "green":
        pass
    else:
        ##nurses find you treat you and lead to office V
        m scream "What... happened?"
        play music "ost/hospital.ogg" fadein 7
        show jl angrytalk with dissolve
        jl "You got attacked by three patients."
        show su neutral with dissolve
        show jl talk with dissolve
        jl "You're lucky the two of us were passing by - I called everyone in the nurses' office to help out."
        show jl neutral with dissolve
        show su smile with dissolve
        sue "You're safe now - that's all that matters!"
        show jl angry with dissolve
        jl "Don't be so cheerful about it, Sue - she could've gotten herself killed."
        show su sadtalk with dissolve
        sue "That looked scary... I've never seen something like this happen here."
        show su sad with dissolve
        show jl talk with dissolve
        jl "Me neither. You must be really unlucky, Hart."
        show jl calmtalk with dissolve
        jl "Come on. You can't be walking around injured like that."
        scene black with dissolve
        "The nurses lead me to their office through the central hall."
        "To my relief, they only find a few bruises and one small cut."
        "After treating all my injuries, Sue leads me outside."
        scene bg central with dissolve
        show su sadtalk with dissolve
        sue "Can you walk?"
        show su sad with dissolve
        "I nod weakly. I'm still quite dizzy, but I think I can handle myself."
        show su talk with dissolve
        sue "I'm sorry to bother you, but when Dr. Sharpe learned of what happened, he said he'd like to talk to you about it."
        show su neutral with dissolve
        sue "I guess it must be to explain why something like this even took place here... It should probably be looked into."
        show su sadtalk with dissolve
        sue "I mean, patients {i}attacking{/i} a staff member..? I'm sure you know how alarming that must be for him."
        show su sad with dissolve
        m talk "I get it."
        show bg offices with dissolve
        show su neutral with dissolve
        sue "Do you want me to follow you inside?"
        m fab "I think I can handle myself. Thank you."
        hide su smile with moveoutright
        "She nods and leaves me alone with an encouraging smile."
        play sound "knock.ogg"
        d "Come in."
        "I'm suddenly reminded of the first time I entered his office... it seems like such a long time from now."
        jump afterattack
label afterattack:
    ##beginning of scene
    scene bg doctor with dissolve
    show d neutral:
        xpos 0
    with dissolve
    "Instantly, I fall onto one of the chairs, exhausted and disoriented."
    "Dr. Sharpe takes a seat next to me."
    "He looks at me in silence for a moment."
    show d regrettalk with dissolve
    d "How do you feel?"
    show d regret with dissolve
    "For a moment, I'm too surprised by his question to answer."
    "This seems very uncharacteristic of him, but I suppose the circumstances are highly unusual for the both of us."
    menu:
        "I'm fine":
            $professional+=1
            show d sidetalk with dissolve
            d "I cannot fully believe that, given the circumstances, but I take it as a good sign."
        "It hurts...":
            $GreenHeart+=1
            $personal+=2
            show d sad with dissolve
            "Something I can't name flashes through his face."
            show d grieftalk with dissolve
            d "...I understand."
        "I could be better":
            show d sidesmile with dissolve
            d "Ha, I suppose..."
            show d regret with dissolve
            "I smile weakly."
        "Why do you care?":
            show d neutalk with dissolve
            d "I care about the well-being of my coworkers, Ms. Hart."
    show d neutral with dissolve
    "He pauses for a moment."
    show d sadtalk with dissolve
    d "First of all, I feel the need to express how deeply sorry I am for what happened."
    show d frusttalk with dissolve
    d "Something like this has no right to occur in a hospital."
    show d foctalk with dissolve
    d "Patients turning on a staff member who has done nothing wrong..."
    if route == "green":
        pass
    else:
        show d talk with dissolve
        d "All I meant to say is - it should not have happened, and there is no way to justify it."
        show d neutral with dissolve
        "I agree, but I'm not sure why he feels responsible."
        if SilverRouteBroken:
            jump moonmidgameroutefail
        "Sure, he's in charge of the hospital, but there might've been very little that could've been done to stop it."
        show d cold with dissolve
        m sad "Do you know who these patients were? Why were they free if they acted aggressively?"
        show d frusttalk with dissolve
        d "These were... particularly troublesome patients, Ms. Hart."
        show d foctalk with dissolve
        d "They all spend the majority of their time here isolated from the others."
        show d cold with dissolve
        "That doesn't sound fair..."
        m fabtalk "Why is that?"
        show d regrettalk with dissolve
        d "They are not like the patients you see, Ms. Hart. There is nothing we could have done for them."
        show d frust with dissolve
        m angry "So where did they come from?"
        show d neutalk with dissolve
        d "Right before the attack, one of them was about to be transferred into room XXI, and anoher one - out of it."
        show d foctalk with dissolve
        d "We usually have everything under control at times like this."
        show d neutral with dissolve
        m fabtalk "What about the third one?"
        show d frusttalk with dissolve
        d "From what we know so far, it is possible that he was freed out of his room by the two others after they escaped."
        show d neu with dissolve
        m angry "Why would they want to escape?"
        show d frusttalk with dissolve
        d "Some patients here lack the ability to understand their situation. They feel threatened by our staff."
        show d regret with dissolve
        "That's horrible..."
        show d neutral with dissolve
        m serious "I hope you can explain what happened and ensure these patients can never hurt anyone again."
        show d frust with dissolve
        "Not to mention the threat they could've posed to the others... If all three of them barged into some other patient's room, they would be completely defenseless."
        "I hate to imagine the things that could've happened... A part of me is glad only I got hurt."
    show d talk with dissolve
    d "Now..."
    show d frusttalk with dissolve
    d "The reason I asked you to come here is something I am very reluctant to do."
    show d regret with dissolve
    if route=="blue":
        d "It -"
        show d neu with dissolve
        play sound "knock.ogg" 
        $renpy.pause()
        d "Come in."
        show d neutral:
            ease 0.5 xpos 200
        show s sadtalk:
            xpos -200
        with dissolve
        s "I -"
        show s sad with dissolve
        "He pauses to catch his breath. Has he ran or something..?"
        show d neu with dissolve
        d "...."
        show d sidetalk with dissolve
        d "Should I be... concerned, Charles?"
        show d siden with dissolve
        show s talk with dissolve
        s "No, it's just... I heard about what happened. To Ms. Hart."
        show s sad with dissolve
        "He looks at me with genuine concern."
        show s paintalk with dissolve
        s "I'm so sorry. It sounded horrible."
        show s pain with dissolve
        show d neutral with dissolve
        "Dr. Sharpe glances at Young, then at me, in silence."
        show d neutalk with dissolve
        d "Well, since you are both here, I was just about to inform you, Ms. Hart:"
        show d frust with dissolve
        if day==12 or day==19:
            d "You are unfit to be back here on Monday."
        else:
            d "You are unfit to be back here tomorrow."
        show s neutral with dissolve
        show d talk with dissolve
        d "I am giving you until next Monday to recover. Is that acceptable?"
        show d neu with dissolve
        "I nod. It seems very generous, in fact."
        show s calmtalk with dissolve
        s "What about the patients? Who will take care of them?"
        show s neutral with dissolve
        show d cold with dissolve
        "He turns to look at Dr. Young again."
        show d talk with dissolve
        d "They will remain under the exclusive care of their psychiatrists. It is only a single week, and there is no way to arrange substitute psychologists on such a short notice."
        show d calm with dissolve
        "I'm glad Charlie is in good hands, at least... even though at this point, I doubt that he can care about me being gone."
        show d neutalk with dissolve
        d "Now, Ms. Hart..."
        show d siden with dissolve
        "He glances at the time."
        show d calmtalk with dissolve
        d "I should not take any more of your time. You are free to leave."
        show d neu with dissolve
        show s sad with dissolve
        stop music fadeout 6
        "Dr. Young helps me up and opens the door."
        show s gasp with dissolve
        s "Here, I'll walk you out."
        show s smile with dissolve
        m gasp "Oh, I can -"
        show s cute with dissolve
        s "Don't worry. It's a pleasure."
        "I leave the office and Dr. Young is about to close the door behind us before -"
        show d coldtalk with dissolve
        d "Charles?"
        show d cold with dissolve
        show s talk with dissolve
        s "What is it?"
        show s sad with dissolve
        show d calmtalk with dissolve
        d "Once you are done escorting Ms. Hart outside, would you mind coming back here for a moment?"
        show d siden with dissolve
        d "There is something I want to ask you."
        show d neu with dissolve
        show s angry with dissolve
        s "Of course."
        play music "ost/tran.ogg" fadein 6
        play sound "doorclose.ogg" fadein 1
        scene bg offices with dissolve
        show bg central with dissolve
        m uncom "What was that about?"
        show s sadtalk with dissolve
        s "To be honest, I have no idea."
        show s pain with dissolve
        s "But it must be important if he bothers to talk to me about it."
        "I hear a tinge of bitterness in his voice."
        show bg cafe with dissolve
        show s neutral with dissolve
        "We make our way to the first floor. It's really nice of him, offering to walk me outside like that."
        "I remind myself to thank him for this."
        "I imagine leaving the hospital alone after something like this would be much less pleasant."
        show bg front with dissolve
        show s cute with dissolve
        s "Here we are."
        show s smile with dissolve
        m flirt "Thank you, Doctor. You've been such a great help."
        show s calm with dissolve
        s "Oh, it's just a few minutes..."
        show s neutral with dissolve
        m gasp "No, I mean... everything. Helping me out with Charlie, telling me more about this place, I..."
        m smile "I don't know who could've done that for me if it weren't for you."
        show s kawaii with dissolve
        "He laughs."
        show s laugh with dissolve
        s "You flatter me, Ms. Hart."
        show s sadsmile with dissolve
        s "Really, it's nothing. I'm just happy to help."
        m bored "...."
        show s neu with dissolve
        m fabtalk "So... I'll be gone for over a week."
        show s neutral with dissolve
        s "I'll be watching over Charlie, if that's what you were worried about."
        m conf "I know you will, Doctor."
        m regrettalk "I just... wish I could stay in touch. I'll get worried about work if I don't know what's going on."
        show s gasp with dissolve
        s "Would you like to exchange phone numbers? That way you can just call me if you need anything."
        show s neu with dissolve
        "How did I not think of that..?"
        m cute "Yes, that would be great. Thank you."
        scene bg sun with dissolve
        "We exchange phone numbers with Dr. Young and part ways."
        "On the way home, my mind wanders back to my recent sessions."
        scene black with dissolve
        "It's a shame I have to leave work today, of all days... I felt like I was starting to understand."
        "If I could see Charlie again tomorrow, maybe I could learn why he acted the way he did."
        "Well, let's hope nothing bad happens while I'm gone."
        jump nextday
    d "...It is clear to me that you are injured and in shock after what happened."
    show d talk with dissolve
    d "You need time to recover, both physically and mentally."
    show d sidetalk with dissolve
    d "That is why I have no choice but to give you some days to rest at home."
    show d calmtalk with dissolve
    d "You are not in the state to be back here tomorrow, do you understand?"
    show d neu with dissolve
    "I nod."
    show d frusttalk with dissolve
    d "Given your injuries, and the psychological damage that must have been inflicted upon you, you should rest until..."
    if route=="green" or route =="golden":
        show d talk with dissolve
        d "...Monday. Five days should be enough."
    else:
        show d talk with dissolve
        d "Next Monday. I hope having a whole week to yourself can help you fully recover."
    show d neutral with dissolve
    "I didn't actually think I would be excused from work temporarily, but it seems reasonable."
    if route == "red" and DevilFreed == False:
        show d sidetalk with dissolve
        d "There is one more thing I forgot to mention, Ms. Hart."
        show d neutral with dissolve
        m fab "What is it?"
        show d frusttalk with dissolve
        d "Regarding one of your patients..."
        show d frust with dissolve
        "I freeze. Could he be talking about Michael..?"
        show d talk with dissolve
        d "Mr. Burnett seemed very... quiet today."
        show d regrettalk with dissolve
        d "I am sure you realize this isn't what I have come to expect from him."
        show d frust with dissolve
        "I keep forgetting Sharpe is also his psychiatrist."
        show d cold with dissolve
        m boretalk "We've... had a bit of a disagreement regarding him, um... past."
        show d regrettalk with dissolve
        d "I see. It must have been a difficult subject to address."
        show d regret with dissolve
        "I nod."
        m serious "I didn't exactly... expect him to react the way he did."
        show d neutalk with dissolve
        d "Everyone has things they would rather not talk about, Ms. Hart."
        show d coldtalk with dissolve
        d "Not just patients. I hope you respect that in the future."
        show d neutral with dissolve
        m talk "I'll keep that in mind."
        $route="no"
    elif route == "silver" and ShadowTalk == False:
        stop music fadeout 6
        show d sidetalk with dissolve
        d "There is one more thing I forgot to mention, Ms. Hart."
        show d neutral with dissolve
        m fab "What is it?"
        show d frusttalk with dissolve
        d "Regarding one of your patients..."
        play music "ost/tension.ogg" fadein 6
        show d frust with dissolve
        "I freeze. Could he be talking about William..?"
        show d talk with dissolve
        d "Mr. Moore came to my office today in the morning, requesting a change of his psychologist."
        show d neutalk with dissolve
        d "I assume you know about this..?"
        show d neutral with dissolve
        m frusttalk "I do. He told me of his decision during our today's session."
        show d coldtalk with dissolve
        stop music fadeout 5
        d "And you have no objections?"
        show d cold with dissolve
        m talk "It's what he wants."
        show d sidetalk with dissolve
        play music "ost/tran.ogg" fadein 6
        d "I see."
        show d regret with dissolve
        d "It is rather unfortunate..."
        show d coldtalk with dissolve
        d "Mr. Moore has been here far too long for his own good, and opposed far too many psychologists."
        show d cold with dissolve
        m regrettalk "It seems I wasn't fit for it, either."
        show d regrettalk with dissolve
        d "It is surprising to me that he never requested to be reassigned to a different psychiatrist, though."
        show d neutral with dissolve
        m fabtalk "I think he appreciates your approach, Doctor. He mentioned it once."
        show d calmsmile with dissolve
        d "It is always heartwarming to see patients appreciate what we do."
        show d regrettalk with dissolve
        d "I am sorry you were not quite as successful, Ms. Hart."
        show d neutral with dissolve
        m regret "...."
        m talk "I hope you can watch over him when I'm gone."
        show d calmtalk with dissolve
        d "I will, Ms. Hart."
        $route="no"
    else:
        m gasp "So I'll be able to get back to work normally after that?"
        show d smirk with dissolve
        "He seems amused by my determination."
        show d sidetalk with dissolve
        d "Yes, that is what I had in mind."
        show d neutral with dissolve
        "Great. I would hate to lose more days at work than necessary."
    show d cold with dissolve
    "He looks at me briefly."
    show d frusttalk with dissolve
    d "I should not take any more of your time, Ms. Hart. You may leave."
    show d neutral with dissolve
    "I get up slowly and make my way towards the door."
    if route == "green":
        pass
    else:
        play sound "doorclose.ogg" fadein 1
        scene bg offices with dissolve
        "After saying goodbye to Dr. Sharpe, I leave his office."
    if route == "golden":
        jump act2begingold
    scene bg front with dissolve
    "I make my way outside."
    "So this is it... I won't see the hospital again for a while."
    "I suppose it's for the best, but... I feel like I'll be anxious to get back to work."
    scene black with Dissolve(1.0)
    stop music fadeout 5
    if route == "red":
        "Michael... I hope he doesn't hurt himself when I'm gone."
        "He seemed a bit calmer today, so I just have to hope he'll be alright without me."
    elif route == "silver":
        "William seemed really anxious today... I hope nothing happens to him when I'm gone."
        "Will I have more dreams about his shadow..? I really hope what he said today isn't true..."
    elif route== "purple":
        "I... What happened with Edward today was just... I couldn't have expected this."
        "I'm glad he seemed happy, though. I hope he won't be bothered by me being gone next week."
    else:
        "I recall all the things I have left unfinished in the hospital..."
        "Well, it's not like I'll be gone forever. It's just a couple of days."
        if route == "no":
            "Though... maybe I've... done certain things wrong..."
            "There's a certain feeling at the back of my mind that something is wrong."
            "I hope I'm mistaken, but it won't go away..."
            jump apathyending
    "I go back to my house and spend the rest of the day resting."
    if route == "purple":
        jump dungeon
    jump nextday
##Apathy Ending
label apathyending:
    scene black with Dissolve(1.0)
    $renpy.pause(5,hard=True)
    nn "[name], [name]..."
    nn "Such a waste."
    play music "ost/dream.wav" fadein 6
    scene intro2 with Dissolve(3.0)
    j "You were given a second chance."
    j "Three weeks to redeem yourself."
    j "To prove you're stronger than the past."
    j "I gave you choice. The ability to forge your own path, different than the one that ends in failure and suffering."
    j "I had hope... Hope that despite everything, you would rise like the sun and shine your light on those who know only darkness."
    j "...But you've learned nothing."
    j "You are still a child... unable to do anything but watch."
    j "Truly, you cannot save anyone..."
    j "...not even yourself."
    scene black with dissolve
    $renpy.pause(2,hard=True)
    nn "My, my..."
    nn "Looks like your journey cannot come to an end."
    stop music fadeout 6
    nn "Close your eyes... you may sleep now."
    $renpy.pause(2,hard=True)
    nn "{cps=5}The tale was left unwritten."
    $renpy.pause(5,hard=True)
    return
## MC'S BREAK EVENTS #############################
##################################################
label breakevent1:
    scene black with dissolve
    "It's the first day of my break. I'm not sure what to do with my time, now that I don't have to go to work."
    play music "ost/neutral.ogg" fadein 10
    scene bg mcbed with dissolve
    "I end up staying in bed until 11 AM and rethinking everything that's happened."
    "Over these past three weeks I never really got a chance to stop and think about everything."
    "My new job, for example."
    "I have a feeling I've done everything right, and yet... yesterday's events disturbed me."
    "How is it possible that aggressive patients were allowed to roam the hospital?"
    "Why it happened should definitely be investigated thoroughly."
    "Judging by how concerned Dr. Sharpe seemed, I'm sure he'll be very serious about explaining these events."
    "Once I'm back to work, there will likely be no danger at all - they'll be very careful after something like this."
    "They should've been from the start, though..."
    "Well, I don't hold it against the staff or anyone else."
    "It was just a mistake, and those happen sometimes."
    show bg mcliving with dissolve
    "I'm only worried about these patients - how threatened did they feel by the staff?"
    "Who exactly were they and what drove them to such extremes?"
    "They seemed absolutely convinced that the doctors wanted to... hurt them."
    "It's very disturbing to think that."
    "Aren't they supposed to feel safe at the hospital?"
    if route == "green":
        "Dr. Sharpe seemed really concerned about me as well."
        "It's not like my injuries are that serious, but I understand why he would want me to rest for a few days."
        "Most people would probably be discouraged and leave after getting attacked like that."
        "I swore to myself I would never give up. I swore to Jane after my first day at work."
        "And I don't plan to break that promise - I'm not leaving this job until I can help my patients."
        "I don't care what happens to me in the process."
    elif route is not "golden":
        "I think back to the patients..."
        "Or rather... to {i}one of them."
        "I hate to think what could've happened if I hadn't ended up as the victim of that attack.."
        if SunLink>0:
            stop music fadeout 4
            pause 1
            $renpy.pause()
            play music "ost/ring.ogg"
            "Huh? My phone is ringing."
            "I don't recognize the number... I decide to pick it up anyway."
            play music "ost/sunny.ogg" fadein 6
            gu "{i}Hey, is this [name]? [name] Hart?"
            m conf "That's me. What is it, Sue?"
            sue "{i}Hi! I was just... you know - worried sick about you!"
            sue "{i}After what happened... I mean, that looked {/i}bad."
            sue "{i}How are you holding up?"
            m neu "...."
            m serious "How did you get my number again?"
            sue "{i}I asked around - you didn't think I'd leave you hanging like that, right?"
            m smile "I'm alright. I think the bruises will be gone in no time."
            sue "{i}Oh gee, that's so good to hear ~"
            m talk "So how is everything? I hope the patients aren't scared after something like that..."
            sue "{i}Well, we've been talking to them about it - you'd be surprised how few actually saw it."
            sue "{i}And I hear they were the more stable ones, so no harm done. I hope."
            m cute "That's good."
            sue "{i}Hey, listen..."
            sue "{i}We were worried about you. You know, like the whole staff."
            sue "{i}And I've been thinking... would you like some company?"
            sue "{i}No pressure or anything, it's just that if you want -"
            "She trips over her words and pauses."
            if TempLink>1:
                sue "{i}Julia wanted to see you, as well."
            if StarLink>0 and not route == "golden":
                sue "{i}O-Oh, and I told Dr. Young about it and apparently you two know each other."
                sue "{i}So he was worried as well."
            sue "{i}If, um... if you want, we could, you know... meet up?"
            sue "{i}You live close to the hospital, right? So it wouldn't be a problem."
            sue "{i}What do you think?"
            stop music fadeout 6
            menu:
                "Just the two of us" if TempLink>1 or (StarLink>0 and not route=="golden"):
                    $social=1
                "Sure, come over" if TempLink<2 and StarLink<1:
                    $social=1
                "I'd love to see you and Julia" if TempLink>1:
                    $social=2
                "Bring Dr. Young with you" if (StarLink>0 and not route=="golden"):
                    $social=3
                "The more the merrier" if TempLink>1 and (StarLink>0 and not route=="golden"):
                    $social=4
                "I'm tired, sorry":
                    $social=0
                    sue "{i}Sure, no problem."
                    sue "{i}Get some rest, [name]. See you around ~"
            if social>0:
                if route=="purple":
                    sue "{i}Okay, great! Is tomorrow fine?"
                    m conf "Sure. What time?"
                    sue "{i}Umm... I get out around 4 PM."
                    m cute "It's settled, then."
                    sue "{i}See you then, [name] ~"
                else:
                    sue "{i}Okay, great! Is Monday fine?"
                    m conf "Sure. What time?"
                    sue "{i}Umm... I get out around 4 PM."
                    m cute "It's settled, then."
                    sue "{i}See you on Monday, [name] ~"
            "She hangs up."
    show bg mclivingnight with dissolve
    "I decide to call my parents in the evening to let them know what happened."
    play music "ost/hospital.ogg" fadein 5
    "My mother sounded like she nearly fainted when I told her about the attack. I explained that everything will be okay from now on."
    "I feel like my whole family is going to worry about this now..."
    "Well, I'm an adult and I'm-{w} {i}trying{/i} to be responsible."
    "The rest of the day passes quite uneventfully."
    "Despite everything, I remain optimistic for the week ahead."
    jump janeback1
label breakevent2:
    scene black with dissolve
    "Huh..?"
    scene bg mcbed with Dissolve(1.0)
    "I just had a dream... about Jane."
    "I... haven't even seen her in my dreams since last week."
    play music "ost/tran.ogg" fadein 8
    "I remember that day... faintly."
    "Why is it coming back to me now?"
    pause 1
    if route=="green":
        scene bg mclivingnight with Dissolve(1.0)
        pause 0.5
        scene black with Dissolve(1.0)
        jump janeback2
    show bg mcliving with dissolve
    "Another day where I have no idea what to do with my time..."
    "I think back to my recent sessions..."
    if route == "red":
        "Michael seemed quite stable last time, given what happened."
        "It's a shame I didn't get to talk to him more... Still, I'm glad I could see him after he attacked me and try to explain what happened."
        "That attack... I didn't see it coming at all."
        "I mean... I knew it was risky to set him free in the first place, I knew he might be aggressive, but..."
        "...I didn't expect to provoke him like that."
        stop music fadeout 6
        "Will he really be fine..?"
        "I decide to call the hospital to ask how everyone's doing without me."
    elif route == "silver":
        "William seemed so shaken last time... I really hope he can handle this next week without me."
        "He said his shadow is close to taking over... I gasp at the thought that occurs to me."
        "No... that's not possible..."
        "And yet... what if he loses control without me to help? And... I'll never see him again..?"
        "No, fate can't be this cruel... I need to see him again. I need at least a chance to help."
        stop music fadeout 6
        "But I can't go back to the hospital until next Monday... what do I do?"
        "I decide to call the reception, just in case."
    elif route == "purple":
        if HangedShip:
            "Edward... let me hug him last time."
        else:
            "Edward... let me close to him last time."
        "It was such a huge leap of progress with him -I don't think he's scared of me touching him anymore."
        "With time, he won't be scared of anyone... Maybe he'll even even grow to have a normal life one day."
        "I'm so proud of how far we've come these past three weeks..."
        "I was exposed to all three of them, and I feel like I know exactly what direction I want to go with this."
        "I'm confident in my ability to help."
        "Though... I've gotten quite... attached to them."
        stop music fadeout 6
        "Especially Edward."
        "Even though I'm almost sure nothing bad will happen to them until I'm back, I decide to call the reception to make sure."
    elif route == "blue":
        stop music fadeout 6 ## calls Star instead, longer conversation
        "Charlie... I don't know if I should even call him that at this point."
        "...{i}the person I knew as Charlie{/i} has turned out to be someone completely different."
        play music "ost/emo.ogg" fadein 5
        "I... still can't decide if I'm more shocked, scared, or... angry?"
        "He tricked me for so long, even though I made it clear that I want to do my best to help."
        "What was the point..? He wouldn't leave the hospital anytime soon if he never cooperated."
        "It's all too... confusing. Far too confusing for one session to explain fully."
        "The only thing I can do now is wait."
        "...actually, there's one more thing I can do."
        stop music fadeout 6
        "I remember that Dr. Young left me his phone number in case I want to check how Charlie is doing."
        "I'm... not sure if he would be able to tell if something is wrong, but I can still call."
        "I'm bored out of my mind here, anyway."
        play music "ost/hospital.ogg" fadein 5
        "I call Dr. Young. Let's hope he's not busy at this hour."
        "He picks up pretty quickly."
        s "{i}Hello, Ms. Hart."
        m talk "Hi. I... wanted to ask about my patients."
        s "{i}Sure. How can I be of help?"
        m fabtalk "How is Charlie doing since I'm gone?"
        s "{i}Well, he asked about you the day after, and I informed him of what happened."
        s "{i}He seemed to take it... surprisingly well."
        "Of course he did."
        s "{i}But he did ask if I knew when you'd be back, so I told him."
        m cute "Thank you, Doctor."
        s "{i}It's the least I can do. And how are you holding up, if I may ask?"
        m flirt "Oh, I'm okay. I think I'll be good as new in a couple of days."
        s "{i}Amazing, given what happened."
        m gasp "Was anything done to determine why I was attacked?"
        s "{i}Yes, there was quite a bit of an investigation, actually."
        s "{i}Surprisingly, I don't think anyone was fired. It was some new nurse, she had to watch the patients who broke free."
        s "{i}She said that... her head hurt? Either way, she lost track of the patients right when she was left alone with them for a moment."
        s "{i}Apparently, she promised to be more careful next time. She seemed genuinely sorry."
        m sadtalk "I'm sure she is, who would've thought an accident like that would occur?"
        s "{i}It was a very unfortunate coincidence, yes."
        m neu "I'm surprised she wasn't fired for something like that, actually."
        s "{i}So am I. Well, sometimes it's hard to predict who will get fired and who won't."
        s "{i}I don't know the details of her story well enough to tell, anyway."
        m uncom "I would hate to be that nurse, either way."
        s "{i}Oh, so would I. It must have been horrible."
        m cute "What matters is that only I got hurt."
        s "{i}That's a surprising dose of optimism for someone who got attacked by three mentally unstable men."
        m sad "I hope the patients took it well."
        s "{i}I think they did. None of mine even saw it - it all happened so quickly."
        m sadsmile "It's probably for the best."
        s "{i}It is."
        "I wonder how my return to the hospital after this break will look like..."
        s "{i}Is there anything else you'd like to talk about?"
        menu:
            "Would you like to visit sometime?" if SunLink<1 or social==0:
                s "{i}Me? Umm..."
                m smile "I live close to the hospital, so feel free to come anytime."
                if StarLink>1:
                    s "{i}I'm... slightly surprised, but I'll gladly visit."
                    s "{i}Is Monday fine?"
                    m conf "Sure."
                    "I give him my address and we settle for 4 PM."
                    $social=17
                else:
                    s "{i}Oh, I'm... afraid I will have to refuse."
                    s "{i}Work has been... hectic recently."
                    s "{i}But thank you for the offer, it's very kind of you, Ms. Hart."
                    m "It's fine. See you at work."
            "How are you?" if SunLink>0 and social>0:
                s "{i}It's been a bit hectic since that incident, but... we're all doing well here."
                m cute "That's good to hear."
                s "{i}Thank you for your concern, though."
                m smile "No problem."
                "We chat for a bit longer."
            "That's all, thank you":
                pass
        "I hang up and sit down on the sofa."
        "I'm glad things seem to be going well in the hospital."
        jump janeback2
    else: ## Elizabeth
        stop music fadeout 6
        "I wonder how Elizabeth's doing..."
        play music "ost/ring.ogg" 
        "Huh..?"
        "I pick up."
        stop music
        m fab "Hello?"
        play music "ost/hospital.ogg" fadein 6
        gu "{i}St.Augustine's hospital, am I speaking to Ms. [name] Hart?"
        m neu "That's right. Is something wrong?"
        gu "{i}You are to return to work on Tuesday. It was a last-minute decision, we apologize if you made any plans."
        "Oh? That's unexpected."
        m cute "No, there's no problem."
        gu "{i}Good. Thank you, Ms. Hart."
        "She hangs up."
        "That was... sudden."
        "So... due to some last-minute change, I'll go back to work more quickly?"
        "That's good, sitting at home for so long wouldn't do me any good."
        jump janeback2
    "A nurse picks up."
    play music "ost/hospital.ogg" fadein 10
    gu "{i}St. Augustine's Hospital, how can I help you?"
    "I introduce myself and explain why I'm calling."
    m talk "I'm worried about my patients. I'll be gone for a while, so I want to know what'll happen to them until I'm back."
    gu "{i}Umm... let me check, Miss."
    "She calls me back in a few minutes."
    gu "{i}Everything seems to be in order."
    gu "{i}Apparently, it was difficult to fit them into anyone else's schedule, so they won't have therapy until you're back."
    gu "{i}Are you... worried about anyone in particular, Ms. Hart?"
    "I consider my options..."
    if route=="red":
        m neu "Michael Burnett, room XV. He was quite... unstable, before I left."
        gu "{i}Ah. I understand your concern now."
        gu "{i}But... I don't think there's been any problems with him."
        "Thank god..."
        gu "{i}Is that all? If you wish, we can call you again if anything alarming occurs."
        m cute "Thank you. That would be great."
    elif route=="silver":
        m neu "William Moore, room XIX. I left him in quite an... unstable state."
        gu "{i}Oh."
        m sadtalk "Could you make sure everything is alright until I'm back?"
        gu "{i}Of course. We'll make sure to keep a close eye on him until then."
        m flirt "Thank you so much."
    elif route=="purple":
        m neu "Tom Richards, room XVI."
        m talk "Has anything noteworthy happened the past few days?"
        gu "{i}I haven't heard of anything like that, so everything must be fine."
        m flirt "Thank you."
        "Even though I wasn't really worried, I felt the urge to check on them."
    elif route=="blue":
        "Charlie... is probably fine."
        "He doesn't seem to care much about me, either way. It's probably for the best."
        m fabtalk "No. I'm fine, actually."
        gu "{i}Alright. Is that all?"
        m neu "It is, thank you."
    "I hang up. It looks like I have nothing to worry about."
    if route=="purple" and SunLink>0 and social>0:
        stop music fadeout 4
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
    if route=="silver":
        jump midnight   
    if route=="blue":
        jump janeback2
    else:
        jump nextday

label visitbreak:
    $empathy+=5
    $sanity+=5 ## yes, you get double on William's route
    scene black with dissolve
    show bg mcliving with Dissolve(1.0) # Some general conversation about the patient attack, the investigation into it, and the characters catching up.
    play sound "knock.ogg" fadein 1
    "I'm waiting in my living room when I hear a knock on my door." # This is the time to bring up route-related stuff like the William nightmare, James showing up or the conversation with Caroline.
    m fabtalk "Coming!"
    play sound "doorclose.ogg" fadein 1
    show su happy with dissolve
    play music "ost/sunny.wav" fadein 6
    sue "Hi ~!"
    if social == 2 or social == 4:
        show jl smile:
            xpos -0.3
        with dissolve
        jl "We're here."
    if social>2:
        show s cute:
            xpos 0.3
        with dissolve
        s "Hello, Ms. Hart."
        show s smile with dissolve
    show su smile with dissolve
    m laugh "It's so good to see you! Please, come in."
    if social>1:
        "My guests take a seat on the sofa and I follow them."
        if social == 2 or social == 4:
            show jl talk with dissolve
            jl "So... how have you been, Hart? I'm not gonna lie, we were all worried sick about you after last time."
            show jl neu with dissolve
        else:
            show su sadtalk with dissolve
            sue "How have you been, [name]? I got so worried after that attack..."
    else:
        "Sue takes a seat on the sofa and looks back at me, so I follow her."
        show su sadtalk with dissolve
        sue "How have you been, [name]? I was really worried about you earlier."
    show su sad with dissolve
    stop music fadeout 5
    m conf "I'm okay. Just... resting. Recovering."
    show su sadsmile with dissolve
    sue "Oh, that's good."
    if social>2:
        show s sadtalk with dissolve
        s "Given what I've heard, I'm surprised that nobody else was hurt..."
        show s angry with dissolve
        if social==4:
            show jl angrytalk with dissolve
            jl "You were in your office when it happened, right?"
            show jl neu with dissolve
            play music "ost/hospital.wav" fadein 6
            show s calmtalk with dissolve
            s "I was. After a session, actually."
            show s sad with dissolve
            s "When I heard about what happened, I was worried one of my patients might have gotten caught up in it, since she left my office right before that."
            show su sadtalk with dissolve
            sue "Did she make it to her room in time?"
            show su neu with dissolve
            show s smile with dissolve
            s "She did, thankfully."
        else:
            show su sadtalk with dissolve
            sue "After what happened to [name], I was certain that someone else had to have been hurt..."
            play music "ost/hospital.wav" fadein 6
            show su angry with dissolve
            sue "I'm glad we managed to contain them so quickly. It could have ended much worse if it weren't for that."
    else:
        show su smile with dissolve
        sue "Well, what matters is that you're getting through it."
        play music "ost/hospital.wav" fadein 6
    m fab "How has the hospital been since the attack? Has anything changed?"
    show su talk with dissolve
    sue "Not really, no."
    show su sad with dissolve
    sue "Well, other than the investigation..."
    if social == 2 or social == 4:
        show jl calmtalk with dissolve
        jl "Nobody got fired yet, though. Which is unusual."
        show jl angry with dissolve
        show su sadtalk with dissolve
        sue "I get the feeling that Dr. Sharpe might feel responsible for it. Maybe he thinks it's his fault for not managing everything right."
        show su neu with dissolve
        if social==4:
            show s pain with dissolve
            s "...."
            show s sadtalk with dissolve
            s "That wouldn't be unlike him. He's always been too quick to blame himself for everything that goes wrong."
            show s sad with dissolve
            show jl neu with dissolve
            jl "I forget you two used to be close."
            show s calm with dissolve
            s "It's been a while."
            "There's a moment of silence before he speaks up again."
        else:
            show jl calm with dissolve
            jl "Maybe. Well, I'm sure whichever nurse was responsible is happy to keep her job."
            show su gasp with dissolve
            sue "I think she mentioned feeling sick that day or something..."
            show jl neu with dissolve
            jl "Doesn't sound like a great excuse to me."
            show su angry with dissolve
            sue "True, we don't know if she was being honest."
            show su neu with dissolve
            sue "But she kept her job, so someone must have believed her."
            show jl talk with dissolve
            jl "A certain someone, yeah."
            show jl angry with dissolve
            m gasp "Well, I'm sure he had his reasons."
    if social>2:
        show s talk with dissolve
        s "It's curious how we managed not to get police involved."
        show s neu with dissolve
        m gasp "Wait, really?"
        show s neutalk with dissolve
        s "I haven't seen any on hospital grounds."
        s "I assume that there must be some kind of agreement that lets the hospital handle affairs like that privately."
        show s neutral with dissolve
        show su happy with dissolve
        sue "I think so, yeah. If we called the police every time someone got injured by the patients, I think they would hate us eventually, haha."
        show su sadsmile with dissolve
        sue "Ha... umm..."
        show su sad with dissolve
        "She pauses. I think she might be really stressed about what happened, despite not wanting to show it."
        if social==4:
            show jl angrytalk with dissolve
            jl "Sue? You okay?"
            show jl neu with dissolve
        else:
            m sad "I'm sorry about that, Sue."
        show su laugh with dissolve
        sue "Huh? I'm fine, I'm fine ~"
        show su smile with dissolve
        show s calmtalk with dissolve
        s "We've been handling incidents like this for at least as long as I've worked there. I'm sure something will be done to improve the safety of the coworkers once again."
        show s smile with dissolve
        m conf "Yeah. Let's hope for that."
    elif social==1:
        m fab "How is that going?"
        show su gasp with dissolve
        sue "I think the version they settled on is that the nurse who was handling transferring that one patient into room XXI wasn't feeling well that day."
        show su neu with dissolve
        sue "She mentioned something about her head hurting that day."
        m uncom "Her head? Did she have a migraine or something?"
        show su talk with dissolve
        sue "It got me curious, too, but nobody I talked to knew any more details."
        show su angry with dissolve
        sue "Either way, I doubt she had bad intentions. It was just unfortunate."
        m sadsmile "Yeah. I'd believe that."
        show su smile with dissolve
    stop music fadeout 5
    "I've been meaning to bring something else up this whole time..."
    "So much has happened that the attack wasn't even the first thing on my mind."
    if route=="red":
        "I want to tell them about Caroline. I'm curious what they'll think."
        play music "ost/emo.wav" fadein 5
        show su neu with dissolve
        m fabtalk "So... you know how Michael Burnett is a patient of mine?"
        if social == 2 or social == 4:
            show jl angrytalk with dissolve
            jl "What did he do this time?"
            show jl angry with dissolve
            jl "Other than attack you."
            m freeze "No, that's-"
            show su sadtalk with dissolve
            sue "Wait, he {i}attacked{/i} you?"
            show su sad with dissolve
            show jl neu with dissolve
            m sadtalk "Umm... Yeah, that was-"
            show su angrytalk with dissolve
            sue "Julia, you knew and you didn't tell me?"
            show su angry with dissolve
            show jl calmtalk with dissolve
            jl "I thought you'd be worried sick about her."
            show jl angry with dissolve
            show su sadtalk with dissolve
            sue "And you were right! Oh my god, [name], are you okay?"
            show jl calm with dissolve
            sue "When did that happen?"
            show su sad with dissolve
            m talk "Tuesday, I think..? A few days before I was sent home."
            show su angry with dissolve
            sue "And you weren't sent home then?"
            m angry "I didn't want to be. I was fine."
            show su angrytalk with dissolve
            sue "\"Fine\"? Oh, I'm going to have to have a serious conversation with Dr. Sharpe when I -"
            show jl angry with dissolve
            jl "Sue. She said she's fine. They agreed that she would keep working after that."
            show su sadtalk with dissolve
            sue "Well, yeah but- Ugh!"
            show su angry with dissolve
            sue "Why do bad things have to happen to you so much, [name]..?"
            show su sadtalk with dissolve
            sue "And...{w} Why didn't either of you tell me?"
            show su sad with dissolve
            menu:
                "It was wrong of us":
                    $w4michaelsue=True # necessary for Sue's rank 4 scene
                    m sadtalk "You're right, Sue. We should have told you."
                    show jl calm with dissolve
                    m sad "I know that you care a lot. And that you would want to help if you found out."
                    show su neu with dissolve
                    m regret "I guess I just... didn't really think about it."
                    show su cute with dissolve
                    sue "Aw, [name], don't worry about it. I get it, I'm more surprised that Julia hasn't told me."
                    show jl angry with dissolve
                    jl "...."
                    show su gasp with dissolve
                    show jl talk with dissolve
                    jl "Sorry, Sue. Had a lot of stuff on my mind."
                    show jl neu with dissolve
                    show su smile with dissolve
                    sue "Mhm. I know."
                "We didn't want you to worry":
                    $w4michaelsue=False # necessary for Julia's rank 5 scene
                    m talk "Both me and Julia had good intentions, I assure you."
                    m regrettalk "Sometimes... things happen too quickly. Too much at once."
                    show jl smile with dissolve
                    m conf "And, like Julia said, we didn't want you to worry too much about me."
                    show su neu with dissolve
                    sue "...."
                    show su smile with dissolve
                    sue "Maybe you're right. Sorry about accusing you."
                    show su sadsmile with dissolve
                    sue "I was just... worried you didn't trust me."
            "I'm glad that didn't escalate. I was getting worried."
            m neu "Umm... but about Michael."
            show jl angry with dissolve
        else:
            show su gasp with dissolve
            sue "What about him?"
            show su neutral with dissolve
        m talk "I've been looking for ways to actually help him improve. Enough for him to leave the hospital."
        show su sadtalk with dissolve
        sue "Him? Leave?"
        show su angry with dissolve
        if social>2:
            show s neutalk with dissolve
            s "I hope you don't mind me asking, but is he not the patient who attacked nurses three years ago?"
            show s neutral with dissolve
            s "The one who must be restrained any time he leaves his room?"
            show su neu with dissolve
            m neu "Yes. That's Michael."
            show s calm with dissolve
            s "Well... I am not sure why you were assigned him in particular, given that you are only starting your career at the hospital."
            show s neu with dissolve
            m fab "Are you implying that I can't handle him?"
            show s calmtalk with dissolve
            s "Few have. As for psychologists, none have been able to actually improve his state thus far."
            show s smile with dissolve
            s "But, if that's your intention... I can only wish you the best of luck."
            m conf "Thank you. I believe it's possible."
            show s neutral with dissolve
        else:
            show su neu with dissolve
            m conf "Yes. I believe it's possible."
        m talk "I ended up contacting someone from his past... Someone who was very reluctant to help me."
        show su sad with dissolve
        m sad "I thought their hatred of him would make them unwilling to even talk about what happened between the two of them, but I got a call earlier today."
        show su neu with dissolve
        m siden "They want to meet tomorrow. I'm not sure I can reveal their identity, but I think they might be crucial to the case."
        show su gasp with dissolve
        sue "Ooh! So you're conducting an investigation?"
        show su neu with dissolve
        m fab "Getting a second perspective, mostly. I want to compare what he told me and what I'm about to hear to piece together what really happened."
        if social == 2 or social == 4:
            show jl talk with dissolve
            jl "So you're saying you don't believe either of them?"
            show jl neu with dissolve
            m frust "His perception might have been a bit warped... or he may have been trying to make his actions seem more justified when he was telling me about it."
            m talk "And the person I reached out to..? They seem {i}very{/i} biased because of what happened."
            m angry "So yeah, I think both of them are unreliable sources to some extent. But listening to both of them should amount to something."
            show jl calmtalk with dissolve
            jl "Sounds reasonable enough."
            show jl neu with dissolve
        else:
            show su sadsmile with dissolve
            sue "That sounds reasonable."
        if social>2:
            show s calmtalk with dissolve
            s "You seem to be treating this patient's case very seriously."
            show s neutral with dissolve
            m sadtalk "Of course I am. I want to help."
            show s pain with dissolve
            s "...."
            show s sadtalk with dissolve
            s "That kind of eagerness to help... It's certainly a virtue, but I hope you don't let it blind you to danger."
            show s paintalk with dissolve
            s "...and exhaustion."
            show s pain with dissolve
            m uncom "...?"
            show s sad with dissolve
            s "I've seen it before and I know how much harm it can do. So... be careful, Ms. Hart."
            m trigger "I- I will. Thank you."
            show su happy with dissolve
            sue "Don't overwork yourself, [name] - if it's ever too much-"
            show su neu with dissolve
            m conf "I know. Don't worry about me."
            show s neutral with dissolve
        else:
            m conf "Yeah. I'm hoping to get some valuable information tomorrow."
        stop music fadeout 6
        show su cute with dissolve
        sue "Well, you seem to have it all figured out. I hope you can use what you learn to help him."
        show su sadtalk with dissolve
        sue "Even though... he's definitely not my favorite patient to interact with."
        show su laugh with dissolve
        sue "Still, I wish him the best. I hope he recovers soon ~"
        show su cute with dissolve
        if social == 2 or social == 4:
            show jl calmtalk with dissolve
            jl "Just make sure he's actually ready to leave before you let him get out."
            show jl angry with dissolve
            show su sad with dissolve
            jl "We don't want any more incidents with him. He's done enough harm as it is."
            m talk "I know."
            show jl calm with dissolve
        else:
            show su smile with dissolve
            m "Thanks, Sue. I hope so too."
    elif route=="purple":
        m talk "So, Sue... I have a question for you."
        show su gasp with dissolve
        sue "Huh? What is it?"
        show su neu with dissolve
        play music "ost/tran.ogg" fadein 6
        m fabtalk "You seem to know a lot about what happens around the hospital, so I've been wondering..."
        show su sad with dissolve
        m fab "One of my patients, Tom Richards, has dissociative identity disorder."
        show su talk with dissolve
        sue "Disso-?{w} Ooooh. I remember."
        show su gasp with dissolve
        sue "He's from room XVI, right?"
        show su neu with dissolve
        m conf "That's him."
        m talk "He has three distinct alters. I was wondering if you've met all of them."
        show su sadtalk with dissolve
        sue "Let me think... I don't think I usually get to interact with him that much, but..."
        show su angry with dissolve
        "Sue starts to think."
        if social == 2 or social == 4:
            jl "I think the one we see the most of is just him. Like, the normal him."
            m "Umm... Well, strictly speaking there's no- Umm-"
            jl "I get you. What do you call it, then?"
            m "The term \"host\" comes to mind."
            jl "Spooky."
            show su smile with dissolve
            sue "Right. That's one."
        else:
            show su  with dissolve
            sue "There's the one we see the most of... He doesn't talk much, and when he does he usually gets himself into arguments."
            "That sure sounds like Tom."
        show su sadtalk with dissolve
        sue "Then there's... I think he's separate..."
        show su sad with dissolve
        sue "There's this really quiet one. He's a lot different than the first one."
        sue "But a third..?"
        show su gasp with dissolve
        sue "Oh. Unless you mean..."
        show su neu with dissolve
        m talk "James. Apparently he's been more active recently."
        if social == 2 or social == 4:
            show jl angrytalk with dissolve
            jl "Wait, they're the same guy?!"
            m  "They are."
            show jl neu with dissolve
            "Julia sinks into the sofa."
            show su cute with dissolve
            jl "Woah. Okay."
        show su angry with dissolve
        sue "Yeah, I think I spoke to him once... Didn't really connect them."
        show su laugh with dissolve
        sue "He just seems so different than the other two."
        show su smile with dissolve
        m smile "He is."
        if social>2:
            show s neutalk with dissolve
            s "I've never had a chance to treat a patient with that particular disorder, but it sounds fascinating."
            show s talk with dissolve
            s "Out of professional curiosity, what is it like? Do you treat them as if they are three different patients, or one?"
            show s neutral with dissolve
            m angry "I try to treat them all like their own people. I think it contributes to more trust."
            show s calm with dissolve
            s "That certainly makes sense."
            show s smile with dissolve
            m frust "And... I would feel bad about disregarding their individuality. It's not just that they have different personalities, they..."
            show s sadsmile with dissolve
            m talk "They're completely different people. They have their own memories, feelings, beliefs..."
            show s neutalk with dissolve
            s "I understand. Though it sounds much more complicated than treating most singular patients."
            show s neutral with dissolve
            m fab "I try to approach it like... group therapy, in a way? I'm trying to get them to understand and communicate with one another."
            m flirt "That way, they can actually become functional."
            show s cute with dissolve
            s "I see. That is indeed quite interesting."
            show s smile with dissolve
        show su angry with dissolve
        "Sue looks at me, puzzled."
        show su sadtalk with dissolve
        sue "[name], do you have any idea what could have caused James to become so active recently?"
        show su sad with dissolve
        sue "Now that you mention it, I have been seeing him around a lot this past week or so."
        if social>2:
            show s sad with dissolve
        m regrettalk "I think it has something to do with our therapy. We've started bringing up certain things from his past that were very distressing for him to talk about."
        m "James feels to me like some kind of defense mechanism for situations like that. Ones where his feelings become too strong."
        show su neu with dissolve
        m sad "He's... strange. He seems not to care much about anything or anyone."
        m angry "I think he may have emerged as a kind of barrier from all the negative feelings Tom would otherwise have."
        stop music fadeout 6
        show su smile with dissolve
        sue "I'm no psychologist, but that sounds pretty on point to me."
        show su sadsmile with dissolve
        sue "I know I wouldn't be able to come up with that myself, so there's that ~"
        m uncom "Well... maybe I shouldn't bring up too many details about him. I wouldn't want to reveal more than I'm allowed to."
    elif route=="silver":
        play music "ost/emo.ogg" fadein 6
        "I want to tell them about the nightmare I had... but... I'm going to have to omit some of the details."
        menu:
            "Tell them I had a nightmare":
                $empathy+=2
                m sad "I..."
                show su neu with dissolve
                "I pause. Can I really talk about it..?"
                show su sadtalk with dissolve
                sue "What is it, [name]? Are you feeling okay?"
                show su sad with dissolve
                m regret "I am. But... this whole situation has been... really difficult for me."
                if social>2:
                    show s sad with dissolve
                m sadtalk "I think all the stress and fear has gotten to me... I-"
                "...."
                m sad "I had a nightmare where one of my own patients attacked me."
                show su sadtalk with dissolve
                sue "Oh no..."
                show su sad with dissolve
                if social == 2 or social == 4:
                    show jl angrytalk with dissolve
                    jl "I knew they shouldn't have assigned that freak to you..."
                    show jl angry with dissolve
                    m freeze "Huh?"
                    show jl calmtalk with dissolve
                    jl "Burnett. From room XV."
                    show jl calm with dissolve
                    m regret "No no, it wasn't Michael..."
                    show jl neu with dissolve
                    jl "...oh. Sorry."
                m sadtalk "And... it's been weighing down on me. A lot."
                show su gasp with dissolve
                sue "Have they ever done anything to hurt you? Maybe you should reassign."
                show su angry with dissolve
                m regret "...."
                "He hasn't done anything to hurt me.{w}.. consciously."
                "...or has he?"
                "I... feel like the professional thing to do, if there even is such a thing anymore, would be to ask for him to be reassigned."
                "But can I really stand to do the same as all his previous psychologists? I told him I wouldn't give up on him, I promised him..."
                m regret "...."
                m sadtalk "I'm sorry, I- I just have a lot of feelings about this..."
                show su sadtalk with dissolve
                sue "Oh, [name]... You don't have to decide now."
                show su sadsmile with dissolve
                sue "And if you feel unsafe, that's reason enough to reassign."
                m sad "You really think so?"
                if social>2:
                    show s sad with dissolve
                    s "If I may, I've seen a lot of reassignments over nothing more than mismatched personalities."
                    show s paintalk with dissolve
                    s "Dr. Sharpe, he's-{w} I mean- He tends to be very understanding about this sort of thing."
                    show s neu with dissolve
                    s "...I know he's handled all my transfers very well. So you should absolutely try."
                    show s sadsmile with dissolve
                    s "In my opinion, no good can come from you forcing yourself to help someone who you're afraid of."
                    m "Thank you. I'll think about it."
                else:
                    show su cute with dissolve
                    sue "I do. You should consider it, at least."
                    show su sadsmile with dissolve
                sue "Regardless of what you choose, we're here for you. If you ever want to talk about this stuff..."
                if social == 2 or social == 4:
                    show jl smile with dissolve
                    jl "Yeah. Don't let those guys intimidate you. We can deal with them together."
                    show su laugh with dissolve
                    sue "Yeah!"
                show su smile with dissolve
                m smile "Thank you. I'm glad to have friends like you."
                "That felt a lot better than I expected it to."
            "Don't tell them":
                "No. I invited them to have fun and relax, not to unwrap my newest trauma."
                "I won't let what happened cripple me."
                stop music fadeout 5
                "...."
                "I feel like things have gotten a little awkward due to my silence."
    else:
        "Charlie... He turned out to be completely different than I expected."
        play music "ost/tension.ogg" fadein 6
        "I wouldn't be surprised if I'm the only around the hospital who knows about his secret."
        "...maybe I shouldn't bring it up now."
        "Sue is friends with him... I wouldn't want to break that."
        show su sadtalk with dissolve
        sue "Is something bothering you, [name]?"
        show su sad with dissolve
        m regret "...."
        stop music fadeout 5
        "I'd rather not talk about it."
        show su neu with dissolve
        m talk "No. I'm fine."
        "...things seem to have gotten a little awkward due to my silence."
    "This feels like the time to ask:"
    play music "ost/sunny.wav" fadein 5
    if social==1:
        m neu "Would you like some coffee?"
    else:
        m fabtalk "Does anyone want coffee?"
    show su cute with dissolve
    sue "Yes, absolutely ~"
    if social==2 or social==4:
        show jl calmsmile with dissolve
        jl "I sure do."
    if social>2:
        show s calmsmile with dissolve
        s "If it's not a problem, yes."
    "I get up to head to the kitchen."
    show su neu with dissolve
    sue "Wait."
    m gasp "Hm?"
    show su sadsmile with dissolve
    sue "Are you sure you don't need any help?"
    if social>1:
        "My guests look at me and I feel like any of them would be fine with going with me."
    menu:
        "Invite Sue": # they talk about their feelings of anxiety about the recent events
            $visitkitchen=1
            m cute "Sure, Sue."
            "Sue follows me into the kitchen."
            scene bg mckitchen with dissolve
            show su smile with dissolve
            "I start working on the coffee while Sue watches."
            stop music fadeout 5
            show su angry with dissolve
            "She seems uneasy."
            if social>1:
                m gasp "So... any reason why you wanted to come with me?"
            else:
                m talk "Is something bothering you?" ## is something bothering you my queen?
            show su sadtalk with dissolve
            sue "No, it's just... {w}Well..."
            play music "ost/tension.ogg" fadein 5
            show su sad with dissolve
            sue "Things haven't been the greatest for me ever since that attack."
            m sad "What do you mean?"
            show su angry with dissolve
            sue "It's just... I feel like if it weren't for sheer luck, we might have had a death on our hands."
            show su sadtalk with dissolve
            sue "And... even worse, it would be the death of my good friend."
            show su sad with dissolve
            sue "...."
            "She's still really worried about what happened."
            menu:
                "I survived, it's okay":
                    m regret "I survived, didn't I? I'd rather not dwell on what could have happened."
                    show su talk with dissolve
                    sue "...you're right."
                    show su neu with dissolve
                    "I think that's the most comforting thing I could have said."
                    "Besides, I really would rather not think about the other possible outcomes."
                "I'm glad I invited you, then":
                    $empathy+=2
                    m smile "I'm glad I invited you. I think this should do us both good."
                    show su gasp with dissolve
                    sue "Huh?"
                    m sadsmile "You seeing that I'm okay and me getting to talk to someone about what happened - it's a good thing."
                    show su talk with dissolve
                    sue "Oh, yeah. Absolutely."
                    show su smile with dissolve
                    "She smiles."
                    sue "Thank you, [name]. I'm glad you understand."
                "I'm sorry":
                    m regrettalk "I'm sorry this whole thing is weighing down on you so much..."
                    show su sadtalk with dissolve
                    sue "No, [name], that's not it... {i}I'm{/i} sorry this had to happen to you."
                    sue "You don't need to apologize to me."
                    show su sad with dissolve
            stop music fadeout 5
            m conf "Well... I'm sure things will return to normal once I'm back."
            m cute "We can still hang out on my break after that. It's all going to turn out okay."
            m sadsmile "It's just that things have become a bit turbulent due to that incident."
            show su sadsmile with dissolve
            sue "Yeah."
            "She takes a deep breath."
            play music "ost/hospital.wav" fadein 5
            show su angrytalk with dissolve
            sue "Well, I hope so. If you get caught up in something like that again, I'm going to start suspecting something."
            show su smile with dissolve
            "I laugh."
            m flirt "Yeah. That would be {i}pretty{/i} suspicious."
            show su cute with dissolve
            sue "Mhm ~"
            m talk "...And that would be it for the coffee. Let's get back to the living room."
        "Invite Julia" if social == 2 or social == 4: # she talks about the other nurses
            $visitkitchen=2
            m uncom "Um, sure."
            m fabtalk "Julia, do you mind?"
            show jl smile with dissolve
            jl "Uhh, no. I'll go."
            "Julia follows me into the kitchen."
            scene bg mckitchen with dissolve
            show jl neu with dissolve
            "I start working on the coffee when Julia approaches."
            show jl talk with dissolve
            jl "So... what kind of help did you want?"
            show jl angry with dissolve
            stop music fadeout 5
            m conf "None, really. Just wanted some company."
            show jl calm with dissolve
            jl "Oh, okay."
            "She takes a seat by the kitchen table and rests her head on her hands."
            play music "ost/emo.wav" fadein 6
            show jl talk with dissolve
            jl "So, that whole attack..."
            show jl angrytalk with dissolve
            jl "You may think it's a one-time thing, but stuff like this has been going on for a while."
            show jl angry with dissolve
            m gasp "Huh? What do you mean?"
            show jl calmtalk with dissolve
            jl "Nurses cutting corners, not watching the patients properly, causing accidents..."
            show jl calm with dissolve
            jl "It happens much more than it should. Not always to such a degree, though."
            menu:
                "It doesn't matter who's at fault":
                    show jl talk with dissolve
                    jl "Does it? If we don't know what went wrong, we can't fix it before next time."
                    show jl angry with dissolve
                    m angry "There won't be a next time."
                    jl "I've been working there a bit longer than you and I assure you, there always is."
                "Aren't you one of them?":
                    show jl talk with dissolve
                    jl "One of the nurses? I am, that's why I try to see what the others are doing wrong an avoid it."
                    show jl calmtalk with dissolve
                    jl "I may not seem like it, but I don't slack off. And trust me, many of the others do."
                    show jl angry with dissolve
                "Can something be done?":
                    $empathy+=1
                    show jl talk with dissolve
                    jl "Done? Not really. At least not the way we've been handling this so far."
                    show jl angry with dissolve
                    jl "Firing one nurse {i}after{/i} she causes an invident like that isn't going to prevent the others from being lazy."
            m sjw "Why are you telling me this? It's not exactly making me feel better."
            show jl angrytalk with dissolve
            jl "It's not supposed to. It's unfortunate that you were the victim this time, but the problem is bigger than just one incident."
            show jl angry with dissolve
            m talk "So you think the management should do more to prevent incidents like this?"
            show jl calm with dissolve
            jl "I... Don't tell this to Sue, she'd argue with me, but..."
            stop music fadeout 4
            "She stands up and approaches me."
            show jl talk with dissolve
            jl "I don't think the current management is good at all. I don't think {i}Sharpe{/i} is doing all he can to prevent problems."
            show jl angrytalk with dissolve
            jl "Someone, be it him or whoever is above him, is making the wrong choices. And until they stop, it won't get any better."
            show jl neu with dissolve
            "She steps away from me."
            play music "ost/hospital.wav" fadein 5
            show jl calm with dissolve
            jl "Well, looks like the coffee is done. Let's get back to the living room."
            m neu "...."
            m boretalk "Right."
        "Invite Dr. Young" if social>2:
            m uncom "Um, sure."
            m fabtalk "Do you mind, Dr, Young?"
            show s gasp with dissolve
            s "Not at all."
            "Dr. Young follows me into the kitchen."
            if social==4:
                $visitkitchen=5 ## Sue and Julia alone, enables Julia's confession
                "We leave Sue and Julia alone in the living room for now."
            else:
                $visitkitchen=3
            scene bg mckitchen with dissolve
            show s smile with dissolve
            stop music fadeout 5
            "I start working on the coffee."
            show s calmtalk with dissolve
            s "I take it you didn't invite me here simply because you needed help?"
            show s calmsmile with dissolve
            m talk "You're right, I didn't."
            "I glance at him before returning to the coffee."
            show s neutral with dissolve
            play music "ost/hospital.wav" fadein 6
            m bored "I guess I wanted to talk."
            show s neutalk with dissolve
            s "Did you have anything in particular in mind?"
            show s neu with dissolve
            m neu "I'm kind of curious about what you said earlier... how there was no police involved."
            show s angry with dissolve
            s "At least not on hospital grounds."
            m angry "So you don't know if the incident was reported?"
            show s calmtalk with dissolve
            s "I don't, unfortunately."
            show s pain with dissolve
            "He sighs."
            show s calmsmile with dissolve
            s "But, I'm sure that measures will be taken to prevent this from happening again."
            show s talk with dissolve
            s "I've heard that the overseeing nurse was tasked with examining the shifts around room XXI."
            show s neutral with dissolve
            m gasp "Oh. That's good news."
            show s smirk with dissolve
            s "Certainly."
            "I tap the counter with my fingers."
            show s angry with dissolve
            m sadtalk "So... you aren't afraid of something like that happening again? To you... or one of your patients?"
            show s sadtalk with dissolve
            s "If you're asking me if this incident will somehow begin a series of attacks, then..."
            show s neutral with dissolve
            s "No. I don't think we have a reason to worry about that."
            "He's being very rational about this, it seems. Maybe our panic really is unfounded."
            menu:
                "You're right":
                    m boretalk "You're probably right. I mean... there's no reason to believe that it was anything more than an unfortunate accident."
                    m sad "And maybe it's for the best not to worry too much."
                    show s neutalk with dissolve
                    s "It definitely is."
                "It's still scary":
                    $empathy+=1
                    m regrettalk "I understand, but... the staff has reasons to be afraid."
                    m angry "I don't think we should disregard that."
                    show s sad with dissolve
                    "He looks at me for a moment, seemingly lost in thought."
                    show s talk with dissolve
                    s "You are absolutely right to worry. I may not have made myself clear, but the well-being of staff and patients is definitely a valid concern."
            show s neu with dissolve
            "It seems we agree."
            show s calmtalk with dissolve
            s "I meant no offense. It's clear that it was a difficult experience for you, as it would be for anyone."
            show s sad with dissolve
            m bored "It's okay. I'm just... trying to move on."
            show s talk with dissolve
            s "Isn't that what this visit was supposed to accomplish? To help you move on and feel better?"
            show s neutral with dissolve
            m conf "You're right. I'm glad to have friends I can talk to about this."
            show s cute with dissolve
            s "If you ever need to talk on your break, I am always free."
            show s smile with dissolve
            m smile "Thank you."
            "Looks like it's done."
        "I'm fine on my own": # internal monologue
            if social==2:
                $visitkitchen=5
            else:
                $visitkitchen=4
            m neu "It's only going to be a minute."
            stop music fadeout 5
            scene bg mckitchen with dissolve
            "I get to work on the coffee."
            "To be honest, I think I needed a break..."
            "I don't want Sue to feel bad, but a lot of things have been on my mind that I'm not ready to talk about."
            "...."
            "Deep breaths, [name]."
            play music "ost/hospital.wav" fadein 5
            "Okay. It's ready."
    scene bg mcliving with dissolve
    "I return with the coffee and take a seat on the sofa once more."
    if social==1:
        show su smile with dissolve
        sue "Ah, it smells so nice ~"
        show su cute with dissolve
        "She falls back, sinking into her seat."
        show su happy with dissolve
        sue "I tell you, [name], there's nothing better than hot coffee after a slog of a day."
        show su sadsmile with dissolve
        "I look at her, puzzled."
        m gasp "I thought you enjoyed your work."
        show su laugh with dissolve
        sue "I do. But... it sure is tiring, especially afterwards."
        show su smile with dissolve
        sue "Every time I come back home, I need some time to unwind..."
        m conf "What do you do then?"
        show su talk with dissolve
        sue "I don't know, sometimes I read a book, other times I just sit under a blanket drinking coffee to warm up."
        show su neu with dissolve
        stop music fadeout 6
        m neu "Oh."
        show su laugh with dissolve
        sue "What did you think I do?"
        m bored "I always thought you more of an extravert, I guess."
        show su smile with dissolve
        sue "I am. Everyone needs to recharge their batteries sometimes, though."
        show su sadsmile with dissolve
        sue "I thought you especially might know that."
        m gasp "Huh? Me?"
        play music "ost/tran.wav" fadein 7
        show su cute with dissolve
        sue "Aw, [name], don't look at me like that - you're just as much of a ray of sunshine as I am."
        "I smile. This feels like a genuine compliment coming from her."
        show su smile with dissolve
        m boresmile "Thank you. Though... I never felt like I had your energy."
        show su talk with dissolve
        sue "I've always felt the same way about you."
        show su neu with dissolve
        m freeze "...oh."
        "Maybe it's just that we always see each other at our most energetic, when we're at work."
        m fabtalk "So do you need a lot of time to unwind after work?"
        show su gasp with dissolve
        sue "Hmm... sometimes. {w}You know how it is - one day, nothing really happens, while the next there's a fight or an attack..."
        show su sadsmile with dissolve
        sue "Some days are hard... But I still love working there."
        "I think that's how I feel too."
        m conf "I do too."
        show su happy with dissolve
        sue "I think what I enjoy the most is the people."
        show su smile with dissolve
        sue "The staff, but the patients as well. I'm grateful I met so many of them and could contribute to helping them."
        show su sadtalk with dissolve
        sue "Of course, there will always be accidents, like what happened to you... but most of these people want so badly to get better, to be happy..."
        show su cute with dissolve
        sue "It's made me appreciate what I have and could still have."
        m neu "...."
        show su gasp with dissolve
        sue "I'm sorry, I talk too much sometimes ~"
        show su sad with dissolve
        menu:
            "You do":
                show su talk with dissolve
                sue "Eh, yeah... sorry."
            "It's fine":
                show su laugh with dissolve
                sue "It is? Thanks, [name]."
            "I like it":
                $empathy+=1
                show su laugh with dissolve
                sue "Eh-? [name], you're funny ~"
        show su smile with dissolve
        m fab "So, the patients. Do you have any favorites?"
        sue "Umm... a few, yeah. Out of yours, I think Charlie is my favorite."
        if route=="blue":
            "Charlie... it's good that I haven't told her."
            "He'll have to come to face that on his own... Decide who he wants to be."
            show su gasp with dissolve
            sue "[name]?"
            show su sad with dissolve
            "I realize I went quiet."
            m uncom "Sorry, it's nothing."
        m fabtalk "Charlie, huh? I can see you two getting along."
        show su laugh with dissolve
        sue "He's a sweet guy ~"
        show su sadtalk with dissolve
        sue "It's just a shame that he can't remember his past... I think he's really suffering because of that."
        show su sad with dissolve
        sue "...."
        "She goes silent for a moment before looking back at me again."
        show su talk with dissolve
        sue "What about you? Any favorites?"
        show su neu with dissolve
        m shock "Umm... Well, I'm not really in a position to pick favorites..."
        show su sad with dissolve
        sue "Oh, right. I forgot about that."
        stop music fadeout 3
        show su gasp with dissolve
        sue "Hey, [name]?"
        m trigger "Yeah?"
        show su talk with dissolve
        sue "Do you think your patients will get to leave the hospital soon?"
        show su angry with dissolve
        m uncom "Umm... Why do you ask?"
        show su sadtalk with dissolve
        sue "I'm sure you want them to, we all do, but... Do you think you can do it?"
        show su neu with dissolve
        play music "ost/emo.wav" fadein 5
        menu:
            "I can and I will":
                if sanity>45:
                    $sanity=50
                else:
                    $sanity+=5
                show su cute with dissolve
                sue "That's a lot of confidence to have in yourself."
                show su smile with dissolve
                m conf "I need it if I want to succeed."
                show su talk with dissolve
                sue "Maybe so, but..."
            "Only if they want to leave":
                $empathy+=2
                show su sadtalk with dissolve
                sue "Huh? Why wouldn't they?"
                show su angry with dissolve
                m regret "Some of them... feel like the hospital is the best place for them. That they can't function safely outside of it."
                show su sad with dissolve
                sue "Oh no... How do you deal with that?"
                m talk "I try to learn what causes them to think that way. And what we can do to change it."
                m sad "But I'm not sure if I'm going to succeed."
            "All I can do is try":
                show su smile with dissolve
                sue "Very true, yes."
                show su cute with dissolve
                sue "But it doesn't have to be a bad thing."
        show su sadsmile with dissolve
        sue "You don't have to do it all at once. Some of them have been here for years."
        sue "You're not a miracle worker, [name]. Just someone who wants to help."
        m gasp "Is that what you think about yourself as well?"
        show su smile with dissolve
        sue "Myself, especially. It takes a lot of effort just to not do harm. To do good is... something we can only attempt."
        m conf "But it's something we must attempt. Always."
        show su angry with dissolve
        sue "Attempt, yes. Succeed at it, no - not everything is within your control."
        show su neu with dissolve
        m angry "I think I understand."
        "I didn't expect to be talking to her about this... it's interesting to see her perspective on this."
    elif social==2:
        show sue smile:
            xpos -200    
        with dissolve
        show jl smile:
            xpos 200
        with dissolve
        "Julia grabs her coffee."
        jl "Now that's what I'm talking about. Thanks, Hart."
        show su angry with dissolve
        sue "Why do you call [name] that? You're friends, aren't you?"
        "I glance at Sue, then Julia."
        show jl angry with dissolve
        jl "Well, yeah... {w}Do you think it's a problem, Hart?"
        stop music fadeout 6
        menu:
            "It's not":
                $empathy+=1
                m neu "No, it's not. It's just what Julia prefers, I see no problem there."
                show jl calm with dissolve
                jl "Yeah."
                show su sadsmile with dissolve
                sue "Ah, I see."
            "It is":
                m fab "It does feel like we're less close than you and Sue."
                jl "Uhh... Yeah, we are."
                show su sadtalk with dissolve
                sue "Julia, don't be mean..."
                show su neu with dissolve
                show jl talk with dissolve
                jl "I'm not being mean. I've known you for years."
                show jl angry with dissolve
                "I can see how Julia might be slow to warm up to people."
        show jl neu with dissolve
        "We sit in silence for a moment before Sue speaks up."
        show su gasp with dissolve
        sue "Hey, so you know how I was filling in for Lisa today?"
        show su neu with dissolve
        show jl angrytalk with dissolve
        jl "Again?"
        show jl calm with dissolve
        play music "ost/sunny.wav" fadein 6
        show su angry with dissolve
        sue "Yeah, don't get me started... {w}Anyway, I was fetching some medicine from the basement storage and I found some boxes that were knocked over."
        show jl angry with dissolve
        jl "Huh? Someone sure wasn't paying attention."
        show su sadtalk with dissolve
        sue "Seemed like it. I couldn't leave them like that, so I was late to the patients hallway."
        show su sadsmile with dissolve
        show jl calmtalk with dissolve
        jl "People really should start taking this more seriously. If they make a mess, someone else is going to have to clean it up for them. Ugh."
        show jl neu with dissolve
        show su cute with dissolve
        sue "Sometimes that's a good thing, though."
        show jl gasp with dissolve
        jl "Huh?"
        show su happy with dissolve
        sue "Remember your first day on the job? You forgot to lock the door to the third floor behind you."
        show jl neu with dissolve
        show su sadsmile with dissolve
        sue "We had to evacuate two patients from that floor because of you... And then Mrs. Manera got upset."
        show jl calm with dissolve
        jl "Yeah, you had to escort me to her office."
        m freeze "Wait, really?"
        show su laugh with dissolve
        sue "Don't worry, [name], it was harmless."
        show jl blush with dissolve
        show su cute with dissolve
        jl "Yeah. Some messes are good."
        "She looks at Sue with an unreadable expression."
        show su smile with dissolve
        sue "But that was four years ago. You've gotten better since then."
        show jl calmsmile with dissolve
        jl "You bet I did. You don't have to rescue me anymore."
        show su sadsmile with dissolve
        sue "I didn't mind. I was getting myself into all kinds of messes at that point as well. I still do."
        show jl gasp with dissolve
        jl "Like what?"
        stop music fadeout 5
        show jl neu with dissolve
        show su talk with dissolve
        sue "One time about two years ago, I was supposed to escort that one patient, what was his name...?"
        show jl smile with dissolve
        jl "Don't look at me, I barely remember the current ones. They come and go so quick."
        show su angrytalk with dissolve
        sue "Yeah, I can't remember either. I was escorting him to Dr. Young's office for a session when he..."
        show su angry with dissolve
        "She looks down at the floor for a moment, lost in thought."
        play music "ost/emo.wav" fadein 6
        show su sadtalk with dissolve
        sue "He told me that there's a girl he talks to around the hospital."
        show jl neu with dissolve
        sue "That she tells him things about the staff."
        show su sad with dissolve
        show jl angrytalk with dissolve
        jl "Things like what?"
        show jl angry with dissolve
        show su talk with dissolve
        sue "He knew my birthday, for one."
        show su neu with dissolve
        show jl talk with dissolve
        jl "Probably overheard it somewhere."
        show jl calm with dissolve
        show su gasp with dissolve
        sue "Yeah. Probably... but I felt weird about it the whole day."
        show su sadsmile with dissolve
        if route=="blue":
            "This reminds me of Charlie's hallucinations..."
        show jl talk with dissolve
        jl "So what happened later?"
        show jl angry with dissolve
        show su talk with dissolve
        sue "He kept telling me weird details about the staff for the whole week, until he asked me for a favor."
        show su angry with dissolve
        m gasp "A favor? What could a patient possibly want from you?"
        show su sadtalk with dissolve
        sue "He said that the girl is in trouble. That he needs to see her behind the hospital. At night."
        show su sad with dissolve
        m trigger "...!"
        "That sounds like he wanted to escape."
        m sadtalk "You didn't... let him, right?"
        show su angry with dissolve
        sue "I... did. I thought maybe she was staff? Or something like that."
        show jl calmtalk with dissolve
        jl "No way she was anywhere outside his own head."
        show jl calm with dissolve
        show su talk with dissolve
        sue "That's what I learned when I eventually let him out. He tried to scale the fence."
        show su sadtalk with dissolve
        sue "I had to call the guards on him..."
        show jl neu with dissolve
        sue "I just felt so bad for him... he was getting worse and worse since he started talking about this stuff."
        show su sad with dissolve
        sue "I thought... maybe believing him would make him feel better, at least..."
        show jl talk with dissolve
        jl "You never told me that story."
        show jl smile with dissolve
        "She shrugs."
        show su sadsmile with dissolve
        sue "I guess so many weird things happen that it's hard to keep track."        
    elif social==3:
        show s cute:
            xpos -200
        with dissolve
        s "Thank you, Ms. Hart."
        show s smile with dissolve
        show su laugh:
            xpos 200
        with dissolve
        sue "It smells incredible ~"
        show su cute with dissolve
        m flirt "You're just tired after a long day, Sue."
        show s cute with dissolve
        s "That wouldn't be unlike her."
        show su smile with dissolve
        show s neutral with dissolve
        "Dr. Young turns to Sue."
        show s calmtalk with dissolve
        s "Ms. Peters, you seem like someone who has a lot of energy at work."
        show s neu with dissolve
        s "It must be exhausting, coming back home after that."
        show su gasp with dissolve
        sue "It... kind of is, yeah. But I love my work ~"
        show su sadsmile with dissolve
        show s calmsmile with dissolve
        s "Hm. I used to have that kind of mindset."
        "I laugh."
        show s smile with dissolve
        m laugh "Does working there for long enough do that?"
        show s smirk with dissolve
        s "Maybe."
        show su talk with dissolve
        sue "You were already there when I was hired four years ago... You're one of the few people I remember lasting this long."
        show su angry with dissolve
        stop music fadeout 4
        m confusion "Really? Do people leave this much?"
        show su sadtalk with dissolve
        sue "A lot of people left three years ago, after..."
        show su sad with dissolve
        if SunLink>3:
            sue "You know. What I told you about."
            show s neutalk with dissolve
            s "The investigation? I'm sure that was a factor."
        else:
            "She glances away, anxious."
            show s sad with dissolve
            sue "...I'd rather not talk about it right now."
        show s neutral with dissolve
        m angry "I understand."
        play music "ost/emo.wav" fadein 6
        show su talk with dissolve
        sue "People also tend to get fired after incidents, like that recent attack."
        show su angry with dissolve
        show s neutalk with dissolve
        s "But not this time, strangely."
        show s neu with dissolve
        show su neu with dissolve
        sue "At least not so far, yeah."
        m talk "So... what was the hospital like four years ago? Or five?"
        show su sad with dissolve
        sue "What's there to say? It wasn't much different of a workplace."
        "She shrugs."
        show s paintalk with dissolve
        s "It was under different management, for one."
        show s pain with dissolve
        show su gasp with dissolve
        sue "Ooooh, true. Dr. Sharpe wasn't in charge until... when, exactly?"
        show s neutalk with dissolve
        s "Three years ago."
        show s neutral with dissolve
        show su talk with dissolve
        sue "Right.{w} Weren't you two... friends? What happened with that?"
        show su smile with dissolve
        show s calmtalk with dissolve
        s "He, um... Became too busy with work."
        show s pain with dissolve
        show su sad with dissolve
        sue "Oh. That's sad."
        m sad "It really is."
        show su smile with dissolve
        sue "Well, I think it's fair to say you know him better than anyone around the hospital."
        show su sadsmile with dissolve
        sue "You two used to spend all your breaks together and all. It seemed like you got along really well."
        show s sadtalk with dissolve
        s "I thought we did. But, well, apparently not well enough."
        show su sad with dissolve
        show s pain with dissolve
        m regret "...."
        show s neutalk with dissolve
        s "I'm sorry I keep bringing the mood down. You had questions, Ms. Hart?"
        show s neu with dissolve
        menu:
            "How many of the patients were the same back then?":
                show s calmtalk with dissolve
                s "All of mine are more recent than that."
                show s neutral with dissolve
                "Dr. Young glances at Sue."
                show su talk with dissolve
                sue "None of the current patients were around at that time."
                show su cute with dissolve
                sue "Which is good - people tend to leave after, I don't know... a few months?"
                show s neutalk with dissolve
                s "Yes, that seems to be the typical duration. Two to three months."
                show s neu with dissolve
            "Any other staff members who remember those days?":
                show su gasp with dissolve
                sue "Hmmm... A few, yeah."
                sue "Other than the ones that were already mentioned, there's Julia, of course."
                show su talk with dissolve
                sue "She was hired about a month after I was."
                sue "And... Hmm... I'm sure a few of the other nurses have been around for a while..."
                show su angry with dissolve
                show s talk with dissolve
                s "Like you mentioned earlier, many nurses quit three years ago. We had to fill many gaps in the staff."
                show s neu with dissolve
                show su sadsmile with dissolve
                sue "True. So we're probably in the minority, having worked there for so long."
        m fab "All of that makes me wonder..."
        "I look at both of them before asking:"
        show s neutral with dissolve
        m serious "Are things getting better at the hospital over time?"
        show su gasp with dissolve
        "Sue opens her mouth to speak and closes it soon afterwards, not having collected her thoughts on the topic yet."
        show su angry with dissolve
        show s pain with dissolve
        s "I would like to be an optimist about this. I think that's where I stand."
        m frust "That doesn't sound very optimistic."
        show su sadtalk with dissolve
        sue "Yeah, it doesn't. Why do you say that?"
        show su sad with dissolve
        show s talk with dissolve
        s "Maybe my perspective is skewed, and if so please correct me, but it seems as though patients have been taking longer to leave."
        show s sad with dissolve
        s "I feel like I don't see as many fast recoveries as I did, say, three years ago."
        show su talk with dissolve
        sue "Hmm... What do you think, [name]?"
        show su sadsmile with dissolve
        m angry "Two of my patients have been here for longer than a year. I think that's pretty alarming."
        show su sad with dissolve
        sue "You got the two most difficult ones, I think. For different reasons, of course."
        "Michael and William. They really have been there for a while..."
        m boretalk "And my other patients aren't exactly the easiest to work with, either. {w}Not that I'm complaining."
        show s angrytalk with dissolve
        s "You have the right to complain, I think. Your selection of patients is not exactly fit for someone new to the hospital."
        show s neutral with dissolve
        show su gasp with dissolve
        sue "Yeah, but that's just her patients. I think most people have been getting out the same as they were three or four years ago."
        show su smile with dissolve
        show s calm with dissolve
        s "Maybe. I lack any statistics to prove my point."
        m neu "Well, I can't speak on that."
        m talk "But what about the atmosphere? And our coworkers? Have things improved over time?"
        show su cute with dissolve
        sue "I think the more time I spend here, the more friends I make. Some have left, but new people always seem to appreciate having me around."
        show su smile with dissolve
        sue "So as far as I'm concerned, things have gotten friendlier. What do you think, Doctor?"
        show s neutalk with dissolve
        s "Things have certainly changed. I'm not sure if I can tell if it was a positive change or not."
        show s sad with dissolve
        s "More problems are being handled behind closed doors nowadays, people seem to have more secrets from each other..."
        show s talk with dissolve
        s "We used to hold open meetings with the previous management. Now Dr. Sharpe seems to settle everything with only a select group of people."
        show s angry with dissolve
        s "I'm not saying I need to be included in every decision, but... I feel like I'm less aware of what's happening around the hospital."
        show s calmtalk with dissolve
        s "And I used to be quite well-informed."
        show s neutral with dissolve
        show su neu with dissolve
        sue "Huh."
        show su talk with dissolve
        sue "I never really went to the open meetings, the gossip was enough for me and back then I felt like I had very little to say."
        show su sadsmile with dissolve
        sue "And I don't really mind how Dr. Sharpe handles things. It's less stressful if you mess up and only those involved are aware."
        m neu "He definitely handles things on very private terms."
        show su cute with dissolve
        sue "It's a good thing, I think. Less stress all around."
    else:
        show su laugh:
            xpos -0.3
        with dissolve
        sue "It smells delicious ~"
        show jl smile with dissolve
        jl "That's what I'm talking about. Thanks."
        show s cute:
            xpos 0.3
        with dissolve
        s "Thank you, Ms. Hart."
        show su smile with dissolve
        "Once everyone settles down with their coffee, I decide to speak up."
        m smile "So... since I invited all of you here..."
        show jl talk with dissolve
        jl "Getting interesting, Hart."
        show jl calmsmile with dissolve
        show su gasp with dissolve
        sue "Julia, let her finish-"
        show s sadsmile with dissolve
        "I smile at the two of them."
        show su neu with dissolve
        m cute "I thought while we're all here, we could get to know each other a bit more."
        m talk "All of us, I mean. I know Sue and Julia have a history, but the rest of us don't know the others nearly as well."
        show su happy with dissolve
        sue "What are you thinking? A game?"
        show su cute with dissolve
        show jl angry with dissolve
        jl "Come on, you can't learn shit about a person by playing games with them."
        show s calmtalk with dissolve
        s "I think we should hear Ms. Hart out before making judgements."
        show s neu with dissolve
        m conf "I was thinking of going around the table and having each of us ask a question for everyone else to answer."
        show jl angrytalk with dissolve
        jl "Where's the fun in that?"
        show jl neu with dissolve
        m gasp "Well, they can't be boring questions. But nothing {i}too{/i} weird."
        show su happy with dissolve
        sue "Let's play ~"
        show su smile with dissolve
        show s smile with dissolve
        s "Yes, it sounds interesting."
        show jl smile with dissolve
        jl "Alright, I'm in."
        m flirt "I'll start."
        menu:
            "Do you believe in astrology?":
                show jl angry with dissolve
                jl "Seriously..? No, hell no."
                show su gasp with dissolve
                sue "Yes! What's your sign, [name]?"
                show su smile with dissolve
                m talk "Scorpio. You?"
                show su laugh with dissolve
                sue "Aries, and so is Julia ~"
                show su cute with dissolve
                "Huh."
                m flirt "Doctor?"
                show s calmsmile with dissolve
                s "I think... if people are willing to believe in it, then I am willing to give some credence to it."
                show s neutral with dissolve
                s "But I never became invested in it, if that's what you're asking."
            "Have you ever collected anything?":
                show su sadsmile with dissolve
                sue "Books on dogs. When I was little"
                m gasp "Wait, really?"
                show su sadtalk with dissolve
                sue "I really wanted a dog as a child, but my mom was allergic."
                show su neu with dissolve
                show s calmsmile with dissolve
                s "I have a sizable collection of teapots, if that counts."
                show s neu with dissolve
                m conf "I'd say it does."
                show jl calmtalk with dissolve
                jl "Uhh... so... That's kind of personal, but I've been collecting pictures I took with friends."
                show jl calmsmile with dissolve
                sue "Oh, yeah. I saw those."
                show jl smile with dissolve
                jl "I started in high school, I think. It's nice to look at."
        show jl neu with dissolve
        show su laugh with dissolve
        sue "Okay, my turn!"
        show su smile with dissolve
        sue "Do you like children?"
        show jl angry with dissolve
        jl "Gee, Sue. I know you do."
        menu:
            "I do":
                show su happy with dissolve
                sue "Yeah, [name] would make a great mom!"
                m shock "Huh?"
                show su smile with dissolve
                sue "Or big sister, if you prefer."
            "I don't":
                show jl talk with dissolve
                jl "Can't blame you..."
        show jl calmtalk with dissolve
        jl "The little buggers drive me insane... Every time I have to take care of my nephew, it's hell."
        show jl neu with dissolve
        show s talk with dissolve
        s "Oh, how unfortunate. I don't think I mind children, though I never had to raise any."
        show s smirk with dissolve
        show jl smile with dissolve
        jl "Alright, prepare for my question: what's your favorite movie genre?"
        sue "Oooh, interesting ~"
        menu:
            "Action":
                show s calm with dissolve
                s "...an interesting pick."
            "Comedy":
                m cute "Everyone needs a good laugh sometimes."
            "Romance":
                show su smile with dissolve
                sue "Aww, [name], I didn't know you were sentimental ~"
            "Horror":
                show jl gasp with dissolve
                jl "Really? I wouldn't have thought of that."
                show jl smile with dissolve
        show s smile with dissolve
        s "I mostly prefer books, but a thriller on a long, winter night tends to make for a good time."
        show su cute with dissolve
        sue "You're going to laugh at me, but I like a good romcom. Nothing more wholesome than seeing two people be happy ~"
        show jl calmsmile with dissolve
        jl "Ha, I've seen your taste in films before, Sue."
        show s neu with dissolve
        s "It looks like it's my turn."
        show s angry with dissolve
        show su neu with dissolve
        s "[name], am I allowed to ask about something a bit more... complex?"
        show jl neu with dissolve
        m confusion "Sure?"
        show s paintalk with dissolve
        s "Would you rather betray your friends or your values?"
        show s neutral with dissolve
        show jl gasp with dissolve
        jl "Oh shit, you weren't kidding."
        show jl smile with dissolve
        show su angry with dissolve
        sue "...."
        "I'm gonna have to think about this one."
        show jl talk with dissolve
        jl "So... I don't think I care about principles as much as I care about people."
        show jl neu with dissolve
        show su sadtalk with dissolve
        sue "But if your friends betray what you believe in, then... were they really good friends in the first place?"
        show su sad with dissolve
        show jl calm with dissolve
        jl "Not everyone believes in the same things you do."
        sue "True, but... if someone I care about does a bad thing... can I really call them a friend?"
        menu:
            "Friends are more important":
                $side-=3
                m conf "I stick by my friends no matter what."
            "Values are more important":
                $side+=3
                m angry "You need principles to tell who you can trust."
        show jl talk with dissolve
        jl "What do you think, Young?"
        show jl neu with dissolve
        show s calmtalk with dissolve
        s "That's something that I am personally conflicted about, so I wanted to hear other opinions."
        show s neu with dissolve
        "I'm not entirely sure of my answer."
        show su neu with dissolve
        m talk "Okay, it's my turn again."
        menu:
            "What kind of kid were you in school?":
                show jl smile with dissolve
                jl "Goth."
                show su gasp with dissolve
                sue "Wait, {i}REALLY?"
                show jl calm with dissolve
                jl "Yeah. My parents didn't like it, though."
                show jl neu with dissolve
                jl "I also got older, had to keep a job."
                show s calm with dissolve
                s "I think I was pretty quiet back then... I didn't have many friends."
                "I can relate to that."
                show su laugh with dissolve
                sue "...Aaand I was the class president. A lot of the time."
            "Do you ever have prophetic dreams?":
                show su angrytalk with dissolve
                sue "Pro... {i}phetic{/i}? You mean like, about the future?"
                show su neu with dissolve
                m smile "Yeah."
                show jl angry with dissolve
                jl "You ask weird questions, Hart. No, I don't."
                show s neutalk with dissolve
                s "I think I may have, at some points? But the phenomenon has not been confirmed to actually exist."
                show s smirk with dissolve
                show su sadtalk with dissolve
                sue "Hmm... I get feelings about people sometimes. Strong feelings."
                show su angry with dissolve
                "Julia chuckles."
                show jl smile with dissolve
                jl "Isn't that normal for you?"
                show su gasp with dissolve
                sue "No, I mean... feeling like someone is trustworthy. Or if they have bad intentions."
                show su smile with dissolve
                m flirt "You must have a really good intuition, then."
                show su cute with dissolve
                sue "Yeah. That's what it's called."
    stop music fadeout 5
    scene black with dissolve
    "We talk for a while, until the sky goes pitch black outside."
    show bg mclivingnight with Dissolve(1.0)
    m cute "Thanks for coming today, it means a lot ~"
    play sound "doorclose.ogg" fadein 1
    "...."
    play music "ost/tran.ogg" fadein 5
    "And with that, they're gone and I'm left alone once more."
    "I... think I'm gonna clean up tomorrow."
    "For some reason, this has drained me quite a bit. Maybe I really did need those days of rest."
    "Either way, it was definitely worth it. I'm glad I have friends at the hospital who care about me and want to help."
    if route=="silver":
        jump mysterycall
    else:
        jump nextday

label breakevent3:
    scene black with dissolve
    "...."
    "Another dream..?"
    scene bg mcbed with Dissolve(1.0)
    play music "ost/jane.ogg" fadein 6
    if route=="green":
        "I just had one yesterday... could it be because Dr. Sharpe told me about his past relationship to Jane?"
    "I remember this one as well... it was just after what I saw in my last dream about Jane."
    "Why am I suddenly remembering it all..?{w} I don't want to...{w} I don't want to see any of that again..."
    "Especially since... I know exactly what's going to happen..."
    stop music fadeout 5
    "...and how helpless I was to stop it."
    "I don't want to be helpless ever again. I don't want to fail anyone else."
    if route=="golden" or route == "red":
        jump nextday
    elif route=="silver" and SunLink>0 and social>0:
        pause 1
        "I remember Sue wanted to meet me today."
        "But... after what happened... can I really talk to her?"
        "I... feel like I can barely stand since that nightmare."
        "It's not that I'm exhausted, I'm... hopeless."
        "Should I cancel our meeting?{w} She'll understand, right?"
        menu:
            "I won't let that thing beat me":
                if sanity<45:
                    $sanity+=5
                else:
                    $sanity=50
                "No. I just won't."
                "I am going to meet my friend and I am going to enjoy it."
                "I'm so glad I have Sue. She has no idea how helpful she is right now."
            "I'm tired...":
                $sanity-=5
                $StrengthCard=False
                "I... can't."
                scene black with dissolve
                "I call Sue to cancel our meeting, explaining to her that I need to rest."
                "Even if I told her the truth, she wouldn't believe me... she'd think I'm crazy."
                "Ugh... there's no right option, is there?"
                jump mysterycall
        if social>1:
            if social>2:
                if social>3:
                    "Dr. Young and Julia apparently wanted to come with her as well."
                else:
                    "Dr. Young planned to come as well."
            else:
                "Julia is going to tag along as well."
        jump visitbreak
    elif route=="blue":
        jump nextday
    jump mysterycall
label mysterycall:
    scene black with dissolve
    play music "rain.mp3" fadein 5
    pause 1
    scene bg mclivingnight with Dissolve(1.0)
    "It's late, but I don't feel like sleeping yet."
    "I'm sitting in the living room alone, sipping tea."
    "A lot's happened recently... I find myself rethinking everything to do with my job at the hospital."
    if route == "green" or route == "golden":
        pass
    else:
        "And to think I'd be excused from work for so long... right when my patients need me the most."
        "I sigh. I guess there's nothing to be done about it until I'm back."
    play music "ost/ring.ogg"
    $renpy.pause(2,hard=True)
    "What..?"
    "Who's calling me at this hour...?"
    "Could it be from the hospital?"
    "Maybe something urgent happened there..."
    scene black with Dissolve(1.0)
    nt "I get up to answer."
    nt "My parents never call me at this time, so it has to be from work."
    scene bg mcphone with dissolve
    nt "I make my way to the phone."
    nt "It's still ringing... it's an unknown number - didn't I save the one from the reception..?"
    nt "Maybe I shouldn't pick up... I don't know who it is."
    menu:
        "Pick it up":
            pass
        "Ignore it":
            nt "I decide to ignore it. It's probably a mistake, anyway."
            play music "rain.mp3" fadein 3
            scene black with dissolve
            nt "The phone goes silent. I sit back down."
            nt "Who knows who could be calling me at this hour? It's surely not from the hospital."
            play music "ost/ring.ogg"
            $renpy.pause(2,hard=True)
            nt "...."
            nt "I guess they're not giving up."
            nt "I should see what it's about. It's not like I have much of a choice."
    stop music 
    play music "rain.mp3"
    show bg mcphone2 with dissolve
    nt "I answer the phone."
    nm "Hello?"
    nn "{i}Y o u \ \ w o r k \ \ a t \ \ S t . A u g u s t i n e ' s ?\nY o u ' r e \ \ H a r t , \ \ t h e \ \ p s y c h o l o g i s t ?"
    nm "That's right."
    nt "I don't recognize the voice at all... How does he know who I am?"
    nn "{i}L i s t e n \ \ c l o s e l y ."
    nn "{i}I \ \ h a v e \ \ s o m e t h i n g \ \ i m p o r t a n t \ \ t o\nt e l l \ \ y o u \ \ a b o u t \ \ t h a t \ \ h o s p i t a l ."
    nn "{i}Y o u \ \ w e r e \ \ a t t a c k e d \ \ l a s t \ \ w e e k."
    nn "{i}I \ \ k n o w \ \ w h y \ \ i t \ \ h a p p e n e d \ \ a n d \ \ w h o \ \ i s \ \ r e s p o n s i b l e ."
    nt "What..?"
    nt "But it was an accident, I was attacked by aggressive patients... What is he talking about?"
    nn "{i}Y o u \ \ a r e \ \ i n \ \ d a n g e r ."
    nm "Who are you?"
    nn "{i}M e e t \ \ m e \ \ t o m o r r o w \ \ a t \ \ 3 P M \ \ b y \ \ t h e \ \ f o r e s t . \ \ A l o n e ."
    stop music fadeout 4
    nn "{i}I ' l l \ \ e x p l a i n \ \ e v e r y t h i n g \ \ t h e n ."
    play music "ost/tension.ogg" fadein 6
    menu:
        "I don't want to":
            pass
        "Why would you tell me that?":
            pass
        "I'll be there":
            pass
    nt "...He already hung up."
    nt "He said I'm in danger... But they wouldn't let patients attack me again, not after what happened..."
    scene black with dissolve
    show bg mclivingnight with Dissolve(1.0)
    nt "How can I be in danger? Everyone's trying their best, they'll make sure no harm is done to me."
    if route=="green":
        nt "I trust Dr. Sharpe. He promised to help me, he wouldn't let anything happen to me."
    nt "Who could this be..? Whoever it was, they seem to have some knowledge of the hospital and its happenings."
    nt "But I don't recall their voice... and besides, if we were coworkers he could approach me anytime these past three weeks."
    nt "He sounded serious about it... I doubt it's just a prank."
    nt "I should listen to his request... I know I'll regret it if I don't."
    nt "He told me to come alone... Should I be worried?"
    nt "He wouldn't... hurt me, right?"
    jump nextday
label gmeeting:
    play sound "doorclose.ogg" fadein 1
    scene black with dissolve
    "I leave my house a while before I was told to meet the mysterious caller from yesterday."
    "On my way to the edge of the forest, I try to remain calm."
    play music "ost/tension.ogg" fadein 8
    "I'm safe... I hope."
    "The man who called me yesterday seemed very shady, but if my life may be in danger and he claims to know why, then the risk is worth it."
    "He already knows enough about me to find my phone number and know I was attacked, so if he wanted to hurt me, he could've already, right?"
    scene bg darkforest with Dissolve(1.0)
    "I reach the edge of a forest. It's huge... and dark."
    "There are no people as far as I can see. The perfect place for something you wouldn't want others to know about."
    "I remember seeing this forest from my house when I was little... We used to live a lot closer to it than I do now, on the other side of it."
    stop music fadeout 5
    "The neverending trees and the dark bring back memories... not necessarily good ones."
    "Wait... I think I can see someone emerging from the forest..."
    show g frust:
        ypos 15
    with Dissolve(2.0)
    m uncom "Are you the one who called me yesterday?"
    show g neutral with dissolve
    "He nods."
    show g calmtalk with dissolve
    mn "I don't trust phone calls - I had to meet you in person."
    show g neu with dissolve
    m angrytalk "What's your name? Who are you?"
    play music "ost/tension.ogg" fadein 6
    show g frusttalk with dissolve
    mn "That's none of your concern. I have more important\nmatters to discuss with you."
    show g neutral with dissolve
    m frust "...."
    show g neutalk with dissolve
    mn "Just call me \"G\" from now on. It'll be a lot smarter."
    show g neu with dissolve
    m angrytalk "And you expect me to trust you?"
    show g frusttalk with dissolve
    g "I don't care about your trust. If you don't believe me and get yourself killed, I won't be responsible."
    show g neutral with dissolve
    "...he's right."
    m fabtalk "So what do you want from me?"
    show g talk with dissolve
    g "I will tell you the truth about the hospital you work in. We don't have much time."
    show g neutral with dissolve
    "He's still being cryptic..."
    show g frusttalk with dissolve
    g "It's about your boss, Dr. Sharpe."
    show g neu with dissolve
    if route == "green":
        "About... him? What does he mean..?"
    else:
        "This is getting interesting..."
    m talk "What about him?"
    show g talk with dissolve
    g "He's been lying to you the whole time. To everyone."
    show g frust with dissolve
    m angrytalk "How so?"
    show g neutalk with dissolve
    g "He's not trying to help the patients. He's hurting them."
    show g neutral with dissolve
    if route == "green":
        "{i}Him?{/i} Hurting the patients?"
        "I've seen how much he cares about them - and about the staff."
        "No, that's impossible. Nonsense!"
        m angry "When are you going to start making any sense? What proof do you have?"
    else:
        "Sharpe? Hurting the patients?"
        "No, that doesn't sound right... he wouldn't do that."
        "Then again, I barely know him..."
        m talk "Go on, convince me."
    show g calm with dissolve
    m angrytalk "Why should I believe you, and not him?"
    show g talk with dissolve
    g "I'll tell you what I've seen, and what I know. Nothing else."
    show g frust with dissolve
    g "...."
    show g neutalk with dissolve
    stop music fadeout 5
    g "I worked there two years ago."
    scene black with Dissolve(1.0)
    pause 1
    g "I was hired as the night guard."
    g "Everything seemed normal until one night..."
    scene goff with Dissolve(1.0)
    g "I sat down in my office as usual. First, I turned the monitor on."
    play music "light.ogg" fadein 2
    scene bg grec with dissolve
    show monitor with dissolve
    g "Then I would always check the drawers, for good measure."
    show gdrawer with dissolve
    $renpy.pause()
    nt "Nothin' but a bunch of trash and an old flashlight. The usual stuff."
    hide gdrawer with dissolve
    nt "Okay, let's see..."
    show click with dissolve
    $renpy.pause()
    hide click with dissolve
    show bg gcaf
    $renpy.pause()
    show bg ghall 
    $renpy.pause()
    show bg gout
    $renpy.pause()
    show bg gpat
    nt "Man, I'm tired..."
    nt "I lean back in my chair."
    nt "The job is boring as hell, but I wouldn't complain."
    nt "Every night, it all looks the same."
    $renpy.pause()
    show bg gpsych 
    $renpy.pause()
    show drk 2 with Dissolve(1.0)
    hide drk with dissolve
    nt "I feel my eyes closing slowly, but struggle to stay awake."
    nt "...."
    stop music
    scene goff ##noise
    $renpy.pause()
    nt "{i}What the hell?"
    $renpy.pause()
    play music "light.ogg" fadein 2
    show bg gpsych
    show monitor with dissolve
    $renpy.pause()
    show bg gthird
    $renpy.pause()
    nt "Seriously? Was that a power outage or what..?"
    nt "Forget it, gotta check the others."
    $renpy.pause()
    show bg gcentr 
    $renpy.pause()
    show bg gpat
    $renpy.pause()
    show bg gpat
    $renpy.pause()
    show bg gcafp
    $renpy.pause(0.4, hard=True)
    show bg gout
    pause 0.5
    show bg gcaf
    $renpy.pause()
    nt "The hell is going on in there..?"
    nt "Were those patients?"
    nt "How could they disappear like that?"
    nt "No, I must be seeing things..."
    $renpy.pause()
    show bg grec
    $renpy.pause()
    show bg gout
    $renpy.pause(1, hard=True)
    show verror
    show bg gbl
    $renpy.pause()
    nt "God dammit, what is going on with this place?!"
    $renpy.pause()
    hide verror
    show bg ghall
    $renpy.pause(2, hard=True)
    show verror
    show bg gbl
    nt "Does {i}anything{/i} work here?"
    $renpy.pause()
    hide verror with Dissolve(0.1)
    show verror with Dissolve(0.1)
    $renpy.pause()
    nt "It won't switch."
    $renpy.pause()
    hide verror with Dissolve(0.1)
    show verror with Dissolve(0.1)
    $renpy.pause()
    hide verror with Dissolve(0.1)
    show verror with Dissolve(0.1)
    $renpy.pause()
    hide verror with Dissolve(0.1)
    show verror with Dissolve(0.1)
    $renpy.pause()
    hide verror with Dissolve(0.1)
    show verror with Dissolve(0.1)
    $renpy.pause()
    hide verror 
    stop music
    show goff 
    pause 0.5
    show bg gface
    hide goff 
    $renpy.pause()
    nt "What the FUCK?!"
    stop music
    scene goff 
    $renpy.pause()
    nt "Get a grip. Come on, focus."
    $renpy.pause()
    play music "light.ogg" fadein 2
    show bg gcaf with Dissolve(0.1)
    show monitor with Dissolve(0.1)
    $renpy.pause()
    show bg gbl
    pause 0.3
    show bg gcafp
    pause 0.2
    show bg gbl
    pause 0.1
    show bg gcafc
    $renpy.pause(4,hard=True)
    nt "...."
    $renpy.pause()
    nt "...."
    $renpy.pause()
    stop music fadeout 1
    scene goff with dissolve
    nt "Did I... {i}really see that..?"
    nt "Alright, let's go and check what happened there."
    $renpy.pause()
    show gdrawer with dissolve
    "I grab a flashlight from the drawer."
    hide gdrawer with dissolve
    nt "If anyone is hiding out there, messing with me, they better come out."
    play sound "doorclose.ogg" fadein 1
    scene black with dissolve
    "I leave my office. I don't think I should be doing this, but if something really is going on, it's my duty to stop it."
    play music "ost/dream.ogg" fadein 5
    $renpy.music.set_volume(0.3, channel = 'music')
    show bg greetnight 
    show flashlight:
        truecenter
    $renpy.pause()
    show flashlight:
        ease 1.0 xalign 1.0
    pause 2
    show flashlight:
        ease 2.0 xalign 0.0
    nt "\"Hello..? Anyone there?\""
    show flashlight:
        ease 2.0 truecenter
    nt "...."
    play sound "doorclose.ogg" fadein 1
    show bg hallwaynight
    nt "Nothing. This place may as well be dead."
    show flashlight:
        ease 2.0 xalign 1.0
    $renpy.pause(2, hard=True)
    show flashlight:
        ease 3.0 truecenter
    nt "Maybe I'm the crazy one."
    ##giggle
    $renpy.pause() 
    nt "Was that... a voice?"
    show flashlight:
        ease 1.0 xalign 1.0
    $renpy.pause(1, hard=True)
    show flashlight:
        ease 0.5 xalign 0.0
    $renpy.pause(1, hard=True)
    show flashlight:
        ease 1.0 xalign 0.8
    nt "\"Where are you?\""
    ##giggle
    $renpy.pause(2, hard=True)
    show drk 2 with dissolve
    hide drk 2 with dissolve
    $renpy.pause(1, hard=True)
    show drk 2 with Dissolve(1.0)
    $renpy.pause(1, hard=True)
    hide drk 2 with dissolve
    nt "What the hell is happening?!"
    play sound "ost/dscare.ogg" fadein 1
    show alicerun:
        xpos 0
        linear 0.3 xpos 800
    show flashlight:
        ease 0.3 xalign 0.0
    pause 0.3
    stop music fadeout 3
    scene black
    $renpy.pause(6, hard=True)
    $renpy.music.set_volume(1.0, channel = 'music')
    g "The next thing I remember is waking up in my chair in the security office."
    g "I was getting ready to head out, it was almost morning, but then I noticed..."
    play music "ost/tension.ogg" fadein 8
    g "The flashlight was gone. So I wanted to check the drawer for it."
    g "But it was locked. That thing was never locked."
    g "But the stuff I saw... there's no way nothing happened back there, that was real."
    g "And I was attacked by someone."
    g "Someone who really didn't want me seeing the truth."
    nt "...."
    nt "I can't wrap my head around what he just told me. It sounded..."
    nt "...insane."
    stop music fadeout 6
    m talk "So what makes you say Sharpe is behind whatever happened?"
    if route=="green":
        $side+=10
        nt "These are the ramblings of a vengeful lunatic, there's no way Dr. Sharpe is involved in any of this."
        nt "He even admitted to being unconscious. It must've been just a weird dream."
    else:
        nt "His evidence seems shaky at best."
    play music "ost/rev.ogg" fadein 10
    g "I knew something was wrong."
    scene gback 1 with dissolve
    g "The next day I came to work early and went straight to Sharpe's office to confront him about what I saw."
    g "He didn't seem concerned when I told him I saw patients running around the hospital, power outages, insane security breaches..."
    g "And the stuff of nightmares. I have no idea what happened there, but he looked at me like it was nothing."
    g "Like it was normal."
    "It's not unreasonable to think he made it all up."
    g "When I brought up my suspicions regarding someone breaking in and hiding something in the security room, he even suggested I must had fallen asleep and dreamt about it, since there were no signs of breaking in."
    g "I asked him about the patients again - he denied everything."
    g "I couldn't get him to tell me the truth, so I decided to seek help from someone else."
    g "There was one psychologist who was willing to talk to me. He promised me he'd ask around and let me know if any of his patients'd heard or seen anything suspicious that night."
    g "According to him, a couple of his patients confirmed my version of events."
    show gback 2 with dissolve
    g "The next day, one of his patients... disappeared. apparently they isolated her in room XXI because she became aggressive."
    g "He couldn't contact her."
    g "A few days later, she came back."
    g "But... she didn't remember anything about that one night. He told me she was acting strange."
    g "The next day... that psychologist called me around 10 AM."
    show gback 3 with dissolve
    g "He said his patient killed herself. He was devastated, but he blamed me for making him ask her about that night."
    g "Then it all got messed up."
    g "Once I got to work that evening, the police were already there."
    g "They questioned me about that night, why I talked to Sharpe afterwards, and if I knew that one patient..."
    g "I didn't know what they were accusing me of, or where they got all these ideas, but they seemed to suggest I was responsible for the suicide and that I was threatening Sharpe before."
    g "Now I know - the bastard framed me so nobody would believe what I saw."
    g "I knew that I would keep investigating the hospital if he hadn't stopped me. I would learn the truth eventually."
    show gback 4 with dissolve
    g "What I saw that night was just the start."
    g "The police investigation ended in a matter of days. I was arrested and charged with causing a suicide and blackmailing the staff."
    g "I didn't get another chance to confront Sharpe about it, since he stayed out of the whole thing - he probably didn't want to draw any attention."
    g "In the end, there wasn't enough evidence against me, so I was released after a week."
    g "It's a small town, though... So everyone knew what happened."
    g "I couldn't stay here. Even if I wasn't proven guilty, nobody trusted me after that."
    stop music fadeout 6
    g "So I moved out of here once it was over."
    scene bg darkforest with dissolve
    m angry "What made you come back now?"
    show g frusttalk:
        ypos 15
    with dissolve
    g "I heard about the patients attacking you. I wanted to confirm it."
    show g neutral with dissolve
    g "Turns out Sharpe's still in charge and things only changed for the worst while I was gone."
    show g talk with dissolve
    play music "ost/hospital.ogg" fadein 8
    g "I don't care what the people here think about me. It's my duty to expose his crimes and save these patients."
    show g calmsmile with dissolve
    m fabtalk "Why should I trust you? As far as I'm conerned, you could be making all this up to trick me."
    show g neu with dissolve
    g "I don't care about your trust, or about you, for that matter."
    show g talk with dissolve
    g "All I'm saying is - listen to what I'm telling you here, and then make your choice."
    show g frusttalk with dissolve
    g "I can accomplish my goals without your help. But you could spare the patients a lot of pain if you agreed now."
    show g calm with dissolve
    "I still don't know what exactly he wants from me... And I'm not sure if I even believe him..."
    "I don't want to believe him... all these things he said - they're horrible, and they should never happen in a hospital."
    "...But I'll hear him out."
    stop music fadeout 5
    show g neu with dissolve
    m talk "So what do you need me for?"
    show g talk with dissolve
    g "I can't get inside the hospital. They'd never let me in, after what happened."
    show g neutral with dissolve
    play music "ost/tension.ogg" fadein 8
    m neu "So you need a spy."
    show g calmtalk with dissolve
    g "I need you to gather the evidence that I couldn't. Find proof against Sharpe and bring it to me. I'll handle it from there."
    show g neu with dissolve
    "This sounds suspicious..."
    show g neutral with dissolve
    m angry "You still haven't told me exactly what you suspect him of. And what should I look for? Where should I start?"
    show g frusttalk with dissolve
    g "I've told you what happened. It's all I can know for sure."
    show g talk with dissolve
    g "But you were attacked by aggressive patients. Didn't they seem a little... out of place?"
    show g neu with dissolve
    m neu "It's a mental hospital we're talking about, it happens sometimes."
    show g calmtalk with dissolve
    g "Before that patient commited suicide, she began exhibiting very unusual behavior."
    show g talk with dissolve
    g "And it was after she was released from XXI."
    stop music fadeout 6
    show g neutalk with dissolve
    g "Where were these patients who attacked you before? Weren't they isolated for a while as well?"
    show g neutral with dissolve
    m serious "I don't know what you're trying to say..."
    play music "ost/fight.ogg"
    show g talk with dissolve
    g "They were drugged, Hart. And so was that girl."
    show g frust with dissolve
    m shock "What? How could anyone -"
    show g talk with dissolve
    g "What do you think was smuggled into the hospital that night?"
    show g calmtalk with dissolve
    g "They didn't have to break in - because they already had the keys."
    show g frust with dissolve
    g "It was Sharpe's doing that night. I'm sure of it."
    show g frusttalk with dissolve
    g "I don't know how he managed to pull something like that off, but I'm sure he's behind whatever happened."
    show g sadtalk with dissolve
    g "And if this is still going on, there's a high chance that something is being smuggled into the hospital and used on the patients."
    show g talk with dissolve
    g "Finding it should be your first lead. We can meet again once you've confirmed anything."
    show g neutral with dissolve
    "That sounds difficult... Snooping around the hospital for something that may not be there, based on an extremely suspicious man's word..."
    "Is that really smart?"
    stop music fadeout 6
    if le:
        $side+=5
        "It's not. I'd be risking my career for this stranger."
        "I'd much rather let him deal with this."
    else:
        if he:
            "I'd be risking my career, but if he's telling the truth and the patients are being hurt... It needs to be stopped."
        else:
            "I'd be riking my career, but if he's telling the truth, patients are being hurt..."
        "But if he's not telling the truth... then {i}he{/i} needs to be stopped before he actually hurts someone over this."
        m frusttalk "\"G\"?"
        show g frusttalk with dissolve
        play music "ost/tension.ogg" fadein 8
        g "What is it now?"
        show g calm with dissolve
        m serious "If I get caught, will you help me?"
        show g talk with dissolve
        g "If you get caught, I can only beat the shit out of you afterwards if you tell them I asked you to do it."
        show g frust with dissolve
        menu:
            "And you want to protect the patients?":
                $empathy+=2
                $side+=5
                show g neutalk with dissolve
                g "What's your problem?"
                show g neu with dissolve
                menu:
                    "You threatened me just now":
                        show g calmtalk with dissolve
                        g "And I can do it again, so you better cooperate."
                        menu:
                            "I don't think you want to help anyone":
                                show g talk with dissolve
                                g "What? Then why would I be doing all of that?"
                                show g frust with dissolve
                                menu:
                                    "For revenge" if he:
                                        $side+=2
                                        $empathy+=1
                                        show g neutalk with dissolve
                                        g "That's none of your business."
                                        show g neu with dissolve
                                        menu:
                                            "It is":
                                                show g neutalk with dissolve
                                                g "Yeah? How?"
                                                show g neutral with dissolve
                                                menu:
                                                    "You asked me for help":
                                                        show g frusttalk with dissolve
                                                        g "I didn't ask for a therapy session, Hart. Don't stick your nose where it doesn't belong."
                                                        show g calm with dissolve
                                                        "Isn't that exactly what he asked me to do for him, though..?"
                                                    "I won't work with someone I know nothing about":
                                                        $side+=2
                                                        show g talk with dissolve
                                                        g "Fine... If you really want to know..."
                                                        show g regrettalk with dissolve
                                                        g "It's just a bonus, but I want to get back at Sharpe for what he did to me two years ago."
                                                        show g frustsmile with dissolve
                                                        g "He'll get what he deserves."
                                                        "I'm still hesitant to believe him, but his motivation seems genuine."
                                            "That doesn't matter":
                                                show g frusttalk with dissolve
                                                g "Well, if it's not your business, then don't stick your nose where it doesn't belong, Hart. I'm warning you."
                                                show g neutral with dissolve
                                                "Isn't that exactly what he asked me to do for him, though..?"
                                    "For justice":
                                        show g calmtalk with dissolve
                                        g "If by justice you mean punishing him for what he's done, then yes, it's for justice."
                                        show g neu with dissolve
                                        "Justice shouldn't be about hurting others, no matter what they did... Everyone deserves to be understood and helped."
                                        "...And I don't like the sound of \"punishing people\" for something..."
                                    "For glory":
                                        show g regrettalk with dissolve
                                        g "\"Glory\" may not be the right word... I won't be loved here either way, because of what happened two years ago."
                                        show g frustsmile with dissolve
                                        g "But it's the right thing to do. And I'm fighting to prove him wrong."
                                        show g neutral with dissolve
                                        "I suppose it makes sense for him to want to uncover the truth for his own sake..."
            "{color=#cc982f}Stay silent":
                "I bite my tongue before I can say something irrational."
                show g neutral with dissolve
                "There's no reason to pick a fight."
                "...Especially with someone like him. I'm pretty sure he's even taller than Sharpe."
    "\"G\" turns to leave."
    show g calmtalk with dissolve
    g "Think about that, Hart. You'll see that siding with me is your only choice."
    show g neutalk with dissolve
    g "If you learn anything by next Tuesday, I'll be waiting for you right here in the evening. Try not to call me again."
    show g neutral with dissolve
    g "Until then, Hart..."
    hide g with Dissolve(2.0)
    stop music fadeout 6
    $persistent.G=True
    play sound "chars.ogg" 
    show screen notify("{size=24} Your Characters Info screen has been updated!")
    "He leaves."
    scene black with Dissolve(1.0)
    "I'm puzzled on my way home."
    "Should I really do as he says..?"
    "The choice is mine alone."
    $side+=GreenHeart*2
    $side+=submissive-dominant
    $side+=professional-personal
    if route=="silver" or route=="green" or route=="purple":
        $side+=3
    elif route=="red":
        $side-=3
    $gameon=True
    if tutorials:
        call screen tuto8
    if route=="green" or route=="red":
        jump janesuicide
    else:
        jump nextday
label callhospital: ##calling the hospital to make your break shorter
    scene bg mcliving with Dissolve(1.0)
    "I've made up my mind. I'm not sitting here idly a single day longer."
    play music "ost/mc.ogg" fadein 6
    "Picking up my phone, I call the hospital."
    gu "{i}St. Augustine's hospital, how may I-{w} Oh."
    gu "{i}Dr. Hart, right?"
    m fabtalk "That's me. I wanted to ask when it would be possible for me to return to work."
    "No point dancing around the subject."
    gu "{i}...oh."
    gu "{i}You were scheduled to return to work on... Monday?"
    m talk "I'm alright now, so there's no point waiting."
    gu "{i}So you want to shorten your break?"
    "I can see how that could be confusing."
    m neu "Yes. Is that possible?"
    gu "{i}Umm... I will call you back as soon as I learn that."
    m cute "Thank you."
    "...."
    "I wonder how long it'll take for her to call back."
    scene black with dissolve
    scene bg mcliving with Dissolve(1.0)
    play music "ost/ring.ogg"
    "There it is. Sooner than I expected."
    "I pick up the phone."
    play music "ost/hospital.ogg" fadein 5
    gu "{i}Hello? Dr. Hart?"
    m conf "Hello."
    gu "{i}I managed to reschedule your return to work."
    "Yes! Finally some good news."
    gu "{i}You are to come to work the day after tomorrow. I hope that's not too soon."
    m flirt "That's perfect, actually. Thank you very much ~"
    stop music fadeout 4
    gu "{i}Alright, that would be all."
    "She hangs up."
    show bg mclivingnight with Dissolve(1.0)
    "Ah... I'm excited to get back to work, but scared at the same time..."
    jump janesuicide
label breakend:
    if route=="golden":
        scene black with dissolve
        "It's the last day of my break."
        "Even though it's only been a few days, I'm anxious to get back to work."
        return
    scene bg mcbed with Dissolve(1.0)
    "I wake up later than usual."
    play music "ost/memory.ogg" fadein 8
    "Memories of Jane are flooding back to me..."
    "I just relived my most horrifying memory..."
    "Jane's death."
    "I had no idea I remembered it in so much detail until now..."
    show drk 2 with dissolve
    "Hiding my face in my shaking hands, I try to keep myself from crying."
    "{i}She killed herself."
    "Right in front of me."
    "I was just a child back then, I didn't understand... I couldn't understand..."
    "...or maybe I just didn't want to understand."
    "I could've stopped her, I was the only one who could've done anything..."
    "And I just stood there and watched it happen."
    "When my parents found me on the floor later, my mom nearly fainted."
    "Not only did she just witness the death of her own daughter, her second child was forced to watch it... While they left both of us."
    show drk with dissolve
    "When I speak to her nowadays, we never mention Jane."
    "It's almost like... she never existed."
    "After her suicide, they thought it was for the best."
    "They tried to wipe her from my memory..."
    "And yet... now it all came back to me."
    hide drk with Dissolve(1.0)
    if route == "green":
        "When Dr. Sharpe told me he knew her, I was... desperate to hear about her."
        "Everything my parents have tried to shield me from came back to me suddenly."
    "I recall the first time I had one of these strange dreams... It was after my first day at work."
    stop music fadeout 6
    "This hospital... it seems to have triggered all my memories of her."
    "I feel like... she's pushing me to make the right choice. So I never make the same mistakes I did again."
    play music "ost/jane.ogg" fadein 8
    "All those years I was scared of remembering her... of these memories."
    "But now I realised that... I needed to see it all again."
    "After Jane died, I blamed myself."
    "I couldn't help her. Thinking back to it now, I understand that there's nothing more I could've done."
    "Because of Jane, I started to think that my sole purpose in life was to help people, even if it cost me everything."
    "I should've died, I told myself - I {i}wanted{/i} to die instead of her."
    "And for a while, I thought that if I died for someone else, I would finally have a sense of closure."
    "Heh... to think that's what I wanted until now."
    "But now I know how wrong I was."
    if route == "red":
        "I would've given up my life if it meant at least a hope of helping Michael..."
        "I didn't have the heart to stop him when he could've killed me."
        "I can't be this reckless anymore... Helping him is my priority, but I can't risk my life for him anymore."
    elif route == "silver":
        "I was reckless with William... I didn't even hesitate before agreeing to meet his shadow."
        "I knew he could hurt me... and now I only made it worse..."
        "Once I'm back at the hospital, I'll be more careful."
        "My \"heroism\" can't put others at risk. It's pointless then."
    elif route == "purple":
        "I understand how Edward must've felt when his mother commited suicide."
        "I... didn't want to tell him about it, it was pointless then, but..."
        "Having someone who's like the whole world to you die right before your eyes is never easy. Even if they hurt you."
    elif route=="blue":
        "I think... hearing about Charlie's past made me think about my own. And about Jane."
        "They both got lost... so lost..."
        "I want to spare him her fate, but I'm not going to be naive anymore. I won't let him trick me."
    "Jane left me, but she never wanted me to die - to pay her back for staying alive instead of her somehow."
    "She always wanted me to be happy. She loved me."
    "I needed these dreams. I remembered her for how she really was."
    "Caring and gentle, but also deeply hurt and... wrong. About the world."
    "She thought there was nothing worth living for. I can't ever reach that point, for her sake."
    stop music fadeout 6
    "She wasn't flawless. But she was my sister, and I still love her."
    "I think I can finally say:"
    m sadsmile "Rest in peace, Jane."
    "We both deserved peace."
    scene black with Dissolve(1.0)
    $renpy.pause(2,hard=True)
    scene bg mcliving with Dissolve(1.0)
    play music "ost/hospital.ogg" fadein 8
    if route=="blue":
        "I think having this dream allowed me to finally calm down."
        "I've been so stressed this past week..."
        "That thing at the door... what the hell was that..?"
        "I was sure I saw something."
        "I've never hallucinated before. {w}But... I'm pretty sure it can happen."
        "As long as it's a one time thing, I shouldn't worry too much about it. Probably."
        scene black with dissolve
        scene bg mclivingnight with Dissolve(1.0)
        "I finished the book I started before."
        stop music fadeout 5
        "...."
        "I'm supposed to come back to work on Monday."
        "I feel fine. And after doing some soul searching, I feel like I'm ready to be back."
        "Yeah. I'm ready."
        "I call the hospital."
        play music "ost/mc.ogg" fadein 6
        "Picking up my phone, I call the hospital."
        gu "{i}St. Augustine's hospital, how may I-{w} Oh."
        gu "{i}Dr. Hart, right?"
        m fabtalk "That's me. I wanted to ask when it would be possible for me to return to work."
        "No point dancing around the subject."
        gu "{i}...oh."
        gu "{i}You were scheduled to return to work on... Monday?"
        m talk "I'm alright now, so there's no point waiting."
        gu "{i}So you want to shorten your break?"
        "I can see how that could be confusing."
        m neu "Yes. Is that possible?"
        gu "{i}Umm... I will call you back as soon as I learn that."
        m cute "Thank you."
        "...."
        "I wonder how long it'll take for her to call back."
        scene black with dissolve
        scene bg mcliving with Dissolve(1.0)
        play music "ost/ring.ogg"
        "There it is. Sooner than I expected."
        "I pick up the phone."
        play music "ost/hospital.ogg" fadein 5
        gu "{i}Hello? Dr. Hart?"
        m conf "Hello."
        gu "{i}I managed to reschedule your return to work."
        "Yes! Finally some good news."
        gu "{i}You are to come to work tomorrow. I hope that's not too soon."
        m flirt "That's perfect, actually. Thank you very much ~"
        stop music fadeout 4
        gu "{i}Alright, that would be all."
        "She hangs up."
        "I can't wait to come back to work."
    else:
        "I wonder if this dream had something to do with yesterday's events..."
        "I'm still confused by that man's request, and everything he told me."
        "Can I really believe him..?"
        "...."
        if route=="green":
            "I don't want to believe him... He's probably spouting lies to manipulate me."
            "I know Dr. Sharpe - he would never hurt the patients."
            "I... can't help but be on his side. I don't trust that man, who didn't even give me his name."
            "He doesn't trust me... So why should I trust him?"
            "The thought of Sharpe hurting someone, much less the patients, terrifies me."
            "It can't be true..."
        else:
            "On a positive note, I finally get to be back at work as of tomorrow."
        if route=="red":
            "I'll see Michael again..."
            "I won't free him this time - I'll be careful around him from now on."
            "But I was told I could release him sometime... maybe once I'm sure it's safe."
        elif route=="silver":
            "The consequences of the recent nightmare I had are coming back to me..."
            "All I can do for now is hope it was just a dream and he isn't actually aware of what happened."
            "...I wouldn't have the heart to tell him if that was the case."
            "Though the chances are quite low. I have to prepare myself to deal with the consequences."
        elif route=="purple":
            "I'm sure I can keep making progress with Tom now."
            "I was told James was more frequent recently, so maybe I'll get to see more of him soon."
            "And Edward... I hope he'll keep trusting me."
    stop music fadeout 3
    scene bg mclivingnight with Dissolve(1.0)
    "I can't stop thinking about everything that's happened recently..."
    if route=="green":
        jump father
    jump janereal
    