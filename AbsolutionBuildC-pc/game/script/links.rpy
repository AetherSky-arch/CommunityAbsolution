default EmpLink=0

image yback 1 = "cg/y1.png"
image yback 2 = "cg/y2.png"
image yback 3 = "cg/y3.png"
image yback 4 = "cg/y4.png"

image nback 1 = "cg/n1.png"
image nback 2 = "cg/n2.png"
image nback 3 = "cg/n3.png"
image nback 4 = "cg/n4.png"

label links:
    if SunLink > 0 or TempLink > 0 or StarLink > 0:
        menu:
            "Who will I spend time with on my break?"
            "Sue" if SunLink > 0:
                if SunLink == 1:
                    jump sun1
                elif SunLink == 2:
                    jump sun2
                elif SunLink == 3:
                    if TempLink>1:
                        jump sun3
                    else:
                        "I should talk to Julia before telling Sue I fulfilled her request."
                        jump links
                else:
                    jump sunafter
            "Julia" if TempLink > 0:
                if TempLink == 1:
                    jump temp1
                if TempLink == 2:
                    jump temp2
                if TempLink == 3:
                    jump temp3
                else:
                    jump tempafter
            "The psychiatrist" if StarLink > 0:
                if StarLink == 1:
                    jump star1
                if StarLink == 2:
                    jump star2
                else:
                    jump starafter
            "Elizabeth" if PrsLink>0 and month==1 and day<6:
                if PrsLink == 1:
                    jump prslink1
                elif PrsLink == 2:
                    jump prslink2
                elif PrsLink == 3:
                    jump prslink3
    elif month==1 and day<6 and PrsLink>0:
        menu:
            "Who will I spend time with on my break?"
            "Elizabeth":
                if PrsLink == 1:
                    jump prslink1
                elif PrsLink == 2:
                    jump prslink2
                elif PrsLink == 3:
                    jump prslink3
### SUN SOCIAL LINK ###################
label sun1:
    if route=="golden":
        pass
    else:
        scene black with dissolve
        "I remember that Sue told me to look for her in the central hall the first time we met."
        "I haven't seen her since then, so thought it would be good to see her again."
        "Especially since I don't have much to do on my breaks."
        scene bg central with dissolve
        play music "ost/sunny.wav" fadein 5
        "Standing by a window, I wait, hoping to see the familiar nurse emerge from one of the doors."
        scene bg central with hpunch
        sue "Hey, it's you!"
        "I turn around, startled by the sound of Sue's loud voice."
        show su cute with moveinright
        m flirt "Hi."
        show su happy with dissolve
        sue "How's work?"
        show su smile with dissolve
        "I open my mouth to reply..."
        show su talk with dissolve
        sue "Hang on..."
        show su sadtalk with dissolve
        sue "You weren't... in a hurry or anything?"
        show su neu with dissolve
        "That didn't even cross my mind..."
        m pity "No, I was actually waiting for you."
        show su happy with dissolve
        sue "Oh, so you wanted to talk?"
        show su laugh with dissolve
        sue "I have time as usual, so..."
    show su smile with dissolve
    sue "What did you want to talk about?"
    menu:
        "How are you?":
            $empathy += 1
            show su cute with dissolve
            sue "Everything's fine, as always."
            show su happy with dissolve
            sue "Hehe~"
            show su smile with dissolve
            m smile "That's good to hear."
        "Did anything interesting happen in the hospital?":
            show su talk with dissolve
            sue "Hmm... let me think..."
            show su neutral with dissolve
            sue "No, not really. Everything's been normal."
    show su neutral with dissolve
    "Sue looks out the window we're standing by..."
    sue "The sky looks lovely today."
    m fabtalk "You think so?"
    show su smile with dissolve
    sue "I like warm days like these... and the sun looks pretty, too... Makes me feel hopeful."
    show su talk with dissolve
    sue "Like..."
    show su smile with dissolve
    sue "Even when I feel kind of down, I look at the sky and it's always the same."
    sue "Shining. Peaceful..."
    show su neutral with dissolve
    "She looks at me suddenly."
    sue "Sorry. I didn't mean to space out like that..."
    sue "It just happens to me sometimes."
    menu:
        "A bit of an airhead?":
            show su smile with dissolve
            sue "Sorry about that, heh~"
        "That's pretty cute":
            show su gasp with dissolve
            sue "C-Cute?"
            show su happy with dissolve
            sue "You're so funny, hehe~"
        "{color=#67beea}Look out the window":
            scene bg sun with dissolve
            "I walk past her and look out the window."
            "Now I'm the one spacing out..."
            m smile "You're right. It is nice outside."
            scene bg central with dissolve
    show su smile with dissolve
    sue "So how are you handling your new job?"
    menu:
        "I like my patients":
            $empathy += 1
            sue "You do? That's great!"
            sue "How many of them do you have?"
            m fabtalk "Four, but I was told I'd get more eventually."
            show su neutral with dissolve
            sue "That's a reasonable number... It's hard to bond with more than four people at once, I think."
            m angry "\"Bond\"?"
            show su gasp with dissolve
            sue "Isn't it what psychologists do? You should let them trust you and see you as their friend before they can be helped."
            show su smile with dissolve
            sue "I think to be a good psychologist, you should first be able to make friends. And by that I mean be really good at it."
            show su happy with dissolve
            sue "That's just my opinion, though~"
            show su smile with dissolve
        "It's better than I expected":
            sue "That's always a good thing."
            show su talk with dissolve
            sue "You know, I never expected to like this hospital as much as I do."
            show su neutral with dissolve
            sue "But as soon as I came here, I started to feel like the people here really need someone like me, someone who can just smile and make them feel better."
            show su smile with dissolve
            sue "Like the sun, right?"
        "I think I'll last some time here...":
            sue "I'm sure you'll get used to this place soon."
            show su happy with dissolve
            sue "I can show you around, introduce you to some of my friends among the staff, whatever you need."
            show su smile with dissolve
            sue "I'll be glad to help if it makes you feel more comfortable here."
            sue "So you can talk to me whenever you want."
        "I don't feel good about this job...":
            show su sad with dissolve
            sue "Oh..."
            show su sadtalk with dissolve
            sue "I'm so sorry to hear that..."
            sue "I've always liked it here, so I can't really relate to that..."
            show su smile with dissolve
            sue "Regardless, if there's anything I can do to help, just let me know~"
            m pity "Thanks."
            show su sadsmile with dissolve
            sue "Yeah... the least I can do is try, right?"
            m smile "practice makes perfect, Sue."
    "She laughs, and I can't help but smile back."
    "I can tell Sue is really trying her best to make everyone here happy."
    "Just like me, in some way."
    "I think our bond has deepened today..."
    show su happy with dissolve
    sue "Anyway, I'm sure you'll do great here."
    sue "You..."
    show su gasp with dissolve
    gu "Sue? Oh, there you are."
    "A nurse emerges from behind Sue, and places her hand on her shoulder."
    show su talk with dissolve
    sue "What is it?"
    gu "We need someone near room XIX... you're free, right?"
    show su smile with dissolve
    sue "Yeah, I'll be there."
    if route == "golden":
        "Turns out she wasn't done with her tasks..."
    else:
        gu "Thanks a lot. I was just on my way out."
    "The nurse leaves, and Sue turns to me with an apologetic smile."
    show su talk with dissolve
    sue "Well, it looks like a busy day for me..."
    show su sadsmile with dissolve
    sue "Sorry about that, [name]. I'll see you later ~"
    hide su with moveoutright
    stop music fadeout 6
    "She disappears into the patient rooms hallway."
    "What a busy nurse..."
    $SunLink += 1
    if route == "golden":
        scene black with dissolve
        "I make my way upstairs and spend the rest of the day resting in my room."
        jump nextday
    else:
        "I realize I only have a couple minutes until the end of my break, so I head back to my office."
        scene black with dissolve
        "Sue seems like a genuinely nice person. I should hang out with her again sometime."
    jump patientchoice
    
