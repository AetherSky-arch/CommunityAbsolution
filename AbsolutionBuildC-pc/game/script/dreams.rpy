image janeintro d:
    im.MatrixColor("images/cg/JaneIntro.png", im.matrix.brightness(0.2)) with Dissolve(1.0)
    pause 1.0
    im.MatrixColor("images/cg/JaneIntro.png", im.matrix.brightness(-0.2)) with Dissolve(1.0)
    pause 1.0
    repeat
image janeintro d2:
    im.MatrixColor("images/cg/JaneIntro.png", im.matrix.brightness(-0.2)) with Dissolve(1.0)
    pause 1.0
    im.MatrixColor("images/cg/JaneIntro.png", im.matrix.brightness(-1.0)) with Dissolve(1.0)
    pause 1.0
    repeat
    
image janeintro dark=im.MatrixColor(
    "cg/JaneIntro.png",
    im.matrix.brightness(-0.6))
image janeintro bright=im.MatrixColor(
    "cg/JaneIntro.png",
    im.matrix.brightness(1.0))

image janehills:
    "cg/JaneHills1.png" with Dissolve(1.0)
    pause 1.5
    "cg/JaneHills2.png" with Dissolve(1.0)
    repeat

image j 1 = "cg/j1.png"
image j 2 = "cg/j2.png"
image eyes:
    "cg/je1.png"
    pause 4
    "cg/je2.png"
    pause 0.06
    "cg/je3.png"
    pause 0.06
    "cg/je2.png"
    pause 0.06
    repeat
    
image bg frontnight:
    "gui/f/black.png" with dissolve
    "bg/FrontNight.png" with Dissolve(1.0)
image bg patientnightmare:
    "bg/n/PatientsNightmare.png" with Dissolve(1.0)
    pause 1.5
    "bg/n/PatientsNightmare2.png" with Dissolve(1.0)
    repeat

define nn = Character("???", color = '#ffffff', screen="cinematic")
define j = Character("Jane", color = '#ffffff', screen="cinematic")
define nm = Character("[name]", color='#ffffff', screen="cinematic")
define mom = Character("Mom", color='#ffffff', screen="cinematic")
define dad = Character("Dad", color='#ffffff', screen="cinematic")
define mot = Character("Voice", color='#ffffff', screen="cinematic")

image intro3 = "cg/intro3.png"
image intro4 = "cg/intro4.png"

image intro5:
    "cg/intro4.png" with Dissolve(0.4)
    pause 1
    "cg/intro5.png" with Dissolve(0.2)
    pause 0.1    
    "cg/intro6.png" with Dissolve(0.2)
    "cg/intro5.png" with Dissolve(0.2)
    pause 0.1
    "cg/intro6.png" with Dissolve(0.2)
    pause 0.2
    repeat
image jb1 = "cg/jb1.png"
image jb2 = "cg/jb2.png"

image janetarot:
    "cg/Tarot1.png" with Dissolve(1.0)
    pause 1.5
    "cg/Tarot2.png" with Dissolve(1.0)
    repeat

##Dream variables
default strength = True
default StrengthCard = False
default sanity = 50

##MOON: BGs
image bg IIIXmirror = "bg/n/IIIXMirror1.png"
image bg IIIXmirrorb = "bg/n/IIIXMirror1b.png"
image bg IIIXmirror2 = "bg/n/IIIXMirror2.png"
image IIIXfog:
    "bg/n/IIIXFog21.png"
    pause 0.4
    "bg/n/IIIXFog22.png"
    pause 0.4
    "bg/n/IIIXFog23.png"
    pause 0.4
    "bg/n/IIIXFog22.png"
    pause 0.4
    repeat
image IIIXfogblue:
    "bg/n/IIIXFog11.png"
    pause 0.4
    "bg/n/IIIXFog12.png"
    pause 0.4
    "bg/n/IIIXFog13.png"
    pause 0.4
    "bg/n/IIIXFog12.png"
    pause 0.4
    repeat
image mirrorcg1:
    "bg/n/MirrorCG1.png"
image mirrorcg2:
    "bg/n/MirrorCG2.png"
image mirrorcg3:
    "bg/n/MirrorCG3.png"
image mirrorcg4:
    "bg/n/MirrorCG4.png"
image mirrorcg5:
    "bg/n/MirrorCG5.png"
    
image bg IIIX:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX.png" with Dissolve(1.0)
image bg IIIXpatients:
    "gui/f/black.png" with dissolve
    "bg/n/IIIXPatients.png" with Dissolve(1.0)
image bg IIIXpatients2s = "bg/n/IIIXPatients2s.png"
image bg IIIXpatients2 = "bg/n/IIIXPatients2.png"
image bg IIIXcentralglass:
    "gui/f/black.png" with dissolve
    "bg/n/IIIXcentral.png" with Dissolve(1.0)
image bg IIIXkeyroom:
    "gui/f/black.png" with dissolve
    "bg/n/IIIXKey.png" with Dissolve(1.0)
image IIIXwater:
    "bg/n/IIIXWater2.png"
    pause 1
    "bg/n/IIIXWater.png" with Dissolve(2.0)
    pause 0.5
    "bg/n/IIIXWater2.png" with Dissolve(2.0)
    repeat
image XVIII = "bg/n/Moon.png" 
    
image drown:
    "gui/f/black.png"
    pause 0.2
    "bg/n/drown.png" with Dissolve(0.15)
    pause 0.3
    "bg/n/drowned.png" with Dissolve(0.15)
    pause 0.2
    repeat
    
##DREAM III
image bg IIIX3start:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3start.png" with dissolve
image bg IIIX3cupboard:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3cupboard.png" with dissolve
image joor = "bg/n/IIIX3JOOR.png"
image bg IIIX3patients:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3patients.png" with dissolve
image bg IIIX3death:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3Death.png" with dissolve
image bg IIIX3scum:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3Scum.png" with dissolve
image bg IIIX3monster:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3Monster.png" with dissolve
image bg IIIX3turnback:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3TurnBack.png" with dissolve
image bg IIIX3axe:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3AxeRoom.png" with dissolve
    
image bg IIIX3patientroom:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3PatientRoom.png" with dissolve
image bg IIIX3XV:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3XV.png" with dissolve
image bg IIIX3XVIII:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3XVIII.png" with dissolve
image bg IIIX3III:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3III.png" with dissolve
    
image bg IIIX3narrow:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3Narrow.png" with dissolve
image bg IIIX3locked:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3Locked.png" with dissolve
image bg IIIX3ventent = "bg/n/IIIX3VentEnt.png"
image bg IIIX3vent1 = "bg/n/IIIX3Vent1.png"
image bg IIIX3vent2 = "bg/n/IIIX3Vent2.png"
image bg IIIX3vent3 = "bg/n/IIIX3Vent3.png"
image bg IIIX3closet:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3Closet.png" with dissolve
image bg IIIX3darknessent:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3DarknessEnt.png" with dissolve
image bg IIIX3darknessent2:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3DarknessEnt2.png" with dissolve
image bg IIIX3darkness:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3Darkness.png" with dissolve
image bg IIIX3cloth:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3ClothRoom.png" with dissolve
image bg IIIX3offices:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3Offices.png" with dissolve

image bg IIIX3hier:
    "bg/n/IIIX3Hier1.png" with Dissolve(1.0)
    pause 1.2
    "bg/n/IIIX3Hier2.png" with Dissolve(1.0)
    repeat
image bg IIIX3mc:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3MC.png" with dissolve
image bg IIIX3young:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3Young.png" with dissolve
image bg IIIX3central:
    "gui/f/black.png" with dissolve
    "bg/n/IIIX3Central1.png"
image IIIX3centralscare:
    "bg/n/IIIX3Central1.png"
    pause 0.3
    "bg/n/IIIX3Central2.png" with dissolve
    pause .2
    "bg/n/IIIX3Central3.png" with dissolve
    pause 1.5
    "gui/f/black.png"
    
image IIIX3knife = "bg/n/IIIX3knife.png"
image IIIX3stick = "bg/n/IIIX3stick.png"
image IIIX3chair = "bg/n/IIIX3chair.png"
image moonnote = "bg/n/Moonnote.png"

image IIIX3door 1 = "bg/n/IIIX3door1.png"
image IIIX3door 2 = "bg/n/IIIX3door6.png"
image IIIX3door scare:
    "bg/n/IIIX3door1.png"
    pause 0.06
    "bg/n/IIIX3door2.png"
    pause 0.06
    "bg/n/IIIX3door3.png"
    pause 0.06
    "bg/n/IIIX3door4.png"
    pause 0.06
    "bg/n/IIIX3door5.png"
    pause 0.06
    "bg/n/IIIX3door6.png"
    pause 0.06
image IIIX3cloth 1 = "bg/n/IIIX3cloth1.png"
image IIIX3cloth 2 = "bg/n/IIIX3cloth2.png"
image IIIX3foot:
    "bg/n/IIIX3foot1.png"
    pause 0.04
    "bg/n/IIIX3foot2.png"
    pause 0.04
    "bg/n/IIIX3foot3.png"
    pause 0.04
    "bg/n/IIIX3foot4.png"

## DREAM IV
image fullmoon1:
    "gui/f/black.png" with dissolve
    "bg/n/Fullmoon1.png" with dissolve
image fullmoon12:
    "gui/f/black.png" with dissolve
    "bg/n/Fullmoon12.png" with dissolve
image fullmoon13:
    "gui/f/black.png" with dissolve
    "bg/n/Fullmoon13.png" with dissolve
image fullmoon14:
    "gui/f/black.png" with dissolve
    "bg/n/Fullmoon14.png" with dissolve
image fullmoon2:
    "gui/f/black.png" with dissolve
    "bg/n/Fullmoon2.png" with dissolve
image fullmoon22:
    "gui/f/black.png" with dissolve
    "bg/n/Fullmoon22.png" with dissolve
image fullmoon23:
    "gui/f/black.png" with dissolve
    "bg/n/Fullmoon23.png" with dissolve
image fullmoon24:
    "gui/f/black.png" with dissolve
    "bg/n/Fullmoon24.png" with dissolve
image fullmoonright:
    "gui/f/black.png" with dissolve
    "bg/n/FullmoonRight.png" with dissolve
image fullmoonleft:
    "gui/f/black.png" with dissolve
    "bg/n/FullmoonLeft.png" with dissolve
image fullmoonleft2:
    "gui/f/black.png" with dissolve
    "bg/n/FullmoonLeft2.png" with dissolve
image fullmoonend 1:
    "gui/f/black.png" with dissolve
    "bg/n/FullmoonEnd1.png" with dissolve
image fullmoonend 2 = "bg/n/FullmoonEnd2.png"
image fullmoonend 3:
    "bg/n/FullmoonEnd2.png" with Dissolve(1.0)
    pause 0.5
    "bg/n/FullmoonEnd3.png" with Dissolve(1.0)
    repeat
define sn = Character("Shadow", screen="cinematic", color="#ffffff")

image shfull 2 = "sprites/moon/s/Fullc1.png" ##far
image shfull 3 = "sprites/moon/s/Fullc2.png" ##really far
image shfull 1: ##hands down
    "sprites/moon/s/Full1.png"
    pause 0.06
    "sprites/moon/s/Full12.png"
    pause 0.06
    "sprites/moon/s/Full13.png"
    pause 4
    "sprites/moon/s/Full12.png"
    pause 0.06
    repeat
image shfull 12: ##hands up
    "sprites/moon/s/Full23.png"
    pause 4
    "sprites/moon/s/Full22.png"
    pause 0.06
    "sprites/moon/s/Full2.png"
    pause 0.06
    "sprites/moon/s/Full22.png"
    pause 0.06
    repeat
image shfull 4: ##close
    "sprites/moon/s/Fullc4.png"
    pause 4
    "sprites/moon/s/Fullc4e2.png"
    pause 0.06
    "sprites/moon/s/Fullc4e3.png"
    pause 0.06
    "sprites/moon/s/Fullc4e2.png"
    pause 0.06
    repeat
image shfull 5: ##really close
    "sprites/moon/s/Fullc3.png"
    pause 4
    "sprites/moon/s/Fullc3e2.png"
    pause 0.06
    "sprites/moon/s/Fullc3e3.png"
    pause 0.06
    "sprites/moon/s/Fullc3e2.png"
    pause 0.06
    repeat
image shwill:
    "gui/f/black.png"
    pause 0.06
    "bg/n/MoonEyes2.png"
    pause 0.06
    "bg/n/MoonEyes3.png"
    pause 0.06
    "bg/n/MoonEyes4.png"
image fm 1a:
    "bg/n/fm/1a.png" with Dissolve(1.0)
    pause 1.0
    "bg/n/fm/1a2.png" with Dissolve(1.0)
    repeat
image fm 1b:
    "bg/n/fm/1b.png" with Dissolve(1.0)
    pause 0.5
    "bg/n/fm/1b2.png" with Dissolve(1.0)
    repeat
image fm 2a:
    "bg/n/fm/2a.png" with Dissolve(1.0)
    pause 1.0
    "bg/n/fm/2a2.png" with Dissolve(1.0)
    repeat
image fm 2b:
    "bg/n/fm/2b.png" with Dissolve(1.0)
    pause 0.5
    "bg/n/fm/2b2.png" with Dissolve(1.0)
    repeat
image fm 3a:
    "bg/n/fm/3a.png" with Dissolve(1.0)
    pause 1.0
    "bg/n/fm/3a2.png" with Dissolve(1.0)
    repeat
image fm 3b:
    "bg/n/fm/3b.png" with Dissolve(1.0)
    pause 0.5
    "bg/n/fm/3b2.png" with Dissolve(1.0)
    repeat
image fm 4a:
    "bg/n/fm/4a.png" with Dissolve(1.0)
    pause 1.0
    "bg/n/fm/4a2.png" with Dissolve(1.0)
    repeat
image fm 4b:
    "bg/n/fm/4b.png" with Dissolve(1.0)
    pause 0.5
    "bg/n/fm/4b2.png" with Dissolve(1.0)
    repeat
image moonshadowfused:
    "MoonShadowFused.png" with Dissolve(1.0)
    pause 1.5
    "MoonShadowFused2.png" with Dissolve(1.0)
    repeat

##Inventory
default IIIXkey1 = False
default moonlightscare = False

##DEVIL: BGs
image bg centralburn = "bg/n/CentralBurn.png"
image bg centralburn2 = "bg/n/CentralBurn2.png"
image closeXVburn = "bg/n/CloseupXVBurn.png"
image closeXVburn2 = "bg/n/CloseupXVBurn2.png"
image revsky1 = "bg/n/RevSky1.png"
image revsky2 = "bg/n/RevSky2.png"
image revsky3 = "bg/n/RevSky3.png"
image revsky4 = "bg/n/RevSky4.png"
image revsky5 = "bg/n/RevSky5.png"
image revsky6 = "bg/n/RevSky6.png"
image revsky7 = "bg/n/RevSky7.png"
image revsky8 = "bg/n/RevSky8.png"
image revsky9 = "bg/n/RevSky9.png"

image d1:
    "ac/d1.png"
    pause 6
    "ac/d2.png" with Dissolve(0.2)
    pause 0.08
    "ac/d3.png" with Dissolve(0.2)
    pause 0.08
    "ac/d4.png" with Dissolve(0.2)
    pause 0.08
    "ac/d5.png" with Dissolve(0.2)
    
image d12 = "ac/d5.png"
image d13 = "ac/d6.png"
image d14 = "ac/d7.png"

image d21 = "bg/n/Devil21.png"
image d22 = "bg/n/Devil22.png"
image d23 = "bg/n/Devil23.png"
image d24 = "bg/n/Devil24.png"

image motherharlot:
    "bg/n/MH1.png" with Dissolve(1.0)
    pause 2
    "bg/n/MH2.png" with Dissolve(1.0)
    repeat
image motherharlot2:
    "bg/n/MH1.png" with Dissolve(1.0)
    pause 0.5
    "bg/n/MH2.png" with Dissolve(1.0)
    repeat

## quotes
image rq 1:
    "bg/n/revq/1.png" with Dissolve(2.0)
    pause 1.2
    "bg/n/revq/12.png" with Dissolve(1.0)
    pause .8
    repeat
image rq 1l = "bg/n/revq/1l.png"
image rq 1g = "bg/n/revq/1g.png"
image rq 2:
    "bg/n/revq/2.png" with Dissolve(2.0)
    pause 1.2
    "bg/n/revq/22.png" with Dissolve(1.0)
    pause .8
    repeat
image rq 2l = "bg/n/revq/2l.png"
image rq 2g = "bg/n/revq/2g.png"
image rq 3:
    "bg/n/revq/3.png" with Dissolve(2.0)
    pause 1.2
    "bg/n/revq/32.png" with Dissolve(1.0)
    pause .8
    repeat
