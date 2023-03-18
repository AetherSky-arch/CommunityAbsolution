### DEVIL NAVIGATION ###########################
################################################

label redintro:
    "I'm not sure why, but his file disturbs me a bit."
    "I feel slightly anxious about meeting him in particular, so I'll have to do my best."
    scene bg mcdesk with dissolve
    $redintro = 1
    "A patient enters my office."
    pause 0.5
    "I freeze for a second."
    "They weren't kidding when they wrote about restraining him at all times."
    play sound "doorclose.ogg" fadein 1
    "I jump up from my seat and close the door behind him."
    "I notice he's barely taller than me."
    play music "ost/tension.ogg" fadein 7
    show dv noeyes with Dissolve(1)
    "Sitting down by my desk again, I finally have the chance to look at him more closely."
    "I can't see his eyes."
    "But I can tell he's staring at me the whole time."
    "I take a deep breath."
    "{color=#bc0b17}I'm safe{/color}. He can't hurt me."
    "Stay calm. Just start talking."
    m talk "I'm [name] Hart, your new psychologist."
    m neutral "I hope our sessions will be beneficial to you."
    "He's silent for a while and I have no idea what to expect."
    show dv notalk with dissolve
    dv "I hope you leave this place in one piece."
    show dv creepy with dissolve
    dv "It would be a shame for you to give up so quickly if I ended up scratching you a bit~"
    menu:
        "\"Scratching\" me?":
            $personal += 1
            show dv notalk with dissolve
            dv "You can ask the nurses - I'm sure some of them remember me."
            show dv creepy with dissolve
            "I shift in my seat, subconsciously attempting to put as much space between us as possible."
            "Who is he?"
            "...or what?"
        "I don't give up easily":
            $RedHeart += 1
            show drk with Dissolve(0.75)
            show r 1 with dissolve
            show r 3 with Dissolve(0.3)
            show r 2 with Dissolve(0.3)
            $renpy.pause(0.75, hard = True)
            hide r with Dissolve(0.5)
            hide drk with dissolve
            show dv talk with dissolve
            dv "I wonder how long you'll last with me..."
            show dv creepy with dissolve
            dv "Psychologists tend to run away from me quite a lot."
            "As unsettled as I am, I'm not planning to leave him that quickly."
        "You can't hurt me":
            $professional += 1
            "He leans in a bit, closer to me."
            show dv noeyes with dissolve
            "I still can't see his eyes, but he's glaring at me."
            show dv creepy with dissolve
            dv "Or can I..?"
            show dv talk with dissolve
            dv "You seem to be shivering already and I wasn't even trying..."
            show dv creepy with dissolve
            "I hold my breath. I'm not afraid of him..."
    "I need to ask him something."
    if easymeter: 
        show screen easymeter
        show screen redmeter
    "I should be the one in control here. I need to make him understand that..."
    "But how can I do that if I don't even believe it myself?"
    "I put my hands on the desk and look down at him. His smile widens a bit."
    m talk "So, Michael..."
    show dv cute with dissolve
    dv "Hm?"
    m talk "How long have you been here for?"
    stop music fadeout 5
    show dv neu with dissolve
    "I notice that his eyes are an unnaturally golden shade."
    "That's odd..."
    "Focus. I need to focus."
    play music "ost/neutral.wav" fadein 8
    show dv talk with dissolve
    dv "{color=#bc0b17}Three years{/color}... maybe more."
    show dv neu with dissolve
    "He sounds as if he genuinely doesn't care."
    "How can he be so indifferent to his time spent here?"
    "Is it possible that he really doesn't care about what happens to him? Or is he just pretending not to care?"
    "I honestly can't tell."
    menu:
        "You like being here?":
            show dv smirk with dissolve
            dv "Heh... No, I don't think I'm that sick."
            show dv sidesmile with dissolve
            "His low laugh sends shivers down my spine."
            show dv smirk with dissolve
            dv "Though with you here... I might have to reconsider."
        "Do you even want to be helped?":
            $personal += 1
            show dv smirk with dissolve
            dv "Who doesn't?"
            show dv devil with dissolve
            dv "The question is what kind of \"help\" we're talking..."
        "And you don't want to leave?":
            $RedHeart +=1
            show dv sidetalk with dissolve
            dv "It's not a question of what I want, really..."
            show dv talk with dissolve
            dv "I can't leave this place just like that."
            show dv devil with dissolve
            dv "If I could, though... I would probably want to."
            show drk with Dissolve(0.75)
            show r 1 with dissolve
            show r 3 with Dissolve(0.3)
            show r 2 with Dissolve(0.3)
            $renpy.pause(0.75, hard = True)
            hide r with Dissolve(0.5)
            hide drk with dissolve
            show dv neu with dissolve
            "So he does care."
            "He seems to have given up, though."
    show dv siden with dissolve
    "In a moment of silence, I finally get a good look at him."
    "I didn't actually think these were still in use..."
    "Well, in his case, is seems somewhat justified..."
    "I had to close the door behind him earlier."
    "It must be difficult to be restrained like this at all times."
    "I look at his face again."
    "He doesn't seem to be bothered by not having his hands free."
    show dv talk with dissolve
    dv "What are you thinking so hard about?"
    show dv smirk with dissolve
    "I collect myself quickly."
    m frust "Your file states that you've hurt staff members..."
    show dv shock with dissolve
    dv "Is that so?"
    show dv smirk with dissolve
    "His eyes light up."
    show dv talk with dissolve
    dv "My file?"
    show dv sidetalk with dissolve
    dv "I was always curious what they wrote about me..."
    show dv talk with dissolve
    dv "Could you {color=#bc0b17}pass me that file{/color}?"
    show dv neu with dissolve
label filepassdevil:
    menu:
        "{color=#bc0b17}Show him the file":
            $RedHeart += 1
            $personal += 1
            "I pass him the file without much hesitation."
            "Why wouldn't I?"
            show dv cute with dissolve
            "He looks at me in surprise."
            show drk with Dissolve(0.75)
            show r 1 with dissolve
            show r 3 with Dissolve(0.3)
            show r 2 with Dissolve(0.3)
            $renpy.pause(0.75, hard = True)
            hide r with Dissolve(0.5)
            hide drk with dissolve
            show dv sidetalk with dissolve
            dv "You know, I actually expected you to say no..."
            show dv frust with dissolve
            dv "I asked a couple of people already, but they either ignored me or said it's none of my business."
            show dv neutral with dissolve
            "I suppose it was a gesture of trust from me then. Or at least the most basic amount of respect for his wishes."
            show dv sidetalk with dissolve
            dv "Anyway, let's see..."
            show dv frust with dissolve
            "He reads through the file carefully."
            show dv sidesmile with dissolve
            dv "Heh... \"must be kept away from sharp objects\"."
            show dv smirk with dissolve
            dv "That's a whole other story, though..."
            "He finishes reading."
            show dv smile with dissolve
        "{color=#bc0b17}Keep it":
            $professional += 1
            m boretalk "You have no need to see this file."
            show dv neutral with dissolve
            m angrytalk "It's for staff members only."
            show dv frust with dissolve
            "And besides, he could be plotting something."
            "I'm keeping a safe distance between us, just in case."
            show dv neu with dissolve
            "He leans back in his chair."
            show dv sidetalk with dissolve
            dv "If that's how it is..."
            show dv talk with dissolve
            dv "Come on, you were going to ask me something."
            show dv neutral with dissolve
            m angry "The file says you've attacked staff members before. Is this true?"
            show dv smirk with dissolve
        "I'm not sure about this...":
            dv "Oh come on, I won't bite..."
            jump filepassdevil
    dv "Yeah, sounds about right."
    stop music fadeout 7
    show dv cute with dissolve
    dv "They didn't think to tie me up when I first got here."
    show dv smirk with dissolve
    "He laughs."
    "I'm... slightly disturbed."
    "It seems that he's restrained for a reason."
    play music "ost/tension.ogg" fadein 7
    show dv cute with dissolve
    dv "I think they thought that... I was in shock? Something like that."
    show dv neutral with dissolve
    menu:
        "You don't regret doing that?":
            $personal += 1
            show dv devil with dissolve
            dv "Why would I?"
            show dv smirk with dissolve
            "He grins."
            show dv talk with dissolve
            dv "They were the ones who allowed it to happen."
            show dv sidetalk with dissolve
            dv "If they were more responsible, they could have avoided it."
            show dv neu with dissolve
            "It seems that he's not accepting responsibility for his actions."
        "How can you blame the people who tried to help you?":
            $wrong += 1
            show dv neutalk with dissolve
            dv "If they'd wanted to help me, they wouldn't have let me hurt them."
            show dv frust with dissolve
            dv "Hey, it was their fault - for not thinking it through."
            "I can sense his irritation. I was right, but I shouldn't have said that."
        "Would you do it again?":
            $RedHeart += 1
            $professional += 1
            show drk with Dissolve(0.75)
            show r 1 with dissolve
            show r 3 with Dissolve(0.3)
            show r 2 with Dissolve(0.3)
            $renpy.pause(0.75, hard = True)
            hide r with Dissolve(0.5)
            hide drk with dissolve
            show dv frust with dissolve
            dv "Uh..."
            show dv cute with dissolve
            dv "I don't know."
            show dv sidetalk with dissolve
            dv "{color=#bc0b17}I can't really predict that{/color}, but I probably would."
            show dv neutral with dissolve
            "That's interesting..."
    stop music fadeout 4
    "I'm silent for another moment and I glance outside."
    "By the looks of it, it seems to be late."
    play music "ost/hospital.wav" fadein 7
    "I should be wrapping this up."
    m fabtalk "We don't have much time left."
    if RedHeart > 2:
        show dv sidesmile with dissolve
        dv "Oh? That's a shame..."
    scene mc with dissolve
    "I get up to lead him outside."
    m smile "Thank you for answering my questions."
    m talk "I will see you again soon."
    play sound "doorclose.ogg" fadein 1
    "I shut the door behind him hurriedly."
    "That was stressful..."
    stop music fadeout 8
    "I don't really know how to handle him and I feel a bit uncomfortable after interacting with him..."
    "I guess there's nothing I can do about it either way, but... he scares me a little."
    $sessions += 1
    show drk with dissolve
    $persistent.Michael=True
    show screen notify("{size=24} Your Characters Info screen has been updated!")
    hide screen redmeter
    hide screen easymeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump rednotes
        "No":
            pass
    jump breaknav
label red:
    if day < 6 and month==1:
        if redinteract == 0:
            jump red1
        elif redinteract == 1:
            jump red2
        elif redinteract == 2:
            jump red3
        elif redinteract == 3:
            jump red4
    else:
        jump redsession
    
label red1:
    play music "ost/hospital.wav" fadein 10
    scene bg mcdesk with dissolve
    if easymeter: 
        show screen easymeter
        show screen redmeter
    "Michael enters my office, smiling from ear to ear."
    show dv smirk with dissolve
    dv "Hello again~"
    if day == 2 and sessions == 0:
        show dv talk with dissolve
        dv "I have to say, I was hoping we'd see each other again soon."
        show dv sidetalk with dissolve
        dv "After yesterday."
        show dv talk with dissolve
        dv "So..."
        show dv neu with dissolve
        "He takes a seat in front of me."
        show dv smirk with dissolve
        dv "I'm your favourite?"
        m shock "What-?"
        show dv devil with dissolve
        dv "Oh come on, you had others to choose from for your first session today."
        show dv neutral with dissolve
        m gasp "I don't-"
        show dv smile with dissolve
        dv "Save the excuses~"
        "His smile feels genuine."
        "Well..."
        "It's not for any emotional reason, but I felt the need to see him first today."
    elif day > 3:
        show dv sidetalk with dissolve
        dv "It's been a while... Have you forgotten about me?"
        show dv frust with dissolve
        dv "I was waiting and waiting..."
        show dv talk with dissolve
        dv "And I hate waiting, you know?"
        show dv neu with dissolve
        dv "I literally have nothing better to do here..."
        show dv sidetalk with dissolve
        dv "That's kind of cruel, if you ask me."
        show dv frust with dissolve
        "...."
    else:
        "He takes a seat in front of me."
        show dv sidesmile with dissolve
        dv "I've been waiting for you to invite me here again ~"
        "I don't think I was looking forward to this..."
    stop music fadeout 5
    show dv neutalk with dissolve
    dv "This is our second session..."
    show dv talk with dissolve
    dv "You'll be asking me things, right?"
    play music "ost/neutral.wav" fadein 8
    show dv neutral with dissolve
    "That's what I had in mind. I wanted to gather information about him so I know what to ask later on."
    "I nod."
    show dv smile with dissolve
    dv "Oh, I love answering questions! Go ahead."
    "He seems quite enthusiastic. Let's see..."
    menu:
        "How many psychologists have you had already?":
            $professional += 1
            show dv frust with dissolve
            dv "Hmm..."
            show dv neutalk with dissolve
            dv "Should I count the ones that lasted less than a week?"
            show dv neu with dissolve
            m neu "...."
            m fabtalk "Sure."
            show dv frust with dissolve
            "He counts in silence for a moment."
            show dv talk with dissolve
            dv "Seventeen?"
            show dv neutalk with dissolve
            dv "From what I've noticed, the staff here changes a lot."
            show dv neu with dissolve
            "I bet."
        "Are you sharing a room with any patients?":
            $personal += 1
            show dv smirk with dissolve
            "He laughs."
            show dv devil with dissolve
            dv "Heh, I wish."
            show dv neutalk with dissolve
            dv "They were on the verge of putting me in {color=#bc0b17}XXI{/color} permanently at first."
            show dv sidetalk with dissolve
            dv "Though... that would probably be smart."
            show dv siden with dissolve
            "There's a hint of awkwardness in his voice."
            "That's new..."
    menu:
        "Are you allowed out of your room on breaks?":
            show dv shock with dissolve
            dv "Uh... sometimes?"
            show dv sidetalk with dissolve
            dv "I'm usually too lazy to get out anyway and no-one really pushes me outside."
        "What do you do most of the time?":
            show dv talk with dissolve
            dv "Nothing, really..."
            show dv sidesmile with dissolve
            dv "I sleep a lot - I'm lazy like that."
            show dv neutalk with dissolve
            dv "There isn't much to do here anyway..."
            show dv neutral with dissolve
            "I open my mouth to reply."
            show dv neutalk with dissolve
            dv "Hey, I'm not complaining..."
    show dv neu with dissolve
    "Interesting... Every patient seems to react to their situation completely differently."
    "I look at him closely..."
    "I can't drag my eyes away from his restrained hands."
    show dv siden with dissolve
    "This must be hell... and for such a long time, too."
    show dv sidetalk with dissolve
    dv "What do you want to say? I can tell what you're looking at..."
    show dv frust with dissolve
    stop music fadeout 5
    "I hesitate."
    m serious "You're not... always like this, right?"
    play music "ost/sunny.wav" fadein 5
    show dv smirk with dissolve
    dv "Would you want me to be~?"
    "I freeze."
    show dv sidetalk with dissolve
    dv "Just saying - some people are into that, I'm not judging."
    show dv siden with dissolve
    "That wouldn't even cross my mind if it wasn't for him..."
    "Uhh... I didn't want to think about that."
    m tsun "I don't think I'm one of them."
    show dv talk with dissolve
    dv "Fair enough. What were you asking me again...?"
    show dv neu with dissolve
    "Right... I was going to ask him questions."
    "Let's get back to something less controvertial..."
    stop music fadeout 4
    menu:
        "Do you know any of the patients here?":
            show dv talk with dissolve
            play music "ost/neutral.wav" fadein 8
            dv "Right now I remember all their faces, but I haven't spoken to most of them..."
            show dv sidetalk with dissolve
            dv "You could say I'm not very popular here..."
            show dv cute with dissolve
            dv "And by that I mean {color=#bc0b17}they usually avoid me."
            show dv sidetalk with dissolve
            dv "But there are a few people I've talked to, mostly ones that've been here for a long time and don't care much for their well-being."
            show dv talk with dissolve
            dv "I don't have anyone I would call a \"friend\" here, if that's what you meant."
            show dv neu with dissolve
            "I note his response."
        "Wait, are you into that?":
            $wrong += 2
            $personal +=1
            show dv devil with dissolve
            dv "I think that's a question for another time..."
            show dv siden with dissolve
            "Why did I have to ask that?"
            "I can't come up with anything to say."
            "The rest of our session passes in silence because of me."
            if sessions == 0:
                $firstpatient = "red"
            $redinteract += 1
            $sessions += 1
            show drk with dissolve
            hide screen redmeter
            hide screen easymeter
            "Should I make notes about what I've learned today?"
            menu:
                "Yes":
                    jump rednotes
                "No":
                    pass
            jump breaknav
    stop music fadeout 4
    show dv frust with dissolve
    "I open my mouth to ask him something else, but I notice that he's oddly quiet, staring intently at my desk."
    m serious "What's wrong?"
    play music "ost/tension.ogg" fadein 4
    "He's still not looking at me. That's unusual..."
    show dv sidetalk with dissolve
    dv "{color=#bc0b17}{i}One of your pens doesn't align with the rest."
    show dv frust with dissolve
    m gasp "Oh?"
    show dv moment with dissolve
    dv "It bothers me."
    show dv frust with dissolve
    "I adjust the pens quickly."
    show dv hes with dissolve
    dv "You made it worse..."
    show dv frust with dissolve
    "I don't think my hands are precise enough for this."
    "I lean in a bit to see the pens better."
    "He's right - they're not in order."
    "I do my best to fix it."
    m talk "Is it better now?"
    stop music fadeout 5
    show dv neutalk with dissolve
    dv "Slightly."
    show dv sidetalk with dissolve
    dv "You know, I would do it myself if I could, but..."
    show dv smile with dissolve
    "Right."
    play music "ost/tran.ogg" fadein 7
    show dv devil with dissolve
    dv "Heh, at least that makes you feel better about yourself, right?"
    m serious "What do you mean..?"
    show dv neutalk with dissolve
    dv "Being in control usually makes people feel more comfortable."
    show dv talk with dissolve
    dv "Am I wrong?"
    show dv neu with dissolve
    menu:
        "You're right":
            $personal += 1
            show dv sidetalk with dissolve
            dv "So at least there's that."
            show dv talk with dissolve
            dv "I bet if I were free, you {color=#bc0b17}wouldn't be so eager to talk with me{/color}."
            show dv neu with dissolve
            "He pauses."
            show dv smirk with dissolve
            dv "And if that's all it takes for me to be able to see your lovely face again, I'll take it~"
            "I decide not to comment on that."
        "If it was possible, I wouldn't want you to be like this":
            $RedHeart += 2
            $personal += 2
            show dv siden with dissolve
            "He's silent for a while."
            "His usual smile is gone and there's a hint of sadness on his face."
            show dv sadtalk with dissolve
            dv "{color=#bc0b17}I wish that was possible."
            show drk with Dissolve(0.75)
            show r 1 with dissolve
            show r 3 with Dissolve(0.3)
            show r 2 with Dissolve(0.3)
            $renpy.pause(0.75, hard = True)
            hide r with Dissolve(0.5)
            hide drk with dissolve
            show dv talk with dissolve
            dv "But that's just the way it is, so get used to it."
            show dv frust with dissolve
            dv "You can't change it, so there's no point complaining now."
            "I wonder if it's possible for him to be free one day..."
        "I won't answer that":
            $professional += 2
            show dv smirk with dissolve
            dv "You don't need to, I can tell I was right."
            "I won't grace that with a response."
    "It's time to end today's session."
    show dv neutral with dissolve
    m angry "I think we're running out of time."
    m neu "We will see each other again soon."
    show dv sidetalk with dissolve
    dv "If that's so..."
    stop music fadeout 5
    hide dv with dissolve
    "He leaves."
    if sessions == 0:
        $firstpatient = "red"
    $redinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen redmeter
    hide screen easymeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump rednotes
        "No":
            pass
    jump breaknav
label red2:
    play music "ost/sunny.wav" fadein 5
    scene bg mcdesk with dissolve
    "Here we are again."
    if easymeter: 
        show screen easymeter
        show screen redmeter
    show dv smirk with dissolve
    "I'm not sure what possessed me to want to see him today..."
    show dv smile with dissolve
    dv "Hello again~"
    "On the contrary, he seems to be perfectly comfortable around me."
    "Our last session gave me an idea of what he's like, but I'd like to learn more about his past."
    m talk "I have a few questions today."
    show dv cute with dissolve
    dv "Oh? You've come prepared, I see."
    stop music fadeout 5
    show dv sidesmile with dissolve
    m flirt "You could say that..."
    show dv neu with dissolve
    m serious "When did your illness start to develop?"
    show dv frust with dissolve
    play music "ost/hospital.wav" fadein 8
    "He looks away from me, wondering how to answer."
    show dv talk with dissolve
    dv "I can't tell... I think {color=#bc0b17}it's always been there{/color}, at least since I can remember."
    show dv neutral with dissolve
    m angrytalk "You don't think it was caused by anything? Any traumatic experiences, anything?"
    "He shakes his head."
    show dv frust with dissolve
    dv "It's {color=#bc0b17}just the way I am{/color}."
    "That's odd..."
    menu:
        "Have you ever had it treated?":
            $professional += 1
            show dv devil with dissolve
            dv "Pfft-"
            show dv talk with dissolve
            dv "Nah, I haven't."
            show dv neu with dissolve
            m serious "If you'd sought help sooner, you probably wouldn't have ended up here."
            show dv talk with dissolve
            dv "True."
            show dv neu with dissolve
            "He shrugs."
            show dv siden with dissolve
            dv "Oh well.."
        "Have you ever tried talking to anyone about it?":
            $personal += 1
            show dv talk with dissolve
            dv "{color=#bc0b17}My parents{/color}, actually. When I first thought something may be wrong."
            show dv sidetalk with dissolve
            dv "But... they said I'm exaggerating and that there's no real problem."
            show dv talk with dissolve
            dv "So yeah..."
            show dv sidesmile with dissolve
            dv "What can you do?"
            show dv siden with dissolve
            "So that's why he never sought help..."
            "If he did, he might not have ended up here."
    m talk "So... you were ill since childhood?"
    show dv neutral with dissolve
    "He nods."
    m talk "When exactly did it start to affect your life? When did you notice that something was wrong?"
    show dv talk with dissolve
    dv "I'm supposed to elaborate, right?"
    show dv neu with dissolve
    m neu "If that's possible."
    show dv sidetalk with dissolve
    dv "Alright then..."
    show dv frust with dissolve
    dv "I was around {color=#bc0b17}eight{/color} when I realized that... the way I think may be a bit different than for most people my age."
    show dv neutral with dissolve
    dv "Before that, I didn't really reflect on such things."
    show dv talk with dissolve
    dv "It occured to me that the other children aren't really exposed to things that I was used to by that time."
    show dv sidetalk with dissolve
    dv "So compared to them, I felt like there was something... {color=#bc0b17}wrong{/color} with me."
    show dv siden with dissolve
    menu:
        "Why was that?":
            $wrong +=1
            stop music fadeout 3
            show dv angrytalk with dissolve
            dv "\"Why\"?"
            show dv angry with dissolve
            dv "You're a psychologist, you studied this, right?"
            m fabtalk "I have. But every case is different, so I wanted to hear about you."
            play music "ost/tension.ogg" fadein 3
            show dv frust with dissolve
            dv "...."
            show dv talk with dissolve
            dv "{color=#bc0b17}At the age of 7, I was already sadistic."
            show dv angrytalk with dissolve
            dv "Is that normal? Because I don't think so."
            show dv sidetalk with dissolve
            dv "Do you really need me to say more to convince you?"
            stop music fadeout 3
            show dv siden with dissolve
            "He's silent for a moment."
            pause 1
        "Did it cause you to distance yourself from the others?":
            $RedHeart += 1
            show drk with Dissolve(0.75)
            show r 1 with dissolve
            show r 3 with Dissolve(0.3)
            show r 2 with Dissolve(0.3)
            $renpy.pause(0.75, hard = True)
            hide r with Dissolve(0.5)
            hide drk with dissolve
            show dv sidetalk with dissolve
            dv "I guess it did..."
            show dv talk with dissolve
            dv "I felt like they wouldn't really understand me if I lied to them about it, but they wouldn't like the truth."
            show dv frust with dissolve
            dv "But that never changed much..."
            show dv neutalk with dissolve
            dv "I only started interacting with people more once I got here."
            show dv devil with dissolve
            dv "I guess everyone knows about me already, so there's {color=#bc0b17}no point avoiding them anymore{/color}, heh..."
            stop music fadeout 5
            show dv siden with dissolve
            "That's interesting."
    "I should know more about the way his illness works before I move on."
    m angry "What exactly does your illness affect?"
    show dv talk with dissolve
    dv "Uhh... everything it can?"
    play music "ost/neutral.wav" fadein 8
    show dv sidetalk with dissolve
    dv "The way I think, my dreams, how I see and feel things, how I judge everything, how I act..."
    show dv neutalk with dissolve
    dv "It's pretty much always there."
    show dv talk with dissolve
    dv "So it's kind of hard to tell what's me and what's it."
    show dv siden with dissolve
    m serious "There really aren't times when it disappears? When you can think clearly?"
    show dv talk with dissolve
    dv "Nope, never. But I got used to it after some time."
    show dv neu with dissolve
    "That's problematic..."
    m talk "Any specific phobias? They often come with OCD."
    show dv neutalk with dissolve
    dv "I don't think so..."
    show dv neutral with dissolve
    "Okay then... What else is there to ask..?"
    "I should probably get some more concrete information about his past."
    "That's it..."
    menu:
        "Tell me more about what you did to these nurses":
            $professional += 1
            stop music fadeout 6
            m talk "On Monday, you said that you hurt some of the nurses when you first came here. What's the full story?"
            show dv sidetalk with dissolve
            dv "Oh, that... that was the last time it happened to me."
            show dv talk with dissolve
            play music "ost/tension.ogg" fadein 6
            dv "I just got inside and there were a few nurses in the reception area."
            show dv sidetalk with dissolve
            dv "I don't actually remember their faces anymore..."
            show dv frust with dissolve
            dv "One of them was supposed to lead me somewhere."
            dv "She... she touched my hand for a moment and..."
            show dv noeyes with dissolve
            dv "I guess that's all it took."
            "Does he really need so little to snap completely?"
            "I said it before and I'll say it again - they really have reasons to keep him like this."
            show dv neu with dissolve
            m angry "How severely did you hurt them?"
            show dv sidesmile with dissolve
            dv "Heh... that question alone proves how little you understand about my illness."
            show dv neutalk with dissolve
            dv "I don't remember - I genuinely don't."
            show dv talk with dissolve
            dv "When I snap like that, I stop caring about anything. {color=#bc0b17}I stop thinking."
            show dv sidetalk with dissolve
            dv "And I didn't get to calm down then to see what I did, so I wouldn't know."
            stop music fadeout 5
            show dv frust with dissolve
            m uncom "I see."
        "Have you ever hurt anyone outside the hospital?":
            $devilhurtbird = True
            $personal += 1
            $RedHeart += 1
            show dv frust with dissolve
            dv "...."
            "I might have to ask some more questions."
            "It's unlikely, but I need to get that out of the way."
            m serious "You... haven't killed anyone, right?"
            show dv hes with dissolve
            "He shakes his head quickly, looking at me with an intense expression."
            m uncom "And have you hurt anyone...? Besides these nurses..."
            show dv noeyes with dissolve
            "He's silent."
            stop music fadeout 6
            m sadtalk "Animals..?"
            show dv cute with dissolve
            dv "Define \"hurt\"...?"
            show dv siden with dissolve
            "Here we go then..."
            m serious "By \"hurt\" I mean either purpusely inflict pain or cause lasting damage."
            show dv frust with dissolve
            dv "That's an unfair definition-"
            "I glare at him."
            show dv angrytalk with dissolve
            dv "Alright, jeez... I have. Are you satisfied?"
            show dv frust with dissolve
            show drk with Dissolve(0.75)
            show r 1 with dissolve
            show r 3 with Dissolve(0.3)
            show r 2 with Dissolve(0.3)
            $renpy.pause(0.75, hard = True)
            play music "ost/tension.ogg" fadein 5
            hide r with Dissolve(0.5)
            hide drk with dissolve
            "I take a deep breath."
            m talk "What sort of animals?"
            show dv neutalk with dissolve
            dv "The biggest one was a small bird, I think."
            show dv talk with dissolve
            dv "I was maybe around {color=#bc0b17}15{/color}... I remember I was having a bad day."
            show dv hes with dissolve
            dv "And... it just so happened to land next to me."
            show dv notalk with dissolve
            dv "I-I couldn't stop myself..."
            show dv dark with dissolve
            "His voice is shaky."
            show dv kh2 with dissolve
            dv "{i}{color=#bc0b17}It... en- ded up in... thirteen pieces."
            show dv darktalk with dissolve
            dv "{i}{color=#bc0b17}I know because I counted them afterwards..."
            show dv kh2 with dissolve
            dv "{i}{color=#bc0b17}I-I remember... I didn't snap its neck for a while, because I wanted to... feel it try to escape..."
            pause 0.5
            show dv darktalk with dissolve
            dv "{i}{b}{color=#bc0b17}Have you ever wondered what sound a bird makes when its wings are being broken...?"
            show dv kh with dissolve
            "I can hear his ragged breath."
            "I've never seen anyone in such a state. He looks... there's no other way to call it... mad."
            menu:
                "{color=#bc0b17}Speak up":
                    $RedHeart += 1
                    m sjw "Michael."
                    show dv moment with dissolve
                    "He looks at me."
                    show dv cute with dissolve
                    "Slowly, his eyes return to normal."
                    show dv sidetalk with dissolve
                    dv "Sorry about that..."
                    stop music fadeout 6
                    show dv siden with dissolve
                    show drk with Dissolve(0.75)
                    show r 1 with dissolve
                    show r 3 with Dissolve(0.3)
                    show r 2 with Dissolve(0.3)
                    $renpy.pause(0.75, hard = True)
                    hide r with Dissolve(0.5)
                    hide drk with dissolve
                    show dv talk with dissolve
                    dv "I don't usually get asked about these things so directly..."
                    show dv frust with dissolve
                    play music "ost/tran.ogg" fadein 6
                    dv "So that caught me off-guard."
                    show dv cute with dissolve
                    dv "If it ever happens again, you should {color=#bc0b17}do what you just did{/color} and I'll... likely stop then."
                    show dv frust with dissolve
                    m serious "Are you okay..?"
                    show dv talk with dissolve
                    dv "Yeah, yeah I am. I should get used to this, right?"
                    show dv siden with dissolve
                "{color=#bc0b17}Wait":
                    show dv noeyes with dissolve
                    "I wait."
                    stop music fadeout 5
                    show dv frust with Dissolve(2.0)
                    "It takes some time, but he gradually returns to normal."
                    show dv talk with dissolve
                    dv "Ughh... {color=#bc0b17}you should've said something{/color}. It would pass more quickly then."
                    show dv sidetalk with dissolve
                    dv "And that way, you kind of left me to deal with that on my own..."
                    show dv neu with dissolve
                    play music "ost/hospital.wav" fadein 6
                    "I should keep that in mind if it ever happens again."
    "Our session is about to end."
    "This took a turn I didn't expect..."
    "But I did learn a lot about his past and the nature of his illness."
    m neutral "I think it's about time to end today's session."
    show dv neutral with dissolve
    "I notice that his usual smile is gone."
    show dv neutalk with dissolve
    dv "Goodbye, [name]."
    stop music fadeout 5
    play sound "doorclose.ogg" fadein 1
    hide dv with dissolve
    "He leaves."
    if sessions == 0:
        $firstpatient = "red"
    $redinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen redmeter
    hide screen easymeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump rednotes
        "No":
            pass
    jump breaknav