label sun2:
    scene black with dissolve
    "I've decided to see Sue again."
    scene bg central with dissolve
    play music "ost/sunny.wav" fadein 5
    show su neutral with dissolve
    "She's standing on her own in the central hall, looking down at her feet."
    "She looks somewhat less cheerful than usual."
    m conf "Hi."
    show su gasp with vpunch
    sue "Oh-"
    show su happy with dissolve
    sue "Hello, [name]~"
    show su smile with dissolve
    menu:
        "Having a bad day?":
            "She shakes her head."
            show su talk with dissolve
            sue "No, it's not like that..."
        "Am I disturbing you?":
            show su cute with dissolve
            sue "Not at all."
        "Were you waiting for someone?":
            $empathy += 1
            show su talk with dissolve
            sue "Yeah... I was."
    show su neu with dissolve
    sue "Earlier today, I asked a friend to meet me here, but it turns out she's busy..."
    show su smile with dissolve
    sue "On a positive note - I guess I have time to talk to you now."
    show su gasp with dissolve
    sue "I have an idea."
    show su happy with dissolve
    sue "Mind if we take a bit of a walk?"
    show su smile with dissolve
    menu:
        "Sure, follow me!":
            "I lead Sue out of the central hall."
            show bg cafe with dissolve
            "We somehow end up in the cafeteria and take a seat by one of the empty tables."
            sue "Ah, much better~"
        "No problem, lead the way":
            $empathy += 1
            "I follow Sue out of the central hall."
            show bg cafe with dissolve
            "We somehow end up in the cafeteria and take a seat by one of the empty tables."
            sue "Ah, much better~"
        "Can we not..?":
            m serious "I'm tired..."
            show su sadtalk with dissolve
            sue "Okay then..."
            sue "We can stay here."
    show su talk with dissolve
    sue "I wanted to ask you something since last time..."
    show su gasp with dissolve
    sue "Do you remember Julia?"
    show su neutral with dissolve
    menu:
        "The receptionist?":
            sue "Exactly. You saw her right after you entered the hospital the day you were hired."
        "That nurse?":
            sue "Right, she's a nurse like me."
        "Ponytail...?":
            show su smile with dissolve
            sue "And green eyes, you got it right."
        "No, I don't":
            sue "Before we met, you talked to her in the reception."
            m gasp "Oh... I think I remember..."
    show su talk with dissolve
    sue "Anyway..."
    sue "I'm friends with her, and..."
    show su sadtalk with dissolve
    sue "She's the one I was supposed to meet today."
    show su smile with dissolve
    sue "T-that didn't work out, but it's fine..."
    show su talk with dissolve
    sue "The point is."
    show su neu with dissolve
    sue "I don't know how to put it, but..."
    show su sadsmile with dissolve
    sue "We're friends, right?"
    show su neu with dissolve
    sue "Because I have something to ask of you."
    m talk "I'm listening."
    show su sad with dissolve
    sue "I'm worried about Julia recently..."
    sue "She seems to be bothered by something, and she's not telling me... Maybe she doesn't want to worry me, but still."
    show su sadtalk with dissolve
    sue "I think she's taking too much responsibility..."
    sue "Like today."
    show su talk with dissolve
    sue "She got some last-minute call from another nurse and had to replace her."
    show su neu with dissolve
    sue "I could've helped her if she asked, but she only informed me afterwards."
    show su sad with dissolve
    sue "She doesn't seem happy at work at all... It used to be different."
    show su gasp with dissolve
    sue "I wanted to ask you - could you maybe talk to her sometime?"
    show su cute with dissolve
    sue "You're good with people, so who knows - she might tell you what bothers her."
    show su smile with dissolve
    sue "She might be a bit... harsh at first, but please give her a chance."
    sue "You'll do it for me, right?"
    menu:
        "I'll talk to her as soon as I can":
            $empathy += 1
            show su laugh with dissolve
            sue "Thank you so much~"
            show su happy with dissolve
            sue "You have no idea how much this means to me."
            show su smile with dissolve
        "I'll try...":
            show su happy with dissolve
            sue "Hey, that's all I was asking for."
            show su cute with dissolve
            sue "Thank you~"
        "I don't think I can":
            show su sadtalk with dissolve
            sue "Is... that so...?"
            show su smile with dissolve
            sue "Well, if you change your mind, it'll make me very happy~"
    "If I choose to accept Sue's request, I can look for Julia in\nthe {color=#a2ef83}NURSES' OFFICE{/color} on the second floor from now on."
    show su happy with dissolve
    sue "Well then... That's just something I wanted you to consider. Thanks for listening."
    show su neutral with dissolve
    "I realize my break is halfway over."
    "Sue seems to notice that as well."
    show su sad with dissolve
    sue "I was so busy talking about my problems I didn't let you say anything..."
    show su smile with dissolve
    sue "Did you want to ask me something?"
    "I consider my options, and come up with two questions."
    menu:
        "Do you have friends outside of work?":
            sue "I do."
            sue "You know, back from school, neighbors..."
            "Sue definitely seems like the type of person to attract people to herself."
            show su happy with dissolve
            sue "You could say I'm quite popular."
            show su laugh with dissolve
            sue "Hehe~"
            show su smile with dissolve
            "We spend a while chatting..."
        "Are you an only child?":
            $empathy += 1
            show su sadsmile with dissolve
            sue "Actually, I am... I always wanted to have siblings, though."
            show su gasp with dissolve
            sue "Do you?"
            show su smile with dissolve
            "Jane..."
            m boretalk "I... used to."
            show su sadtalk with dissolve
            sue "Oh my god, I'm so sorry... I had no idea, I shouldn't have asked..."
            show su sad with dissolve
            m pity "It's fine, really..."
            "A moment of unsettling silence follows my last sentence."
            "Regardless, I feel like I've opened up a bit to Sue, even if it was by accident."
    show su sadtalk with dissolve
    sue "Sorry about taking up your whole break..."
    show su sadsmile with dissolve 
    m gasp "Oh. It's over already?"
    "She nods."
    show su smile with dissolve
    sue "I can walk you back to your office."
    menu:
        "Let's go":
            show bg offices with dissolve
            "Sue reads the label on my office."
            show su talk with dissolve
            sue "[name] Hart, huh..? I didn't actually know your full name."
            show su smile with dissolve
            m talk "What's yours?"
            sue "Sue Peters. But hey, most people call me by my first name anyway~"
            $persistent.Suelast = "Peters"
            "She looks curiously at the door."
            show su gasp with dissolve
            sue "This is the red one, right?"
            show su smile with dissolve
            sue "The office, I mean."
            m fabtalk "It is..."
            show su laugh with dissolve
            sue "At least it suits you color-wise in a way, huh?"
            show su cute with dissolve
            "I never thought of that... She's right..."
        "I'll be fine":
            show su neutral with dissolve
            sue "If you say so..."
            show su smile with dissolve
            sue "I'll be on my way, then."
    m flirt "It was nice to see you again."
    show su laugh with dissolve
    sue "Likewise~"
    show su smile with dissolve
    "She turns to leave."
    stop music fadeout 6
    show su gasp with dissolve
    sue "Oh, and remember about Julia, alright?"
    scene black with dissolve
    "We part and my break is over."
    "I should see Julia and then talk to Sue to let her know what I learned."
    $SunLink += 1
    $TempLink = 1
    jump patientchoice