image rq 3l = "bg/n/revq/3l.png"
image rq 3g = "bg/n/revq/3g.png"
image rq 4:
    "bg/n/revq/4.png" with Dissolve(2.0)
    pause 1.2
    "bg/n/revq/42.png" with Dissolve(1.0)
    pause .8
    repeat
image rq 4l = "bg/n/revq/4l.png"
image rq 4g = "bg/n/revq/4g.png"
image rq 5:
    "bg/n/revq/5.png" with Dissolve(2.0)
    pause 1.2
    "bg/n/revq/52.png" with Dissolve(1.0)
    pause .8
    repeat
image rq 5l = "bg/n/revq/5l.png"
image rq 5g = "bg/n/revq/5g.png"
image rq 61:
    "bg/n/revq/61.png" with Dissolve(2.0)
    pause 1.2
    "bg/n/revq/612.png" with Dissolve(1.0)
    pause .8
    repeat
image rq 62:
    "bg/n/revq/62.png" with Dissolve(2.0)
    pause 1.2
    "bg/n/revq/622.png" with Dissolve(1.0)
    pause .8
    repeat
image rq 6l = "bg/n/revq/6l.png"
image rq 6g = "bg/n/revq/6g.png"

## TOWER
define em = Character("Emperor", color='#ffffff', screen="cinematic")
#BGs:
image bg patientshanged = "bg/n/PatientsHanged.png"
image hangedscare:
    "gui/f/black.png" with dissolve
    pause 1.5
    "bg/n/Hanged2.png" with Dissolve(1)
    pause 1.2
    "bg/n/Hanged1.png" with Dissolve(0.6)
    pause 4
    "bg/n/Hanged2.png" with Dissolve(0.1)
    pause 0.2
    "bg/n/Hanged1.png" with Dissolve(0.1)
    pause 0.2
    "bg/n/Hanged2.png" with Dissolve(0.1)
    pause 0.2
    "bg/n/Hanged1.png" with Dissolve(0.2)
    pause 3
    "bg/n/Hanged3.png" with Dissolve(0.2)
    pause .8
    "bg/n/Hanged1.png" with dissolve
    pause 0.5
    "gui/f/black.png" with Dissolve(0.6)
    pause 0.2
    "bg/n/Hanged4.png" with Dissolve(1.0)
    pause 3
    "gui/f/black.png" with Dissolve(2.0)
    
image hangedchild = "bg/n/ChildHanged.png"
    
## HERMIT 
image hdream1:
    "cg/CharlieDream1.png" with Dissolve(1.0)
    pause 1.5
    "cg/CharlieDream12.png" with Dissolve(1.0)
    repeat
image patientshermit:
    "bg/n/PatientsHermit2.png" with Dissolve(1.0)
    pause 2
    "bg/n/PatientsHermit.png" with Dissolve(1.0)
    pause 0.5
    repeat
image hermitforest1:
    "gui/f/black.png" with dissolve
    "bg/n/HermitForest1.png" with Dissolve(1.0)

image hermitforest2:
    "gui/f/black.png" with dissolve
    "bg/n/HermitForest2.png" with Dissolve(1.0)
    
image a hermitforest3:
    "gui/f/black.png" with dissolve
    "bg/n/HermitForest4.png" with Dissolve(1.0)

image hermitforest4:
    "gui/f/black.png" with dissolve
    "bg/n/HermitForest3.png" with Dissolve(1.0)

image a help = "bg/n/Transparency.png"
image moonforest = "bg/n/MoonForest.png"
image hangedforest:
    "bg/n/Transparency.png" with dissolve
    "bg/n/HangedForest.png" with Dissolve(1.0)
image devilforest:
    "bg/n/DevilForest1.png"
    pause .8
    "bg/n/DevilForest2.png"
    pause 0.1
    "bg/n/DevilForest3.png"
    pause 0.1
    "bg/n/DevilForest4.png"
    pause 0.1
    "bg/n/Transparency.png"
image hermithand = "bg/n/HermitHand.png"
image hermithands = "bg/n/HermitHands.png"

default Hermitloop=0
image hermitalice:
    "bg/n/HermitA1.png"
    pause 2
    "bg/n/HermitA2.png"
    pause 0.15
    "bg/n/HermitA3.png"
    pause 0.15
    "bg/n/Transparency.png"
image centralhermit:
    "bg/n/HermitCentral.png" with Dissolve(1.0)
    pause 2
    "bg/n/HermitCentral2.png" with Dissolve(1.0)
    repeat
image hermitMC:
    "bg/n/HermitMC.png" with Dissolve(1.0)
    pause 1
    "bg/n/HermitMC2.png" with Dissolve(1.0)
    repeat

#####################################################
### JANE DREAMS #####################################
#####################################################

label janeintro:
    scene black with Dissolve(1.0)
    pause 1
    nt "What is this...? Am I... dreaming?"
    if tutorials:
        call screen tuto4
    play music "ost/jane.ogg" fadein 6
    nn "{cps=5}[name]... [name]..?"
    nt "A voice..? Who is it..?"
    show janeintro bright with Dissolve(0.2)
    show janeintro dark with Dissolve(1.0)
    show janeintro d with dissolve
    show janeintro bright with dissolve
    show janeintro dark with dissolve
    show janeintro d with dissolve
    nn "{i}[name]...? You... hear...?"
    nt "The voice is fading in and out."
    nm "Who are you? Where am I?"
    nn "[name]...{w} [name]..."
    play sound "ost/janes.ogg"
    show intro1 with Dissolve(0.1)
    hide intro1 with Dissolve(0.1)
    show intro2 with Dissolve(0.05)
    hide intro2 with Dissolve(0.3)
    show intro1 with Dissolve(0.2)
    hide intro1 with Dissolve(0.2)
    show intro2 with Dissolve(0.1)
    hide intro2 with dissolve
    nm "...!"
    nm "I... I know you..!"
    nm "You... your name..."
    nt "What is her name..? I...{w} I can't remember..."
    nn "[name]... remember..."
    nn "Remember... what happened..."
    nm "What... what happened?"
    nn "{cps=5}Don't... {i}don't...{/i} don't{w} give{w} up"
    show janeintro d2 with Dissolve(1.0)
    nt "\n{i} \ \ \ \  \ \ \ \ memories"
    stop music fadeout 4
    show janeintro dark with Dissolve(1.0)
    nm "No! {i}WAIT!"
    nn "[name]... {w}be careful..."
    scene black with Dissolve(1.0)
    pause 1
    jump nextday

label janehills:
    scene black with Dissolve(1.2)
    pause 2
    nt "Another dream...?"
    play music "ost/jane.ogg" fadein 6
    scene janehills with Dissolve(1.5)
    nt "I... I remember that day."
    nt "We left the house to go on one of our \"adventures\"."
    nt "When I was little, she used to take me with her on these long walks."
    nt "I can't remember where exactly we went on that day anymore, but it was further away from home than usual."
    nm "Did you tell mom and dad where we're going?"
    nn "I did, don't worry."
    nn "I'm just... tired, I don't want to see any stupid adults right now."
    nn "Just the two of us, right?"
    nm "It's pretty here ~"
    nn "..."
    nt "She wasn't looking at me at all."
    nt "I was worried about her that day, even if I was very young - I could tell something was wrong."
    nm "Why are you sad?"
    nt "She chuckled softly."
    nn "Do I seem sad?"
    nt "I hesitated."
    nm "No, but..."
    nm "Bad things happen when you want to be alone."
    nt "She was silent for a moment."
    nn "You may be right, then."
    nn "But right now I'm happy. Nothing bad is going to happen."
    nm "Promise?"
    nn "I promise."
    nt "...."
    nn "Are you worried about me?"
    nt "I nodded. Of course I was, as much as any caring sister would be."
    stop music fadeout 5
    nn "You're one cute dork, [name]."
    scene black with Dissolve(2.0)
    pause 1
    jump nextday
    
label janeroute:
    stop music fadeout 2
    scene black with Dissolve(2.0)
    $renpy.pause(2,hard=True)
    nt "Is that... you again..?"
    nm "I remember you."
    play music "ost/jane.ogg" fadein 8
    if route == "silver":
        image janemoon = "cg/JaneSilver.png"
        show janemoon with Dissolve(1.0)
        nt "I hear the voice of my younger self."
        nm "Jane?"
        j "What is it?"
        nm "What happens to people after they die..?"
        nt "She looks at me in silence."
        j "Where did that come from, [name]?"
        nm "I asked mom and dad, but they said I'm too small and I shouldn't ask about that..."
        j "That's bullshit... You aren't too small to be curious about it."
        nm "So..?"
        j "The truth is..."
        nt "She looks outside towards the sky for a moment..."
        j "Nothing happens."
        nm "What does that mean..?"
        j "It's over. Empty."
        nm "How do you know?"
        j "I don't."
        j "I just hope so."
    elif route == "blue":
        image janehermit = "cg/JaneBlue.png"
        show janehermit with Dissolve(1.0)
        nm "Come back! I won't ask you to play with me again, I promise..."
        j "Leave me alone, [name]."
        nm "Where are you going, Jane..?"
        j "You wouldn't understand... I need to be alone right now."
        nm "...."
        j "Hey, [name]... I'm just going out for a walk, like we used to."
        nm "Take me with you, then ~!"
        j "It's different this time... Please, just let me go once..."
        j "I'll be back."
        j "I need some time to rethink everything..."
        j "...Don't tell parents where I went."
        scene black with Dissolve(1.0)
        nt "She didn't come home until late at night."
        nt "It wasn't the first time."
    elif route == "purple":
        image janetower = "cg/JanePurple.png"
        show janetower with Dissolve(1.0)
        j "Look at me, [name]..."
        j "Is this who I really am?"
        nm "What do you mean?"
        nm "You're just... in the mirror."
        nt "She chuckles, but keeps looking at her reflection."
        j "You know, I feel weird looking at myself like that..."
        j "Most of the time, you try to picture yourself however you want to, but faced with your own reflection..."
        j "It's impossible to fool yourself, isn't it?"
        j "And I still do, huh..?"
        j "That's... an unpleasant sight."
        j "It's just how people want to see me."
        nt "She touches the glass with her pale hand."
        j "This isn't the real me..."
        j "But then again, who am I to judge..?"
        j "I don't know what \"the real me\" even means."
    elif route == "red":
        image janedevil = "cg/JaneRed.png"
        show janedevil with Dissolve(1.0)
        "I see a familiar scene play out."
        mom "Is something wrong, dear?"
        j "Huh? No, of course not!"
        mom "Then why do you keep avoiding us?"
        j "What? I never -"
        mom "Stop arguing with me and tell me the truth."
        j "I... don't have anything to tell you..."
        mom "Are you sure of that?"
        j "Yes. Yes I am, mother."
        mom "Then I suppose you aren't going to explain to me why you're wearing that hoodie in the middle of summer?"
        mom "You could at least roll the sleeves up a bit, you're going to boil in th-"
        j "{i}No!"
        j "I... I'm fine."
        nt "My mother scoffed."
        mom "As you wish."
        mom "Ah, what have I done to deserve a daughter as stubborn as you..?"
        mom "At least your sister knows how to behave. You should be setting an example for her, not the other way around."
        mom "And you keep wandering off to god knows where... She's going to turn out troublesome because of you."
        j "Shut up!"
        mom "Excuse me?"
        j "I said shut up! I care about [name] more than both of you ever have!"
        mom "That's enough! I think you need some alone time to rethink what you said."
        mom "Go to your room. I expect an apology tomorrow."
        play sound "doorclose.ogg" fadein 1
    elif route == "green":
        pass
    scene black with Dissolve(1.0)
    jump nextday
label janeback1:
    define mom = Character("Mom", color='#ffffff', screen="cinematic")
    define dad = Character("Dad", color='#ffffff', screen="cinematic")
    stop music fadeout 2
    scene black with Dissolve(1.0)
    $renpy.pause(1,hard=True)
    scene jb1 with Dissolve(1.0)
    play music "ost/jane.ogg" fadein 8
    j "How could you?!"
    j "Are you heartless?"
    mom "Jane, sweetie, it was just a bird..."
    j "It wasn't just another bird! It lived with us for three months now -"
    j "And now... now it's..."
    dad "It's your fault for not thinking about it enough."
    dad "Treat it as a lesson - if you care about something,you should take responsibility."
    mom "Paul, that's a bit harsh..."
    dad "Who did you expect to handle your own problems?"
    dad "You took it in - you should be grateful we agreed to keep it in the first place."
    j "{i}Are you deaf?{/i} You fucking murdered it!"
    mom "Language -!"
    j "Mom, can't you be on my side for once..? You're always following his orders..."
    mom "That \"he\" is your father, Jane. Show some respect."
    j "I'm so done with you... I wish you would both just go to hell."
    play sound "doorclose.ogg" fadein 1
    scene black with hpunch
    nt "The door swung open and nearly hit me in the face. I shouldn't be here..."
    nt "I fell down."
    nt "Jane doesn't notice me as she storms through the hallway and to her room, slamming the door behind her."
    nt "I never liked fights..."
    jump nextday
label janeback2:
    stop music fadeout 2
    scene black with Dissolve(1.0)
    $renpy.pause(1,hard=True)
    scene jb2 with Dissolve(1.0)
    play music "ost/jane.ogg" fadein 8
    play sound "knock2.ogg" 
    nm "Jane? Are you there?"
    j "Leave me alone, [name]!"
    nm "I won't yell at you..."
    j "I don't care, just go with them."
    nt "My parents were about to leave the house to go shopping."
    nt "But, somehow... I knew I couldn't leave Jane alone like this."
    nt "Not that day. Not at that moment."
    play sound "doorclose.ogg" fadein 1
    nt "I stayed by the door until I heard my parents leave."
    nt "Jane was silent."
    play sound "knock.ogg" 
    j "{i}Wha -?"
    j "You're still there? What on earth are you doing here..?"
    nm "I didn't want you to be alone."
    nt "I heard a chuckle, but it doesn't sound happy at all."
    j "You know, [name], you're the only good thing that's ever happened to me."
    j "Maybe it's because you don't really understand everything, but you never question what I do and how I act..."
    j "You're always so determined to help, I... I wish I had your strength, [name]."
    j "...But I don't."
    j "So I just wanted to say..."
    j "I'm sorry. For every time I was selfish and didn't consider you."
    j "And for what is about to happen."
    show drk with dissolve
    j "Thanks for sticking with me until the end, {i}[name] -"
    stop music fadeout 5
    nt "Her voice cracked. I think she was crying."
    nm "Jane?"
    j "Y-yes?"
    nm "...can you open the door?"
    scene black with Dissolve(2.0)
    play sound "doorclose.ogg" fadein 1
    jump nextday
label janesuicide:
    scene black with Dissolve(1.0)
    $renpy.pause(1,hard=True)
    play music "ost/jane.ogg" fadein 8
    play sound "doorclose.ogg" fadein 1
    scene intro1 with Dissolve(2.0)
    nt "I spotted Jane by her bird's cage."
    nt "I couldn't make out if it was inside or not... the cage was locked."
    nm "Are you still sad about it..?"
    j "It... doesn't really matter now, either way."
    nt "She looked out the window."
    scene intro2 with Dissolve(1.0)
    j "Parents are out... They just left."
    nt "I looked closely at Jane, confused."
    nm "If you're not sad about your bird, why are you crying..?"
    j "Oh, [name]... you can tell?"
    nt "I nodded."
    j "I don't really know..."
    j "I guess I'm crying for a lot of different reasons."
    j "Look at mom and dad."
    j "First they let it die, then blame me, and they're leaving like it's none of their business."
    j "Their shopping is probably more important than me, anyway."
    nm "Don't say that! They're just angry, but it'll pass. It always does!"
    j "How many times have I told myself that..?"
    j "They stop being angry, then yell at me again the next day."
    j "Nothing changes, [name]. And it won't."
    j "I don't know what they expect from me anymore..."
    j "It's like they only care when I do well at school."
    nm "But they care - we all care about you!"
    j "You're too kind, [name]... They don't deserve a child like you..."
    nt "She touched the glass in front of her."
    j "Why are you here, [name]...?\nJust to watch me suffer? You can't help me."
    j "Leave."
    nm "I won't leave you, Jane."
    j "If that's so..."
    stop music fadeout 1.5
    show intro3 with Dissolve(1.0)
    nt "She opened the window."
    nt "It was snowing outside..."
    nt "The bright light filled the room for a brief moment..."
    nt "Before I realized what's happening, it was too late."
    scene black with vpunch
    nm "{i}{b}JANE!"
    scene intro4 with Dissolve(2.0)
    nt"I fall to my knees, unable to process what I just saw."
    nt "I hear my mom's scream first, then my dad's curses."
    nt "My face on the cold floor, I close my eyes and listen."
    nt "An ambulance. A police car."
    nt "Footsteps."
    nt "My parents' voices."
    show intro5 with dissolve
    nt "Everything was so distant... I stopped caring after a while."
    nt "Jane..."
    nt "{i}She left me."
    nt "Now I was as alone as she's always felt."
    $renpy.pause(3,hard=True)
    jump nextday