label red3:
    play music "ost/neutral.wav" fadein 5
    scene bg mcdesk with dissolve
    "He enters my office."
    if easymeter: 
        show screen easymeter
        show screen redmeter
    show dv smirk with dissolve
    dv "Who would've thought we'd be seeing each other so often~"
    show dv sidesmile with dissolve
    dv "I could've sworn you would freak out after last time."
    show dv siden with dissolve
    "Turns out I didn't."
    menu:
        "You'll have to try harder than that":
            $RedHeart += 1
            show dv smirk with dissolve
            show drk with Dissolve(0.75)
            show r 1 with dissolve
            show r 3 with Dissolve(0.3)
            show r 2 with Dissolve(0.3)
            $renpy.pause(0.75, hard = True)
            hide r with Dissolve(0.5)
            hide drk with dissolve
            dv "Is that a dare? Because I don't think you want to challenge me like that."
            show dv neu with dissolve
            m flirt "I'm your psychologist - whatever it takes to get more information about you."
            show dv smirk with dissolve
            dv "Heh. You asked for it."
        "I was tempted to":
            $personal += 1
            show dv smirk with dissolve
            dv "I can tempt you even more today, if that's what you want ~"
        "I didn't consider that":
            $professional += 1
            show dv sidesmile with dissolve
            dv "Guess I'll have to try harder then..."
    show dv neutalk with dissolve
    dv "Anyway..."
    show dv talk with dissolve
    stop music fadeout 5
    dv "Since you already asked me things last time..."
    show dv smile with dissolve
    dv "I had a {color=#bc0b17}bunch of questions for you."
    "I'm not sure that's how it works..."
    "I should be the one gathering information here, but he might trust me more if I agree..."
    menu:
        "I won't answer":
            $professional += 3
            $wrong += 1
            show dv frust with dissolve
            dv "Seriously..?"
            show dv sidetalk with dissolve
            dv "You're no fun..."
            scene black with Dissolve(2.0)
            "We talked for a while then, but he wasn't very willing to answer my questions."
            "I guess he was more serious about it then I thought."
            "Well, my job is my responsibility."
            "Nothing noteworthy happened until the end of our session."
            if sessions == 0:
                $firstpatient = "red"
            $redinteract += 1
            $sessions += 1
            show drk with dissolve
            hide screen redmeter
            hide screen easymeter
            "Should I make notes about what I've learned today?"
            menu:
                "Yes":
                    jump rednotes
                "No":
                    pass
            jump breaknav
        "Sure, ask away":
            $personal += 1
            play music "ost/mc.wav" fadein 6
            show dv sidesmile with dissolve
            dv "Yay~"
            show dv smile with dissolve
            dv "Hmmm, let's start with..."
            show dv cute with dissolve
            dv "When is your birthday?"
            show dv neu with dissolve
            m gasp "Where did that come from?"
            show dv smile with dissolve
            dv "I like numbers."
            show dv sidesmile with dissolve
            dv "As well as having a lot of that kind of information on people."
            "I guess that makes sense..."
            m fabtalk "It's the 24th of October."
            show dv neu with dissolve
            dv "...that's fitting."
            m gasp "Why is that?"
            show dv neutalk with dissolve
            dv "It's the color scheme."
            show dv smile with dissolve
            "...."
            m talk "What about you?"
            show dv neutalk with dissolve
            dv "{color=#bc0b17}The 9th of June."
            show dv neu with dissolve
            "June being the sixth month makes it oddly appropriate."
            show dv talk with dissolve
            dv "Actually, how old are you?"
            show dv neutral with dissolve
            m neu "I'm 28."
            show dv neu with dissolve
            dv "...."
            show dv neutalk with dissolve
            dv "Really? You look younger than that."
            show dv neu with dissolve
            m flirt "I'll take that as a compliment."
            show dv smile with dissolve
            dv "You should."
            show dv sidetalk with dissolve
            dv "I'm {color=#bc0b17}26{/color}, by the way. Though you probably already knew that from that file they keep about me."
            "So he's a bit younger than me... I guess that's to be expected."
            show dv smile with dissolve
            dv "What's your favourite color?"
            menu:
                "Blue":
                    show dv sidetalk with dissolve
                    dv "That's kind of a boring pick... doesn't everyone like blue?"
                "Red":
                    show dv neutalk with dissolve
                    dv "Then we have something in common."
                    show dv devil with dissolve
                    dv "Red like... I'm pretty sure you can tell why it's my favourite."
                    "...like {color=#bc0b17}blood{/color}."
                "Black":
                    show dv neutalk with dissolve
                    dv "Fair enough, that's my second favourite."
                "Pink":
                    show dv cute with dissolve
                    dv "You're serious, aren't you?"
                    show dv sidesmile with dissolve
                    dv "That's cute."
            show dv talk with dissolve
            dv "How many patients do you have?"
            show dv neutral with dissolve
            m angry "Four in total."
            show dv cute with dissolve
            dv "Is that a lot?"
            show dv neu with dissolve
            m talk "I don't think so."
            show dv frust with dissolve
            dv "Yeah, assuming there's up to 30 patients, we'd need 7.5 psychologists like you."
            show dv talk with dissolve
            dv "And there's {color=#bc0b17}four of you{/color}, as far as I know."
            show dv siden with dissolve
            m fabtalk "Judging by the offices, that seems about right. I haven't actually met any of them yet."
            show dv neutalk with dissolve
            dv "You're already the best one I've had so far, so I don't think you're missing out on much."
            show dv neu with dissolve
            menu:
                "Why do you think that?":
                    $RedHeart+=1
                    show dv sidetalk with dissolve
                    dv "I guess... you're talking to me like you would to a normal person."
                    show dv frust with dissolve
                    dv "Sure, you're a bit clumsy at times, but I don't really care."
                    show dv hes with dissolve
                    dv "You're... kind of more open than them. That's probably why I think you're better."
                    show drk with Dissolve(0.75)
                    show r 1 with dissolve
                    show r 3 with Dissolve(0.3)
                    show r 2 with Dissolve(0.3)
                    $renpy.pause(0.75, hard = True)
                    hide r with Dissolve(0.5)
                    hide drk with dissolve
                "I've barely started working here":
                    $personal += 1
                    show dv sidesmile with dissolve
                    dv "Then I guess you're just talented."
                    show dv talk with dissolve
                    dv "And besides, does it really matter? The rest of them only got worse over time."
                "You don't know all of them":
                    $professional += 1
                    show dv sidetalk with dissolve
                    dv "Jeez, okay..."
                    show dv frust with dissolve
                    dv "I was trying to be nice for once..."
            show dv neutalk with dissolve
            dv "...So what are your other patients like?"
            show dv sidetalk with dissolve
            dv "Actually, you can just give me the names. Unless it's classified or whatever..."
            show dv neu with dissolve
            m fab "I don't think it is."
            m talk "Other than you, I'm seeing Charlie from room IX, Tom from XVI and William from XIX."
            show dv frust with dissolve
            dv "I don't know the Tom guy, so he must be new, but other than that..."
            show dv cute with dissolve
            dv "Wait, you have Moore as well? Oh damn, that's a coincidence."
            show dv smile with dissolve
            m neu "...?"
            show dv sidetalk with dissolve
            dv "Uh, I would label our relationship as \"it's complicated\"."
            show dv talk with dissolve
            dv "I mean, he probably hates me at this point - I guess?"
            show dv frust with dissolve
            dv "I don't really get him, anyway."
            show dv smile with dissolve
            dv "Still, I like the guy - he's alright."
            "It never really occured to me that some of my patients may know each other..."
            "I guess they live here, so it's likely for them to have interacted at some point."
            show dv sidetalk with dissolve
            dv "And about Charlie... I've seen him a couple of times. He doesn't seem bothered by me, so that's kind of neat."
            show dv frust with dissolve
            dv "But it's not much fun to talk to someone who doesn't really understand everything you say."
            stop music fadeout 5
            "...."
            show dv siden with dissolve
            "I remember our last session... Namely the end of it."
            m serious "Can I ask you about the last time we met?"
            show dv neutalk with dissolve
            dv "Uhh... I guess?"
            show dv neu with dissolve
            play music "ost/tension.ogg" fadein 8
            if devilhurtbird:
                m angry "How did killing that bird make you feel?"
                show dv siden with dissolve
                m serious "Did it bring you any satisfaction, or a sense of fulfillment?"
                show dv sidetalk with dissolve
                dv "...no."
                show dv frust with dissolve
                dv "{color=#bc0b17}The things in my head{/color} were silent for a moment, but..."
                show dv sadtalk with dissolve
                dv "After that, they only got worse."
                show dv sad with dissolve
                dv "So they wouldn't stop until I killed it and then when I ripped it apart, they still weren't satisfied."
                show dv talk with dissolve
                dv "It's not a question of satisfying it, because it's impossible."
                show dv sad with dissolve
                dv "The only thing I can do is {color=#bc0b17}muffle them{/color} for a few seconds."
                show dv frust with dissolve
                dv "...Because I'm far past the point where I could give them everything they demanded."
                show dv neu with dissolve
                m talk "So there was a time when you did everything they wanted you to?"
                show dv sidetalk with dissolve
                dv "Yeah, {color=#bc0b17}when I was a child{/color}. I didn't really get how that could be dangerous - it started out kind of innocently."
                show dv sadtalk with dissolve
                dv "But..."
                show dv frust with dissolve
                stop music fadeout 5
                dv "By 13 it became unbearable."
                show dv sadtalk with dissolve
                dv "I knew I couldn't hurt other people, so I started trying to repress that, since there was no way to make it stop completely."
                show dv sad with dissolve
                menu:
                    "I'm so sorry to hear that":
                        show dv neutalk with dissolve
                        play music "ost/hospital.wav" fadein 6
                        dv "Hey, there's no point pitying me."
                        show dv talk with dissolve
                        dv "I lived like that {color=#bc0b17}my whole life{/color}, I got used to it."
                    "What about now?":
                        $RedHeart += 1
                        show dv gasp with dissolve
                        dv "What-?"
                        show dv neutral with dissolve
                        m talk "Are you still trying to repress it?"
                        play music "ost/hospital.wav" fadein 8
                        show dv sidetalk with dissolve
                        dv "Well..."
                        show dv frust with dissolve
                        dv "I know I can't really hurt anyone like this, but..."
                        show dv neutalk with dissolve
                        dv "Yeah. In a way, I am."
                        show dv neu with dissolve
                        dv "If I wasn't constantly stopping myself, I wouldn't be able to talk to you like this."
                        show drk with Dissolve(0.75)
                        show r 1 with dissolve
                        show r 3 with Dissolve(0.3)
                        show r 2 with Dissolve(0.3)
                        $renpy.pause(0.75, hard = True)
                        hide r with Dissolve(0.5)
                        hide drk with dissolve
                        show dv frust with dissolve
                        m sad "Is it really so difficult for you to repress these thoughts?"
                        show dv sad with dissolve
                        dv "If I'm being completely honest, it is. But I've handled myself pretty well so far... most of the time."
                    "You could stop it if you tried":
                        play music "ost/tension.ogg" fadein 3
                        show dv angrytalk with dissolve
                        dv "\"If I tried\"? Like I haven't!"
                        show dv frust with dissolve
                        dv "I'm telling you, it's impossible."
                        show dv sidetalk with dissolve
                        dv "And even if it was, I'm too lazy to try."
            else:
                m talk "Can you tell me more about how you hurt these nurses? How did it make you feel?"
                show dv frust with dissolve
                dv "That's a tough one..."
                show dv neutalk with dissolve
                dv "It was just... {color=#bc0b17}chaos."
                show dv talk with dissolve
                dv "When you repress these things for years and something finally makes you break after all that..."
                show dv sidetalk with dissolve
                dv "It's {color=#bc0b17}overwhelming{/color}, to be honest."
                show dv frust with dissolve
                dv "The amount of feelings you didn't allow yourself to experience, sounds, colors... It's too much to process at once."
                show dv talk with dissolve
                dv "So it becomes a blur."
                show dv neutalk with dissolve
                dv "I don't \"feel\" any way in particular in that state, I don't really have the time to think about that."
            stop music fadeout 7
            show dv siden with dissolve
            m neu "...."
            show dv neutalk with dissolve
            dv "Well, I think it's about time for me to leave."
            show dv neutral with dissolve
            "I nod."
            m fabtalk "Thank you for today."
            show dv smile with dissolve
            dv "Always a pleasure to see you, [name]~"
            hide dv with dissolve
            "He leaves and I'm left to ponder what he told me today."
            "I hope I can help him somehow..."
    if sessions == 0:
        $firstpatient = "red"
    $redinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen redmeter
    hide screen easymeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump rednotes
        "No":
            pass
    jump breaknav
label red4:
    scene bg mcdesk with dissolve
    play music "ost/sunny.wav" fadein 6
    show dv smile with dissolve
    if easymeter: 
        show screen easymeter
        show screen redmeter
    "Michael enters my office with the usual smile on his face."
    m gasp "Why so cheerful today?"
    show dv sidetalk with dissolve
    dv "Today is our fifth session this week..."
    show dv smirk with dissolve
    dv "That means we've been meeting {color=#bc0b17}every day{/color} since you started to work here~"
    show dv sidesmile with dissolve
    dv "I think I may be your favourite..."
    "It's true that I've been seeing him as often as possible this week..."
    m flirt "I don't know about favourites, but I intend to keep seeing you every day if possible."
    show dv moment with dissolve
    dv "...You do?"
    "I nod."
    show dv smile with dissolve
    "He smiles at me. I'm glad he at least appreciates what I do for him."
    stop music fadeout 5
    m talk "Moving on..."
    show dv neu with dissolve
    m neu "I had a few questions for today."
    show dv talk with dissolve
    dv "I'm all ears. What do you want to know?"
    show dv neu with dissolve
    play music "ost/neutral.wav" fadein 7
    m angry "You said yesterday that you never had your illness treated."
    "He nods."
    m serious "So how did you end up here?"
    show dv cute with dissolve
    dv "Uhhh..."
    show dv sidetalk with dissolve
    dv "I was actually {color=#bc0b17}arrested."
    show dv siden with dissolve
    m angry "Care to elaborate on that?"
    show dv talk with dissolve
    dv "You know, that's kind of a long story... It would probably take a few sessions to explain properly."
    show dv sidetalk with dissolve
    dv "How about {color=#bc0b17}next week{/color}?"
    show dv sidesmile with dissolve
    dv "I'll tell you all about what happened before I was admitted then - we'll have lots of time if you want to keep talking every day."
    "That sounds reasonable."
    m fabtalk "Alright, next week it is then. Don't forget."
    show dv smirk with dissolve
    dv "I won't."
    show dv neu with dissolve
    m talk "Thankfully, I had some more questions for you."
    show dv sidesmile with dissolve
    dv "I hoped so... it would be awkward if you ran out of things to talk about."
    menu:
        "Where did you live before you got here?":
            show dv talk with dissolve
            dv "Outskirts of the city. It's a big place, I think most people here used to live there."
            show dv sidetalk with dissolve
            dv "But to be honest, it's a pretty shitty place to live."
            show dv frust with dissolve
            dv "...At least in my opinion."
            m neu "I actually used to live outside the city, closer to the forest."
            show dv neutalk with dissolve
            dv "Oh. So you're from around here as well?"
            show dv neutral with dissolve
            "I nod."
        "Were you studying before you got here?":
            $RedHeart +=1
            show dv talk with dissolve
            dv "The short answer to that is... \"no\"."
            show dv sidetalk with dissolve
            dv "I figured university is kind of a waste of time for me, since I always got distracted and had trouble studying at school."
            show dv talk with dissolve
            dv "So I've been kind of going from job to job, you know? Whatever could occupy my thoughts for some time was good."
            show dv neutral with dissolve
            show drk with Dissolve(0.75)
            show r 1 with dissolve
            show r 3 with Dissolve(0.3)
            show r 2 with Dissolve(0.3)
            $renpy.pause(0.75, hard = True)
            hide r with Dissolve(0.5)
            hide drk with dissolve
    m talk "...Have you ever been in a relationship?"
    show dv sidetalk with dissolve
    dv "{color=#bc0b17}Once{/color}, actually. Not so long ago..."
    show dv siden with dissolve
    menu:
        "How long were you together?":
            show dv talk with dissolve
            dv "About a year, I think?"
        "Why did you break up?":
            show dv neu with dissolve
            dv "Technically, we never did, but {color=#bc0b17}we stopped seeing each other{/color} after I got here."
    show dv neu with dissolve
    m serious "What was she like?"
    show dv talk with dissolve
    dv "Let me think..."
    show dv neutral with dissolve
    "He looks at me analytically."
    show dv talk with dissolve
    dv "She was shorter than you."
    show dv neu with dissolve
    m neu "Anything else?"
    show dv sidetalk with dissolve
    dv "I'd say she was kind of shy... but stubborn, as well?"
    show dv talk with dissolve
    dv "The most accurate description would probably be - {color=#bc0b17}the kind of person who seems polite and quiet at first, but then you realize she's just hiding things from you."
    show dv frust with dissolve
    dv "But it's not like she had any real issues, she was just... normal, I guess."
    stop music fadeout 5
    "The way he says it makes it sound like an insult."
    show dv talk with dissolve
    dv "And what about you? It's not fair if I'm the only one sharing that stuff ~"
    show dv neutral with dissolve
    play music "ost/sunny.wav" fadein 6
    menu:
        "I've had a couple of boyfriends already":
            show dv neutalk with dissolve
            dv "Oh? Damn, you sound like you have some serious experience."
            show dv siden with dissolve
            m serious "I wouldn't say that, it was nothing serious."
        "I had a few girlfriends":
            show dv sidesmile with dissolve
            dv "Now that's interesting..."
            show dv talk with dissolve
            dv "What was it like?"
            show dv smirk with dissolve
            m serious "I can't really tell, it never got serious."
        "I've never been in a relationship":
            $RedHeart += 1
            show dv cute with dissolve
            dv "Is that so..?"
            show dv sidesmile with dissolve
            dv "With a face as pretty as yours, I find that hard to believe ~"
            show dv neu with dissolve
            show drk with Dissolve(0.75)
            show r 1 with dissolve
            show r 3 with Dissolve(0.3)
            show r 2 with Dissolve(0.3)
            $renpy.pause(0.75, hard = True)
            hide r with Dissolve(0.5)
            hide drk with dissolve
            m blush "..."
            "Am I... blushing?"
        "I won't answer that":
            $professional +=1
            show dv sidesmile with dissolve
            dv "Can't say I haven't tried..."
    "In a moment of silence, I'm reminded of my upcoming conversation with Dr. Sharpe."
    "He told me to meet him in his office after I finish my work here."
    "Have I done well in this job?"
    "Or will he fire me..?"
    "I wonder what Michael thinks about it..."
    stop music fadeout 5
    menu:
        "{color=#bc0b17}Ask him": 
            $RedHeart+=1
            show drk with Dissolve(0.75)
            show r 1 with dissolve
            show r 3 with Dissolve(0.3)
            show r 2 with Dissolve(0.3)
            $renpy.pause(0.75, hard = True)
            hide r with Dissolve(0.5)
            hide drk with dissolve
            m talk "My boss asked me to meet him today after work..."
            show dv neutral with dissolve
            m fabtalk "To see if I handled the job well and everything..."
            m serious "He said he would fire me if I failed this week."
            show dv neu with dissolve
            dv "And do you think you failed?"
            m frusttalk "I don't know... what do you think?"
            if RedHeart>=13:
                play music "ost/mc.wav" fadein 6
                show dv sidetalk with dissolve
                dv "I can only judge how well you did with me and I think you shouldn't worry about that."
                show dv smirk with dissolve
                dv "Though it would be hilarious if you really sucked at handling the others..."
                show dv neutral with dissolve
                m frusttalk "I don't think I do."
                show dv sidesmile with dissolve
                dv "Then you shouldn't be fired unless you do something unbelievably stupid during that talk today..."
                show dv smile with dissolve
                dv "You wouldn't do that, though, right? You're pretty smart, after all."
            else:
                play music "ost/neutral.wav" fadein 6
                show dv talk with dissolve
                dv "Uhh... I guess I can wish you luck."
                show dv neutral with dissolve
            m flirt "Thanks."
            show dv neutral with dissolve
            m neu "I think it's time to end our last session this week."
            "I follow him to the door."
            m smile "It's been a pleasure to work with you so far."
            if RedHeart >=13:
                show dv smirk with dissolve
                dv "Why so formal?"
                show dv sidesmile with dissolve
                dv "I really hope you don't get fired today. You're the best psychologist here."
                show dv smile with dissolve        
                dv "And I still have to tell you how I got here, so..."
                show dv neu with dissolve
                dv "Don't you dare ditch me like that."
                show dv smile with dissolve
                dv "See you next week, [name]~"
            else:
                show dv talk with dissolve
                dv "Sure. See you next week."
        "{color=#bc0b17}Dismiss him":
            show dv neutral with dissolve
            m neu "I think it's time to end our last session this week."
            "I follow him to the door."
            show dv neu with dissolve
            m talk "It's been a pleasure to work with you so far."
            show dv talk with dissolve
            dv "Sure. See you next week."
    play sound "doorclose.ogg" fadein 1
    stop music fadeout 5
    scene bg mc with dissolve
    "He leaves."
    if RedHeart>=13:
        play music "ost/tran.ogg" fadein 6
        "Why did I choose to spend time with him specifically..?"
        "I think I know the answer to that."
        "There's something pulling me towards him - maybe it's his strange charm, or how casual he seems to act around me."
        "Then there's his illness. It ruined his life, I can tell - even if he never complains."
        "His mind has been corrupted since childhood... of course it affected him."
        "And... then there's the last reason why I find him to intruiging..."
        "The way he makes me go from pity for him to fear of him and back."
        "He's unpredictable. Maybe that's what I'm drawn to."
        stop music fadeout 5
    else:
        "I hope I can keep seeing him next week."
    if sessions == 0:
        $firstpatient = "red"
    hide screen redmeter
    hide screen easymeter
    $redinteract += 1
    $sessions += 1
    show drk with dissolve
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump rednotes
        "No":
            pass
    jump breaknav