label sun3:
    $SunLink+=1
    play music "ost/sunny.wav" fadein 6
    scene bg central with dissolve
    "I decided to see Sue again."
    "After talking to Julia, I feel like I've fulfilled her request."
    "I notice her standing in her usual spot."
    show su neutral with dissolve
    m cute "Hi, Sue."
    show su gasp with dissolve
    sue "Hello ~"
    show su cute with dissolve
    sue "I didn't see you there, heh."
    m smile "I spoke to Julia, like you asked me to. I think we're off to a great start."
    show su gasp with dissolve
    sue "Really? What did she say?"
    show su smile with dissolve
    m happy "She said that if I ever want to spend time with her on my break, we could hang out again."
    show su laugh with dissolve
    sue "That... makes me so happy, [name] ~ Thank you so much, I knew you could make friends with her!"
    show su sadsmile with dissolve
    "It's heartwarming to see her this happy because of something I did."
    m conf "It's not that big a deal, Sue, really..."
    show su neutral with dissolve
    sue "It is for me."
    stop music fadeout 4
    show su neu with dissolve
    sue "...."
    show su sadtalk with dissolve
    sue "There's... another reason why I asked you to do this..."
    show su angry with dissolve
    m talk "What is it?"
    play music "ost/emo.wav" fadein 5
    show su sad with dissolve
    sue "I... I'm really sorry I haven't told you about it earlier... I thought you'd refuse if you knew..."
    "...huh?"
    "What could Sue possibly be hiding from me?"
    show su neu with dissolve
    sue "I... I wanted to trust you."
    show su sadsmile with dissolve
    sue "I know it sounds silly, me needing a reason to trust you when we're already friends, but..."
    show su gasp with dissolve
    sue "A-And I really wanted to trust you. I did! It's just that..."
    show su sadtalk with dissolve
    sue "Some things... they can't be undone. I'm sorry."
    show su sad with dissolve
    menu:
        "What happened?":
            $professional+=1
            "She takes a deep breath."
            show su talk with dissolve
            sue "Right... you should know."
        "It's okay, don't worry":
            $empathy+=2
            $personal+=1
            show su gasp with dissolve
            sue "It's not about you, I swear-"
            show su neutral with dissolve
            sue "Umm..."
            show su neu with dissolve
            sue "...thanks for being so nice to me about it - I know I shouldn't keep secrets."
        "It's not about me, is it?":
            $personal+=2
            sue "No no, it's not about you at all."
            sue "It's stupid, really."
    show su sadtalk with dissolve
    sue "The truth is..."
    show su talk with dissolve
    sue "Remember how when you were hired, it was because one of our psychologists left?"
    show su neu with dissolve
    sue "Well..."
    show su sad with dissolve
    sue "That psychologist was my friend. We would spend breaks together, just like we do now."
    show su sadsmile with dissolve
    sue "And... I liked him. I really did. I thought he was a good friend."
    show su smile with dissolve
    sue "He always seemed so kind to his patients, the staff, everyone."
    show su neutral with dissolve
    sue "But... I was stupid. He had us all fooled."
    stop music fadeout 6
    m gasp "What did he do?"
    show su sadtalk with dissolve
    sue "It all started when we hired a new night guard... It was two years ago."
    scene black with dissolve
    sue "I didn't talk to him much, didn't really see him around - night guards are like that."
    show nback 1 with dissolve 
    play music "ost/memory.ogg" fadein 6
    sue "But... then one day I saw him going to Dr. Sharpe's office in the morning. He seemed... mad."
    sue "I heard that guard yelling, accusing him of all these horrible things..."
    sue "He was out of line and honestly kind of scary."
    sue "I saw my psychologist friend later that day."
    sue "He... he said such strange things... It sounded almost like he agreed with that lunatic from before."
    sue "He said he's going to help him, that he'll ask his patients about these ridiculous accusations, see if anyone knows something."
    sue "I... don't know much about psychology, but I don't think he should make his patients anxious by suggesting any of that was real."
    sue "I mean, that night guard talked about... drugs, breaking in at night, m-murder even."
    m wut "Murder?"
    sue "I was shocked, too. I thought he of all people would know how ridiculous that sounded."
    sue "I wanted to convince him not to believe that shady guy, but... I think it was too late."
    m confusion "Too late? How?"
    sue "The next day I tried to talk to him again. He seemed... angry."
    show nback 2 with dissolve 
    sue "He told me he found a patient of his who could back up the guard's claims, but she was taken to XXI."
    sue "She had to be isolated, you see - she was in a very bad shape."
    m sad "What happened to her?"
    sue "She was... a fragile one. Had some anxiety disorder, kept... seeing things, thinking everyone was a threat to her."
    sue "And that day, she woke up screaming. I'd never seen her this afraid. We were worried she would harm herself, so we isolated her."
    m sjw "And he was mad about that? Didn't he care about her safety?"
    scene black with dissolve
    sue "He... seemed more concerned about proving that night guard was telling the truth."
    m confusion "Why would he believe him?"
    sue "I had no idea at the time."
    sue "But... the worst thing of all was just about to happen."
    sue "It was the day after we let that girl out of XXI, back into her own room."
    sue "We... thought she would be okay by then."
    sue "...."
    "She seems anxious, but continues before I can say anything."
    sue "I was doing my morning round of the patients' rooms hallway."
    sue "When- when I looked into her room, I-"
    "Her voice cracks."
    m regrettalk "Sue, if you can't talk about it, it's -"
    stop music 
    sue "No. You need to know."
    play music "ost/rev.ogg"
    show nback 3 with hpunch
    sue "She was dead."
    m freeze "!!!"
    sue "I- I found her there. Stabbed to death."
    sue "It was... it was {i}so horrible, [name]..."
    if le:
        m uncom "...."
    else:
        m sadtalk "I'm so sorry..."
    "I have no idea what else to say."
    m talk "How did it happen? She shouldn't have had access to anything dangerous."
    sue "The knife, it... must've come from outside of the hospital."
    sue "It happened at night... Someone gave it to her and..."
    sue "He made her do it. It must have been him."
    sue "They were close. I don't... think it was difficult for him to manipulate her."
    m fabtalk "What did the police say?"
    sue "They found nothing. Other than traces of some illegal drug in her blood."
    sue "The night guard claimed it was smuggled into the hospital by the staff."
    m angrytalk "Why would anyone do that?"
    sue "The drugs, they... the police found them. They said the nightguard must have smuggled them."
    sue "Everyone here thought the psychologist was the mastermind, but they found no evidence to link them."
    sue "Until three months ago."
    scene black with Dissolve(1.0)
    stop music fadeout 6
    sue "We were all... sick and confused. Devastated."
    sue "We just wanted that nightmare to end... Me especially."
    scene bg central with dissolve
    m talk "Is that why you didn't trust me at first?"
    show su sad with dissolve
    play music "ost/ship.wav" fadein 6
    "She nods."
    show su sadtalk with dissolve
    sue "I... kept thinking about that psychologist... He seemed so kind at first, I..."
    show su angry with dissolve
    sue "I didn't know if I could trust anyone for a while."
    show su sad with dissolve
    sue "Especially when I learned they hired you in his place, I..."
    show su talk with dissolve
    sue "...it's stupid, I know."
    show su sad with dissolve
    if le:
        "I can't argue with that."
    elif he:
        m sad "It's not. You were afraid. Everyone must've been."
    else:
        "It makes sense now that I know what happened."
    show su sadtalk with dissolve
    sue "How could anyone hurt someone like that..?"
    sue "That girl... she was so young... She had a whole life to live..."
    sue "If it weren't for these monsters, she'd be out of here by now."
    show su angrytalk with dissolve
    sue "How can people be this cruel..?"
    show su sad with dissolve
    "She sobs."
    sue "...."
    "A while passes in silence."
    show su sadsmile with dissolve
    sue "Sorry, I... I got a little emotional..."
    menu:
        "Thank you for telling me about it":
            $professional+=1
            show su gasp with dissolve
            sue "Oh?"
            show su smile with dissolve
            sue "I feel like... it's been sitting there for a while. At the back of my mind."
            show su sadtalk with dissolve
            sue "And... you're new, so you had no idea. I had to tell you that."
        "It's fine":
            show su cute with dissolve
            "She laughs."
            show su smile with dissolve
            sue "Yeah. I know."
        "{color=#67beea}Hug her" if he:
            $personal+=2
            $suehug=True
            "I hug Sue. I can't help it."
            show su gasp with dissolve
            sue "Huh?"
            show su laugh with dissolve
            sue "Oh, [name], you really didn't have to..."
            "She laughs."
            show su smile with dissolve
            sue "...thanks."
            show su sadsmile with dissolve
            sue "It really feels like I've made a friend."
            "I let go of her with a smile."
            m cute "Anytime."
    stop music fadeout 5
    show su neu with dissolve
    "...."
    show su sadsmile with dissolve
    sue "Oh gee, that took up your whole break..."
    m gasp "Really?"
    show su smile with dissolve
    "I check the time. I should get going."
    show su cute with dissolve
    m flirt "See you around, Sue ~"
    scene black with dissolve
    "I wave at her before disappearing in the offices hallway."
    jump patientchoice
    
label sunafter:
    scene black with dissolve
    "I spent the break with Sue."
    jump patientchoice
    
### JULIA #############################
#######################################
label temp1:
    $TempLink+=1
    scene black with dissolve
    "I decide to do what Sue's asked me to and find Julia."
    scene bg central with hpunch
    show jl angrytalk with dissolve
    jl "Hey! Watch it!"
    play music "ost/sunny.wav" fadein 6
    show jl angry with dissolve
    "I nearly crashed into her in the doorway. Great."
    "Well, at least I found her."
    show jl talk with dissolve
    jl "Aren't you that psychologist I saw at the reception a while ago? You were applying for a job here, right?"
    show jl angry with dissolve
    m conf "That's me."
    show jl neutral with dissolve
    jl "Congrats, I guess."
    m fabtalk "I just wanted to talk."
    show jl angrytalk with dissolve
    if le:
        $TempLink=0
        $SueLink=0
        stop music fadeout 3
        jl "Yeah, no thanks."
        scene black with dissolve
        "I try to convince her that I need to talk to her, but I can't seem to."
        "...."
        "In the end, I give up and come back to Sue to let her know that I couldn't get Julia to talk to me."
        su "Oh? That's fine, [name]. Don't let it get you down."
        "I go back to my office. Maybe there really was nothing I could have done."
        jump patientchoice
    jl "To me? Why?"
    show jl angry with dissolve
    menu:
        "I'm Sue's friend":
            show jl gasp with dissolve
            jl "Oh? Another one?"
            show jl talk with dissolve
            jl "And she sent you here so we can be \"friends\" too, right?"
            show jl angry with dissolve
            m sadsmile "That's kind of what she said..."
        "I want to be friends":
            $personal+=1
            show jl angrytalk with dissolve
            jl "\"Friends\"? Isn't that a big word given that this is our second conversation?"
            show jl angry with dissolve
            m cute "It's never too late."
            jl "Umm... fine."
        "Do you have anything better to do?":
            show jl calmtalk with dissolve
            jl "Actually, I can think of a couple of things..."
            show jl angry with dissolve
            jl "I have a lot of work to do."
            show jl neutral with dissolve
            jl "But... I guess I can spare some time."
    show jl talk with dissolve
    jl "I was on my way downstairs."
    stop music fadeout 4
    show jl calmtalk with dissolve
    jl "Now that you're here, feel free to follow me. Or not."
    hide jl with dissolve
    "She leaves."
    scene bg patients with dissolve
    show jl talk with dissolve
    play music "ost/hospital.wav" fadein 10
    jl "I've been working here for a while, and I've always thought there was something strange about this hallway."
    show jl neutral with dissolve
    menu:
        "It's really narrow":
            show jl talk with dissolve
            jl "Isn't it? I find it kind of uncomfortable to walk with the doors all around me..."
        "Is it the patients?":
            show jl talk with dissolve
            jl "They're everywhere, the whole hospital would feel strange if it was just for them."
            show jl angry with dissolve
            jl "Not to mention XXI... watching over that room whenever there's someone inside is the worst part of this job, I swear."
        "Is it... haunted?":
            show jl talk with dissolve
            jl "What are you, twelve?"
            show jl smile with dissolve
            "She's smiling, even though she sounds annoyed."
    show jl talk with dissolve
    jl "No, the weirdest thing here are the room numbers."
    show jl smile with dissolve
    m gasp "Numbers?"
    show jl talk with dissolve
    jl "Yes. Didn't you notice?"
    show jl neutral with dissolve
    "I shake my head."
    show jl smile with dissolve
    jl "I'll let you in on a couple of secrets here, then."
    show jl talk with dissolve
    jl "In this hallway, the rooms are labelled from II to XX."
    jl "So immediately, I thought: \"where's room number I?\"."
    show jl calmtalk with dissolve
    jl "One of the older nurses - she doesn't work here anymore - told me that room I isn't in this hallway with the rest."
    show jl neutral with dissolve
    m talk "Where is it, then?"
    show jl talk with dissolve
    jl "Somewhere on the third floor. I never actually saw it, but there's a lot of unused rooms there that were never renovated."
    show jl gasp with dissolve
    jl "Apparently, it's where aggressive patients used to be isolated from the rest."
    show jl calm with dissolve
    jl "Well, now it's probably some dusty locked waste of space."
    show jl talk with dissolve
    jl "Weird, huh? How there's a room somewhere and nobody knows where it is."
    show jl neutral with dissolve
    menu:
        "Yeah":
            $empathy+=1
        "Not really":
            pass
    show jl talk with dissolve
    jl "Also, did you notice how there's no room XVIII?"
    show jl smile with dissolve
    m gasp "Really?"
    show jl calmtalk with dissolve
    jl "...Not particularly observant, are you?"
    show jl talk with dissolve
    jl "I heard that was just a mistake made when labelling the rooms, and they never bothered to fix it."
    jl "Look over there - do you see room XIX?"
    show jl neutral with dissolve
    "Isn't that William's room..?"
    show jl angrytalk with dissolve
    jl "By all logic, it should be labelled as XVIII. But I guess it was more convenient that way."
    show jl calmtalk with dissolve
    jl "To be honest, not much in this hospital makes sense. My pay, for instance."
    show jl calm with dissolve
    show bg cafe with dissolve
    "We make our way downstairs."
    show jl angrytalk with dissolve
    jl "Actually, I never got to ask your name."
    show jl talk with dissolve
    jl "I know you said it once when we first met at the reception, but I didn't really bother to remember it."
    show jl neutral with dissolve
    m flirt "It's [name] Hart. Nice to meet you."
    show jl talk with dissolve
    jl "Julia Watts."
    $persistent.Julialast= "Watts"
    show jl angry with dissolve
    jl "...."
    show jl talk with dissolve
    jl "Are we just going to stand here awkwardly?"
    hide jl with dissolve
    "We sit by one of the empty tables and chat for a while."
    "I think that fulfills my promise to Sue."
    show jl talk with dissolve
    jl "I better go now. I hate being late."
    show jl neutral with dissolve
    m neu "I'm typically late."
    show jl smile with dissolve
    jl "You're just like Sue... Come on."
    show bg central with dissolve
    "We make our way back upstairs ahead of time. Surprisingly."
    show jl talk with dissolve
    jl "Hey, if you ever want to chat again, I should be somewhere around here most of the time. If I'm not busy."
    show jl calm with dissolve
    jl "...I'm very busy, you see."
    show jl neutral with dissolve
    m flirt "Thanks. I'll see you soon, Julia~"
    stop music fadeout 2
    scene bg mc with dissolve
    "I make my way back to my office and spend the remaining five minutes of my break looking out the window."
    jump patientchoice

