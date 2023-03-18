define re = Character("Receptionist", color = '#ffffff')
define gu = Character("Nurse", color = '#ffffff')
define m = Character("[name]", color = '#ffffff', image = "sprites/mc/.png")
define d = Character("Sharpe", color = '#ffffff')
define t = Character("Tom", color = '#ffffff')
define dv = Character("Michael", color = '#ffffff')
define w = Character("William", color = '#ffffff')
define h = Character("Charlie", color = '#ffffff')
define e = Character("Elizabeth", color = '#ffffff')
define sue = Character("[suename]", color = '#ffffff')
define jl = Character("Julia", color = '#ffffff') 
define pt = Character("Patient", color = '#ffffff')
define er = Character("James", color = '#ffffff')
define s = Character("[star]", color = '#ffffff')
define mm = Character("Mom", color='#ffffff')

define wm = Character("Woman", color = '#ffffff')
define mn = Character("Man", color = '#ffffff')
define cd = Character("Child", color = '#ffffff')
define doc = Character("Doctor", color = '#ffffff')
define girl = Character("Girl", color = '#ffffff')

define g = Character("\"G\"", color = '#ffffff')
define l = Character("Milena", color = '#ffffff')

define nt = Character(None, screen="cinematic")
#########################################################################
### VARIABLES ###########################################################
#########################################################################
default journal=False

default redintro = 0
default blueintro = 0
default silverintro = 0
default purpleintro = 0

default firstpatient = "no"
default sessions = 0

default social = 0
default suename = "Nurse"
## Patient interactions ############
default redinteract = 0
default blueinteract = 0
default purpleinteract = 0
default silverinteract = 0

default hanged = "Tom"
define pr = Character("[hanged]", color = '#ffffff')

default name = "Me"
default empathy = 0

default mood = 1 ##mood of non-route patient

default thirdfloor=False

## Notes ###########################
default nmoon1 = ""
default nmoon2 = ""
default nmoon3 = ""
default nmoon4 = ""
default nmoon5 = ""
default nmoon6 = ""
default nmoon7 = ""
default nmoon8 = ""
default nmoon9 = ""
default nmoon10 = ""
default nmoon11 = ""
default nmoon12 = ""
default nmoon13 = ""
default nmoon14 = ""
default nmoon15 = ""
default nmoon16 = ""
default nmoon17 = ""
default nmoon18 = ""
default nmoon19 = ""
default nmoon20 = ""

default nhermit1 = ""
default nhermit2 = ""
default nhermit3 = ""
default nhermit4 = ""
default nhermit5 = ""
default nhermit6 = ""
default nhermit7 = ""
default nhermit8 = ""
default nhermit9 = ""
default nhermit10 = ""
default nhermit11 = ""
default nhermit12 = ""
default nhermit13 = ""
default nhermit14 = ""
default nhermit15 = ""
default nhermit16 = ""
default nhermit17 = ""
default nhermit18 = ""
default nhermit19 = ""
default nhermit20 = ""

default ndevil1 = ""
default ndevil2 = ""
default ndevil3 = ""
default ndevil4 = ""
default ndevil5 = ""
default ndevil6 = ""
default ndevil7 = ""
default ndevil8 = ""
default ndevil9 = ""
default ndevil10 = ""
default ndevil11 = ""
default ndevil12 = ""
default ndevil13 = ""
default ndevil14 = ""
default ndevil15 = ""
default ndevil16 = ""
default ndevil17 = ""
default ndevil18 = ""
default ndevil19 = ""
default ndevil20 = ""

default ntower1 = ""
default ntower2 = ""
default ntower3 = ""
default ntower4 = ""
default ntower5 = ""
default ntower6 = ""
default ntower7 = ""
default ntower8 = ""
default ntower9 = ""
default ntower10 = ""
default ntower11 = ""
default ntower12 = ""
default ntower13 = ""
default ntower14 = ""
default ntower15 = ""
default ntower16 = ""
default ntower17 = ""
default ntower18 = ""
default ntower19 = ""
default ntower20 = ""

## Social Links ####################
default SunLink = 0
default TempLink = 0
default PrsLink = 0
default StarLink = 0

default GoldRouteFail = False

default SilverRouteBroken = False

default star = "???"
## Affection #######################
default GoldenHeart = 0
default Goldinteract = 0
default BlueHeart = 0
default RedHeart = 0
default SilverHeart = 0
default PurpleHeart = 0
default GreenHeart = 0
default submissive = 0
default dominant = 0

default personal = 0
default wrong = 0
default professional = 0

default devilhurtbird = False 
default Moonhandfriday = False

default DevilFail = False
## ILLUSTRATIONS ####################################################
image map = "cg/Map.png"
image map 2 = "cg/Map2.png"

image mcphone 1 = "cg/MCPhone1.png"
image mcphone 2 = "cg/MCPhone2.png"
image mcphone 3 = "cg/MCPhone3.png"

image pback 1 = "cg/p1.png"
image pback 2 = "cg/p2.png"
image pback 3 = "cg/p3.png"
image pback 6 = "cg/p1.png"
image pback 7 = "cg/p7.png"
image pback 8 = "cg/p8.png"
image pback 9 = "cg/p9.png"
image pback 10 = "cg/p10.png"
image pback 11 = "cg/p11.png"

image rback 0 = "cg/rpause.png"
image rback 1 = "cg/r1.png"
image rback 2 = "cg/r2.png"
image rback 3 = "cg/r3.png"
image rback 4 = "cg/r4.png"
image rback 5 = "cg/r5.png"
image rback 6 = "cg/r6.png"
image rback 7 = "cg/r7.png"
image rback 8 = "cg/r8.png"
image rback 9 = "cg/r9.png"

image sback 1 = "cg/s1.png"
image sback 2 = "cg/s2.png"
image sback 3 = "cg/s3.png"
image sback 4 = "cg/s4.png"
image sback 5 = "cg/s5.png"
image sback 6 = "cg/s6.png"
image sback 7 = "cg/s7.png"
image sback 8 = "cg/s8.png"
image sback 91 = "cg/s91.png"
image sback 92 = "cg/s92.png"
image sback 93 = "cg/s93.png"
image sback 10 = "cg/s10.png"
image sback 11 = "cg/s11.png"

image mcshock:
    "gui/f/black.png" with dissolve
    "cg/MCShock.png" with Dissolve(1.0)
image mcblood:
    "gui/f/black.png" with dissolve
    "cg/MCBlood.png" with Dissolve(1.0)
    
## BACKGROUNDS ######################################################
image bg front = "bg/FrontDay.png"
image bg frontsun = "bg/FrontSun.png"
image bg frontnight:
    "gui/f/black.png" with dissolve
    "bg/FrontNight.png" with Dissolve(1.0)
image bg greet = "bg/Reception.png"
image bg greetsun = "bg/ReceptionSun.png"
image bg greetnight:
    "gui/f/black.png" with dissolve
    "bg/ReceptionNight.png" with Dissolve(1.0)
image bg hallway = "bg/Hallway.png"
image bg hallwaynight:
    "gui/f/black.png" with dissolve
    "bg/HallwayNight.png" with Dissolve(1.0)
image bg cafe = "bg/Cafeteria.png"
image bg cafenight:
    "gui/f/black.png" with dissolve
    "bg/CafeteriaNight.png" with Dissolve(1.0)
image bg patients = "bg/PatientsHallway.png"
image bg patientsblur = "bg/PatientsHallwayblur.png"
image bg patientsnight:
    "gui/f/black.png" with dissolve
    "bg/PatientsNight.png" with Dissolve(1.0)
image bg closeXIX = "bg/CloseupXIX.png"
image bg closeXIX2 = "bg/CloseupXIX2.png"
image bg closeXV = "bg/CloseupXV.png"
image bg closeXV2 = "bg/CloseupXV2.png"
image bg central = "bg/CentralHall.png"
image bg centralsun = "bg/CentralSun.png"
image bg centralnight:
    "gui/f/black.png" with dissolve
    "bg/CentralNight.png" with Dissolve(1.0)
image bg centralthird = "bg/CenralThird.png"
image bg offices = "bg/Offices.png"
image bg officesnight:
    "gui/f/black.png" with dissolve
    "bg/OfficesNight.png" with Dissolve(1.0)
image bg doctor = "bg/Doctor.png"
image bg mc = "bg/MC.png"
image bg mcdark = "bg/MCdark.png"
image bg mcnight:
    "gui/f/black.png" with dissolve
    "bg/MCnight.png" with Dissolve(1.0)
image bg mcdesk = "bg/MCdesk.png"
image bg outside:
    "gui/f/black.png" with dissolve
    "bg/Outside.png" with Dissolve(1.0)
##image bg outsidesun = "bg/OutsideSun.png" with Dissolve(1.0)
image bg outsidenight:
    "gui/f/black.png" with dissolve
    "bg/OutsideNight.png" with Dissolve(1.0)
image bg desk = "bg/Desk.png"
image bg mcdeskdark = "bg/MCdeskdark.png"
image bg mcmoon = "bg/Moonenter.png"
image bg mchanged = "bg/Hangedenter.png"

image bg young = "bg/Young.png"
image bg officeiv = "bg/OfficeIV.png"
image bg thirdhall = "bg/Thirdhall.png"
image bg thirdhallblur = "bg/Thirdhallblur.png"
image bg thirdhallnight:
    "gui/f/black.png" with dissolve
    "bg/Thirdhallnight.png" with Dissolve(1.0)
image bg psychologist = "bg/Psychologist.png"

image bg dawn = "bg/Dawn.png"
image bg sun = "bg/Sunny.png"
image bg night = "bg/NightSky.png"
image bg sunset = "bg/Sunset.png"

image bg mcliving = "bg/Living.png"
image bg mclivingnight = "bg/LivingNight.png"
image bg mcbed="bg/MCbed.png"
image bg mcbednight="bg/MCbedNight.png"

image fired = "cg/fired.png"
## EFFECTS ##########################################################
image blood = "blood.png"
image drk 2 = "dark2.png"
image punchblood = "darkred.png"
image drk 3 = "darkred.png"

## SPRITES ##########################################################
##Julia
image jl neutral = "sprites/temperance/Neutral.png"
image jl talk = "sprites/temperance/Talk.png"
image jl neu = "sprites/temperance/Neu.png"
image jl neutalk = "sprites/temperance/Neutalk.png"
image jl smile = "sprites/temperance/Smile.png"
image jl blush = "sprites/temperance/Blush.png"
image jl angry = "sprites/temperance/Angry.png"
image jl angrytalk = "sprites/temperance/AngryTalk.png"
image jl gasp = "sprites/temperance/Gasp.png"
image jl calm = "sprites/temperance/Calm.png"
image jl calmtalk = "sprites/temperance/Calmtalk.png"
image jl calmsmile = "sprites/temperance/Calmsmile.png"
##Sue
image su neutral = "sprites/sun/Neutral.png"
image su smile = "sprites/sun/Smile.png"
image su happy = "sprites/sun/Happy.png"
image su gasp = "sprites/sun/Gasp.png"
image su talk = "sprites/sun/Talk.png"
image su sad = "sprites/sun/Sad.png"
image su sadtalk = "sprites/sun/SadTalk.png"
image su sadsmile = "sprites/sun/SadSmile.png"
image su angry = "sprites/sun/Angry.png"
image su angrytalk = "sprites/sun/AngryTalk.png"
image su neu = "sprites/sun/Neu.png"
image su cute = "sprites/sun/Cute.png"
image su laugh = "sprites/sun/Laugh.png"
##Elijah
image d neu = "sprites/hierophant/2Neu.png"
image d neutral = "sprites/hierophant/2Neutral.png"
image d smile = "sprites/hierophant/2Smile.png"
image d neutalk = "sprites/hierophant/2Neutalk.png"
image d smirk = "sprites/hierophant/2Smirk.png"
image d talk = "sprites/hierophant/2Talk.png"
image d gasp = "sprites/hierophant/2Gasp.png"
image d cold = "sprites/hierophant/2Cold.png"
image d coldsmile = "sprites/hierophant/2Coldsmile.png"
image d coldtalk = "sprites/hierophant/2Coldtalk.png"
image d sad = "sprites/hierophant/2Sad.png"
image d sadtalk = "sprites/hierophant/2Sadtalk.png"
image d pity = "sprites/hierophant/2Pity.png"
image d grit = "sprites/hierophant/2Grit.png"
image d siden = "sprites/hierophant/2Side.png"
image d sidetalk = "sprites/hierophant/2Sidetalk.png"
image d sidesmile = "sprites/hierophant/2Sidesmile.png"
image d regret = "sprites/hierophant/2Regret.png"
image d regretsmile = "sprites/hierophant/2Regretsmile.png"
image d regrettalk = "sprites/hierophant/2Regrettalk.png"
image d frust = "sprites/hierophant/2Frust.png"
image d frusttalk = "sprites/hierophant/2Frusttalk.png"
image d frustsmile = "sprites/hierophant/2Frustsmile.png"
image d shock = "sprites/hierophant/2Shock.png"
image d freeze = "sprites/hierophant/2Freeze.png"
image d fury = "sprites/hierophant/2Fury.png"
image d yell = "sprites/hierophant/2Yell.png"
image d fear = "sprites/hierophant/2Fear.png"
image d pant = "sprites/hierophant/2Pant.png"
image d calm = "sprites/hierophant/2Calm.png"
image d calmsmile = "sprites/hierophant/2Calmsmile.png"
image d calmtalk = "sprites/hierophant/2Calmtalk.png"
image d foc = "sprites/hierophant/2Focus.png"
image d foctalk = "sprites/hierophant/2Focustalk.png"
image d pain = "sprites/hierophant/2Pain.png"
image d grief = "sprites/hierophant/2Grief.png"
image d grieftalk = "sprites/hierophant/2Grieftalk.png"
image d griefsmile = "sprites/hierophant/2Griefsmile.png"
image d suffer = "sprites/hierophant/2Suffer.png"
image d focused = "sprites/hierophant/2Focus.png"
image d focustalk = "sprites/hierophant/2Focustalk.png"
image d surp = "sprites/hierophant/2Surp.png"
##Tom
image t neu = "sprites/tower/Neu.png"
image t neutral = "sprites/tower/Neutral.png"
image t neutalk = "sprites/tower/Neutalk.png"
image t smile = "sprites/tower/Smile.png"
image t talk = "sprites/tower/Talk.png"
image t smirk = "sprites/tower/Smirk.png"
image t gasp = "sprites/tower/Gasp.png"
image t angry = "sprites/tower/Angry.png"
image t angrytalk = "sprites/tower/Angrytalk.png"
image t regret = "sprites/tower/Regret.png"
image t regrettalk = "sprites/tower/Regrettalk.png"
image t regretsmile = "sprites/tower/Regretsmile.png"
image t sad = "sprites/tower/Sad.png"
image t sadtalk = "sprites/tower/Sadtalk.png"
image t evil = "sprites/tower/Evil.png"
image t trigger = "sprites/tower/Trigger.png"
image t siden = "sprites/tower/Siden.png"
image t sidetalk = "sprites/tower/Sidetalk.png"
image t sidesmile = "sprites/tower/Sidesmile.png"
image t frust = "sprites/tower/Frust.png"
image t frusttalk = "sprites/tower/Frusttalk.png"
image t hurt = "sprites/tower/Hurt.png"
image t hurttalk = "sprites/tower/HurtTalk.png"
image t pa = "sprites/tower/PA.png"
image t patalk = "sprites/tower/PAtalk.png"
image t calm = "sprites/tower/Calm.png"
image t calmtalk = "sprites/tower/Calmtalk.png"
image t mad = "sprites/tower/Mad.png"
image t madtalk = "sprites/tower/Madtalk.png"

image t full = "sprites/tower/Full.png"
##Edward
image hg hostile = "sprites/hanged/Hostile.png"
image hg talk = "sprites/hanged/Talk.png"
image hg neutral = "sprites/hanged/Neutral.png"
image hg neu = "sprites/hanged/Neu.png"
image hg smile = "sprites/hanged/Smile.png"
image hg happy = "sprites/hanged/Happy.png"
image hg angry = "sprites/hanged/Angry.png"
image hg sad = "sprites/hanged/Sad.png"
image hg sadtalk = "sprites/hanged/SadTalk.png"
image hg pale = "sprites/hanged/Pale.png"
image hg shock = "sprites/hanged/Shock.png"
image hg dread = "sprites/hanged/Dread.png"
image hg pant = "sprites/hanged/Pant.png"
image hg gasp = "sprites/hanged/Gasp.png"
image hg calm = "sprites/hanged/Calm.png"
image hg calmtalk = "sprites/hanged/CalmTalk.png"
image hg pain = "sprites/hanged/Pain.png"
image hg grief = "sprites/hanged/Grief.png"
image hg blush = "sprites/hanged/Blush.png"
image hg smileblush = "sprites/hanged/SmileBlush.png"
image hg cry = "sprites/hanged/Cry.png"
image hg scream = "sprites/hanged/Scream.png"
image hg cry2 = "sprites/hanged/Cry2.png"
image hg cry2talk = "sprites/hanged/Cry2talk.png"
image hg crysmile = "sprites/hanged/Crysmile.png"
image hg hiden = "sprites/hanged/Hiden.png"
image hg full = "sprites/hanged/Full.png"
##Charlie
image h neu = "sprites/hermit/Neutral.png"
image h smile = "sprites/hermit/Smile.png"
image h happy = "sprites/hermit/Happy.png"
image h bored = "sprites/hermit/Bored.png"
image h gasp = "sprites/hermit/Gasp.png"
image h talk = "sprites/hermit/Talk.png"
image h angry = "sprites/hermit/Angry.png"
image h angrytalk = "sprites/hermit/AngryTalk.png"
image h evil = "sprites/hermit/Evil.png"
image h sad = "sprites/hermit/Sad.png"
image h sadsmile = "sprites/hermit/SadSmile.png"
image h sadtalk = "sprites/hermit/SadTalk.png"
image h frust = "sprites/hermit/Frust.png"
image h frusttalk = "sprites/hermit/FrustTalk.png"
image h siden = "sprites/hermit/SideNeu.png"
image h sidesmile = "sprites/hermit/SideSmile.png"
image h sidetalk = "sprites/hermit/SideTalk.png"
image h sideblush = "sprites/hermit/SideBlush.png"
image h blush = "sprites/hermit/SmileBlush.png"
image h tsun = "sprites/hermit/Tsundere.png"
image h cute = "sprites/hermit/Cute.png"
image h kawaii = "sprites/hermit/Kawaii.png"
image h laugh = "sprites/hermit/Laugh.png"
image h laughblush = "sprites/hermit/LaughBlush.png"
image h full = "sprites/hermit/Full.png"