label janereal: ##Monday, week IV on Sharpe's route
    scene black with Dissolve(1.5)
    $renpy.pause(2,hard=True)
    play music "ost/jane.ogg" fadein 6
    nt "I'm... dreaming?"
    nn "{i}[name]..? [name]!"
    nt "The voice is quiet, but it... it sounds familiar."
    nn "[name]? You can hear me?"
    nm "I can. Who are you?"
    nn "...."
    nn "Don't you recognize your own sister..?"
    scene j 2 with Dissolve(1.5)
    show eyes
    nm "Jane!? But you -"
    j "I'm here now. It's so good to see you again, [name]."
    nm "H- How? How are you... here?"
    nt "She smiles at my confusion."
    nt "It's not a forced smile like the ones she used to put on for my sake."
    nt "She seems... different than I remember. More mature."
    nm "Jane..? You're not real, are you..?"
    nm "I'm just... remembering things and they must have -"
    j "No. This isn't a memory. {w}I'm {i}here."
    nm "Who are you..?"
    j "I'm your sister, you dork."
    nm "But... she's dead. You're dead."
    j "I am. I know it's hard to understand, but... I'm back. {w}Somewhat."
    show j 1 with dissolve
    j "Do you remember the dream you had after your first day of work?"
    nm "Someone... told me not to give up."
    j "That was me. I've been trying to talk to you since you started working at that hospital."
    nm "What does that have to do with you?"
    j "Everything."
    j "I... think what happened sixteen years ago is connected to what is happening now."
    nm "How?"
    j "I don't know! I just- Just trust me on this."
    j "I feel like... someone's been watching me. Ever since I could start contacting you."
    nm "Watching you? How?"
    j "If I knew anything more, I would've explained it better, gosh..."
    nm "...sorry."
    j "No no no- It's fine. Just let me finish because I have no idea how much time we have."
    j "And... I had to warn you. I feel like something bad is about to happen to you if you're not careful enough."
    j "So. This whole dream thing."
    j "I've been... still. For sixteen years."
    j "Well, not exactly... But I couldn't leave. I couldn't even see you."
    j "But then... once you took this job, I... I found something like. A door."
    show j 2 with dissolve
    j "[name], I see that look and I don't blame you, but bear with me."
    show j 1 with dissolve
    j "I tried to reach you then, but failed. It was like you were far away."
    nm "And now you're... closer? Why?"
    j "It became easier to reach you over time."
    j "I think... it might have to do with this place."
    nm "The hospital?"
    nt "I remember Jane used to be into the occult when she was alive."
    nt "...my mother wasn't too happy about that."
    show j 2 with dissolve
    j "Ah, that. It's coming in handy now."
    nm "You... heard my thoughts?"
    j "You didn't say that? Huh."
    nt "This can't be real... I'm dreaming, anything can happen in a dream."
    show j 1 with dissolve
    j "...."
    j "I'm sorry."
    nm "Huh?"
    j "I know it's hard to wrap your head around and you don't believe me yet."
    j "And... if it weren't for me leaving you this would never have happened."
    menu:
        "Do you regret having done that?":
            j "Dying? Yes, of course I do."
            j "I was... I was stupid. I let my feelings take over."
            j "I'm really sorry I left you like that. You were just a kid."
            nm "...."
        "It's your fault":
            $StrengthCard=False
            $sanity-=20
            j "My... my fault?"
            j "It really is..."
            j "...."
        "What was it like?":
            $StrengthCard=False
            $sanity-=20
            j "Dying?"
            nm "Yes."
            j "I don't remember. I just woke up... different, I guess."
    nm "So you showing up in my dreams has to do with the hospital?"
    show j 2 with dissolve
    j "Yes! Yes, I'm sure of that."
    nm "And it's not because I had dreams about what happened sixteen years ago?"
    j "Huh? Dreams?"
    show j 1 with dissolve
    nm "I... saw things. That I didn't want to remember."
    j "[name], I... I had no idea..."
    nm "It's okay. I moved on."
    nt "I don't want to dwell on the past."
    nm "So... you didn't cause those dreams?"
    show j 2 with dissolve
    j "No. But they might be why I was able to talk to you like this."
    j "I... might have a theory."
    j "Okay [name], listen up."
    show j 1 with dissolve
    nt "She pauses to collect her thoughts."
    j "Someone or something to do with that place bridged the gap between life and death."
    j "It's why I was able to talk to you once you started working there."
    j "And... for whatever reason, whatever is responsible is watching me."
    j "They might be interested in you. And they probably don't mean well."
    j "I just... have a feeling that something bad has attached itself to you."
    j "I don't know what it is. You might want to find someone who senses these things and ask them."
    nt "I... struggle to believe any of this."
    nm "What could happen if that \"something bad\" gets me?"
    j "Anything, really. Depends on what it is and how much power it has."
    j "But... I'm certain it doesn't have good intentions."
    show drk with Dissolve(1.0)
    nt "Whether or not I believe Jane, I should be careful once I'm back to the hospital."
    j "Okay. I think that's all. I might be gone in a moment, I think it's breaking up..."
    nm "Jane! Wait..!"
    j "Oh?"
    show drk 2 with dissolve
    nt "I reach out to her and hug her. She's fading and so is my vision."
    nm "Please... {w}come back..."
    nm "...whenever you can."
    scene black with Dissolve(1.0)
    $renpy.pause()
    j "I'll keep an eye out for you, dork."
    pause 2
    $renpy.pause()
    play sound "page.ogg" fadein 1
    show buildc with Dissolve(1.0)
    $renpy.pause()
    return
    
label routedream:
    scene black with Dissolve(1.0)
    nt "I'm exhausted after today... I go to bed earlier than usual and fall asleep almost immediately."
    pause 2
    play music "ost/dream.wav" fadein 6
    nt "...."
    scene bg frontnight
    nt "I'm... standing before the hospital..?"
    nt "...how did I get here?"
    nt "The last thing I remember is falling asleep... I must be dreaming."
    play sound "ost/janes.ogg"
    show bg frontnight:
        ease 1.0 zoom 1.2 
    scene black with dissolve
    nt "I take a step forward and soon feel the ground slipping from under my feet."
    nt "Where am I now..?"
    nt "I can't see a thing."
    pause 1
    show bg patientnightmare
    pause 2
    nt "Woah... what is this place..?"
    nt "I hear... voices calling me from all directions... pulling me towards..."
    nt "...the doors."
    if route=="green":
        stop music fadeout 3
        nt "But..."
        scene black with Dissolve(1.0)
        nt "Somehow, I'm pulled further inside."
        nt "{i}The place few have reached..."
        nt "It's too dark to see, but... I open a door that appears before me."
        play sound "doorclose.ogg" fadein 1
        nt "Suddenly, everything around me disappears."
        nn "{i}Did you really think I'd let you see everything so soon ~?"
    elif route=="red":
        stop music fadeout 3
        scene black with dissolve
        nt "I approach the door labelled XV."
        nt "It... feels warm. It's like sunlight on my skin."
        nt "I pull the handle."
        play sound "doorclose.ogg" fadein 1
        nt "Suddenly, everything around me disappears."
        nm "Oh god... {i}What happened here?"
    elif route=="silver":
        stop music fadeout 3
        scene black with dissolve
        nt "I approach the door labelled XVIII."
        nt "Something shines above me... I can feel a cool breeze waft through my hair."
        nt "It feels like midnight by a river."
        play sound "doorclose.ogg" fadein 1
        nt "I push the door open and suddenly, everything around me disappears."
        nn "{b}{i}Not so fast."
    elif route=="purple":
        stop music fadeout 3
        scene black with dissolve
        nt "I approach the door labelled XVI."
        nt "It's almost... bursting with energy."
        nt "The sudden flash of lightning makes me feel like there's so much more to see beyond the door."
        play sound "doorclose.ogg" fadein 1
        nt "Once I open it, everything disappears."
        nn "{i}[name]... [name]..? Are you... there?"
    elif route=="blue":
        stop music fadeout 3
        scene black with dissolve
        nt "I approach the door labelled IX."
        nt "Something feels so familiar about it... maybe it's the smell of trees."
        nt "I feel like my heart walks in before my feet."
        play sound "doorclose.ogg" fadein 1
        nm "Huh..? Where am I?"
    else: 
        stop music fadeout 3
        scene black with dissolve
        nt "I approach the door labelled II."
        nt "Is that... a fog? It feels unnatural."
        nt "I have to go inside."
        nt "Suddenly, everything around me disappears."
        nt "All is still and quiet."
    pause 1
    scene black with Dissolve(1.0)
    if route=="green" or route=="golden":
        $renpy.pause()
        "This route is not available beyond week 1 in the current build. Please choose a different one to continue."
        return
    jump nextday
label skycollapse:
    stop music fadeout 2
    scene black with Dissolve(1.0)
    $renpy.pause(3,hard=True)
    play sound "page.ogg" fadein 1
    show rq 1l with dissolve
    show rq 1g with dissolve
    play sound "page.ogg" fadein 1
    show rq 1
    $renpy.pause()
    scene black with Dissolve(1.0)
    pause 1
    nt "Where... am I?"
    play music "fire.ogg" fadein 10
    nt "Slowly, an image emerges before my eyes."
    scene bg centralburn with Dissolve(1.5)
    nt "It's as if I'm not really here... {i}where{/i} am I?"
    nt "I get up. I can't see my hands."
    nt "Flames. A fire."
    nt "What is this?"
    nt "And why am I here?"
    nt "I walk up to the window. The glass is hot under my fingers. I flinch away."
    nt "This is the hospital... I don't understand."
    scene black with dissolve
    play sound "glass.ogg"
    scene bg centralburn2 with dissolve
    nt "The window broke due to the heat... I can barely see anything..."
    nt "The fire threatens to engulf the building in flames."
    stop music fadeout 5
    nt "I'm forced to retreat until my back hits the wall."
    nt "I escape into a dark hallway."
    scene black with dissolve
    nt "Where do I go from here? I can barely see..."
    scene bg patientsnight with dissolve
    nt "Keeping my hand on the wall to my left, I hesitantly start walking."
    nt "I can still get out."
    nt "To where? I don't know."
    nt "I don't know if there's anything left outside."
    play sound "light.ogg" fadein 2
    show bg patients with Dissolve(0.3)
    stop sound fadeout 1
    show bg patientsnight with dissolve
    nt "...huh?"
    nt "Are the lights still on?"
    play sound "light.ogg" fadein 2
    show bg patients with Dissolve(0.35)
    show bg patientsnight with Dissolve(0.2)
    show bg patients with Dissolve(0.15)
    pause 0.3
    play sound "glass2.ogg" fadein 1
    scene black with Dissolve(0.1)
    nt "The lights are out. I can't see anything."
    nt "I keep walking, carefully moving my hand on the wall."
    nt "Glass beneath my fingers... warm... Doors to the rooms of patients, all no longer there."
    scene closeXVburn with dissolve
    play music "fire.ogg" fadein 4
    nt "What is this door..?"
    nt "It's one of the patient rooms."
    nt "I can faintly see the number... XV."
    nt "Walking towards the door, I need to shield my eyes from the intense light coming from behind the door."
    nt "Is this... fire?"
    nt "For reasons I can't explain, I find myself unable to move away from it."
    scene closeXVburn2 with dissolve
    "I open the door."
    "A gust of hot air hits my face."
    "I go inside."
    stop music fadeout 1
    scene black with Dissolve(1.0)
    play music "ost/ludu.ogg"
    scene black with dissolve
    pause 0.5
    show revsky1 with Dissolve(1.0)
    $renpy.pause(4,hard=True)
    show revsky2 with Dissolve(2.0)
    show revsky3 with Dissolve(0.75)
    show revsky4 with Dissolve(0.75)
    show revsky5 with Dissolve(0.75)
    show revsky6 with Dissolve(0.75)
    show revsky7 with Dissolve(0.75)
    show revsky8 with Dissolve(0.75)
    show revsky9 with Dissolve(0.75)
    pause 2
    scene black with Dissolve(1.0)
    pause 1
    play sound "page.ogg" fadein 1
    show rq 2l with dissolve
    show rq 2g with dissolve
    play sound "page.ogg" fadein 1
    show rq 2
    stop music fadeout 6
    $renpy.pause()
    scene black with Dissolve(1.0)
    pause 1
    show d1 with Dissolve(2.0)
    $renpy.pause(5, hard=True)
    play sound "ost/dscare.ogg"
    scene d12 with dissolve
    show d13 with Dissolve(0.1)
    hide d13 with Dissolve(0.1)
    show d13 with Dissolve(0.1)
    show d14 with Dissolve(0.1)
    hide d14 with Dissolve(0.1)
    hide d13 with Dissolve(0.1)
    play music "ost/devil.wav"
    show d13 with Dissolve(0.1)
    hide d13 with Dissolve(0.1)
    show d13 with Dissolve(0.1)
    show d14 with Dissolve(0.1)
    hide d14 with Dissolve(0.1)
    scene black with dissolve
    pause 1
    jump nextday
label ladyinsun:
    stop music fadeout 2
    scene black with Dissolve(1.0)
    pause 1
    play sound "page.ogg" fadein 1
    show rq 3l with dissolve
    show rq 3g with dissolve
    play sound "page.ogg" fadein 1
    show rq 3
    $renpy.pause()
    scene black with Dissolve(1.0)
    pause 1
    ##sfx
    pause 1
    play music "ost/devil.wav" 
    nt "I wake up to the sound of a knife being plunged into flesh."
    nn "Dead... She's already dead..."
    show d21 with Dissolve(1.0)
    nn "...but there's still blood left to spill."
    nn "Further, further..."
    nn "I need... more..."
    nn "...Is there anything more?"
    nn "She's dead..."
    nn "...dead."
    nn "Does it matter?"
    nn "It doesn't change anything."
    nn "You were always dead... right?"
    nn "At least to me."
    show d22 with Dissolve(1.0)
    pause 1
    nn "It's over... it's over..."
    nn "You can't even scream anymore..."
    nn "That's right. I... only had one chance to do this..."
    nn "I can't part with you yet... why?"
    $renpy.music.set_volume(0.5, 2, 'music')
    pause 1.5
    show d23 with Dissolve(1.0)
    nn "...I see you."
    nn "You're the reason why I can't rest yet."
    nn "[name]..."
    show d24 with Dissolve(1.0)
    nn "You're next."
    play sound "ost/dscare.ogg"
    scene black
    pause 1
    show rq 4l with dissolve
    show rq 4g with dissolve
    show rq 4
    $renpy.pause()
    scene black with Dissolve(1.0)
    jump nextday
    