label temp2:
    $TempLink+=1
    play music "ost/hospital.wav" fadein 15
    scene bg central with dissolve
    m smile "Hello, Julia."
    show jl gasp with dissolve
    jl "Oh, it's you. Hey."
    show jl talk with dissolve
    jl "I need to watch over the patients outside in some... 5 minutes. Want to join me?"
    show jl neu with dissolve
    m conf "Sure. I'd love to get some fresh air."
    scene bg outside
    "I follow Julia outside."
    "There are a few patients walking around. I don't recognize any of them."
    show jl talk with dissolve
    jl "How many patients do you have?"
    show jl neutral with dissolve
    m gasp "Me? Four so far."
    show jl calmtalk with dissolve
    jl "Hmm... it's probably because you're new."
    show jl angrytalk with dissolve
    jl "Is four patients a lot of work?"
    show jl angry with dissolve
    m "I don't really see it as work... I'm handling everything quite well, I think."
    show jl talk with dissolve
    jl "I see. So you don't get tired listening to people whining about their problems all day?"
    show jl neutral with dissolve
    menu:
        "It's not tiring":
            show jl calmtalk with dissolve
            jl "Right, I forgot you have your own office you can sit all day in..."
        "I stopped caring":
            show jl calmtalk with dissolve
            jl "Just like me, then."
            show jl neutral with dissolve
            jl "You really need to be tough to get used to working here, huh?"
        "They're not \"whining\"":
            show jl calmtalk with dissolve
            jl "I've never been to a psychologist. I wouldn't know."
    show jl neutral with dissolve
    "She's silent."
    "I start humming quietly."
    show jl angrytalk with dissolve
    jl "Stop that."
    show jl angry with dissolve
    m "Huh?"
    show jl smile with dissolve
    jl "People might think we're slacking off here."
    m shock "Oh no."
    show jl calm with dissolve
    jl "Right, I'm working... Unlike you right now."
    show jl talk with dissolve
    jl "So what do you think about the patients in general?"
    show jl neu with dissolve
    menu:
        "I like them a lot":
            $empathy+=1
            show jl gasp with dissolve
            jl "Wow, you're enthusiastic."
            show jl neutral with dissolve
        "I can handle them":
            $professional+=1
            show jl talk with dissolve
            jl "Yeah, sometimes you just have to grit yout teeth and do whatever you have to."
            show jl neutral with dissolve
        "They seem like a lot of work":
            show jl neu with dissolve
            jl "I guess..."
            show jl talk with dissolve
            jl "Some of them have been here for a couple of years..."
            show jl neutral with dissolve
            jl "I'm not sure if it's because of the staff, or if they're just so messed up."
    m fabtalk "Julia, you've been here for a while."
    show jl talk with dissolve
    jl "Right."
    show jl neu with dissolve
    m serious "How do you feel about this place? You don't seem very happy here."
    show jl angrytalk with dissolve
    jl "Aren't you getting a bit too... psychologist-like on me?"
    stop music fadeout 8
    show jl angry with dissolve
    m flirt "It's my job."
    show jl talk with dissolve
    jl "Besides, I don't need to be happy about it. I work." 
    show jl neutral with dissolve    
    m gasp "Don't you like your job?"
    play music "ost/tension.ogg" fadein 10
    show jl angrytalk with dissolve
    jl "Who would want a shitty job like this? Doing all the dirty work here while you just wait for the patients to come to you and talk?"
    show jl calmtalk with dissolve
    jl "Tsk, forget it... Your break's almost over. You should go."
    show jl angry with dissolve
    m regret "...."
    scene black with dissolve
    "I leave Julia be, despite how bad it makes me feel."
    stop music fadeout 5
    "I don't think I could've done anything to help."
    "If I see her again sometime, maybe she'll be more willing to talk about it."
    jump patientchoice
label temp3:
    $TempLink+=1
    scene bg central with dissolve
    show jl calm with dissolve
    play music "ost/tran.ogg" fadein 8
    "I find Julia resting in the nurses' office."
    m fabtalk "Hey. Are you busy?"
    show jl neutral with dissolve
    "She looks at me."
    show jl talk with dissolve
    jl "Not really."
    show jl neu with dissolve
    "I sit down next to her."
    m talk "Do you want to talk about something?"
    show jl calmtalk with dissolve
    jl "Pfft, now you really sound like a psychologist..."
    show jl neutalk with dissolve
    jl "I'm fine."
    show jl neutral with dissolve
    m fab "Are you sure..? It's not like talking about it would make anything worse."
    show jl angrytalk with dissolve
    jl "True. Unless you tell someone else about it."
    show jl angry with dissolve
    m conf "It's a secret, then. I promise."
    show jl calmtalk with dissolve
    jl "Then..."
    show jl calm with dissolve
    jl "...."
    stop music fadeout 5
    show jl angry with dissolve
    m laugh "That's what friends are for, right?"
    show jl gasp with dissolve
    jl "Are we... friends yet?"
    show jl neu with dissolve
    m gasp "I think so."
    play music "ost/hospital.wav" fadein 8
    show jl neutalk with dissolve
    jl "Alright. I'll tell you, if you really want to know."
    show jl talk with dissolve
    jl "My parents were both doctors. Half of my family is."
    show jl calm with dissolve
    jl "It's been kind of obvious from the start that I'd end up as one as well."
    show jl talk with dissolve
    jl "And I didn't mind - it's easy to find a job, and it's well-paid. Obviously."
    show jl neu with dissolve
    jl "I spent my whole childhood studying just to be like the rest of my family."
    show jl smile with dissolve
    jl "My older brother kept encouraging me... he graduated university while I was still in high school."
    show jl calmtalk with dissolve
    jl "My parents were always so proud of him... how he got the job they always wanted both of us to have."
    show jl talk with dissolve
    jl "And I..?"
    show jl angry with dissolve
    jl "I failed."
    show jl talk with dissolve
    jl "No matter how hard I tried, I just couldn't..."
    show jl neu with dissolve
    jl "My parents thought I should just be a nurse instead."
    show jl calmtalk with dissolve
    jl "So here I am, working at this hospital for... four years now."
    show jl talk with dissolve
    jl "At first, my brother suggested me working with him, but I couldn't stand the thought of having to be his assistant."
    show jl angrytalk with dissolve
    jl "...like that's all I'm good for."
    show jl calm with dissolve
    jl "I never wanted this job. But since there's nothing else I can do, I learned to stop complaining about it."
    show jl talk with dissolve
    jl "It's just how life is when you're an adult."
    show jl neutalk with dissolve
    jl "Not everyone gets to do what they want, like you do."
    show jl neu with dissolve
    menu:
        "How does your family feel about your job?":
            show jl calm with dissolve
            jl "Disappointed."
            show jl angrytalk with dissolve
            jl "But, as my mother once said: \"Somebody has to do it\"."
            show jl angry with dissolve
            jl "...made me feel like a janitor or something."
        "Did you want to be a doctor?":
            show jl angrytalk with dissolve
            jl "What kind of question is that? Of course I did!"
            show jl neutalk with dissolve
            jl "Listen, Hart, I work for the money. I don't care if I enjoy it or not, because I don't."
        "Do you feel bad about working here?":
            show jl calm
            jl "Does it matter? I'm used to it now."
    show jl talk with dissolve
    jl "It's just... frustrating to look at you people, bossing me around."
    show jl calmtalk with dissolve
    jl "I could've been that if I'd just worked harder..."
    show jl angry with dissolve
    jl "But I guess that's what I get."
    m uncom "It's not... that hard, is it..?"
    show jl gasp with dissolve
    jl "Oh, it's great, I love it -"
    show jl angrytalk with dissolve
    jl "...not."
    show jl talk with dissolve
    jl "Now you got me complaining... I know I shouldn't."
    show jl angry with dissolve
    m serious "Do you think your job makes you inferior to the doctors here?"
    show jl neutalk with dissolve
    jl "Uhhh... why ask me that? Are you suggesting something..?"
    show jl calm with dissolve
    jl "I just failed once, alright? I get that... I can't get what I wanted."
    m talk "Is that job really what you want?"
    show jl talk with dissolve
    jl "I... I wanted to get it my whole life."
    show jl neutral with dissolve
    m angry "What about now? Do you still care about it so much?"
    show jl calmtalk with dissolve
    jl "I don't know, Hart. I just don't."
    stop music fadeout 5
    show jl calm with dissolve
    m flirt "That's fine."
    show jl neu with dissolve
    m smile "Just think about it - maybe you'll come to some conclusions."
    play music "ost/sunny.wav" fadein 6
    show jl calmtalk with dissolve
    jl "...I guess. It's not like there's anything more engaging to do here..."
    show jl talk with dissolve
    jl "Like that time at the reception when we first met."
    show jl neutalk with dissolve
    jl "I was bored to death that day..."
    show jl neutral with dissolve
    jl "This place is a pain. I don't think you can change that."
    m cute "I can at least try to make your breaks more interesting."
    show jl calmtalk with dissolve
    jl "Yeah... that works, I guess."
    show jl smile with dissolve
    "We spend a while chatting until Julia has to go back to work."
    scene black with dissolve
    "I feel like I understand her better now."
    jump patientchoice