### HERMIT NAVIGATION ##########################
################################################
label blueintro:
    "I've dealt with schizophrenia before, so I know roughly what to expect."
    "I'm still very curious to meet him, though."
    scene bg mcdesk with dissolve
    $blueintro = 1
    play music "ost/sunny.wav" fadein 6
    "A {color=#5185ff}tall young man{/color} enters my office."
    show h happy with dissolve
    h "Hello~!"
    if easymeter: 
        show screen easymeter 
        show screen bluemeter
    show h smile with dissolve
    "I'm slightly surprised by his cheerfulness, but I smile back at him."
    m talk "Take a seat, please."
    show h neu with dissolve
    "He listens to me and sits down."
    show h siden with dissolve
    "He looks around the office, seeming interested in everything other than me."
    m smile "I'm [name] Hart, your new psychologist."
    m flirt "It's nice to meet you."
    show h happy with dissolve
    h "Nice to meet you too~"
    show h smile with dissolve
    h "I'm Charlie. I don't have a last name."
    show h sidesmile with dissolve
    "He smiles innocently, like he's completely oblivious to how unusual this situation is."
    "His file didn't list his last name, though... Is it possible that nobody knows what it is?"
    "I'll have to ask about him around the hospital sometime..."
    m serious "Why don't you have a last name?"
    show h frust with dissolve
    stop music fadeout 5
    h "I don't know..."
    show h talk with dissolve
    h "Why do people always ask me that?"
    show h frust with dissolve
    play music "ost/neutral.wav" fadein 6
    menu:
        "Because it's suspicious":
            $professional += 1
            show h gasp with dissolve
            h "Huh...?"
            show h sadtalk with dissolve
            h "Am I... suspicious...?"
            show h sad with dissolve
        "Because you act like it doesn't matter":
            $personal += 1
            show h talk with dissolve
            h "Why should it matter, anyway?"
            show h bored with dissolve
            h "It's kind of pointless."
        "I don't know":
            $wrong += 1
            show h angrytalk with dissolve
            h "Then why were you even asking?"
            show h angry with dissolve
            m talk "That's..."
            show h neu with dissolve
            "He's right, in a strange way."
    "He must have a name, he just doesn't know it."
    "And somehow the staff hasn't managed to identify him."
    "Very odd..."
    show h siden with dissolve
    "He keeps shifting in his chair, like a restless child who wants to run around and play instead of sitting in one place."
    "Well, sadly he has to last some time here with me."
    "With how distracted he is, I doubt I'll get much information out of him."
    "I have to grab his attention somehow."
    "What should I ask...?"
    menu:
        "How old are you?":
            show h sidetalk with dissolve
            h "Let me think..."
            show h gasp with dissolve
            h "I feel like I'm close to... {color=#5185ff}23? 24{/color}?"
            show h smile with dissolve
            "So he doesn't know that as well."
        "Where did you live before here?":
            $BlueHeart += 1
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
            show h sidetalk with dissolve
            h "I don't really know what's outside and I don't remember living anywhere else..."
            show h neu with dissolve
            "It's worse than I thought."
    "He doesn't seem to know anything about himself, other than his first name."
    "Could it be because of a permanent memory loss? I can't think of a mental illness that could cause something like that..."
    "I'll have to learn more about the circumstances of him being admitted here eventually."
    m talk "How long have you been here?"
    show h angrytalk with dissolve
    h "What do you mean...?"
    show h angry with dissolve
    m serious "In this hospital. How long has it been since you'd came here?"
    show h sadtalk with dissolve
    h "I... I don't... understand?"
    show h sidetalk with dissolve
    h "{color=#5185ff}I don't remember ever living anywhere else{/color}, so I can't tell..."
    show h siden with dissolve
    "This is difficult..."
    menu:
        "How can you not know that?":
            $wrong +=1
            $professional +=1
            show h sadtalk with dissolve
            h "I... I..."
            show h angrytalk with dissolve
            h "Stop asking me already, I told you I don't know!"
            show h frust with dissolve
            "I give up asking for now."
            "It seems to be pointless."
        "It must be difficult not to know any of that":
            $personal += 1
            show h neu with dissolve
            h "It's not."
            show h happy with dissolve
            h "I don't remember what it was like to know that~"
            show h sidesmile with dissolve
            "He laughs, but it feels empty."
            "It feels wrong, laughing it off like that."
        "I won't ask you about it further":
            $BlueHeart+=1
            show h gasp with dissolve
            h "You... won't?"
            show h happy with dissolve
            h "Thanks, [name]~"
            show h sidesmile with dissolve
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
            "Oh. At least he can't stay anxious for long..."
            "And it looks like he's completely relaxed again."
    stop music fadeout 4
    m neu "So..."
    "Despite everything, I want to gather some basic information."
    m serious "You have schizophrenia, right?"
    play music "ost/sunny.wav" fadein 3
    show h gasp with dissolve
    h "Yes-!"
    show h sadsmile with dissolve
    h "Sorry... I just get so excited whenever I can answer a question from you."
    show h talk with dissolve
    h "At least, {color=#5185ff}that's what the doctors told me{/color}... About my illness."
    stop music fadeout 5
    show h sad with dissolve
    "He trails off, realising that he doesn't even know that for sure."
    "I feel sorry for him."
    show h frust with dissolve
    play music "ost/tension.ogg" fadein 12
    "He's silent, looking around with an intense expression."
    "This time he doesn't look as restless or distracted as before... he seems more uncomfortable."
    show h siden with dissolve
    "Suddenly, he turns his head a bit to the right and focuses on something in the distance."
    "I can't quite notice what he's looking at..."
    show h bored with dissolve
    "He looks more depressed than before when he looks at me again."
    "Something must've occured to him..."
    menu:
        "Why are you suddenly so silent?":
            $wrong += 1
            "He turns to me as if he just noticed I'm there."
            show h gasp with dissolve
            h "H-huh...?"
            h "Oh, I was just..."
            show h sidesmile with dissolve
            h "Nevermind."
            show h happy with dissolve
            h "{color=#5185ff}I'm fine now~"
            show h smile with dissolve
            "I don't think he's being honest."
        "You can trust the doctors":
            $BlueHeart +=1
            $personal += 1
            show h sadtalk with dissolve
            h "You think so..?"
            show h bored with dissolve
            stop music fadeout 5
            m conf "I'm sure of it. They only want to help you."
            "He thinks for a moment before his eyes light up suddenly."
            show h gasp with dissolve
            play music "ost/mc.wav" fadein 6
            h "No-one ever told me otherwise, so {color=#5185ff}it must be true{/color}!"
            show h happy with dissolve
            h "Thank you, thank you so much~ !"
            show h smile with dissolve
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
            "I had no idea he would react so emotionally. I suppose I was right to say that."
        "{color=#5185ff}Stay silent":
            $professional += 1
            "He's still ignoring me..."
            "A while passes until he looks at me again."
            stop music fadeout 5
            show h happy with dissolve
            h "Oh, hi!"
            show h sidesmile with dissolve
            h "I forgot about you..."
            "How could he have forgotten that I'm right in front of him...?"
            play music "ost/neutral.wav" fadein 5
    "I glance at the time."
    "We just have a few more minutes."
    show h neu with dissolve
    m smile "Charlie, it was nice to talk to you. I think we're running out of time for today."
    show h sadsmile with dissolve
    h "Really..? And I was hoping we could talk for longer..."
    m serious "Maybe some other time. I'll see you again soon."
    show h happy with dissolve
    stop music fadeout 8
    h "Yay~ Thank you for talking to me, [name]."
    hide h with dissolve
    "He leaves with a cheerful smile."
    "I wonder... His file isn't technically wrong, but he doesn't seem to be just schizophrenic."
    "There's something wrong about his memory as well..."
    "Not to mention his mood swings and lack of understanding of his situation."
    "This will be a tough patient to deal with..."
    "But at least he was nice to me. That should make him a bit easier to interact with..."
    "Charlie... what an odd case."
    $sessions += 1
    show drk with dissolve
    hide screen bluemeter
    hide screen easymeter
    $persistent.Charlie=True
    show screen notify("{size=24} Your Characters Info screen has been updated!")
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump bluenotes
        "No":
            pass
    jump breaknav
label blue:
    if day < 6 and month==1:
        if blueinteract == 0:
            jump blue1
        elif blueinteract == 1:
            jump blue2
        elif blueinteract == 2:
            jump blue3
        elif blueinteract == 3:
            jump blue4
    else:
        jump bluesession
label blue1:
    scene bg mcdesk with dissolve
    "I'm about to see-"
    show h smile with dissolve
    play music "ost/sunny.wav" fadein 8
    h "Hello~"
    if easymeter: 
        show screen easymeter 
        show screen bluemeter
    "...well, he cut me off there... Charlie is here again."
    m fabtalk "How are you today?"
    show h sidesmile with dissolve
    h "It's so good to be here again~~"
    if day == 2:
        show h frust with dissolve
        h "Though... wasn't I just here yesterday? I think so..."
        show h neu with dissolve
        m neu "That's right."
        show h talk with dissolve
        h "You're my psychologist - [name]?"
        show h neu with dissolve
        "I nod."
        show h sidetalk with dissolve
        h "You invited me here so quickly then..."
        show h cute with dissolve
        h "Thank you~ I hate sitting in my room alone."
    elif day > 3:
        show h sidetalk with dissolve
        h "You... You're my psychologist, right?"
        show h neu with dissolve
        "I nod."
        show h talk with dissolve
        h "I'm sorry, it's been a while... I need some time to start recognizing you."
        show h neu with dissolve
    else:
        show h cute with dissolve
        "He smiles."
    m fabtalk "So, Charlie..."
    show h happy with dissolve
    h "Yes?"
    show h smile with dissolve
    "I smile at his enthusiasm."
    show h siden with dissolve
    m flirt "I tried asking you somethings last time, but you couldn't really answer anything."
    m talk "Do you think you can tell me anything other than your first name today?"
    show h frust with dissolve
    h "Umm... I know a couple of things about myself."
    m fab "Yes?"
    show h talk with dissolve
    h "I'm in a mental hospital, my room number is IX, I'm 6'6\" and I remember the name of every nurse here."
    show h sidesmile with dissolve
    h "I also like going outside whenever it's not too cold. And my favourite color is blue."
    show h talk with dissolve
    h "...That's about it."
    show h bored with dissolve
    "I guess he really doesn't know anything about his past."
    show h sidetalk with dissolve
    h "What about you, [name]?"
    show h smile with dissolve
    m shock "H-Huh?"
    show h sidesmile with dissolve
    h "Tell me something about yourself."
    menu:
        "I'm 28":
            show h gasp with dissolve
            h "You're so old-!"
            m shock "...Excuse me?"
            show h talk with dissolve
            h "I- I'm sorry, was that, um... insensitive?"
            show h bored with dissolve
            m conf "It's fine."
            show h sidesmile with dissolve
            h "Oh, thank you~"
        "I was born in that town nearby":
            show h talk with dissolve
            h "The one you can see from the windows?"
            show h smile with dissolve
            m talk "Yes."
            show h laugh with dissolve
            h "Oh, I wish I could go there sometime ~"
            show h smile with dissolve
        "I'm 5'5\"":
            show h gasp with dissolve
            h "Are you..?"
            show h laugh with dissolve
            h "You're so short, [name]~"
            show h cute with dissolve
            "I am mildly offended right now."
    show h smile with dissolve
    m flirt "And... this is my first week of work here."
    show h gasp with dissolve
    h "Really?"
    show h sidesmile with dissolve
    h "You could've said so earlier, I would've given you a tour of the hospital!"
    show h happy with dissolve
    h "You wouldn't have to get lost then..."
    show h smile with dissolve
    m talk "I think I can handle myself..."
    show h sad with dissolve
    m flirt "But thanks for the offer."
    show h happy with dissolve
    h "No problem! If you ever want to walk around anyway, I'm always free ~"
    show h smile with dissolve
    stop music fadeout 6
    "Aw, that's so nice of him... Maybe I should take a stroll around the hospital sometime with him."
    show h sadtalk with dissolve
    h "Ummm.... Was it hard to get a job here?"
    show h sad with dissolve
    play music "ost/neutral.wav" fadein 6
    menu:
        "Nah, it's easy":
            $personal+=1
            show h happy with dissolve
            h "That sounds great~!"
            show h sidesmile with dissolve
            h "I wish I could work somewhere as well..."
        "A little":
            $professional+=1
            show h frust with dissolve
            m cute "But hey, if I got this job it can't be that hard."
            show h happy with dissolve
            h "You're right! I could get a job once I'm out of here too, if I wanted to ~"
        "It was dreadful":
            $wrong+=1
            show h sadtalk with dissolve
            h "That... doesn't sound nice..."
            show h talk with dissolve
            h "But... it can't be that bad..."
            show h frust with dissolve
            h "...."
            show h happy with dissolve
            h "You're just really smart!"
    show h talk with dissolve
    h "How many patients do you have?"
    show h neu with dissolve
    m talk "Four, including you."
    show h cute with dissolve
    h "Do you have friends among the staff? I know everyone here ~"
    show h smile with dissolve
    m fabtalk "I've talked to a couple of people but... I guess making friends isn't exactly my priority here."
    show h talk with dissolve
    h "Then what is?"
    show h sidetalk with dissolve
    h "Why did you want to be a psychologist in the first place?"
    show h smile with dissolve
    "That's an interesting question..."
    menu:
        "I wanted to have an office":
            show h sidetalk with dissolve
            h "I see..."
            show h happy with dissolve
            h "You got your wish! I like this one."
            show h frusttalk with dissolve
            h "It's... really red, though..."
            show h sidesmile with dissolve
            h "My psychiatrist has a blue one. It's nicer there."
            show h neu with dissolve
            m angry "I like mine."
        "I like people":
            $empathy+=1
            $BlueHeart+=1
            show h laugh with dissolve
            h "That's such a nice thing to say~"
            show h smile with dissolve
            h "I think I like people as well..."
            show h kawaii with dissolve
            h "I like {i}you{/i}, [name]."
            show h smile with dissolve
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
        "I wanted to help people like you":
            $BlueHeart+=2
            $personal+=1
            show h gasp with dissolve
            h "Really..? Like me?"
            show h sidesmile with dissolve
            m conf "That's right."
            show h laughblush with dissolve
            h "Wow, I feel so special now ~"
            show h smile with dissolve
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
    show h cute with dissolve
    h "I like the staff here a lot. They're nice to me."
    show h smile with dissolve
    m flirt "They should be."
    show h laugh with dissolve
    h "I think they like me as well~"
    show h smile with dissolve
    "I wouldn't be surprised, with how friendly he seems. "
    m talk "What about the patients? Do you get along with them?"
    show h sidesmile with dissolve
    h "Most of them..."
    show h sadtalk with dissolve
    h "I think... some of them don't really want to talk to me."
    show h frust with dissolve
    h "I don't know why... I just want to be friends with them..."
    show h bored with dissolve
    m sadsmile "It happens sometimes."
    show h sad with dissolve
    h "Why?"
    show h neu with dissolve
    m fabtalk "Everyone has different people they like and don't like." 
    "...Besides, some of these patients have illnesses that force them to avoid others."
    show h sad with dissolve
    m talk "You can't be friends with everyone."
    show h gasp with dissolve
    h "...unless you act different around every person you meet."
    show h smile with dissolve
    m regrettalk "That... I don't think it's possible."
    show h sadtalk with dissolve
    h "Really?"
    show h sad with dissolve
    "I mean, unless you have DID and an insane amount of alters."
    show h neu with dissolve
    m angry "Besides, people would think it's not genuine."
    show h sadtalk with dissolve
    h "Oh... Not... genuine?"
    show h talk with dissolve
    h "What does it mean? What if there's no such thing as genuine?"
    show h sadtalk with dissolve
    h "Then we'd have to just keep pretending to be someone else the whole time."
    show h frust with dissolve
    h "...And that wouldn't be genuine."
    show h sad with dissolve
    h "...."
    show h talk with dissolve
    h "Even if we stuck to pretending to be one exact person at all times?"
    show h sad with dissolve
    m gasp "I... I don't know."
    m fabtalk "It's complicated."
    m talk "I think..."
    menu:
        "Everybody chooses how to pretend":
            $BlueHeart+=1
            $personal+=1
            show h talk with dissolve
            h "So... nobody is really genuine?"
            show h sad with dissolve
            m fabtalk "I mean..."
            m talk "To an extent, yeah."
            show h talk with dissolve
            h "Why?"
            show h sad with dissolve
            m frust "Because doing exactly what they'd want to at all times would be considered... improper, I guess."
            m talk "So I guess we all adjust however we can."
            show h frust with dissolve
            h "...if that's so..."
            show h happy with dissolve
            h "Thank you for explaining it to me, [name]."
            show h smile with dissolve
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
        "People should try not to lie":
            $professional+=1
            $wrong+=1
            show h gasp with dissolve
            h "Oh... You... You think so?"
            show h neu with dissolve
            m talk "I do."
            show h sad with dissolve
            h "...okay."
            show h siden with dissolve
            h "I'll keep that in mind."
        "As long as you're honest with the people you care about, it's fine":
            show h frust with dissolve
            h "But..."
            show h talk with dissolve
            h "If I stop lying to them, to the others it would seem like I'm not being honest."
            show h siden with dissolve
            "Wait, what..?"
            show h frusttalk with dissolve
            h "If someone treats people differently depending on their relationship... isn't that lying too?"
            show h bored with dissolve
            "Umm... no?"
            m talk "It's not."
            show h angrytalk with dissolve
            h "How can you know that for sure?"
            show h angry with dissolve
            m neu "I... I just do, I guess."
            show h cute with dissolve
            h "That's so amazing, [name]~!"
            show h happy with dissolve
            h "I wish I were like that, too!"
    show h frust with dissolve
    h "Ummm..."
    stop music fadeout 6
    show h siden with dissolve
    h "...."
    "He falls silent suddenly."
    m sad "Is something wrong?"
    show h angry with dissolve
    play music "ost/hospital.wav" fadein 7
    h "You... said people like different kinds of... other people?"
    m talk "That's right."
    show h frusttalk with dissolve
    h "So..."
    show h talk with dissolve
    h "What kind of people do you like, [name]?"
    show h smile with dissolve
    m gasp "Me?"
    show h laugh with dissolve
    h "Yes."
    show h cute with dissolve
    m fabtalk "I guess..."
    show h smile with dissolve
    "I never really thought about it, but..."
    menu:
        "The friendly ones":
            $personal+=1
            show h laugh with dissolve
            h "That's great!"
            show h sidetalk with dissolve
            h "...I'm friendly, right?"
        "The smart ones":
            $professional+=1
            show h talk with dissolve
            h "Like you? You're smart, you must be smart."
        "The honest ones":
            $wrong+=1
            h "...oh."
            show h sadsmile with dissolve
            h "You... you really care about that a lot, don't you?"
            show h neu with dissolve
            m "It's important."
            show h bored with dissolve
            h "...."
        "The strange ones":
            $BlueHeart+=1
            show h sidetalk with dissolve
            h "Like..."
            show h gasp with dissolve
            h "...like me?"
            m boresmile "You {i}are{/i} pretty... unusual."
            show h happy with dissolve
            h "Wow, that means you must like me, then!"
            show h smile with dissolve
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
    stop music fadeout 6
    show h siden with dissolve
    "He seems somehow distracted."
    "In a moment of silence, I look at him more closely..."
    "Something about his face bothers me... What is it?"
    play music "ost/neutral.wav" fadein 8
    m "Ummm... Excuse me, Charlie?"
    show h gasp with dissolve
    h "Yes-?"
    show h neu with dissolve
    "He seems a little startled."
    m regrettalk "It's a bit of an indelicate question, but..."
    show h laugh with dissolve
    h "Go ahead. People call me that all the time ~"
    show h cute with dissolve
    m talk "It's about your eyes."
    show h sidetalk with dissolve
    h "Oh, the nurses told me it can't be fixed."
    show h frust with dissolve
    h "It's just some weird muscle thing causing my right eye to be, um... a bit closed at all times."
    "Huh."
    show h talk with dissolve
    h "Does it bother you? It's really beyond my control."
    show h neu with dissolve
    m gasp "No no, I was just curious."
    stop music fadeout 5
    show h smile with dissolve
    h "Well, now you know."
    show h happy with dissolve
    h "If it bothers you, you can always just look at the left side of my face!"
    show h smile with dissolve
    play music "ost/sunny.wav" fadein 6
    "I guess... Jeez, this is ridiculous..."
    "I smile to myself. Charlie is really nice."
    "Unfortunately..."
    m talk "I think we're running out of time for today."
    show h sadtalk with dissolve
    h "Aww..."
    show h neu with dissolve
    m flirt "I'll see you again soon, I promise."
    show h cute with dissolve
    h "Thank you~"
    scene mc with dissolve
    stop music fadeout 4
    "He leaves. I enjoyed this second session - who wouldn't?"
    if sessions == 0:
        $firstpatient = "blue"
    $blueinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen easymeter
    hide screen bluemeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump bluenotes
        "No":
            pass
    jump breaknav
label blue2:
    scene bg mcdesk with dissolve
    "Charlie enters my office."
    play music "ost/sunny.wav" fadein 10
    show h cute with dissolve
    h "Hello~"
    if easymeter: 
        show screen easymeter 
        show screen bluemeter
    show h smile with dissolve
    m conf "It's good to see you again. Take a seat."
    show h sidetalk with dissolve
    h "Soo..."
    show h sidesmile with dissolve
    "He seems impatient."
    show h smile with dissolve
    h "What are we doing today?"
    m pity "I thought that... Since I talked a lot about myself last time, maybe I could ask you somethings today?"
    show h gasp with dissolve
    h "Ask... me?"
    show h sadtalk with dissolve
    stop music fadeout 6
    h "But... I don't know anything, I already told you..."
    m conf "These are questions even you'll be able to answer, so don't worry about it."
    show h sad with dissolve
    h "It's not about answering..."
    m gasp "Huh?"
    show h laugh with dissolve
    h "It's nothing. Nothing at all, [name] ~"
    play music "ost/neutral.wav" fadein 6
    show h cute with dissolve
    m fabtalk "Do you have any closer friends in the hospital?"
    show h frust with dissolve
    h "Ummm..."
    show h gasp with dissolve
    h "Real ones?"
    show h neu with dissolve
    m fab "...."
    show h laugh with dissolve
    h "I'm kidding, I don't have any imaginary friends."
    stop music fadeout 1
    show h sad with dissolve
    h "...even they left me."
    m gasp "What was that?"
    play music "ost/neutral.wav" fadein 10
    show h laugh with dissolve
    h "Oh, I'm just talking to myself ~"
    show h sadtalk with dissolve
    h "...definitely not to these imaginary friends, since I don't have any."
    show h talk with dissolve
    h "How could I be talking to someone who doesn't exist?"
    show h sidetalk with dissolve
    h "Though... is talking to myself any better?"
    show h frust with dissolve
    menu:
        "Imaginary friends don't exist either way":
            $BlueHeart+=1
            $professional+=1
            show h gasp with dissolve
            h "That's... such an enlightened thing to say."
            show h sidetalk with dissolve
            h "...you're right. I never thought of it that way."
            show h cute with dissolve
            h "You really are broadening my horizons, [name] ~"
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
        "At least you're real":
            $wrong+=1
            show h gasp with dissolve
            h "...."
            show h sad with dissolve
            h "...."
            m serious "What's wrong?"
            show h sidetalk with dissolve
            h "I'm... real..."
            show h siden with dissolve
            "He's silent for a while."
        "You can talk to me instead":
            $personal+=1
            show h laugh with dissolve
            h "You're right. That sounds like a great idea."
            show h neu with dissolve
            "He leans in a little to look me straight in the eye."
            show h smile with dissolve
            h "I'm going to talk to you now."
    show h talk with dissolve
    h "Do you have any other questi-"
    show h gasp with dissolve
    h "Oh wait. I didn't answer your previous one."
    show h sadtalk with dissolve
    h "I... I don't know."
    show h talk with dissolve
    h "How can I know who is my friend and who isn't?"
    show h sidetalk with dissolve
    h "I know everyone here, but... friendship is... something else..."
    stop music fadeout 5
    show h gasp with dissolve
    h "[name]?"
    show h neu with dissolve
    m serious "Yes?"
    show h talk with dissolve
    h "Can you tell me something?"
    show h neu with dissolve
    "I nod."
    show h sidetalk with dissolve
    h "What is friendship? How can I know I'm friends with someone?"
    play music "ost/tran.ogg" fadein 6
    show h neu with dissolve
    "He's asking a lot of difficult questions... I guess all I can do is try to define it as accurately as possible."
    m talk "Friendship is..."
    menu:
        "When you have someone very well and they know you":
            $professional+=1
            $wrong+=1
            show h sadtalk with dissolve
            h "I... I don't like the sound of that..."
            show h talk with dissolve
            h "...I don't know anything."
            show h sad with dissolve
            h "Nobody knows me."
            h "...so I have no friends."
        "When you really care about someone":
            $wrong+=1
            show h sad with dissolve
            h "...oh."
            show h sadtalk with dissolve
            h "I see..."
            show h frust with dissolve
            h "I don't like that definition..."
        "When you feel good around someone":
            $personal+=1
            $BlueHeart+=1
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
            show h gasp with dissolve
            h "\"Good\"?"
            show h neu with dissolve
            m conf "Yeah. Like, you're happier around them than usual."
            show h sidetalk with dissolve
            h "I see..."
            show h happy with dissolve
            h "Am I your friend, then?"
            show h neu with dissolve
            m shock "I'm... I'm your psychologist."
            show h sadtalk with dissolve
            h "Can't psychologists have friends?"
            show h sad with dissolve
            m uncom "I... I mean..."
            show h neu with dissolve
            m frust "It's complicated."
    stop music fadeout 7
    show h siden with dissolve
    h "...."
    m fab "I have another question."
    show h gasp with dissolve
    h "Huh?"
    show h neu with dissolve
    m talk "I noticed you're often distracted and look somewhere to the side."
    m angry "What do you see there?"
    show h frusttalk with dissolve
    h "Ummm... a lot of things."
    show h sidetalk with dissolve
    play music "ost/tension.ogg" fadein 10
    h "Sometimes I see some people. But... I also hear their voices."
    show h sad with dissolve
    h "It's like... they're somewhere in the distance."
    show h neu with dissolve
    m gasp "Like in they're in that room behind the wall?"
    show h talk with dissolve
    h "...Yes."
    show h sadtalk with dissolve
    h "But... the doctors say they're not real."
    show h frust with dissolve
    h "That... they only exist if someone else notices them."
    m talk "What did you see just now?"
    show h talk with dissolve
    h "Just..."
    show h frust with dissolve
    h "...darkness."
    show h sadtalk with dissolve
    h "Like it's night."
    show h frusttalk with dissolve
    h "I know it's not, but still..."
    show h siden with dissolve
    m smile "It's fine. I get it."
    m fabtalk "So you mostly see these things?"
    show h neu with dissolve
    "He nods."
    show h sidesmile with dissolve
    h "Oh, it's you again ~"
    m uncom "Who?"
    show h talk with dissolve
    h "There's this little girl I see sometimes. She never says anything."
    show h  with dissolve
    h "She just..."
    stop music fadeout 2
    show h sad with dissolve
    h "...leaves."
    pause 1
    play music "ost/tran.ogg" fadein 8
    menu:
        "What does she look like?":
            $professional+=1
            show h frusttalk with dissolve
            h "Um..."
            show h talk with dissolve
            h "She has blonde hair, she looks around 12."
            show h angry with dissolve
            m uncom "Is there anything unusual about her appearance?"
            show h frust with dissolve
            h "I don't think so..."
        "How does she make you feel?":
            show h frust with dissolve
            h "...."
            show h sadtalk with dissolve
            h "Kind of... sad."
            show h talk with dissolve
            h "I don't know why."
            show h sad with dissolve
            h "She seems lonely."
        "I'm sorry":
            $BlueHeart+=1
            $personal+=1
            show h neu with dissolve
            h "...."
            show h cute with dissolve
            h "You're so nice to me, [name] ~"
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
    m fabtalk "What other things do you see?"
    show h frust with dissolve
    h "Umm..."
    show h talk with dissolve
    h "Trees. Some kind of forest."
    show h sidetalk with dissolve
    h "Fog. Sometimes it's so thick I can't see anything else."
    show h neu with dissolve
    m neu "Are we alone now?"
    show h siden with dissolve
    "He looks around my office quickly."
    show h talk with dissolve
    h "I think so."
    show h siden with dissolve
    m angry "What about the voices?"
    show h sidetalk with dissolve
    h "It's... I can hardly ever make out any words."
    show h talk with dissolve
    h "It's like there's a whole crowd around me, talking."
    show h sidetalk with dissolve
    stop music fadeout 8
    h "But sometimes there's just one or two people."
    show h siden with dissolve
    menu:
        "Do they talk to you?":
            show h talk with dissolve
            h "Rarely... Most of the time it seems completely unrelated to anything else."
        "Do they say things about you?":
            $BlueHeart+=1
            show h talk with dissolve
            h "...sometimes."
            show h neu with dissolve
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
            show h sad with dissolve
            h "...."
            "Strangely, I don't think he wants to say anything about that."
        "Do they bother you?":
            $personal+=1
            show h talk with dissolve
            h "I mean... it's like hearing people talk normally."
            show h frusttalk with dissolve
            h "And I'm used to that. Somewhat."
            show h sidetalk with dissolve
            h "It's... hard to differenciate most of the time."
            show h neu with dissolve
    m serious "From what you remember, do these things change over time?"
    play music "ost/neutral.wav" fadein 8
    show h sidetalk with dissolve
    h "...not really."
    show h talk with dissolve
    h "It's been... quite consistent."
    show h neu with dissolve
    m angrytalk "And that little girl is the only person you've seen a lot of times?"
    show h frust with dissolve
    h "Umm..."
    show h talk with dissolve
    h "I sometimes see... a girl with long, black hair and blue eyes."
    show h sidetalk with dissolve
    h "She looks around my age."
    show h frust with dissolve
    h "She wears a black dress."
    m fabtalk "Does she talk to you?"
    show h talk with dissolve
    h "Sometimes..."
    show h sadtalk with dissolve
    h "Most of the time, I can see her walking through the hallways, just out of my reach. She's not looking at me."
    show h talk with dissolve
    h "But... other times she comes to my room and sits on the floor staring at me for a long time in silence."
    show h siden with dissolve
    m uncom "Have you ever tried talking to her?"
    show h cute with dissolve
    h "Of course I have."
    show h smile with dissolve
    h "I talk to everyone I meet here."
    show h sidetalk with dissolve
    h "But... over time, I realized that... nobody else really pays attention to her."
    show h sadtalk with dissolve
    h "So... I decided she must not really be there."
    show h frust with dissolve
    m angry "Right."
    m talk "And when she talks, what does she say?"
    show h sidetalk with dissolve
    h "It's... it's difficult to explain..."
    show h sadtalk with dissolve
    h "She says things I... don't really understand..."
    show h sad with dissolve
    "That's odd..."
    m fabtalk "So you see this dark-haired girl the most?"
    show h neu with dissolve
    h "I think so."
    m neu "Do you see anyone besides her and that younger girl?"
    show h siden with dissolve
    h "Umm..."
    show h talk with dissolve
    h "Some... people older than me... a few teenagers..."
    show h sadtalk with dissolve
    h "Some of them look... unwell."
    show h siden with dissolve
    m uncom "Like... sick?"
    stop music fadeout 1
    show h sidetalk with dissolve
    h "...like... dead."
    show h siden with dissolve
    m sadtalk "And they're walking around the hospital?"
    show h talk with dissolve
    h "Yes."
    show h neu with dissolve
    "That's... surprisingly dark."
    play music "ost/tension.ogg" fadein 8
    show h siden with dissolve
    m serious "What do they do?"
    show h frusttalk with dissolve
    h "They don't talk. I sometimes see them in other patients' rooms, or following some of them around."
    show h frust with dissolve
    m sad "Do they follow you around as well?"
    show h siden with dissolve
    h "Sometimes."
    show h talk with dissolve
    h "But... I can only remember the faces of those two girls."
    show h neu with dissolve
    m talk "So they're the most important?"
    show h sidetalk with dissolve
    h "Yes."
    show h siden with dissolve
    "I take a moment to make some sense out of that in my notes."
    m fab "Are you taking any medicine right now?"
    show h sidetalk with dissolve
    h "My psychiatrist thought it was for the best..."
    show h sad with dissolve
    "It certainly is."
    show h sadtalk with dissolve
    h "...I don't like medicine, though..."
    show h neu with dissolve
    stop music fadeout 6
    m uncom "Why is that?"
    show h sidetalk with dissolve
    h "It, um... makes me feel kind of... weird."
    show h frust with dissolve
    h "Like... I don't know, I just feel bad looking at it."
    "That's interesting..."
    m talk "Do you get along with your psychiatrist?"
    show h happy with dissolve
    play music "ost/hospital.wav" fadein 6
    h "He's great! He's like a second dad for me ~"
    show h frust with dissolve
    h "...even though I don't remember my first one."
    "...."
    show h neu with dissolve
    m conf "Don't worry about that. I'll do anything I can to help."
    show h laughblush with dissolve
    h "Really? That's so nice of you, [name] ~"
    show h cute with dissolve
    h "You can be like my second mom then!"
    m laugh "Maybe."
    show h smile with dissolve
    m talk "We're out of time for today, though. You should hurry back to your room."
    show h sadsmile with dissolve
    h "Aww..."
    show h sidetalk with dissolve
    h "If I have to..."
    hide h with dissolve
    "He leaves."
    "Despite everything, he seems to act really friendly towards me. I appreciate that a lot."
    stop music fadeout 3
    if sessions == 0:
        $firstpatient = "blue"
    $blueinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen easymeter
    hide screen bluemeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump bluenotes
        "No":
            pass
    jump breaknav