image h dead = "sprites/hermit/Dead.png"
image h deadtalk = "sprites/hermit/DeadTalk.png"
image h deadsmile = "sprites/hermit/DeadSmile.png"
image h kek = "sprites/hermit/kek.png"
image h surp = "sprites/hermit/Surp.png"
image h regret = "sprites/hermit/Regret.png"
image h regretsmile = "sprites/hermit/RegretSmile.png"
image h regrettalk = "sprites/hermit/RegretTalk.png"
image h frusttsmile = "sprites/hermit/FrustSmile.png"

##Michael
image dv neutral = "sprites/devil/Neutral.png"
image dv neu = "sprites/devil/Neu.png"
image dv smile = "sprites/devil/Smile.png"
image dv talk = "sprites/devil/Talk.png"
image dv hes = "sprites/devil/Hes.png"
image dv smirk = "sprites/devil/Smirk.png"
image dv breath = "sprites/devil/Breath.png"
image dv neutalk = "sprites/devil/Neutalk.png"
image dv angry = "sprites/devil/Angry.png"
image dv angrytalk = "sprites/devil/AngryTalk.png"
image dv sad = "sprites/devil/Sad.png"
image dv sadtalk = "sprites/devil/SadTalk.png"
image dv sadsmile = "sprites/devil/SadSmile.png"
image dv cute = "sprites/devil/Cute.png"
image dv blush = "sprites/devil/Blush.png"
image dv shock = "sprites/devil/Shock.png"
image dv siden = "sprites/devil/Siden.png"
image dv sidesmile = "sprites/devil/SideSmile.png"
image dv sidetalk = "sprites/devil/SideTalk.png"
image dv devil = "sprites/devil/Devil.png"
image dv frust = "sprites/devil/Frust.png"
image dv frusttalk = "sprites/devil/Frusttalk.png"
image dv moment = "sprites/devil/Moment.png"
image dv pant = "sprites/devil/Pant.png"
image dv gasp = "sprites/devil/Gasp.png"
image dv dark = "sprites/devil/Dark.png"
image dv kh = "sprites/devil/Khhh.png"
image dv kh2 = "sprites/devil/Khhh2.png"
image dv darktalk = "sprites/devil/DarkTalk.png"
image dv yandere = "sprites/devil/Yandere.png"
image dv darkgasp = "sprites/devil/Darkgasp.png"
image dv creepy = "sprites/devil/Creepy.png"
image dv noeyes = "sprites/devil/NoEyes.png"
image dv notalk = "sprites/devil/NoTalk.png"
image dv twitch = "sprites/devil/Twitch.png"
image dv darkblush = "sprites/devil/DarkBlush.png"
image dv tsun = "sprites/devil/Tsun.png"
image dv full = "sprites/devil/Full.png"
##William
image w neutral = "sprites/moon/Neutral.png"
image w smile = "sprites/moon/Smile.png"
image w talk = "sprites/moon/Talk.png"
image w angry = "sprites/moon/Angry.png"
image w angrytalk = "sprites/moon/AngryTalk.png"
image w evil = "sprites/moon/Evil.png"
image w sad = "sprites/moon/Sad.png"
image w sadtalk = "sprites/moon/SadTalk.png"
image w sadsmile = "sprites/moon/SadSmile.png"
image w tense = "sprites/moon/Tense.png"
image w tensetalk = "sprites/moon/TenseTalk.png"
image w siden = "sprites/moon/Siden.png"
image w sidesmile = "sprites/moon/SideSmile.png"
image w sidetalk = "sprites/moon/SideTalk.png"
image w frust = "sprites/moon/Frust.png"
image w frustsmile = "sprites/moon/FrustSmile.png"
image w frusttalk = "sprites/moon/FrustTalk.png"
image w regret = "sprites/moon/Regret.png"
image w regretsmile = "sprites/moon/RegretSmile.png"
image w regrettalk = "sprites/moon/RegretTalk.png"
image w blush = "sprites/moon/BlushSide.png"
image w calm = "sprites/moon/Calm.png"
image w calmsmile = "sprites/moon/CalmSmile.png"
image w pain = "sprites/moon/Pain.png"
image w fear = "sprites/moon/Fear.png"
image w shock = "sprites/moon/Shock.png"
image w crazy = "sprites/moon/Crazy.png"
image w gasp = "sprites/moon/Gasp.png"
image w crit = "sprites/moon/Crit.png"
image w wrong = "sprites/moon/wrong.png"
image w yuri = "sprites/moon/Yuri.png"
image w paintalk = "sprites/moon/Paintalk.png"
image w dread = "sprites/moon/Dread.png"
image w dis = "sprites/moon/Dis.png"
image w cry = "sprites/moon/Cry.png"
image w scream = "sprites/moon/Scream.png"
image w crysmile = "sprites/moon/Crysmile.png"
image w tsun = "sprites/moon/Tsun.png"
image w broke = "sprites/moon/Break.png"
image w broketalk = "sprites/moon/BreakTalk.png"
image w scaredblush = "sprites/moon/Scaredblush.png"
image w disblush = "sprites/moon/DisBlush.png"
image w full = "sprites/moon/Full.png"
image w hiden = "sprites/moon/Hiden.png"
##Elizabeth
image e neutral = "sprites/priestess/Neutral.png"
image e talk = "sprites/priestess/Talk.png"
image e smirk = "sprites/priestess/Smirk.png"
image e neu = "sprites/priestess/Neu.png"
image e neutalk = "sprites/priestess/NeuTalk.png"
image e smile = "sprites/priestess/Smile.png"
image e angry = "sprites/priestess/Angry.png"
image e angrytalk = "sprites/priestess/AngryTalk.png"
image e conf = "sprites/priestess/Conf.png"
image e bite = "sprites/priestess/Bite.png"
image e calm = "sprites/priestess/Calm.png"
image e calmtalk = "sprites/priestess/CalmTalk.png"
image e calmsmile = "sprites/priestess/Calmsmile.png"
image e foc = "sprites/priestess/Foc.png"
image e foctalk = "sprites/priestess/Foctalk.png"
image e focsmile = "sprites/priestess/Focsmile.png"
image e pain = "sprites/priestess/Pain.png"
image e paintalk = "sprites/priestess/PainTalk.png"
image e painsmile = "sprites/priestess/Painsmile.png"
image e bored = "sprites/priestess/Bored.png"
image e boretalk = "sprites/priestess/Boretalk.png"
image e boresmile = "sprites/priestess/Boresmile.png"
image e baka = "sprites/priestess/Baka.png"
image e bakatalk = "sprites/priestess/Bakatalk.png"
image e bakasmile = "sprites/priestess/Bakasmile.png"
image e regret = "sprites/priestess/Regret.png"
image e regrettalk = "sprites/priestess/RegretTalk.png"
image e regretsmile = "sprites/priestess/RegretSmile.png"
image e tsun = "sprites/priestess/Tsun.png"
##Milena
image l neu = "sprites/lovers/Neu.png"
image l neutral = "sprites/lovers/Neutral.png"
image l talk = "sprites/lovers/Talk.png"
image l smile = "sprites/lovers/Smile.png"
image l smirk = "sprites/lovers/Smirk.png"
image l gasp = "sprites/lovers/Gasp.png"
image l blush = "sprites/lovers/Blush.png"
image l cute = "sprites/lovers/Cute.png"
image l happy = "sprites/lovers/Happy.png"
image l laugh = "sprites/lovers/Laugh.png"
image l left = "sprites/lovers/Left.png"
image l siden = "sprites/lovers/Siden.png"
image l sidetalk = "sprites/lovers/Sidetalk.png"
image l sidesmile = "sprites/lovers/Sidesmile.png"
image l sidesad = "sprites/lovers/Sidesad.png"
image l sidepity = "sprites/lovers/Sidepity.png"
image l sidesadtalk = "sprites/lovers/Sidesadtalk.png"
image l sideangry = "sprites/lovers/Sideangry.png"
image l sideangrytalk = "sprites/lovers/Sideangrytalk.png"
image l sad = "sprites/lovers/Sad.png"
image l sadsmile = "sprites/lovers/Sadsmile.png"
image l sadtalk = "sprites/lovers/Sadtalk.png"
image l angry = "sprites/lovers/Angry.png"
image l angrytalk = "sprites/lovers/Angrytalk.png"
image l regret = "sprites/lovers/Regret.png"
image l regrettalk = "sprites/lovers/Regrettalk.png"
image l pity = "sprites/lovers/Pity.png"
image l shy = "sprites/lovers/Shy.png"
image l frust = "sprites/lovers/Frust.png"
image l frusttalk = "sprites/lovers/Frusttalk.png"
image l freeze = "sprites/lovers/Freeze.png"
image l pant = "sprites/lovers/Pant.png"
image l shock = "sprites/lovers/Shock.png"
image l fear = "sprites/lovers/Fear.png"
image l feartalk = "sprites/lovers/Feartalk.png"
##Charles
image s neu = "sprites/star/Neu.png"
image s neutral = "sprites/star/Neutral.png"
image s smile = "sprites/star/Smile.png"
image s talk = "sprites/star/Talk.png"
image s smirk = "sprites/star/Smirk.png"
image s happy = "sprites/star/Happy.png"
image s gasp = "sprites/star/Gasp.png"
image s neutalk = "sprites/star/NeuTalk.png"
image s blush = "sprites/star/Blush.png"
image s angry = "sprites/star/Angry.png"
image s angrytalk = "sprites/star/AngryTalk.png"
image s evil = "sprites/star/Evil.png"
image s sad = "sprites/star/Sad.png"
image s sadtalk = "sprites/star/SadTalk.png"
image s sadsmile = "sprites/star/SadSmile.png"
image s cute = "sprites/star/Cute.png"
image s laugh = "sprites/star/Laugh.png"
image s kawaii = "sprites/star/Kawaii.png"
image s blush2 = "sprites/star/LaughBlush.png"
image s calm = "sprites/star/Calm.png"
image s calmtalk = "sprites/star/CalmTalk.png"
image s calmsmile = "sprites/star/CalmSmile.png"
image s pain = "sprites/star/Pain.png"
image s paintalk = "sprites/star/PainTalk.png"

## VARIOUS IMAGES ###################################################
image save = "bg/save.png"
image folder = "bg/folder.png"

image file1 = "cg/MoonFile.png"
image file2 = "cg/HermitFile.png"
image file3 = "cg/TowerFile.png"
image file4 = "cg/DevilFile.png"

## ANIME CUTSCENES ##################################################
image ac 1:
    "ac/11.png"
    pause 0.5
    "ac/12.png"
    pause 0.06
    "ac/13.png"
    pause 1
    "ac/14.png"
    pause 0.06
    "ac/15.png"
    pause 0.06
    "ac/14.png"
    pause 0.06
    "ac/13.png"
    pause 1
image ac 31 = "ac/31.png"
image ac 32 = "ac/32.png"
image ac 33 = "ac/33.png"

## AFFECTION ########################################################
image drk = "hrt/drk.png"
image gr 1 = "hrt/gr1.png"
image gr 2 = "hrt/gr2.png"
image gr 3 = "hrt/gr3.png"

image p 2 = "hrt/p2.png"
image p 3 = "hrt/p3.png"

image r 1 = "hrt/r1.png"
image r 2 = "hrt/r2.png"
image r 3 = "hrt/r3.png"

image b 1 = "hrt/b1.png"
image b 2 = "hrt/b2.png"
image b 3 = "hrt/b3.png"

image s 1 = "hrt/s1.png"
image s 2 = "hrt/s2.png"
## SIDE IMAGES ######################################################
image side neu = "sprites/mc/Neu.png"
image side neutral="sprites/mc/Neutral.png"
image side smile="sprites/mc/Smile.png"
image side talk="sprites/mc/Talk.png"
image side happy="sprites/mc/Happy.png"
image side gasp="sprites/mc/Gasp.png"
image side conf="sprites/mc/Conf.png"
image side sad="sprites/mc/Sad.png"
image side sadtalk="sprites/mc/Sadtalk.png"
image side angry="sprites/mc/Angry.png"
image side angrytalk="sprites/mc/Angrytalk.png"
image side sadsmile="sprites/mc/Sadsmile.png"
image side regret="sprites/mc/Regret.png"
image side regrettalk="sprites/mc/Regrettalk.png"
image side frust="sprites/mc/Frust.png"
image side frusttalk="sprites/mc/Frusttalk.png"
image side frustsmile="sprites/mc/Frustsmile.png"
image side bored="sprites/mc/Bored.png"
image side boretalk="sprites/mc/Boretalk.png"
image side boresmile="sprites/mc/Boresmile.png"
image side fab="sprites/mc/Fab.png"
image side fabtalk="sprites/mc/Fabtalk.png"
image side flirt="sprites/mc/Flirt.png"
image side blush="sprites/mc/Blush.png"
image side blush2="sprites/mc/Blush2.png"
image side tsun="sprites/mc/Tsun.png"
image side uncom="sprites/mc/Uncom.png"
image side pity="sprites/mc/Pity.png"
image side serious="sprites/mc/Serious.png"
image side cute="sprites/mc/Cute.png"
image side kawaii="sprites/mc/Kawaii.png"
image side laugh="sprites/mc/Laugh.png"
image side freeze="sprites/mc/Freeze.png"
image side shock="sprites/mc/Shock.png"
image side wut="sprites/mc/Wut.png"
image side hfh="sprites/mc/HFH.png"
image side fear="sprites/mc/Fear.png"
image side scream="sprites/mc/Scream.png"
image side cry="sprites/mc/Cry.png"
image side crytalk = "sprites/mc/Crytalk.png"
image side yell = "sprites/mc/Yell.png"
image side trigger = "sprites/mc/Trigger.png"
image side sjw = "sprites/mc/SJW.png"
image side blushu = "sprites/mc/Blushu.png"
image side confusion = "sprites/mc/Confusion.png"
image side bloody = "sprites/mc/Bloody.png"
image side bloodtalk = "sprites/mc/BloodyTalk.png"

## THE GAME BEGINS HERE ########################################################
################################################################################
label tour:
    scene bg greet with dissolve
    pause 1
    "Entering the hospital, I find myself in the reception area."
    "I glance around the room only to see a pair of green eyes looking back at me."
    scene black with dissolve
    show ac 1 with dissolve
    $renpy.pause(3,hard=True)
    hide ac 1 with dissolve
    scene bg greet with dissolve
    play music "ost/hospital.wav" fadein 8
    show jl neutral with dissolve
    "It seems she's been waiting for me to notice her."
    "I approach her desk slowly."
    re "Good morning..."
    "She doesn't seem too friendly... Not like I'm not used to it."
    if persistent.Fool:
        play sound "page.ogg" fadein 1
        show skipreminder with dissolve
        $renpy.pause()
        hide skipreminder with dissolve
    show jl talk with dissolve
    re "What brings you here, Miss?"
    show jl neutral with dissolve
    m neu "..."
    "I'm suddenly at a loss of words - I'm finally here..!"
    "I really need to focus."
    show jl angrytalk with dissolve
    re "Excuse me, Miss? If you have no business here, please leave."
    m gasp "I'm sorry, I didn't-"
    show jl calm with dissolve
    if easymeter: 
        show screen easymeter
        show screen empathymeter
    "..."
    show jl neutral with dissolve
    m talk "I applied for a job here."
    re "I need to check that before I let you in..."
    "Right... Nothing out of the ordinary."
     