label tempafter:
    scene black with dissolve
    "I spent time with Julia."
    jump patientchoice
    
### Elizabeth ##########################
########################################
label prslink1:
    $PrsLink+=1
    scene black with dissolve
    "I decide to find Elizabeth again on my break."
    play music "ost/sunny.wav" fadein 7
    "She said she'd be outside, so I make my way to where I met her last time."
    scene bg outside with dissolve
    show e bored with dissolve
    "I spot her sitting on her own again."
    show e neu with dissolve
    m conf "Hello."
    show e talk with dissolve
    e "You again... you came back."
    show e neutral with dissolve
    m flirt "Why wouldn't I?"
    show e neutalk with dissolve
    e "I don't know, thought you had better things to do."
    show e boretalk with dissolve
    e "...turns out you don't actually have all that much work. Or you're just being lazy and not doing what you're supposed to be doing."
    show e baka with dissolve
    m fabtalk "I'm on my break, so I don't have any work to do right now."
    show e calm with dissolve
    e "...."
    show e neutral with dissolve
    e "So..."
    show e neutalk with dissolve
    e "What do you want from me again?"
    show e neu with dissolve
    m conf "I just thought that after our last conversation, it might be nice to see you again."
    show e bored with dissolve
    e "...."
    show e boretalk with dissolve
    e "...okay then?"
    show e baka with dissolve
    "....."
    m talk "You said you don't have any friends here."
    show e calmtalk with dissolve
    stop music fadeout 6
    e "I don't."
    show e calm with dissolve
    m fabtalk "Wouldn't you like to change that?"
    show e calmtalk with dissolve
    e "By having two psychologists instead of one? Not particularly."
    show e bored with dissolve
    play music "ost/hospital.wav" fadein 8
    m angry "I'm not here to be your second psychologist. I have patients of my own."
    show e foctalk with dissolve
    e "You wanna be my \"friend\"?"
    show e baka with dissolve
    m conf "I want to help you. If that involves being your friend, then I'll gladly do that."
    show e bakatalk with dissolve
    e "Why would you want to help me, anyway?"
    show e angry with dissolve
    e "I'm none of your concern."
    show e calmtalk with dissolve
    e "I'm my psychologist's problem, not yours."
    show e foc with dissolve
    m uncom "You aren't anyone's problem."
    show e boretalk with dissolve
    e "Yeah, definitely."
    show e calmsmile with dissolve
    "She stretches lazily, completely ignoring me for a while."
    show e talk with dissolve
    e "Ugh, say that to my parents..."
    show e neu with dissolve
    "Huh..?"
    menu:
        "Do they not want to help you?":
            $personal+=1
            $GoldenHeart+=1
            show e calmtalk with dissolve
            e "I guess they do..."
            show e bakatalk with dissolve
            e "I don't want their help."
        "You're not a problem for them":
            $professional+=1
            pass
        "Are they worried about you?":
            $personal+=1
            $empathy+=1
            show e angry with dissolve
            e "No."
    show e foc with dissolve
    e "...."
    show e calmtalk with dissolve
    e "Let's not talk about 'em."
    stop music fadeout 6
    show e neutalk with dissolve
    e "I don't get 'em either way."
    show e neutral with dissolve
    "I should change the topic."
    play music "ost/sunny.wav" fadein 8
    m talk "If you don't like to talk to other patients, what do you do in your free time?"
    show e boretalk with dissolve
    e "Nothing."
    show e foctalk with dissolve
    e "Not used to really doing anything on my own..."
    show e bored with dissolve
    m fab "Is there anything you think you'd enjoy doing, then?"
    show e neu with dissolve
    "She shrugs."
    show e neutalk with dissolve
    e "Don't know."
    show e bored with dissolve
    "...."
    m gasp "Would you like to try some things? There are a lot of activities organized here for the patients."
    show e foc with dissolve
    e "Group. Activities."
    show e neutral with dissolve
    m conf "Not all of them."
    show e calmtalk with dissolve
    e "I mean... I guess..."
    show e neutalk with dissolve
    e "Got nothing better to do."
    show e bored with dissolve
    menu:
        "That's the spirit!":
            show e calmtalk with dissolve
            e "Uhh... yeah."
        "You should give it a try sometime":
            show e calm with dissolve
            e "...maybe."
        "I can help you with that":
            $GoldenHeart+=1
            show e neutalk with dissolve
            e "...oh."
            show e calmtalk with dissolve
            e "I mean, if you want to..."
    show e neu with dissolve
    "It's about time for me to leave, if I don't want to to be late for my second session."
    m flirt "Think about it. It could be a nice change for you."
    show e calmtalk with dissolve
    e "Alright, alright... I'll consider it."
    show e bored with dissolve
    stop music fadeout 4
    m kawaii "I should get back to my patients now. It was nice to talk to you again."
    "She's silent. I leave her be."
    jump patientchoice
label prslink2:
    $PrsLink+=1
    scene black with dissolve
    play music "ost/sunny.wav" fadein 7
    "I'm going to see Elizabeth today, but this time I have an idea."
    scene bg cafe with dissolve
    show e neu with dissolve
    "I spot her in the cafeteria."
    show e calm with dissolve
    m flirt "Hello ~"
    show e boretalk with dissolve
    e "...again."
    show e baka with dissolve
    m smile "How are you today? Have you thought about these activities I mentioned last time?"
    show e calm with dissolve
    "She shrugs."
    show e neutalk with dissolve
    e "Whatever you say, Doctor."
    show e neu with dissolve
    m fabtalk "If you're still unsure about it, I can always show you around."
    show e neutalk with dissolve
    e "What? Me?"
    show e calmtalk with dissolve
    e "Been here long enough to see everything I needed to see."
    show e neu with dissolve
    m conf "Trust me. You're missing out."
    show e talk with dissolve
    e "...fine."
    show e boretalk with dissolve
    e "Lead the way... or something."
    show e calm with dissolve
    show bg patients with dissolve
    m fab "As you know, as patients, you're not really supposed to stay in your rooms all day and sleep."
    show e baka with dissolve
    m uncom "...if you don't want to."
    show e neu with dissolve
    m talk "There's plenty of things you can do to keep yourself occupied. It's also a great opportunity to meet other patients."
    m cute "First of all, going out is a great habit to have - nothing better than some fresh air."
    show e foctalk with dissolve
    e "Too many people here... makes me sick."
    show e baka with dissolve
    m uncom "...Exactly."
    m flirt "Well, I interrupted your usual routine to show you something else."
    play sound "doorclose.ogg" fadein 1
    show bg central with dissolve
    show e neutalk with dissolve
    e "What is it?"
    show e neutral with dissolve
    m talk "I asked around after work yesterday, and learned all you need to know."
    m fabtalk "Group activities take place in Office IV, but outside of that time the room is accessible to any staff member to use for the patients' benefit."
    show e foctalk with dissolve
    e "I ain't your patient."
    show e baka with dissolve
    m cute "I'm sure your psychologist wouldn't mind, though."
    show e boretalk with dissolve
    e "Hmph. Not like they'd care."
    show e foctalk with dissolve
    e "Actually..."
    show e foc with dissolve
    "She stops abruptly. Is something wrong..?"
    show e neutalk with dissolve
    e "Who're your patients?"
    show e neutral with dissolve
    m talk "Currently I have four of them - Michael Burnett from room XV, Tom Richards from XVI, William Moore from XIX and Charlie from IX."
    show e baka with dissolve
    e "...."
    show e calm with dissolve
    "She nods to herself."
    show e neutalk with dissolve
    e "All guys. Kind of a weird coincidence."
    show e neu with dissolve
    stop music fadeout 5
    m neu "I guess."
    show e calmsmile with dissolve
    e "It's almost like your boss wanted to set you up with one of 'em."
    show e bored with dissolve
    m freeze "...."
    m fabtalk "Excuse me..? No, I don't think that was, umm..."
    m tsun "...."
    show e smirk with dissolve
    play music "ost/sunny.wav" fadein 8
    "A blush creeps onto my cheeks at the ridiculous idea... Me? With a patient?"
    "Come on, I'm a professional... I'd never do something like that..."
    "...Here I am, hanging out with a patient that's not even one of my own on my break. Great."
    show e neutalk with dissolve
    e "What, was that really so offensive? You need to toughen up, Hart."
    show e neutral with dissolve
    "...."
    "I need to remind myself that her illness probably makes her immune to the feeling of awkwardness."
    "It's at times like these when I kind of wish I had some sort of an asocial disorder."
    show e bored with dissolve
    play sound "doorclose.ogg" fadein 1
    show bg offices with dissolve
    m fabtalk "How many patients does your psychologist have, then?"
    show e neutalk with dissolve
    e "Beats me. Never asked."
    show e calm with dissolve
    m talk "Which office is theirs, if I may ask?"
    show e boretalk with dissolve
    e "II? I don't bother to remember psychologists' names since I was  shuffled from person to person so much this year."
    show e baka with dissolve
    "Fair enough."
    stop music fadeout 5
    m fabtalk "What about psychiatrists?"
    show e regret with dissolve
    e "...."
    show e foctalk with dissolve
    e "Don't get me started, he's such a pain..."
    show e pain with dissolve
    m gasp "Why is that?"
    show e angrytalk with dissolve
    e "He just is, okay? What's your problem, asking me all that?"
    show e baka with dissolve
    "I'm a psychologist. I guess."
    play music "ost/tension.ogg" fadein 5
    m uncom "I'm sorry about -"
    show e calmtalk with dissolve
    e "Don't care. Just stop talking."
    show e neu with dissolve
    "...."
    show e boretalk with dissolve
    e "A lot better. Get back to your patients, Hart."
    hide e with dissolve
    play sound "doorclose.ogg" fadein 1
    "She leaves the way we came."
    "I take a deep breath. I shouldn't get discouraged."
    jump patientchoice