label blue3:
    scene bg mc with dissolve
    "...."
    play music "ost/hospital.wav" fadein 10
    "I've been waiting for Charlie to arrive for the past 15 minutes now."
    "Something must be wrong."
    "I decide to look for him and check if he's alright."
    scene bg offices with dissolve
    m neu "...?"
    "I look around the hallway, but can't see Charlie anywhere."
    "Hmmm..."
    "Maybe he's still in his room..?"
    scene bg central with dissolve
    "...oh."
    stop music fadeout 6
    if easymeter: 
        show screen easymeter 
        show screen bluemeter
    show h full with dissolve
    "I spot him standing by one of the windows."
    "He's staring off into the distance..."
    m talk "Charlie?"
    play music "ost/tension.ogg" fadein 10
    "He ignores me completely. I approach him slowly and lean against the wall next to him."
    h "...."
    menu:
        "Say something":
            $personal+=1
            m fab "You were going to meet me today, do you remember?"
            h "...you?"
            "He looks down at his feet."
            h "I don't... know."
            "He seems to be in a worse condition than last time."
        "Wait":
            $professional+=1
            "I give him some time, hoping he'll talk to me on his own eventually."
            h "...."
    m serious "Is something wrong?"
    "He shakes his head hesitantly, as if he can't quite see me."
    m "Charlie, come with me. We'll get tired standing around like this eventually."
    "He follows me to my office, still not really looking at me."
    play sound "doorclose.ogg" fadein 1
    scene bg mcdesk with dissolve
    show h siden with dissolve
    "I try talking to him... but it doesn't seem much for conversation."
    "I think he's just a little apathetic today - it's nothing particularly troublesome for me, and should pass soon."
    show h bored with dissolve
    m fabtalk "...Charlie?"
    show h frust with dissolve
    stop music fadeout 5
    "I see how it is. Well, I should give him some time."
    "And if he really can't talk to me today, it might be better to send him back to his room."
    show h sad with dissolve
    h "...."
    show h frusttalk with dissolve
    h "...wait."
    show h sad with dissolve
    play music "ost/neutral.wav" fadein 8
    "I freeze, but soon realize he's still not talking to me."
    "He's staring at something in the distance intently."
    "Whenever I see people like that, I'm always curious about what they're seeing."
    "I wish they had some means of capturing it... so I could understand them better."
    "Sometimes words just aren't enough."
    "It's always the biggest struggle of working with patients like Charlie - understanding."
    "I know I'll never really get what he sees or hears, but I'd like to have enough of an understanding of them to be able to analyze them and help him."
    show h sidetalk with dissolve
    h "Umm..."
    show h talk with dissolve
    h "[name]?"
    show h neu with dissolve
    m gasp "Yes?"
    show h sadtalk with dissolve
    h "How did I get here..?"
    show h siden with dissolve
    m talk "I invited you."
    show h gasp with dissolve
    h "...oh."
    show h cute with dissolve
    h "That makes sense."
    show h neu with dissolve
    m neu "I found you in the central hall by the windows."
    show h sadtalk with dissolve
    h "I see..."
    show h sad with dissolve
    "I notice he seems a lot less cheerful than usual."
    show h talk with dissolve
    h "I'm sorry if I'm... a bit confused today."
    show h neu with dissolve
    m conf "It happens sometimes, it's fine."
    show h sidesmile with dissolve
    h "...thank you."
    show h talk with dissolve
    h "I sometimes, uh... lose track of what's happening for a while."
    show h sadtalk with dissolve
    h "This Monday I wasn't exactly... \"myself\" either."
    show h frust with dissolve
    h "I was... more disoriented than usual."
    show h neu with dissolve
    m fab "I noticed."
    show h sadtalk with dissolve
    h "That must've been... a bad first impression... I think some people would assume I'm always like that."
    show h sadsmile with dissolve
    menu:
        "Do you care a lot about what others think about you?":
            $BlueHeart+=1
            show h frust with dissolve
            h "Ummm..."
            show h talk with dissolve
            h "I think so. If I want to make friends here, I need people to like me first."
            show h neu with dissolve
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
        "I assumed that":
            $personal+=1
            show h gasp with dissolve
            h "And you still wanted to see me again so soon?"
            show h neu with dissolve
            m fabtalk "Yeah, why not?"
            show h happy with dissolve
            h "Wow... that's amazing, [name]..."
        "I would never think that":
            $personal+=2
            show h frust with dissolve
            m uncom "I mean... everyone has worse days sometimes."
            show h neu with dissolve
            m smile "I didn't want to judge you based on one session."
            show h laugh with dissolve
            h "Thank you, [name] ~"
    stop music fadeout 6
    show h sidetalk with dissolve
    h "You know... I think the staff here likes me."
    show h kawaii with dissolve
    h "...And it makes me really happy."
    show h sadtalk with dissolve
    h "But it wasn't always this way."
    show h talk with dissolve
    play music "ost/tran.ogg" fadein 6
    h "At first, I didn't know how to act around anybody."
    show h sad with dissolve
    h "...I just tried to stay out of everyone's way."
    show h frusttalk with dissolve
    h "And... I saw the nurses seemed happier around friendly patients."
    show h sidesmile with dissolve
    h "I think I... learned a lot by watching others be nice to each other."
    show h talk with dissolve
    h "I spent a lot of time perfecting that."
    show h sidetalk with dissolve
    h "I just... felt like you should know. I'm not... always like that."
    show h bored with dissolve
    h "Today, I don't really feel like doing anything... it's just one of these days."
    show h talk with dissolve
    h "On days like these I don't really... seem all that nice."
    show h frust with dissolve
    m conf "I get it."
    show h gasp with dissolve
    h "Really?"
    show h neu with dissolve
    m talk "You don't have to act cheerful all the time - you should do whatever you want."
    stop music fadeout 6
    show h sad with dissolve
    h "...."
    m serious "What's wrong?"
    show h sadtalk with dissolve
    h "I don't... know."
    play music "ost/tension.ogg" fadein 6
    show h frusttalk with dissolve
    h "I don't know..."
    show h talk with dissolve
    h "I don't know what I want... how should I know?"
    show h sad with dissolve
    m talk "You really don't know?"
    show h sadtalk with dissolve
    h "I don't... I just... try to do whatever's expected of me. I don't know why."
    show h talk with dissolve
    h "I know that I don't like being alone... But not always."
    show h sidetalk with dissolve
    h "Is that strange, [name]? Should I know these kinds of things about myself?"
    show h bored with dissolve
    stop music fadeout 8
    menu:
        "You should":
            $professional+=1
            show h sad with dissolve
            h "...."
            show h sadtalk with dissolve
            h "...but I don't..."
        "You already do":
            $BlueHeart+=1
            show h neu with dissolve
            m regretsmile "You just forgot them."
            show h siden with dissolve
            m pity "I can help you remember it again."
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
            show h happy with dissolve
            h "That sounds... great, [name] ~!"
        "It doesn't matter":
            $wrong+=1
            h "Really..?"
            h "So... it's fine if I don't know any of that?"
            m conf "If it doesn't bother you, that is."
            h "...You're so smart, [name]!"
    show h neu with dissolve
    play music "ost/hospital.wav" fadein 10
    m fab "Why do you think you want to befriend everyone here?"
    show h sidetalk with dissolve
    h "Umm... I don't know..."
    show h talk with dissolve
    h "I just... don't like people not liking me."
    show h neu with dissolve
    m "I see."
    m talk "You said you observed how other patients act around the staff and tried to mimic it."
    show h talk with dissolve
    h "Yes."
    show h bored with dissolve
    m uncom "Why would you do that? Were you really that worried about people not liking you?"
    show h sidetalk with dissolve
    h "I mean... I guess."
    show h talk with dissolve
    h "I never thought about any reasons for that."
    show h bored with dissolve
    m fabtalk "Do you think there may have been a reason why you're so determined to make friends, but you just don't remember it?"
    show h sidetalk with dissolve
    h "...maybe. I really can't tell."
    show h siden with dissolve
    "I guess that's an assumption for now."
    show h sadtalk with dissolve
    h "Is there... anything wrong with wanting people to like me?"
    show h neu with dissolve
    m shock "No, not at all! I just wanted to ask."
    show h sidetalk with dissolve
    h "...okay."
    show h sidesmile with dissolve
    m fabtalk "Hey, about earlier today..."
    m talk "What happened before I brought you to my office?"
    show h gasp with dissolve
    h "I don't... oh wait, you mean... from my perspective..?"
    show h siden with dissolve
    "I nod."
    show h sidetalk with dissolve
    h "I... remember walking through a forest."
    show h angry with dissolve
    h "I saw a woman there I've only seen once before. Older than you."
    show h bored with dissolve
    m uncom "Did she say anything?"
    show h talk with dissolve
    h "I... wanted to ask her somethings, since she seemed important, but..."
    show h sadtalk with dissolve
    h "She only told me to wait. And that everything will be revealed to me soon."
    show h frust with dissolve
    h "...."
    m serious "What is it?"
    stop music fadeout 6
    show h sidesmile with dissolve
    h "Nothing... I was just wondering if... she wasn't talking about you."
    m gasp "H-Huh?"
    show h talk with dissolve
    h "I mean... maybe I'll learn everything I'm missing now thanks to you."
    play music "ost/neutral.wav" fadein 7
    show h happy with dissolve
    h "You'll help me, right [name]? You can do anything, right [name]?"
    show h cute with dissolve
    menu:
        "Of course I'll help":
            show h talk with dissolve
            h "Then she was right. That... that was a vision."
            show h laugh with dissolve
            h "I'm counting on you, [name]!"
            show h smile with dissolve
        "I'm not sure if it's possible...":
            show h sad with dissolve
            h "...oh."
            show h talk with dissolve
            h "Well... I guess she was only in my head."
            show h sadtalk with dissolve
            h "D-Don't worry, [name] - it's not your fault."
            show h neu with dissolve
        "Only if you try as well":
            $BlueHeart+=1
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
            show h happy with dissolve
            h "I will!"
            show h kawaii with dissolve
            h "Wow, I feel so determined now ~"
            show h smile with dissolve
    "Our time is running out for today."
    m fabtalk "That should be all. We're out of time."
    show h sadsmile with dissolve
    h "Aww... it's because I was late, right?"
    show h neu with dissolve
    m conf "It's fine. I'll see you again soon."
    show h happy with dissolve
    h "Bye ~!"
    scene bg mc with dissolve
    stop music fadeout 3
    "He leaves. He seemed a lot more serious today than he did before."
    "He even said he's not always like this... I guess it's not all that surprising."
    if sessions == 0:
        $firstpatient = "blue"
    $blueinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen easymeter 
    hide screen bluemeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump bluenotes
        "No":
            pass
    jump breaknav
label blue4:
    scene bg mcdesk with dissolve
    show h smile with dissolve
    if easymeter: 
        show screen easymeter 
        show screen bluemeter
    "Charlie is back. This is the fifth time I'm seeing him this week, since I chose to meet him every day."
    "Huh... I guess I must be really invested in helping him."
    play music "ost/neutral.wav" fadein 10
    show h talk with dissolve
    h "Hi."
    show h siden with dissolve
    "Just like yesterday, he seems a little less cheerful than before."
    m uncom "Is something wrong?"
    show h frust with dissolve
    h "...."
    show h sidetalk with dissolve
    h "I've... been thinking..."
    show h talk with dissolve
    h "...About all these things you asked me... that I couldn't answer."
    show h bored with dissolve
    m gasp "Did you remember anything?"
    show h sad with dissolve
    h "...no."
    show h gasp with dissolve
    h "{i}But!"
    show h sidetalk with dissolve
    h "I asked my psychiatrist how I got here - I thought he must know."
    show h siden with dissolve
    m fabtalk "What did he tell you?"
    show h sadtalk with dissolve
    h "He... He said that they found me wandering near the hospital about a year ago."
    show h sad with dissolve
    m gasp "What do you mean, \"wandering\"?"
    show h talk with dissolve
    h "He said I couldn't answer any of their questions then. I wasn't in the state to, I think."
    show h siden with dissolve
    "So how he got here remains a mystery..."
    m fab "Did he say anything else?"
    show h sadtalk with dissolve
    h "Not really."
    show h gasp with dissolve
    h "...Was that helpful?"
    show h neu with dissolve
    m angry "I mean... You should ask yourself that first."
    show h sidetalk with dissolve
    h "...I see."
    show h siden with dissolve
    m talk "Did you not remember that before you asked your psychiatrist?"
    show h frust with dissolve
    "He shakes his head."
    show h frusttalk with dissolve
    h "It was all... blurry."
    show h talk with dissolve
    h "I think I remembered it, but... I wasn't sure if it really happened or not."
    show h bored with dissolve
    m fabtalk "Do you think you remember more things like that?"
    show h sadtalk with dissolve
    h "I have a lot of memories. But... they're confusing."
    show h siden with dissolve
    m talk "So you can't tell which ones are real?"
    show h neu with dissolve
    "He nods."
    show h talk with dissolve
    h "So... I figured it's better to assume none of it happened."
    show h bored with dissolve
    menu:
        "Isn't it better to assume it all happened?":
            $personal+=1
            show h sidetalk with dissolve
            h "...that wouldn't make any sense, I think."
            show h frust with dissolve
            m "So the memories contradict each other?"
            "He nods again."
            show h bored with dissolve
            "That makes is a bit complicated..."
        "What are these memories about?":
            $BlueHeart+=1
            show h sidetalk with dissolve
            h "A lot of different things..."
            show h talk with dissolve
            h "Sometimes they're about some people I don't recognize."
            show h frusttalk with dissolve
            h "Some are, umm... bad."
            show h frust with dissolve
            m "Like?"
            show h sadtalk with dissolve
            h "They aren't a nice thing to talk about, [name]."
            show h frust with dissolve
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
        "What time are they from?":
            $professional+=1
            show h gasp with dissolve
            h "I have some that seem like early childhood."
            show h sidetalk with dissolve
            h "But... most of them don't seem like a very long time ago."
            show h talk with dissolve
            h "I can't really tell."
            show h neu with dissolve
    m fabtalk "And you've had the same psychiatrist for all your time here?"
    show h talk with dissolve
    h "That's what he said. I'm pretty sure I could remember if I had a different one as well."
    show h bored with dissolve
    m talk "So you generally remember your time here?"
    show h sidetalk with dissolve
    h "That's right."
    show h sadsmile with dissolve
    h "I think... I have slightly fuzzy memories of some days I was really... confused..?"
    show h cute with dissolve
    h "But overall, I remember this past year quite well."
    stop music fadeout 7
    "Hmmm..."
    m fab "So there's a point somewhere around a year ago past which you just don't remember anything clearly?"
    show h neu with dissolve
    "He nods vigorously."
    show h talk with dissolve
    h "That's it."
    show h siden with dissolve
    m talk "In that case..."
    play sound "page.ogg" fadein 2
    "I flip through my notes, wondering if I really can be sure of my assumption."
    play music "ost/hospital.wav" fadein 6
    m fabtalk "It's memory loss, isn't it?"
    show h talk with dissolve
    h "Probably."
    show h neu with dissolve
    m talk "For now, let's assume that for some unknown reason you've lost your memories sometime before coming here."
    show h sad with dissolve
    m serious "Still, it's been a year... A normal patient would already remember a lot of things."
    show h sadtalk with dissolve
    h "I'm sorry-"
    show h sad with dissolve
    m scream "No no, it's not your fault!"
    show h frust with dissolve
    stop music fadeout 4
    h "I know I'm not normal, [name]. You don't have to remind me of that."
    show h angry with dissolve
    "Suddenly, he sounds completely serious."
    play music "ost/tension.ogg" fadein 6
    menu:
        "I think you're hiding somethings":
            $wrong+=2
            $professional+=1
            show h gasp with dissolve
            h "Huh?"
            show h talk with dissolve
            h "Hiding... things? From you?"
            show h angrytalk with dissolve
            h "How could I hide something if I don't even know anything myself?"
            show h frust with dissolve
            h "You're supposed to help me, [name]..."
            "Maybe he really doesn't remember anything."
        "I just want to help you":
            $BlueHeart+=1
            $personal+=2
            show h sad with dissolve
            h "...."
            show h sadtalk with dissolve
            h "I'm sorry if that sounded harsh..."
            show h cute with dissolve
            h "I know you're trying your best, [name]."
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
        "I didn't mean to offend you":
            $personal+=1
            show h siden with dissolve
            h "I know, I know..."
    show h neu with dissolve
    m fabtalk "Why do you think you can't remember anything?"
    show h frust with dissolve
    stop music fadeout 6
    h "...."
    show h talk with dissolve
    h "I mean... maybe... some of these memories I have are real..."
    show h sadtalk with dissolve
    h "But I have no way of knowing what's real and what isn't."
    show h bored with dissolve
    play music "ost/hospital.wav" fadein 6
    m serious "Does your illness have anything to do with that?"
    show h neu with dissolve
    "He nods slowly."
    show h talk with dissolve
    h "It's possible."
    show h sadtalk with dissolve
    h "Maybe if I were... \"normal\", I would be able to differenciate memories from dreams and my own imagination."
    show h sadsmile with dissolve
    m uncom "I'm sorry for implying you're not normal."
    show h laugh with dissolve
    h "It's fine, it's fine ~"
    show h cute with dissolve
    "His laughter sounds somewhat distant."
    m regret "...."
    "I decide to change the topic."
    show h smile with dissolve
    m talk "You mentioned being close with your psychiatrist once."
    show h talk with dissolve
    h "I did."
    show h smile with dissolve
    m gasp "Have you had more than one psychologist here before me?"
    show h neu with dissolve
    "He nods hesitantly."
    m fab "So your psychiatrist is the person you've known for the longest time out of the staff."
    show h cute with dissolve
    h "That's right."
    stop music fadeout 5
    "Maybe I should talk to his psychiatrist sometime... He might know things about Charlie that I don't."
    show h neu with dissolve
    h "...."
    show h laugh with dissolve
    play music "ost/sunny.wav" fadein 6
    h "Don't worry, [name], I'm sure you can do as well as him someday ~"
    show h kawaii with dissolve
    "I wasn't thinking about that..."
    m talk "What do you mean?"
    show h happy with dissolve
    h "He's great, he really is!"
    show h smile with dissolve
    m fabtalk "Why is that?"
    show h sidesmile with dissolve
    h "I don't know... He's just so nice to me ~"
    show h talk with dissolve
    h "He showed me around when I first got here, explained a lot of things to me..."
    show h sadsmile with dissolve
    h "If it wasn't for him I would really be lost here..."
    show h gasp with dissolve
    h "I want to get a job once I'm out of here - then, I could help people just like him ~!"
    show h smile with dissolve
    "That's... admirable, in a way. I smile at him."
    menu:
        "I'm sure you'll do great":
            $BlueHeart+=1
            show h gasp with dissolve
            h "You think so..?"
            show h laughblush with dissolve
            h "Thank you, thank you ~"
            show drk with Dissolve(0.75)
            show b 1 with dissolve
            show b 2 with Dissolve(1.0)
            $renpy.pause(0.75, hard = True)
            hide b with dissolve
            hide drk with dissolve
        "I help people too":
            $personal+=1
            show h sidetalk with dissolve
            h "You're right..."
            show h sad with dissolve
            h "But..."
            show h smile with dissolve
            h "You're different. I don't know how."
            show h laughblush with dissolve
            h "...But you're also great! In your own way!"
        "It would take a lot of work":
            $professional+=1
            show h talk with dissolve
            h "I know."
            show h kawaii with dissolve
            h "But if I really try, I can do it, right?"
    if BlueHeart>14:
        stop music fadeout 3
        show h siden with dissolve
        h "...."
        "He falls silent suddenly."
        play music "ost/tension.ogg" fadein 6
        show h neu with dissolve
        "He's looking in my direction, but not really at me."
        "Again."
        "I should get used to this..."
        show h bored with dissolve
        "I wait, but he's silent for a while."
        menu:
            "Hello?":
                show h neu with dissolve
                "He blinks quickly."
                stop music fadeout 5
                show h gasp with dissolve
                h "H-Huh?"
                show h talk with dissolve
                h "Oh... It's you..."
                show h sadtalk with dissolve
                h "I'm sorry about that..."
                show h sad with dissolve
                m serious "Are you okay?"
                show h neu with dissolve
                play music "ost/neutral.wav" fadein 7
                "He nods."
                show h sadsmile with dissolve
                h "I just got a little... confused."
                m conf "Sure thing. It's fine, really."
            "{color=#5185ff}Wait":
                show h bored with dissolve
                h "...."
                "He's staring at me intently."
                show h talk with dissolve
                h "You..?"
                show h neu with dissolve
                "It's clear he's not talking to me right now."
                "I think waiting was the right choice - I might get to witness something interesting and ask him about it later."
                show h siden with dissolve
                "...."
                show h frust with dissolve
                "...."
                show h sidetalk with dissolve
                h "What? N-No."
                show h tsun with dissolve
                h "Ummm..."
                show h sad with dissolve
                h "...."
                hide h with dissolve
                "He crosses his arms on my desk and his head falls onto them."
                "I can't see his face."
                "Now might be the right time to intervene."
                menu:
                    "Talk to him":
                        m "Hey, Charlie..."
                        "I lean in a bit, unsure of how he feels and if I should be helping him right now."
                        stop music fadeout 4
                    "Touch his shoulder":
                        $BlueHeart+=2
                        show drk with Dissolve(0.75)
                        show b 1 with dissolve
                        show b 2 with Dissolve(1.0)
                        $renpy.pause(0.75, hard = True)
                        hide b with dissolve
                        hide drk with dissolve
                        "I carefully lay my hand on his shoulder."
                        m "Charlie?"
                        stop music fadeout 4
                        show h gasp with vpunch
                        "He pretty much jumps up and looks at me, eyes wide."
                        "It takes him a moment to regain a neutral expression."
                show h neu with dissolve
                h "Oh..."
                show h sidetalk with dissolve
                h "It's you."
                show h frust with dissolve
                play music "ost/hospital.wav" fadein 5
                h "Ummm..."
                show h sadsmile with dissolve
                h "I'm sorry about that."
                show h sidetalk with dissolve
                h "I just... saw someone."
                stop music fadeout 2
                show h neu with dissolve
                m gasp "Who was it?"
                show h frust with dissolve
                play music "ost/tension.ogg" fadein 6
                h "You."
                "Huh?"
                show h talk with dissolve
                h "I... mean..."
                show h sidetalk with dissolve
                h "I saw you as that girl I mentioned one time. The one in a black dress."
                show h bored with dissolve
                m fabtalk "She was here?"
                show h sidetalk with dissolve
                h "{i}You{/i} were her."
                show h sadtalk with dissolve
                h "And... everything went... kind of... dark."
                show h talk with dissolve
                h "The window was obstructed by trees."
                show h sadtalk with dissolve
                h "Trees coming out of the walls. It felt really... cold."
                show h sad with dissolve
                m angry "I... see."
                show h gasp with dissolve
                h "Does that sound strange to you?"
                show h siden with dissolve
                m uncom "Umm... as a psychologist, no."
                show h sadsmile with dissolve
                h "And... as a person?"
                show h neu with dissolve
                m talk "...A little bit. But go on."
                m fab "Did she do anything?"
                show h talk with dissolve
                h "She, um... stood up from your chair and walked up to me."
                show h siden with dissolve
                m gasp "And?"
                show h frusttalk with dissolve
                h "She... said something... I'd rather not repeat."
                show h frust with dissolve
                m "Huh? Why is that?"
                show h angrytalk with dissolve
                h "It was about you, [name]."
                stop music fadeout 5
                show h sad with dissolve
                "The fact that his delusions start to concern me is noteworthy, definitely."
                "What could that girl have said that caused someone like Charlie not to want to tell me about it?"
                "I guess I shouldn't pressure him..."
        play music "ost/neutral.wav" fadein 6
        show h sidetalk with dissolve
        h "Umm..."
        show h talk with dissolve
        h "I think I should get going now."
        show h smile with dissolve
        "He gets up to leave and I follow him to the door."
        stop music fadeout 3
        show h sidetalk with dissolve
        h "Oh, and before I leave..."
        show h kawaii with dissolve
        h "Good luck with your boss. I'm sure you'll do great ~"
        m talk "Thank-"
        play music "ost/tension.ogg" fadein 5
        m fab "Wait."
        show h neu with dissolve
        m gasp "I didn't tell you I was going to meet my boss after work."
        show h gasp with dissolve
        h "You... You didn't?"
        show h sidesmile with dissolve
        h "I was sure I heard you say that..."
        show h laugh with dissolve
        "He laughs."
        show h sadsmile with dissolve
        h "Sorry, my memory is quite blurry."
        stop music fadeout 3
        show h cute with dissolve
        h "I better go now. Good luck ~"
        play sound "doorclose.ogg" fadein 1
        scene bg mc with dissolve
        "What..?"
    else:
        stop music fadeout 4
        show h neu with dissolve
        h "...."
        "I remember Dr. Sharpe told me to meet him after work today."
        play music "ost/neutral.wav" fadein 6
        m talk "My boss asked me to see him after work."
        show h talk with dissolve
        h "What's it about?"
        show h smile with dissolve
        m serious "He, um... said he'd judge my progress with all of you and decide if I'm fit to work here."
        show h laugh with dissolve
        h "Ooh, I forgot it's your first week here..."
        show h smile with dissolve
        h "Well, good luck ~ I should probably be going now."
        scene bg mc with dissolve
        stop music fadeout 3
        "He leaves my office with a smile."
    if sessions == 0:
        $firstpatient = "blue"
    $blueinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen easymeter 
    hide screen bluemeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump bluenotes
        "No":
            pass
    jump breaknav
    