label motherharlot:
    stop music fadeout 2
    scene black with Dissolve(1.0)
    pause 1
    play sound "page.ogg" fadein 1
    show rq 5l with dissolve
    show rq 5g with dissolve
    play sound "page.ogg" fadein 1
    show rq 5
    $renpy.pause()
    scene black with Dissolve(1.0)
    pause 1
    nt "...."
    nt "Is this... another nightmare?"
    pause 1
    play music "ost/devilA.wav" fadein 6
    nt "I hear a voice calling me from the darkness..."
    nn "{cps=10}{i}Come, take my hand."
    nt "I reach out, to whatever is out there."
    show motherharlot with Dissolve(1.0)
    $renpy.pause()
    nn "{i}{cps=10}Welcome to my domain, wandering soul ~"
    nn "{i}{cps=10}Why are you here..? You do not know?"
    nt "The woman smiles."
    nn "{i}{cps=10}There is room for everyone in my chains, love ~"
    nt "I back out. I can't."
    nt "She was and she is,  and she is yet to come."
    nn "{i}{cps=10}Why, you ask? Why would you join me?"
    nn "{i}{cps=10}Look at them - they all craved me. Desired me."
    nn "{i}{cps=10}I was the only one who understood. Who accepted."
    nn "{i}{cps=10}I am their only love."
    nn "{i}{cps=10}Their only wish."
    nn "{i}{cps=10}They all came begging to me. Desperate."
    nn "{i}{cps=10}How could I refuse ~?"
    nn "{i}{cps=10}My wine is what draws them to me. Do you want to taste it?"
    nn "{i}{cps=10}Do you want to taste me?"
    nn "{i}{cps=10}...they were all like you at first."
    nn "{i}{cps=10}Lost. Confused."
    nn "{i}{cps=10}But once I poured them my wine..."
    nn "{i}{cps=10}They accepted the chains of their own making."
    nn "{i}{cps=10}I am not the monster here, nor am I the tormentor."
    nn "{i}{cps=10}I only gave them what they desired... And I will keep giving for all eternity."
    nn "{i}{cps=10}There is nothing that can tear us apart."
    nn "{i}{cps=10}I am a part of them. They feast on my flesh and bathe in my blood."
    nn "{i}{cps=10}They cannot live without me."
    nn "{i}{cps=10}They gave up everything they had to be a part of me as well."
    pause 2
    nt "I hear the distant clattering of chains."
    nt "It's coming from underground."
    nn "{i}{cps=10}Oh..."
    nn "{i}{cps=10}It must be the eighth."
    nn "{i}{cps=10}My Beast still defies me... It does not yet understand our love."
    nn "{i}{cps=10}It thinks it can leave me... even though I have been with it for so long."
    nn "{i}{cps=10}...."
    nn "{i}{cps=10}I took it when nobody else wanted it. It would have died if it weren't for me."
    stop music fadeout 2
    nn "{i}{cps=10}It saddens me to see my lover reject me... for..."
    nn "{i}{cps=10}...."
    play music "ost/devilB.wav" fadein 2
    show motherharlot2
    nn "{i}{cps=*2}FOR YOU?"
    nn "{i}{cps=*2}YOU ARE THE WHORE WHO WANTS TO TAKE HIM FROM ME?!"
    nn "{i}{cps=*2}THIS IS HIS PLACE. I WILL NEVER LET YOU TEAR HIM AWAY FROM ME."
    nn "{i}{cps=*2}IT WAS HIS CHOICE. HE CHOSE ME."
    nn "{i}{cps=*2}I AM THE ONLY ONE HE LOVES."
    nn "{i}{cps=*2}I AM THE ONLY ONE HE CAN DESIRE."
    nn "{i}{cps=*2}YOU ARE NOTHING. A DROP OF WATER IN A RIVER."
    scene black with vpunch ## Alice screech
    stop music fadeout 3
    nn "{i}{cps=*2}HE WILL NEVER BE FREE. MY WINE FLOWS IN HIS VEINS."
    pause 3
    nt "Darkness swallows me once again."
    stop music fadeout 2
    scene black with Dissolve(1.0)
    pause 1
    play sound "page.ogg" fadein 1
    show rq 6l with dissolve
    show rq 6g with dissolve
    play sound "page.ogg" fadein 1
    show rq 61
    $renpy.pause()
    play sound "page.ogg" fadein 1
    show rq 62 with dissolve
    $renpy.pause()
    jump nextday
##################### MOON ###############################################
label moonrise:
    stop music fadeout 2
    scene black with dissolve
    pause 1
    play music "ost/dream.wav" fadein 8
    nt "Darkness."
    nt "Where am I..?"
    scene bg greetnight
    nt "The hospital..? It must be, except..."
    nt "I've never been here during the night. So what is this..?"
    nt "None of the lights are on, but I can see roughly what's in front of me thanks to the moonlight coming from the windows."
    nt "There's a full moon in the sky..."
    nt "I take a step forward, and open the door."
    scene bg hallwaynight
    nt "The hospital looks normal so far."
    scene bg cafenight
    nt "I go further in, unsure of what to expect, but knowing something awaits me here."
    nt "Calling me."
    nt "I can feel it."
    nt "The pull to go further in... the second floor."
    nt "I don't try to rationalize it, I just keep walking."
    scene black with dissolve
    nt "I end up in the staircase leading to the second floor."
    nt "It's dark... Wait, what's that?"
    show quick with Dissolve(0.3)
    hide quick with Dissolve(0.3)
    $ ui.timer(1, ui.jumps("stairsqtefail"))
    menu:
        "CAREFUL":
            nt "I notice a step missing and navigate over it safely in the darkness."
            nt "That might've been dangerous..."
            jump moonrise2
label stairsqtefail:
    scene black with vpunch
    nt "Ow!"
    nt "I trip on the stairs, failing to notice a missing step."
    nt "I should be more careful in the future."
    jump moonrise2
label moonrise2:
    scene bg officesnight
    nt "When I arrive on the second floor, I'm suddenly in the hallway near my office. Alright."
    nt "Nothing looks out of the ordinary, then again I can barely see anything."
    nt "This isn't where I need to go, though..."
    menu:
        "Check my office":
            nt "The door is unlocked."
            nt "I walk in."
            scene bg mcnight
            nt "What's going on here?"
            nt "And why does my office look so... unfamiliar?"
            menu:
                "Look out the window":
                    show bg night with dissolve
                    nt "The moon looks as if it's watching me..."
            pause 2
            show bg mcnight
            nt "I leave my office, convinced that something is wrong."
        "Leave the offices hallway":
            nt "It's better for me to hurry."
    scene bg centralnight
    nt "Even this place looks threatening at night... So empty..."
    nt "Moonlight is shining through the windows."
    menu:
        "Stop":
            nt "I stop and listen..."
            nt "Voices..."
            nt "They're getting louder as I approach the door."
        "Keep going":
            pass
    scene bg patientsnight
    nt "I open the door and find myself in the patients' rooms hallway."
    nt "There's no lights on, I can barely see..."
    nt "I don't like this."
    nt "I do my best to stay close to the walls... I wonder if there's anyone in the rooms I'm passing by."
    nt "I'm so close now... I can feel it."
    nt "The voices are calling me, pulling me further into the darkness."
    nt "I'm not sure if I'm the one walking anymore."
    nt "The whispers grow louder, more desperate, and I'm stopped suddenly by one of the doors."
    nt "The room is labelled with the number XIX."
    scene black with Dissolve(1.0)
    nt "...."
    nt "There's no point hesitating now..."
    nt "I push the door open."
    scene bg IIIXmirror with dissolve
    show IIIXfogblue with Dissolve(1.0)
    nt "What... is this place?"
    nt "This isn't the hospital..."
    nt "I look behind me."
    nt "The door doesn't budge. Looks like I'm stuck here."
    nt "It's still labelled as room XIX, though..."
    nt "The moon is shining its blueish light on the floor..."
    nt "There are some things scattered on it."
    $mooncheckfloor=False
    $mooncheckwindow=False
    $mooncheckwall=False
label moonrise3:
    menu:
        "Check floor" if mooncheckfloor==False:
            $mooncheckfloor=True
            nt "Pictures..?"
            nt "They all seem to be torn."
            nt "...."
            nt "It's too dark to see them clearly."
            jump moonrise3
        "Check windows" if mooncheckwindow==False:
            $mooncheckwindow=True
            nt "It's snowing outside..."
            nt "I stop by one of the windows and can't look away."
            nt "It looks just like that evening... with Jane..."
            jump moonrise3
        "Check walls" if mooncheckwall==False:
            $mooncheckwall=True
            nt "Missing person posters..."
            nt "They seem to be scattered everywhere in this room."
            nt "I wonder who that is..."
            jump moonrise3
        "Done looking" if mooncheckfloor or mooncheckwindow or mooncheckwall:
            nt "I move further into the room, called by the whispers around me..."
    nt "I'm close now, I can feel it..."
    nt "What called me here? Is it in this room...?"
    nt "A strange symbol appears on the wall..."
    nt "It looks like the sun..."
    nt "Why would there be a sun drawn here?"
    nt "This whole room is a mystery to me."
    show bg IIIXmirrorb with Dissolve(1.0)
    show bg IIIXmirror with dissolve
    show bg IIIXmirrorb with dissolve
    show bg IIIXmirror with dissolve
    nt "What... is happening?"
    menu:
        "Touch the sun":
            pass
        "Look closely":
            nt "My eyes hurt just looking at it, but I force myself to examine it more closely."
            nt "It's just a sun, there's nothing unusual about the drawing itself..."
    nt "I don't know why, but I feel the urge to put my hand on the symbol."
    stop music fadeout 4
    nt "It's... warm."
    show bg IIIXmirrorb with Dissolve(0.3)
    show IIIXfog with Dissolve(0.2)
    show bg IIIXmirror2 with dissolve
    nt "What... happened?"
    nt "I'm still in the same room, but it looks... different."
    nt "Is that... ash? What happened outside?"
    nt "Something appeared on the wall in front of me."
    nt "There's no point trying to go back now."
    nt "I have to see why I'm here."
    show drk with dissolve
    nt "The curtain is heavy..."
    nt "But I know whatever is behind it is crucial to me."
    nt "I need answers."
    nt "I need the truth."
    nt "I tear the curtain."
    scene mirrorcg2 with Dissolve(0.1)
    play music "ost/moons.ogg" fadein 6
    show mirrorcg1 with Dissolve(0.2)
    nt "A mirror..?"
    nt "Is this what I came here to see..?"
    nt "My reflection looks so..."
    nt "Fragile. Helpless."
    nt "No, that's not me. I would never be so... vulnerable. I'm not that person."
    $renpy.pause(1,hard=True)
    show mirrorcg4 with dissolve
    show mirrorcg5 with dissolve
    nt "The voices. They've stopped."
    nt "Have I really found what they wanted me to see?"
    show mirrorcg4 with dissolve
    show mirrorcg3 with Dissolve(0.3)
    scene black
    pause 1
    jump nextday
label moonlight:
    pause 1
    scene black with Dissolve(1.0)
    nt "I wake up in an unfamiliar room."
    nt "It's dark, but... I think I'm in the hospital."
    nt "I'm dreaming again."
    nt "This feels similar to the nightmare I had last week..."
    show bg IIIX with dissolve
    show IIIXfog with Dissolve(1.0)
    nt "I sit up on the floor."
    nt "There's a mirror behind me."
    nt "Could it be..?"
    nt "The room on the other side of the mirror looks familiar."
    nt "I remember it from my previous dream."
    nt "A dark figure appeared behind me... it..."
    nt "It must've pulled me here."
    nt "I stand up slowly."
    nt "So, this is the other side of the mirror..."
    nt "The air seems unusually dense here."
    nt "It's like fog."
    play music "ost/moon.wav" fadein 10
label roomIIIX:
    if IIIXkey1:
        stop music fadeout 3
        scene black with dissolve
        pause 1
        nt "I feel hands on my shoulders."
        nt "Someone is right behind me."
        play music "ost/shadow.ogg" fadein 5
        nn "{b}{i}Hello."
        nt "The voice sounds like a thousand whispers glitched into one."
        nn "{b}{i}You're not supposed to be here, you know?"
        nn "{b}{i}You should play along for now..."
        stop music fadeout 5
        nn "{b}{i}We will see each other again soon."
        play music "ost/moon.wav" fadein 6
        show bg IIIXpatients with hpunch
        show IIIXfog with dissolve
        $sanity-=10
        $strength = False
        jump IIIXpatients1
    else:
        show bg IIIX with dissolve
        menu:
            "Go out":
                jump IIIXpatients1
            "Look around":
                nt "I spot a IIIX written on the door."
                nt "I feel like this isn't just a random detail..."
                nt "The room is dark."
                nt "I can't see much other than that."
                jump roomIIIX
label IIIXpatients1:
    show bg IIIXpatients
    $renpy.pause()
label IIIXpatients1choice:
    menu:
        "Go back to room IIIX" if strength:
            jump roomIIIX
        "Go further into the hallway":
            jump IIIXpatients2
        "Look behind me":
            "There's a door."
            if IIIXkey1:
                nt "Should I use the key to open it?"
                menu:
                    "Yes":
                        nt "I use the key I found..."
                        nt "The door opened!"
                        scene black with dissolve
                        play sound "doorclose.ogg" 
                        nt "I find myself in a narrow hallway."
                        nt "I wonder why this place was locked..."
                        stop music fadeout 6
                        show IIIXfogblue with Dissolve(1.0)
                        nt "Walking further in, I freeze."
                        hide IIIXfogblue with dissolve
                        show IIIXwater with dissolve
                        $renpy.pause()
                        show IIIXfogblue with Dissolve(1.0)
                        nt "Is that... water?"
                        nt "The corridor seems to have collapsed."
                        nt "Why is it ruined like that..?"
                        nt "It's still very dark."
                        nt "The water looks completely black to me."
                        nt "It's cold..."
                        nt "But I feel like I need to go in."
                        menu:
                            "Rush in":
                                $sanity-=10
                                $strength = False
                                scene black with vpunch
                                nt "I can't tell what's ahead of me..."
                                play music "underwater.mp3" fadein 3
                                scene black with hpunch
                                nt "I think I hit my head on something. Ouch."
                                nt "Huh..? I can't feel the water around me anymore."
                                stop music fadeout 3
                                nt "I open my eyes."
                            "Be careful":
                                play music "underwater.mp3" fadein 3
                                nt "Slowly, I put one foot in the water."
                                nt "I don't know why, but I know that I have to go in."
                                show drk with dissolve
                                nt "I dive further into the dark water carefully."
                                nt "Before I can disappear under it completely, I close my eyes."
                                scene black with dissolve
                                nt "But... I don't feel the water covering my face anymore."
                                stop music fadeout 3
                                nt "I raise my head and open my eyes."
                        play music "ost/moon2.ogg" fadein 6
                        scene XVIII with Dissolve(2.0)
                        nt "I'm standing in a river. I look around."
                        nt "This place... it's so beautiful..."
                        nt "Where am I? And how did I get here?"
                        nt "The moon shines above me... it looks so peaceful this time."
                        nt "I take a hesitant step forward."
                        scene drown with vpunch
                        play music "ost/fight.ogg"
                        nm "Gah-!"
                        nt "I'm being pulled back into the water."
                        nt "What's happening?!"
                        show drk with dissolve
                        nt "I can't breathe."
                        nt "The hands around me aren't letting go..."
                        show drk 2 with dissolve
                        nt "I..."
                        $renpy.pause(1,hard=True)
                        nt "{cps=5}...I can't feel anything..."
                        $renpy.pause(2,hard=True)
                        scene black with Dissolve(2.0)
                        jump nextday
                    "No":
                        jump IIIXpatients1choice
            nt "It doesn't budge. It seems to be locked."
            jump IIIXpatients1choice
        "Look around":
            nt "There are rooms around me..."
            nt "This looks like a mirrored version of the hallway on the second floor I came here through."
            nt "Every room has its mirrored number on it..."
            nt "...Except for the one I came from. \"IIIX\"."
            nt "This one room seems special."
            jump IIIXpatients1choice
label IIIXpatients2:
    if IIIXkey1 and moonlightscare==False:
        scene black with dissolve
        pause 0.5
        scene bg IIIXpatients2s with Dissolve(1.0)
        $renpy.pause()
        scene bg IIIXpatients2 with Dissolve(1.0)
        play music "ost/moon.wav" fadein 6
        nm "Who's there..?"
        nm "Hello?"
        nt "There's nobody there. I must be seeing things..."
        show IIIXfog with dissolve
        $moonlightscare = True
    show bg IIIXpatients
    nt "The rooms are labelled with mirrored versions of their regular numbers."
label IIIXpatients2choice:
    menu:
        "Look inside room II":
            if IIIXkey1:
                nt "The key doesn't seem to open this door..."
            else:
                nt "It's... empty?"
            jump IIIXpatients2choice
        "Look inside room IX":
            if IIIXkey1:
                nt "The key doesn't seem to open this door..."
            else:
                nt "There seems to be a dense forest inside."
                nt "Tree branches are blocking my view..."
                nt "It's so quiet... it seems to be empty."
            jump IIIXpatients2choice
        "Look inside room XV":
            if IIIXkey1:
                nt "The key doesn't seem to open this door..."
            else:
                play music "fire.ogg" fadein 5
                nt "I look inside and instantly my eyes burn with pain due to the heat emanating from it."
                nt "Flames are all I can see... I'm blinded temporarily."
                nn "{i}I know you're there..."
                nn "{i}Don't be scared."
                nn "{i}Isn't this what you want?"
                nn "{i}Come in, come in~"
                stop music fadeout 2
                play music "ost/moon.wav" fadein 5
                nt "I step back. This feels wrong."
            jump IIIXpatients2choice
        "Look inside room XVI":
            if IIIXkey1:
                nt "The key doesn't seem to open this door..."
            else:
                nt "My face is instantly hit with a gust of wind."
                nt "There's a storm inside... I see lightning flash in the sky."
                nt "My vision blurs... I step away from the door."
            jump IIIXpatients2choice
        "Go further":
            nt "I walk further down the hallway."
            jump IIIXcentralglass
        "Go back":
            jump IIIXpatients1choice