label prslink3:
    $PrsLink+=1
    scene black with dissolve
    play music "ost/sunny.wav" fadein 4
    scene bg offices with dissolve
    "I leave my office in search of Elizabeth."
    "Yesterday's conversation took a turn I didn't expect after I mentioned her psychiatrist..."
    "I know I should avoid that topic now, along with her parents."
    stop music fadeout 1
    show bg offices with hpunch
    e "Hey, you! I'm right here, idiot -!"
    "I hear her voice coming from Office IV. The door is open."
    scene bg officeiv with dissolve
    show e talk with dissolve
    e "Taking your sweet time, I see. Sit down."
    show e calm with dissolve
    play music "ost/hospital.wav" fadein 10
    "I take a seat next to her. She's not looking at me."
    show e bakatalk with dissolve
    e "Jeez, I've been waiting for you here for the past... 10 minutes or so."
    show e bored with dissolve
    menu:
        "I'm sorry":
            $wrong+=1
            show e talk with dissolve
            e "Don't say that."
        "Waiting... for me?":
            $personal+=1
            show e talk with dissolve
            e "Who else, dumbass?"
        "I had work to do!":
            $professional+=1
            show e calmtalk with dissolve
            e "Yeah, so much \"work\"."
    show e baka with dissolve
    m fabtalk "How did you even get here?"
    show e calmtalk with dissolve
    e "I, uh... sweet-talked the last psychologist who was here not to close yet, since you were going to be here soon."
    show e foc with dissolve
    "Her gaze is fixated on something in her hands."
    m talk "So you expected me to be here?"
    show e neutalk with dissolve
    e "You said you wanted to get me to do some activities. So here I am."
    show e neutral with dissolve
    "She's very true to her word, at least."
    m gasp "What... What is that you're holding, actually?"
    show e baka with dissolve
    "She hides a crumbled piece of paper in her hands."
    show e regrettalk with dissolve
    e "It's private. Classified."
    show e foc with dissolve
    m fabtalk "Were you... drawing?"
    show e angrytalk with dissolve
    e "No-"
    show e bakatalk with dissolve
    e "I mean..."
    show e talk with dissolve
    e "...A little bit."
    show e foctalk with dissolve
    e "Hey, don't judge me- I never drew in my life."
    show e baka with dissolve
    m gasp "Really?"
    show e angry with dissolve
    e "What's so weird about that?"
    show e neutral with dissolve
    m talk "Drawing as a child stimulates development in many areas... So I just find it -"
    show e talk with dissolve
    e "Strange? Just like me, right?"
    show e calmtalk with dissolve
    e "...Get over it."
    show e neu with dissolve
    m flirt "It's never too late to start, though. What did you draw?"
    show e foctalk with dissolve
    e "I... don't know."
    show e bored with dissolve
    e "It's such a weird thing to do."
    show e neutalk with dissolve
    e "I mean... there's no point."
    show e calmtalk with dissolve
    e "No benefits to it."
    show e foc with dissolve
    m boretalk "Not even having a good time?"
    show e baka with dissolve
    "She scoffs."
    show e talk with dissolve
    e "You can't measure that. You can't... lose anything without it."
    show e neutral with dissolve
    m fabtalk "Actually, you can lose a lot. Like your mental health, in the long run."
    show e boretalk with dissolve
    e "You implying somethin'..?"
    show e baka with dissolve
    m neu "Not at all."
    m talk "It's not my job to diagnose you in any way."
    show e foctalk with dissolve
    e "Great... had enough of that already."
    show e bored with dissolve
    "She crushes the ball of paper in her hands abscentmindedly."
    show e talk with dissolve
    e "Everyone thinks there's... literally so much wrong with me."
    show e neutalk with dissolve
    e "Anyone else would've brushed it off as just being a bit... socially inept."
    show e baka with dissolve
    e "...but not my parents."
    show e neutalk with dissolve
    e "Either way, I'm not sure what being here fixes, other than 'em not having to worry about what I'm doing."
    show e talk with dissolve
    e "Which I guess suits 'em."
    show e bakatalk with dissolve
    e "They're probably better off without me, anyway... not that I blame them."
    show e neu with dissolve
    e "It's always less dead weight to slow them down."
    menu:
        "You're not dead weight":
            $wrong+=1
            show e foctalk with dissolve
            e "That's easy to say for someone who doesn't know me at all. Or my parents."
        "Do they really seem happier without you?":
            $personal+=1
            show e talk with dissolve
            e "Hell if I know."
            show e foctalk with dissolve
            e "I'm not in their heads."
            $GoldenHeart+=1
        "If you had a problem, it's good they sought help":
            $professional+=1
            show e foctalk with dissolve
            e "I don't need their help. Not when it's like this."
    stop music fadeout 5
    show e foc with dissolve
    "...."
    "A moment passes in silence."
    show e bored with dissolve
    m uncom "So, um..."
    show e neu:
        linear 0.3 xpos 0.7
    play music "ost/tension.ogg" fadein 5
    nn "Ms. Price..?"
    "A nurse enters the office suddenly."
    show e neutalk with dissolve
    e "Umm, yeah? That's me."
    show e neu with dissolve
    gu "I was only instructed to make sure you're still in Office IV."
    show e boretalk with dissolve
    e "Where else should I be?"
    show e foc with dissolve
    "The nurse looks at me."
    gu "You're not her psychologist."
    m talk "She's here under my supervision. Is there a problem?"
    "She looks at me suspiciously and leaves."
    show e neu:
        linear 0.3 xpos 0.5
    e "...."
    stop music fadeout 15
    show e regret with dissolve
    $persistent.Elizabethlast="Price"
    "So her full name is Elizabeth Price."
    "Wait... that last name... I've heard it somewhere before..."
    m fabtalk "Um, Elizabeth?"
    show e angrytalk with dissolve
    e "What?"
    show e angry with dissolve
    m serious "Are your parents, um..."
    show e talk with dissolve
    e "{i}Those{/i} Prices? Yes, they are."
    show e bakatalk with dissolve
    e "The richest family in the city. That's them."
    show e calm with dissolve
    play music "ost/tran.ogg" fadein 10
    "...oh."
    "I can see why she was reluctant to talk about her family now."
    show e angrytalk with dissolve
    e "What's that look for? Wasn't my choice."
    show e baka with dissolve
    m regrettalk "I know. I'm sorry."
    show e pain with dissolve
    e "...."
    if GoldenHeart>4:
        show e regrettalk with dissolve
        e "Does that... mean we can't hang out anymore?"
        show e neu with dissolve
        "What-?"
        show e calmtalk with dissolve
        e "I mean... I don't care if you wouldn't want to, it's cool."
        show e baka with dissolve
        m gasp "No no, really, that doesn't change anything."
        m smile "As long as you want to, we can keep talking like this on breaks next week."
        show e regrettalk with dissolve
        e "Really? You're not... trolling me, right?"
        show e angry with dissolve
        m flirt "No."
        show e neu with dissolve
        e "...."
        show e calmsmile with dissolve
        e "Thanks, I guess. It's been alright."
        $route = "golden"
    else:
        show e talk with dissolve
        e "Well then..."
    show e neutral with dissolve
    "She gets up to leave."
    "Right, my break's nearly over."
    if route == "golden":
        show e neu with dissolve
        m cute "I'll walk you back to your room, if you don't mind. I still have some time."
        show e calmtalk with dissolve
        e "Sure. Tag along if you want."
        show bg patients with dissolve
        show e neu with dissolve
        "We walk through the entire hallway until she stops."
        show e boretalk with dissolve
        e "That's my room. II."
        show e baka with dissolve
        m fabtalk "Are you alone here?"
        show e foctalk with dissolve
        e "Thankfully. My parents had that arranged, even though usually dangerous patients are the priority when it comes to single rooms."
        show e neutral with dissolve
        "...."
        stop music fadeout 7
        m talk "I'll see you next week, then."
        show e talk with dissolve
        e "Yeah."
        play sound "doorclose.ogg" fadein 1
        hide e with dissolve
        "She disappears in her room and I get back to my office."
    else:
        show e talk with dissolve
        e "See ya."
        play sound "doorclose.ogg" fadein 1
        hide e with dissolve
        "She leaves and I get back to my office."
    jump patientchoice