### TOWER NAVIGATION ###########################
################################################
label purpleintro:
    "Dissociative identity disorder, so multiple personalities... His file says he has three of them."
    "I wonder which ones I'll meet today."
    scene bg mcdesk with dissolve
    $purpleintro = 1
    play sound "doorclose.ogg" fadein 1
    play music "ost/neutral.wav" fadein 10
    "{color=#cb76f9}A man around my age{/color} enters the office and closes the door behind him."
    m talk "Tom Richards? Please, take a seat."
    if easymeter: 
        show screen easymeter
        show screen purplemeter
    show t neutral with dissolve
    "He looks at me with a hint of mistrust, but comes closer to sit by the other side of my desk."
    show t talk with dissolve
    t "So you're the new psychologist?"
    show t neutral with dissolve
    m flirt "Yes. I'm [name] Hart."
    show t neu with dissolve
    "A moment of slightly awkward silence is enough to urge me to say something."
    menu:
        "How are you today?":
            show t angrytalk with dissolve
            t "Why would I tell you that?"
            show t frusttalk with dissolve
            stop music fadeout 4
            t "Like you care..."
            show t frust with dissolve
            m neutral "I do."
        "You have three personalities?":
            $wrong +=1
            show t angrytalk with dissolve
            t "How should I know? That's what they told me."
            show t angry with dissolve
            stop music fadeout 4
            m fabtalk "I was only making sure."
        "Tell me something about yourself":
            $personal += 1
            show t angrytalk with dissolve
            t "What are you trying to do?"
            show t angry with dissolve
            m uncom "I won't be able to help you if you don't tell me anything."
            stop music fadeout 3
            show t angrytalk with dissolve
            t "\"Help me\"?"
    show t angry with dissolve
    t "Listen."
    play music "ost/tension.ogg" fadein 5
    show t angrytalk with dissolve
    t "I'm not the one who needs to be here."
    t "{color=#cb76f9}There is nothing wrong with me."
    show t frusttalk with dissolve
    t "Why do you doctors never understand that...?"
    show t frust with dissolve
    "His behavior feels odd to me - what have I done to anger him so much?"
    "Regardless, I stay calm."
    show t angry with dissolve
    m angrytalk "You wouldn't be here if there was nothing wrong with you."
    show t trigger with dissolve
    t "It's not about me, it's them who are the problem!"
    show t angrytalk with dissolve
    t "{color=#cb76f9}The other ones-"
    t "They ruined my life and now I'm told by all of you that {color=#cb76f9}THEY{/color} need help?"
    show t angry with dissolve
    t "They don't need shit."
    show t angrytalk with dissolve
    t "They're {color=#cb76f9}useless and wrong{/color}. Why would they need help?"
    menu:
        "Both you and they need my help":
            $PurpleHeart += 1
            $personal += 1
            stop music fadeout 6
            show t angry with dissolve
            m fab "My goal is to help all three of you."
            m angrytalk "And I don't plan to be subjective."
            show t pa with dissolve
            show drk with Dissolve(0.75)
            show p 2 with dissolve
            show p 3 with Dissolve(0.55)
            $renpy.pause(0.5, hard = True)
            hide p with Dissolve(0.7)
            hide drk with dissolve
            show t angrytalk with dissolve
            t "How can you say that?! {color=#cb76f9}I was the first one{/color}, they're just the illness..."
        "You aren't here because of me":
            $professional += 1
            show t angry with dissolve
            m neutral "I am not responsible for you being here, so I would appreciate it if you stopped accusing me."
            show t frust with dissolve
            "I can see him growing more tense, but he doesn't say a word."
        "Stop accusing me already":
            $wrong += 1
            show t frust with dissolve
            m o angrytalk "What have I done to you?"
            m o angry "You're blaming the wrong person here."
            show t frusttalk with dissolve
            t "The problem is, you're the only one I can blame."
            show t neu with dissolve
            t "So that's just what I'll do."
    show t angry with dissolve
    m angry "You need to calm down. We won't be able to have a normal conversation if you don't."
    m fabtalk "If you're trying to prove that you're perfectly sane, be rational about this."
    show t trigger with dissolve
    t "And now you're blaming me?"
    show t angry with dissolve
    "He glares at me suddenly."
    play music "ost/tension.ogg" fadein 6
    show t angrytalk with dissolve
    t "Why do you even work here...? Is it just the money?"
    show t angry with dissolve
    stop music fadeout 5
    "I'm speechless. Does he really think that's why I'm here, trying to help him?"
    m talk "I only work here because I want to help people like you."
    show t angrytalk with dissolve
    t "\"Like me\"? What are \"people like me\" like?"
    stop music fadeout 4
    menu:
        "Stubborn":
            show t angry with dissolve
            m angrytalk "You're stubborn - I'm here to convince you that you need my help."
        "Hurt":
            $personal += 1
            $PurpleHeart += 1
            show t angry with dissolve
            play music "ost/tran.ogg" fadein 5
            m neu "I believe people like you are simply hurt."
            show t neutral with dissolve
            m serious "Maybe fate wasn't too kind to you?"
            show drk with Dissolve(0.75)
            show p 2 with dissolve
            show p 3 with Dissolve(0.55)
            $renpy.pause(0.5, hard = True)
            hide p with Dissolve(0.7)
            hide drk with dissolve
            show t frust with dissolve
            "He looks away from me and I can tell I was right."
            show t hurt with dissolve
            "There's a glimpse of pain in his eyes for just a moment."
            stop music fadeout 3
            "It was only a guess... Either way, I think I just learned something important."
        "Troubled":
            $professional += 1
            show t angry with dissolve
            m angrytalk "Everyone here is facing some problems - you need to realize that you're no exception."
        "Annoying":
            $wrong += 1
            show t angry with dissolve
            m angry "Why are you so angry all the time?"
            show t pa with dissolve
            m angrytalk "It's getting frustrating..."
    play music "ost/tension.ogg" fadein 5
    show t angrytalk with dissolve
    t "Shut up!"
    show t angry with dissolve
    "I freeze, shocked by his sudden outburst."
    show t madtalk with dissolve
    t "I'm done with all this- This is some sick joke!"
    show t angrytalk with dissolve
    t "Hospitals? Doctors, therapy? Who are you taking me for?"
    show t angrytalk with dissolve
    t "Look at me - do I deserve to be treated like some psychopath?"
    menu:
        "Be quiet.":
            stop music fadeout 2
            $professional += 1
            stop music fadeout 5
            show t angry with dissolve
            m neu "Please lower your voice. Yelling at me won't solve anything."
            pause 1 
            play music "ost/hospital.wav" fadein 5
        "You're here, so you do":
            $personal += 1
            stop music fadeout 4
            show t angry with dissolve
            m fabtalk "Like it or not, you are ill - there's no denying that."
            play music "ost/hospital.wav" fadein 5
            show t frusttalk with dissolve
            t "{color=#cb76f9}\"Ill\"{/color}... It sounds so odd..."
            show t frust with dissolve
            m uncom "It will take time, but you'll be able to leave this place."
            m angry "Only if you let me help."
            show t regrettalk with dissolve
            t "You don't really... mean it..."
        "I'm sorry...":
            $wrong += 1
            show t angry with dissolve
            m serious "I shouldn't have made you angry..."
            show t trigger with dissolve
            t "Are you serious right now?"
            show t angrytalk with dissolve
            t "What is this, guilt tripping?"
            m shock "No, I didn't mean to..."
            stop music fadeout 4
            show t angry with dissolve
            t "Just stop it already. You aren't helping anyone right now."
            "He's right. I should just shut up..."
            pause 1 
            play music "ost/hospital.wav" fadein 5
    show t siden with dissolve
    "A while passed in silence."
    "I wonder if Tom is rethinking what just happened."
    "I look at the nearest clock."
    "If I want to meet all my patients before I finish work today, I should end this first session soon."
    m talk "We're running out of time. Thank you for talking to me."
    show t neutral with dissolve
    t "...."
    "He doesn't seem to be listening to me."
    m fabtalk "I'll see you again soon."
    show t talk with dissolve
    t "You're not planning to help me after all, right?"
    show t neu with dissolve
    m serious "What do you mean?"
    show t angrytalk with dissolve
    t "I don't belong here, no matter what you tell me. I'm better than all these delusional madmen."
    show t angry with dissolve
    m angry "I think just saying that makes you worse."
    show t frusttalk with dissolve
    t "So that's how it is... You really are all the same."
    show t frust with dissolve
    t "It's hopeless then."
    play sound "doorclose.ogg" fadein 1
    scene bg mc with dissolve
    "He leaves my office and I close the door behind him, exhaling loudly."
    "To be honest, I was definitely unprepared to be yelled at by a patient."
    "What a strange case... Sane for the most part, but still trapped here..."
    "I would feel sorry for him if he wasn't so angry from the start."
    "He overreacted, but on his own he doesn't seem particularly \"troubled\"."
    "I decide to assume his two alters are as sane as him."
    stop music fadeout 4
    "I hope I get to meet them soon..."
    $sessions += 1
    show drk with dissolve
    $persistent.Tom=True
    show screen notify("{size=24} Your Characters Info screen has been updated!")
    hide screen easymeter
    hide screen purplemeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump purplenotes
        "No":
            pass
    jump breaknav
label purple:
if day < 6 and month==1:
    if purpleinteract == 0:
        jump purple1
    elif purpleinteract == 1:
        jump purple2
    elif purpleinteract == 2:
        jump purple3
    elif purpleinteract == 3:
        jump purple4
else:
    jump purplesession
    
label purple1:
    scene bg mcdesk with dissolve
    play music "ost/neutral.wav" fadein 10
    show t neutral with dissolve
    if easymeter: 
        show screen easymeter
        show screen purplemeter
    "Tom takes a seat in front of me and looks at me in silence for a moment."
    "He doesn't seem as tense as the last time I saw him."
    if sessions == 0 and day == 2:
        show t talk with dissolve
        t "When you said yesterday that we'll meet soon, I didn't know you meant this soon."
        show t neu with dissolve
        m fabtalk "Is that a problem that I chose to talk to you first?"
        show t talk with dissolve
        t "No. But you're treating me like the one who needs your help the most."
        show t frusttalk with dissolve
        t "I don't know who your other patients are, but surely {color=#cb76f9}they're worse than me{/color}."
        show t neutral with dissolve
        m neu "I guess I just wanted to see you again today."
        m talk "To go over what happened yesterday..."
        "The truth is, I felt the most comfortable around him after yesterday, even if he was a bit aggressive."
    elif day > 3 or day == 3 and sessions == 1:
        show t frusttalk with dissolve
        t "You really took your time after Monday..."
        show t neutral with dissolve
        m gasp "What do you mean?"
        show t talk with dissolve
        t "You probably had other patients to get through."
        show t neutral with dissolve
        "The truth is, after he yelled at me last time, I wasn't too eager to interact with him again."
        m serious "I wanted to mention what happened last time..."
    else:
        m uncom "How should I start..? I think it's best to adress the main issue right away."
        m talk "I wanted to mention what happened the last time we met."
    show t talk with dissolve
    t "Before you start talking..."
    show t neutral with dissolve
    m talk "Yes?"
    show t frusttalk with dissolve
    t "{color=#cb76f9}I had a rough day last time{/color}... I didn't really mean to blame you like I did."
    show t angry with dissolve
    m conf "I understand."
    show t neutral with dissolve
    m talk "Can I ask you some questions today?"
    "He nods, but I can tell he's not too eager to talk about himself."
    menu:
        "How long have you been here for?":
            show drk with Dissolve(0.75)
            show p 2 with dissolve
            show p 3 with Dissolve(0.55)
            $renpy.pause(0.5, hard = True)
            hide p with Dissolve(0.7)
            hide drk with dissolve
            $PurpleHeart += 1
            show t talk with dissolve
            t "Only a {color=#cb76f9}month{/color} so far."
            show t frusttalk with dissolve
            t "But the place is driving me crazy... Literally in a way."
            show t neutral with dissolve
        "How old are your alters?":
            show t talk with dissolve
            t "How would I know?"
            show t sidetalk with dissolve
            t "Are you saying I talk to them or something?"
            show t talk with dissolve
            t "I'm 29 and they're probably around that as well."
            show t neutral with dissolve
            "No new information there."
    menu:
        "What's your occupation?":
            $professional += 1
            show t talk with dissolve
            t "I'm not sure if you would really understand..."
            t "The point is, I set up a company a few years ago."
            show t sidetalk with dissolve
            t "Everything was going well until..."
            show t frust with dissolve
            "He pauses for a moment."
            show t frusttalk with dissolve
            t "...{i}They{/i} ruined it."
            show t frust with dissolve
            "I can sense he doesn't want to talk about the details."
        "What do you do in your free time?":
            $personal += 1
            show t talk with dissolve
            t "Back when I had a job, I didn't get much time for myself."
            show t sidetalk with dissolve
            t "And now...?"
            show t angry with dissolve
            t "The days are boring and monotone here. I tried to get something done at first, but I can't focus at all since I came here..."
            show t talk with dissolve
            t "So most of the time I sleep or try to sleep at least."
            show t sidetalk with dissolve
            t "I never had the time to develop any hobbies in particular, so now that I don't have much to do, I just waste a lot of time."
            show t siden with dissolve
    m gasp "Where did you live before you were admitted here?"
    show t talk with dissolve
    t "{color=#cb76f9}The city{/color}. I moved when I first started looking for work."
    stop music fadeout 6
    t "Everything is easier there - finding a job especially."
    show t sidetalk with dissolve
    t "And... there's so many people that nobody really recognizes you or cares."
    show t talk with dissolve
    play music "ost/hospital.wav" fadein 5
    t "You know, I used to live {color=#cb76f9}here{/color}. I was born here actually."
    show t hurttalk with dissolve
    t "But, uh... I had to move out when I got older... People here..."
    show t angry with dissolve
    "His expression changes suddenly."
    show t angrytalk with dissolve
    t "I wanted to {color=#cb76f9}start over{/color}, is that so unusual?!"
    show t angry with dissolve
    m talk "Not at all."
    stop music fadeout 5
    "I think the people around town might know somethings about Tom's past that I don't..."
    show t neutral with dissolve
    "But I shouldn't start an investigation out of nowhere - he's likely to tell me everything I need to know eventually."
    play music "ost/tension.ogg" fadein 2
    show t angrytalk with dissolve
    t "Hey, what are you doing?" 
    m shock "What-?"
    show t trigger with dissolve
    "I realize I'm resting my elbows on the desk, leaning in slightly while listening to him."
    "It's nothing but a habit - I like to be close to the people I talk to."
    "But for whatever reason this seems to have made him uncomfortable."
    show t madtalk with dissolve
    t "{color=#ffffff}{i}Get. Away from me.{/i} {b}Right now.{/b}"
    show t mad with dissolve
    "His voice is shaky, but his tone is growing more and more tense."
    show t angry with dissolve
    "He's glaring at me coldly."
    "I fall back into my chair and remove my hands from the desk."
    "I look at him, carefully."
    if personal > professional and professional > wrong and PurpleHeart > 4:
        "His blue eye seems to express something slightly different than his brown one."
        "It looks anxious, more scared than angry."
        "I just want to help him, but all I can do is wait for him to say something."
    else:
        "I didn't mean to startle him with my behavior."
    show t neutral with dissolve
    t "...."
    show t frust with dissolve
    "He looks away from me with a frustrated expression on his face."
    stop music fadeout 5
    menu:
        "Are you okay?":
            $empathy += 1
            show t angrytalk with dissolve
            t "Do I look okay?"
            show t neutral with dissolve
        "What did I do wrong?":
            $personal += 1
            show t siden with dissolve
            $PurpleHeart += 1
            show drk with Dissolve(0.75)
            show p 2 with dissolve
            show p 3 with Dissolve(0.55)
            $renpy.pause(0.5, hard = True)
            hide p with Dissolve(0.7)
            hide drk with dissolve
            show t regrettalk with dissolve
            t "Look, I know you didn't mean to..."
        "Talk to me":
            $wrong += 1
            show t angry with dissolve
            "He gives me a hateful glare before speaking up."
            show t frusttalk with dissolve
            t "You're a pain..."
    show t talk with dissolve
    t "Just {color=#cb76f9}don't ever do that again."
    show t angrytalk with dissolve
    t "Is that clear?"
    show t angry with dissolve
    play music "ost/neutral.wav" fadein 8
    menu:
        "Of course":
            $professional += 1
            $PurpleHeart += 1
            m serious "It won't happen again, I promise."
            show t talk with dissolve
            t "Good..."
            show t neutral with dissolve
            show drk with Dissolve(0.75)
            show p 2 with dissolve
            show p 3 with Dissolve(0.55)
            $renpy.pause(0.5, hard = True)
            hide p with Dissolve(0.7)
            hide drk with dissolve
            if PurpleHeart > 3:
                show t neu with dissolve
                t "Thank you."
        "I guess":
            $wrong += 1
            show t neutral with dissolve
            m serious "If you say so..."
            show t angrytalk with dissolve
            t "I mean it. Stay away from me from now on."
        "Why does it bother you?":
            t "I already made it clear, {color=#cb76f9}I don't want to talk about it."
    show t siden with dissolve
    "He looks at the nearby clock."
    show t talk with dissolve
    t "It's late..."
    show t neutral with dissolve
    m serious "Before you go, can I ask you something?"
    show t neu with dissolve
    "He has a questioning look on his face with a hint of uneasiness."
    show t frusttalk with dissolve
    t "Ask if you have to."
    show t neutral with dissolve
    if personal > professional + 10:
        m serious "I'm sorry for making you angry last time."
        show t neu with dissolve
        m "It was my first day working here, I didn't know what to expect..."
        "He stops me before I can go any further."
        show t talk with dissolve
        t "You're really worried about that?"
        show t sidetalk with dissolve
        t "What's done is done - I don't really care about these sessions as long as you're doing something about {i}Them."
        show t neutral with dissolve
        t "Don't make a fuss over it. I wasn't exactly myself then either."
    else:
        m talk "How often do you switch?"
        show t angry with dissolve
        m fabtalk "I guess what I'm asking is - when can I expect to meet the others?"
        show t hurttalk with dissolve
        t "Meet... them?"
        show t talk with dissolve
        t "In person...?"
        show t regret with dissolve
        m neutral "Yes."
        show t talk with dissolve
        t "I don't know... sometimes it takes weeks and sometimes just days."
        show t neutral with dissolve
        t "I never switch when I'm conscious nowadays, so it only happens overnight."
        show t talk with dissolve
        t "It largely depends on stress, I think."
        show t hurttalk with dissolve
        t "So try not to make me nervous, please... I can't guarantee you'll like the results."
        show t hurt with dissolve
    m talk "I think it's time to end today's session."
    show t neu with dissolve
    m conf "Thank you for being honest and answering my questions."
    show t talk with dissolve
    t "Goodbye, Hart."
    show t neutral with dissolve
    m happy "Have a nice day~"
    play sound "doorclose.ogg" fadein 1
    scene bg mc with dissolve
    "He leaves my office and I feel relieved that we could have a mostly normal conversation."
    "It went a lot smoother than I thought it would after last time."
    "I noted how reluctant he seems to be when talking about his past - I wonder if whatever happened to him is the origin of his illness..."
    "It's possible."
    stop music fadeout 4
    "I decide to leave the thinking for another time."
    if sessions == 0:
        $firstpatient = "purple"
    $purpleinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen easymeter
    hide screen purplemeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump purplenotes
        "No":
            pass
    jump breaknav