label IIIXcentralglass:
    show bg IIIXcentralglass
    nt "I spot a glass wall."
    nt "I can see the central hall from here, but..."
    nt "It feels different."
    nt "I move into a small hallway to my left."
label IIIXkeyroom:
    show bg IIIXkeyroom
    nt "It's a dead end."
    menu:
        "Go back":
            jump IIIXpatients2
        "Look around" if IIIXkey1 == False:
            nt "If this is a dead end, there must be something here..."
            nt "I decide to look around."
            nt "A metallic shine catches my eye."
            nt "I look down at my feet."
            $renpy.pause()
            nt "A small key is laying on the ground. Huh."
            $IIIXkey1 = True
            nt "I picked it up."
            stop music fadeout 4
            nt "It might be useful."
            jump IIIXpatients2

label midnight:
    $lighter=False
    $axe=False
    $hammer=False
    $cheater=False
    $stick=False
    $needknife=False
    $knife=False
    $midnightlockedscare=False
    $midnighthangedscare=False
    $screwdriver=False
    $chair=False
    $ventpassed=False
    $needtorch=False
    $needstick=False
    $cloth=False
    $torch=False
    stop music fadeout 3
    scene black with Dissolve(1.0)
    $renpy.pause(2, hard=True)
    nt "I'm... dreaming again..?"
    play music "ost/moon.wav" fadein 8
    scene bg IIIX3start
    $renpy.pause()
    menu:
        "Look around the room":
            nt "I can barely see anything... What is this place?"
            nt "My previous nightmare ended with... me being drowned."
            nt "Did he... take me here to keep me from reaching that river I saw?"
            nt "...."
        "Leave":
            play sound "doorclose.ogg" fadein 1
label IIIX3cupboard:
    scene bg IIIX3cupboard
    nt "At least there's some light here."
    $renpy.pause()    
    menu:
        "Search the cupboard" if not lighter:
            show drk with dissolve
            nt "I don't know what I should be looking for, but... the only thing that seems to work is a small lighter."
            nt "It's better to have a source of light than not to, I suppose."
            nt "Should I take it?"
            menu:
                "Yes":
                    nt "I grab the lighter."
                    $lighter=True
                    jump IIIX3cupboard
                "No":
                    jump IIIX3cupboard
        "Look through the window":
            show bg IIIX3offices
            show joor with dissolve
            $renpy.pause()
            if axe or hammer:
                nt "Should I try to smash the window?"
                menu:
                    "Hell yes":
                        $sanity-=10
                        $cheater=True
                        play sound "glass2.ogg" 
                        scene bg IIIX3offices with vpunch
                        nt "I break the window and jump inside."
                        scene bg IIIX3offices
                        nt "What is... happening..?"
                        if hammer:
                            stop music fadeout 3
                            scene black with dissolve
                            nt "Suddenly, I feel his hands covering my eyes."
                            nt "His fingers feel cold on my skin..."
                            pause 1
                            sh "{b}{i}I can't punish you for thinking outside the box, Hart..."
                            sh "{b}{i}Maybe a little."
                        else:
                            scene bg IIIX3offices
                            nn "Cheater."
                        jump IIIX3offices
                    "Nah":
                        nt "It feels like a bit too much..."
            else:
                nt "Glass prevents me from reaching the room."
                nt "I might stumble upon it later."
            jump IIIX3cupboard
        "Exit the room":
            play sound "doorclose.ogg" fadein 1
            jump IIIXpatients3
label IIIXpatients3:
    scene bg IIIX3patients
    $renpy.pause()
    menu:
        "Enter the first room on the left":
            scene bg IIIX3III ## III, broken matches
            nt "It looks like the room of a patient."
            menu:
                "Look around":
                    nt "I look closely at the room..."
                    nt "It's labellled \"III\". There's definitely a room like that in the real hospital."
                    nt "There's nothing useful here. I only spot a box of broken matches."
                "Leave":
                    nt "Nothing to see here."
            play sound "doorclose.ogg" fadein 1
            jump IIIXpatients3
        "Enter the second room on the left":
            scene bg IIIX3XV
            if not knife:
                show IIIX3knife with dissolve
            nt "It looks like the room of a patient."
            menu:
                "Look around":
                    nt "I look closely at the room..."
                    nt "It's labellled \"XV\". There's definitely a room like that in the real hospital."
                    if knife:
                        nt "I have to wonder if taking that knife was a good idea..."
                        nt "Should I really keep it?"
                        menu:
                            "Drop it":
                                $knife=False
                            "Don't":
                                pass
                    else:
                        nt "There's a knife laying on the floor..."
                        nt "It's... covered in blood."
                        nt "I don't want to touch that thing..."
                        nt "But... maybe I could use it for something."
                        nt "Should I take it?"
                        menu:
                            "Yes":
                                $knife=True
                            "No":
                                pass
                "Leave":
                    nt "Nothing to see here."
            play sound "doorclose.ogg" fadein 1
            jump IIIXpatients3
        "Enter the third room on the left":
            play sound "doorclose.ogg" fadein 1
            jump IIIX3narrow1
        "Enter the first room on the right":
            scene bg IIIX3death ##cheater's path
            nt "...."
            nt "The door is labelled with the word \"DEATH\"."
            nt "Should I... really open it? It doesn't sound all that safe."
            menu:
                "Go in":
                    $sanity-=1
                    $StrengthCard=False
                    scene bg IIIX3scum
                    nt "I... don't think this is the way to go."
                    nt "Whoever write \"SCUM\" on this door probably wouldn't want me going here."
                    menu:
                        "Go further":
                            $sanity-=1
                            $StrengthCard=False
                            scene bg IIIX3monster
                            nt "I'm beginning to suspect someone {i}really{/i} doesn't want me here..."
                            menu:
                                "Open the door":
                                    $sanity-=1
                                    $StrengthCard=False
                                    scene bg IIIX3turnback
                                    nt "Okay, this is a pretty direct message."
                                    nt "Should I really go there..? I'm being given all these chances to leave..."
                                    menu:
                                        "Enter the next room":
                                            $sanity-=1
                                            $StrengthCard=False
                                            scene bg IIIX3axe
                                            $renpy.pause()
                                            menu:
                                                "Check the floor":
                                                    $sanity-=1
                                                    $StrengthCard=False
                                                    nt "There's... an axe?"
                                                    nt "Should I take it?"
                                                    menu:
                                                        "Yes":
                                                            $sanity-=5
                                                            $StrengthCard=False
                                                            $axe=True
                                                            nt "It could be used to smash that window I saw."
                                                            nt "There's a note on the floor, next to the axe."
                                                            nt "I pick it up."
                                                            show moonnote with dissolve
                                                            $renpy.pause()
                                                            hide moonnote with dissolve
                                                            nt "Who wrote this..?"
                                                            nt "...is this really the right thing to do?"
                                                        "No":
                                                            nt "I don't see why I would."
                                                "Leave":
                                                    nt "Let's get out of here."
                                        "Get out":
                                            pass
                                "Leave it":
                                    pass
                        "Get back":
                            pass
                "Leave it be":
                    pass
            play sound "doorclose.ogg" fadein 1
            jump IIIXpatients3
        "Enter the second room on the right":
            scene bg IIIX3XVIII
            if not stick:
                show IIIX3stick with dissolve
            nt "...."
            menu:
                "Look around":
                    nt "This room is labelled as \"XVIII\". I don't think there's a room like that in the hospital..."
                    menu:
                        "Check the rope":
                            nt "...."
                            nt "It... looks like someone was trying to..."
                            nt "Ugh, I don't want to think about it."
                            nt "Looking at this room makes me feel... uneasy."
                        "Check the chair":
                            if needstick:
                                nt "Hang on... I could use the leg of this chair to make a torch."
                                nt "Should I try to break the chair?"
                                menu:
                                    "Yes":
                                        nt "It breaks up surprisingly easily."
                                        nt "I take the newly found stick with me."
                                        $stick=True
                                    "No":
                                        nt "I don't think that would work."
                            else:
                                nt "The chair looks like it's fallen over at some point."
                        "Leave":
                            pass
            play sound "doorclose.ogg" fadein 1
            jump IIIXpatients3
        "Enter the third room on the right":
            show bg IIIX3patientroom
            nt "Nothing to see here."
            play sound "doorclose.ogg" fadein 1
            jump IIIXpatients3
        "Go back":
            play sound "doorclose.ogg" fadein 1
            jump IIIX3cupboard
label IIIX3narrow1:
    scene bg IIIX3narrow
    $renpy.pause()
    jump IIIX3locked
label IIIX3narrow2:
    scene bg IIIX3narrow
    $renpy.pause()
    jump IIIXpatients3
label IIIX3locked:
    scene bg IIIX3locked
    if chair:
        show IIIX3chair with dissolve
    if midnightlockedscare:
        if ventpassed:
            show IIIX3door 1 with dissolve 
        else:
            show IIIX3door 2 with dissolve
        menu:
            "Check the vent":
                if ventpassed:
                    nt "I don't want to go back in there..."
                elif chair:
                    if midnighthangedscare:
                        if screwdriver:
                            nt "Alright, let's open this thing."
                            ##climbing the vent
                            jump IIIX3vent
                        else:
                            nt "I'll need something to open the vent..."
                    else:
                        $midnighthangedscare=True
                        nt "I place the chair by the vent and climb up."
                        scene bg IIIX3ventent:
                            yalign 0.0
                        with dissolve
                        nt "Alright, let's see what I..."
                        show drk with dissolve
                        hide drk with dissolve
                        nt "Huh?"
                        show bg IIIX3ventent:
                            linear 0.2 yalign 1.0
                        pause 0.22
                        scene bg IIIX3locked with vpunch
                        show IIIX3door 2 with dissolve
                        show IIIX3chair with dissolve
                        pause 1
                        nt "What... was that?"
                        nt "...."
                        nt "I'm fine. I think."
                else:
                    nt "I can't reach the vent..."
            "Go further" if ventpassed:
                jump IIIX3darknessent
            "Look behind me":
                jump IIIX3closet
            "Go back to the patients' rooms":
                jump IIIX3narrow2
    else:
        show IIIX3door 1 with dissolve
        $midnightlockedscare=True
        $renpy.pause()
        play sound "doorclose.ogg" fadein 1
        pause 0.1
        show IIIX3door scare
        nt "Did... did the door just close?"
        menu:
            "Check the door":
                nt "Locked. I can't get any further."
        nt "...."
        nt "Unless..."
        nt "I spot a vent in the wall. Maybe I could use it to get to the other side."
        nt "But... it's too high for me to reach, and I'd need to open it somehow."
        nt "Maybe I can look around for something that can help."
    jump IIIX3locked
label IIIX3closet:
    scene bg IIIX3closet
    if not chair:
        show IIIX3chair with dissolve
    nt "It looks like a supply closet. I might find something useful here."
    menu:
        "Search the boxes by the wall":
            nt "...."
            nt "I found... some old-looking newspapers."
            nt "Should I take them?"
            menu:
                "Yes":
                    nt "Who knows, these might come in handy."
                "No":
                    pass
        "Search the shelves":
            nt "...."
            nt "I found a screwdriver. Should I take it?"
            menu:
                "Yes":
                    $screwdriver=True
                "No":
                    pass
        "Search the cupboard":
            nt "...."
            nt "I found... a hammer."
            nt "Should I take it?"
            menu:
                "Yes":
                    $hammer=True
                "No":
                    pass
        "Take the chair" if not chair:
            nt "I think the chair might be useful."
            $chair=True
        "Go back":
            jump IIIX3locked
    jump IIIX3closet
label IIIX3vent:
    stop music fadeout 3
    scene black with dissolve
    nt "I climb into the vent carefully."
    nt "It's dark, but... at least I can fit inside."
    scene bg IIIX3vent1:
        truecenter
        zoom 0.25
    with Dissolve(1.0)
    nt "Just... keep moving forward, [name]..."
    show bg IIIX3vent1:
        ease 0.5 zoom 0.26
    $renpy.pause()
    show bg IIIX3vent1:
        ease 0.5 zoom 0.27
    $renpy.pause()
    show bg IIIX3vent1:
        ease 0.5 zoom 0.3
    $renpy.pause()
    show bg IIIX3vent1:
        ease 0.5 zoom 0.34
    $renpy.pause()
    show bg IIIX3vent1:
        ease 0.5 zoom 0.38
    $renpy.pause()
    show bg IIIX3vent1:
        ease 0.5 zoom 0.45
    $renpy.pause()
    show bg IIIX3vent1:
        ease 0.5 zoom 0.52
    $renpy.pause()
    show bg IIIX3vent1:
        ease 0.5 zoom 0.65
    $renpy.pause()
    show bg IIIX3vent1:
        ease 0.5 zoom 0.8
    $renpy.pause()
    show bg IIIX3vent1:
        ease 0.5 zoom 1.0
    $renpy.pause()
    scene black with dissolve
    scene bg IIIX3vent2:
        truecenter
        zoom 0.25
    with Dissolve(1.0)
    nt "How long is this thing?"
    show bg IIIX3vent2:
        ease 0.5 zoom 0.26
    $renpy.pause()
    show bg IIIX3vent2:
        ease 0.5 zoom 0.28
    $renpy.pause()
    show bg IIIX3vent2:
        ease 0.5 zoom 0.31
    nt "There... must be an exit, right..?"
    show bg IIIX3vent2:
        ease 0.5 zoom 0.35
    $renpy.pause()
    show bg IIIX3vent2:
        ease 0.5 zoom 0.39
    menu:
        "Leave":
            scene black with dissolve
            nt "I can't."
            jump IIIX3locked
        "Keep going":
            pass
    show bg IIIX3vent2:
        ease 0.5 zoom 0.45
    $ventpassed=True
    $renpy.pause()
    show bg IIIX3vent2:
        ease 0.5 zoom 0.52
    $renpy.pause()
    show bg IIIX3vent2:
        ease 0.5 zoom 0.65
    $renpy.pause()
    show bg IIIX3vent2:
        ease 0.5 zoom 0.8
    $renpy.pause()
    show bg IIIX3vent2:
        ease 0.5 zoom 1.0
    $renpy.pause()
    scene black with dissolve
    scene bg IIIX3vent3:
        truecenter
        zoom 0.25
    with Dissolve(1.5)
    nt "Thank god, there {i}is{/i} an exit..."
    show bg IIIX3vent3:
        ease 0.5 zoom 0.26
    $renpy.pause()
    show bg IIIX3vent3:
        ease 0.5 zoom 0.28
    $renpy.pause()
    show bg IIIX3vent3:
        ease 0.5 zoom 0.31
    $renpy.pause()
    show bg IIIX3vent3:
        ease 0.5 zoom 0.35
    $renpy.pause()
    show bg IIIX3vent3:
        ease 0.5 zoom 0.39
    $renpy.pause()
    show bg IIIX3vent3:
        ease 0.5 zoom 0.45
    $renpy.pause()
    show bg IIIX3vent3:
        ease 0.5 zoom 0.52
    $renpy.pause()
    show bg IIIX3vent3:
        ease 0.5 zoom 0.65
    nt "Almost... there..."
    show bg IIIX3vent3:
        ease 0.5 zoom 0.8
    $renpy.pause()
    show bg IIIX3vent3:
        ease 0.5 zoom 1.0
    nt "I gasp once my head is out of the vent."
    scene black with dissolve
    play music "ost/moon.wav" fadein 6
    nt "One more desperate motion later I land on the ground with a thud."
    scene bg IIIX3darknessent
    nt "Finally out of that vent."
    nt "I look around."
    nt "The door behind me was locked from this side. I could go back if I wanted."
    jump IIIX3darknessent