### PSYCHIATRIST ######################
#######################################
label star1:
    $StarLink+=1
    scene black with dissolve
    "I decide to try to talk to Dr. Young on my break."
    scene bg offices with dissolve
    play music "ost/sunny.wav" fadein 6
    "He seemed eager to spend time with me when we met, and I'm hoping to get to know him a little better."
    play sound "knock.ogg" fadein 1
    m fabtalk "Dr. Young?"
    s "One moment!"
    show s smile with dissolve
    "I hear rushed footsteps and the door flies open."
    show s gasp with dissolve
    s "Ms. Hart?"
    show s cute with dissolve
    s "Please, come in."
    show bg young with dissolve
    show s smile with dissolve
    "We enter his office. It resembles Dr. Sharpe's slightly, but it has a much more welcoming feel to it."
    "And there's more sunlight."
    show s neutalk with dissolve
    s "You came to talk?"
    show s neutral with dissolve
    m flirt "I thought it might be nice. Only if you have time, Doctor."
    show s laugh with dissolve
    s "Of course, of course - take a seat."
    show s sadsmile with dissolve
    s "I'm sorry if my office is a... bit of a mess at the moment, I wasn't expecting you."
    m cute "That's fine."
    show s neu with dissolve
    "I sit down by his desk and so does he."
    show s talk with dissolve
    stop music fadeout 5
    s "So you're here since the beginning of November?"
    show s smile with dissolve
    m talk "I am."
    play music "ost/hospital.wav" fadein 6
    if not route=="golden":
        show s sadtalk with dissolve
        s "How do you like working here so far? It gets a little difficult at times, I'm sure."
        show s neu with dissolve
        if month==1:
            if day<13:
                m flirt "I'm still adjusting, but I think I'm doing alright."
                show s smile with dissolve
                m conf "What matters is that I know what I have to do."
                show s neutalk with dissolve
                s "Certainty is a good thing to have. A luxury, some might say."
                show s kawaii with dissolve
                s "I'm glad you're doing well."
            else:
                m frusttalk "Things are piling up, but... I think I know what I'm doing."
                show s gasp with dissolve
                s "Oh? Trouble with patients?"
                show s neutral with dissolve
                m neu "Mostly. Nothing I can't handle."
                show s cute with dissolve
                s "I admire your determination."
        else:
            if day<6:
                "I decide to make it simple."
                show s neutral with dissolve
                m conf "I'm doing okay. The important thing is that I'm making progress."
                show s smile with dissolve
                s "Good. Progress is always good."
            else:
                "Let's not involve him in this..."
                m smile "I'm doing well. My patients seem to trust me a lot."
                show s laugh with dissolve
                s "Well done, Ms. Hart. That {i}is{/i} an achievement."
    show s neu with dissolve
    m gasp "What about you, Doctor? You seem to have been here for quite some time."
    show s gasp with dissolve     
    s "You think so? What gives that away?"
    show s cute with dissolve
    menu:
        "Your age":
            show s blush2 with dissolve
            "He laughs."
            show s smile with dissolve
            s "Is that it?"
        "Your attitude":
            show s neutalk with dissolve
            s "The attitude of someone who has a lot of experience in this place? Fair enough."
        "You know people":
            $empathy+=1
            show s sadsmile with dissolve
            s "Oh yes, I did mention not having seen you before when we first met."
    show s talk with dissolve
    s "To answer your question, I have worked here for five years."
    show s smile with dissolve
    m neu "That {i}is{/i} a long time. You must be one of the more perseverant staff members here."    
    show s sadsmile with dissolve
    s "Very true. Many people come and go in a matter of months."
    m fab "Yes, some of my patients have had many different psychologists in their time here."
    show s laugh with dissolve
    s "Oh? Then you must be dealing with some of the most {i}perseverant{/i} patients here, so to speak."
    show s smirk with dissolve
    m talk "Do most of them leave quickly?"
    show s angry with dissolve
    s "A month or two. It really depends on why they're here."
    m gasp "What do you mean?"
    show s neutalk with dissolve
    s "You see, some patients are admitted here because they themselves sought help."
    show s sad with dissolve
    s "Others are here due to suicide attempts. They are meant to be monitored and treated until the threat lessens."
    show s sadtalk with dissolve
    s "And then there's the small minority of people who would've been imprisoned, had they been sane when committing a crime."
    show s neutral with dissolve
    "Michael."
    m neu "Why is there so much variety in one hospital? Shouldn't these groups be separated?"
    show s sadtalk with dissolve
    s "They should, no doubt."
    stop music fadeout 6
    show s neu with dissolve
    s "But I'm sure you're aware of how far the nearest other institution is from here."
    show s angrytalk with dissolve
    s "And it doesn't look like they'll be building a new one anytime soon."
    show s sad with dissolve
    play music "ost/mc.wav" fadein 6
    s "So it is what it is. All we can do is work hard and hope nothing terrible happens."
    m talk "You sound rather determined, Doctor."
    show s neutalk with dissolve
    s "Somebody has to be. We would all lose it in a place like this if it weren't for that."
    show s sadsmile with dissolve
    "He smiles briefly."
    show s laugh with dissolve
    s "I am glad to have someone like you as a coworker. We need more enthusiasm here, I think."
    show s smile with dissolve
    m sadsmile "I'm not sure if Dr. Sharpe would agree with that sentiment."
    show s angry with dissolve
    "Young goes silent for a moment and looks at me, puzzled."
    show s neutalk with dissolve
    s "I am honestly unsure of what he would think about that."
    show s talk with dissolve
    s "We're two doors apart, and it feels like a whole galaxy sometimes."
    show s sad with dissolve
    m flirt "He's not exactly the most open person around, true."
    stop music fadeout 6
    show s calm with dissolve
    "The psychiatrist looks away from me with an unreadable expression."
    show s sadtalk with dissolve
    s "He used to be."
    show s pain with dissolve
    m gasp "...."
    show s laugh with dissolve
    play music "ost/tran.ogg" fadein 5
    s "I'm sorry, don't let me bore you with stories."
    show s sadsmile with dissolve
    s "Besides."
    show s neu with dissolve
    "He stands up suddenly and so do I."
    show s talk with dissolve
    s "It isn't polite to gossip about old friends."
    show s smirk with dissolve
    "He walks me out of his office."
    show bg offices with dissolve
    show s sadtalk with dissolve
    s "I believe our break is nearly over."
    show s kawaii with dissolve
    s "It was very nice to talk to you, Ms. Hart. Whenever you have the time, you're welcome in my office."
    show s smile with dissolve
    m conf "Likewise, Doctor. Excuse me."
    show s cute with dissolve
    s "Of course. Good luck with your patients."
    play sound "doorclose.ogg" fadein 1
    hide s with dissolve
    "I leave his office and can't help but rethink what I learned."
    "Particularly, what I learned about his past relationship to Dr. Sharpe."
    "I can't imagine our overseeing psychiatrist being friends with... well, anyone, really."
    "Dr. Young did suggest he changed somehow..."
    "I wonder what went on between these two."
    jump patientchoice