label purple2:
    scene bg mcdesk with dissolve
    show t hurt with dissolve
    "Tom seems to be a bit uneasy today."
    "I wonder if anything happened to him since we talked last time..."
    m talk "Take a seat, Tom."
    if easymeter: 
        show screen easymeter
        show screen purplemeter
    show t neutral with dissolve
    "He glares at me suddenly."
    show t frusttalk with dissolve
    play music "ost/neutral.wav" fadein 8
    t "Let's get this over with already..."
    show t frust with dissolve
    "I don't think he's too eager to elaborate on anything right now..."
    show t neutral with dissolve
    "I was curious about his past last time, so maybe I should ask anyway."
    menu:
        "Tell me more about your work":
            $professional += 1
            show t sidetalk with dissolve
            t "I don't think you mean the technical details..."
            show t talk with dissolve
            t "After I graduated, I wanted to start working as quickly as possible."
            t "It wasn't easy for the first year or so, but I got used to it."
            show t neutral with dissolve
            t "I had a lot of work, actually... but that meant I could occupy myself with something most of the time."
            show t hurttalk with dissolve
            t "And... my job mostly didn't require working with other people."
            show t talk with dissolve
            t "{color=#cb76f9}I was sick of that{/color} after school..."
        "How was your life at school?":
            $personal +=1
            show t gasp with dissolve
            t "Oh..."
            show t angry with dissolve
            t "{color=#cb76f9}I hated it{/color}, to be honest."
            show t neutral with dissolve
            m gasp "Why's that?"
            show t talk with dissolve
            t "{color=#cb76f9}I didn't have the time to study{/color} until the end of middle school, so adjusting to highschool was difficult."
            show t frusttalk with dissolve
            t "Not to mention other students... Most of the time all I wanted was to get out of there."
            show t angrytalk with dissolve
            t "It's not that I was bullied or anything like that, it was just... strange."
            show t neutral with dissolve
            "I wonder what happened to distract him from school earlier on..."
            "I'll have to ask him about that later."
            "He mentioned not getting along with his fellow students... that might be a new lead."
    "He generally seems to dislike being in the company of other people."
    "The way he interacts with me could support this."
    "It's worth knowing, but doesn't directly point to the source of his problem."
    "I'll need him to be more specific."
    "If I ask the right questions, I might learn something valuable."
    menu:
        "Did you never like the company of other people?":
            $professional += 1
            show t frusttalk with dissolve
            t "No... I mean..."
            show t talk with dissolve
            t "It's, uhh... complicated."
            show t neutral with dissolve
            m flirt "Take your time, I'm all ears."
            show t siden with dissolve
            "He's silent for a moment."
            show t hurttalk with dissolve
            t "I feel like people don't really... {color=#cb76f9}understand{/color} why I act the way I do."
            show t frust with dissolve
            m angrytalk "And have you ever tried to explain it to them?"
            show t gasp with dissolve
            t "What-? Why would I? They don't care either way."
            show t sidetalk with dissolve
            t "Besides..."
            show t frusttalk with dissolve
            t "{color=#cb76f9}They don't need to know{/color} all of that..."
            show t neutral with dissolve
            m serious "And have you ever had anyone you trusted enough to tell them about it?"
            show t siden with dissolve
            t "...No."
            show t sidetalk with dissolve
            t "I don't really... I don't usually {i}trust{/i} people like that."
            show t angry with dissolve
            "There it is."
            m uncom "I see."
        "Have you ever been in a romantic relationship?":
            $personal +=1
            show t gasp with dissolve
            "He freezes at my question."
            "I think this may have been the right lead."
            show t talk with dissolve
            t "A... romantic relationship?"
            show t hurttalk with dissolve
            t "No, {color=#cb76f9}I've never{/color}... umm..."
            show t hurt with dissolve
            "He looks away from me."
            "That's about all I needed to know..."
            show t neutral with dissolve
            m talk "And why is that?"
            show t sidetalk with dissolve
            t "I don't really... like the idea of interacting with someone in such a way."
            show t siden with dissolve
            m serious "I see."
            show t frusttalk with dissolve
            t "And besides... {color=#cb76f9}I wouldn't trust anyone enough."
            show t frust with dissolve
            "I nod quickly and note his last response."
    show t neutral with dissolve
    "This is getting a bit clearer."
    "While I still don't know the exact cause, he seems to not enjoy the company of other people out of lack of trust."
    "My previous theory comes back to me."
    "Maybe he really has dealt with some difficult experiences in the past... ones that made him wary of other people."
    "He doesn't seem very eager to mention his past, though."
    stop music fadeout 6
    "I should try to find a way to get to the source of his problems."
    menu:
        "What is your family like?":
            $wrong += 1
            show t hurttalk with dissolve
            t "Uhhh..."
            show t regret with dissolve
            "He's silent."
            "That may have been a bit blunt."
            play music "ost/hospital.wav" fadein 8
            show t talk with dissolve
            t "{color=#cb76f9}I was raised by my mother."
            show t angrytalk with dissolve
            t "But I don't maintain contact with any family members anymore."
            show t neutral with dissolve
            "Oh. That seems relevant."
        "Has anyone you know suffered from a mental illness?":
            $PurpleHeart+=1
            show t hurttalk with dissolve
            play music "ost/tran.ogg" fadein 8
            t "{color=#cb76f9}My mother..."
            show t hurt with dissolve
            "He mutters the words to the point that I'm not sure what I heard."
            show t regrettalk with dissolve
            t "I think she may have been... {color=#cb76f9}ill{/color}."
            show t regret with dissolve
            show drk with Dissolve(0.75)
            show p 2 with dissolve
            show p 3 with Dissolve(0.55)
            $renpy.pause(0.5, hard = True)
            hide p with Dissolve(0.7)
            hide drk with dissolve
            "He's not looking at me. I don't think asking about it further now is a good idea."
    "I look at him more closely..."
    "I'm learning a lot about him today."
    "Let's keep this up."
    "Suddenly, I remember our last session."
    "He got angry with me after I unintentionally moved closer to him."
    show t neutral with dissolve
    "I ask him about that."
    m serious  "Is there any reason why you acted that way?"
    show t hurttalk with dissolve
    t "...."
    show t hurt with dissolve
    "His expression is tense... I don't think he'll tell me."
    "I should use what I learned today... what is the actual reason behind his previous behavior?"
    stop music fadeout 6
    "If I want to be thorough, I should dig deeper... What happened to him?"
    menu:
        "Is it about trust?":
            "It seems like a reasonable guess."
            show t neutral with dissolve
            t "I suppose..."
            show t talk with dissolve
            play music "ost/neutral.wav" fadein 6
            t "You could say that I have... difficulty trusting people to be close to me."
            show t frusttalk with dissolve
            t "...{color=#cb76f9}Literally and methaphorically{/color}, I mean."
            show t neutral with dissolve
            "I nod."
            m neu "I understand."
            m serious "It's difficult to open up to other people without stepping out of your comfort zone sometimes."
            show t talk with dissolve
            t "I guess."
        "Is it about your mother?":
            $PurpleHeart +=1
            show t gasp with dissolve
            t "How..."
            show t talk with dissolve
            t "...How did you guess that?"
            show t neutral with dissolve
            show drk with Dissolve(0.75)
            show p 2 with dissolve
            show p 3 with Dissolve(0.55)
            $renpy.pause(0.5, hard = True)
            hide p with Dissolve(0.7)
            hide drk with dissolve
            play music "ost/neutral.wav" fadein 6
            m talk "The way you mentioned her before sounded odd to me."
            show t neutral with dissolve
            t "If that's so..."
            show t smirk with dissolve
            t "I think I underestimated you, Hart."
            show t smile with dissolve
            t "Lying is out of question with you."
            "I smile, but soon realize he just tried to distract me."
            "I wasn't done asking... but I suppose I got the most important part."
            show t neutral with dissolve
            "His mother... that seems important."
        "Is it about your personal life?":
            $wrong += 1
            show t trigger with dissolve
            t "What?"
            show t angry with dissolve
            t "I've never been in a relationship."
            show t angrytalk with dissolve
            t "I thought you could tell-"
            show t frust with dissolve
            "He's getting anxious."
            show t angrytalk with dissolve
            t "Were you even listening, you moron?"
            show t angry with dissolve
            "I don't think that was the right question to ask..."
            play music "ost/neutral.wav" fadein 6
    show t neu with dissolve
    "He's silent for a moment."
    show t talk with dissolve
    t "It's time to end today's session, isn't it?"
    show t neutral with dissolve
    "I glance at the time."
    m gasp "Oh, right."
    "I get up to follow him to the door."
    m flirt "Thank you for answering my questions today. I'll see you again soon."
    show t hurttalk with dissolve
    t "Goodbye."
    play sound "doorclose.ogg" fadein 1
    scene bg mc with dissolve
    "He leaves in a hurry."
    "Did my last question really make him so nervous? Or is it about the whole session?"
    "I did ask a lot, but... I had no idea it was making him anxious."
    stop music fadeout 4
    "I freeze."
    "He should switch under pressure."
    "Should I expect to see someone else the next time I invite him to my office?"
    if sessions == 0:
        $firstpatient = "purple"
    $purpleinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen easymeter
    hide screen purplemeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump purplenotes
        "No":
            pass
    jump breaknav
label purple3:
    scene bg mc with dissolve
    play sound "knock2.ogg" 
    "I hear a faint knock on the door."
    "That's new..."
    m talk "Come in."
    play music "ost/tension.ogg" fadein 6
    "The door slowly opens and Tom enters my office."
    show bg mchanged with dissolve
    "Wait... that's not Tom..."
    "Is this a different personality?"
    pr "you are dr. hart, right..? our psychologist?"
    pr "i was told you would be here..."
    "I recover from my initial shock quickly. It's just an alter I haven't met yet."
    stop music fadeout 5
    m conf "Yes. I'm [name] Hart, nice to meet you."
    pr "...can i sit here?"
    m flirt "Of course."
    scene bg mcdesk with dissolve
    play music "ost/hospital.wav" fadein 8
    if easymeter: 
        show screen easymeter
        show screen purplemeter
    show hg neutral with dissolve
    "He seems much different than Tom already."
    m smile "What's your name?"
    "I realized it's likely for him to use a name separate from that of the first personality."
    show hg calmtalk with dissolve
    pr "it's {color=#9370e5}edward."
    show hg talk with dissolve
    pr "but... won't you call me by our given name? isn't it easier for you?"
    show hg hostile with dissolve
    menu:
        "I will use your own name":
            $PurpleHeart +=1
            $personal +=1
            show hg gasp with dissolve
            pr "...oh."
            show hg neutral with dissolve
            pr "that's very considerate of you"
            show hg smile with dissolve
            pr "thank you."
            show drk with Dissolve(0.75)
            show p 2 with dissolve
            show p 3 with Dissolve(0.55)
            $renpy.pause(0.5, hard = True)
            hide p with Dissolve(0.7)
            hide drk with dissolve
            $hanged = "Edward"
        "I'll keep calling you Tom":
            $professional +=1
            $hanged = "Tom"
            show hg talk with dissolve
            pr "our previous psychologist thought it was for the best..."
    show hg talk with dissolve
    pr "may i ask you something..?"
    show hg neutral with dissolve
    m flirt "Whatever you want to know."
    show hg calmtalk with dissolve
    pr "what day is it? i think it's been a while since i..."
    show hg calm with dissolve
    if day == 4:
        m talk "Today is the 4th of November, Thursday."
    else:
        m talk "Today is the 5th of November, Friday."
    show hg neutral with dissolve
    pr "i see..."
    menu:
        "How many times have you fronted since you're here?":
            show hg talk with dissolve
            stop music fadeout 6
            pr "{color=#9370e5}twice{/color}..?"
            pr "one was just after we came here and the last time - about two weeks ago..."
            show hg neutral with dissolve
            pr "it's not as frequent as it would seem."
        "For how long do you front for at a time?":
            $PurpleHeart +=1
            show hg talk with dissolve
            pr "{color=#9370e5}two, three days..."
            pr "the longest time was four days, i think."
            show hg hostile with dissolve
            stop music fadeout 5
            m uncom "That's so little, given that you don't switch very often..."
            show hg neutral with dissolve
            pr "it used to be even shorter {color=#9370e5}when we were younger{/color}. i'm grateful for having more time nowadays..."
            show drk with Dissolve(0.75)
            show p 2 with dissolve
            show p 3 with Dissolve(0.55)
            $renpy.pause(0.5, hard = True)
            hide p with Dissolve(0.7)
            hide drk with dissolve
    play music "ost/neutral.wav" fadein 6
    "I pity him. I thought he was in control as frequently as the core personality."
    "But it seems to be a rare occurance for him to appear."
    m serious "And you don't remember absolutely anything that happens when one of the others is fronting?"
    show hg hostile with dissolve
    "He shakes his head."
    show hg talk with dissolve
    pr "no."
    pr "some years ago, i sometimes got {color=#9370e5}glimpses of their memories."
    show hg sadtalk with dissolve
    pr "at first, i remembered everything, but after a few years as we seperated further, it stopped."
    show hg grief with dissolve
    "That brings another question to my mind."
    show hg neutral with dissolve
    m "How old were you at the time of your earliest memory?"
    show hg talk with dissolve
    pr "...it wasn't that clear at first... i wasn't immediately my own person, it was quite... blurry."
    pr "but... i think at {color=#9370e5}11{/color} i was seperate from tom."
    show hg hostile with dissolve
    "That's early... Really early, in fact."
    "I note the way he acknowledges himself as just another part of Tom..."
    "To an extent, he's his own person and should be treated as that."
    "But then again... shouldn't I try to bring all three of them closer together so they can integrate?"
    stop music fadeout 6
    menu:
        "You seem to understand your situation well.":
            $professional +=1
            show hg neutral with dissolve
            pr "...i try."
            show hg talk with dissolve
            pr "{color=#9370e5}i want to make it easier for everyone."
            show hg neutral with dissolve
            m pity "I appreciate it."
            show hg grief with dissolve
            pr "...it's better that way."
            show hg sadtalk with dissolve
            pr "{i}{b}{cps=*3}{color=#ffffff}n o b o d y\ \ \ w a n t s\ \ \ m e\ \ \ t o\ \ \ e x i s t\ \ \ a n y w a y -"
        "You're not just a part of someone else.":
            $personal += 1
            show hg sadtalk with dissolve
            pr "..what are you saying...?"
            show hg sad with dissolve
            m angrytalk "You deserve to be treated like a person, not someone else's problem."
            show hg talk with dissolve
            pr "but... isn't it what i am?"
            show hg sadtalk with dissolve
            pr "it's not just about me."
            show hg sad with dissolve
            pr "all three of us are here {color=#9370e5}because of me."
            show hg sadtalk with dissolve
            pr "{i}{b}{cps=*4}{color=#ffffff}i f\ \ \ i\ \ \ n e v e r\ \ \ e x i s t e d,\ \ \ i t\ \ \ w o u l d\ \ \ b e\ne a s i e r\ \ \ f o r\ \ \ e v e r y o n e -"
    play music "ost/tension.ogg" fadein 6
    show hg hiden with Dissolve(1.0)
    "His voice breaks suddenly and he covers his mouth."
    pr "i'm sorry... {color=#9370e5}i shouldn't have said that"
    "I'm speechless. That really took me off-guard."
    "I didn't expect him to be like this..."
    "He seems to have problems of his own, other than the illness itself."
    show hg grief with Dissolve(1.0)
    m serious "[hanged]..."
    show hg pain with dissolve
    pr "don't..."
    show hg sad with dissolve
    pr "don't ask me about it."
    show hg sadtalk with dissolve
    pr "{i}please, just forget i said that..."
    menu:
        "I won't":
            $professional += 1
            $wrong += 1
            show hg grief with dissolve
            "He leans back in his chair and closes his eyes."
            show hg calm with dissolve
            pr "...."
            show hg calmtalk with dissolve
            pr "ask if you have to"
            pr "you heard it already."
            show hg calm with dissolve
            stop music fadeout 5
            pr "do whatever you want with that"
            show hg pain with dissolve
            pr "i won't take it back."
            "....."
        "As you wish":
            $personal += 1
            $PurpleHeart+=1
            show hg shock with dissolve
            show drk with Dissolve(0.75)
            show p 2 with dissolve
            show p 3 with Dissolve(0.55)
            $renpy.pause(0.5, hard = True)
            hide p with Dissolve(0.7)
            hide drk with dissolve
            stop music fadeout 6
            show hg pale with dissolve
            "He looks at me, surprised."
            show hg sad with dissolve
            "Was he expecting me to disrespect his wishes?"
            show hg neutral with dissolve
            "We still have time."
            "If he ever wants to mention it again, I'll listen and do my best to help."
    m serious "How do you feel about living in the hospital?"
    show hg talk with dissolve
    play music "ost/neutral.wav" fadein 8
    pr "i can't really tell... {color=#9370e5}i haven't been here for long enough."
    show hg neutral with dissolve
    "He's right... For him, it's only been a few days."
    show hg talk with dissolve
    pr "but..."
    show hg smile with dissolve
    pr "...the nurses are nice."
    show hg sadtalk with dissolve
    pr "they always tell me which office to go to and who to look for..."
    pr "it's always so confusing... but they understand."
    show hg smile with dissolve
    pr "{color=#9370e5}they treat us well."
    "I note his choice of words. I'm not sure if I should be looking too deep into this, but it feels odd."
    m pity "I'm glad to hear that."
    "We have 5 minutes left."
    m talk "We should be wrapping this up."
    show hg talk with dissolve
    pr "oh"
    show hg hostile with dissolve
    "I lead him to the door."
    m uncom "Do you think I'll see you again the next time we meet?"
    "He nods slowly, a bit uncertain."
    m smile "I'm looking forward to it."
    show hg smile with dissolve
    pr "thank you, dr. hart."
    play sound "doorclose.ogg" fadein 1
    scene bg mc with dissolve
    "He leaves my office."
    "He seems so helpless and vulnerable... I hope he can be himself tomorrow as well."
    "He wasn't entirely what I expected, though..."
    "That time near the end... What he said shocked me completely."
    "He even told me to forget about it... Of course I won't."
    "I feel like to help Tom, I first need to help his other two personalities seperately."
    stop music fadeout 4
    "Maybe once I understand the source of their problem, I can help them connect."
    if sessions == 0:
        $firstpatient = "purple"
    $purpleinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen easymeter
    hide screen purplemeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump purplenotes
        "No":
            pass
    jump breaknav
label purple4:
    play music "ost/neutral.wav" fadein 10
    scene bg mcdesk with dissolve
    "[hanged] enters my office."
    show hg talk with dissolve
    pr "hello..."
    show hg hostile with dissolve
    m pity "It's good to see you again."
    m talk "Take a seat."
    if easymeter: 
        show screen easymeter
        show screen purplemeter
    show hg neutral with dissolve
    "He looks at me briefly."
    m "How are you today? How do you feel?"
    show hg smile with dissolve
    pr "i think... a lot better than yesterday."
    show hg sadtalk with dissolve
    pr "i'm sorry if i acted strangely last time... {color=#9370e5}it usually happens the day i come back."
    show hg talk with dissolve
    pr "it's just the confusion at first... you understand, right?"
    show hg hostile with dissolve
    menu:
        "I do":
            $PurpleHeart += 1
            m pity "You need time to adjust and that's okay."
            show hg smile with dissolve
            pr "thank you"
            show drk with Dissolve(0.75)
            show p 2 with dissolve
            show p 3 with Dissolve(0.55)
            $renpy.pause(0.5, hard = True)
            hide p with Dissolve(0.7)
            hide drk with dissolve
        "That's not an excuse":
            $professional += 1
            show hg sadtalk with dissolve
            pr "maybe it isn't... but it's all i have."
    show hg grief with dissolve
    pr "i..."
    show hg calmtalk with dissolve
    pr "...how do i put it?"
    show hg sadtalk with dissolve
    pr "...i wanted to {color=#9370e5}ask you something."
    show hg talk with dissolve
    pr "is that okay?"
    show hg hostile with dissolve
    m conf "Of course it is, ask away."
    show hg sadtalk with dissolve
    pr "you've had multiple interactions with us before i came back, is that right?"
    show hg sad with dissolve
    m fabtalk "I did. Three of them, actually."
    show hg talk with dissolve
    pr "so... you had the chance to talk to one of them..."
    pr "which one was it?"
    show hg neutral with dissolve
    menu:
        "The core":
            $PurpleHeart+=1
            $professional += 1
            show hg talk with dissolve
            pr "oh, that makes sense..."
        "The mean one":
            $personal += 1
            show hg talk with dissolve
            pr "from what i know, they're both like that..."
            show hg neutral with dissolve
            pr "but i think i know which one you mean"
        "The one with a ponytail":
            $wrong += 1
            show hg talk with dissolve
            pr "i... actually don't know what the others look like."
            show hg neutral with dissolve
            pr "...that's interesting."
            m fab "It was the first one."
            show hg talk with dissolve
            pr "oh, okay"
    show hg talk with dissolve
    pr "so you haven't met {color=#9370e5}the third one{/color} yet?"
    show hg hostile with dissolve
    "I shake my head."
    m conf "I'm sure I'll get the chance to soon."
    show hg talk with dissolve
    pr "the psychologists usually seem relieved when i come back and he was before me."
    show hg neutral with dissolve
    m uncom "Why is that?"
    pr "i think it's due to his... attitude. it's a little problematic"
    stop music fadeout 6
    m neu "..."
    m talk "I see."
    show hg sadtalk with dissolve
    pr "can i keep asking? i don't really have much time and i wanted to learn somethings."
    show hg sad with dissolve
    "I nod with a smile. Being asked questions by a patient is often a source of more valuable information than asking them things."
    show hg talk with dissolve
    play music "ost/hospital.wav" fadein 6
    pr "what do you think... of the first one, so far?"
    show hg hostile with dissolve
    "I have mixed feelings about him... what should I say?"
    menu:
        "He's kind of harsh":
            $personal += 1
            m serious "The first time we met, he just yelled at me for no reason."
            show hg sad with dissolve
            m talk "He wasn't as bad the next time we met, but he's still kind of cold..."
            show hg calm with dissolve
            pr "..."
            show hg talk with dissolve
            pr "i'm glad i'm not like him. "
            show hg smile with dissolve
        "I don't have problems with him":
            $professional += 1
            m fabtalk "I don't know, I don't have any opinion of him in particular."
            show hg talk with dissolve
            pr "i see..."
            show hg neutral with dissolve
        "I like you more":
            $PurpleHeart += 1
            show hg pale with dissolve
            stop music fadeout 2
            "His face turns pale."
            show hg shock with dissolve
            pr "like... me..?"
            show drk with Dissolve(0.75)
            show p 2 with dissolve
            show p 3 with Dissolve(0.55)
            $renpy.pause(0.5, hard = True)
            hide p with Dissolve(0.7)
            hide drk with dissolve
            show hg pale with dissolve
            "I spoke without thinking. I didn't mean it in any weird way, just that my time with Edward has been more enjoyable than it was with Tom."
            show hg neutral with dissolve
            play music "ost/hospital.wav" fadein 5
            m fabtalk "You're a lot more pleasant to be around than him."
            show hg sadtalk with dissolve
            pr "is... that so...?"
            show hg neutral with dissolve
    "I think I have questions of my own."
    "Regarding his curiosity about the alters."
    menu:
        "Have you ever seen what the others look like?":
            $personal += 1
            show hg talk with dissolve
            pr "no, i haven't gotten to chance to in a few years at least."
            show hg sadtalk with dissolve
            pr "since we don't really communicate in any way..."
            show hg hostile with dissolve
            pr "i'm... honestly curious now."
        "Have you tried contacting the others?":
            $PurpleHeart += 1
            show hg talk with dissolve
            pr "when i first woke up in the hospital, i left a message in our room."
            show hg hostile with dissolve
            "That's actually a good idea..."
            show hg talk with dissolve
            pr "neither of them has responded yet..."
            show hg neutral with dissolve
            m uncom "That's a shame... I could try convincing one of them to contact you when I get the chance."
            show hg smile with dissolve
            pr "it would be nice... i just want to get along with them..."
            show hg hostile with dissolve
            pr "{i}despite what they did"
            show drk with Dissolve(0.75)
            show p 2 with dissolve
            show p 3 with Dissolve(0.55)
            $renpy.pause(0.5, hard = True)
            hide p with Dissolve(0.7)
            hide drk with dissolve
    m angry "Is there anything else you'd like to ask me?"
    show hg gasp with dissolve
    pr "m-me?"
    show hg sadtalk with dissolve
    pr "i don't know... people usually don't care about my opinion, so..."
    show hg sad with dissolve
    "He shakes his head. I guess he's not used to speaking up on his own."
    "It was worth a try."
    m fabtalk "So, [hanged]... You were the first one to seperate?"
    show hg talk with dissolve
    stop music fadeout 6
    pr "that's right. it was {color=#9370e5}almost twenty years ago{/color}..."
    show hg hostile with dissolve
    m serious "Do you have any idea what might have caused it? Whatever did must've happened multiple times for you to fully develop, you should remember..."
    show hg sad with dissolve
    "He's silent. Even if he remembers everything, he might not realize what the direct cause was."
    m talk "I was told that the first one usually shifts due to stress."
    play music "ost/tension.ogg" fadein 7
    m frust "It's likely that this is what caused you to emerge in the first place."
    m angrytalk "What could've caused Tom so much stress that you were needed?"
    "I realize my question is quite direct, but there's a chance that he remembers it and can spare me a lot of trouble by telling me."
    show hg sadtalk with dissolve
    pr "i... {i}don't know..."
    show hg sad with dissolve
    "He might be hiding something."
    m angry "You said yesterday that when you first took control, you remembered a lot of what happened before that."
    m gasp "So there must be something you-"
    show hg shock with dissolve
    pr "i-i won't talk about it."
    show hg pant with dissolve
    pr "please... {color=#9370e5}i can't{/color}..."
    show hg sad with dissolve
    "I don't know what to do... He clearly knows the reason behind his illness, but won't tell me about it."
    menu:
        "You have to tell me":
            $professional += 1
            show hg dread with dissolve
            pr "...."
            show hg pant with dissolve
            pr "{color=#9370e5}stop it..."
            show hg sad with dissolve
            "He hides his face in his hands."
            "I think I heard a sob."
            m serious "[hanged]..."
            m regrettalk "I'm sorry. I didn't know it would cause you so much pain."
            show hg sadtalk with dissolve
            pr "no, it's fine..."
            show hg neutral with dissolve
            "He uncovers his face."
            show hg talk with dissolve
            pr "{color=#9370e5}{i}i'm used to it anyway"
        "Does it hurt that much?":
            $personal += 1
            $PurpleHeart += 1
            show hg pant with dissolve
            pr "{color=#9370e5}{i}you have... no idea..."
            show hg dread with dissolve
            m regrettalk "...."
            show hg calm with dissolve
            m sadtalk "I only want to help you."
            show hg sadtalk with dissolve
            pr "...i know."
            show hg sad with dissolve
            show drk with Dissolve(0.75)
            show p 2 with dissolve
            show p 3 with Dissolve(0.55)
            $renpy.pause(0.5, hard = True)
            hide p with Dissolve(0.7)
            hide drk with dissolve
            m uncom "You don't have to tell me yet. I'll wait."
            "He nods."
            show hg smile with dissolve
            pr "thank you, dr. hart."
        "Take your time":
            show hg calm with dissolve
            pr "...."
            "I wait for a few moments."
            show hg neutral with dissolve
            "Nothing happens, but he seems calmer now."
    stop music fadeout 5
    "Maybe I can ask him something else."
    m serious "[hanged]?"
    "He looks at me."
    m talk "Could you tell me what usually causes you to shift?"
    play music "ost/neutral.wav" fadein 8
    show hg talk with dissolve
    pr "...oh."
    pr "i think it's stress, like for the first one."
    show hg sadtalk with dissolve
    pr "but it's not the same, because i tend to come back when he's struggling with some conflicted feelings or is in pain."
    show hg calmtalk with dissolve
    pr "and as for me... i usually disappear when i have some {color=#9370e5}responsibility{/color} that i can't handle."
    show hg talk with dissolve
    pr "you know..."
    show hg sadtalk with dissolve
    pr "{color=#9370e5}i can take a lot{/color}. but i can only receive"
    pr "i can't really... {i}act{/i} on anything."
    show hg talk with dissolve
    pr "i think the other two are the opposite of me in that way."
    pr "they must be, judging by their actions..."
    show hg neutral with dissolve
    "Our session is about to end."
    m pity "Thank you for sharing all of that with me."
    m talk "You gave me a lot of valuable information today."
    show hg smile with dissolve
    pr "i'm just glad to help..."
    "I remember what's about to happen today."
    m serious "My boss asked me to meet him after work."
    show hg neutral with dissolve
    m talk "He'll judge my progress and if I'm handling the job well..."
    show hg talk with dissolve
    pr "this is your first week here, isn't it?"
    show hg neutral with dissolve
    "I nod."
    if PurpleHeart>=12:
        show hg smile with dissolve
        pr "{color=#9370e5}i'm sure you did well..."
        show hg smileblush with dissolve
        pr "we only talked twice, but i know you're good at this."
    else:
        show hg talk with dissolve
        pr "i can't really judge how well you did yet, so..."
        show hg neutral with dissolve
        pr "good luck"
    show hg smile with dissolve
    m smile "Thank you."
    show hg talk with dissolve
    pr "i... should be leaving..."
    m gasp "Right..."
    stop music fadeout 5
    show hg neutral with dissolve
    "He stands up to leave and I follow him to the door."
    show hg sadtalk with dissolve
    pr "{i}are you... staying here for the weekend?"
    show hg sad with dissolve
    "I shake my head."
    show hg talk with dissolve
    play music "ost/tran.ogg" fadein 6
    pr "then... {color=#9370e5}i don't think we'll meet again on monday."
    show hg sad with dissolve
    "For some reason, it makes me sad to hear this."
    m conf "Whenever you're back, I'll see you again."
    show hg shock with dissolve
    pr "r-really? {i}you must have other patients..."
    show hg neutral with dissolve
    m pity "I have time for everyone."
    show hg talk with dissolve
    pr "if that's so..."
    show hg smile with dissolve
    pr "{color=#9370e5}it makes me happy to hear that, dr. hart."
    m flirt "Goodbye, [hanged]~"
    play sound "doorclose.ogg" fadein 1
    scene bg mc with dissolve
    pause 1
    "I decided to spend every session I could with them."
    "Regardless, I have no regrets."
    "If I keep this job after today's conversation with Dr. Sharpe, I should still meet them every day."
    stop music fadeout 4
    "I can't wait to see them again next week... any of them."
    if sessions == 0:
        $firstpatient = "purple"
    $purpleinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen easymeter
    hide screen purplemeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump purplenotes
        "No":
            pass
    jump breaknav