label IIIX3darknessent:
    scene bg IIIX3darknessent
    $renpy.pause()
    menu:
        "Go left":
            show bg IIIX3darknessent2
            if needtorch and not stick:
                nt "I'll need something to light the way..."
                nt "What should I use?"
                menu:
                    "Lighter" if lighter:
                        nt "The lighter won't do on its own..."
                        nt "I'll need something to light on fire."
                    "Axe" if axe:
                        nt "I don't think I can stumble around blindly, swinging at whatever may be out there."
                    "Knife" if knife:
                        nt "Umm... no."
                    "Screwdriver" if screwdriver:
                        nt "I... can't imagine how that could help."
                    "Hammer" if hammer:
                        nt "Not really..?"
                    "Cloth" if cloth:
                        if lighter:
                            nt "Oh, I could definitely try to burn that."
                            nt "But... won't that hurt me?"
                            nt "I think I need something to place the fabric on and then set it on fire."
                            nt "That might last for some time."
                            $needstick=True
                        else:
                            nt "It might be a good idea to set it on fire somehow, but I can't."
                            nt "Maybe there's something I can find..."
            elif stick and cloth:
                stop music fadeout 4
                nt "I wrap the cloth around the end of the stick and grab the lighter."
                play music "fire.ogg" fadein 3
                nt "The torch lights up. It worked!"
                $torch=True
                menu:
                    "Enter the darkness":
                        scene black with dissolve
                        show bg IIIX3darkness
                        show flashlight:
                            truecenter
                            xalign 1.0
                        pause 1
                        show flashlight:
                            ease 1.0 xalign 0.5
                        nt "It looks like the only way to go is forward."
                        $renpy.pause()
                        show bg IIIX3darkness:
                            ease 0.3 yalign 0.1
                            ease 0.5 zoom 1.25
                        show flashlight:
                            ease 0.5 yalign 0.3
                        nt "Nearly there. I'm glad my torch is working so well."
                        $renpy.pause()
                        stop music fadeout 2
                        show drk 2 with dissolve
                        hide drk 2 with dissolve
                        nt "The flame is dying. I should get going."
                        nt "{i}Quickly."
                        play music "ost/moon.wav" fadein 6
                        play sound "doorclose.ogg" fadein 1
                        jump IIIX3offices
                    "Go back":
                        pass
            else:
                $needtorch=True
                $renpy.pause()
                nt "There's a sign pointing towards the hallway."
                nt "It says \"Therapists' offices\"."
                nt "But..."
                nt "It's too dark to see clearly..."
                nt "I'll need something to light the way."
                if lighter:
                    nt "I try to use the lighter I found, but I still can't see what's ahead of me."
                    nt "I'll need something more effective than that."
            jump IIIX3darknessent
        "Go right":
            play sound "doorclose.ogg" fadein 1
            jump IIIX3cloth
        "Go back":
            play sound "doorclose.ogg" fadein 1
            jump IIIX3locked
label IIIX3cloth:
    scene bg IIIX3cloth
    if cloth:
        show IIIX3cloth 2 with dissolve
    else:
        show IIIX3cloth 1 with dissolve
    $renpy.pause()
    menu:
        "Look around":
            nt "Something large is covered in white cloth in the center of the room."
            if cloth:
                nt "I... don't think I want to touch that thing."
            elif needtorch:
                nt "Maybe I could use a piece of that fabric for something..."
            else:
                nt "I don't see why I would need anything from this room."
            jump IIIX3cloth
        "Examine the fabric":
            nt "I approach the cloth slowly."
            nt "I... for some reason, I can't seem to lift it."
            nt "It's heavier than it looks."
            if needtorch and not cloth:
                nt "Should I take a piece of the fabric?"
                menu:
                    "Yes":
                        nt "I... can't seem to rip it off that easily..."
                        nt "I might need to use something."
                        menu:
                            "Use the screwdriver" if screwdriver:
                                nt "I... don't see how that would work."
                                jump IIIX3cloth
                            "Use the bloody knife" if knife:
                                nt "I cut the fabric carefully."
                            "Use the axe" if axe:
                                nt "A bit extreme, but... let's try it."
                            "Use the hammer" if hammer:
                                nt "What?"
                                jump IIIX3cloth
                            "Use the lighter" if lighter:
                                nt "I... don't want to burn this thing..."
                                jump IIIX3cloth
                            "Use the chair's leg" if stick:
                                nt "I can poke it, I guess."
                                jump IIIX3cloth
                        $renpy.pause()
                        show IIIX3cloth 2
                        show IIIX3foot
                        $renpy.pause(0.13, hard=True)
                        hide IIIX3foot with Dissolve(0.1)
                        $cloth=True
                        nt "What... was that?"
                    "No":
                        pass
            jump IIIX3cloth
        "Go back":
            play sound "doorclose.ogg" fadein 1
            jump IIIX3darknessent
label IIIX3offices:
    scene bg IIIX3offices
    nt "This looks like the offices hallway from the hospital."
    menu:
        "Go further":
            show drk with dissolve
            nt "There's a locked door..."
            stop music fadeout 5
            nt "It looks like I need to input some numbers to unlock it."
            $IIIXcode = renpy.input("What should I input?", allow="1234567890", length = 3)
            if IIIXcode=="463":
                nt "I... got it?"
                nt "The door flies open."
                play sound "doorclose.ogg" fadein 1
                scene bg IIIX3central
                $renpy.pause(2,hard=True)
                play music "ost/sscare.ogg"
                show IIIX3centralscare
                $renpy.pause(4,hard=True)
                jump nextday
            else:
                nt "Dammit. I have to try again."
                nt "Maybe I can find clues somewhere around here."
                play music "ost/moon.wav" fadein 6
                jump IIIX3offices
        "Check the left office":
            scene black with dissolve
            show bg IIIX3hier
            pause 1
            nt "That's Dr. Sharpe's office."
            nt "He's William's psychiatrist, right?"
            $renpy.pause()
            play sound "doorclose.ogg" fadein 1
            jump IIIX3offices
        "Check the office in front of me":
            scene bg IIIX3young
            if StarLink>1:
                nt "Isn't that... Dr. Young's office?"
            else:
                nt "Looks like a therapist's office." 
            $renpy.pause()
            play sound "doorclose.ogg" fadein 1
            jump IIIX3offices
        "Check the right office":
            scene bg IIIX3mc
            nt "That's... my office."
            $renpy.pause()
            play sound "doorclose.ogg" fadein 1
            jump IIIX3offices
label fullmoon:
    $moondoorcheck=False
    $axe=False
    $hammer=False
    $glass=False
    $hammercheck=False
    $fullmoonwake=0
    $corpsecheck=0
    stop music fadeout 3
    scene black with Dissolve(1.0)
    pause 2
    nt "I'm... dreaming again?"
    nt "I'm laying on the floor. It's cold."
    play music "ost/moon.wav" fadein 8
    scene bg IIIX3central
    nt "I'm in the central hall..?"
    nt "I get up."
    nt "The door behind me is locked. It must be the one I came through in my last dream."
    scene black with dissolve
    nt "Seeing no other way to proceed, I open the door in front of me."
    play sound "doorclose.ogg" fadein 1
label fullmoon1:
    scene fullmoon1
    $renpy.pause()
    if moondoorcheck and axe:
        stop music fadeout 6
        mot "[name]! Hurry!"
        nt "I run to the door, axe in hand."
        nm "Get away from the door, I'm going to destroy it!"
        nt "No reply. I assume he's safe."
        nt "I swing at the door as hard as I can."
        show fullmoon12 with vpunch
        nt "Damn. I'll need to hit it again."
        show fullmoon13 with vpunch
        nt "...and again."
        show fullmoon14 with vpunch
        nt "Great. Now I can finally free him."
        show fullmoonend 1
        play music "ost/shadowB.ogg" fadein 10
        nt "I enter the dark hallway."
        nt "I can't see him anywhere."
        nm "William..? Where are you?"
        show shfull 3 with dissolve
        mot "[name]... you're here..."
        mot "You're really..."
        play sound "doorclose.ogg" fadein 1
        pause 0.2
        show fullmoonend 2 with dissolve
        nn "{i}You really are that stupid."
        nm "What..?"
        show shfull 2 with dissolve
        nn "You really had no idea what you were doing?"
        nn "Pathetic... so easily fooled."
        nt "This isn't William anymore..."
        nt "I take a step back only to realize there's no door behind me anymore."
        nt "I'm trapped."
        nn "So you finally understand, don't you?"
        $quick_menu=False
        $_game_menu_screen = None
        show shfull 1 with dissolve
        sn "Hello, [name]."
        nm "Where is William? What did you do to him?"
        sn "Me? I didn't do anything."
        sn "Always so quick to blame me for your own mistakes... You did all the work for me."
        sn "In fact, I should be thanking you - if you hadn't hanged him back there, I could be in trouble right now."
        sn "But you left him too quickly to even consider that."
        sn "He's gone now. At least until he wakes up."
        sn "And that means..."
        show shfull 4 with dissolve
        sn "We're alone now, [name]. And there's nobody left to protect you."
        nt "For some reason I can't move away from him. I'm literally frozen in place."
        sn "Don't even bother to run - you can't."
        sn "I created this dream."
        sn "You can only move if I allow it, [name]."
        nt "I try to tell myself it can't be that bad, that it's just a nightmare... But does that really change anything?"
        nt "His glare is as cold as ice."
        sn "You're just starting to realize what you've gotten yourself into, aren't you?"
        sn "Yes, if you never pushed him to let you meet me, this would not have happened."
        sn "And yet here we are. All because you let him believe you \"care\"."
        nm "I do!"
        sn "These are just words... shallow promises."
        sn "I wonder how you'll feel about him..."
        show shfull 5 with dissolve
        sn "Once I'm done with you."
        nt "I can only see his eyes glowing in the darkness when he moves even closer to me."
        sn "[name]... Tell me..."
        sn "Can you still care after this?"
        nt "I feel his breath on my skin, taunting me."
        sn "Or will you see how pointless it really is to care about someone like him?"
        sn "Will you ever be able to look at him without seeing me?"
        sn "Or are you still seeing him right now?"
        nt "He grabs my chin and forces me to look up into his eyes."
        sn "Who are you seeing, [name]? Who am I?"
        menu:
            "You are him":
                sn "We are one."
                sn "And he is looking at you right now."
            "You are not him":
                nm "He could never -"
                nt "My voice is cut off."
                sn "Keep lying to yourself, [name]."
                sn "I am both."
            "Stay silent":
                sn "So you don't know?"
                sn "Or do you just think I'm not worth talking to?"
                sn "I can make you talk, [name]. There is no rush."
        sn "Either way, he's here as well."
        sn "He's seeing everything I do to you. And there's nothing he can do to stop me."
        sn "You're both helpless. The only difference is that he's not even trying."
        nm "What do you mean..?"
        sn "Did you already forget? I'm just a part of him."
        sn "Everything I do has to come from him, one way or another."
        sn "He can't lie to himself enough to think he doesn't want this as well."
        sn "Though consciously, he would only enjoy this the other way around."
        nm "{i}!!!"
        sn "You couldn't guess that?"
        sn "If you tried to do the same to him, he wouldn't even try to stop you."
        nm "That... can't be true... You're lying!"
        sn "Am I..? Believe what you want, [name]. I have no reason to lie to you."
        sn "Just like I'm not lying when I say he and I both will enjoy this." 
        show fullmoonend 3  
        show drk with dissolve
        hide shfull with dissolve
        nt "He closes what remained of the gap between us suddenly and kisses me."
        nm "{i}!!!"
        nt "{i}I can't move."    
        nt "It's... forceful, demanding. I'm not left any space to fight back."
        nt "I feel his hands on my shoulders, pressing me harder onto the wall behind me."
        nt "His hands trail down my arms slowly."
        nt "I have no idea what he's about to do and it terrifies me."
        nt "His fingertips brush against mine briefly, but it disappears as quickly as it came."
        show shfull 4 with hpunch
        nt "!!!"
        nt "He slips his hand under my shirt."
        nt "I can feel the other one on my hip, forcing me to remain in place."
        nt "His thin fingers slide over my spine before stopping abruptly."
        nt "He unhooks my bra before I can realize what's going on."
        show shfull 1 with dissolve
        nt "Slowly, he pulls away."
        sn "What's with that face? Are you scared already?"
        nt "He's not letting me speak."
        sn "I wouldn't be so quick about it..."
        sn "After all, you will only wake up once I allow it, so there's no rush."
        sn "Or are you just feeling a bit shy..?"
        nt "He touches the small of my back, this time over my shirt."
        nt "He's taunting me. Of course he'll take his time."
        sn "It's not time to undress you. Not just yet."
        nt "His hand on my back drops down suddenly."
        sn "I've only just begun to have fun."
        nt "He places his hands on my hips firmly."
        sn "I wonder how he's going to feel..."
        show shfull 5 with dissolve
        nt "He pulls me closer forcefully."
        nt "I'm... I can't be any closer to him. I can feel his heartbeat on my chest."
        sn "When I do this..?"
        nt "He falls silent."
        nt "He really looks like William... if it weren't for the eyes, they would really be the same."
        nt "His hair feels so soft... {i}William..."
        nt "If only it were really you instead of this monster..."
        nt "I want him back. I really do. I feel like crying, but I can't."
        nt "I think back to every time he didn't allow me to get closer to him when I knew it would comfort him."
        nt "Now that I'm so close I feel... This feels wrong."
        nt "He's different. Anytime I touched him or got close to him when he was normal, he would be trembling."
        nt "And now he's perfectly calm. And that scares me the most."
        sn "Oh?"
        show shfull 4 with dissolve
        nt "He pulls back slightly to look me in the eye."
        sn "You're really... thinking about him right now?"
        sn "Even like this?"
        nm "You..."
        sn "I see your thoughts. Pieces of them, at least."
        sn "You are in my dream, after all."
        nm "...."
        sn "And..."
        show shfull 5 with dissolve
        nt "He pulls me closer again."
        sn "As I said..."
        sn "This is still his body. Completely. In every detail."
        nt "He moves his hand over the back of my neck slowly."
        sn "I owe him for that - I don't have a body of my own."
        nt "I swallow."
        nt "Everything I'm seeing and feeling right now... It's real. It's him."
        show shfull 1 with dissolve
        sn "Let's see, [name] - let's see how you really feel."
        nt "He... frees me?"
        nt "I can move my hands, but I'm still frozen in place. I can't run."
        sn "Go on. You're \"free\"."
        nt "He's mocking me, but... what should I do?"
        menu:
            "Nothing":
                nt "I don't do anything. It's pointless."
                sn "So... composed. I'm impressed, I admit."
            "Fight back":
                nt "I punch him in the face."
                nt "Even if I can't run away, I can still struggle."
                show shwill with dissolve
                hide shwill with dissolve
                nt "He smiles from ear to ear."
                sn "Are you trying to make me laugh?"
                nt "He tilts his head back like he did when I pushed him back in my office."
                sn "He's begging me to get you to do it again."
                nt "I freeze. I don't want to hurt him... I just wanted to show I can fight back."
                sn "Are you stupid or do you actually want to bring him back that desperately?"
                sn "Honestly..."
                nt "He grabs my wrists suddenly and pulls me closer."
                sn "It would take a lot more than that."
                sn "You would really need to make me suffer to draw him out."
                nt "I don't like the way he smiles at me."
                sn "You're welcome to try, of course."
            "Hug him":
                $SilverHeart+=2
                show shfull 5 with dissolve
                nt "Desperate, I wrap my arms around him."
                nm "William..."
                nt "I want to believe he's in there, somewhere... That I haven't lost him yet."
                sn "...."
                sn "So that's what you want? You really don't care about what I'm about to do..?"
                sn "You just want him."
                sn "Desperately enough to hug someone who's about to do something horrible to you, just because they look like him..."
                sn "...."
                sn "I can hear him now. He hasn't been this desperate in a while."
                nm "He wouldn't hurt me."
                sn "Maybe. But so far he hasn't done anything to stop me."
                nt "He removes his hands from my shoulders."
        show shfull 4 with dissolve
        nt "I can't move anymore."
        sn "[name], [name], [name]... You really are strange."
        sn "Now, if you don't mind..."
        nt "He touches me again."
        sn "I have things to do here."
        nt "His hands reach lower on my back again. My whole body is screaming for me to get away from him right now."
        nt "He's too close for me to handle."
        sn "Let's see..."
        nt "He pauses briefly over the edge of my shirt before stopping further down on my pants."
        nm "{i}!!!"
        sn "...."
        nt "I can't name the sound he just made."
        sn "I thought I should at least take the time to see everything you have to offer."
        nt "I can feel the tip of his tongue on my ear when he whispers:"
        sn "After all, I'll be preoccupied with other places later."
        nt "He tightens his grip on my butt."
        sn "On that note..."
        nt "He moves one of his hands down, between my legs, barely brushing against me."
        nm "{i}Khh-!"
        nt "He's too quick for me to muffle everything in time."
        scene black
        nt "I shut my eyes as tightly as I can, trying not to look at him."
        nt "I'm stronger than this. I am."
        sn "Are you..?"
        show fullmoonend 3 with Dissolve(1.0)
        show shfull 4 with dissolve
        nt "My eyes snap open."
        sn "You're already breaking, [name]."
        nt "His hand caresses the inside of my thigh slowly."
        nt "I feel like my knees are giving up, despite my attempts to stand."
        show shfull 5 with dissolve
        nt "He places his other hand on my back, keeping me close."
        sn "It won't be long now, [name]... I know you're getting impatient."
        nt "I really can't move away. I keep trying to struggle, but it's pointless."
        nt "I... I can't feel this way! Why can I not make it stop?!"
        sn "I can make it stop. But only once you give up."
        nt "He moves his hand to my face slowly."
        sn "It won't hurt if you do."
        nt "I don't move a muscle."
        sn "I wonder..."
        sn "If it was him instead of me, would you still struggle..?"
        nm "He would never -!"
        sn "I wouldn't be so sure of that... He's the one who wants this."
        sn "Don't forget, [name] - I am him and he is me."
        show shfull 4 with dissolve
        stop music fadeout 5
        nt "He looks at me with a smile that sends shivers down my spine."
        sn "I've already stolen the first kiss from him..."
        sn "I want to steal some more."
        scene black with vpunch
        play music "ost/shadowA.ogg" fadein 3
        nm "!!!"
        nt "I hit the floor with a thud."
        show fm 1a:
            zoom 0.55
            truecenter
        sn "Let's see you beg me to stop."
        nt "He rips my sweater off. He's not wasting any time."
        show fm 2a
        sn "[name]..."
        nt "His hands are on my shoulders before he moves down."
        nt "His eyes follow the hands when he trails my sides with his fingers, my hips, my thighs..."
        nt "He's everywhere. Claiming everything he touches as his own."
        nt "He doesn't want to leave any part of me unscarred after this."
        nt "His hands make their way back up slowly until he reaches my shirt and looks at me with a sinister spark in his eye."
        sn "You know it's coming, [name]."
        nt "He finds my bra under my shirt and slowly pulls it down to him, only to toss it on the floor."
        nt "I take a deep breath, waiting for whatever he's about to do now."
        nt "He grabs the edge of my shirt suddenly and starts pulling it up, bit by bit."
        show fm 2b
        nm "{i}!!!"
        scene black
        nt "I can't take it. I shut my eyes as tightly as possible and wait."
        sn "[name]..? You really are shy, aren't you..?"
        nt "His hand on my neck urges me to open my eyes again."
        show fm 2b:
            zoom 0.55
            truecenter
        nt "Before I can react, he crushes my throat with his hand, pressing me down onto the floor."
        sn "You don't really have a choice..."
        nt "I'm running out of air."
        sn "You know I'm going to do it anyway."
        sn "And it's going to be painful."
        nt "He tightens his grip on my neck. My eyes water from the pain, but I can barely see it."
        sn "This is nothing, [name]."
        nt "He lets go of me and I gasp for air."
        show fm 2a
        nt "I can't make out what he's doing when he comes closer to me, lower, and his hands find my breasts through the fabric of my shirt."
        nt "I barely feel the pain at first when he bites into my neck."
        nt "There's nothing I can do to make it stop. I... feel like I'm about to faint..."
        nm "William... don't..."
        nt "He pulls away."
        sn "My name is not William. And i have no reason to obey you."
        show fm 2b
        nm "Agh -!"
        nt "My eyes snap open when he slaps me in the face so hard it hits the floor."
        sn "Yes... I am definitely starting to enjoy this."
        show fm 2a
        nt "It takes me a few second to recover and look at him."
        nm "Just... get it over with..."
        sn "It won't be over in a while, [name]. If I could, I would keep you here until you'd lose your mind."
        sn "But I'll settle for a little more... just enough for him to lose all will to live."
        sn "Everything you've worked so hard on these past three weeks..."
        sn "...gone. Crushed."
        sn "By me."
        sn "Just like you're about to be."
        nt "He presses his body to mine again."
        nt "Except this time, I..."
        nt "I can feel him. He..."
        nt "...Oh God."
        show fm 2b
        sn "Are you scared now? It's almost time."
        nt "He moves on top of me slightly."
        nt "I feel it again."
        nt "{i}Calm down, calm down..."
        nt "His hand moves slowly between my legs, this time more boldly."
        show fm 2a
        sn "...."
        sn "You're warm already..."
        nt "He presses his fingers further against the fabric of my pants."
        sn "That's a shame. It would hurt more if you weren't so eager."
        nt "I... I couldn't stop it."
        nt "Not even because of what he's about to do, but because..."
        nt "...he still looks just like him."
        sn "Show me..."
        nt "He leans down until his face is an inch away from mine."
        sn "{i}...Everything."
        nt "His hands find the edge of my pants and pull them all the way down quickly."
        nt "He sits up over me and touches the hem of my panties slowly."
        sn "You have no idea for how long he's longed to see a woman like this."
        sn "Helpless. Afraid."
        sn "Of me. And only me."
        nt "He pulls lightly, letting them slide down ever so slightly."
        sn "It's what he's always wanted. For others to be as helpless as he is."
        nt "He pulls my underwear off impatiently and slides it off my legs."
        nt "This... this is it. I can't prepare myself for what is about to happen in any way."
        nt "He opens my legs forcefully."
        nt "They're trembling. I'm scared."
        nt "I don't want this... {i}I DON'T WANT ANY OF THIS."
        nt "He looks into my eyes, this time wet from tears."
        sn "Isn't it beautiful, [name]? How I can destroy two lives with one act of cruelty?"
        nt "With the last of my strength, I manage to reply."
        nm "You... you can't destroy me."
        sn "He will."
        sn "And then he'll kill himself out of guilt."
        nm "...."
        nt "Is this... really how things have to end?"
        sn "I won't stop you from talking anymore."
        nt "He bends down over me again."
        sn "I want. To hear. {i}Everything."
        show fm 4b with hpunch
        nt "Before I realize what's happening, he forces himself all the way in."
        nt "I can't look away... I can't move..."
        nt "He crushes me."
        nt "It hurts... it hurts so much..."
        nt "And it never stops."
        nt "I lose consciousness after three times."
        stop music fadeout 3
        $renpy.pause(3,hard=True)
        $quick_menu=True
        $_game_menu_screen = "save"
        jump afterfullmoon
    menu:
        "Left door":
            nt "The door is locked. It won't budge."
            if moondoorcheck:
                nt "I have to get him out of there."
            else:
                $moondoorcheck=True
                nt "I... suppose there must be somewhere else for me to go."
                play sound "knock2.ogg"
                nt "{i}!?"
                mot "{i}Is anyone there? Please, I need help!"
                nt "I freeze. I know that voice."
                nm "William..? Is that you?"
                mot "{i}[name]... I can't believe you're here."
                nm "How did you get there? And why is the door locked?"
                mot "{i}I don't know, I just woke up here... And I can't get out."
                mot "{i}Please, you have to help me. Find something to smash the lock and we can both leave this place for good."
                nm "I'll see what I can find. Just hang in there."
                mot "{i}You have to hurry, [name]. And don't let him deceive you."
                nm "What do you mean?"
                mot "{i}No matter what he put in your path, you have to remember to come back here."
                mot "{i}Do you understand?"
                menu:
                    "Yes":
                        pass
                    "No":
                        $StrengthCard=False
                        $sanity-=10
                mot "{i}Just... come back here soon."
                mot "{i}I don't... know how much longer I can last here."
                nm "I'll be back, I promise."
                nt "I can feel my hands shaking when I step away from the door."
                nt "I tried to keep my voice steady, but this place terrifies me."
                nt "Why would the shadow do this to us? To prove some sick point?"
                nt "This is the first time he let me and William interact in a dream."
                nt "What's going on here..?"
                nt "He told me not let the shadow deceive me... How hard can it be to remember what my goal is?"
                nt "I should hurry into the room to my right."
            jump fullmoon1
        "Right door":
            play sound "doorclose.ogg" fadein 1
            jump fullmoon2