label name:
    $name = renpy.input("Your first name, please", allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZńŃśŚĆćłŁęĘąĄóÓŻżŹź", length = 12)
    $name = name.strip()
    if name == "" or name == "...":
        re "Well...?"
        jump name
    elif name == "Lol" or name == "lol" or name == "LOL":
        show jl angry with dissolve
        re "You can't be serious..."
        jump name
    elif name == "Kurwa" or name == "kurwa" or name == "Kurde" or name == "kurde":
        show jl angrytalk with dissolve
        re "Nie przeklinaj! To miejsce publiczne..."
        return
    elif name == "fuck" or name == "Fuck" or name == "bitch" or name == "Bitch" or name == "shit" or name == "Shit":
        show jl angrytalk with dissolve
        re "What...? If that's a joke, I don't think it's funny."
        return
    elif name == "Alice":
        "She looks at me with an unreadable expression on her face."
        "What's that about...?"
        m angrytalk "That's my name."
    elif name == "Julia":
        show jl smile with dissolve
        re "Really? That's... kind of funny, actually."
        show jl neutral with dissolve
    elif name == "Elizabeth":
        re "I think I heard that name somewhere around here..."
    elif name == "Jane":
        "It's kind of strange, but that's my name..."
    elif name == "Sue":
        show jl smile with dissolve
        re "Sue? That's just perfect..."
    elif name == "Nekora":
        show jl smile with dissolve
        re "Stay magical, my friend ~"
    else:
        re "Okay then..."
    show jl talk with dissolve
    re "Umm... Let me see..."
    show jl neu with dissolve
    re "Oh, right."
    show jl talk with dissolve
    re "[name] Hart, correct? The psychologist?"
    re "We were looking for one since the position became... available recently."
    re "Anyway, I hope you're qualified - we can't hire just anyone here. I'm sure you know why..."
    show jl neutral with dissolve
    m talk "I understand."
    re "Give me a moment..."
    "The nurse takes out a cellphone and calls someone."
    show jl talk with dissolve
    re "Are you busy...?"
    re "That's good... listen, I need you to guide someone to {color=#a2ef83}Dr. Sharpe's office."
    show jl smile with dissolve
    re "...Thanks."
    show jl neutral with dissolve
    "She looks at me again."
    show jl angry with dissolve
    re "Aren't you a bit... young?"
    show jl neutral with dissolve
    if tutorials:
        call screen tuto1
    menu:
        "Is that a problem?":
            m angrytalk "Is that a problem?"
            re "It is."
            show jl angry with dissolve
            re "We don't hire people with no previous experience."
            show jl talk with dissolve
            re "But I suppose you have what it takes if you were invited for a {color=#a2ef83}job interview..."
        "I'm not that young...":
            m gasp "I'm not that young..."
            show jl talk with dissolve
            re "I assume whoever invited you here for {color=#a2ef83}that job interview{/color} knew what they were doing..."
        "I have all the necessary experience":
            "I start digging around my bag to find something to convince her."
            m gasp "I can-"
            show jl smile with dissolve
            re "Save that for your {color=#a2ef83}job interview."
    show jl neutral with dissolve
    re "..." 
    "Another moment of awkward silence passes before a door flies open, revealing a different nurse."
    show jl smile with dissolve
    re "Well, good luck."
    menu:
        "Thanks":
            $empathy += 1
            m smile "Thank you."
            re "Right... see you around, [name]."
        "Luck?":
            m angry "I don't need luck."
            show jl talk with dissolve
            re "Don't get overconfident - you won't get through that interview if you will."
        "{color=#a2ef83}Stay silent":
            show jl neutral with dissolve
            re "...."
    scene bg hallway with dissolve
    stop music fadeout 8
    show su neutral with moveinright
    pause 0.5
    show su happy with dissolve
    gu "Hello!"
    if tutorials:
        call screen tuto2
    show su smile with dissolve
    gu "{color=#67beea}Julia{/color} - you know, from the reception, asked me to lead you to an interview."
    $persistent.Julia=True
    if not persistent.Julialast=="Watts":
        $persistent.Julialast="????"
    play sound "chars.ogg" 
    show screen notify("{size=24} Your Characters Info screen has been updated!")
    show su cute with dissolve
    gu "But... I have some spare time, so if you want I can show you around as well."
    show su laugh with dissolve
    gu "It's easy to get lost here at first, heh..."
    show su smile with dissolve
    menu:
        "{color=#67beea}Full tour":
            $empathy += 1
            m smile "I'd like a full tour, if that's fine."
            show su gasp with dissolve
            gu "Really?" 
            show su happy with dissolve
            gu "That's great, follow me!"
            play music "ost/sunny.wav" fadein 5
            play sound "footsteps.ogg" fadein 1
            show bg cafe with dissolve
            gu "{color=#67beea}The cafeteria{/color}. Patients eat here, so it gets pretty crowded at times."
            show su smile with dissolve
            menu:
                "How many patients eat here?":
                    show su talk with dissolve
                    gu "Currently, I think we have around thirty patients."
                    show su neu with dissolve
                    gu "Not all of them are allowed to eat here with the rest, though..."
                    m talk "Why is that?"
                    show su talk with dissolve
                    gu "For the others' safety - and their own."
                "Can I eat here as well?":
                    $empathy += 1
                    $empathymeter = True
                    show su gasp with dissolve
                    m talk "Is that an option?"
                    gu "If you want to, I guess..."
                    show su talk with dissolve
                    gu "I'm not sure. You'd have to arrange that with the staff in the kitchen and everything..."
                    m angrytalk "There's no need for that."
                    show su neu with dissolve
                    m neu "I can eat with the patients and eat the same they do."
                    m angry "Why should I be treated differently?"
                    show su neutral with dissolve
                    m frust "It doesn't seem fair."
                    show su talk with dissolve
                    gu "You know what?"
                    show su cute with dissolve
                    gu "You're a lot different than the other doctors and psychologists here."
                    show su smile with dissolve
                    gu "It's a nice change."
                "No questions.":
                    m talk "Let's go."
                    show su gasp with dissolve
                    "Oh, right."
                    show su neutral with dissolve
            scene black with dissolve
            "The nurse opens a locked door and we enter a staircase."
            gu "Careful, it's a bit narrow..."
            menu:
                "Is that safe?":
                    gu "Well, uhh... I don't know."
                    gu "There weren't any accidents so far."
                    "We start walking up the set of stairs together."
                    gu "It's an old building, not everything was renovated - it used to be worse, I heard."
                "Thanks for the warning.":
                    $empathy += 1
                    gu "Oh? No problem... I'm just doing my job."
                    m flirt "And you're doing well."
            scene bg patients with dissolve
            "We enter a long hallway."
            show su smile with dissolve
            gu "Well, here it is - {color=#67beea}the second floor{/color}."
            show su neutral with dissolve
            gu "As you can see, this is where {color=#67beea}patients' rooms{/color} are located."
            show su neu with dissolve
            gu "It's also where you will work - given that you're hired, of course."
            menu:
                "How many patients live in one room?":
                    $empathy+=1
                    gu "Usually we can afford single rooms, some of them have two patients inside."
                    show su talk with dissolve
                    gu "It really depends, but generally we never had to fit more than two people in one room."
                    show su neu with dissolve
                    m neu "That's good."
                "How much time do patients spend outside their rooms?":
                    $empathy += 1
                    show su talk with dissolve
                    gu "Most of the day, really."
                    show su sadtalk with dissolve
                    gu "Save for some... \"difficult\" patients, they see psychologists and psychiatrists every day,"
                    show su neu with dissolve
                    gu "We organize group activities quite often, which are optional."
                    show su smile with dissolve
                    gu "Patients can go everywhere on the first and second floor, as long as they're watched over by someone."
                    show su laugh with dissolve
                    gu "So we really aren't keeping them locked in here, heh."
                "When do you lock the rooms?":
                    show su talk with dissolve
                    gu "We lock all rooms for the night, after 8 PM."
                    show su angry with dissolve
                    gu "No-one can leave their room until 8 AM, when therapy sessions usually start."
                    show su talk with dissolve
                    gu "Of course, we watch over patients at all times, especially outside their rooms. "
                    show su cute with dissolve
                    gu "So there's no reason to worry about anyone's safety."
            show su smile with dissolve
            "We walk quietly through the hallway between patients' rooms. "
            show su neu with dissolve
            "No matter how I look at it, I feel uncomfortable here..."
            "Like I'm trapped."
            "I don't like this part of the building at all..."
            stop sound fadeout 0.5 
            show su neutral with dissolve
            "Suddenly, the nurse stops near the end of the hallway."
            show su talk with dissolve
            gu "Behind this wall is the {color=#67beea}nurses' office{/color}. We usually spend breaks here."
            show su sadsmile with dissolve
            gu "Honestly, we don't have many of them - we're more busy than you'd think."
            show su talk with dissolve
            gu "Oh, and from there you can get to {color=#67beea}room XXI{/color} - the isolated one."
            menu:
                "What do you like to do on breaks?":
                    $empathy += 1
                    show su gasp with dissolve
                    "She seems surprised that I asked about her."
                    show su neu with dissolve
                    gu "Me?"
                    show su sadsmile with dissolve
                    gu "I try to avoid this room - I prefer to walk around the building to make sure everything is fine, talk to people, you know..."
                    show su cute with dissolve
                    gu "I often spend breaks with Julia, if she's free as well - we're good friends."
                "Is it empty now?":
                    show su sad with dissolve
                    gu "Oh, no - there's always someone in there, just to watch over room XXI."
                    show su talk with dissolve
                    gu "It's where aggressive patients are moved sometimes..."
                    show su sadsmile with dissolve
                    gu "I don't think it's occupied right now, thankfully."
                "How are nurses treated here?":
                    $empathy += 1 
                    show su angry with dissolve
                    gu "Why do you ask?"
                    show su neu with dissolve
                    m talk "You do lots of work and you're sometimes pushed around by the doctors."
                    m serious "Does that happen here as well?"
                    show su gasp with dissolve
                    gu "Oh... I don't know, I never really felt... mistreated here."
                    show su sadsmile with dissolve
                    gu "Dr. Sharpe can be cold at times, but he appreciates what we do."
                    show su cute with dissolve
                    gu "I think I'm speaking for all nurses here."
                    show su smile with dissolve
                    m smile "I'm glad to hear that."
            play sound "footsteps.ogg" fadein 0.5
            show bg central with dissolve
            "We move to a spacious room connecting two hallways and the nurses' office."
            show su smile with dissolve
            gu "This is {color=#67beea}the central hall{/color}."
            gu "It's one of the few parts of the orginal building that was never changed since the XIXth century."
            show su talk with dissolve
            gu "To be honest, it's good to have an open space between all these narrow corridors."
            show su smile with dissolve
            stop sound 
            gu "You can even see {color=#67beea}the third floor{/color} from here."
            show su neu with dissolve
            gu "If you get chosen for the nightshift, that's where you'll stay."
            gu "We won't go there today, though."
            show su talk with dissolve
            gu "Any questions...?"
            show su neutral with dissolve
            gu "I guess not - we're nearly there, too, so let's go."
            play sound "footsteps.ogg" fadein 0.5
            show bg offices with dissolve
            show su neu with dissolve
            "Another narrow hallway... this one is slightly more comfortable for me."
            gu "This is where our psychiatrists and psychologists have their {color=#67beea}offices."
            "So, this is it... My job interview will soon begin."
            stop sound 
            "I was so caught up in the tour I nearly forgot about it until now."
            "I wonder which of these doors I'll have to enter..."
        "{color=#67beea}Quick tour":
            m talk "Just a quick walk around the place should do."
            play music "ost/hospital.wav" fadein 4
            show su talk with dissolve
            gu "That's... probably smart."
            show su sadtalk with dissolve
            gu "I wouldn't want you to be late because of me..."
            show su neu with dissolve
            play sound "footsteps.ogg" fadein 0.5
            scene bg cafe with dissolve
            "We passed by {color=#67beea}the cafeteria..."
            "This must be where patients eat their meals."
            "I wonder if I'm going to eat here as well..."
            scene black with dissolve
            "We go up a narrow staircase to get to {color=#67beea}the second floor."
            scene bg patients with dissolve
            "This must be where patients' rooms are located."
            "Despite the nurse's encouraging smile, I feel unsettled by this place."
            "We pass through quickly."
            scene bg central with dissolve
            "The open space feels much more inviting than the previous rooms. "
            "I'm reminded of how old the building must be."
            scene bg offices with dissolve
            stop sound 
            "This is it."
            "My job interview will take place behind one of these doors."
        "Let's hurry":
            m angrytalk "No, thanks."
            play music "ost/hospital.ogg" fadein 4
            show su talk with dissolve
            gu "Sure, let's get going."
            scene black with dissolve
            "We make our way through the hospital quickly."
            "I feel like I'll regret not asking for a tour."
            show bg offices with dissolve
            "This is it."
            "For the first time I stop - my interview will soon begin."
    show su neu with dissolve
    gu "Are you nervous about the interview?"
    menu:
        "Some advice, please?":
            show su talk with dissolve
            gu "I mean... Dr. Sharpe can be a bit harsh at first, but it's only for the good of the patients."
            show su smile with dissolve
            gu "Just {color=#67beea}stay professional, speak only when asked to and you should be fine."
            m conf "Alright then... Thanks."
        "I'm not.":
            gu "Good - really, there's nothing to worry about."
            show su happy with dissolve
            gu "You'll do great!"
            show su smile with dissolve
        "Let's just get it over with...":
            show su talk with dissolve
            gu "Right."
            show su smile with dissolve
    if empathy >= 4:
        gu "I'll wait for you outside, so we can talk once you're done."
        $SunLink = 1
        play sound "knock.ogg" 
        stop music fadeout 3
        "The nurse knocks on one of the doors and looks at me with an encouraging smile."
        show su cute with dissolve
        gu "Good luck~"
    else:
        $SunLink = 0
        gu "...."
        show su neutral with dissolve
        gu "I should probably go now. My break is nearly over..."
        stop music fadeout 4
        m neu "Sure, I can handle myself."
        hide su with moveoutright
        "The nurse leaves the way we came."
        "What am I waiting for...?"
        play sound "knock.ogg" 
        "I knock on the door before I can hesitate and overthink it."
    d "Come in."
    show drk with dissolve
    "{i}Would you like to save your game?"
    menu:
        "Yes":
            show text "{size=100}{color=#ffffff}Before\njob interview":
                ypos 300
            $renpy.pause()
            $ renpy.call_in_new_context("_game_menu")
        "No":
            pass
    hide drk with dissolve
    scene bg doctor with dissolve
    "I enter the office slowly."
    if easymeter:
        show screen greenmeter
    show d siden with dissolve
    play music "ost/hier.ogg" fadein 5
    "The man sitting behind the desk must be Dr. Sharpe, the psychiatrist."
    "I expected him to be older..."
    show d neutral with dissolve
    "Once I enter the office, he looks up from the documents on his desk."
    show d talk with dissolve
    d "[name] Hart?"
    show d cold with dissolve
    m talk "That's right. I..."
    show d coldtalk with dissolve
    d "You are here for the job interview?"
    show d neu with dissolve
    "I nod, realising I should say as little as possible."
    show d neutalk with dissolve
    d "Take a seat, please."
    show d neutral with dissolve
    "I sit down in a chair on the other side of his desk. He doesn't seem to be in a hurry."
    show d talk with dissolve
    d "You applied for a job here as a psychologist, correct?"
    show d neutral with dissolve
    m "I did."
    show d cold with dissolve
    "He pauses and looks at me briefly."
    show d coldtalk with dissolve
    d "Someone of your age might not be suited to work here..."
    show d sidetalk with dissolve
    d "A fragile young mind such as yours is likely to be unprepared for what you may encounter here."
    show d siden with dissolve
    menu:
        "Are you implying that I'm inexperienced?":
            $GreenHeart -= 1
            show d neutral with dissolve
            d "I was merely warning you, Ms.  Hart."
            show d talk with dissolve
            d "You might want to reconsider your choice of a workplace if you took it personally."
            show d neu with dissolve
        "I am prepared.":
            show d smirk with dissolve
            d "We will see about that, Ms.  Hart."
            show d neu with dissolve
        "{color=#51ad93}Stay silent":
            $GreenHeart += 1
            "I bite my tongue before I can say anything stupid."
            show d neutral with dissolve
            d "..."
            show d neutalk with dissolve
            d "I take your silence as a means of acknowledging my warning."
            show d neutral with dissolve
    "He's silent, watching me."
    hide d with dissolve
    show drk with dissolve
    "I look around the office - it looks nice, but it has a slightly ominous feel to it."
    "The curtains are nearly closed, which makes it quite dark and stuffy."
    "His presence itself, the situation I'm in and the athmopshere of the room is enough to make me slightly nervous..."
    "I realize that he's probably doing it on purpose, so I do my best to remain composed."
    "His silence is deliberate - it's obviously a test of my patience."
    "He's looking at me again... But this time he seems more analytical."
    "I want to be assertive about it and say something, but..."
    "I'm not sure what is expected from me."
    menu:
        "{color=#51ad93}Look down":
            $submissive += 1
            "I focus on the floor and keep my gaze locked there."
            "If he's testing my patience, I have a lot of it."
        "{color=#51ad93}Look him straight in the eye":
            $dominant += 2
            $GreenHeart += 1
            hide drk with dissolve
            show d neutral with dissolve
            "I look back at him without hesitation."
            "I will not be toyed with."
            m angrytalk "I came here for an interview, not a therapy session."
            show d neu with dissolve
            d "..."
            show d smirk with dissolve
            "His smile is far from genuine."
            show d coldtalk with dissolve
            d "My apologies, it must be a habit of mine."
            show d cold with dissolve
            "The way he looks at me is different now - like my resistance made him give up."
            "I don't care if this is what he expected or not - I won't hesitate to remind him that I don't like people acting like they have power over me."
            jump interviewquestions
        "{color=#51ad93}Stay still":
            "I do my best not to let him see how uncomfortable I am."
            "I wait for him to speak up again."
            jump interviewquestions
    "I can almost feel his gaze on my face..."
    "I'm tempted to look at him, but..."
    "...I shouldn't."
    menu:
        "{color=#51ad93}Look":
            "I give up and look at him, wanting him to stop."
            "He looks at me as if nothing happened."
        "{color=#51ad93}Don't":
            $submissive += 1
            "It's... becoming more difficult to keep looking away..."
            "It's as though he can see right through me."
            "I'm not sure where he's looking anymore."
            menu:
                "{color=#51ad93}Look at him":
                    "I give up and look at him, wanting him to stop."
                    "He looks at me as if nothing happened."
                "{color=#51ad93}Stay still":
                    $submissive += 1
                    "Why is this so unsettling for me...?"
                    "It's because I'm nearly certain that he's not just looking at my face right now."
                    "Oh god..."
                    "The thought of him acting so boldly is unbelievable to me at first."
                    "It's... scandalous, to say the least, but..."
                    "I remind myself this is still a test."
                    "He's judging my every move."
                    menu:
                        "{color=#51ad93}Look":
                            "I give up and look at him, wanting him to stop."
                            "He looks at me as if nothing happened."
                        "{color=#51ad93}Wait":
                            $GreenHeart += 1
                            $submissive += 1
                            "His gaze is still fixed on me."
                            "I can feel my breath quicken and my face grow hotter..."
                            "I... can't..."
                            "If he doesn't stop it now, I..."
                            "I can't break."
                            hide drk with dissolve
                            show d smirk with dissolve
                            d "You are quite tense, Ms.  Hart. Is there something you want to say?"
                            show d neutral with dissolve
                            "His calm tone makes me think I imagined everything that just happened..."
                            "He must be toying with me."
                            menu:
                                "No, I'm fine.":
                                    $GreenHeart += 1
                                    $submissive += 1
                                    show d smirk with dissolve
                                    d "I am glad to hear that."
                                    "I can hear a tinge of satisfaction in his voice... Have I done everything right?"
                                "I'm not tense at all.":
                                    show d neutalk with dissolve
                                    d "If you say so."
                                    show d neutral with dissolve
                                    "Is this... disappointment I hear in his voice?"
label interviewquestions:
    hide drk with dissolve
    show d neutalk with dissolve
    d "The nurse that led you here..."
    show d coldtalk with dissolve
    d "She wasn't much trouble, was she?"
    show d neu with dissolve
    menu:
        "I'm glad she's gone now.":
            $GreenHeart -= 1
            if SunLink == 0:
                show d talk with dissolve
                d "Regardless of your opinion, you will be coworkers soon."
                show d cold with dissolve
                d "I expect you to be objective in your judgement of our staff next time."
            else:
                $GreenHeart -= 1
                show d neutalk with dissolve
                d "How curious..."
                show d sidetalk with dissolve
                d "You say you disliked her and yet she is waiting for you outside this very door."
                show d coldtalk with dissolve
                d "I must admit, I rarely see someone as duplicitous."
                show d neutral with dissolve
                d "Toying with the feelings of other people must be amusing for you, if you treat her that way."
        "She was great":
            $empathy += 1
            show d siden with dissolve
            d "I... did not ask for your opinion."
            show d coldtalk with dissolve
            d "My only intention was making sure she did what she was supposed to."
            if SunLink == 0:
                $GreenHeart -= 1
                show d sidetalk with dissolve
                d "It seems to me that she has already left..."
                show d sidesmile with dissolve
                d "Pity... being able to make her wait for you outside would be quite the achievement."
            else:
                $GreenHeart += 2
                show d neutalk with dissolve
                d "She is waiting for you outside this door, correct?"
                show d sidetalk with dissolve
                d "You managed to create a bond with your future coworker in a matter of minutes..."
                show d frust with dissolve
                d "It should not be overlooked when judging your abilities."
        "She did her job":
            $GreenHeart += 1
            show d neutalk with dissolve
            d "As she was supposed to."
            if SunLink == 0:
                $GreenHeart -= 1
                show d sidetalk with dissolve
                d "It seems to me that she has already left..."
                show d sidesmile with dissolve
                d "Pity... being able to make her wait for you now would be quite the achievement."
            else:
                $GreenHeart += 2
                show d neutalk with dissolve
                d "She is waiting for you outside this door, correct?"
                show d sidetalk with dissolve
                d "You managed to create a bond with your future coworker in a matter of minutes..."
                show d frust with dissolve
                d "It should not be overlooked when judging your abilities."
    show d neutalk with dissolve
    d "You had a chance to walk through the hospital on your way here - what did you think of it?"
    show d neutral with dissolve
    "What has that got to do with anything...?"
    "I haven't been here for long enough to really make up my mind, but so far..."
    menu:
        "It feels odd":
            $GreenHeart -= 2
            show d sidetalk with dissolve
            d "If the sight of the building alone unsettles you, it might not be wise for you to work here..."
        "It's really impressive":
            $empathy += 1
            show d neutalk with dissolve
            d "I suppose so."
        "It doesn't affect my work, does it?":
            $GreenHeart += 1
            show d cold with dissolve
            d "I see you have a practical mind. Good."
            show d coldtalk with dissolve
            d "Your new job will require your complete focus."
    show d neutral with dissolve
    "I wonder what else he can ask me..."
    show d regret with dissolve
    d "Due to the sensitive nature of your work, I feel obliged to ask:"
    show d talk with dissolve
    d "Have you ever suffered from a mental illness?"
    show d cold with dissolve
    menu:
        "No, never":
            show d neu with dissolve
            "He looks at me with a hint of disbelief."
            "I told him the truth... right?"
        "A long time ago":
            $GreenHeart += 1
            show d sidetalk with dissolve
            d "I suppose it is difficult to avoid at some point..."
            show d neu with dissolve
            "What...is that supposed to mean?"
        "Actually...":
            $GreenHeart -= 1
            m gasp "I'm schizophrenic."
            show d neutalk with dissolve
            d "I do not appreciate being lied to in such a disrespectful manner, Ms.  Hart."
            show d neutral with dissolve
            "He's right - I lied."
    show d neutral with dissolve
    "I shift a bit in my seat in preparation for his next question."
    show d neutalk with dissolve
    d "What do you value the most in this job?"
    show d neu with dissolve
    "Finally, something I can actually answer honestly."
    menu:
        "The pay":
            $empathy -= 2
            $GreenHeart -= 1
            show d coldtalk with dissolve
            d "This is definitely not the kind of work a person who values only money would choose."
        "The workplace":
            $GreenHeart += 1
            show d neutalk with dissolve
            d "That... is a rare opinion here, Ms.  Hart."
            show d smirk with dissolve
            d "Your appreciation of this hospital has been noted."
        "Being able to help people":
            $empathy += 2
            show d sidetalk with dissolve
            d "Help people...?"
            show d neutalk with dissolve
            d "I suppose that is one way of looking at it."
    show d siden with dissolve
    "He looks away from me abscently for a moment."
    "Is that it?"
    show d sidetalk with dissolve
    d "Today is the 31st of October."
    show d neutalk with dissolve
    d "I heard some nurses are having a party for the occasion."
    show d talk with dissolve
    d "Do you have plans?"
    show d neutral with dissolve
    menu:
        "Of course I do":
            $GreenHeart -= 1
        "I don't celebrate":
            $GreenHeart += 1
        "I don't know yet":
            pass
    show d coldtalk with dissolve
    d "Of course, I wasn't asking out of curiousity..."
    show d sidetalk with dissolve
    d "However you chose to spend the evenings, make sure to never let it interfere with your work."
    show d neu with dissolve
    m fabtalk "I understand."
    show d sidetalk with dissolve
    d "Well then, Ms.  Hart..."
    if empathy > 5:
        show d neutalk with dissolve
        d "You definitely have what it takes in terms of personality."
        if SunLink == 1:
            show d talk with dissolve
            d "The nurse who led you here confirmed that."
    if empathy < 1:
        show d neutalk with dissolve
        d "A psychologist needs some amount of empathy..."
        show d coldtalk with dissolve
        d "I think that is what you lack."
    if empathy >= 1 and GreenHeart > 0:
        show d talk with dissolve
        d "You are expected here tomorrow at 7AM."
        show d neutral with dissolve
        menu:
            "Thank you":
                $empathy += 1
                show d neutalk with dissolve
                d "There is nothing you need to thank me for."
            "So... I was hired?":
                show d sidesmile with dissolve
                d "Yes, you were."
            "Of course":
                $GreenHeart += 1
                show d smirk with dissolve
                "I think I can see a hint of a smile on his face."
        if GreenHeart > 3:
            show d smile with dissolve
            d "It has been a pleasure."
        show d neutalk with dissolve
        d "I will await you tomorrow in your new office, Ms.  Hart."
        show d neu with dissolve
        "I nod."
    else: 
        show d talk with dissolve
        d "You are not fit to work here."
        if GreenHeart > 0:
            show d siden with dissolve
            d "It is a shame, but I do not think we will meet again."
        else:
            show d frusttalk with dissolve
            d "Interacting with you has been a waste of my time."
        show d talk with dissolve
        d "Get out, please."
    hide screen empathymeter
    hide screen greenmeter
    hide screen easymeter
    stop music fadeout 3
    scene bg offices with dissolve
    "I leave the office and shut the door behind me, letting out a breath I had no idea I was holding."
    play music "ost/tran.wav" fadein 6
    "It feels like a different world outside of that room..."
    $persistent.Sharpe=True
    if persistent.Sharpefirst=="":
        $persistent.Sharpefirst="????"
        $persistent.Sharpeage="????"
        play sound "chars.ogg" 
        show screen notify("{size=24} Your Characters Info screen has been updated!")
    $journal=True
    $renpy.pause()
    if tutorials:
        call screen tuto25
    if empathy >= 1 and GreenHeart > 0:
        "I'm glad to have that behind me..."
        "At least I was finally hired."
        if GreenHeart < 3:
            "Hopefully I won't have to interact with my new boss much..."
        else:
            "I think I did well... He seemed to be satisfied with how I handled myself."
            "Still..."
        "There was something unsettling about that man and the way he asked me questions I wasn't prepared for."
    else:
        "Well... it was worth a try."
        "I'll have to look for another job now, but..."
        "...At least I won't have to see that strange man again."
        stop music fadeout 2
        "\"Look for positives\", as I always tell myself."
    if SunLink == 1:
        stop music fadeout 5
        show su smile with moveinright
        "The nurse from before is standing by the wall, waiting for me as she said."
        "When she sees me emerging from the office, she approaches me with a smile."
        if empathy >= 2 and GreenHeart > 0:
            play music "ost/sunny.wav" fadein 7
            m conf "I got the job! I'm starting tomorrow."
            show su happy with dissolve
            gu "Congrats! How was it?"
            menu:
                "Great!":
                    show su smile with dissolve
                    gu "I'm glad to hear that."
                    show su cute with dissolve
                    gu "Either you caught him on a good day, or you have some serious skills."
                    show su talk with dissolve
                    gu "You're a psychologist, though, so..."
                    show su smile with dissolve
                    gu "I'm betting for the second one."
                "I'm glad it's over...":
                    show su talk with dissolve
                    gu "You'll get used to him eventually... we all had to stand that talk at some point."
                "Ughh...":
                    show su talk with dissolve
                    gu "Heh, I know how you feel."
                    show su sadsmile with dissolve
                    gu "You must've had some really bad luck..."
                    show su neu with dissolve
                    gu "But hey, if he was unpleasant today, that can only mean..."
                    show su laugh with dissolve
                    gu "It'll be better tomorrow, right?"
            show su smile with dissolve
            gu "Either way, don't get discouraged by his attitude."
            gu "He really cares a lot about the patients and the staff - he just doesn't show it much."
            m talk "By the way..."
            m flirt "Thank you."
            show su gasp with dissolve
            gu "For what?"
            m conf "I think you helped convince him that I have what it takes."
            show su happy with dissolve
            gu "Really? I'm glad to have helped then~"
            show su smile with dissolve
            show bg central with dissolve
            "We walk back to the central hall."
            "I think I'm starting to get used to the hospital's layout."
            "I'll need to memorize it eventually."
            show su talk with dissolve
            gu "Hey. Mind if we stop here for a moment?"
            show su neu with dissolve
            m neu "Not at all."
            show su smile with dissolve
            gu "I'll have to go to the nurses' office soon to get some work done, but it's been a real treat showing you around."
            show su happy with dissolve
            gu "It's always nice to see new faces here, especially friendly ones."
            menu:
                "Likewise":
                    $empathy += 1
                "Thank you.":
                    pass
                "You'll get sick of me soon enough.":
                    show su smile with dissolve
                    gu "Heh, we'll see."
            show su talk with dissolve
            gu "I... never got to ask your name."  
            show su neutral with dissolve
            m flirt "It's [name]."
            show su smile with dissolve
            gu "I'm {color=#67beea}Sue{/color}. Nice to meet you, [name]."
            $suename="Sue"
            stop music fadeout 2
            show ac 31:
                yalign 0.0
                linear 3.0 xalign 1.0
            pause 2.5
            show ac 32
            pause 0.08
            show ac 33
            pause 2
            "{color=#67beea}I feel a bond forming between me and Sue..."
            "Have I made a friend here already?"
            play music "ost/sunny.wav" fadein 3
            scene bg central with dissolve
            show su happy with dissolve
            sue "Well, if you need anything, I'm sure I can spare some time tomorrow."
            show su smile with dissolve
            sue "Look for me here on your break if you want to talk."
            m happy "Sounds good. Thanks for the tour and everything, Sue."
            show su cute with dissolve
            sue "No problem. See you tomorrow!"
            hide su with moveoutleft
            "Sue disappears in the nurses' office."
            "I'm glad to have made her acquaintance today."
            "It'll be good to have someone I know from the start in the hospital."
            "If I need anything from Sue, I can look for her in the {color=#67beea}CENTRAL HALL{/color} on my break."
            $persistent.Sue=True
            $persistent.Suelast="????"
            play sound "chars.ogg" 
            show screen notify("{size=24} Your Characters Info screen has been updated!")
        else:
            gu "How was it?"
            m regrettalk "I... didn't get the job."
            show su sad with dissolve
            "There was genuine sadness on the nurse's face when she heard it."
            "At least she cares - even if I wasn't hired, I made a friend."
            "\"Look for positives\", I tell myself."
            show su sadtalk with dissolve
            gu "That... sucks."
            show su smile with dissolve
            gu "Hey, don't worry - you'll find another hospital."
            show su neu with dissolve
            gu "I'll walk you to the entrance - I still have some time."
            m sadsmile "Thanks."
            return
    else:
        if empathy >= 1 and GreenHeart > 0:
            "The important thing was that I got the job and I would come here again tomorrow."
            "I walk to the central hall and leave the offices hallway behind me for now."
        else:
            return
    stop music fadeout 10
    scene bg patients with dissolve
    "Walking back the way I came here, I have to pass through the patients' rooms hallway."
    "It has an eerie feel to it..."
    "I'm not afraid of the patients and tight spaces never really unsettled me."
    "And yet I want to get through this hallway as fast as possible..."
    scene black with dissolve
    "Conveniently enough, the door by the staircase opens on its own from the inside."
    play sound "doorclose.ogg" fadein 0.5
    "I'll have to get some keys tomorrow."  
    play music "ost/mc.wav" fadein 5
    scene bg greetsun with dissolve
    "Passing through the reception once again, I catch the eye of the nurse named Julia."
    "I smile at her before leaving - I'm too happy to care."
    scene bg frontsun with dissolve
    m happy "I'll meet my patients tomorrow~~"
    "I'm so excited for my first day of work! I wonder what kind of people my patients will be..."
    "Walking back home, I turn around to take a look at my new workplace."
    "It looks so... serious. I'm really working at a hospital, finally!"
    "After so much work to get here, I'll have therapy with people who really need my help."
    "I can't help but feel at peace - soon, I'll be able to do what I always wanted to."
    "I barely keep myself from bouncing while walking back home."
    "{i}Would you like to save your game?"
    menu:
        "Yes":
            show text "{size=100}{color=#ffffff}After\njob interview":
                ypos 300
            $renpy.pause()
            $ renpy.call_in_new_context("_game_menu")
        "No":
            pass
    jump calendar
## FIRST DAY OF WORK ###################################################
########################################################################
label dayone:
    scene black with dissolve
    "My alarm clock woke me up."
    "It's 7 AM... I should be getting up."
    "Yesterday, I... I got the job-"
    play music "ost/mc.wav" fadein 3
    scene black with vpunch
    "It's my first day at work! I'll meet my patients in just a few hours, I..."
    "I need to hurry up."
    "\"Stay calm\", I tell my enthusiastic face on the other side of the mirror while brushing my hair."
    "I'm more than ready for today."
    scene bg dawn with dissolve
    "Thankfully my new house isn't far from the hospital, so once I'm ready I decide to walk."
    "The weather today is surprisingly nice for November."
    show bg front with dissolve
    "After twenty minutes I find myself by the entrance."
    show bg greet with dissolve
    "I push the front door open confidently and feel the familiar thrill of being inside the hospital again."
    "After confirming my identity to a nurse I didn't recognize, I was handed a pair of keys and told to go to my new office."
    show bg cafe with dissolve
    "I passed the now empty cafeteria and a staircase to get to the second floor."
    show bg patients with dissolve
    "I make my way through the patients' rooms hallway."
    show bg central with dissolve
    "Going deeper into the hospital, I pass through the central hall to enter the offices hallway."
    show bg offices with dissolve
    "One of the offices was already labelled:"
    "{b}{color=#af2626}\"Office III\n[name] Hart\nPsychologist\"{/b}"
    stop music fadeout 1
    show bg mcdark with dissolve
    "I open the door and I'm instantly overwhelmed."
    play music "ost/tran.wav" fadein 6
    "The inside of my office resembles Dr. Sharpe's slightly, but the color scheme is completely different."
    "Immediately I decide to open up the thick curtains to let more sunlight into the room."
    "There is nothing more depressing than a dark room, especially on a sunny day like this."
    scene bg mc with Dissolve(1.0)
    "From the window in my office, which has bars on it - for safety reasons, I assume - I can see a bit of the nearby town where I'm staying, but mostly the forest surrounding the hospital."
    "I'm one floor above the ground."
    "A fall from here probably wouldn't be deadly."
    "Thankfully."
    stop music fadeout 2
    d "How do you like your new office, Ms.  Hart?"
    show d smirk with dissolve
    "Startled a bit by Dr. Sharpe's voice and the sound of the door being closed, I turn around to face my boss."
    m fabtalk "It's... spacious."
    show d neu with dissolve
    "Still slightly overwhelmed by the room, I'm at a loss of words, so I figure it's better to say the first thing that comes to my mind."
    play music "ost/hospital.wav" fadein 6
    show d neutalk with dissolve
    d "I will take this as a sign of enthusiasm for the job."
    show d coldtalk with dissolve
    d "{color=#51ad93}I have already assigned patients to you yesterday{/color}. Since you are new here and obviously lack experience, you will have fewer of them than the others at first."
    show d neutalk with dissolve
    d "Here are their {color=#51ad93}files{/color} - I expect you to read them beforehand."
    show d neutral with dissolve
    "He hands me a few documents after looking through them briefly and I place them carefully on my desk."
    show d sidetalk with dissolve
    d "{color=#51ad93}Richards, Moore, Burnett{/color}... {color=#51ad93}\"unknown\"{/color}... it shouldn't be difficult for you to interact with all four of them frequently enough to progress the therapy."
    show d talk with dissolve
    d "You can choose who to meet with and how long your sessions will last."
    show d neutalk with dissolve
    d "Your scheduled break is from 12:00 to 12:30 every day."
    show d talk with dissolve
    d "Do you have any further questions?"
    show d neutral with dissolve
label firstdayquestions:
    menu:
        "How many sessions a day should I have?":
            show d talk with dissolve
            d "I would recommend two, one before your break and one after."
            show d neutalk with dissolve
            d "But I assume you want to meet all your patients today so you know what to expect."
            show d sidetalk with dissolve
            d "It shouldn't be difficult to arrange four shorter sessions."
            jump firstdayquestions 
        "Why were these specific patients chosen for me?":
            show d sidetalk with dissolve
            d "For no particular reason."
            show d talk with dissolve
            d "I considered which of them you would communicate with the best."
            show d siden with dissolve
            d "As a psychologist, you value having a good relationship with your patients, no?"
            jump firstdayquestions 
        "Will you be overseeing my work?":
            show d neutalk with dissolve
            d "For the first week, yes."
            show d coldtalk with dissolve
            d "I have to be certain you are not causing the patients any harm."
            jump firstdayquestions 
        "{color=#51ad93}I understand everything":
            show d talk with dissolve
            d "I see."
    show d neutalk with dissolve
    d "Once you have read your patients' files, you can fetch a nurse to {color=#51ad93}lead one of them to your office{/color}."
    show d talk with dissolve
    d "I highly encourage you to be as objective as possible when judging your patients."
    show d sidetalk with dissolve
    d "It would be a shame for you to {color=#51ad93}neglect{/color} some patients in favor of others."
    show d siden with dissolve
    m conf "I'll try my best."
    show d frusttalk with dissolve
    d "\"Trying\" may not be enough."
    show d neu with dissolve
    "He steps away from me and moves towards the door."
    show d talk with dissolve
    d "The next time we see each other, I will judge how well you handle your current position."
    show d coldtalk with dissolve
    d "Be mindful of how you choose to interact with your patients."
    show d neu with dissolve
    d "Until we meet again, Ms.  Hart."
    play sound "doorclose.ogg" fadein 1
    hide d with dissolve
    "I nod and he's gone, leaving me to read my patients' files."
    stop music fadeout 4
    "I sit by my desk and put the files in a neat pile before me."
    "It's 7:30, so I shouldn't have to hurry."
    play sound "page.ogg"
    show drk with Dissolve(0.2)
    show file1 with dissolve
    $renpy.pause()
    play sound "page.ogg"
    hide file1 with dissolve
    call screen gad
    show file2 with dissolve
    $renpy.pause()
    play sound "page.ogg"
    hide file2 with dissolve
    call screen schizophrenia
    show file3 with dissolve
    $renpy.pause()
    play sound "page.ogg"
    hide file3 with dissolve
    call screen did
    show file4 with dissolve
    $renpy.pause()
    play sound "page.ogg"
    hide file4 with dissolve
    call screen ocd
    hide drk with dissolve
    play music "ost/mc.wav" fadein 3
    "That seems to be all my patients."
    "Interestingly, each of them has a completely different illness."
    "It looks like I'll be dealing with really serious problems... Well, it's what I was hoping for all this time and yet..."
    "I am a bit nervous."
    if tutorials:
        call screen tuto3
    show drk with dissolve
    "{i}Would you like to save your game?"
    menu:
        "Yes":
            show text "{size=100}{color=#ffffff}First day of work,\nbefore sessions":
                ypos 300
            $renpy.pause()
            $ renpy.call_in_new_context("_game_menu")
        "No":
            pass
    hide drk with dissolve
    "Who should I start with...?"
label patientchoiceintroduction:
    stop music fadeout 5
    call screen patientsintro
label aftersessiononefirstday:
    scene bg mc with dissolve
    "I have time for one more patient before my break."
    "Who's it going to be?"
    jump patientchoiceintroduction
label firstdaybreak:
    scene bg mc with dissolve
    "It's time for my mid-day break."
    play music "ost/tran.wav" fadein 5
    scene bg sun with Dissolve(1)
    "I look out the window."
    "I want to keep having sessions..."
    "But I'm really not sure if I'm doing everything right... Should I really be jumping head-first into this?"
    "I don't think I was really prepared for today, but still... I definitely don't regret applying for this job."
    if redintro == 1:
        "It may not have been a good idea to start with Michael..."
        "Either way, I handled myself the best I could."
        "Thinking back to it, he wasn't as bad as I'd feared he would be."
    if blueintro == 1:
        "Charlie wasn't really troublesome or stressful, but interacting with him was frustrating in a way."
        "He was nice to me and I didn't really feel uncomfortable with him, but he's just so distracted..."
        "Well, I'm here to help."
    if purpleintro == 1:
        "Tom... he just yelled at me."
        "Like he doesn't belong here - of course he does."
        "I only wanted to help and he seems to not even acknowledge the problem."
    if silverintro == 1:
        "William. I guess I don't have many reasons to complain."
        "I wasn't particularly surprised that he didn't trust me at first, but..."
        "I really hope it will pass eventually. If he never opens up, I won't be able to help him."
    scene bg mc with dissolve
    "Oh."
    "And just like that, my break is nearly over. Finally..."
    "I have two more patients to get through, so I have to choose again."
    "Who'll it be this time?"
    jump patientchoiceintroduction
label afterworkfirstday:
    scene bg mc with dissolve
    "Only one patient left. Let's do it."
    jump patientchoiceintroduction
label dayoneafterwork:
if wrong > 4:
    scene black with dissolve
    "I was asked by Dr. Sharpe to meet him in his office after I was done with the sessions."
    "He said I couldn't even handle my first day of work and that he can't allow someone like me to keep working here."
    "I was forced to leave the hospital forever."
    scene fired with Dissolve(1.0)
    "You were fired. Return to the beginning of the day and make different choices to alter your ending."
    return
else:
    scene bg mc with dissolve
    "That seems to be everyone."
    play music "ost/tran.wav" fadein 5
    "I'm a little tired after today, but that's okay."
    "It's been a while since I poured this much energy into something. I really don't want to mess this up."
    scene bg offices with dissolve
    "I pack my things and leave, locking my office as I was instructed to."
    scene bg patients with dissolve
    "While passing by my patients' rooms I can't help but glance at them."
    "I spot Charlie smiling and waving at me."
    "Michael is staring at me in silence like he did before."
    "Tom doesn't even notice me passing by his room."
    "William obviously saw me but avoids my eyes, so I look away quickly."
    "And that's all of them. My patients."
    "It feels kind of overwhelming to work with them at last."
    "Still..."
    "Charlie seems friendly enough, but it's clear to me he's far from sane, Tom blamed me for something that wasn't my fault, being around Michael unsettles me and William doesn't seem to want my help."
    "Looking back at all the sessions today, I don't think any of them will be particularly easy to work with, but that's okay."
    scene bg frontsun with dissolve
    "Upon leaving the hospital, a thought occurs to me."
    "What if I'm doing something wrong..?"
    "Am I too excited about this job to be focused?"
    "What if I messed up already?"
    "No, it can't be..."
    scene sunset with dissolve
    "Come on, it's only been one day - I shouldn't be so harsh on myself. I'll figure everything out when the time comes."
    "And until tomorrow, I can only hope for the best."
    "Yeah. That's it."
    scene black with Dissolve(1.0)
    stop music fadeout 3
    "..."
    scene bg night with dissolve
    "Still, the confusion lingers in my mind as I reach my house..."
    "Have I really done everything right?"
    jump janeintro
    
### SECOND DAY OF WORK, WITH Elizabeth ####################################
###########################################################################
label daytwo:
    scene black with dissolve
    "7 AM. My alarm clock woke me up."
    "...."
    play music "ost/jane.wav" fadein 5
    "I... feel like I'm forgetting something..."
    "I had... a dream..?"
    stop music fadeout 3
    "Eh, whatever. I won't remember it now, either way."
    show bg mcliving with dissolve
    "I feel oddly relaxed today."
    "Like... I shouldn't worry about yesterday."
    play sound "ost/janes.ogg" fadein 2
    nt "{cps=10}{i}\ndon't give up"
    "Yeah. I can't give up yet."
    "I'm going to go to work and do my best. It'll turn out alright as long as I try."
    play music "ost/mc.wav" fadein 4
    "With newfound determination, I head to work once again, knowing what is waiting for me ahead."
    scene bg dawn with dissolve
    "It's a sunny day like yesterday."
    "I hum on my way to work."
    scene bg mc with dissolve
    "I arrive in my office on time."
    "I guess I really overreacted yesterday... I should keep a cool head today and do my best."
    play sound "chars.ogg" 
    show screen notify("{size=24} Your Location Info screen has been updated!")
    "Upon settling my things on my desk, I'm ready to choose who I'll spend time with today."
    "I only have time for two patients, so it would be wise to choose carefully and pick the two I want to interact with the most."
    "Like Dr. Sharpe told me yesterday, I should plan my sessions carefully so I don't neglect anyone."
    if tutorials:
        call screen tuto5
    jump patientchoice
label patientchoice:
    scene black with dissolve
    pause 0.5
    scene desk with dissolve
    "Who should I meet today?"
    stop music fadeout 2
    call screen patients
label goldenintroduction:
    scene black with dissolve
    "Today's session took longer than yesterday, so it's already time for my break."
    "Since I want to get closer to the patients, I decide to see where they spend the breaks."
    scene bg outside
    play music "ost/hospital.wav" fadein 5
    "I end up on the first floor and notice a large group of patients outside."
    "Taking advantage of the weather, I decide to join them."
    "A nurse I don't recognize greets me politely. I look around."
    "All patients are interacting in small groups or seem occupied with something."
    show e bored with dissolve
    "Wait."
    "I spot one young girl sitting on her own, looking down."
    "She seems so lonely..."
    "I approach her."
    m happy "Hi."
    show e neutral with dissolve
    "She looks at me, puzzled."
    show e talk with dissolve
    pt "You are..?"
    show e baka with dissolve
    m conf "I'm a psychologist, [name] Hart."
    show e foctalk with dissolve
    pt "Figures. Only you guys are weird enough."
    show e calm with dissolve
    menu:
        "What's your name?":
            show e bakatalk with dissolve
            pt "Why do you care...?"
            show e calm with dissolve
            pt "Just give up and look for someone more entertaining."
            m fabtalk "I think you're entertaining enough for me."
        "Is it weird to talk to people?":
            $GoldenHeart += 1
            show e talk with dissolve
            pt "Yes."
            show e boretalk with dissolve
            pt "I just wish you'd leave me alone..."
            show e bored with dissolve
            m fabtalk "Why is that?"
    show e foctalk with dissolve
    pt "You really are a pain..."
    show e boretalk with dissolve
    pt "You won't give up, right?"
    show e baka with dissolve
    "I shake my head. I'm not sure where this interaction will lead, but I surely won't give up."
    show e foc with dissolve
    pt "Fine."
    show e boretalk with dissolve
    pt "You can talk if you want."
    show e bored with dissolve
    "I wonder what I should talk about... she doesn't seem willing to start a conversation."
    show e talk with dissolve
    pt "By the way."
    show e bakatalk with dissolve
    pt "It's {color=#ffdd8e}Elizabeth{/color}. My name."
    show e baka with dissolve
    m flirt "It's nice to meet you, Elizabeth."
    show e angrytalk with dissolve
    e "Ugh, don't call me that... it sounds weird when people say that."
    show e angry with dissolve
    m talk "What should I call you then?"
    show e boretalk with dissolve
    e "\"You\" is fine. What's the problem?"
    show e baka with dissolve
    menu:
        "How long have you been here?":
            $GoldenHeart += 1
            show e neutalk with dissolve
            e "Since the beginning of the year I think...?"
            show e calmtalk with dissolve
            e "Hard to count days when everything is so monotone."
        "What's your illness?":
            show e bakatalk with dissolve
            e "Called it \"schizoid personality disorder\"..?"
            show e boretalk with dissolve
            e "Don't ask me what the hell that stands for and if you know, good for you - don't care."
    show e bored with dissolve
    menu:
        "Why don't you like your name?":
            show e boretalk with dissolve
            e "What makes you so interested...?"
            show e foctalk with dissolve
            e "Stop interrogating me already... I wouldn't tell you either way."
            show e calm with dissolve
            "We sat in silence for a while."
            show e bored with dissolve
            "It got pretty awkward after a moment, so I left Elizabeth be."
            hide e with dissolve
            "She didn't say a word to me."
            $GoldRouteFail = True
            $GoldenHeart = 0
        "How old are you?":
            $GoldenHeart += 1
            show e boretalk with dissolve
            e "Pretty sure I'm twenty."
            show e neutalk with dissolve
            e "Haven't seen you here yet. You new?"
            show e neu with dissolve
            m fabtalk "This is actually my second day of work here."
            show e talk with dissolve
            e "Thought so."
            show e calm with dissolve
            m talk "Do you usually spend breaks like this?"
            show e neutalk with dissolve
            e "Breaks...? Doctors have breaks now, right?"
            show e neu with dissolve
            "I nod."
            show e boretalk with dissolve
            e "If I have free time, I'm alone. You probably figured as much."
            show e calmtalk with dissolve
            e "But I thought today I'd do something different, I don't know..."
            show e bored with dissolve
            m fab "Do you have friends among other patients?"
            show e smirk with dissolve
            e "\"Friends\"? Me and friendship? Nah, thankfully never happened."
            show e calmtalk with dissolve
            e "Don't really like other people."
            show e bored with dissolve
            m conf "But you're still here talking to me."
            show e bakatalk with dissolve
            e "Are you implying we're \"friends\" now?"
            show e bored with dissolve
            m fabtalk "Not at all."
            m conf "You seem quite talkative for someone who doesn't like people."
            show e foctalk with dissolve
            e "Do I...?"
            show e bakatalk with dissolve
            e "Maybe it's just 'cause you're a psychologist and I got used to talking with 'em already."
            show e calmtalk with dissolve
            e "You all have a similiar way of trying to interrogate me about my problems. Do they teach you that or what?"
            show e bored with dissolve
            m "Not really. I guess it comes with practice."
            show e talk with dissolve
            e "You practising right now?"
            show e neu with dissolve
            m talk "You could say that."
            show e calmtalk with dissolve
            e "I hope it brought you some satisfaction then, or whatever you wanted from me."
            show e neutalk with dissolve
            e "Your break is nearly over now, you should probably go."
            show e bored with dissolve
            menu:
                "I had a good time.":
                    show e calmtalk with dissolve
                    e "At least you did..."
                "That was boring.":
                    show e calmtalk with dissolve
                    e "A conversation is only as boring as the person you're talking to."
                    $GoldRouteFail = True
                    $GoldenHeart = 0
                "Will you be here again tomorrow?":
                    $GoldenHeart += 1
                    show e neutalk with dissolve
                    e "What...?"
                    show e talk with dissolve
                    e "Why would you want to meet me again?"
                    show e neu with dissolve
                    m neu "I'm only asking."
                    show e neutalk with dissolve
                    e "{color=#ffdd8e}I'll be here unless it rains{/color}, if that's what you're asking."
                    show e smirk with dissolve
                    m smile "Thanks."
                "See you later!":
                    pass
            show e boretalk with dissolve
            e "Well, see you around, [name]..."
    scene bg cafe with dissolve
    "I walk back inside, thinking about the strange girl I just met."
    stop music fadeout 6
    if GoldRouteFail:
        $PrsLink = 0
    else:
        $PrsLink = 1
        $persistent.Elizabeth=True
        $persistent.Elizabethlast="????"
        play sound "chars.ogg" 
        show screen notify("{size=24} Your Characters Info screen has been updated!")
    if GoldenHeart > 2:
        "Elizabeth is interesting - she seems more relaxed and \"normal\" when it comes to behavior than the other patients I've met."
        "Though I can tell she's dealing with a lot just like them."
        "Her coldness didn't really bother me that much and in a strange way I think she's actually a nice person."
        "She just doesn't want to show it."
        "I'd like to spend more time with her tomorrow."
    else:
        "I wonder... will we see each other again?"
    scene black with dissolve 
    "I get to my office on time before the end of my break."
    "I think this next session will last until the end of the day..."
    "Who do I want to see?"
    jump patientchoice
    
label daytwoafterwork:
    scene bg frontsun with dissolve
    play music "ost/mc.wav" fadein 3
    "Today I felt a lot better than I did yesterday."
    "Meeting Elizabeth was interesting and the therapy sessions went a lot smoother."
    "Maybe I was exaggerating yesterday, or maybe Jane helped me in that dream."
    "All I know is that I survived this second day and I'm ready for more."
    jump nextday
    
label dayfivelate:
    scene bg greet with dissolve
    "I think I'm a bit late..."
    "It's 8:12, I should've been here some twenty minutes ago..."
    scene bg offices with dissolve
    play music "ost/tension.ogg" fadein 2
    d "Ms. Hart?"
    show d neutral with dissolve
    "I turn on my heel. Of all the days he could notice me going to work, why must it be the one I'm late?"
    show d neutalk with dissolve
    d "Are you by any chance... late?"
    show d cold with dissolve
    m uncom "That's right. It won't happen again."
    show d neutalk with dissolve
    d "I sincerely hope so."
    show d neu with dissolve
    m serious "I'm sorry, but I have patients to meet..."
    show d neutral with dissolve
    "I open the door to my office in a hurry."
    show d sidetalk with dissolve
    d "Of course."
    show d talk with dissolve
    d "I only have one thing to tell you, Ms. Hart."
    show d coldtalk with dissolve
    d "{color=#51ad93}I expect you in my office today after you finish your work."
    show d neutalk with dissolve
    d "We will discuss how you handle your current position in detail."
    show d sidetalk with dissolve
    d "And if you have failed, I will not hesitate to {color=#51ad93}fire{/color} you."
    show d neutral with dissolve
    "Right..."
    m uncom "I understand."
    show d talk with dissolve
    stop music fadeout 3
    d "I expect you to not be late again."
    scene mc with dissolve
    "I nod and practically jump into my office."
    "I wasn't prepared for that..."
    "Alright, despite the small loss of time, my usual schedule should work."
    jump patientchoice
label fridayjudgement:
    scene black with dissolve
    play music "ost/hospital.wav" fadein 5
    "My last session of this week is over."
    "I gather my belongings into my bag, take my jacket and head outside."
    play sound "doorclose.ogg" fadein 1
    scene bg offices with dissolve
    "Locking the door behind me, I remember that Dr. Sharpe told me to meet him after work."
    "He said he would judge my ability to keep working here... if I'm not careful enough, he might fire me."
    "I really hope I can keep this job, though..."
    play sound "knock.ogg" 
    "I find his office on the far end of the hallway and knock."
    "There's nobody there."
    "Maybe he's out temporarily... I should wait."
    "Ten minutes pass until I hear footsteps."
    show d talk with dissolve
    d "Ms. Hart, you were here early..?"
    show d frust with dissolve
    "I nod."
    show d regrettalk with dissolve
    d "I apologize for the wait. I needed to confirm something before our meeting."
    show d frust with dissolve
    stop music fadeout 4
    "He unlocks the door and I go in."
    show bg doctor with dissolve
    show d neu with dissolve
    "The office looks the same as it did a week ago."
    "I seem to be interrogated every time I'm here... I hope I can handle myself today."
    play music "ost/hier.ogg" fadein 5
    show d siden with dissolve
    "He's not looking at me... he pulls out a notebook and adjusts his glasses."
    show d sidetalk with dissolve
    d "As I have said before, I kept track of who you chose to interact with during the entire week."
    show d siden with dissolve
    "Hearing that makes me a bit anxious. I've done everything right... haven't I?"
    show d talk with dissolve
    d "Is this correct?"
    show d neu with dissolve
    "He shows me a page of the notebook."
    "All days of the week are written down with the names of my patients listed under them."
    "It's accurate. I nod."
    show d sidetalk with dissolve
    d "Regarding your schedule..."
    show d frust with dissolve
    "He looks over the names carefully for a moment."
    if redinteract == 0 or purpleinteract == 0 or blueinteract == 0 or silverinteract == 0:
        show d neutalk with dissolve
        d "Ms.  Hart... I believe there is a problem."
        show d neu with dissolve
        "He shows me my schedule again."
        show d coldtalk with dissolve
        d "One of your patients was {color=#51ad93}completely neglected{/color}."
        d "Do you sincerely not care that much or have you forgotten about them...?"
        show d frusttalk with dissolve
        d "Both of these reasons are absolutely unacceptable."
        show d cold with dissolve
        "I forgot about one of my patients... I failed."
        jump firedfriday
    elif redinteract == 4 or purpleinteract == 4 or blueinteract == 4 or silverinteract == 4:
        show d sidetalk with dissolve
        d "You already seem to have a {color=#51ad93}favourite{/color} among your patients..."
        show d frusttalk with dissolve
        d "I believe I had warned you about this..."
        if redinteract == 0 or purpleinteract == 0 or blueinteract == 0 or silverinteract == 0:
            show d coldtalk with dissolve
            d "In doing so, you have {color=#51ad93}neglected the other patients{/color} assigned to you."
            show d frusttalk with dissolve
            d "How irresponsible..."
            show d coldtalk with dissolve
            d "Ms.  Hart, I would not be bothered by you picking favourites if you did not make your lack of interest in the others so blatantly obvious."
            show d cold with dissolve
            "It's true... I may have forgotten about one of my patients..."
            jump firedfriday
        else:
            show d sidetalk with dissolve
            d "Surprisingly, despite your obvious preference for this patient in particular, you managed to maintain a fairly {color=#51ad93}balanced{/color} schedule."
            show d frust with dissolve
            d "You have not neglected any of your other patients..."
            show d cold with dissolve
            "He glares at me."
            show d coldtalk with dissolve
            d "...barely."
            show d neutalk with dissolve
            d "But I suppose there is some purpose to your actions so far."
            show d talk with dissolve
            d "Your schedule shows that you have done some amount of planning, which I appreciate."
            d "We will discuss your preference in patients later on."
    elif redinteract == 2 and purpleinteract == 2 and blueinteract == 2 and silverinteract == 2:
        show d neu with dissolve
        d "...Ms. Hart?"
        m fabtalk "Yes?"
        show d regretsmile with dissolve
        d "Your schedule this week... it was {color=#51ad93}perfect{/color}."
        show d talk with dissolve
        d "You showed no sign of subjectiveness when choosing patients."
        show d sidetalk with dissolve
        d "In addition..."
        show d talk with dissolve
        d "You must have planned it all beforehand."
        show d sidesmile with dissolve
        d "Four days, four patients, eight sessions to spare..."
        m neu "...."
        show d smile with dissolve
        d "I admit, you have impressed me, Ms. Hart."
        "Did I just... hear a compliment from him?"
        show d sidesmile with dissolve
        "I wouldn't have expected that from him. Damn."
        "It's true that my schedule was quite well-calculated, but I had no idea he would even notice it."
    else:
        show d sidetalk with dissolve
        d "There doesn't seem to be anything of note regarding your choice of patients..."
        show d frust with dissolve
        d "It isn't perfect, of course, but I can look past that."
    show d sidetalk with dissolve
    if easymeter: 
        show screen easymeter
        show screen proper
    d "Now, moving on to {color=#51ad93}your methods{/color}..."
    show d cold with dissolve
    "He hides the notebook and looks at me closely."
    if wrong > 7:
        show d coldtalk with dissolve
        d "I have received multiple {color=#51ad93}complaints{/color} about the way you interact with your patients."
        show d frusttalk with dissolve
        d "They stated that you act in a very unprofessional and improper manner and that you were of no help to your patients."
        show d cold with dissolve
        "I... may have slipped up a few times..."
        show d coldtalk with dissolve
        d "I cannot ignore such accusations towards you."
        show d cold with dissolve
        "Does that mean...?"
        jump firedfriday
    else:
        show d siden with dissolve
        d "I have not received any valid criticism towards your working style."
        "Does that mean I've done well this week?"
    if professional > personal + 5:
        show d neutalk with dissolve
        d "From what I have gathered, you seem to be primarily {color=#51ad93}professional{/color} when interacting with patients."
        show d sidetalk with dissolve
        d "You rarely let a patients influence your actions and try not to behave in an emotional manner."
        show d sidesmile with dissolve
        d "I appreciate your approach to these sessions, Ms. Hart."
    elif personal > professional + 5:
        show d talk with dissolve
        d "Ms.  Hart, is it true that while interacting with your patients, you frequently reacted in an {color=#51ad93}emotional{/color} manner?"
        show d neu with dissolve
        menu:
            "That's right":
                show d talk with dissolve
                d "It is what I heard about your approach..."
            "No":
                show d sidesmile with dissolve
                d "I'm afraid I trust my sources more than your answer right now..."
        show d neutalk with dissolve
        d "It does not affect my judgement today, but I believe you should be warned."
        show d talk with dissolve
        d "Do not let your patients control you."
        show d coldtalk with dissolve
        d "Letting them influence how you feel and act is a dangerous path that leads to nothing good."
        show d sidetalk with dissolve
        d "I hope you understand my concern for {color=#51ad93}your safety{/color}."
        show d neu with dissolve
        "I nod. I'm not stupid, I know when a patient crosses a line."
        "I can handle myself, I'm sure of that."
    else:
        show d sidetalk with dissolve
        d "There seems to be nothing of note regarding the way you work overall..."
    show d neutalk with dissolve
    d "Everything seems to be in order."
    hide screen proper
    if redinteract > 3 or purpleinteract > 3 or blueinteract > 3 or silverinteract > 3:
        if easymeter:
            if redinteract > 3:
                show screen redmeter
            elif purpleinteract > 3:
                show screen purplemeter
            elif blueinteract > 3:
                show screen bluemeter
            elif silverinteract > 3:
                show screen silvermeter
        show d talk with dissolve
        d "There is only one thing left for us to discuss..."
        d "I mentioned your preference for one of your patients before."
        show d neutalk with dissolve
        d "I will consider letting you keep working that way..."
        show d neu with dissolve
        "Wait, really?"
        show d talk with dissolve
        d "Meeting with this one patient every day."
        show d cold with dissolve
        d "But only if you answer one question."
        "A question...? I better think before I answer."
        "My career seems to be on the line here..."
        show d sidetalk with dissolve
        d "Why have you decided to interact with this patient in particular from the start? After talking to them once, you have already chosen them as your favourite."
        show d coldtalk with dissolve
        d "Why is that?"
        show d cold with dissolve
        menu:
            "They interest me the most":
                if redinteract > 3 and RedHeart>=13:
                    $route = "red"
                elif purpleinteract > 3 and PurpleHeart>=12:
                    $route = "purple"
                elif blueinteract > 3 and BlueHeart>16:
                    $route = "blue"
                elif silverinteract > 3 and SilverHeart>=13:
                    $route = "silver"
                m gasp "...because..."
                menu:
                    "I can relate to them in some ways":
                        $personal += 1
                        show d sidetalk with dissolve
                        d "That is an interesting statement to make, Ms. Hart..."
                        show d neu with dissolve
                        d "Regardless, I accept your reasons."
                    "Their case is the most complex":
                        $professional += 1
                        show d frusttalk with dissolve
                        d "I see..."
                        show d smirk with dissolve
                        d "In that case, I wish you luck with this patient."
                hide screen easymeter
                hide screen redmeter
                hide screen bluemeter
                hide screen purplemeter
                hide screen silvermeter
                "It seems that our conversation is over. That was quick."
            "I like them the most":
                show d neutalk with dissolve
                d "Excuse me..?"
                show d neu with dissolve
                d "I would not expect such immaturity from you, Ms. Hart."
                show d cold with dissolve
                d "Your schedule is passable, but this... "
                show d coldtalk with dissolve
                hide screen easymeter
                hide screen redmeter
                hide screen bluemeter
                hide screen purplemeter
                hide screen silvermeter
                d "If this was really your reasoning behind choosing this patient, you leave me no choice."
                jump firedfriday
            "I don't know":
                show d neutalk with dissolve
                d "Are you saying that your choice of patients was completely random?"
                hide screen easymeter
                hide screen redmeter
                hide screen bluemeter
                hide screen purplemeter
                hide screen silvermeter
                show d coldtalk with dissolve
                d "You have spent nearly eighteen hours with one of them and you have not yet realized why..?"
                show d cold with dissolve
                m fabtalk "...I guess."
                show d frusttalk with dissolve
                d "You are truly the most frustrating coworker I have yet to deal with..."
                show d frust with dissolve
                "He looks down for a moment, likely pondering my lack of thought put into this job."
                show d neutral with dissolve
                d "However, it does not matter. You may keep working here."
                "I open my mouth to respond."
                show d frust with dissolve
                d "Leave before I change my mind..."
                "That was a bit harsh."
                jump leaveworkfriday
    else:
        hide screen easymeter
        if route == "golden":
            pass
        else:
            $route = "no"
        if GreenHeart > 3:
            show d smile with dissolve
            d "In all honesty, I am glad to see that you handled your work responsibly."
            show d smirk with dissolve
            d "It would be a shame for me to be forced to fire you now."
    show d neutral with dissolve
    "He stands up to gather his belongings and I follow him."
    show d neutalk with dissolve
    d "There is nothing left for us to discuss today..."
    stop music fadeout 6
    if GreenHeart > 2 and redinteract == 2 and purpleinteract == 2 and blueinteract == 2 and silverinteract == 2 and route == "no":
        if easymeter: 
            show screen easymeter 
            show screen greenmeter
        show d neu with dissolve
        "He stops me before I can leave."
        show d sidetalk with dissolve
        d "Ms. Hart, do you mind if I follow you outside?"
        show d neu with dissolve
        "I freeze. I didn't expect that at all."
        show d talk with dissolve
        d "Although I am staying here for the nightshift, I still have some amount of time to spare."
        show d neu with dissolve
        "Do I want him to walk me to the entrance...?"
        menu:
            "I don't mind":
                play music "ost/hospital.wav" fadein 6
                $GreenHeart+=2
                $route = "green"
                m flirt "I'll be glad to be accompanied by you."
                scene bg offices with dissolve
                "We leave his office and I'm still wondering what just happened."
                "Does he really enjoy my company?"
                "There's no other way to explain it, but it still strikes me as odd..."
                scene black with dissolve
                "On our way to the reception, he asks me various things about my job, the hospital, my patients..."
                "I like working here and I make sure to let him know that."
                "Strangely, I don't feel as anxious while talking to him now as I used to."
                "Unlike before, he doesn't make me feel pressured or interrogated."
                "I guess he really was doing it on purpose before."
                "Once I get over the fact that I'm talking to him like this, it's surprisingly easy for me."
                scene bg greetsun with dissolve
                show d smirk with dissolve
                "We arrive at the reception and I stop in the door leading outside."
                show d neutral with dissolve
                "He looks at me in silence for a brief moment and I somehow can't bring myself to speak up."
                show d neutalk with dissolve
                d "I will see you again on Monday."
                show d smile with dissolve
                "For a split second, I think there's a genuine smile on his face."
                stop music fadeout 2
                show d sidetalk with dissolve
                d "Don't be late again."
                play sound "doorclose.ogg" fadein 1
                hide screen greenmeter
                hide screen easymeter
                scene black with hpunch
                "He shuts the door behind me and I'm left alone outside."
                play music "ost/hospital.wav" fadein 5
                "I was painfully reminded that he's still my boss and likely doesn't intend to let our relationship interfere with my work."
                "The word \"relationship\" sounds odd like this... I don't know if I should call it that, but he's taken a liking of sorts to me for sure."
                scene bg sunset with dissolve
                "Walking back home, I wonder..."
                "What about me? Am I really willing to look at him as more than just my boss..?"
                "It's just that he intruiges me in some way and that right now I feel like I may be more interested in him than any of my patients here..."
                "...What am I saying?"
                "I must be tired after today... I'm not thinking straight."
                stop music fadeout 5
                "With him or not, this is my job and I intend to take it seriously."
                "And about what I called \"our relationship\"... only time can tell."
                show drk with dissolve
                "{i}Would you like to save your game?"
                menu:
                    "Yes":
                        show text "{size=100}{color=#ffffff}Week I, Friday\nevening\nSharpe's route":
                            ypos 300
                        $renpy.pause()
                        $ renpy.call_in_new_context("_game_menu")
                    "No":
                        pass
                hide drk with dissolve
                "Dr. Sharpe's route is currently unavailable. Please select a different one to continue to week 2."
                return
            "No, thank you":
                d "In that case..."
                d "You may leave, Ms. Hart. I will see you again on Monday."
                jump leaveworkfriday
    else:
        d "You are dismissed, Ms. Hart."
        jump leaveworkfriday
label leaveworkfriday:
    stop music fadeout 3
    scene bg offices with dissolve
    "I leave Dr. Sharpe's office and close the door behind me quickly."
    "That got tense..."
    if route is not "no" and tutorials:
        call screen tuto7
    play music "footsteps.ogg" fadein 0.5
    scene bg patients with dissolve
    "I make my way through the hospital."
    "It's quite dark outside already."
    "My footsteps echo in the empty hallways..."
    scene black with dissolve
    play music "ost/tran.wav" fadein 6
    "I pass a couple of nurses on my way, but most of the staff must have left for the weekend already."
    "After leaving the hospital, I rethink my choices from this week..."
    scene bg frontsun with dissolve
    stop music fadeout 5
    if GreenHeart > 3 and redinteract == 2 and purpleinteract == 2 and blueinteract == 2 and silverinteract == 2 and professional > personal + 5:
        "Dr. Sharpe offered to walk me downstairs, but I refused."
        "I don't really feel comfortable enough around him to want to spend any more time than necessary with him."
        "He's my boss and a very strict one at that."
        "I'd rather avoid him as much as possible."
    if route == "red":
        "This week allowed me to create a bond with Michael."
        "I wonder where my relationship with him will lead me..."
        show drk with dissolve
        "{i}Would you like to save your game?"
        menu:
            "Yes":
                show text "{size=100}{color=#ffffff}Week I, Friday\nevening\nMichael's route":
                    ypos 300
                $renpy.pause()
                $ renpy.call_in_new_context("_game_menu")
            "No":
                pass
    elif route == "blue":
        "This week allowed me to create a bond with Charlie."
        "I wonder where my relationship with him will lead me..."
        show drk with dissolve
        "{i}Would you like to save your game?"
        menu:
            "Yes":
                show text "{size=100}{color=#ffffff}Week I, Friday\nevening\nCharlie's route":
                    ypos 300
                $renpy.pause()
                $ renpy.call_in_new_context("_game_menu")
            "No":
                pass
    elif route == "silver":
        "This week allowed me to create a bond with William."
        "I wonder where my relationship with him will lead me..."
        show drk with dissolve
        "{i}Would you like to save your game?"
        menu:
            "Yes":
                show text "{size=100}{color=#ffffff}Week I, Friday\nevening\nWilliam's route":
                    ypos 300
                $renpy.pause()
                $ renpy.call_in_new_context("_game_menu")
            "No":
                pass     
    elif route == "purple":
        "This week allowed me to create a bond with Tom."
        "I wonder where my relationship with him will lead me..."
        show drk with dissolve
        "{i}Would you like to save your game?"
        menu:
            "Yes":
                show text "{size=100}{color=#ffffff}Week I, Friday\nevening\nTom's route":
                    ypos 300
                $renpy.pause()
                $ renpy.call_in_new_context("_game_menu")
            "No":
                pass
    if route == "golden":
        "Elizabeth... I think I'll keep meeting her on my breaks whenever I can."
        "I should be able to help her with whatever problems she's facing."
        show drk with dissolve
        "{i}Would you like to save your game?"
        menu:
            "Yes":
                show text "{size=100}{color=#ffffff}Week I, Friday\nevening\nElizabeth's route":
                    ypos 300
                $renpy.pause()
                $ renpy.call_in_new_context("_game_menu")
            "No":
                pass
        "Elizabeth's route is currently unavailable. Please select a different one to continue to week 2."
        return
    if route=="no":
        pause 1.5
        scene black with dissolve
        pause 3
        "Days pass uneventfully..."
        "I keep coming to the hospital every day, but nothing changes."
        "It feels empty..."
        pause 1
        "I quit my job. It was meaningless."
        "I couldn't help anyone."
        "I never managed forge bonds with my patients."
        "I wish I could start again... maybe I would do better."
        $renpy.quit()
    else:
        scene black with Dissolve(1.0)
        if easymeter:
            "Would you like to adjust your difficulty settings for the rest of the game?"
            menu:
                "Yes":
                    call screen difficulty
                "No":
                    pass
        jump routedream
        
label firedfriday:
    stop music fadeout 6
    show d coldtalk with dissolve
    d "It seems that you are not fit for this job, given the circumstances of your first week of work."
    show drk with dissolve
    show d neutalk with dissolve
    d "Gather your belongings from your office and {color=#51ad93}leave the hospital{/color} as quickly as you can, Ms. Hart."
    show d neutral with dissolve
    stop music fadeout 3
    d "I hope to never see you again here."
    scene fired with Dissolve(1.0)
    "You were fired. Return to the beginning of the week and make different choices to reach the end of the demo."
    return
    
label momcall:
    scene black with dissolve
    "What... was that dream?"
    "I was... in the hospital..?"
    "I... feel like there was more to it..."
    pause 1
    play music "ost/tran.wav" fadein 3
    scene bg mcliving with Dissolve(1.0)
    $renpy.pause()
    play sound "chars.ogg" 
    show screen notify("{size=24} Your Location Info screen has been updated!")
    "I don't really have anything to do today..."
    "Other than..."
    stop music
    m freeze "...!"
    "I... {w}I haven't called mom since I got the job."
    "Oh my god. That's... bad."
    "I search for my phone and call."
    ".{w}.{w}.{w}."
    play music "ost/sunny.wav" fadein 6
    show mcphone 2 with dissolve
    mm "...[name]? I was wondering whether or not I should call the police at this rate."
    show mcphone 3 with dissolve
    m no "Umm... I'm sorry I didn't call at all this week..."
    mm "I was worried sick about you! What happened?"
    mm "Did you at least get that job?"
    m "I did! It... it wasn't that hard, mom..."
    show mcphone 1 with dissolve
    mm "Well, you sure made it sound that way."
    mm "What were you thinking, moving there before even getting the job?"
    m "I... I figured it couldn't be that hard..."
    mm "Sweetheart, you know I believe in you, but..."
    show mcphone 2 with dissolve
    m "Amelia said I could move in anytime."
    mm "How long will she be gone for, either way?"
    m "A whole year. She's coming back in summer."
    mm "It's a good thing you two kept in touch since high school."
    mm "How is the house, by the way?"
    show mcphone 1 with dissolve
    m "It's almost too big for me, to be honest."
    mm "You know, [name]... It's not like you're going to live alone forever."
    show mcphone 3 with dissolve
    m "...."
    mm "Ah, I remember when you two were just kids..."
    mm "And look at her now - she's travelling so much she barely lives in her own house."
    "I can sense my mom's mild disappointment from miles away."
    show mcphone 2 with dissolve
    m "Well... At least I can walk to work every day."
    show mcphone 1 with dissolve
    mm "It's that close?"
    m "Yeah. I was surprised as well."
    mm "That's convenient."
    mm "How big is that town, anyway? Do you have everything you need there?"
    show mcphone 2 with dissolve
    m "It's pretty small, but it's not like I need that much..."
    mm "[name], I've seen how you used to pack for school trips."
    show mcphone 1 with dissolve
    m "That was a long time ago!"
    mm "Just don't forget to take care of yourself! You know how you used to -"
    show mcphone 3 with dissolve
    m "Mom, I remember."
    m "I'm an adult. I can handle it."
    mm "Are you sure about that?"
    show mcphone 2 with dissolve
    m "I'll be fine. If anything happens, I'll call you."
    mm "That's what I like to hear. Dad and I are both rooting for you, [name]."
    show mcphone 3 with dissolve
    stop music fadeout 4
    m "Mom..."
    mm "I know. You're not a child anymore."
    scene black with dissolve
    "I tell mom to say hi to dad from me and hang up."
    "...."
    show bg mcliving with dissolve
    play music "ost/hospital.wav" fadein 5
    "Ever since I was a teenager, my mom felt the compulsive need to make sure everything is okay with me."
    "It's like she was sure something would go wrong."
    "In her defense, I've always been good at getting myself in trouble..."
    stop music fadeout 3
    show bg mclivingnight with Dissolve(1.0)
    "I can live here until summer. After that, who knows..?"
    scene black with Dissolve(1.0)
    jump janehills
label sundayweekone:
    scene black with dissolve
    "What... was that dream?"
    "...."
    "Who was that..?"
    show janehills with dissolve
    hide janehills with dissolve
    "I can't... remember. What did I see in that dream..?"
    "Did that... really happen?"
    "I feel like it did... Why would I dream about a memory like that now?"
    "Maybe it's because I haven't talked to mom in a while..."
    jump nextday
label suemonday:
    scene bg greet with dissolve
    "I'm back at the hospital. Let's see what -"
    show su neu with moveinright
    play music "ost/sunny.wav" fadein 6
    sue "...."
    show su laugh with dissolve
    sue "Hey, it's good to see you, [name] ~"
    show su smile with dissolve
    sue "Back to work after the weekend?"
    m cute "Sure am. It's good to be back."
    show su happy with dissolve
    sue "You got through the first week, congrats ~"
    show su cute with dissolve
    sue "Trust me, it's only going to get easier now."
    show su smile with dissolve
    m conf "Thanks ~"
    m fabtalk "I better go now. I wouldn't want to be late."
    show su talk with dissolve
    sue "I should... be leaving as well."
    hide su happy with moveoutright
    sue "See you around, [name]! Good luck out there ~"
    play sound "footsteps.ogg" fadein 2
    show bg cafe with dissolve
    show bg patients with dissolve
    show bg central with dissolve
    show bg offices with dissolve
    scene bg mcdark with dissolve
    stop music fadeout 5
    "Someone must've cleaned my office over the weekend."
    "The curtains are closed again."
    scene bg mc with dissolve
    "Alright, I'm ready. Let's get to work."
    if route=="red":
        jump rednav
    elif route=="blue":
        jump bluenav
    elif route=="silver":
        jump silvernav
    elif route=="purple":
        jump purplenav
    else:
        jump patientchoice
label afterjanereveal:
    play sound "ost/janes.ogg"
    scene bg mcbed with vpunch
    m no "{i}JANE..!"
    play music "ost/jane.wav" fadein 6
    "Jane. {color=#ad86e0}Jane, my older sister{/color}...{w} How could I have forgotten..?"
    "I... I haven't seen her in my dreams for a few years at least."
    "I haven't even thought about her all this time..."
    "And now she showed up in my dream... That can't be a coincidence."
    "I remember that day... It really happened."
    "...wait."
    stop music fadeout 5
    "I... had a dream last week... On Saturday."
    "Was that..? {w}Jane, that was Jane. I remember now."
    "She... used to take me on these \"adventures\" whenever she didn't want to be around our parents."
    "I saw it... in a dream... Even though I was sure I forgot about it."
    scene black with dissolve
    "That was a happy memory... {w}Jane..."
    if route=="red":
        jump rednav
    elif route=="purple":
        jump purplenav
    elif route=="blue":
        jump bluenav
    elif route=="silver":
        jump silvernav
    elif route=="golden":
        jump goldnav
    elif route=="green":
        jump greennav
    else:
        jump patientchoice
    
label hierweek2:
    stop music fadeout 3
    scene bg mc with Dissolve(1.0)
    play sound "knock.ogg" 
    if route =="blue":
        "My office sure is a popular destination lately."
    else:
        "Huh..? Who could this be?"
    m neu "Come in."
    play music "ost/tension.ogg" fadein 6
    show d neutalk with dissolve
    d "Ms. Hart? Do you have a moment?"
    show d neutral with dissolve
    m fab "Of course. I just finished my work."
    show d sidetalk with dissolve
    d "I apologize for bothering you this late, but I was..."
    stop music fadeout 5
    show d frust with dissolve
    d "...Becoming worried. About your second week of work here."
    show d cold with dissolve
    "...oh?"
    m frusttalk "I thought you said you wouldn't oversee my work after the first week."
    play music "ost/hospital.wav" fadein 8
    show d neutral with dissolve
    m fabtalk "Is something wrong?"
    show d neutalk with dissolve
    d "No, nothing of the sort. I simply wanted to check if everything is going as you desired."
    show d talk with dissolve
    d "Did you encounter any problems? Are you still making progress with the patients?"
    show d neutral with dissolve
    menu:
        "Everything is going well":
            $professional+=1
            m flirt "I really had no problems so far, everything is going well."
            m conf "My patients are a pleasure to work with."
            show d sidesmile with dissolve
            d "I am very glad to hear that."
            show d smile with dissolve
            d "I hope it remains this way."
        "...I've had no problems":
            m conf "I'm sure it will be fine, I've had no serious problems so far."
            show d regrettalk with dissolve
            d "I... suppose I can take it as a good sign."
            show d cold with dissolve
            m talk "It's really fine, I can handle it."
        "I don't need help":
            $wrong+=1
            m talk "I managed everything on my first week, why would I fail now?"
            show d neu with dissolve
            m fab "I'm perfectly capable of handling my patients on my own, Doctor."
            show d regrettalk with dissolve
            d "I apologize if my questions made you think I mistrusted you, Ms. Hart."
            show d calmtalk with dissolve
            d "There is no harm in asking for help if you need it."
            show d neu with dissolve
        "It's getting difficult":
            $personal+=1
            m serious "To be honest, after last week, everything became a little... hectic."
            show d cold with dissolve
            m regrettalk "...with my patients."
            show d sidetalk with dissolve
            d "How so?"
            show d frust with dissolve
            m "I feel like... I'm losing control more and more."
            m talk "I'm not sure, though... I could be overreacting. I'm sorry."
            show d coldtalk with dissolve
            d "There is nothing to apologize for, Ms. Hart. Are you sure you can handle your current set of patients?"
            show d neutral with dissolve
            m angry "I won't give up now. I just... need to think about everything that's going on."
            show d calmtalk with dissolve
            d "I understand."
            show d calm with dissolve
    "He steps away from me."
    show d regrettalk with dissolve
    d "I should not bother you for any longer."
    show d regretsmile with dissolve
    d "You must be tired after a whole day of work."
    show d calmsmile with dissolve
    menu:
        "I still have questions":
            $personal+=1
            show d gasp with dissolve
            d "Oh? Is that so?"
            stop music fadeout 6
            show d sidetalk with dissolve
            d "I am all ears. What do you wish to know?"
            show d calmsmile with dissolve
            play music "ost/tran.wav" fadein 8
            "He takes a seat by my desk. I'm somehow surprised by his openness."
            "It's not often that I get to talk to him like this."
            show d smirk with dissolve
            "I should make the most of it."
            m frust "Ummm..."
            "I'm not sure what to ask. There's so much I can learn from him."
            menu:
                "Ask for advice about my patients":
                    show d neutral with dissolve
                    m fab "Could you tell me some more about my patients?"
                    show d neutalk with dissolve
                    d "Your patients? Are you sure you aren't referring to one of them in particular?"
                    show d siden with dissolve
                    "One of them..?"
                    "Of course I'm referring to one of them. The one I've been spending the most time with..."
                    "The one I've been having trouble with."
                    show d neu with dissolve
                    if route=="red":
                        "...Michael."
                        "He told me about how he got here today, but... our last session ended up quite tense."
                        m talk "I'm still focusing on Michael."
                        show d sidetalk with dissolve
                        d "And how is that going?"
                        show d frust with dissolve
                        m frusttalk "It's been... getting a little complicated recently."
                        m sadtalk "Do you know what happened before he got here?"
                        show d neutalk with dissolve
                        d "Of course. I am his psychiatrist, after all."
                        show d smirk with dissolve
                        m gasp "...."
                        m fab "I didn't know that."
                        show d sidetalk with dissolve
                        d "It is true that I know all the patients here, but I can help you the most with the ones I have personally worked with."
                        show d neutalk with dissolve
                        d "So what is the problem? Have you learned too much for your\ncomfort, Ms. Hart?"
                        show d cold with dissolve
                        menu:
                            "Yes":
                                m boretalk "I... just need some time to process everything I learned."
                                m fabtalk "These last few sessions felt a lot more in-depth than our previous ones."
                                show d calmtalk with dissolve
                                d "I understand. Mr. Burnett has a habit of making psychologists uncomfortable."
                                show d calmsmile with dissolve
                                m neu "...."
                                show d neu with dissolve
                                m fabtalk "What about psychiatrists?"
                                show d talk with dissolve
                                d "I have nothing to fear from him, and neither do you."
                                show d calmtalk with dissolve
                                d "As long as you remain reasonable, that is."
                            "No":
                                m angry "I think I can handle it."
                                show d calmtalk with dissolve
                                d "Very well."
                        show d neutalk with dissolve
                        d "How is your experience with him so far? You seem to be doing well, from what I know."
                        show d neutral with dissolve
                        m frust "It's been... intense. But I think we're going in the right direction."
                        show d sidetalk with dissolve
                        d "He claims you are the best psychologist he has ever had."
                        show d sidesmile with dissolve
                        m gasp "Have you... asked him about me?"
                        show d neutalk with dissolve
                        d "Only during your first week of work here. I had to make sure you were not doing anyone harm."
                        show d neutral with dissolve
                        "I... guess that makes sense."
                        m boretalk "Did he not... have any issues with me?"
                        show d regretsmile with dissolve
                        "He chuckles. I don't think it's very professional to ask him about it, but still..."
                        "I don't think he minds, strangely."
                        show d talk with dissolve
                        d "No, he was very open about his opinion of you."
                        show d neutalk with dissolve
                        d "Believe it or not, the first few psychologist he has had here reported that he barely talked to them."
                        show d frusttalk with dissolve
                        d "Of course, it was due to his state right after... the incident. He has recovered quite quickly."
                        show d sidetalk with dissolve
                        d "With the amount of scars he has, I would assume it was a necessity."
                        show d frust with dissolve
                        "Interesting point. He does seem to move on quickly from all kinds of trauma."
                        show d neutalk with dissolve
                        d "Is there anything else you would like to ask about him?"
                        show d neutral with dissolve
                        stop music fadeout 8
                        menu:
                            "Does he enjoy working with you?":
                                $personal+=2
                                show d regrettalk with dissolve
                                d "I never directly asked him about it, but..."
                                show d talk with dissolve
                                d "I believe so. He has never showed any sign of unease around me."
                                show d calmtalk with dissolve
                                d "And if he does not enjoy working with me, he must at least tolerate my presence."
                                show d smirk with dissolve
                                m conf "That's good to hear."
                            "Do you think I can get him out of here?":
                                m regrettalk "After all, he {i}has{/i} had 17 psychologists so far..."
                                show d cold with dissolve
                                m sad "It's possible there's a point past which I can't help him."
                                show d regrettalk with dissolve
                                d "There is no such thing as being unable to help, Ms. Hart."
                                show d neutalk with dissolve
                                d "Whether you are capable of making him \"normal\" or not is beyond me."
                                show d sidesmile with dissolve
                                d "But I do think you have what it takes."
                        play music "ost/neutral.ogg" fadein 6
                        menu:
                            "Could there be more to him than that?":
                                show d neu with dissolve
                                d "\"More\"?"
                                show d talk with dissolve
                                d "Are you implying he never really moved on after what happened three years ago?"
                                show d siden with dissolve
                                m talk "It's a possibility."
                                show d frusttalk with dissolve
                                d "It is, and what happened definitely had some repercussions, at least on a subconscious level."
                                show d sadtalk with dissolve
                                d "Other than that, I simply do not know."
                                show d neutalk with dissolve
                                d "However, Mr. Burnett does not strike me as the kind of person to keep secrets."
                                show d sidetalk with dissolve
                                d "If you have the mindset of questioning everything you learn about a patient, you may be focusing on the wrong person."
                                show d frust with dissolve
                                m gasp "What..?"
                                show d calm with dissolve
                                d "We were talking about Mr. Burnett. Let us not discuss the others."
                            "You never felt threatened by him?":
                                $personal+=1
                                show d neu with dissolve
                                d "Threatened? No, not quite."
                                m regrettalk "I mean... he has a history of hurting staff members... who's to say he can't hurt one of us?"
                                show d sidetalk with dissolve
                                d "I would not be bothered by such a possibility, Ms. Hart."
                                show d coldtalk with dissolve
                                d "The nurses are quite wary of him after the incident involving one of them three years ago."
                                show d talk with dissolve
                                d "They would never mishandle someone like him."
                                show d neu with dissolve
                                m frust "...."
                                show d sidetalk with dissolve
                                d "Unless... your anxiety is caused by your own intentions."
                                show d neutral with dissolve
                                m shock "..!"
                                show d neutalk with dissolve
                                d "I would not feel threatened by him without any... \"safety measures\", but I would advize you to think carefully."
                                show d calmsmile with dissolve
                                d "Other than that, I wish you the best of luck."
                                "What... was that just now?"
                                "I better change the topic."
                            "That's all":
                                $professional+=1
                    elif route=="silver":
                        $moonsharpeknow=True
                        "...William."
                        "Our last session was quite... tense. He finally told me about what happened two years ago."
                        "I can't help but worry about him after what happened... he seemed very shaken today."
                        show d neu with dissolve
                        m regrettalk "I'm still focusing on William, but... it's gotten a little difficult."
                        "I recall today's events, and how anxious he got after telling me the truth."
                        "I didn't know what to do... I can only hope I did the right thing."
                        show d talk with dissolve
                        d "How so? What happened?"
                        show d cold with dissolve
                        m serious "He... told me what happened two years ago. Before he was admitted here."
                        show d frusttalk with dissolve
                        d "Ah. I understand."
                        show d regret with dissolve
                        stop music fadeout 5
                        m talk "Do you know about his past?"
                        show d neutalk with dissolve
                        d "Of course I do. I am his psychiatrist, after all."
                        show d neutral with dissolve
                        m gasp "...."
                        m fab "I didn't know that."
                        play music "ost/neutral.ogg" fadein 8
                        show d calmtalk with dissolve
                        d "It is true that I know all the patients here, but I can help you the most with the ones I have personally worked with."
                        show d talk with dissolve
                        d "So what is the problem? I know William tends to be quite... sensitive."
                        show d neutral with dissolve
                        "...."
                        "I think that's the first time I heard him adress someone by their first name."
                        show d neutalk with dissolve
                        d "Well? You seem somewhat distracted, Ms. Hart."
                        show d cold with dissolve
                        "Right. I should tell him about my concerns." ##Tell them, Naegi
                        m regrettalk "I've never seen him this anxious before. I'm not sure if I handled it correctly..."
                        show d neu with dissolve
                        m sad "I feel bad, asking for advice about this, but I really don't want to mess it up."
                        show d calmtalk with dissolve
                        d "I understand. There is nothing wrong with asking for help, Ms. Hart."
                        show d neutral with dissolve
                        "I... I guess. If it's for the good of my patients, I have to swallow my pride for once."
                        m talk "Do you have any experience handling such anxiety? What should I do if it happens again?"
                        show d frust with dissolve
                        d "That is a difficult question, Ms. Hart. William is a complicated patient to work with."
                        show d sidetalk with dissolve
                        d "The approach you should choose depends on a lot of factors: how comfortable he is around you, how anxious he feels, what reason behind his anxiety is..."
                        show d neutalk with dissolve
                        d "Sometimes it is difficult to predict how he is going to react to your actions."
                        show d regrettalk with dissolve
                        d "I have tried and failed at the beginning, I admit, but I think now I know what to expect."
                        show d neutral with dissolve
                        m "How do you usually deal with situations like this?"
                        show d neutalk with dissolve
                        d "I am fortunate enough to be one of the few staff members he seems to tolerate, at least."
                        show d calmsmile with dissolve
                        d "From what he has told me, I can assume he feels the same way about you."
                        show d neu with dissolve
                        m boretalk "What do you mean by \"tolerate\"?"
                        show d calmtalk with dissolve
                        d "He refuses to interact with most staff members, and that is no exaggeration."
                        show d sidetalk with dissolve
                        d "However, there is a small group fortunate enough to be able to communicate with him well."
                        show d smile with dissolve
                        d "I believe we are both part of it."
                        menu:
                            "Were you his psychiatrist from the start?":
                                $personal+=1
                                show d regretsmile with dissolve
                                d "I was. I am very grateful for this turn of events - I am not sure how he would feel about the others."
                                show d smile with dissolve
                                "It definitely seems like William has taken a liking of sorts to Dr. Sharpe."
                                "I suppose that's a good thing."
                                show d neu with dissolve
                                m gasp "Why do you think he trusts you this much?"
                                show d sidetalk with dissolve
                                d "I cannot quite tell. I can only assume the reason."
                                show d neutral with dissolve
                                m fabtalk "What is it, then?"
                                show d frusttalk with dissolve
                                d "I believe that is something that should remain between the two of us, Ms. Hart."
                                show d calmtalk with dissolve
                                d "William is quite secretive - I am sure he would not like us gossiping about him."
                                show d neutral with dissolve
                                "Fair point. Even though now I'm getting curious..."
                            "Has he said anything important about me?":
                                $personal+=2
                                show d neutalk with dissolve
                                d "When I asked him about you last week?"
                                show d neu with dissolve
                                m neu "Yes."
                                show d calmtalk with dissolve
                                d "He was quite vague, naturally, but I think what he meant is that you are doing well."
                                show d smirk with dissolve
                                "That's a relief."
                                m flirt "Thank you. That's really good to hear."
                            "That's good":
                                $professional+=1
                                pass
                                stop music fadeout 6
                        show d talk with dissolve
                        d "As for your question, if you believe he feels comfortable around you, your options are greatly expanded."
                        show d sidetalk with dissolve
                        d "Determining what he expects from you at that particular moment is crucial."
                        play music "ost/hospital.wav" fadein 8
                        show d calmtalk with dissolve
                        d "Sometimes he wants to be left alone, and bothering him only makes everything worse."
                        show d regrettalk with dissolve
                        d "And sometimes... he wants the opposite. You must pay attention to the most subtle of signs, or you will make a terrible mistake."
                        show d siden with dissolve
                        "That doesn't sound very comforting."
                        m talk "How have you managed to deal with that for two years now?"
                        show d neutalk with dissolve
                        d "It was not always perfect, but most of the time I can avoid making him anxious."
                        show d neutral with dissolve
                        "That's an achievement."
                        m cute "If it's possible, then I can try to do as well as you."
                        show d calmtalk with dissolve
                        d "I believe you have what it takes to surpass me in that regard."
                        show d smile with dissolve
                        d "I wish you the best of luck. I hope you can get him out of here sometime soon."
                    elif route=="purple":
                        "...Tom."
                        "Today I finally learned what his mother's done to him."
                        "As horrible as it was, I was somewhat prepared for that confession."
                        "Edward seemed very anxious about having to tell me all of that, though."
                        show d neutral with dissolve
                        m talk "I'm still focusing on Tom. He's been telling me about his past."
                        m boretalk "Well, him and one of his alters."
                        show d sidetalk with dissolve
                        d "His past? It must be very difficult for him."
                        show d regret with dissolve
                        m serious "Do you know what happened to him?"
                        show d neutalk with dissolve
                        d "I was told of it briefly when he was first admitted here."
                        show d calmtalk with dissolve
                        d "A month ago, maybe two."
                        show d talk with dissolve
                        d "You mentioned one of his alters. Have you met all three of them yet?"
                        show d cold with dissolve
                        stop music fadeout 5
                        m talk "Only two so far. But... the one I spoke to yesterday seemed quite anxious, so..."
                        show d neu with dissolve
                        m "It's possible I might see one of the others tomorrow."
                        play music "ost/neutral.wav" fadein 8
                        show d sidetalk with dissolve
                        d "I cannot quite give you advice, since I have no experience working with Mr. Richards..."
                        show d talk with dissolve
                        d "I could ask his psychiatrist about him, if you have any specific questions."
                        show d neu with dissolve
                        m bored "No, that won't be necessary."
                        show d calmtalk with dissolve
                        d "From what I know, he has expressed no problems with working with you."
                        show d neutral with dissolve
                        "That's a relief, at least."
                        m angry "Do you have any experience working with patients affected by DID?"
                        show d neutalk with dissolve
                        d "Do you?"
                        show d neutral with dissolve
                        m neu "I... I don't. Tom is the first one I've encountered."
                        show d sidetalk with dissolve
                        d "Then I suppose you really need advice."
                        show d siden with dissolve
                        m frust "...."
                        show d neutalk with dissolve
                        d "All I can say for sure is that there is no such thing as a harmful alter."
                        show d calmtalk with dissolve
                        d "They all have a reason for existing within one person - they are, in a way, irreplacable."
                        show d talk with dissolve
                        d "Your goal should be to help them individually with no preconceptions, and then allow them to integrate."
                        show d neutalk with dissolve
                        d "If integration is impossible right now, you should at least aim to make them capable of communication and cooperation."
                        show d frust with dissolve
                        d "The first thing you should be concerned about is not causing them new anxiety, or they may split again."
                    elif route=="blue": ##if hermitfail=True, this event doesn't even happen
                        "...Charlie."
                        "He barely spoke to me today after that dream he supposedly had last night."
                        "I'm not sure if I should really believe everything he says... isn't it dangerous to assume all of it is true?"
                        stop music fadeout 6
                        show d neutral with dissolve
                        m regrettalk "Charlie, he..."
                        m fab "I couldn't get him to meet me in my office today, so I attempted to talk to him in his room."
                        show d neutalk with dissolve
                        d "And how did it go?"
                        show d siden with dissolve
                        m serious "I'm not sure if I can call it a success..."
                        play music "ost/neutral.wav" fadein 8
                        m fab "He's convinced that his memories are coming back to him in the form of dreams."
                        show d talk with dissolve
                        d "And what does he see in these dreams?"
                        show d cold with dissolve
                        m regrettalk "He saw his parents last night. And it made him believe they never loved him, just because he saw them yelling at him."
                        show d calm with dissolve
                        d "I see."
                        m talk "How likely is it for that dream to be a real memory?"
                        show d sidetalk with dissolve
                        d "I cannot tell, Ms. Hart. But it is possible. Maybe he remembers everything already, but refuses to accept it."
                        show d frust with dissolve
                        m angry "Why would he refuse to accept the memories he claims to want so much?"
                        show d neutalk with dissolve
                        d "Sometimes the truth is hard to accept. Maybe he simply wanted it to be different."
                        show d neutral with dissolve
                        m fabtalk "On top of that, he claims that he keeps seeing a forest in his dreams. And he thinks it must be real."
                        m regret "I really don't know what to believe anymore... everything he sees could be false at this point."
                        show d sidetalk with dissolve
                        d "A forest, you say? There are two forests close to this hospital. It is entirely possible that he ended up in one of them at some point."
                        show d neu with dissolve
                        m "He... says that in his dreams, he's always lost. That he doesn't know where to go."
                        stop music fadeout 4
                        show d regret with dissolve
                        d "...."
                        m neu "..?"
                        show d foctalk with dissolve
                        d "Forgive me, Ms. Hart. I think I know what he is talking about when he mentions this forest."
                        show d frust with dissolve
                        play music "ost/emo.wav" fadein 6
                        m serious"What is it?"
                        show d coldtalk with dissolve
                        d "There is a forest on the west side of this town. It is known to be a place where many people go missing."
                        show d neutral with dissolve
                        m sadtalk "Missing?"
                        show d regrettalk with dissolve
                        d "Most of them... never return."
                        show d frust with dissolve
                        "For some reason, he seems reluctant to talk about it."
                        menu:
                            "Could this have happened to Charlie?":
                                $professional+=1
                                show d calmtalk with dissolve
                                d "It... is possible."
                            "Is something wrong?":
                                $personal+=1
                                $GreenHeart+=2
                                show d foctalk with dissolve
                                d "I... was reminded of something I would rather not talk about."
                                show d siden with dissolve
                                "What..? What could he mean by that?"
                        show d neutalk with dissolve
                        d "This forest may well be the place where Charlie has gone at some point."
                        show d sidetalk with dissolve
                        d "Maybe he planned to never leave it when he entered it."
                        show d calmtalk with dissolve
                        d "We may never know, if his memories do not come back."
                        show d neu with dissolve
                        m sadtalk "Do you really think he may have wanted to die there?"
                        m frusttalk "He said he felt lost... it sounded like he wanted to escape."
                        show d talk with dissolve
                        d "It is entirely possible that he changed his mind while he was there."
                        show d siden with dissolve
                        m sadtalk "What could have driven him to something like that?"
                        show d frusttalk with dissolve
                        d "There are many things that could have caused it."
                        show d neutalk with dissolve
                        d "It is not that difficult to cause someone to be willing to commit such an act."
                        show d frust with dissolve
                        d "Especially if he had a history of being mentally unstable before that, which is very likely."
                        "Charlie... Before today, I would never have imagined him like this."
                        show d neutral with dissolve
                        "But now that I saw him depressed, quiet, unwilling to talk..."
                        "I'm starting to doubt if what I saw last week was what he's really like."
                        "I can't tell truth from lie anymore."
                        m uncom "Should I believe him when he claims his dreams to be real?"
                        show d neutalk with dissolve
                        d "It might be the best approach. It could allow you to learn more about him."
                        show d frusttalk with dissolve
                        d "Besides, if you never believe him, he might mistrust you."
                        show d cold with dissolve
                        m regrettalk "I just wish I didn't have to believe such things to help him..."
                        show d calmtalk with dissolve
                        d "Sometimes, we must cross our barriers in order to help, Ms. Hart."
                        show d  with dissolve
                        m frust "...."
                        m talk "Have you ever been forced to cross yours?"
                        d "I have."
                        m serious "Did it benefit your patient?"
                        show d calmtalk with dissolve
                        d "I... believe so."
                        show d regrettalk with dissolve
                        d "But I do wish I was never forced to do such a thing."
                        show d frust with dissolve
                        d "...."
                        stop music fadeout 5
                        show d coldtalk with dissolve
                        d "Ms. Hart, there are times when your sense of duty must be stronger than your beliefs."
                        show d neutral with dissolve
                        "I'm not sure what to make of what he said, but I appreciate any advice."
                        play music "ost/hospital.ogg" fadein 6
                    show d neu with dissolve
                    m smile "Thank you, Doctor. I will take everything you said into consideration."
                    show d calmtalk with dissolve
                    d "I hope it helps you make better choices from now on, Ms. Hart."
                    show d smile with dissolve
                    menu:
                        "That's all, thank you":
                            $professional+=1
                            show d calmsmile with dissolve
                            d "You are welcome, Ms. Hart."
                            play sound "doorclose.ogg" fadein 1
                            scene bg mc with dissolve 
                            "He leaves my office and I gather my things."
                            jump afterwork
                        "I have more questions":
                            show d neutalk with dissolve
                            d "Ask away, then. We have time."
                            show d neutral with dissolve
                "Don't":
                    pass
            $hierques1=False
            $hierques2=False
            $hierques3=False
            $hierques4=False
            jump hier2questions
        "Goodbye":
            $professional+=1
            show d neu with dissolve
            m talk "I will see you tomorrow, then."
            show d frusttalk with dissolve
            d "Goodbye, Ms. Hart."
            show d neutral with dissolve
            show bg offices with dissolve
            "He follows me out of my office and I lock it for the night."
            scene black with dissolve
            "After exchanging glances, we part our ways and I go home."
            if route=="purple":
                jump wednesdayhanged
            jump nextday
label hier2questions:
    "What should I ask now..?"
    menu:
        "Job interview":
            $personal+=3
            $hierques1=True
            "It won't leave me alone."
            show d neu with dissolve
            m confusion "I'm... sorry if this comes across as too forward, but -"
            show d calmsmile with dissolve
            d "Go ahead."
            show d neutral with dissolve
            m talk "The way you acted last week, when you interviewed me and monitored my work, it was completely different."
            show d sidesmile with dissolve
            d "And you are wondering why I changed it now?"
            show d neu with dissolve
            m "Yes."
            show d calmtalk with dissolve
            d "We are coworkers now, Ms. Hart. There is no need for me to intimidate you or test you in any way."
            show d regrettalk with dissolve
            d "The position of a psychologist in this place is a difficult one, a stressful one."
            show d frusttalk with dissolve
            d "If you were to break under pressure, you would not last a day here. I had to see how you reacted to it."
            show d neutral with dissolve
            m fabtalk "So it was just a test?"
            show d calmtalk with dissolve
            d "Of course it was. I hope you did not take it personally, Ms. Hart."
            show d smile with dissolve
            m boresmile "I'm... glad we can cooperate like this now."
            show d sidesmile with dissolve
            d "My job is to make yours easier."
            m cute "~"
            show d neutral with dissolve
            d "But it does not mean I will ignore your mistakes."
            m frust "Of course."
            show d calmtalk with dissolve
            d "Work as you are supposed to, and I will do my best to aid you."
            show d cold with dissolve
        "How long have you worked here?":
            $personal+=2
            $hierques2=True
            show d neutalk with dissolve
            d "Why do you ask?"
            show d neu with dissolve
            menu:
                "Out of curiousity":
                    $personal+=1
                    show d calmsmile with dissolve
                    "He smiles."
                "I want to know if you're reliable":
                    $wrong+=1
                    $professional+=1
                    show d sidetalk with dissolve
                    d "Is that so?"
            show d neutalk with dissolve
            d "I was hired four years ago. And I have been in charge of this place for three."
            show d neutral with dissolve
            "Wow, that's... that's quick."
        "About the psychiatrists":
            $hierques3=True
            m fabtalk "There are three psychiatrist here, right?"
            show d calmtalk with dissolve
            d "That is correct."
            if StarLink>2:
                show d sidetalk with dissolve
                d "Of course, you may as well ask Dr. Young about this, he knows many things about this place."
                show d neutalk with dissolve
                d "He treats one of your patients, Charlie." 
                show d talk with dissolve
                d "The only one you have not met yet, at least to my knowledge, is Dr. Bright - her office is the one numbered VI."
            else:
                show d talk with dissolve
                d "Office VII belongs to Dr. Young - he treats one of your patients, Charlie."
                show d sidetalk with dissolve
                d "And the psychiatrist in VI is Dr. Bright."
            show d calmtalk with dissolve
            d "She oversees Mr. Richards' therapy."
            show d neutral with dissolve
            m neu "I see."
            show d sidetalk with dissolve
            d "It might be of interest to you that I am the psychiatrist of two of your patients, Mr. Moore and Mr. Burnett."
            if route=="silver":
                if moonsharpeknow==False:
                    show d siden with dissolve
                    "He's William's, psychiatrist... I hope he's doing his best to help him."
            show d neu with dissolve
            m gasp "do psychiatrists choose which patient is assigned to them?"
            show d calmtalk with dissolve
            d "Sometimes, yes. Each of us has different disorders we have the most experience with."
            show d neutalk with dissolve
            d "Most of the time, when a new patient is admitted, one of us decides to treat them."
            show d neutral with dissolve
            m fab "Why do you choose the patients you do?"
            show d frust with dissolve
            d "I tend to deal with the most \"troubled\" cases. Ones that are either aggressive or at a high risk of suicide."
            show d neu with dissolve
            m gasp "Why is that?"
            show d calmtalk with dissolve
            d "I know most doctors feel less comfortable around these patients. I assume it must be draining for them."
            show d regretsmile with dissolve
            m frust "But... it isn't for you?"
            show d sidesmile with dissolve
            d "Not quite, no. I am not easily disturbed."
            "It's admirable, in a way. But... also a little scary. Anyone would feel at least a little on edge around someone like Michael."
        "About being in charge":
            $hierques4=True
            $personal+=2
            show d neu with dissolve
            if hierques2:
                m fabtalk "So you've been in charge for three years now..."
                "He nods."
            m angry "What's it like to run this place? It must be difficult to manage all of this."
            show d sidetalk with dissolve
            d "I would not say it is easy, but I do think it comes naturally after a while."
            show d neutalk with dissolve
            d "Nobody seems to have any objections, so I do what is expected of me."
            show d neutral with dissolve
            m frust "Maybe nobody complains because no-one really wants this job. I mean... that's a lot of responsibility."
            show d regretsmile with dissolve
            d "One might say I am used to taking responsibility. Really, you should not concern yourself with me."            
        "Ask about me" if hierques1 and hierques2 and hierques4:
            $personal+=5
            m boretalk "I'm trying my best, but... I hope I've lived up to everyone's expectations."
            show d neu with dissolve
            "He glares at me in what I can only assume to be surprise."
            show d sidetalk with dissolve
            d "Why would you not? You have done well thus far, of course you have."
            show d frust with dissolve
            m talk "Do you really think so?"
            show d talk with dissolve
            d "I would not lie about this."
            show d calmtalk with dissolve
            d "It is perfectly normal to struggle - nobody expects you to achieve the impossible and treat any one of your patients within two weeks."
            show d smile with dissolve
            "I sigh. I know he's right, but... I can't help but feel like I could do better."
            if StarLink>2:
                show d neu with dissolve
                m serious "But you needed a month for your first two patients. And you weren't even supposed to treat them that way."
                show d sidetalk with dissolve
                d "Dr. Young told you, did he not?"
                show d neutral with dissolve
                "I nod."
                show d sadtalk with dissolve
                d "Ms. Hart, every case is different. Your patients are not the easiest ones to handle, you must be aware of that."
                show d cold with dissolve
                m regrettalk "But... they'd both been here for over a year. They must've been difficult."
                show d calm with dissolve
                "He falls silent for a moment."
                show d sidetalk with dissolve
                d "You should not base your evaluation of yourself on other people."
                show d neu with dissolve
                m talk "I know."
            show d talk with dissolve
            d "If you want my honest opinion, I believe you are handling this very well." 
            show d regretsmile with dissolve
            d "You have more energy and good will than most - it is what matters in the end."
            show d smile with dissolve
            m regrettalk "Thank you. I don't know why I feel that way, I just..."
            "I stop myself."
            show d calmsmile with dissolve
            d "It is what I am here for, after all."
            show d smirk with dissolve
        "That's all, thank you" if hierques1 or hierques2 or hierques3 or hierques4:
            show d smirk with dissolve
            d "I hope this helped you in some way. If you have any further questions, please do not hesitate to come to my office anytime."
            m smile "Thank you, Doctor."
            show d calm with dissolve
            "He gets up and leaves."
            if route=="purple":
                jump wednesdayhanged
            jump afterwork
    jump hier2questions