##### MOON NAVIGATION ##########################
################################################
label silverintro:
    "Anxiety disorders are quite common, so helping him shouldn't be a problem."
    "I think I know what to expect from him."
    $silverintro = 1
    scene bg mc with dissolve
    "The door to my office opens and I look up from my desk."
    scene bg mcmoon with Dissolve(1.0)
    play music "ost/tension.ogg" fadein 10
    "The young man who just entered my office must be {color=#fff1c1}William Moore."
    "He's frozen in place, not moving towards my desk at all."
    m serious "You're William, right?"
    "He nods, never taking his eyes off of mine."
    m angrytalk "I'm your new psychologist, [name] Hart."
    m talk "Please, take a seat. I just want to talk."
    scene bg mcdesk with dissolve
    show w tense with dissolve
    if easymeter: 
        show screen easymeter
        show screen silvermeter
    "Slowly, he sits down on the other side of my desk."
    "I notice how tense he is and how he's sitting on the edge of his chair as if to run away from me at any moment."
    show w frust with dissolve
    "I should be mindful of what I say."
    menu:
        "Are you okay?":
            $personal +=1
            "He looks at me suddenly."
            show w angry with dissolve
            w "{i}I am."
        "Can we begin?":
            $professional += 1
            show w calm with dissolve
            "He nods, but doesn't look convinced."
        "{color=#fff1c1}Stay silent":
            $SilverHeart+=1
            "I keep looking at him in silence with a gentle smile."
            show w calm with dissolve
            "If I started asking him questions, he might feel attacked in a way, so I'm patient."
            show w pain with dissolve
            "It's more valuable for me to have him speak to me on his own, rather than throw questions at him."
            show drk with Dissolve(0.75)
            show s 1 with dissolve
            show s 2 with Dissolve(1.0) 
            $renpy.pause(0.75, hard = True)
            hide s with dissolve
            hide drk with dissolve
            show w angry with dissolve
            w "What are you {i}doing{/i}?"
            "His voice is surprisingly calm and quiet. I would even call it cold."
            m fabtalk "Nothing in particular. I was waiting for you to say something."
            show w frusttalk with dissolve
            w "Tsh-"
    show w siden with dissolve
    "I can tell he wants this conversation to end as quickly as possible."
    "I have to find something he'd be willing to talk about..."
    stop music fadeout 6
    m talk "How long have you been here for?"
    show w talk with dissolve
    w "{color=#fff1c1}Two years{/color}? Something like that."
    show w siden with dissolve
    "Two years is a long time in a place like this..."
    "Something doesn't add up... His illness shouldn't take that long to treat."
    ## play music "ost/normal.ogg" fadein 10
    menu:
        "You have GAD?":
            show w sidetalk with dissolve
            w "That's right."
            show w siden with dissolve
            "Hmm... this must be an odd case."
        "Do you have more than one illness?":
            $SilverHeart+=1
            show w tensetalk with dissolve
            w "{color=#fff1c1}I... don't think so..."
            show w tense with dissolve
            "He seems hesitant. Something is definitely odd about him."
            show drk with Dissolve(0.75)
            show s 1 with dissolve
            show s 2 with Dissolve(1.0) 
            $renpy.pause(0.75, hard = True)
            hide s with dissolve
            hide drk with dissolve
        "It must be tough to stay here":
            $personal +=1
            show w frusttalk with dissolve
            w "Do I look like I'm {i}complaining{/i}?"
            show w siden with dissolve
            "There's a hint of bitterness in his voice."
    "His behavior doesn't let me find any questions to ask him."
    "He seems to purposefully answer in a way that doesn't give me any more information than what I ask about."
    "It's quite bothersome."
    "I can respond to a lot of problems, but I always have trouble handling situations like this one - where I have to come up with things to say and ask completely on my own."
    show w angry with dissolve
    m serious "Why aren't you talking to me, William? I was hoping we could have a conversation and get to know each other..."
    show w angrytalk with dissolve
    w "I'll answer your questions, but don't expect a friendly chat from me."
    w "{color=#fff1c1}I don't intend to \"get to know you\"."
    show w frust with dissolve
    "On a positive note, he spoke to me at last. This may not be as difficult as I thought it would be."
    m fabtalk "Then what do you want out of these sessions? Surely there's something I can do for you..."
    stop music fadeout 4
    show w frustsmile with dissolve
    w "Heh..."
    show w tensetalk with dissolve
    w "You put it that way to make it seem more personal, didn't you?"
    show w talk with dissolve
    w "How many patients do you have?"
    show w neutral with dissolve
    m neu "You and three others."
    play music "ost/tension.ogg" fadein 8
    show w angrytalk with dissolve
    w "And you expect me to believe you {i}actually care{/i} about all of us? About how we feel?"
    show w angry with dissolve
    menu:
        "I care about you all":
            $personal += 1
            show w talk with dissolve
            w "This is your first day at work, isn't it?"
            show w calm with dissolve
            m gasp "How..?"
            show w siden with dissolve
            w "It's obvious."
            show w talk with dissolve
            w "So you can't possibly \"care\" about any of us yet."
        "I want to help":
            show w calm with dissolve
            w "...."
            show w talk with dissolve
            w "Well?"
            show w sidetalk with dissolve
            w "I'm waiting."
        "Make me care":
            $SilverHeart += 1
            show w evil with dissolve
            w "Is that a dare?"
            show w talk with dissolve
            w "I should be asking you - make me care about these sessions."
            show w regretsmile with dissolve
            w "How about that?"
            show drk with Dissolve(0.75)
            show s 1 with dissolve
            show s 2 with Dissolve(1.0) 
            $renpy.pause(0.75, hard = True)
            hide s with dissolve
            hide drk with dissolve
    stop music fadeout 6
    show w siden with dissolve
    "I note that I got him talking."
    "At least there's that."
    "The more he says, the more information I get about him."
    "Let's keep this up."
    m fabtalk "I wanted to ask you something..."
    play music "ost/tension.ogg" fadein 5
    show w regret with dissolve
    "I look at him once more and realize that his gaze is fixated on the floor again."
    "I messed up."
    "He's not looking back at me, just like before."
    "Maybe he thought he'd said too much and regretted it."
    "I wouldn't be surprised - it seems very characteristic of his illness."
    "I decide to give him some time. We still have a while, so there's no rush."
    "...."
    "He's silent."
    if purpleintro == 1:
        "It's not like with Tom at all..."
        "At least with him I knew what was going through his head and what to expect, but William... he's difficult."
    show w tense with dissolve
    "I look down at my hands on the desk and immediately catch a glimpse of silver - he's glaring at me silently."
    "I don't think it's to intimidate me or anything of the sort - he seems to be very cautious of his surroundings."
    "I raise my head quickly enough to meet his eyes. He freezes."
    show w fear with dissolve
    "Keeping my eyes on his for a while, I don't let him look away from me this time."
    show w neutral with dissolve
    "I need to make him maintain some amount of contact with me."
    "I haven't lost him yet."
    "He's not looking away, even though I can tell he'd want to."
    show w tense with dissolve
    "He shifts in his seat, as if attempting to put as much space between us as possible."
    "He's tense."
    menu:
        "{color=#fff1c1}Keep pushing":
            $dominant +=2
            $SilverHeart += 1
            "I keep my eyes on him, letting him know I won't stop until he talks to me at last."
            show w pain with dissolve
            "He breaks."
            show drk with Dissolve(0.75)
            show s 1 with dissolve
            show s 2 with Dissolve(1.0) 
            $renpy.pause(0.75, hard = True)
            hide s with dissolve
            hide drk with dissolve
            show w frusttalk with dissolve
            w "{i}Why{/i} are you doing that?"
            show w tense with dissolve
            "There's a hint of genuine confusion in his voice."
            show w tensetalk with dissolve
            w "If you want to say something, say it and quit staring at me."
            show w frust with dissolve
            m fabtalk "I'm not the one who should be talking now."
            show w tensetalk with dissolve
            w "Then why are you even here?"
            m angrytalk "To help you."
        "{color=#fff1c1}Let it go":
            $submissive += 2
            "I look down again, trying not to make him anxious."
            "I'm patient. And making him nervous is the last thing I want."
            "I wait..."
            "A few minutes pass."
            m serious "Listen, I just want to help you."
    show w regret with dissolve
    w "...."
    show w regrettalk with dissolve
    w "And what makes you think I want your help?"
    show w angrytalk with dissolve
    w "{color=#fff1c1}I'm here because I want to. I chose this."
    show w talk with dissolve
    w "I don't need your help. So do what your predecessors did and give up."
    show w sidetalk with dissolve
    w "It'll be easier for both of us..."
    show w siden with dissolve
    stop music fadeout 10
    "He falls silent just like before, looking at me."
    "It's clear to me he won't say anything more about that."
    "We still have half an hour, but..."
    "I don't think he wants to be here any longer than necessary."
    "I give him a moment to calm down before I speak again."
    play music "ost/neutral.wav" fadein 8
    m talk "We could still talk, but I think I learned everything I needed to know for now."
    show w tense with dissolve
    m fabtalk "You may go back to your room earlier."
    show w calm with dissolve
    "He nods quickly and stands up. I don't need to tell him twice."
    play sound "doorclose.ogg" fadein 1
    scene bg mc with dissolve
    "After he leaves, I wonder..."
    "This surely isn't a typical case - if it was, he wouldn't be here for so long..."
    "He said he chose to be here. I wonder what drove him to want to be in this place..."
    "Was life outside the hospital really that horrible for him?"
    stop music fadeout 4
    "It doesn't look like I'll learn a lot from him, though... I'm not sure if I have what it takes to get him to trust me."
    $sessions += 1
    show drk with dissolve
    $persistent.William=True
    show screen notify("{size=24} Your Characters Info screen has been updated!")
    hide screen easymeter
    hide screen silvermeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump silvernotes
        "No":
            pass
    jump breaknav
label silver:
    if day < 6 and month==1:
        if silverinteract == 0:
            jump silver1
        elif silverinteract == 1:
            jump silver2
        elif silverinteract == 2:
            jump silver3
        elif silverinteract == 3:
            jump silver4
    else:
        jump silversession
label silver1:
    scene bg mcdesk with dissolve
    "William enters my office slowly."
    play music "ost/hospital.wav" fadein 8
    "I look at him, unsure of what to say after last time."
    m conf "It's good to see you again. Take a seat."
    if easymeter: 
        show screen easymeter
        show screen silvermeter
    show w tensetalk with dissolve
    w "Dr. Hart..?"
    show w frusttalk with dissolve
    w "I wanted to mention something regarding last time..."
    show w tense with dissolve
    m gasp "...Oh?"
    show w frusttalk with dissolve
    w "I acted too harshly towards you. It was... uncalled for."
    show w tense with dissolve
    "I actually didn't expect him to apologize for any of that, but I'm glad he did."
    stop music fadeout 6
    m flirt "It's fine, really. I understand that everyone has worse days sometimes."
    show w calm with dissolve
    "He leans back in his chair, seeming slightly calmer than before."
    show w talk with dissolve
    play music "ost/neutral.wav" fadein 7
    w "Great. I hope you never have to see any of that again."
    show w neutral with dissolve
    "It wasn't... that bad, was it?"
    "Either way, I'm sure I won't have trouble working with him from now on."
    show w siden with dissolve
    m fabtalk "So, William..."
    "I glance at him."
    m talk "Actually, is it okay for me to use your first name?"
    show w frust with Dissolve(0.3)
    show w neutral with dissolve
    "He nods."
    show w talk with dissolve
    w "That's not a problem for me."
    show w neutral with dissolve
    m fabtalk "How are you today?"
    "I thought it might be good to start off with something simple, trying not to make him anxious."
    show w sidetalk with dissolve
    stop music fadeout 5
    w "Same as always. Nothing noteworthy besides being tired - I didn't get much sleep last night."
    show w frust with dissolve
    m gasp "Why is that? Did something happen?"
    show w frusttalk with dissolve
    play music "ost/tension.ogg" fadein 3
    w "No, it's just that..."
    show w tense with dissolve
    w "{color=#fff1c1}There are things in my head that keep me up at night."
    show w pain with dissolve
    "...I see."
    show w talk with dissolve
    w "Is that all you wanted to know?"
    show w frust with dissolve
    stop music fadeout 4
    "I don't think he trusts me enough to go into detail about that..."
    m talk "It is. Now..."
    play music "ost/neutral.wav" fadein 8
    menu:
        "What made you act like you did last time?":
            show w frusttalk with dissolve
            w "I... I'm not sure."
            show w frust with dissolve
            w "I just felt, um... worse than I usually do."
            show w tense with dissolve
            w "I think I had a strange dream the night before as well... I can't really remember it."
        "Has anyone here threatened you or treated you badly?":
            $SilverHeart+=1
            show drk with Dissolve(0.75)
            show s 1 with dissolve
            show s 2 with Dissolve(1.0) 
            $renpy.pause(0.75, hard = True)
            hide s with dissolve
            hide drk with dissolve
            show w tensetalk with dissolve
            w "...No, I don't think so."
            show w frusttalk with dissolve
            w "If you asked that regarding me being unable to sleep last night, then no - it's not the other patients here I'm so... unsettled by."
            show w frust with dissolve
        "What are you actually so afraid of?":
            $wrong +=1
            show w tensetalk with dissolve
            w "I... I don't think this is the right question at this time, given that this is our second time interacting."
            show w angrytalk with dissolve
            w "And I really don't like getting interrogated this directly."
            show w angry with dissolve
            "Wrong question..."
    m serious "How do you feel about living here?"
    show w sidesmile with dissolve
    w "How am I supposed to feel?"
    show w tensetalk with dissolve
    w "I stay here because it's the only place someone like me should be."
    show w tense with dissolve
    "Interesting choice of words."
    show w frusttalk with dissolve
    w "It's not as bad as I'd imagined it before I got here, though."
    show w sidetalk with dissolve
    w "I suppose it could be worse - it's as good as any place can be for me."
    show w frusttalk with Dissolve(0.3)
    show w talk with dissolve
    w "Though, being admitted here forced me to quit university -  I guess it's still for the best."
    show w neutral with dissolve
    menu:
        "What were you studying?":
            show w talk with dissolve
            w "Physics, actually."
            show w frusttalk with dissolve
            w "It wasn't that difficult of a choice, to be honest."
            show w neutral with dissolve
        "That's a shame...":
            $wrong+=1
            show w tensetalk with dissolve
            w "I knew the consequences when I chose to live here."
            show w frusttalk with dissolve
            w "I don't want your pity for something you don't even understand."
            show w frust with dissolve
        "It's good you were able to get help at least":
            $SilverHeart+=1
            show drk with Dissolve(0.75)
            show s 1 with dissolve
            show s 2 with Dissolve(1.0) 
            $renpy.pause(0.75, hard = True)
            hide s with dissolve
            hide drk with dissolve
            show w talk with dissolve
            w "I agree. It would be risky to pretend like there was no problem and try to keep acting like..."
            show w frust with dissolve
            w "...like a normal person, I guess."
    stop music fadeout 6
    "Whatever his life used to be like, he's here now and seems to accept it."
    m fabtalk "Listen, I know that our first session wasn't a good start, but I really think we can work together to help you if you trust me enough."
    show w tense with dissolve
    play music "ost/hospital.wav" fadein 6
    m uncom "I'm not asking you to tell me everything right now, of course, all I want to know is..."
    m serious "Do you think I'm the right person for it?"
    m "I'm sure you've already had at least a couple of psychologists and yet you're still here."
    stop music fadeout 7
    m regrettalk "I just... don't want to be the next one to fail you. Do you think you can handle trusting me eventually?"
    "He's silent for a moment."
    show w frust with dissolve
    w "I..."
    if SilverHeart>5:
        play music "ost/tran.ogg" fadein 6
        show w tensetalk with dissolve
        w "I'll try. It won't be easy for me, but maybe if you keep doing what you're doing, you can get somewhere with this..."
        show w tense with dissolve
        m flirt "Thank you, William. I'll do my best, I promise."
    else:
        show w angrytalk with dissolve
        w "I don't know what you expect to do here."
        show w frusttalk with dissolve
        play music "ost/hospital.wav" fadein 8
        w "There's a reason I've been here for this long, Dr. Hart. I don't think you can change it."
        show w frust with dissolve
        m serious "Then... let me at least try."
    "It's way too early to give up on him."
    "Sure, two years here is a long time, but I believe I can help. I have hope for him."
    show w neutral with dissolve
    m conf "Thank you for being honest with me."
    show w siden with dissolve
    "He nods, but looks away from me."
    "I should ask him something else..."
    stop music fadeout 6
    m "Do you ever get visited here? Friends? Family?"
    show w frust with dissolve
    w "..."
    show w talk with dissolve
    w "No."
    show w tensetalk with dissolve
    w "I don't."
    show w frust with dissolve
    play music "ost/neutral.wav" fadein 8
    "Well then..."
    menu:
        "Doesn't that make you feel lonely here?":
            $personal +=1
            show w talk with dissolve
            w "Dr. Hart..."
            show w sidesmile with dissolve
            w "If the solution to loneliness was spending time with people, my life would be a lot easier."
        "Doesn't anyone know you're here?":
            show w regretsmile with dissolve
            w "Ironically, I think everyone who cared would have realized what'd happened to me."
        "Why would everyone leave you like that?":
            show w talk with dissolve
            w "Why wouldn't they?"
            show w regrettalk with dissolve
            w "Nobody would want to be associated with me after I got here."
            show w regretsmile with dissolve
            w "It's understandable, really."
    show w neutral with dissolve
    m uncom "And before you got here, did you maintain contact with your parents?"
    stop music fadeout 4
    show w sidesmile with dissolve
    "He chuckles."
    m fabtalk "What's so funny?"
    show w talk with dissolve
    w "It would be quite difficult to keep in touch..."
    show w sidetalk with dissolve
    play music "ost/tension.ogg" fadein 5
    w "{color=#fff1c1}...with someone who's dead."
    show w siden with dissolve
    menu:
        "I'm sorry":
            $personal +=1
            m uncom "I didn't mean to sound insensitive."
            show w neutral with dissolve
            w "It's been a while... I don't even remember them much."
        "What happened?":
            show w talk with dissolve
            w "Just a regular accident. I was told I was lucky to have survived, though."
            show w regret with dissolve
            w "...."
        "How old were you when it happened?":
            $professional +=1
            show w talk with dissolve
            w "4... 5? It's really been a while."
            show w neutral with dissolve
    stop music fadeout 6
    "I'm drawing conclusions way too quickly here, but whatever happened after his parents' death may have caused his illness."
    m serious "Are you okay? I didn't mean to pressure you."
    show w sidetalk with dissolve
    play music "ost/neutral.wav" fadein 6
    w "I'll live... It's not like sharing that with you changes anything."
    show w talk with dissolve
    w "Judging by the time, I should be leaving around now."
    show w siden with dissolve
    "He's right."
    show w sidetalk with dissolve
    w "If you'll excuse me for today, Dr. Hart..."
    scene bg mc with dissolve
    "He gets up and opens the door to leave."
    m conf "I'll see you again soon, William. Goodbye."
    play sound "doorclose.ogg" fadein 1
    stop music fadeout 4
    "He leaves."
    if sessions == 0:
        $firstpatient = "silver"
    $silverinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen easymeter
    hide screen silvermeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump silvernotes
        "No":
            pass
    jump breaknav
label silver2:
    scene bg mcdesk with dissolve
    show w neutral with dissolve
    play music "ost/neutral.wav" fadein 10
    w "Hello."
    if easymeter: 
        show screen easymeter
        show screen silvermeter
    "William takes a seat in front of me."
    show w talk with dissolve
    w "So what's the plan for today?"
    show w neutral with dissolve
    "He seems eager to talk this time. Great."
    "I may have a few questions today..."
    m uncom "I've read your file. It says that you..."
    menu:
        "Spend all your time alone":
            show w frusttalk with dissolve
            w "What's so unusual about needing some space?"
            show w talk with dissolve
            w "I don't feel the need to talk to anyone, that's all."
        "Refuse to interact with the staff members":
            show w talk with dissolve
            w "I only talk to them when it's necessary."
            show w sidetalk with dissolve
            w "I don't think I'm obliged to befriend everyone I meet, but I cooperate when it's needed."
        "Are known to become aggressive at times":
            show w talk with dissolve
            w "Actually, that would be outdated."
            show w frusttalk with dissolve
            w "The first few times they would approach me when, um... {i}those{/i} happened to me, I would get a bit... agitated."
            show w talk with dissolve
            w "But I've learned to ignore every staff member attempting to \"help me\" when that happens."
    show w neutral with dissolve
    m fabtalk "Overall, what's your relationship with the other patients?"
    show w talk with dissolve
    w "It varies from person to person, I guess."
    w "I don't pay attention to most of them and in turn, they leave me be."
    show w tensetalk with dissolve
    w "Some of them act nice, so it wouldn't be right to be cold towards them."
    show w sidetalk with dissolve
    w "And then... "
    show w frusttalk with dissolve
    w "There are some that just won't stop bothering me."
    show w angry with dissolve
    w "It's like they don't even realize I don't want to spend any more time with them than necessary..."
    m serious "Do any of them give you trouble?"
    show w sidetalk with dissolve
    w "No, it's not like they do anything of the sort... They're just..."
    show w frusttalk with dissolve
    w "...persistent. Like one clear \"no\" isn't enough for them."
    show w frust with dissolve
    m neutral "I see."
    show w talk with dissolve
    w "Don't get me wrong, if they needed help or anything like that, I wouldn't avoid them - I'm not that kind of person."
    show w frusttalk with dissolve
    w "But all they seem to want from me is amusement. And I don't appreciate that."
    show w frust with dissolve
    m talk "I understand."
    menu:
        "How do you think other patients feel about you?":
            $SilverHeart+=1
            show w talk with dissolve
            w "About me?"
            show w frusttalk with dissolve
            w "Let me think..."
            show w sidetalk with dissolve
            w "They definitely don't like me, they have no reason to..."
            w "Mostly, I think they avoid me."
            show w frust with dissolve
            w "To be honest, I don't really blame them."
            show drk with Dissolve(0.75)
            show s 1 with dissolve
            show s 2 with Dissolve(1.0) 
            $renpy.pause(0.75, hard = True)
            hide s with dissolve
            hide drk with dissolve
            show w talk with dissolve
            w "I've been here for long enough for everyone to at least recognize me here, so their judgement is likely correct."
        "How do you feel about the staff?":
            $personal+=1
            show w frusttalk with dissolve
            w "I..."
            show w talk with dissolve
            w "I don't have much of an attachment to any of them."
            show w sidetalk with dissolve
            w "They're doing their job and I try not to make it more difficult for them."
        "Are there many patients who bother you like that?":
            w "Um..."
            show w tensetalk with dissolve
            w "...not really."
    show w neutral with dissolve
    m serious "Is there any reason why you don't like interacting with the other patients?"
    show w frust with dissolve
    w "I... I don't know, I just don't really... like doing that."
    m neutral "I see."
    show w frusttalk with dissolve
    w "I guess it could be because... I wouldn't exactly trust myself to spend time with people."
    show w frust with dissolve
    m fab "And why is that?"
    w "..."
    m uncom "Does being with people cause you anxiety?"
    show w talk with dissolve
    w "You mean like that girl from room III who always gets scared whenever someone tries to talk to her?"
    show w sidetalk with dissolve
    w "She seems to have trouble maintaining a normal conversation because of the stress."
    show w talk with dissolve
    w "But no, I'm not like that."
    show w neutral with dissolve
    m angrytalk "So you're just naturally introverted and that's it?"
    show w sidetalk with dissolve
    w "Most likely."
    show w siden with dissolve
    m conf "Okay then. I just wanted to make sure."
    show w neutral with dissolve
    stop music fadeout 5
    "He nods."
    m fabtalk "And you were always like this?"
    show w frusttalk with dissolve
    w "Umm... maybe since some... 15 years ago? 10?"
    play music "ost/tran.ogg" fadein 8
    show w frust with dissolve
    "Alright then..."
    menu:
        "Did you have any friends before you got here?":
            show w regret with dissolve
            w "..."
            show w regrettalk with dissolve
            w "I had {i}some{/i} friends..."
            show w tensetalk with dissolve
            w "But apparently they weren't close enough to visit me here or care."
        "Did you enjoy being with people before that time?":
            $SilverHeart+=1
            show w regret with dissolve
            w "I did... with a couple of them in particular."
            show w regrettalk with dissolve
            w "But... I must've liked that too much."
            show drk with Dissolve(0.75)
            show s 1 with dissolve
            show s 2 with Dissolve(1.0) 
            $renpy.pause(0.75, hard = True)
            hide s with dissolve
            hide drk with dissolve
        "What happened then?":
            $SilverHeart+=1
            show w regrettalk with dissolve
            w "I'm... not sure."
            show w tensetalk with dissolve
            w "Maybe I just realized it's not worth it."
            show drk with Dissolve(0.75)
            show s 1 with dissolve
            show s 2 with Dissolve(1.0) 
            $renpy.pause(0.75, hard = True)
            hide s with dissolve
            hide drk with dissolve
    show w tense with dissolve
    m serious "So when did your illness start to develop?"
    show w regrettalk with dissolve
    w "I don't know..."
    show w tensetalk with dissolve
    w "I think it was just shaped over time into what it is now. I really can't tell when it started."
    show w tense with dissolve
    m talk "And could you estimate when it started to affect your life negatively?"
    show w tensetalk with dissolve
    w "Maybe when I was around... 16?"
    show w tense with dissolve
    stop music fadeout 5
    "That's already something. I like to have a timeline to work with."
    play sound "page.ogg" 
    "I look through my notes quickly..."
    "Oh."
    show w fear with dissolve
    m serious "Are you okay talking about the panic attacks?"
    show w sidetalk with dissolve
    play music "ost/neutral.wav" fadein 10
    w "...if I have to."
    show w frusttalk with dissolve
    w "It's not exactly something I'm proud of."
    show w regret with dissolve
    m neutral "I understand."
    m fabtalk "How often do you have them?"
    show w talk with dissolve
    w "Usually around once or twice a week."
    show w neutral with dissolve
    m talk "And is there any indication before it happens?"
    show w frusttalk with dissolve
    w "I would say I can tell when it's coming almost every time."
    show w frust with dissolve
    m serious "So you have some time to prepare for it?"
    show w sidetalk with dissolve
    w "My \"preparing\" is usually hurrying to my room if I'm not already there. I don't like people seeing any of that."
    show w frust with dissolve
    menu:
        "Why do you not want people to see you like that?":
            show w tensetalk with dissolve
            w "I don't think anyone in their right mind would want to be seen in such a state."
            show w frusttalk with dissolve
            w "Besides, sometimes the staff would intervene - I don't like how that turned out."
        "What's the likelihood of it happening here?":
            w "Umm..."
            show w talk with dissolve
            w "Low."
            show w tensetalk with dissolve
            w "Unless something happens that really, {i}really{/i} affects me."
        "If it happens here, what should I do?":
            $SilverHeart+=1
            show drk with Dissolve(0.75)
            show s 1 with dissolve
            show s 2 with Dissolve(1.0) 
            $renpy.pause(0.75, hard = True)
            hide s with dissolve
            hide drk with dissolve
            show w talk with dissolve
            w "If it theoretically happened here?"
            show w tense with dissolve
            m talk "That's right. In my office."
            show w angrytalk with dissolve
            w "You should leave me be. I know how to get through that and you don't."
            show w regrettalk with dissolve
            w "Besides, you could get hurt."
            show w frusttalk with dissolve
            w "It wouldn't be very smart to let me stay here if it happened."
            show w frust with dissolve
            "I don't like the idea of leaving him be when he needs my help the most... But I should take what he says into consideration."
    show w tense with dissolve
    "It's getting late."
    show w neutral with dissolve
    m flirt "Thank you for answering my questions today, William."
    show w sidetalk with dissolve
    w "It's that late already? I didn't realize..."
    show w neutral with dissolve
    "He gets up."
    show w talk with dissolve
    w "Well, goodbye, Dr. Hart."
    play sound "doorclose.ogg" fadein 1
    scene bg mc with dissolve
    stop music fadeout 4
    "He leaves my office."
    if sessions == 0:
        $firstpatient = "silver"
    $silverinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen easymeter
    hide screen silvermeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump silvernotes
        "No":
            pass
    jump breaknav