label fullmoon2:
    if axe:
        scene fullmoon24
    elif corpsecheck>4:
        scene fullmoon22
    else:
        scene fullmoon2
    $renpy.pause()
    menu:
        "Check mirror":
            if axe:
                nt "I don't need to look at it."
            elif corpsecheck==4:
                nt "Should I... try it?"
                menu:
                    "Break the mirror":
                        $corpsecheck=5
                        play sound "glass.ogg" fadein 1
                        scene fullmoon22 with vpunch
                        nt "I hit the mirror with my hands as hard as I can."
                        nt "The glass breaks enough for me to see one loose shard."
                        nt "I pick it up carefully, but end up cutting myself anyway. That thing is sharp."
                        nt "Wait... What is that?"
                        nt "There's something behind the mirror. I can't quite see is yet, but..."
                        nt "Maybe I should check it out."
                    "Don't":
                        pass
            elif hammer:
                nt "Should I try to smash the mirror with the hammer I... {i}found{/i}?"
                menu:
                    "Yes":
                        play sound "glass2.ogg" fadein 1
                        scene fullmoon23 with vpunch
                        pause 1
                        nt "Is that... a lever? What does it do?"
                        menu:
                            "Pull it":
                                pass
                            "Don't":
                                $sanity-=5
                                $StrengthCard=False
                                nt "I better not."
                                nt "...what? Of course I'll pull it."
                        $axe=True
                        scene fullmoon24
                        nm "{i}?!"
                        nt "What... was that noise?"
                        play sound "doorclose.ogg" fadein 1
                        scene black with dissolve
                        nt "I hurry to the room to my left."
                        show fullmoonleft2
                        $renpy.pause()
                        nm "Oh god... {i}William..."
                        nt "I... I can't bear to look at this, even if it's not real."
                        nt "{i}I did this."
                        nt "The thought itself makes me feel sick."
                        menu:
                            "Take the axe and leave":
                                nt "{i}At...{/i} at least I can take the axe now."
                        scene black with Dissolve(1.0)
                        nt "I bore my eyes into the floor before leaving the room in a hurry."
                        if moondoorcheck:
                            nt "{i}This isn't real, this isn't real."
                    "No":
                        pass
            else:
                nt "...."
                nt "It's me."
                nt "Why a mirror, of all things, in a place like this?"
            jump fullmoon2
        "Go left":
            if axe:
                nt "{size=26}No."
                jump fullmoon2
            play sound "doorclose.ogg" fadein 1
            jump fullmoonleft
        "Go right":
            play sound "doorclose.ogg" fadein 1
            jump fullmoonright
        "Go back":
            play sound "doorclose.ogg" fadein 1
            jump fullmoon1
label fullmoonleft:
    scene fullmoonleft
    $renpy.pause()
    menu:
        "Look around":
            nt "What... is this?"
            nt "I run up to him and kneel down on the floor."
            nm "William?"
            nt "He's... alive, but seems unconscious. Like he's been knocked out."
            nt "Who did this to him? And why?"
            nt "I struggle to free him at least, but the rope doesn't move an inch."
            if moondoorcheck:
                nt "I... don't know what to do."
                nt "William told me the shadow might try to sway me away from my task."
                nt "I have to focus and keep going, no matter what he shows me."
                nt "It's not real."
                menu:
                    "Leave the room":
                        pass
                    "Try to wake him again":
                        if fullmoonwake==6:
                            $sanity+=20
                            stop music fadeout 1
                            play sound "glass2.ogg"
                            scene black with Dissolve(0.3)
                            nt "Why... why is it so dark?"
                            wt "{i}!!!"
                            wt "{i}[name]..?"
                            nm "William? Is that really you?"
                            wt "[name]... is this another dream?"
                            nm "It is. I just woke up here, I didn't know what to do, I -"
                            nm "Are you hurt?"
                            wt "If this is a dream, I wouldn't be worried about that. I'm fine."
                            nt "For some reason, he's not tied up anymore. Maybe it's because I woke him up."
                            wt "...."
                            wt "You haven't... seen him in your previous dream, right?"
                            nt "The initial shock of him knowing about that nightmare passes more quickly than one would expect."
                            nm "At the end. He just... stood there."
                            wt "And in this one?"
                            nm "No."
                            wt "That's a relief. I felt like he might try something..."
                            nm "...wait."
                            play music "ost/shadow.ogg" fadein 6
                            nm "I saw... you. At the beginning of this dream."
                            wt "[name]. Are you sure?"
                            nt "He sounds concerned."
                            wt "That wasn't me, [name]. He's trying to trick you."
                            nm "What?"
                            wt "What did he tell you to do?"
                            nm "He was stuck behind a locked door... he told me to break it and help him."
                            nm "...no matter what the shadow might put in my path."
                            wt "Which was me? He would've had you make sure I couldn't interfere."
                            nm "Oh god... I'm so sorry. I don't know why I believed him."
                            wt "It's fine, [name]. He's good at this."
                            nm "How do we get out of here?"
                            wt "Well... he's going to try to seperate us."
                            wt "Or convince you he's the real one."
                            nt "He stands up and I suddenly realize we were sitting on the floor."
                            wt "Come on. If he wants us to get somewhere, it's best to hurry."
                            nt "Still unable to see anything, I follow the sound of his footsteps."
                            scene fullmoonend2 with Dissolve(1.0)
                            nt "He looks at me once we enter the dimly lit corridor."
                            wt "Are you okay?"
                            nt "I nod."
                            nm "Let's get out of here."
                            show shfull 2 with dissolve
                            nn "{b}{i}And where do you think you're going?"
                            nt "Everything stops for a second before we see him walk in."
                            nt "He looks... different. Like something out of a nightmare."
                            nt "William steps forward to face him. I freeze."
                            wt "What do you want?"
                            sn "{b}{i}The same as I've always wanted. For you to look me in the eye and tell me we are one and the same."
                            wt "No."
                            nt "Suddenly, he turns to me."
                            sn "{b}{i}Hello, [name]."
                            show moonshadowfused with Dissolve(1.0)
                            nt "He pushes William out of the way and walks up to me."
                            nm "{i}Get-"
                            nt "I can't move. I can't scream."
                            wt "What did you do to her?"
                            sn "{b}{i}How about you stop attacking me and hear me out?"
                            wt "...."
                            nt "The shadow grabs me by the shoulder and looks at William."
                            sn "{b}{i}Now that I have your full attention, here's what I want:"
                            sn "{b}{i}I want you to choose."
                            sn "{b}{i}Either you let go of her and I show her everything you've been hiding from her."
                            sn "{b}{i}That way, no harm will come to you and you will wake up very soon."
                            sn "{b}{i}Or... if you really care that much about what she thinks, I can settle for you."
                            sn "{b}{i}I won't harm her, but... I can't promise you won't."
                            wt "What are you going to do to me?"
                            show shfull 1 with dissolve
                            hide moonshadowfused with dissolve
                            nt "He lets go of me and walks up to his other self with a smile."
                            sn "{b}{i}What do you think I want to do..?"
                            nt "All the color fades from William's face in an instant."
                            sn "{b}{i}I want us to be united. All this fighting is making us both weak."
                            wt "I'd rather be weak than become something like you."
                            sn "{b}{i}So you'd rather hand her to me than have a fair fight?"
                            wt "What?"
                            sn "{b}{i}I never said I wanted us to be equal. I just want one of us in control."
                            wt "You want to fight for dominance."
                            sn "{b}{i}Of course I do."
                            wt "Either I let you do that, or you take [name]?"
                            sn "{b}{i}It's your choice."
                            sn "{b}{i}Of course, with enough willpower, you could just stop me and wake up, but we both know you can't."
                            nt "The shadow places his hand on William's cheek. He freezes."
                            sn "{b}{i}You never had the strength to control me. You were always supposed to lose to me."
                            nt "He steps away from William and glances at me again."
                            sn "{b}{i}I like to think of myself as patient, but this is really taking a long time."
                            sn "{b}{i}What will it be?"
                            wt "...."
                            nt "He looks the shadow straight in the eye with a certainty I've never seen before."
                            wt "I will fight you until one of us no longer exists."
                            sn "{b}{i}That's surprisingly brave, coming from someone like you."
                            sn "{b}{i}Unfortunatey, I can't make the same promise."
                            nt "He walks up to him again and grabs his wrist, pulling him closer."
                            sn "{b}{i}You see, I think I'll enjoy locking you up at the back of my mind too much to let you die."
                            sn "{b}{i}Reducing you to less than a fleeting thought. No, killing you would only be an act of mercy."
                            nt "He looks at me briefly."
                            sn "{b}{i}Goodbye, [name]. You won't see one of us again."
                            nt "Before I can do anything to stop him, he disappears in the darkness behind him, taking William with him."
                            nt "...."
                            nt "Oh god... what just happened?"
                            scene black with dissolve
                            nt "Everything disappears. Is the dream over?"
                            $moonshadowfused=True
                            $renpy.pause(2,hard=True)
                            jump nextday
                        else:
                            $sanity-=2
                            $StrengthCard=False
                            $fullmoonwake+=1
                            nt "He's knocked out. There's nothing I can do."
            else:
                nt "It feels wrong to leave him like this, but..."
                nt "Maybe I should look for a way out, and come back here."
                nt "There might be something I can use behind the door I haven't checked yet."
            jump fullmoonleft
        "Leave":
            pass
    jump fullmoon2