label star2:
    $StarLink+=1
    scene bg offices with dissolve
    play music "ost/hospital.wav" fadein 6
    "I'm interested to talk to Dr. Young again after what I've learned last time."
    play sound "knock2.ogg"
    "I knock on the door to his office."
    show s happy with dissolve
    s "Ms. Hart?"
    show s cute with dissolve
    m fab "May I come in?"
    show s blush with dissolve
    s "I was hoping you'd ask. Please."
    show bg young with dissolve
    "He opens the door wide enough to let me in."
    show s neutalk with dissolve
    s "...what brings you here?"
    show s neutral with dissolve
    m talk "I was curious to learn more about this place. You seem to know it very well."
    show s gasp with dissolve
    s "So you want information. Why?"
    show s neu with dissolve
    menu:
        "To help my patients":
            show s gasp with dissolve
            s "How exactly does that..?"
            show s sadtalk with dissolve
            s "I'm sorry, I don't follow."
            show s sadsmile with dissolve
            m conf "Learning more about the hospital might help me understand them."
            show s talk with dissolve
            s "It might, I suppose."
        "Maybe there's some things I should know":
            show s sadsmile with dissolve
            s "I don't follow."
            show s neu with dissolve
            m fabtalk "I'm new here. Where am I supposed to learn the things everyone else knows?"
            show s angry with dissolve
            s "You might be right..."
        "It's just an excuse":
            show s blush2 with dissolve
            s "To spend time with me?"
            show s cute with dissolve
            "He laughs."
            show s happy with dissolve
            s "I apologize, it's just that there are many people here who are much more interesting than I am."
            show s smile with dissolve
            m cute "I think I'll stay."
            show s sadsmile with dissolve
            s "You flatter me, Ms. Hart."
    stop music fadeout 6
    show s kawaii with dissolve
    s "So what do you need to know? I'll see if I can be of help."
    "I consider how straightforward I should be here. I know what I want to know most, but..."
    show s smile with dissolve
    "No, I think I can trust him with this."
    play music "ost/tension.ogg" fadein 6
    m pity "I'm sorry if I'm being persistent about it, but it's been bothering me since last time."
    show s laugh with dissolve
    s "Ask away."
    show s neu with dissolve
    m frust "It's about Dr. Sharpe."
    show s neutral with dissolve
    s "...Oh."
    show s angrytalk with dissolve
    s "You want me to tell you things you shouldn't know."
    show s angry with dissolve
    m gasp "How so?"
    show s sadtalk with dissolve
    s "I was his friend, Ms. Hart. To talk about him behind his back would be betraying his trust."
    show s calm with dissolve
    s "...."
    show s paintalk with dissolve
    s "That is, if there's any trust in me left."
    show s neutral with dissolve
    m talk "What do you mean? Why wouldn't he trust you anymore?"
    show s sadtalk with dissolve
    s "He... He's changed. And he hasn't been the same since three years ago."
    show s paintalk with dissolve
    s "I barely talk to him anymore, only about work."
    show s calm with dissolve
    m regrettalk "I'm sorry. I wasn't aware it was like this."
    show s sadsmile with dissolve
    s "It's okay. It just... pains me to see him so much different."
    m gasp "What made him change like that?"
    stop music fadeout 6
    show s angry with dissolve
    s "If I may, why do you want to talk about this so much?"
    m conf "I'm trying to understand how to get along with someone like him."
    show s neutral with dissolve
    m angry "He's my boss, I don't want to make things difficult."
    play music "ost/tran.ogg" fadein 6
    m boretalk "I was hoping... someone who knew him could shed some light on this."
    show s neutalk with dissolve
    s "That's it?"
    show s neutral with dissolve
    m smile "That's all there is to it."
    show s sadtalk with dissolve
    s "Pardon my curiosity, but are you sure this is a strictly professional interest?"
    show s calmtalk with dissolve
    s "Because if it isn't, take my word for it - this isn't something you want to get into."
    show s neutral with dissolve
    "I'm stunned."
    "Did he just... suggest I might be interested in Dr. Sharpe..? Personally..?"
    m tsun "It's nothing like that."
    stop music fadeout 5
    show s cute with dissolve
    s "What do you want to know, then?"
    show s smile with dissolve
    m fabtalk "How long have you known him?"
    show s smirk with dissolve
    s "Four years. Since he started working here."
    play music "ost/hospital.wav" fadein 6
    show s pain with dissolve
    "He sighs."
    show s sadsmile with dissolve
    s "It feels like a very long time ago."
    m talk "What was he like back then?"
    show s calmtalk with dissolve
    s "Well..."
    show s neutalk with dissolve
    s "When he first came to work here, he was young. Very young, for a psychiatrist in a place like this."
    show s calmsmile with dissolve
    s "We thought he was just one of the naive, inexperienced ones who think they can change everything with sheer willpower."
    show s talk with dissolve
    s "That once he saw what it's really like, he would break."
    show s neutral with dissolve
    m gasp "He didn't?"
    show s smirk with dissolve
    s "Never. He was a lot like you when I first met him."
    stop music fadeout 5
    show s calmtalk with dissolve
    s "Full of energy. Determined to make the world a better place."
    show s sadsmile with dissolve
    s "Forgive my judgement, it's just the way you talk and act."
    show s talk with dissolve
    play music "ost/sunny.wav" fadein 6
    s "You look like you want to make a difference by working here, not just to make a living."
    show s smile with dissolve
    m conf "I do. You're absolutely right."
    show s gasp with dissolve
    s "Dare I say it, you were even similiar in age... If I may ask, how old are you, exactly, Ms. Hart?"
    show s neutral with dissolve
    m talk "I'm 28."
    show s neu with dissolve
    "He looks at me analytically for a moment, almost in amazement."
    show s smirk with dissolve
    s "He was your age when I met him."
    m shock "...."
    $persistent.Sharpeage="32"
    play sound "chars.ogg" 
    show screen notify("{size=24} Your Characters Info screen has been updated!")
    show s laugh with dissolve
    "He muffles a sudden burst of laughter."
    show s smirk with dissolve
    m gasp "What is it?"
    show s sadsmile with dissolve
    s "No, no, I shouldn't be surprised..."
    show s calmtalk with dissolve
    s "I suppose it's hard to tell now."
    show s smile with dissolve
    stop music fadeout 5
    m confusion "...anyway. Go on, please."
    show s neutalk with dissolve
    s "I was intrigued when he succeeded with two of his patients who'd been here for over a year by then."
    show s sad with dissolve
    play music "ost/hierback.wav" fadein 6
    s "Nobody knew how to get to them. How to earn their trust."
    show s talk with dissolve
    s "It seemed almost supernatural, him coming here with no previous experience and being able to read people so quickly, so accurately."
    show s neutral with dissolve
    m talk "Is that when you first approached him?"
    show s sadtalk with dissolve
    s "I decided to visit him in his office after work. I wanted to see what is it about him that made him capable of these things."
    show s neu with dissolve
    m neu "Were you jealous of him?"
    show s neutalk with dissolve
    s "Curious, mostly."
    show s gasp with dissolve
    s "But when I talked to him, I was... shocked. On many levels."
    show s neutral with dissolve
    m gasp "Why was that?"
    show s calm with dissolve
    s "Well..."
    show s talk with dissolve
    s "The way he talked, it was like... He had so much {i}wisdom{/i}. More than anyone I knew."
    show s sad with dissolve
    s "Like despite his age, he's seen and thought things most people never do in their whole lives."
    show s calmtalk with dissolve
    s "He understood people on a completely different level than I did."
    show s neu with dissolve
    s "On top of that, he was so cultured and educated... I felt like a child when I first talked to him."
    show s sadtalk with dissolve
    s "He was ahead of me in every way. But I couldn't bring myself to envy him for it."
    show s smile with dissolve
    m neu "Why not?"
    show s talk with dissolve
    s "Because he was also the kindest friend I've ever had."
    show s sadtalk with dissolve
    s "He always had time for other people, worked so much more than he was expected to..."
    show s neutral with dissolve
    s "When I asked him how he managed to treat these two first patients, he simply told me this:"
    show s neutalk with dissolve
    s "He paid very close attention to how they behaved around him, drew conclusions, then went through everything we had on them to fill in the blanks."
    show s smirk with dissolve
    s "Once he knew everything there is to know and got them to trust him, he approached their psychologists and explained everything to them."
    show s sadtalk with dissolve
    s "How to talk to them, how they feel, what they need."
    show s calmtalk with dissolve
    s "A month later, they were both out of here."
    show s smile with dissolve
    m neu "...."
    m gasp "Wow."
    show s cute with dissolve
    s "I was surprised when I heard it from him as well."
    show s sadsmile with dissolve
    stop music fadeout 6
    s "But he was always like this. Always doing more than anyone could've asked in order to help."
    show s calmsmile with dissolve
    s "The whole staff became fond of him. They had no reason not to."
    m talk "It sounds like he had no flaws."
    play music "ost/hospital.wav" fadein 6
    show s neutalk with dissolve
    s "None that I can remember. He was a saint, that man. Honestly."
    show s neutral with dissolve
    m neu "What happened to him?"
    show s pain with dissolve
    "He sighs."
    show s sadtalk with dissolve
    s "I'm not sure."
    show s paintalk with dissolve
    s "I know what caused it and how it started, but..."
    show s sad with dissolve
    s "I can't tell you what happened."
    show s sadsmile with dissolve
    s "Unlike him, reading people doesn't come naturally to me."
    stop music
    play sound "knock.ogg" fadein 1
    show s gasp with dissolve
    s "Who could that be..?"
    show s neu with dissolve
    "He gets up to answer the door."
    play sound "doorclose.ogg" fadein 1
    play music "ost/hier.ogg" fadein 5
    show s neu:
        ease 0.5 xpos 0.2
    show s gasp with dissolve
    show d neutral with dissolve
    "I look at the man who just entered the office with pure bewilderment."
    show s neutral with dissolve
    show d neu with dissolve
    "He glances at me from above Young's shoulder, clearly just as surprised as I am."
    "Then he looks back at his fellow psychiatrist with a small smile."
    show d regretsmile with dissolve
    d "I apologize, I seem to have interrupted something."
    show s sad with dissolve
    "Suddenly, I feel like I shouldn't be here."
    show d talk with dissolve
    d "Have I, Charles?"
    show d neu with dissolve
    show s laugh with dissolve
    s "Not at all. How can I help?"
    show s smile with dissolve
    show d sidetalk with dissolve
    d "This is a professional matter which doesn't concern Ms. Hart. Regarding one of your patients."
    show s neutral with dissolve
    show d cold with dissolve
    "He looks at me and I feel his gaze piercing through me."
    show d neutral with dissolve
    "I get up and approach the door."
    show s neu with dissolve
    m conf "I was just about to leave. My break is nearly over."
    show d regrettalk with dissolve
    d "I would hate to keep you."
    show d neu with dissolve
    stop music fadeout 5
    "He opens the door and I say goodbye to Dr. Young before leaving."
    play sound "doorclose.ogg" fadein 1
    scene bg offices with dissolve
    "Speak of the devil, jeez..."
    play music "ost/hospital.wav" fadein 5
    "I can't picture Sharpe as the person Dr. Young described today."
    "It's clear he's still very dedicated to his work and tries his best to help everyone, but there's nothing kind or caring about the way he treats the staff."
    "He seems so... cold. Strict."
    "I hope I can learn what caused him to change like he did soon."
    jump patientchoice
    
label starafter:
    $StarLink+=1
    scene black with dissolve
    "I spent a pleasant break with Dr. Young."
    jump patientchoice