label silver3:
    scene bg mcdesk with dissolve
    show w neutral with dissolve
    play music "ost/neutral.wav"
    "William is back in my office."
    if easymeter: 
        show screen easymeter
        show screen silvermeter
    m conf "It's good to see you again."
    show w talk with dissolve
    w "Yeah... what are we doing today?"
    show w frust with dissolve
    "He seems to be in somewhat of a rush."
    menu:
        "Are you okay?":
            $personal +=1
            show w tense with dissolve
            "He glances at me."
            show w tensetalk with dissolve
            w "I'm fine. Can't you see?"
            show w frust with dissolve
            m fabtalk "I had some questions for today..."
        "Did something happen?":
            show w regrettalk with dissolve
            w "Um... last night."
            show w paintalk with dissolve
            w "I... don't want to talk about it."
            show w tense with dissolve
            m serious "Let me know if you change your mind. I'm here to help."
            show w frusttalk with dissolve
            w "I guess..."
            show w tense with dissolve
            m talk "I had some questions for today..."
        "I wanted to ask you something...":
            $professional+=1
            show w talk with dissolve
            w "Go on."
            show w neutral with dissolve
    m talk "On Monday, you said that you chose to be here."
    show w fear with dissolve
    w "I... said that?"
    show w frusttalk with dissolve
    w "If I did, it's true."
    show w frust with dissolve
    m fabtalk "Were you seeing a therapist before you got here?"
    show w frustsmile with dissolve
    "He chuckles."
    show w talk with dissolve
    w "No, the truth is actually quite far from that..."
    show w angry with dissolve
    w "I've never been treated for any mental illness before I got here."
    show w sidetalk with dissolve
    stop music fadeout 5
    w "To be honest, it didn't even occur to me for a while that I may be... affected."
    show w neutral with dissolve
    m talk "I see."
    m serious "What changed your mind, then?"
    play music "ost/tension.ogg" fadein 6
    show w regret with dissolve
    w "..."
    m talk "Tell me, William - what happened two years ago?"
    show w pain with dissolve
    w "..."
    show w hiden with Dissolve(1.0)
    w "I..."
    w "You don't want to know..."
    m angry "I need to."
    show w frusttalk with Dissolve(1.0)
    w "Why? Why do you need to know that?"
    show w angrytalk with dissolve
    w "Can't you just leave me be and let me rot here until I feel I've suffered enough and end my miserable existence?"
    show w angry with dissolve
    menu:
        "What?!":
            $wrong+=1
            m sjw "Did you really mean all of that?"
            show w sidetalk with dissolve
            w "And what do you think I meant?"
        "Stop right there.":
            $professional+=1
            m angrytalk "I don't like that trail of thought. You have some explaining to do."
            show w sidetalk with dissolve
            w "I'll explain all you want."
        "No.":
            $SilverHeart+=1
            show w neutral with dissolve
            m regrettalk "No, I can't leave you be. Not today and never until you can leave this place."
            show w shock with dissolve
            w "Excuse me?"
            show w fear with dissolve
            m angry "You've heard me right. I'm going to get you out of here one way or another."
            show drk with Dissolve(0.75)
            show s 1 with dissolve
            show s 2 with Dissolve(1.0) 
            $renpy.pause(0.75, hard = True)
            hide s with dissolve
            hide drk with dissolve
            show w sadtalk with dissolve
            w "You... you don't know what that'll take... you're just saying it to make a point."
    show w regret with dissolve
    m serious "William, whatever happened, you don't deserve to remain here for the rest of your life."
    show w frust with dissolve
    m angry "And you definitely don't deserve to die. Nobody does."
    show w angrytalk with dissolve
    w "You have no idea what you're talking about..."
    show w angry with dissolve
    m conf "I do. Trust me."
    show w regrettalk with dissolve
    w "I can't... not after what happened..."
    show w regret with dissolve
    m neu "William. Look at me."
    show w sad with dissolve
    m serious "Do I look like I would judge you for whatever happened two years ago?"
    show w regrettalk with dissolve
    w "[name]... You don't even know what you're trying to do..."
    show w regret with dissolve
    w "You're asking me to trust you - how can I if you don't trust {i}me{/i}?"
    show w tensetalk with dissolve
    w "I know what I've done and I know I shouldn't leave this place. You can't change it."
    show w tense with dissolve
    m fabtalk "Tell me then. It's the only way I can be convinced. What have you done?"
    show w pain with dissolve
    w "..."
    show w paintalk with dissolve
    w "I..."
    show w tensetalk with dissolve
    w "I've done something horrible."
    show w regrettalk with dissolve
    w "Something that... can't be undone."
    show w sadtalk with dissolve
    w "...or forgiven."
    show w regrettalk with dissolve
    w "All I can do to make up for it is to stay here and make sure it never happens again."
    show w pain with dissolve
    "...."
    show w frusttalk with dissolve
    w "There. Is that what you wanted to hear?"
    show w tense with dissolve
    m talk "As long as it's the truth, then yes."
    show w talk with dissolve
    w "Of course it is. I wouldn't lie about something like this."
    show w siden with dissolve
    menu:
        "What exactly have you done?":
            $wrong+=1
            show w regrettalk with dissolve
            w "...I can't tell you."
            show w frusttalk with dissolve
            w "You... you wouldn't understand."
            show w frust with dissolve
            "I may have pushed too far..."
        "And you think you deserve to die because of it?":
            $SilverHeart+=1
            show w angrytalk with dissolve
            w "I meant what I said. And I don't care if you don't agree with me."
            show w angry with dissolve
            show drk with Dissolve(0.75)
            show s 1 with dissolve
            show s 2 with Dissolve(1.0) 
            $renpy.pause(0.75, hard = True)
            hide s with dissolve
            hide drk with dissolve
            "Okay... this is bad."
            "So I'm dealing with someone who's definitely suicidal."
        "How horrible is it?":
            $SilverHeart+=1
            show w regrettalk with dissolve
            w "So horrible that... I can't sleep."
            show w tensetalk with dissolve
            w "I can't live knowing what I've done."
            show w sadtalk with dissolve
            w "It's that horrible."
            show w pain with dissolve
            show drk with Dissolve(0.75)
            show s 1 with dissolve
            show s 2 with Dissolve(1.0) 
            $renpy.pause(0.75, hard = True)
            hide s with dissolve
            hide drk with dissolve
            m regret "..."
    m regrettalk "William, I still truly believe that what you've done doesn't make you a bad person."
    m serious "I can help you move on from that."
    show w dis with dissolve
    w "I... I can't..."
    show w regrettalk with dissolve
    w "I can't move on..."
    show w sadtalk with dissolve
    w "If I do, I'll never... repent for what I've done."
    show w sad with dissolve
    "I see I've hit a wall here. It'll take a while for him to change that way of thinking..."
    m angry "From my point of view, it's not worth it. But I can't force you to change your mind about it."
    show w frustsmile with dissolve
    w "And from my point of view..."
    show w neutral with dissolve
    w "No, that quote's way too old."
    show w talk with dissolve
    w "You're right. You can't change my mind about it and therefore you won't."
    show w siden with dissolve
    "I don't think I can move this conversation any further until he trusts me enough to tell me the whole story."
    stop music fadeout 4
    "I should change the subject..."
    m fabtalk "Can I ask you about the attacks?"
    show w tense with dissolve
    play music "ost/neutral.wav" fadein 3
    w "Um... I guess."
    show w frust with dissolve
    menu:
        "Is there anything in particular that usually causes them?":
            show w tensetalk with dissolve
            w "I don't... think so..."
            show w sidetalk with dissolve
            w "They just... happen, most of the time."
        "How do you deal with them on your own?":
            $SilverHeart+=1
            show w tensetalk with dissolve
            w "I just... wait it out in my room."
            show w regrettalk with dissolve
            w "It only makes it worse when there's someone with me to worry about."
            show drk with Dissolve(0.75)
            show s 1 with dissolve
            show s 2 with Dissolve(1.0) 
            $renpy.pause(0.75, hard = True)
            hide s with dissolve
            hide drk with dissolve
        "How long does it last at a time?":
            show w talk with dissolve
            w "It depends."
            show w sidetalk with dissolve
            w "Sometimes it's over in some 15 minutes, but..."
            show w regrettalk with dissolve
            w "It can take me a few hours to calm down."
            show w tense with dissolve
            m neu "I see."
    stop music fadeout 4
    show w frust with dissolve
    w "...."
    show w angrytalk with dissolve
    w "I... don't think I've made myself clear."
    show w tensetalk with dissolve
    play music "ost/tension.ogg" fadein 4
    w "[name], I'm not a good person."
    w "You're wasting your time on me. I can't leave this place."
    show w sadtalk with dissolve
    w "It would be best if you just stopped seeing me."
    show w regrettalk with dissolve
    w "I won't tell anyone, so you won't get in trouble..."
    show w tensetalk with dissolve
    w "You just... need to leave me be."
    show w sadtalk with dissolve
    w "This may be your last chance to quit before there's no way out of it."
    w "Please. It's for the best."
    show w regrettalk with dissolve
    w "I'll just end up hurting you some way if you don't leave me..."
    show w tense with dissolve
    m gasp "I..."
    show w talk with dissolve
    stop music fadeout 6
    w "We're running out of time. I hope you take a moment to think about that before you consider seeing me again."
    play sound "doorclose.ogg" fadein 1
    scene bg mc with dissolve
    "Without another word, he stands up and leaves my office."
    "It takes me a while to get up and close the door behind him."
    "What should I do...?"
    if sessions == 0:
        $firstpatient = "silver"
    $silverinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen easymeter
    hide screen silvermeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump silvernotes
        "No":
            pass
    jump breaknav
label silver4:
    scene bg mc with dissolve
    play music "ost/hospital.wav" fadein 8
    "I've decided to keep seeing William every day, despite what he told me last time."
    "I think it's his illness that causes him to consider himself unworthy of my help. He really doesn't seem like a bad person."
    "...."
    "Normally, he would be here by now... Is something wrong?"
    if SilverHeart>=10:
        "I decide to check what happened."
        scene bg offices with dissolve
        stop music fadeout 4
        m fabtalk "William...?"
        "Maybe I really should go to look for him..."
        play music "ost/tension.ogg" fadein 8
        scene bg offices with vpunch
        m shock "Oh-!"
        if easymeter: 
            show screen easymeter
            show screen silvermeter
        show w full with dissolve
        "I notice him standing outside my office."
        m serious "What's wrong? Why are you here?"
        w "...."
        "He seems really unwilling to enter my office for some reason."
        "Now that I think about it, he looks quite shaken. Did something happen?"
        menu:
            "Is everything alright?":
                $personal +=1
                "He shakes his head. Of course it isn't..."
                m uncom "Do you mind entering? This conversation will be easier for both of us then."
                "He hesitantly complies and follows me into my office. I notice his hands trembling."
            "Come on, just go in":
                $wrong +=1
                w "I..."
                w "I can't..."
                w "...I'm sorry."
                hide w full with dissolve
                "Before I can reply, he turns around and leaves in a hurry. Oh."
                "I don't think it would do any good to chase after him now."
                "But... I should have time to see someone else before my break."
                stop music fadeout 4
                $silverinteract=3
                $firstpatient="silver"
                $sessions = 0
                jump patientchoice
            "Thank you for coming today":
                $SilverHeart+=1
                m serious "I know it wasn't easy for you. Please, come in."
                show drk with Dissolve(0.75)
                show s 1 with dissolve
                show s 2 with Dissolve(1.0) 
                $renpy.pause(0.75, hard = True)
                hide s with dissolve
                hide drk with dissolve
                "He looks at me, his eyes wide."
                w "[name]...?"
                "I open the door. He's not moving despite my attempts."
                "Should I..?"
                menu:
                    "{color=#fff1c1}Hold out my hand":
                        $SilverHeart+=1
                        $personal+=2
                        $Moonhandfriday = True
                        "To my surprise, he takes it without hesitation and follows me to my office."
                        "He only lets go once I lead him to my desk."
                        show drk with Dissolve(0.75)
                        show s 1 with dissolve
                        show s 2 with Dissolve(1.0) 
                        $renpy.pause(0.75, hard = True)
                        hide s with dissolve
                        hide drk with dissolve
                    "{color=#fff1c1}Invite him in":
                        $professional+=1
                        m neu "Do you mind going in?"
                        "He seems to have snapped out of his unusual state instantly."
                        "He follows me to my office without another word."
        scene mcdesk with dissolve
        if Moonhandfriday:
            show w tsun with dissolve
        else:
            show w regret with dissolve
        "He's silent for a while."
        m neu "William? Are you okay?"
        show w regrettalk with dissolve
        stop music fadeout 7
        w "I'm sorry... about what you saw just now."
        show w regret with dissolve
        m talk "There's nothing to be sorry for."
        show w tense with dissolve
        w "Are... you sure?"
        m conf "Absolutely sure."
        show w tensetalk with dissolve
        play music "ost/tran.ogg" fadein 8
        w "May I... start by saying something?"
        show w tense with dissolve
        m fabtalk "Of course. Go ahead."
        show w regrettalk with dissolve
        w "I... can't understand why you would want to see me again after what I told you last time."
        show w frusttalk with dissolve
        w "I thought I'd made myself clear when I said you shouldn't even consider talking to me anymore."
        show w tensetalk with dissolve
        w "It's... never turned out well when people got close to me."
        show w regrettalk with dissolve
        w "Please, don't let me deceive you - I can't be trusted."
        w "If you keep going like this I will ruin your life, I swear."
        show w regret with dissolve
        menu:
            "Why shouldn't I trust you?":
                show w sadtalk with dissolve
                w "Because I know things about myself that nobody else does. And these things make me not want to trust myself."
            "How exactly can you ruin my life?":
                show w sadtalk with dissolve
                w "I... I don't want to talk about it."
                show w regrettalk with dissolve
                w "But if you keep doing this, I'll have to warn you eventually."
            "You can't hurt me":
                show w tensetalk with dissolve
                w "I wish I could say the same with that much confidence..."
        show w regret with dissolve
        m pity "Everything will be okay, I'm sure of it."
        stop music fadeout 5
        show w frusttalk with dissolve
        w "I can't say I haven't warned you..."
        show w regrettalk with dissolve
        w "I- I won't feel responsible if you get hurt."
        play music "ost/neutral.wav" fadein 8
        show w regret with dissolve
        "I feel like he's lying to me right now."
        "...But I guess I should change the subject."
        m gasp "What happened earlier today? Was it an attack?"
        show w frust with dissolve
        w "Ummm..."
        show w pain with dissolve
        "He looks somewhat flustered."
        show w paintalk with dissolve
        w "Yes. Yes it was."
        show w tensetalk with dissolve
        w "I've... been having them more frequently than usual recently."
        show w tense with dissolve
        m uncom "Do you want to tell me about it?"
        show w frusttalk with dissolve
        stop music fadeout 4
        w "Not... particularly..."
        show w frust with dissolve
        m serious "Is there anything that could cause them to intensify? Do you have any idea what causes you such anxiety?"
        show w tense with dissolve
        w "...no. I don't."
        play music "ost/hospital.wav" fadein 8
        menu:
            "Is it about me?":
                $personal+=1
                show w angrytalk with dissolve
                w "W-What? Why would it be about {i}you{/i}?"
                show w frusttalk with dissolve
                w "You're just my psychologist. You're doing your job."
                show w frust with dissolve
                "True, but that doesn't mean I'm completely emotionally detached from him and vice versa."
            "Am I doing a bad job as your psychologist?":
                $personal+=1
                show w frusttalk with dissolve
                w "No, you're..."
                show w tensetalk with dissolve
                w "You're fine."
                show w tense with dissolve
                m smile "Thank you."
                "That makes me feel a bit better about myself, I guess."
            "Is it about your past?":
                show w frusttalk with dissolve
                w "Somewhat."
                show w regrettalk with dissolve
                w "You... you brought back some memories I never wished to revisit."
                show w frust with dissolve
        if Moonhandfriday:
            "I think back to the beginning of our session..."
            "He was so unlike himself then. He even took my hand when I meant to lead him to my office."
            "And it didn't even seem forced on his part - it felt like he'd been waiting for me to do that the whole time."
            m serious "William..?"
            show w talk with dissolve
            w "What is it?"
            show w neutral with dissolve
            m talk "Right before you entered my office, you took my hand and let me lead you inside."
            show w fear with dissolve
            stop music fadeout 3
            w "...oh."
            m angry "It seemed to have calmed you down somewhat."
            show w regret with dissolve
            m fabtalk "So I guess what I'm asking is - does it actually help you?"
            play music "ost/tension.ogg" fadein 7
            show w angrytalk with dissolve
            w "No-"
            show w frusttalk with dissolve
            w "And even if it did - who are you to do such things without my consent?"
            show w frust with dissolve
            m "If I hadn't had your permission, you wouldn't have taken my hand when I asked."
            show w tensetalk with dissolve
            w "That doesn't really... count. I don't expect myself to be capable of making rational decisions when I'm like this."
            show w regret with dissolve
            m serious "If that's so, then I'm sorry to have done that."
            show w tense with dissolve
            stop music fadeout 5
            "He looks hesitant."
            m conf "But if you think it could help, don't worry about me. As long as it benefits you somehow, I'm fine with it."
            pause 1
            play music "ost/tran.ogg" fadein 6
        show w regret with dissolve
        m serious "William... I feel like we need to discuss one more thing today."
        show w talk with dissolve
        w "Yes?"
        show w angry with dissolve
        m "I... don't want to rush you, but... if you want to give me a chance to help you, I'll need to know what caused you to be that way."
        m fabtalk "Along with everything else from your past that may have affected you."
        show w frust with dissolve
        m angry "...and that also means learning what happened two years ago."
        stop music fadeout 6
        show w pain with dissolve
        w "...."
        "He shifts in his seat."
        m serious "I know it won't be easy, but I'll need you to trust me. I don't mean you harm."
        show w tense with dissolve
        w "...."
        m "I have to ask - do you trust me after this one week?"
        show w tensetalk with dissolve
        w "I..."
        play music "ost/tension.ogg" fadein 8
        show w frust with dissolve
        w "If I didn't, I wouldn't have come here today. Not after what happened yesterday and what I told you."
        show w frusttalk with dissolve
        w "I warned you and you didn't listen. I thought..."
        show w regrettalk with dissolve
        w "I thought that I would hurt you because of that. I... I don't want to."
        show w paintalk with dissolve
        w "I broke this morning. I'm not even scared to admit that now, because it's true. And you did this to me."
        show w regrettalk with dissolve
        w "But I understand why you wouldn't believe me when I warned you. Why would anyone even care what I say to them?"
        show w paintalk with dissolve
        w "So I shouldn't have been surprised to hear you wanted me here again. I just wasn't prepared for it."
        show w angrytalk with dissolve
        w "Do you think I would drag myself here in the state I was in this morning for someone I didn't even trust to be at least remotely competent?"
        show w angry with dissolve
        "I'm not sure what to say..."
        stop music fadeout 5
        m sadsmile "I... I really appreciate you coming here today, despite everything."
        show w siden with dissolve
        m smile "It makes me really happy to hear that you trust me that much already."
        show w sidetalk with dissolve
        play music "ost/neutral.wav" fadein 8
        w "Heh, of course it does. That way you can keep disrespecting my wishes and dragging me here every single day."
        show w talk with dissolve
        w "That's the plan, isn't it?"
        show w angry with dissolve
        m regret "William... It's not like that."
        m regrettalk "I only want to help you."
        show w sidesmile with dissolve
        w "Whatever you say, Dr. Hart."
        show w angrytalk with dissolve
        w "No matter what conclusions you may be drawing now, I am {i}not{/i} okay with this."
        show w angry with dissolve
        m angry "If you want to remain in this hospital, you have to meet me regularly. That's the point."
        show w frusttalk with dissolve
        w "I know..."
        show w talk with dissolve
        w "I guess I was just hoping you'd be more like the others."
        show w frust with dissolve
        w "They never really... tried to do anything with me."
        show w tensetalk with dissolve
        w "And you... you seem to have some goal, some purpose to what you're doing. And I really don't like that."
        show w regrettalk with dissolve
        w "Because it means I may get out of here sooner than I should."
        show w regret with dissolve
        stop music fadeout 6
        m uncom "Tell me, is it just about making up for the past? If I managed to help you with your illness, you'd be perfectly capable of living outside this place..."
        show w frusttalk with dissolve
        w "It's not that simple..."
        play music "ost/tran.ogg" fadein 8
        show w regrettalk with dissolve
        w "I'm also here because... I don't want what happened two years ago to occur again."
        show w tensetalk with dissolve
        w "And my illness has nothing to do with that."
        show w tense with dissolve
        "Interesting... So it's more complex than I assumed."
        show w regrettalk with dissolve
        w "You can't fix the reason I'm here. Nobody can."
        show w regret with dissolve
        stop music fadeout 6
        menu:
            "Why can't I?":
                $personal+=1
                show w frusttalk with dissolve
                w "Because..."
                show w dis with dissolve
                w "{i}...because it's me!"
                show w shock with dissolve
                w "I'm the only cause of everything that happened."
                show w frust with dissolve
                w "The only way to really erase the problem would be..."
                show w dread with dissolve
                w "{i}{color=#ffffff}...to kill me."
                show w pain with dissolve
                "...."
            "You need to tell me the truth":
                $SilverHeart+=1
                show w shock with dissolve
                w "N-No... Please, don't make me tell you about it..."
                show w dis with dissolve
                w "You... you don't want to have anything to do with it. Trust me."
                show w regrettalk with dissolve
                w "Nobody deserves that."
                show w pain with dissolve
                show drk with Dissolve(0.75)
                show s 1 with dissolve
                show s 2 with Dissolve(1.0) 
                $renpy.pause(0.75, hard = True)
                hide s with dissolve
                hide drk with dissolve
                m regret "...."
            "Let me at least fix your illness then":
                $professional+=1
                show w frusttalk with dissolve
                w "I... I suppose there's no harm in that..."
                show w talk with dissolve
                w "Though I'm not sure if you can help me even with that."
                show w pain with dissolve
        play music "ost/neutral.wav" fadein 8
        "We're short on time."
        m fabtalk "I hope you rethink everything we talked about this week."
        m conf "If you're willing to come here on Monday, I'll gladly see you again."
        show w neutral with dissolve
        m pity "And whenever you're just not feeling it for some reason, don't worry about it - I won't force you."
        show w talk with dissolve
        w "Alright then. Is... that all? I think I should be leaving now."
        show w neutral with dissolve
        "He's right. I follow him to the door."
        show w regrettalk with dissolve
        w "Once again, I really apologize for earlier today. I'll see you next week, Dr. Hart."
        play sound "doorclose.ogg" fadein 1
        scene bg mc with Dissolve(0.7)
        "I watch him leave my office."
        "I chose to spend every session I could with him... what is it about him that draws me to him that much?"
        "Maybe it's pity. Maybe it's the overwhelming feeling that if I don't do anything now, it might be too late soon."
        "After all, he appears to be particularly... endangered."
        "He seems to have so many feelings he can't deal with... fear, shame, guilt..."
        "And pain. definitely."
        "If none of his previous psychologists managed to help, I need to be the one to stop this."
        stop music fadeout 4
        "This man has suffered long enough. I'm determined to help him leave this place for good."
    else:
        play sound "knock.ogg" fadein 0.5
        m conf "Come in."
        show su neutral:
            ypos 0.1
            xpos 0.35
        with dissolve
        "Oh... it's just a nurse."
        if SunLink>0:
            show su talk with dissolve
            sue "Hey, I'm sorry to bother you, but William really wasn't willing to cooperate today."
            show su sad with dissolve
            sue "We, uh... couldn't get him to get out of his room."
            show su neutral with dissolve
            m talk "I... see."
            m serious "Is there anything I can do to help?"
            show su sadsmile with dissolve
            sue "Not really... when he's like this, there's really nothing we can do."
            show su talk with dissolve
            sue "Well... I just came to let you know what happened."
            show su neutral with dissolve
            m conf "Thank you."
            show su sadsmile with dissolve
            sue "I'm sorry about that. You tried your best."
            show su sad with dissolve
            m serious "Shouldn't you be going now? I wouldn't want to take up too much of your time..."
            show su smile with dissolve
            sue "Don't worry about me~"
            show su neutral with dissolve
            sue "Are you sure you'll be fine? I don't think anyone will blame you if you take a break until your next scheduled session."
            m gasp "You think so?"
            show su smile with dissolve
            sue "Absolutely. You've done all you can."
        else:
            $SunLink = 1
            show su sadtalk with dissolve
            gu "Um... I'm supposed to tell you that... your patient wasn't willing to cooperate today."
            stop music fadeout 6
            show su talk with dissolve
            gu "We... couldn't get him to get out of his room."
            show su sad with dissolve
            gu "I'm sorry it took such a long time to inform you - we weren't sure what to do about it."
            m serious "You, um... You could've told me sooner. Do you think I could help?"
            show su talk with dissolve
            play music "ost/tension.ogg" fadein 6
            gu "Uh... I don't think so. It's one of these things you just have to wait out."
            show su neutral with dissolve
            "Sounds simple enough. As long as it's nothing serious, I don't want to pressure him to see me."
            m "Shouldn't you be going now? I mean..."
            show su smile with dissolve
            gu "Don't worry about me."
            show su talk with dissolve
            stop music fadeout 6
            gu "But, since it took us so long to inform you... which I'm still sorry for... there's no point starting another session now."
            show su neutral with dissolve
            "She's right. I would only have about half the time if I started now."
            show su talk with dissolve
            play music "ost/hospital.wav" fadein 8
            gu "Umm... you're the psychologist I showed around the hospital last Sunday?"
            show su neutral with dissolve
            m conf "That's me."
            show su smile with dissolve
            gu "I never got to know your name. Now that you have nothing to do... I guess we could use this to our advantage."
            show su happy with dissolve
            gu "I'm Sue Peters. Nice to meet you."
            $suename="Sue"
            show su smile with dissolve
            m fabtalk "[name] Hart. Thanks for... trying to make me feel better about it."
            show su sadsmile with dissolve
            sue "I don't think it's your fault, [name]. Some patients are just... more difficult to help than the others."
            show su talk with dissolve
            sue "Um, I should be going now..."
            show su smile with dissolve
            sue "If you ever want to talk, you can find me in the central hall on your break."
        hide su with dissolve
        "Sue leaves my office. At least her presence is comforting, after learning of my failure with William."
        "I mean... maybe it wasn't a failure. Maybe he wouldn't want to see me today anyway."
        "Yes, let's keep telling myself that. I don't know what to think about it."
        stop music fadeout 4
        "I spend the time until my break in the office."
    if sessions == 0:
        $firstpatient = "silver"
    $silverinteract += 1
    $sessions += 1
    show drk with dissolve
    hide screen silvermeter
    hide screen easymeter
    "Should I make notes about what I've learned today?"
    menu:
        "Yes":
            jump silvernotes
        "No":
            pass
    jump breaknav