label fullmoonright:
    scene fullmoonright
    $renpy.pause()
    menu:
        "Look around" if corpsecheck<1:
            nt "The room is dark, but I can definitely make out one object on the floor."
            nt "It's... a dead body."
            $corpsecheck=1
            jump fullmoonright
        "Examine the corpse" if corpsecheck>0 and moondoorcheck:
            if hammer:
                nt "I don't want to look at that mess."
            elif corpsecheck>4:
                nt "Should I use the glass shard I found to cut the throat open?"
                menu:
                    "Yes":
                        $hammer=True
                        nt "I... I don't know if this will work..."
                        nt "But the prospect of making William wait any longer than necessary isn't pleasant either."
                        nt "I have to do this."
                        nt "Kneeling down slowly on the floor, I push the glass shard into the burnt skin."
                        nt "Ugh... it feels wrong."
                        nt "...."
                        nt "I found... a hammer?"
                        nt "It {i}is{/i} a hammer. It's just very... dirty."
                        nt "I'd rather not touch the glass shard again."
                    "Bad idea":
                        nt "I thought so."
            elif corpsecheck>3:
                nt "Whatever is inside, I'm not getting it like this."
            elif corpsecheck>2:
                nt "No... I don't... want to..."
                nt "I... I feel sick."
                menu:
                    "Reach down the corpse's throat":
                        $corpsecheck=4
                        nt "Oh god... why?"
                        scene black with dissolve
                        nt "I force myself to push two fingers into its mouth."
                        nt "It sounds like I'm about to tear it apart."
                        nt "!!!"
                        nt "{i}There's something inside."
                        nt "Something... cold and... metal?"
                        nt "I push as far as I can, but can't grab it."
                        nt "If I really need this thing, there has to be another way."
                    "Hell no":
                        nt "No. I can't do this."
            elif corpsecheck>1:
                $corpsecheck=3
                nt "Do I... really have to look at it again..?"
                nt "This whole place makes me feel on edge, and that... {i}person{/i} isn't helping."
                nt "Wait... there's something wrong... with their throat."
            else:
                $corpsecheck=2
                nt "I force myself to look at the charred corpse on the floor."
                nt "It looks... very much dead. I can't tell what age or gender they were."
                nt "Something looks... odd about it. I can't tell what it is."
            jump fullmoonright
        "Leave":
            jump fullmoon2

###################### HERMIT ############################################
label darkforest:
    scene black with Dissolve(2.0)
    play music "ost/hylo.wav" fadein 4
    $renpy.pause(3, hard=True)
    nt "...Darkness."
    nt "Huh..? Where am I?"
    scene bg patientsnight
    nt "Oh. It's the patients' rooms hallway. But... it's so dark..."
    nm "Hello? Is anyone there?"
    nt "...."
    nt "Nothing. My voice echoes in the hallway."
    nt "Suddenly, I notice something isn't quite right."
    show patientshermit
    nt "I approach the door. What is that..?"
    nt "Touching the dark object emerging from the glass, I realize it must be the branch of a tree."
    nt "Maybe I can get this door open..."
    nt "Surprisingly, it opens without any trouble. Now I can enter."
    menu:
        "Enter the room":
            scene hermitforest1
            nt "Huh. It's a forest, but there's something unsettling about it."
    nt "I can't see a way out, or anything that looks different than anything else."
    nt "I... don't know where to go."
    stop music fadeout 6
    nt "I'm not sure if I can even go anywhere."
    nt "Wait... I can hear some voices..."
    scene black with dissolve 
    play music "ost/memory.wav" fadein 6
    nt "Finally, I manage to barge into the room."
    nt "...more like we. I wouldn't be capable of that on my own."
    nt "But there he is."
    show hdream1
    $actualname=name
    $name="Me"
    m "Why won't you answer us?"
    m "We haven't seen you in three days, haven't talked to you in at least a week..."
    m "We were so worried about you... why won't you talk to us now?"
    "...."
    mn "This is getting ridiculous, what the hell is going on?!"
    m "Calm down, darling, yelling at him won't solve anything."
    mn "Then what will? I'm done with this, if you want to keep trying to be nice, go ahead."
    play sound "doorclose.ogg" fadein 1
    show drk with dissolve
    "He leaves the room. I'm... on my own."
    "I don't know what to do."
    "{i}I don't know what to do!"
    $name=actualname
    scene black with Dissolve(1.0)
    jump nextday 
   
label alicehylophobia:
    scene black with Dissolve(2.0)
    play music "ost/hylodis.wav" fadein 4
    $renpy.pause(3, hard=True)
    nn "{i}Poor, poor [name]..."
    nn "{i}She wants answers so desperately, but only finds more questions..."
    nt "I don't know this voice."
    nn "{i}[name], don't be afraid... {/i}I know you."
    scene hermitforest2
    pause 1
    nt "I'm back in that forest... why am I here?"
    nt "And... why can I not see anything..?"
    nt "The voice is gone. There's nothing left to do but move forward."
    nt "...."
    nt "But... where is that?"
    show a help
    menu:
        "Go left":
            show devilforest
        "Go right":
            show moonforest
        "Go straight ahead":
            show hangedforest
    show a hermitforest3
    pause 1
    nt "What... is this place?"
    nt "How do I get out of here?"
    nt "{i}I have to leave."
    nt "I have to live."
    nn "{i}[name], [name]... why the rush..?"
    nt "I hear footsteps on the grass."
    show a hermitforest3 with hpunch
    nt "Where..? Where is she?"
    nt "I turn around, but I can't see her anywhere."
    nn "{i}You really want to leave so soon..?"
    nn "{i}I thought you wanted answers..."
    nn "{i}You want knowledge? You'll find all you need if you follow me. {/i}Deeper."
    menu:
        "Go deeper":
            scene hermitforest4
            pause 1
            nt "I follow the girl into the depths."
    nt "I don't know why, but I need to know what she has to tell me."
    nt "{i}I need her."
    nn "{i}That's right. You need me."
    nn "{i}If it weren't for me, you would never find your way to this place."
    nt "Suddenly, the voice sounds like it's coming from far away."
    nn "{i}You're almost there. So close to getting your answers."
    nt "I hurry into the darkness, following her voice."
    scene black with dissolve
    nm "Where are you?"
    nn "{i}Do you trust me, [name]?"
    nm "I do."
    nn "{i}Reach out. I will answer."
    scene hermithand with Dissolve(1.0)
    nn "{i}Now. Do you want all the answers?"
    menu:
        "Yes":
            nn "{i}Good."
        "Who are you?":
            $sanity-=10
            $StrengthCard=False
            nn "{i}Does it matter?"
    nn "{i}I \ can help you find all your answers. But you need to be patient and trust me."
    nn "{i}Do you trust me, [name]?"
    nm "I do!"
    nn "{i}Then... do you want my help?"
    menu:
        "Yes":
            nn "{i}It's the right choice, [name]."
            show hermithands with Dissolve(1.0)
            nt "!!!"
            nt "{i}{size=26}It's her."
            nn "{i}Don't be afraid, [name] - it'll be done soon."
            nn "{i}With my help, you can have anything you want."
            scene black with Dissolve(3.0)
        "No":
            $HermitApathyEnd=True
            $sanity-=20
            $StrengthCard=False
            scene black
            stop music
            nn "{i}Then you are doomed."
    $renpy.pause(1,hard=True)
    jump nextday

label backintheforest:
    $day-=1
    $Hermitloop+=1
    $actualname=name
    $name="Me"
    scene black with Dissolve(2.0)
    pause 1
    nn "Wake up."
    nt "...."
    nn "Wake up. Open your eyes."
    nt "A voice... in the darkness. A whisper."
    nt "{i}She's gone."
    nt "I open my eyes."
    show bg charlie with Dissolve(1.0)
    play sound "knock.ogg"
    pause 1
    nn "Follow me. There are things for you to see."
    nt "I turn to look at the door, but she's already left."
    nt "I need to follow her."
    menu:
        "Leave the room":
            play sound "footsteps.ogg"
            show bg patients with dissolve
            nm "Where are you?"
    show drk with dissolve
    hide drk with dissolve
    nm "I... I don't know where to go."
    show drk with dissolve
    show hermitalice with Dissolve(0.1)
    hide drk with dissolve
    $renpy.pause()
    nt "I need to follow her."
    menu:
        "Follow her":
            pass
        "Follow her":
            pass
        "Follow her":
            pass
    scene bg central with dissolve
    nt "Where is she..?"
    nt "I can't... I can't see her anywhere."
    nt "I draw a breath to call her, but realize I don't know her name."
    show centralhermit with Dissolve(1.0)
    play music "ost/hermittense.ogg"
    nt "The... the forest. {i}I'm in the forest again."
    nt "I back up as far as I can before my back hits the wall."
    nt "{i}i don't want to see this"
    nt "She... she led me here, and..."
    show bg with vpunch
    nt "And where is she now?!"
    nt "There's nothing... nowhere to go."
    nt "I... think I'm crying."
    nt "I scream as loud as I can, but nobody hears me."
    nt "Nobody can hear. I'm all alone."
    nt "{i}She left me here."
    stop music fadeout 4
    nn "I'm right here ~"
    hide centralhermit with Dissolve(1.0)
    nt "What..?"
    show bg with hpunch
    nt "No, she- she's right?"
    nn "Come with me. I know the way."
    nt "This isn't the forest. And she's showing me the way out."
    menu:
        "Follow her":
            show bg officesnight
            nm "[actualname]."
            nn "She's inside."
    nm "[actualname]... I need to see her."
    nn "You will. Just open the door."
    nt "I touch the door slowly. My hand is shaking."
    nt "[actualname] can fix this. [actualname] can make it go away."
    scene black with dissolve
    nt "Once I see her, everything will be okay. I won't be in the forest anymore."
    play sound "knock2.ogg"
    nm "[actualname]?"
    play sound "doorclose.ogg" fadein 1
    nt "I push the door open."
    $renpy.pause()
    nm "[actualname], I-"
    play music "ost/hermittense.ogg"
    show hermitMC with hpunch
    nt "!!!"
    nm "[actualname]? [actualname]!"
    nt "I can't move. I can't make a single step closer."
    nn "You can't save her from this."
    nt "She's behind me, whispering into my ear."
    nn "And she can't save you."
    nt "She lowers her voice. Her words are slow. Deliberate."
    nn "{cps=5}S h e \ \ a l r e a d y \ \ k n o w s."
    show hermitMC with vpunch
    nt "!!!"
    nm "No... that's not possible!"
    nn "She isn't stupid. Did you really think she could fall for it?"
    nn "She's had her suspicions for a while now."
    nm "No... she- she would tell me. She wouldn't hide this from me-"
    nn "Do you really expect her to be honest with you? Nobody is."
    nn "She knows everything. You can't hide anymore."
    pause 2
    scene black with Dissolve(1.0)
    jump nextday
label backintheforest2:
    $name=actualname
    $day-=1
    $Hermitloop+=1
    play music "ost/fight.ogg"
    scene bg charlie with vpunch
    "[name]."
    "She... she knows. She must know."
    "Of course she knows, she's smarter than she looks..."
    "What do I do? What- {i}WHAT DO I DO?!"
    "Don't panic. Do {i}not panic."
    "I exchange glances with the girl in black."
    "There must be a way out of this."
    pause 2
    "What... what if there isn't..?"
    "She can't be fooled twice... can she?"
    jump nextday

###################### TOWER #############################################
label entrance:
    scene black with Dissolve(1.0)
    $renpy.pause(2, hard=True)
    play music "ost/dream.wav" fadein 8
    nt "Darkness."
    nt "Where am I..?"
    pause 1
    nt "I can't see anything."
    nt "But I'm standing on something... I take a few steps forward."
    scene bg patientsnight
    nt "I'm in the patients' rooms hallway."
    nt "But... it's dark."
    nt "Why are the lights off?"
    nt "I can barely see."
    nt "I slowly move forward."
    nt "The doors around me... I feel like they're watching me."
    nt "I should be careful."
    nt "Are these... voices?"
    nt "They're coming from one of the rooms..."
    wm "Where do you think you're going?!"
    mn "Away from here."
    mn "From you, more importantly."
    wm "Wh...{i}What..?"
    wm "Why... why would you leave me now..?"
    wm "I thought you said we could... be happy... Together."
    mn "And you really believed me?"
    wm "I... Why wouldn't I believe you?! I love you!"
    mn "You're of no use to me like this. What do you think my family would say if I told them I'm having a child?"
    mn "With a girl who's barely seventeen?"
    wm "I... I thought you... loved me..."
    wm "{i}I gave you everything I had, you scumbag!"
    wm "{i}YOU THINK MY FAMILY WOULD APPROVE OF THIS?! I HAVE NOTHING!"
    mn "You should've thought about that before you agreed to this."
    wm "{i}How dare you?!"
    play sound "doorclose.ogg" fadein 1
    nt "The voices go silent."
    nt "...."
    nt "I move further into the hallway."
    wm "What have I done to deserve you..?"
    wm "...."
    nt "I take a few more steps forward."
    nt "More voices..."
    wm "{i}Who do you think you are to RUN AWAY from me like this?"
    cd "Get away from me!"
    wm "Not until I'm done talking."
    nt "I hear some movement."
    wm "I've been trying my best for you these past six years, and you just {i}KEEP FAILING ME!"
    cd "...."
    wm "...What's that look supposed to mean? ANSWER ME!"
    ##hit 
    wm "See? Do you really want me to get mad at you?!"
    wm "I don't want to have to do this, but you leave me no choice."
    cd "It was your choice to have me."
    wm "{i}-!!!"
    wm "What did you say, you brat?!"
    cd "It's your fault."
    wm "...."
    scene bg patientshanged with dissolve
    stop music fadeout 5
    nt "I stop by another door. For some reason, it feels special."
    nt "Come in, [name]."
    nt "...."
    nt "I open the door."
    show hangedscare
    play music "rain.mp3" fadein 3
    $renpy.pause(18,hard=True)
    jump nextday
label dungeon:
    scene black with Dissolve(1.0)
    pause 2
    nn "[name]... where are you..?"
    nt "A lonely voice calls me."
    nt "I look around, but I can't see anything."
    nt "Am I... dreaming..?"
    play music "ost/tower.wav" fadein 6
    nt "Standing up from the floor, I feel a wall behind me."
    nt "Stone... cold and rough."
    nt "What is this place..?"
    nn "Ngh -!"
    nt "A groan of pain coming from somewhere ahead."
    scene black with hpunch
    nt "Another one."
    nt "I follow the sounds blindly, hoping to reach their source."
    wm "What, you won't fight back?"
    nt "A series of thuds echoes around me, but the child is silent."
    nt "Something feels wrong..."
    wm "You think you're too good for this?!"
    wm "...or have you given up completely?"
    cd "...i don't want to fight you"
    nt "One more thud."
    wm "{i}LIAR!"
    wm "You're nothing but a liar! You hate me, I know it!"
    cd "i don't..."
    wm "Why..."
    wm "WHY WON'T YOU RESIST ME?!"
    nt "The voices fade away."
    pause 2
    nn "[name]... i see you over there..."
    nn "don't leave yet... not now..."
    nt "I try to move towards the source of the voice."
    scene hangedchild with Dissolve(2.0)
    nt "This is the child I heard before..."
    nm "Tom..."
    nt "The child nods slowly."
    nt "I can't look away from all the bruises..."
    nt "Is this what it used to be like?"
    nn "i... didn't think you would get here..."
    nn "that... made me happy."
    menu:
        "Who are you?":
            $sanity-=10
            $strength=False
            nn "what do you mean..?"
            nn "you know me, don't you?"
            nn "of course you do"
        "Are you okay?":
            nn "of course i am"
            nn "can't you see..?"
            nt "The child seems oblivious to their injuries."
    nn "now that you're here..."
    nn "i want to ask something of you."
    nn "you are underground."
    nn "these stairs will lead you to a tall building."
    nn "a tower."
    nn "i can't leave this place... i'm stuck here."
    nn "but... there's something i need you to find."
    nn "you're free. you can help me."
    nn "you will, won't you..?"
    menu:
        "Yes":
            nt "The child's eyes light up."
        "No":
            $sanity-=20
            $strength=False
            nn "you have to..."
    nn "go up these stairs."
    nn "don't stop until you reach the top."
    nn "there, you will find what i need."
    nn "you have to..."
    show drk with dissolve
    nn "{cps=12}c l i m b . . ."
    show drk 2 with dissolve
    nn "{cps=8}. . . t h e \ \ t o w e r"
    scene black with Dissolve(2.0)
    pause 1
    jump nextday