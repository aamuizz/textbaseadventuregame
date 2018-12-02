# Name : Life in the Galaxy
#Made by Abdul Muizz
import time
import random
def wakeup(): #function1
    a = input(">>")
    if a == 'turn on light' or a == 'turn on the light' or a == 'on the light':
        time.sleep(0.5)
        print('\nGood start to the day. Pity it is going to be the worst one of your life. The light is now on.\nBedroom, in the bed\nThe bedroom is a mess.\nIt is a small bedroom with a faded carpet and old wallpaper. There is a washbasin, a chair with a tatty dressing gown slung over it, and a window with the curtains drawn. Near the exit leading south is a phone.\nThere is a flathead screwdriver here. (outside the bed)\nThere is a toothbrush here. (outside the bed)')
    elif a == 'south' or a == 'west' or a == 'north' or a == 'east':
        print("\nIt is dark you can't see anything\nYou have to turn on light first")
        wakeup()
    else:
        print('Command not found')
        wakeup()
def outofbed(): #function2
    b = input(">>")
    if b == 'get out of bed' or b == 'out of bed':
        time.sleep(0.5)
        print('\nVery difficult, but you manage it. The room is still spinning. It dips and sways a little.')
    elif b == 'south' or b == 'north' or b =='west' or b == 'east':
        print("\nYou'll have to get out of the bed first.")
        outofbed()
    elif b == 'wakeup' or b =='wake up':
        print("\nYou are already Awaken")
        outofbed()
    elif b == 'get screwdriver':
        print ("\nYou can't")
        outofbed()
    elif b == 'get toothbrush':
        print ("\nYou can't")
        outofbed()
    else:
        print('Command not found')
        outofbed()
def screwdriver1(): #function3
    c = input(">>")
    if c == 'take screwdriver' or c == 'take screw driver' or c == 'take the screw driver':
        time.sleep(0.5)
        print("\nIt slips through your fumbling fingers and hits the carpet with a nerve-shattering bang")
    elif c == 'north':
        print("\nYou reached the front of house\nThere is nothing to do here. You have gone back to the bedroom")
        screwdriver1()
    else:
        print('Command not found\nHint(Now you have to take screw driver)')
        screwdriver1()
def gown1(): #function4
    d = input(">>")
    if d == 'take gown' or d == 'takegown' or d == 'take the gown':
        print("\nLuckily, this is large enough for you to get hold of. You notice something in the pocket.")
    else:
        print('Command not found\nHint(Now take gown)')
        gown1()
def pocket1(): #function5
    e = input(">>")
    if e == 'look in pocket' or e == 'look in the pocket' or e == 'look into your pocket':
        print("\nIt's hard to open or close the pocket unless you're wearing the gown.\nHint(Now you have to wear gown)")
    else:
        print("command not found")
        pocket1()
def gown2(): #function6
    f = input(">>")
    if f == 'wear gown' or f == 'wear the gown':
        print("\nYou are now wearing your gown.\nHint(Now look into your pocket)")
    elif f == 'south' or f == 'west' or f == 'east' or f == 'north':
        print("You can't go there")
        gown2()
    else:
     print("Command not found")
     gown2()
def pocket2(): #function6
    g = input(">>")
    if g == 'look into your pocket' or g == 'look into pocket':
        print("\nOpening your gown reveals a thing your aunt gave you which you don't' know what it is, a buffered analgesic, and pocket fluff.\nHint(Now take analgesic)")
    else:
     print("Command not found")
     pocket2()
def analgesic(): #function7
    h = input(">>")
    if h == 'take analgesic' or h == 'take the analgesic':
        print("\nYou swallow the tablet. After a few seconds the room begins to calm down and behave in an orderly manner. Your terrible headache goes.\nHint(Now you have to get the screwdriver)")
    else:
     print("Command not found")
     analgesic()
def screwdriver2(): # function8
    j = input(">>")
    if j == 'get screwdriver' or j == 'get screw driver' or j == 'get the screw driver':
          time.sleep(0.5)
          print("\nTaken.\nHint(Now you have to get the toothbrush)")
    else:
        print('Command not found')
        screwdriver2()
def toothbrush(): #function9
    h = input(">>")
    if h == 'get toothbrush' or h == 'pick toothbrush' or h == 'get the toothbrush':
          time.sleep(0.5)
          print("\nAs you pick up the toothbrush a tree outside the window collapses. There is no causal relationship between these two events.\nHint(Now you have to open curtains)")
    else:
        print('Command not found')
        toothbrush()
def opencurtains(): #function10
    i = input(">>")
    if i == 'open curtains' or i == 'open the curtains' or i == 'opencurtains':
        print("\nAs you part your curtains you see that it's a bright morning, the sun is shining, the birds are singing,\nthe meadows are blooming, and a large yellow bulldozer is advancing on your home.\nHint(Now choose directions)")
    else:
        print("I don't know this command")
        opencurtains()
def frontporch():   #function11
    k = input(">>")
    if k == 's' or k == 'south':
        print("\nYou rush down the stairs in panic.\nFront Porch\nThis is the enclosed front porch of your home.\nOn the doormat is a pile of junk mail.")
    elif k == 'west' or k == 'w' or k == 'east' or k == 'e' or k == 'n' or k == 'north':
        print("You can't go that way")
        frontporch()
    else:
        print("I don't know this command")
        frontporch()
def mail():        #function12
    l = input(">>")
    if l == 'taken mail' or 'takemail':
        print("You gather up the pile of mail.\nHint(Now you have to choose directions)")
    else:
        print("I don't know this command.\nHint(Now take mail)")
        mail()
def fronthouse(): #function13
    m = input(">>")
    if m == 's' or m == 'south':
        print("Front of House.\nA countrylane is visible to the south. All that lies between your home and the huge yellow bulldozer bearing down on it\nis a few yards of mud.\nMr. Prosser, from the local council, is standing on the other side of the bulldozer. He seems to be wearing a\ndigital watch.He looks startled to see you emerge, and yells at you to get out of the way.\nThe bulldozer rumbles slowly toward your home.\nHint(Now you have to wait for bulldozer)")
    elif m == 'north' or m == 'west' or m == 'east':
        print("You can't go that way")
        fronthouse()
    else:
        print("I don't know this command")
        fronthouse()
def timepass():  #function14
    n = input(">>")
    if n == 'wait' or n == 'w':
       print("Time passes...\nThe bulldozer rumbles slowly toward your home.\nHint(Now you have to lie down)")
    else:
        print("I don't know this command")
        timepass()
def liedown():  #function15
    o = input(">>")
    if o == 'liedown' or o == 'lie down':
        print("You lie down in the path of the advancing bulldozer. Prosser yells at you to for crissake move!!!\nHint(Now you have to wait)")
    else:
        print("I don't know this command")
        liedown()
def timepass1(): #function16
    p = input(">>")
    if p == 'wait':
        print("Time passes...\nThe noise of the giant bulldozer is now so violently loud that you can't even hear Prosser yelling to warn you\nthat you will be killed if you don't get the hell out of the way. You just see him gesticulating wildly.\nHint(You have to wait some more)")
    else:
        print("I don't know this command")
        timepass1()
def timepass2(): #function17
    q = input(">>")
    if q == 'wait':
        print("Time passes...\nWith a terrible grinding of gears the bulldozer comes to an abrupt halt just in front of you. It shakes,\nshudders, and emits noxious substances all over your rose bed. Prosser is incoherent with rage.\nMoments later, your friend Ford Prefect arrives. He hardly seems to notice your predicament, but keeps\nglancing nervously at the sky. He says 'Hello, Arthur,' takes a towel from his battered leather satchel, and\n offers it to you.\nHint(Ask ford about your home)")
    else:
        print("I don't know this command")
        timepass2()
def askhouse():  #function18
    r = input(">>")
    if r == 'ford what about my home' or r == 'what about my home':
        print("Ford looks startled, then guilty. He starts to say something and stops. He starts to say something else and\nstops. Suddenly he seems to see the bulldozer for the first time, stops starting to say things and starts.\nHe seems to come to a momentous decision, says he has something of Earth-shattering importance to tell\nyou, and stresses the importance of a quick drink at the Horse 'n Groom.\nPointing toward Prosser, you exclaim 'But that man wants to knock my house down!' Ford goes off for a\nquiet word with Prosser. From where you're lying, you cannot hear what's happening, although they seem\ndeeply engrossed in conversation.\nHint(Now you have to wait)")
    elif r == 'ford how are you':
        print("I'm Fine.....\nDo you have any question?")
        askhouse()
    else:
        print("I don't know this command\nHint(Ask ford what about my home)")
        askhouse()
def timepass3():  #function19
    s = input(">>")
    if s == 'wait':
        print("Time passes...\nFord and Prosser stop talking and approach you. Ford says that Prosser has agreed to lie in your place so\nthat the two of you can go off to the Pub. Reluctantly, Prosser steps forward and lies down in front of the\nbulldozer. You stand up.\nHint(Now you have to take towel)")
    else:
        print("I don't know this command")
        timepass3()
def towel():     #function20
    t = input(">>")
    if t == 'take towel' or t == 'taketowel':
        print("Taken.\nHint(Now choose directions)")
    else:
        print("I don't know this command")
        towel()
def road():  #function21
    u = input(">>")
    if u == 's' or u == 'south':
        print("Country Lane\nThe road runs from your home, towards the village Pub, to the west.")
    elif u == 'n' or u == 'north':
        print("You reached front of house. There's nothing to do here\nYou have gone back to the country lane")
        road()
    elif u == 'east' or u == 'west':
        print ("You can't go that way")
        road()
    else:
        print("I don't know this command")
        road()
def road2():  #function22
    v = input(">>")
    if v == 'w' or v == 'west':
        print("Pub\nThe Pub is pleasant and cheerful and full of pleasant and cheerful people who don't know they've got about twelve minutes to live and are therefore having a spot of lunch. Some music is playing on an old jukebox. The exit is east.\nThere is a barman serving at the bar.\nBehind the bar is a shelf. It is full of the sort of items you find on shelves behind bars in pubs.")
    else:
        print("I don't know this command")
        road2()
def lookself(): #function23
    w = input(">>")
    if w == 'look at shelf' or w == 'look at the self':
        print("On the shelf behind the bar is the usual array of bottles, glasses and soggy beermats, some packets of\npeanuts, and a plate of uninviting cheese sandwiches.\nFord hurries after you.\nHint(Now you have to buy sandwich)")
    else:
        print("I don't know this command\nHint(Now you have to look at shelf)")
        lookself()
def buysandwich(): #function24
    x = input(">>")
    if x == 'buy sandwich':
        print("The barman gives you a cheese sandwich. The bread is like the stuff that stereos come packed in, the cheese\nwould be great for rubbing out spelling mistakes, and margarine and pickle have performed an unedifying\nchemical reaction to produce something that shouldn't be, but is, turquoise. Since it is clearly unfit for\nhuman consumption you are grateful to be charged only a pound for it.\nFord buys lots of beer and offers half to you. 'Muscle relaxant...' he says, impenetrably.\n")
    else:
        print("I don't know this command")
        buysandwich()
def drinkbeer(): #function25
    y = input(">>")
    if y == 'drinkbeer' or y == 'drink beer':
        print("It's very good beer, brewed by a small local company. You particularly like its flavour, which is why you woke\nup feeling so wretched this morning. You were at somebody's birthday party here in the Pub last night.\nYou begin to relax and enjoy yourself, so when Ford mentions that he's from a small planet in the vicinity of\nBetelgeuse, not from Guildford as he usually claims, you take it in your stride, and say 'Oh yes, which part?'\nHint(Drink beer again)")
    else:
        print("I don't know this command")
        drinkbeer()
def drinkbeer1(): #function26
    z = input (">>")
    if z == 'drink beer' or z == 'drinkbeer':
        print("It is really very pleasant stuff, with a very good dry, nutty flavour, some light froth on top, and a deep colour.\nIt is at exactly room temperature. You reflect that the world cannot be all bad when there are such pleasures\nin it.\n\nFord mentions that the world is going to end in about twelve minutes.\nHint(Drink beer again)")
    else:
        print("I don't know this command")
        drinkbeer1()
def drinkbeer2():  #function27
    ab = input(">>")
    if ab == 'drinkbeer' or ab == 'drink beer':
        print("There is a distant crash which Ford explains is nothing to worry about, probably just your house being knocked down.\nHint(Now choose directions)")
    else:
        print("I don't know this command")
        drinkbeer2()
def east(): #function28
    ac = input(">>")
    if ac == 'e' or ac == 'east':
        print("Country Lane\nYou see the huge bulldozer heaving itself among the cloud of brick dust which is all that remains of your\nhome. As you start up the lane, a small dog runs up to you, yapping.\nFord hurries after you.")
    elif ac == 'west' or ac == 'south' or ac == 'north':
        print("You can't go that way")
        east()
    else:
        print("I don't know this command\nHint(Now you have to look at dog)")
        east()
def lookdog(): #function29
    ad = input(">>")
    if ad == 'look at the dog' or ad == 'look at dog' or ad == 'look dog':
        print("The mongrel looks hungry.")
    else:
        print("I don't know this command")
        lookdog()
def sandwichtodog(): #function30
    ae = input(">>")
    if ae == 'give sandwich to dog' or ae == 'give sandwich to the dog':
        print("The dog is deeply moved. With powerful sweeps of its tail it indicates that it regards this cheese sandwich as\none of the great cheese sandwiches. Nine out of ten pet owners could happen by at this point expressing any\npreference they pleased, but this dog would spurn both them and all their tins. This is a dog which has met\nits main sandwich. It eats with passion, and ignores a passing microscopic space fleet.\nHint(Now choose directions)")
    else:
        print("I don't know this command\Hint(You have to give sandwich to dog)")
        sandwichtodog()
def north1(): #function31
    af = input(">>")
    if af == 'n' or af == 'north':
        print("You reach the site of what was your home. It is now a pile of rubble. Mr. Prosser looks sheepishly\ntriumphant, a trick few people can do, as it requires a lot of technically complex deltoid muscle work.\nFront of House\nMr. Prosser, from the local council, is standing on the other side of the bulldozer. He seems to be wearing\na digital watch.\n\nFord hurries after you.\nHint(Now yell at prosser)")
    elif af == 'south' or af == 'west' or af == 'east':
        print("You can't go that way")
        north1()
    else:
        print("I don't know this command")
        north1()
def yell(): #function32
    ag = input(">>")
    if ag == 'yell at prosser':
        print("You begin to get a sore throat.There is also vogon fleet there.) ")
    else:
        print("I don't know this command")
        yell()
def vogonfleet():   #function33
    ah = input(">>")
    if ah == 'look at vogon fleet'or ah == 'look at vogon ships':
        print("The fleet consist of terrifying numbers of huge, ugly, yellow ships, all\nscarred with the results of many such past demolition jobs. Chicago's John\nHancock tower, knocked about a bit and painted yellow, is what they each look\nlike. That is, knocked about a bit, painted yellow, and flying.\n\nThe vast yellow ships thunder across the sky, spreading waves of terror and\npanic in their wake.The voice of the Vogon Captain slams across the country, insisting that the planning charts and demolition orders have been available\nat the local planning office in Alpha Centauri for fifty years and it's too\n late to start making a fuss about it now\\nthroughout the noise, Ford is shouting at you. He removes a small black device\nfrom his satchel, but accidentally drops it at your feet")
    else:
        print("I don't know this command\nHint(Now look at vogon ships or fleet)")
        vogonfleet()
def takedevice():  #function34
    aj = input(">>")
    if aj == 'takedevice' or aj == 'take device':
        print("Taken\nFierce gales whip across the land, and thunder bangs continuously through the air in the wake of the giant\nships. Ford fights to reach you, but the wind is too fierce. Further announcements from the Vogon Captain\nmake it clear that demolition will begin in just a few seconds.\n\nThrough the blinding rain, you see lights flickering on the small device.")
    else:
        print("I don't know this command\nHint(You have to take the device that ford dropped)")
        takedevice()
def examinedevice(): #function35
    ak = input(">>")
    if ak == 'examine device' or ak == 'check device':
        print("The Electronic signaling device is shaped like a small fist with an\nextended thumb. Various lights along its 'knuckles' are currently blinking\nwildly, indicating a spaceship in the vicinity. It has two small buttons, a red one called 'Call Engineer' and a green one call 'hitchhike'. It\nbears a small label which reads 'Another fine product of the 'Sirius Cybernetics Corporation'.Affix to the Thumb is a lifetime guarantee.) ")
    else:
        print("I don't know this command\nHint(Now you have to examine device)")
        examinedevice()
def greenbutton():  #function36
    al = input(">>")
    if al == 'press greenbutton' or al == 'press green button':
        print("Lights whirl sickeningly around your head, the ground arches away beneath your\nfeet, and every atom of your being is scrambled, an experience you're probably\ngoing to have to get used to.You are in...\n\nDark")
    elif al == 'press red button' or al == 'press redbutton':
        print("Calling...Calling..\nNo one responds")
        greenbutton()
    else:
        print("I don't know this command")
        greenbutton()
def dark(): #function37
    am = input (">>")
    if am == 'n' or am == 'north' or am == 'south' or am == 's' or am == 'w' or am == 'west' or am == 'east' or am == 'e':
        print("There's nothing you can taste, nothing you can see, nothing you can hear, nothing you can feel, nothing you\ncan smell, you do not even know who you are.")
        dark()
    elif am == 'smell':
        print("(darkness)\nIt does smell a bit. There's something pungent being waved under your nose. Your head begins to clear. You\ncan make out a shadow moving in the dark.")
        dark()
    elif am == 'look at shadow':
        print("This is a squalid room filled with grubby mattresses, unwashed cups, and unidentifiable bits of smelly alien\nunderwear. A door lies to port, and an airlock lies to starboard.\nAlong one wall is a tall dispensing machine.\nIn the corner is a glass case with a switch and a keyboard.\nIt looks like the glass case contains:\n an atomic vector plotter\n\nFord removes the bottle of Santraginean Mineral Water which he's been waving under your nose. He tells you that you are aboard a Vogon spaceship, and gives you some peanuts.")
    else:
        print("I don't know this command\Hint(You can't see anything but you can see a shadow. look at it")
        dark()
def peanuts(): #function38
    an = input(">>")
    if an == 'eat peanuts':
        print("You feel stronger as the peanuts replace some of the protein you lost in the matter transference beam. There is a glass case here.")
    else:
        print("I don't know this command\nHint(eat the peanuts that ford give you)")
        peanuts()
def glasscase():  #function39
    ao = input(">>")
    if ao == 'look at glass case' or ao == 'look at glasscase':
        print("The glass case is closed. Attached to it are a keyboard and a switch.")
    else:
        print("I don't know this command\n")
        glasscase()
def keyboardandswitch():  #function40
    ap = input(">>")
    if ap == 'press keyboard':
        print("Pushing the keyboard accomplishes nothing.")
        keyboardandswitch()
    elif ap == 'press switch':
        print ("A recording plays: 'Aorkeftkwaefthuvd timbi lzitimb ohuvtruhuverlchop wollimbgryl m oirbr gimbkwai lollz\nzfuda re h od tr gx jvups ghuvvupo sz zzit ohuvfimr goshkwaerld td td te h.\nThere is a dispensing machine there")
    else:
        print ("I don't know this command")
        keyboardandswitch()
def dispensingmachine(): #function41
    aq = input (">>")
    if aq == 'look at dispensing machine' or aq == 'look at dispensingmachine':
        print("The dispenser is tall, has a button at around eye-level, and says 'Babel Fish' in large letters. Anything dispensed would probably come out the slot at around knee-level. It bears a small label which reads 'Another fine product of the Sirius Cybernetics Corporation.'")
    else:
        print("I don;t know this command\nHint(Now look at dispensing machine)")
        dispensingmachine()
def buttonpress():   #function42
    ar = input('>>')
    if ar == 'pressbutton' or ar == 'press button':
        print("Which button do you mean, the dispenser button, the red button, or the green button?")
    else:
        print("I don't know this command\nHint(You to have to press button on the dispensing machine)")
        buttonpress()
def redgreenbutton():  #function43
    az = input('>>')
    if az == 'press red button' or az =='press redbutton':
        print('With a screech of ion brakes a Sirius Cybernetics Corporation Repair Robot pulls up on a bike.')
        redgreenbutton()
    elif az =='press greenbutton' or az == 'press green button':
        print("The Thumb winks and flashes for a second. Nothing further happens.\nThe Engineer robot looks around. 'Somebody call the repair service?'")
        redgreenbutton()
    elif az == 'press dispensor button' or az == 'press dispensor':
        print("A single babel fish shoots out of the slot. It sails across the room and through a small hole in the wall, just under a metal hook.\nIt is of course well known that careless talk costs lives, but the full scale of the problem is not always\nappreciated. For instance, at the exact moment you said 'what to do know' a freak wormhole opened in the\nfabric of the space-time continuum and carried your words far far back in time across almost infinite reaches\nof space to a distant galaxy where strange and warlike beings were poised on the brink of frightful\ninterstellar battle.\n\nThe two opposing leaders were meeting for the last time. A dreadful silence fell across the conference table\nas the commander of the Vl'Hurgs, resplendent in his black jewelled battle shorts, gazed levelly at the\nG'Gugvunt leader squatting opposite him in a cloud of green, sweet-smelling steam. As a million sleek and\nhorribly beweaponed star cruisers poised to unleash electric death at his single word of command, the\nVl'Hurg challenged his vile enemy to take back what it had said about his mother.\n\nThe creature stirred in its sickly broiling vapour, and at that very moment the words 'what to do know'\ndrifted across the conference table. Unfortunately, in the Vl'hurg tongue this was the most dreadful insult\nimaginable, and there was nothing for it but to wage terrible war for centuries. Eventually the error was\ndetected, but over two hundred and fifty thousand worlds, their peoples and cultures perished in the holocaust.\nYou have destroyed most of a small galaxy. Please pick your words with greater care.")
    else:
        print("I don't know this command\nHint(You have to Press the dispensor button)")
        redgreenbutton()
def consultguide(): #function44
    ba = input(">>")
    if ba == 'consult guide about babel fish':
        print ("The Guide checks through its Sub-Etha-Net database and eventually comes up with the following entry:\n\nA mind-bogglingly improbable creature. A babel fish, when placed in one's ear, allows one to understand any language.")
        consultguide()
    elif ba == 'take off gown':
        print ("Okay, you're no longer wearing your gown.\nHint(Now hang gown from hook)")
    else:
        print ("Command not found\nHint(You have to take off gown, you can also consult guide about babel fish)")
        consultguide()
def hanggown():  #function45
    bb = input (">>")
    if bb == 'hang gown from hook':
        print("The gown is now hanging from the hook, covering a tiny hole.")
    else:
        print("I don't know this command\nHint(Now hang gown from hook)")
def dispenserbutton(): #function46
    bc = input(">>")
    if bc == 'press dispensor button' or bc == 'dispenser button':
        print("A single babel fish shoots out of the slot. It sails across the room and hits the dressing gown.The fish slides\ndown the sleeve of the gown and falls to the floor, vanishing through the grating of a hitherto unnoticed\ndrain.There is a satchel there")
    else:
       print("I don't know this command\nHint(Press again the dispenser button on the device and see what happens)")
def takesachel():   #function47
    bd = input (">>")
    if bd == 'take satchel' or bd == 'take the satchel':
        print ("Taken")
    else:
        print("I don't know this command\nHint(You have to take the satchel)")
def opensatchel(): #fuction48
    be = input(">>")
    if be == 'open satchel' or be == 'open the satchel':
        print("You can't. It's not yours. It's Ford's and it's private. There is a tiny robot panel here.")
        opensatchel()
    elif be == 'put satchel in front of panel':
            print("Okay, the satchel is lying on its side in front of the tiny robot panel.\nHint(Now put mail on satchel)")
    else:
        print ("I don't know this command\nHint(You can try opening the satchel and see what happens, and then put satchel in front of panel)")
def mailsatchel():  #fuction49
    bf = input(">>")
    if bf == 'put mail on satchel' or bf == 'mail on satchel':
        print("Okay, the loose pile of junk mail is now sitting on the satchel.\nHint(Now take all the things that you have)")
    else:
        print("I don't know this command")
def takeall():  #function50
    bg = input(">>")
    if bg == 'take all' or bg == 'take all the things':
        print ("loose pile of junk mail: Taken.\nsatchel: Taken.\nyour gown: Taken.\ntowel: Taken.\nthing your aunt gave you which you don't know what it is: Taken.\nkeyboard: What a concept.\nHint(Now wear gown)")
    else:
         print("Command not found\n")
def weargown(): #function51
    bh = input(">>")
    if bh == 'wear gown' or bh == 'wear my gown':
        print ("You are now wearing your gown. You notice a switch on the device ")
    else:
        print ("I don't know this command")
def pressswitch(): #fuction52
    bk = input(">>")
    if bk == 'press switch' or bk == 'press the switch':
        print("Guards brush in and grab you and Ford who comes slowly awake. They drag you\ndown the corridor to a large cabin where they strap you into large menacing\nchairs..\n\nCaptains's Quarter in thepoetry\nappreciation chairs.\nThis is the cabin of the vogon Captain. You and Ford are strapped into poetry\nappreciation chairs.\nThe Captain is indescribably hideous, indescribably blubbery, and\nindescribably mid-to-dark green. He is holding samples of his favourite poetry")
    else:
        print ("I don't know this command\nHint(You have to press the switch)")
def consultguide1(): #function53
    bl = input(">>")
    if bl == 'consult guide on vogon poetry' or bl == 'consult guide vogon poetry':
        print ("The Guide checks through its Sub-Etha-Net database and eventually comes up with the following entry:\nVogon poetry is so awful that even the Sarkopsi of Burphon XII, whose religion strictly forbids the taking of\none's life, consider suicide a preferable alternative to a Vogon poetry reading.")
    elif bl == 'consult guide on vogon':
        print ("The Guide checks through its database and eventually comes up with the following entry:\nVogons, whose specialties are bureaucracy and planet-smashing, are the most unpleasant race in the Galaxy.\nThey wouldn't think twice about throwing someone into space, and wouldn't lift a finger to save their own\ngrandmother from the Ravenous Bugblatter Beast of Traal. Also see the entries on Vogon poetry and the\nRavenous Bugblatter Beast of Traal.")
    else:
        print ("I don't know this command\nHint(You can consult guide on vogon poetry or vogon)")
        consultguide1()
def releaseyou():  #function55
    bn = input(">>")
    if bn == 'ask guard to release you':
        print("The guard releases you and your friend ford and begins cycling the air in the airlock.\n'Hey Guard!'shouts Ford, did you really enjoy this sort of thing? Shouting, stomping around, shouting people is it really a fulfilling career?")
    elif bn == "fight with guard":
        print("The hold of the Vogon ship is virtually undamaged by the explosion of the glass case. You, however,\nare blasted into tiny bits and smeared all over the room. Several cleaning robots fly in and wipe you neatly off\nthe walls.\n\n\n****  You have died  ****\n\nGame End")
        playagain()
    else:
        print ("I don't know this command\nHint(You can ask guard to release you or you can try fight with guard)")
def pressswitch1():  #function56
    bo = input(">>")
    if bo == 'press switch' or 'pressswitch':
        print ("Nothing Happens! You see a atomic vector plotter lying nearby you\n\nFord Continues trying to talk the guard into a sudden career change")
    else:
        print ("I don't know this command\Hint(You can try pressing the switch again)")
        pressswitch()
def plotter():  #function57
    bq = input(">>")
    if bq == 'take plotter'or bq == 'takeplotter':
        print ("Taken\nFord Continues trying to talk the guard into a sudden career change")
    else:
        print ("I don't know this command\nHint(You have to take that plotter)")
def consultplotter():
    consult = input(">>")
    while consult == 'consult guide on plotter':
        print("The Guide checks through its database and eventually comes up with the following entry:\nThe atomic vector plotter is one of the most primary application device of\nThe atomic vector plotter is one of the primary application devices of\nimprobability Physics.\n\nFord continues to talk to the guard in a sudden change.")
        break
    else:
        print("I don't know this command\nHint(Do you know what is plotter? You should Consult guide on plotter))")
        consultplotter()
def consultearth():
    consultearth1 = input(">>")
    while consultearth1 == 'consult guide on earth':
        print("The Guide checks through its Sub-Etha-Net database and eventually comes up with the following entry\nMostly harmless\n\nThe guard say, 'Well,all things considered, I guess I Like being a guard.\nEspecially the shouting.REsistance is useless!'He throws you and ford into airlock and closes the door\n\nAirlock\nThis airlock has massive doors to port and starboard.")
        break
    else:
        print("I don't know this command\nHint(Now you have to consult guide on earth)")
        consultearth()
def portstarboard():
    portstar = input(">>")
    if portstar =='port'or portstar == 'go port':
        print("The inner door is closed")
        portstarboard()
    elif portstar == 'starboard' or portstar == 'go starboard':
        print("The outer door is closed")
        portstarboard()
    elif portstar =='wait':
        print("Wait..\nTime passes\n\nFord points at the outer door.'In about two minutes, it will open and we will be ejected into the vaccum of space.But don't panic,I'll think of something.\nthere is a device here")
    else:
        print("Command not found\nHint(You can go try go port or starboard or you can wait for the ford)")
        portstarboard()
def device123():
    device12 = input(">>")
    while device12 == 'look at device' or device12 == 'look at the device':
        print("The electronic signaling device is shaped like a small fist with an\nextended thumb. Various lights along its 'knuckles' are also blinking\nwildly indicating a spaceship. it has a small button a green one\nlabelled'Galaxylife'\nFord is mumbling to himself")
        break
    else:
        print("I don't know this command\nHint(You have to look at the device)")
        device123()
def pressgreen1():
    pressgreen = input(">>")
    while pressgreen == 'press green button' or pressgreen == 'green button':
        print("Every Molecule in your body pull away from every other molecule.then suddenly they snap back again like elastic, and you find,with a\na dizzy head and very sore molecules, that you are in..\n\nDark")
        break
    else:
        print("Command not found")
        pressgreen1()
def dark1():
    dark = input(">>")
    if dark == 'n' or dark == 'north' or dark == 'e' or dark == 'east' or dark == 's' or dark == 'south' or dark =='w' or dark == 'west' or dark == 'smell' or dark == 'feel':
        print("There's nothing you can taste, nothing you can see, nothing you can hear, nothing you can feel, nothing you\ncan smell, you do not even know who you are.")
    elif dark == 'listen':
        print("(to darkness)You hear the deep and distant hum of a star drive coming from far above. There is a exit to port")
    else:
        print("I don't know this command\nHint(You can't do anything but you can listen)")
        dark1()
def port2():
    ported = input(">>")
    if ported == 'go port' or ported == 'port':
        print("You can't go that way.")
        port2()
    elif ported == 'exit port':
        print("(You were lying at the exit of the port)You emerge from a small doorway..\n\nEntry Point\nThere is an entry bay number 2 from the heart of gold.A corridor lies after from here.\nThere is a sales brochure here.")
    else:
        print("Command not found\nHint(You have to exit port)")
        port2()
def brocure():
    brochure = input(">>")
    while brochure == 'take brochure':
        print("Taken\n'Come on let's look for the Bridge.'You follow ford and eventually come to the...\n\nBridge\nThis is the bridge of the heart of gold. A gangway leads down, and steam comes\nfrom entrance to port. Next to the control console is Eddie(the shipboard\ncomputer).\n\nAt the controls appartently expecting you and ford, are a man with more than the usual number of heeds(the name 'Zaphord' is written on his shirt) and a\ndark haired women, holding a handbag.Both seems somehow familiar.\nThere is a molecular hyperwave pincer here.")
        break
    else:
        print("I don't know this command\nHint(take the brochure)")
def pincer():
    pincer1 = input(">>")
    if pincer1 == 'take pincer':
        print("You're holding too much already.\n\nHey!Zaphod how you doing? says ford.He's cool.'Not bad, Ford.Great to see you, replies Zaphod.He's cooler.You suddenly realize that the women is Emma. whom you were trying to pick up at a\nparty in Islington just a few weeks ago, and that Zaphod is the guy she\neventually left the party with.")
    elif pincer1 == 'what is pincer':
        print("a tool made of two pieces of metal with blunt concave jaws that are arranged like the blades of scissors, used for gripping and pulling things.")
        pincer()
    else:
        print(" I don't know this command\Hint(You have to take pincer)")
        pincer()
def putallthings():
    putallthe = input(">>")
    if putallthe == 'put all things in bag':
        print("Sales Brochure:Done\nyour gown:You have to remove it first\ntowel:Done\ntoothbrush:Done\nScrewdriver:Done\nHint(Now go port)")
    else:
        print("Command not found\nHint(You have to put all things in bag")
        putallthings()
def port11():
    port = input(">>")
    if port == 'go port'or port =='port':
        print("You enter the sauna. After several hours, you cameout a changed man\nHint(Now take pincer again)")
    else:
        print("I don't know this command")
        port11()
def takepincer():
    pincer = input(">>")
    if pincer == 'take pincer':
        print("Taken..\nHint(Now open handbag)")
    else:
        print("Command not found")
        takepincer()
def handbag():
    handbag1 = input(">>")
    while handbag1 == 'open handbag':
        print("Opening the bag reveals a pair of tweezers\nHint(Now drop things that you have(e.g pincer and screwdriver)")
        break
    else:
        print("Command not found")
        handbag()
def dropallthings():
    dropthings = input(">>")
    while dropthings == 'drop things':
        print("Dropped pincer, screwdriver, toothbrush\nHint(Now you have to choose directions)")
        break
    else:
        print("Command not found")
        dropallthings()
def south1():
    south = input(">>")
    if south == 's' or south == 'south':
        print("You reached Corridor fore-end\nThere is nothing there")
    elif south == 'west' or south == 'east' or south == 'north':
        print("You can't go that way")
        south1()
    else:
        print("I don't know this command")
        south1()
def dropbag():
    bag = input(">>")
    if bag == 'drop bag':
        print("Dropped\Hint(Now go the corridor aft end)")
    else:
        print("I don't know this command\nHint(Drop bag here)")
        dropbag()
def cooridorend():
    corridor = input(">>")
    while corridor == 'corridor aft end' or corridor == 'go corridor aft end':
        print("This is one end of a short corridor that continues forealong the main deck of\nthe heart of gold.A gangway leads downwards.")
        break
    else:
        print("I don't know this command")
        cooridorend()
def downwards():
    downward1= input(">>")
    while downward1 == 'downwards' or downward1 == 'go downwards':
        print("You are at the bottom of a gangway. A hatch below you is closed. There is a small access space to starboard.")
        break
    else:
        print("I don't know this command")
        downwards()
def star():
    star1 = input(">>")
    while star1 == 'starboard' or star1 == 'access starboard':
        print("That entrance is so narrow that you probably could not pass by holding\nanything. Well, maybe ONE thing.\Hint(Now open hatch)")
        break
    else:
        print("I don't know this command\nHint(Now access starboard)")
        star()
def hatch():
    hatch1 = input(">>")
    while hatch1 == 'open hatch':
        print("Loud sirens blare, fantastically bright red lights flash from all sides, and a\nsoft female voice mentions that opening this hatch in space will evacuate the\nair from the ship")
        break
    else:
        print("I don't know this command")
        hatch()
def port10():
    port = input(">>")
    if port == 'port' or port == 'go port':
        print("The Screening Door is closed\n\nYou Feel a wave of depression sweep over you, and you turn to see that Marvin\nthe robot has stalked miserably into the room")
    else:
        print("I don't know this command\Hint(Now go port)")
        port10()
def opendoor():
    opendoor1 = input (">>")
    if opendoor1 == 'open door' or opendoor1 == 'open the door':
        print("The door explains, in a naughty tone that the room is occupied by a\nsuperintelligent robot and that lesser beings(by which it means you) are not to be admitted.'Show me tiny examples of your intelligence,'it says,'and maybe,just maybe, I might reconsider.\n\nMarvin enters a room to port, and the door closes behind him\nHint(Now Consult guide on intelligence)")
    else:
        print("I don't know this command\nHint(Now you have to open the door that is closed)")
        opendoor()
def consultguide23():
    consultguide = input(">>")
    if consultguide == 'consult guide on intelligence':
        print("The Guide checks through its Sub-Etha-Net database and eventually comes up with the following entry:\nThirty million generations of philosophers have debated the definition of intelligence. The most popular\ndefinition appears in the Sirius Cybernetics Corporation android manuals: 'Intelligence is the ability to\nreconcile totally contradictory situations without going completely bonkers -- for example, having a stomach\nache and not having a stomach ache at the same time, holding a hole without the doughnut, having good luck\nand bad luck simultaneously, or seeing a real estate agent waive his fee.'\Hint(Now go aft)")
    else:
        print("I don't know this command\nHint(Do you know that is intelligence? consult guide on intelligence")
        consultguide23()
def goaft():
    goaft1 = input(">>")
    if goaft1 == 'go aft':
        print("That entrance lead to the Infinite Inprobabilty Drive chamber. It's supposed\nto be a terrible dangerous area of the ship. Are you sure you want to go?")
    else:
        print("I don't know this command")
        goaft()
def yes():
    yes1 = input(">>")
    if yes1 == "yes" or yes1 == 'y':
        print("I can tell you don't want to really. You stride away with a spring in your\nstep, wisely leaving the Drive chamber safely behind you.Telegrams arrive\nfrom well-wisher in all corners of the galaxy congratulating you on your\nprudence and wisdom, cheering you up immensely\nHint(Now Look here and there)")
    elif yes1 == 'no' or yes1 == 'n':
        print("You have died")
        playagain()
    else:
        print("I don't know this command")
        yes()
def engineroom():
    engineroom1 = input(">>")
    if engineroom1 == 'look here and there':
        print("Engine Room\n\nThere are few things to see here. This the room that houses the powerful\ninfinite improbability generator that drives the heart of gold.\nAn exit lies fore of here.\nSitting in the corner is a spare improbabilty generator.\nThere is an ionic diffusion rasp here.\nThere is a pair of hypersonic pliers here.")
    else:
        print("I don't know this command")
        engineroom()
def taken2():
    taken = input(">>")
    if taken == 'take rasp' or taken == 'ionic diffusion rasp':
        print("Taken")
        taken2()
    elif taken == 'take pliers' or taken == 'hypersonic pliers':
        print("Taken\nHint(You have to take generator too)")
        taken2()
    elif taken == 'take generator':
        print("Taken.")
    else:
        print("I don't know this command")
        taken2()
def consultguide11():
    consult = input(">>")
    while consult == 'consult guide on generator':
        print("The Guide checks through its Sub-Etha-Net database and eventually comes up with the following entry:\n\nThe best randomness generator is simple Brownian motion. Any hot gas or liquid\nis a good source.")
        break
    else:
        print("I don't know this command\nHint(You have to consult guide on generator)")
        return consultguide11()
def fore():
    fore2 = input(">>")
    if fore2 == 'go corridor foreend':
        print("Corridor foreend\n\nThere is a sale brochure here\nThere is an electronic device here\nThere is a toothbrush here\nThere is a handbag here")
        fore()
    elif fore2 == 'take toothbrush':
        print("Taken")
        fore()
    elif fore2 == 'take handbag':
        print("Taken")
        fore()
    elif fore2 == 'go port' or fore2 == 'port':
        print("You are in the Gallery area of the ship, containing a machine which is the\nstate of the art in Nutritional Technology\nA carton labelled 'Nutrimat/computer interface' is sitting here.\n\nYou feel a wave of depression sweep over you, and you turn to see that Marvin\nhas stalked miserably into the room.")
    else:
        print("I don't know this command\nHint(You have to go port or you can try going the corridor foreend)")
        fore()
def carton():
    carton1 = input(">>")
    while carton1 == 'open carton':
        print("Opening a shipping carton reveals a strange gun\n\nMarvin wanders off")
        break
    else:
        print("I don't know this command\nHint(You have to open carton)")
        carton()
def take1():
    take = input(">>")
    while take == 'take gun' or take == 'take that gun':
        print("Taken")
        break
    else:
        print("I don't know this command\nHint(take that gun and then examine gun)")
        take1()
def examinegun():
    gun = input(">>")
    if gun == 'examine gun' or gun == 'examine gun':
        print("The gun has a large label which reads'Anti-Bugblatter Beast Ray Gun.'It\nbears a small label which reads 'Another fine product of the Sirius\nCybernetics Corporation' There is a dispensing machine there.")
    else:
        print("I don't know this command")
        examinegun()
def turnmachine():
    turn = input(">>")
    if turn == 'turn on machine' or turn == 'turn machine on':
        print("The Nutrimat makes an instant but highly detailed examination of your taste\nbuds, a spectroscopic analysis of your metabolism and sends tiny experimental\nsignals down your neural pathway to see what you like.\n\nA cupful of Advanced Tea substitute appears in the dispensing slot")
    else:
        print("I don't know this command\nHint(Now turn on Machine)")
        turnmachine()
def cup():
    cup1 = input(">>")
    if cup1 == 'take cup':
        print("Taken\n\nZaphod walks in and presses the touch sensitive pad. The Nutrimat\n produces a huge, ice cold Pan-Galactic Gargle Blaster. Zaphod heads off toward\nthe sauna, sipping loudly")
    else:
        print("I don't know this command\nHint(Take tea that is in dispensing slot)")
        cup()
def consultguide40():
    consult = input(">>")
    if consult == 'consult guide on gargle blaster':
        print("The Guide checks through its Sub-Etha-Net database and eventually comes up with the following entry:\n\nThe best drink in existence; somewhat like having your brains smashed out by a slice of lemon wrapped\naround a large gold brick.")
        consultguide40()
    elif consult == 'examine cup':
        print("About the only characteristic it shares with tea is that of brownian motion")
        consultguide40()
    elif consult == 'drop cup':
        print("Dropped\nThere is device name 'drive' here")
    else:
        print("I don't know this command\nHint(You have done drinking tea now drop the cup)")
        consultguide40()
def drive98():
    drive = input(">>")
    if drive == 'examine drive':
        print("The Spare improbability device has a switch, a long cord ending with a large\nplug and short cord ending with a small plug.It bears a small label which\nreads'Another fine product of the Sirius Cybernetics Corporation")
        drive98()
    if drive == 'plug large plug into large receptacle':
        print("Plugged.Eddie(the shipboard computer) says, 'You shouldn't be playing around\nwith a spare improbability drive. Who knows where it's been?\n\nAnnouncement!Announcement.This is Edie(the shipboard computer).Someone\nhas connnected a spare improbability drive to the manual override receptacle\nBetter be an emergency, that's all i have to say")
    else:
        print("I don't know this command\nHint(First examine driven then You have to plug large plug into large receptacle)")
        drive98()
def unplug():
    un = input(">>")
    while un == 'unplug the large plug' or un == 'unplug large plug':
        print("Done..")
        break
    else:
        print("I don't know this command\nHint(Now unplug the large plug) ")
        unplug()
def plugsmall():
    small = input(">>")
    if small == 'plug small plug into small receptacle':
        print("Plugged..Nothing Happens\nHint(Now put all things in pocket)")
    else:
        print("I don't know this command")
        plugsmall()
def put():
    pocket = input(">>")
    while pocket == 'put all things in pocket':
        print("Strange gun:Done\npair of hypersonic pliers:Done\nionic diffusion rasp:Done\nHint(Now you have to turn on drive)")
        break
    else:
        print("I don't Know this command")
        put()
def driveon():
    drive = input(">>")
    if drive == 'turn on drive' or drive == 'on drive':
        print("Like fog rolling in off the ocean, a shroud of blackness billows towards you.\nUnlike fog rolling in off the ocean, the blackness hits you like a sixteen-tonne truck\n\nDark")
    else:
        print("Command not found")
        driveon()
def dark40():
    dark = input(">>")
    if dark == 'see':
        print("There's nothing you can taste, nothing you can see, nothing you can hear, nothing you can feel, nothing you\ncan smell, you do not even know who you are.")
        dark40()
    elif dark == 'smell':
        print("It does smell a bit. There's something pungent wavibng under your nose. Your\nhead begins to clear. You can make out a shadow moving in the dark")
        dark40()
    elif dark == 'look at shadow':
        print("The Shadow is vaguely Bugblatter beast shaped.\n\nLair\nThis is the lair of the Ravenous Bugblatter beasts of traal.\nThe Ravenous bugblatter beasts of traal is here,looking particularly nusty and hungry\n\nThe Beast whips its evil smelling tail away from your nose and bellows a\nbrain shattering roar\n\nYou notice the beasts Lasero-Zap eyes, its Swivel Shear Teeth, and its\nZangrijad. It has skin like a motorway and breath like a 747. It advances on\nyou, and roars out a demand that says your name")
    else:
        print("I don't know this command\nHint(There's is nothing you can see but you can look at shadow)")
        dark40()
def name():
    na = input(">>")
    while na == 'say arthur':
        print("The Beast roar your name with relish, and explain that once it has eaten you, your name will be added to the list of remembrance\Hint(Now choose directions)")
        break
    else:
        print("I don't know this command\Hint(You have to say your name. Your name is Arthur as you know)")
        name()
def east12():
    east = input(">>")
    if east == 'e' or east == 'east':
        print("Beast's Outer layer\nThis is a large walled courtyard. There is also a sandstone memorial in the middle of the courtyard, on which\nthe beast has roughly carved the name of all its victims\nSome sharp stones lies near the exit to the west.\nBellowing with rage, the Beast charges after you")
        east12()
    elif east == 'west' or east == 'south' or east == 'north':
        print("You can't go that way")
        east12()
    elif east == 'look at memorial':
        print("There are countless name carved on memorial:\nJack, John, Brian, Spike\n\nWith a head-splitting roar, the ravenous bug blatter beast of Traal charges\ntowards you\Hint(Shoot beast with gun)")
    else:
        print("I don't know this command")
        east12()
def shoot():
    sho = input(">>")
    if sho == 'shoot beast with gun':
        print("Some rays from the gun strike the ravenous Bugblatter beast of traal, but it only seems to make it madder.\n\nThe Beast is nearly upon you\nHint(Now Wrap head with towel)")
    elif sho == 'wait':
        print("You Have been Died\n\nGame End")
        playagain()
    else:
        print("I don't Know this Command\nHint(You have gun to save you now shoot beast with gun)")
        shoot()
def towelwarp():
    wrap = input(">>")
    if wrap == 'wrap head with towel':
        print("The Ravenous Bugblatter beast of traal is completely bewildered. It is so dim\nit thinks that if you can't see it, it can't see you. You a few seconds before it realises its mistake.")
    else:
        print("I don't Know this command\nHint(Now you have to save yourself. you should wrap head with towel)")
        towelwarp()
def memorial():
    memo = input(">>")
    if memo == 'write my name on memorial':
        print("You have no carving instrument")
        memorial()
    elif memo == 'take stone' or memo == 'take the stone':
        print("Taken")
    else:
        print("I don't know this command\nHint(You can try writing write your name on memorial or taking the stone)")
        memorial()
def carvename():
    carve = input(">>")
    while carve == 'carve my name with stone':
        print("You chip away with the stone. It's not your best writing, what with your mounting sense of panic and a towel wrapped around your head. However, it suffices..\n\nJust as the Beast is trying to workout where you've diappeared to, it suddenly sees your name freshly carved on its memorial of remembrance.Mystery\nsolved.It realises it must have already eaten you in a fit of absentmindedness\nHint(Now take off towel)")
        break
    else:
        print("I don't know this command\Hint(Now carve your name with stone)")
        carvename()
def offtowel():
    towel = input(">>")
    if towel == 'take off towel' or towel == 'off towel':
        print("You unwrap the towel from your head\Hint(Now look around)")
    else:
        print("I don't know this command\nHint(Now you can take off towel)")
        offtowel()
def lookaround():
    look = input(">>")
    if look == 'look around':
        print("Inner Liar\n\nThis is the heart of the beast lair.\n\nThe Skeleton of deadbeast hunter lies nearby, cluthing something labelled\n'Nutrimat Computer Interface'")
    else:
        print("I don't know this command")
        lookaround()
def takeinter():
    take = input(">>")
    if take == 'take interface':
        print("Taken\nHint(Now wait)")
    elif take == 'drop gun':
        print("Dropped")
        takeinter()
    else:
        print("I don't know this command")
        takeinter()

def waiting():
    wait = input(">>")
    while wait == 'wait':
        print("Time passes...\n\nSuddenly a team of beasthunter charges in, intent on catching\n the beast for their zoo.Mistaking you for the Beast, they fire stun guns at\nyou, wrap you in nets, and install you in a lovely little lair in the\nNational Zoo.\n\nThree Months later the error is discovered but while your damaged suit is\npending in the courts the planet is invaded by Pirates\nImpressed into bondage for a 16 year filing and sorting\nmission on the so-called 'basement world' of Sporla in the Lesser Magellanic\nCloud, you escape with the help of a tribe of nomadic asteroid\npainters\n\nYou develop a unique talent for asteroid painting, gaining considerable fame\nthroughout the Cloud. A nickel-ore deluxe is commissioned by his royal\nGorpness,the ruler of the Nine Hundred Worlds of Gorp, but while\nworking on this new masterpiece your asteroid slips into a small passing black\nhole. Everything becomes...\n\nDark ")
        break
    else:
        print("Command not found")
        waiting()
def darking():
    dark = input(">>")
    if dark == 'see' or dark == 'feel':
        print("There's nothing you can taste, nothing you can see, nothing you can hear, nothing you can feel, nothing you\ncan smell, you do not even know who you are.")
        darking()
    elif dark == 'listen':
        print("(to darkness)\nYou hear the deep and distant hum of a star drive coming from far above. There\nis an exit to the port\nHint(Now go aft)")
    else:
        print("I don't Know this command\nHint(You can't feel or see anything but you can listen)")
        darking()
def aft10():
    aft = input(">>")
    if aft == 'go aft':
        print("(we were lying about the exit to the port)You emerge from a doorway.\n\nEntry Bay Number two\nThere is a flathead screwdriver here.\nThere is a molecular hyperwave pincer here.\nThere is a pair of tweezers here")
    else:
        print("I don't know this command")
        aft10()
def aft11():
    aft = input(">>")
    if aft == 'go aft':
        print("You reached corridor foreend\nThere is a sales brochure here\nThere is an electronic device here\nThere is a toothbrush here\nThere is a handbag here")
    elif aft == 'take screwdriver':
        print("Taken")
        aft11()
    elif aft == 'take pincer':
        print("Taken")
        aft11()
    elif aft == 'take tweezers':
        print("Taken")
        aft11()
    else:
        print("I don't Know this command\nHint(Now go aft)")
        aft11()
def prt():
    port = input(">>")
    if port == 'go port' or port == 'port':
        print("Galley\nA carton labelled 'Nutrimat/Computer Interface' is sitting here. There is a dispensing machine here.\nHint(Now look at machine)")
    elif port == 'take toothbrush':
        print("Taken")
        prt()
    elif port == 'take device':
        print("Taken")
        prt()
    elif port == 'take brochure':
        print("Taken")
        prt()
    elif port == 'take handbag':
        print("Taken")
        prt()
    else:
        print("I don't know this command")
        prt()
def lookmachine1():
    lookmachine = input(">>")
    while lookmachine == 'look at machine':
        print("The Nutrimat has a touch-sensitive pad, a dispensing slot, and a service panel\nwhich is closed. It has a small label which reads 'Another fine product of\nSirius Cybernetics Corporation'")
        break
    else:
        print("I don't Know this command")
        lookmachine1()
def openpanel():
    open = input(">>")
    if open == 'open panel' or open == 'open the panel':
        print("Opening the Nutrimat reveals a circuit board")
    else:
        print("I don't Know this command\nHint(Now you have to open the panel)")
        openpanel()
def takeboard():
    take = input(">>")
    if take == 'take board':
        print("Taken")
        takeboard()
    elif take == 'insert interface into nutrimat':
        print("Done")
    else:
        print("I don't Know this command\nHint(Now insert interface into nutrimat)")
def closepanel():
    close = input(">>")
    while close == 'close panel':
        print("Okay, the Nutrimat is now closed\nHint(Now turn on Machine)")
        break
    else:
        print("I don't Know this command\nHint(Now close panel)")
        closepanel()
def turnon9():
    turn = input(">>")
    if turn == 'turn on machine' or turn == 'turn on the machine':
        print("The Nutrimat is puzzled that you want something made by pouring boiling water\non dead leaves and squirting stuff from a cow in it, and says that it will need some help from Eddie(the shipboard computer).\n\nThe nutrimat begins to whirr\nHint(Now wait four times)")
    else:
        print("I don't KNow this command")
        turnon9()
def wait89():
    wait = input(">>")
    if wait == 'wait':
        print("'Time passess..\n\nA red sign lights up saying:\n\nMEMORY OVERLOAD'")
        wait89()
    elif wait == 'more wait':
        print("Time passes..\n\nAnother red sign lights up saying\n\nRESERVE MEMORY OVERLOAD")
        wait89()
    elif wait == 'more more wait':
        print("Time passes..\n\nA third sign lights up:\nPROCESSOR OVERLOAD\nSWITCH TO TERMINAL MODE")
        wait89()
    elif wait == 'more more more wait':
        print("Time passes..\n\nmore and more signs light up:\nSHIPBOARD COMPUTER ACCESSED\nMAIN MEMORY OVERLOAD\nRESERVE MEMORY ACCESSED\nPARALLEL PROCESSORS ON LINE\n\nNUMBERS BEING CRUNCHED")
    else:
        print("I don't Know this command")
        wait89()
def wait45():
    wait = input(">>")
    if wait == 'wait':
        print("Time passes..\n\n'Announcement, announcement. This is Eddie (the shipboard computer) Emergency\nsituation! Nuclear missiles have just been launched at us from the approaching the\nplanet, which my data banks indicate is the legendary lost planets of\nMagrathea.I cannot perform evasive maneuvers because all circuits are currently engaged by the Nutrimat. The missiles will turn this ship into a\nhuge atomic fireball in approximately eight turns. By the way someone didn't\nfinish their spinach at dinnerHint(Now plug large plug into large receptacle)")
    else:
        print("I don't know this command")
        wait45()
def plugger():
    plug = input(">>")
    if plug == 'plug large plug into the large receptacle':
        print("Plugged")
        plugger()
    elif plug == 'turn on drive':
        print("As you flip the switch, sparks fly from the large receptacle'My new control console!'wails Eddie (the shipboard computer).'This is the thanks i get'\n\nThe universe goes crazy for a moment\n\n'Announcement, announcement. This is Eddie(the shipboard computer). The\nmissiles have turned into a sperm whale at an improbability factor of 2 to the\n39,745th power to 1 against. The whale is currently plummeting toward the\nlegendary lost planet of Magrathea. I hope this will teach you to listen to me\nwhen i say that legendary lost planets can be dangerous. I am proceeding with\nthe present landing instructions.\n\nFord, Zaphod, and Trillian saunter by on their way back to the sauna. 'Good work kid says Zaphod, slaming you on the back.")
    else:
        print("I don't know this command\nHint(Now you can plug large plug into large receptacle and then turn on drive)")
        plugger()
def directions():
    galley = input(">>")
    if galley == 'w' or galley == 'west':
        print("Galley\nA carton labelled 'Nutrimat/Computer interface' is sitting here.\n\nIt looks like the slot contains:\ntea")
        directions()
    elif galley == 'take tea':
        print("no tea: Dropped")
    else:
        print("I don't Know this command\nHint(Now go west and take tea)")
        directions()
def turndrive():
    drive = input(">>")
    if drive == 'turn on drive':
        print("Like fog rolling in off the ocean, a shroud of blackness billows towards you\nUnlike fog rolling in off the ocean, the blackness hits you like a sixteen-tone truck...\n\nDark\nHint(Now ask who i am or go any direction north, west or northeast)")
    else:
        print("I don't Know this Command\nHint(Now turn on drive)")
        turndrive()
def darko():
    dark = input(">>")
    if dark == 'see' or dark == 'hear' or dark == 'taste':
        print("There's nothing you can taste, nothing you can see, nothing you can hear, nothing you can feel, nothing you\ncan smell, you do not even know who you are.")
        darko()
    elif dark == 'feel':
        print("(darkness\nIt does feel a bit cold and wet and squishy. There seems to be some liquid at\nyour fingertips")
        darko()
    elif dark == 'taste liquid':
        print("It tastes just like wine. In fact, you realise with growing embarrassment that\nyour hand is sitting in a glass of white wine\nYou're at a party being given by a distant and incredibly boring acquaintance\nAmong the people you've been introduced to are a shy, mousy fellow from the\nWest Country named Arthur, and a flamboyant guy name Phil. You've had too\nmany drinks already, and the room is beginning to buzz..\nLiving Room\nYou are in a large living room. There is party going on. Other rooms lie to\nthe west\nHint(Try asking who i am)")
    else:
        print("I don't Know this command\nHint(You can feel)")
        darko()
def sowest():
    sow = input(">>")
    if sow == 'who am i' or sow == 'who i am':
        print("You are Trillian")
        sowest()
    elif sow == 'w' or sow == 'west':
        print("Dinning Room\nYou are in a large Dining Room. There is a party going on. Other rooms lie to the south ")
        sowest()
    elif sow == 'south' or sow == 's':
        print("Kitchen\nYou are in a large Kitchen. There is a party going on. Other room lie to the northeast")
        sowest()
    elif sow == 'northeast' or sow == 'ne':
        print("Living Room\nPhil is here\nArthur is here.\nHint(Now take fluff) ")
    else:
        print(" I don't Know this command")
        sowest()
def fluff():
    fluff1 = input(">>")
    while fluff1 == 'take fluff':
        print("You remove the jacket fluff, improving Arthur's appearance greatly. He is\nclearly touched, and starts happily to chat away to you. You dicover that he\nis only slightly more interesting to talk to than an averagely interesting\nwall\nHint(Now put pluff in the bag)")
        break
    else:
        print("I don't Know this command")
        fluff()
def putfluff():
    put = input(">>")
    while put == 'put fluff in the bag' or put == 'put fluf in bag':
        print("Inspection reveals that the handbag isn't open\nHint(Now open purse)")
        break
    else:
        print("I don't Know this Command")
def openbag90():
    openbag = input(">>")
    if openbag == 'open purse' or openbag == 'open purse':
        print("Opening the handbag reveals a pair of tweezers.")
    else:
        print("I don't Know this command")
        openbag90()
def putfluffing():
    fluff = input(">>")
    if fluff == 'put fluff in bag' or fluff == 'put fluff in purse':
        print("Done\nHint(Now talk to phil")
    else:
        print("I don't Know this command")
        putfluffing()
def talkphil():
    talkto = input(">>")
    if talkto == 'talk to phil' or talkto == 'talk with phil':
        print("Phil must not have noticed you, because he just moved into the Dinning Room\nHint(Dinning Room lies to the west)")
    else:
        print("I don't Know this command")
        talkphil()
def westo():
    west = input(">>")
    if west == 'w' or west == 'west':
        print("Dining Room\nPhil is here\n\nArthur follows you like an eager puppy\nHint(Now talk to phil)")
    elif west == 'east' or west == 'north' or west == 'south':
        print ("You can't go that way")
        westo()
    else:
        print("I don't Know this command")
        westo()
def kitc():
    kit = input(">>")
    if kit == 'talk to phil':
        print("phil must not have noticed you, because he just moved to the kitchen\nHint(Kitchen lies to the south)")
    else:
        print("I don't Know this command")
        kitc()
def kit():
    ki = input(">>")
    if ki == 'talk to phil':
        print("Phil must have not noticed you, because he just moved to the living room\nHint(Living room lies either northwest or northeast)")
    else:
        print("I don't Know this command")
        kit()
def livingroom12():
    living = input(">>")
    if living == 'nw' or living == 'northwest':
        print("You can't go that way")
        livingroom12()
    elif living == 'ne' or living == 'northeast':
        print("Living Room\nPhil is here\nPhil Comes up and grips your shoulder.'Hey, this guy boring you? Why not come with me instead? I'm from a different planet. 'He takes you\nout to the parking lot, where his flashy interorbital ion scooter is parked between two\nVolkswagen. After mounting it, the scooter accelerates at such a great speed\nthat you black out almost immediately. Everything becomes..\n\nDark")
    else:
        print("I don't Know this command")
def dark56():
    dark = input(">>")
    if dark == 'see':
        print("There's nothing you can taste, nothing you can see, nothing you can hear, nothing you can feel, nothing you\ncan smell, you do not even know who you are.")
        dark56()
    elif dark == 'listen':
        print("(to darkness) You hear the deep and distant hum of a star drive coming from far above")
        dark56()
    elif dark == 'feel':
        print("It does feel a bit warm and wet and squishy. There is some liquid at\nfingertips\nHint(Now taste liquid)")
    else:
        print("I don't Know this command\nHint(You can feel)")
        dark56()
def tasto():
    taste = input(">>")
    if taste == 'taste liquid':
        print("Yukhhh! You are jerked to your senses by the realisation that you are licking\nthe lining of the whale stomach\n\nInside the whale\nYou are now in the stomach of the whale. You can hear a distant sound of\nrushing wind.\nThere is a flowerpot here\nHint(Now take directions carefully the game is now come to an ending point)")
    else:
        print("I Don't Know this Command")
        tasto()
def survival():
    surted = input(">>")
    if surted == 'take pot':
        print("Taken")
        survival()
    elif surted == 'n' or surted == 'north' or surted == 'w' or surted == 'west':
        print("You have been died\nGame end")
        playagain()
    elif surted == 's' or surted == 'south' or surted == 'e' or surted == 'east':
        print("You have survived!\nYou Won the game\n\nGame End!")
        playagain()
    else:
        print("I don't Know this command")
        survival()
def playagain():
    playagain2 = input("Do You want to Play Again? Yes or No")
    while playagain2 == 'yes' or playagain2 == 'y':
        print("You wake up. The room is spinning very gently round your head. Or at least it would be if you could see\nit which you can't.")
        print('''''')
        print('It is pitch black.')
        wakeup()
        outofbed()
        screwdriver1()
        gown1()
        pocket1()
        gown2()
        pocket2()
        analgesic()
        screwdriver2()
        toothbrush()
        opencurtains()
        frontporch()
        mail()
        fronthouse()
        timepass()
        liedown()
        timepass1()
        timepass2()
        askhouse()
        timepass3()
        towel()
        road()
        road2()
        lookself()
        buysandwich()
        drinkbeer()
        drinkbeer1()
        drinkbeer2()
        east()
        lookdog()
        sandwichtodog()
        north1()
        yell()
        vogonfleet()
        takedevice()
        examinedevice()
        greenbutton()
        dark()
        peanuts()
        glasscase()
        keyboardandswitch()
        dispensingmachine()
        buttonpress()
        redgreenbutton()
        consultguide()
        hanggown()
        dispenserbutton()
        opensatchel()
        mailsatchel()
        takeall()
        weargown()
        pressswitch()
        consultguide1()
        releaseyou()
        pressswitch1()
        plotter()
        consultplotter()
        consultearth()
        portstarboard()
        device123()
        pressgreen1()
        dark1()
        port2()
        brocure()
        pincer()
        putallthings()
        port11()
        takepincer()
        handbag()
        dropallthings()
        south1()
        dropbag()
        cooridorend()
        downwards()
        star()
        hatch()
        port10()
        opendoor()
        consultguide23()
        goaft()
        yes()
        engineroom()
        taken2()
        consultguide11()
        fore()
        carton()
        take1()
        examinegun()
        turnmachine()
        cup()
        consultguide40()
        drive98()
        unplug()
        plugsmall()
        put()
        driveon()
        dark40()
        name()
        east12()
        shoot()
        towelwarp()
        memorial()
        carvename()
        offtowel()
        lookaround()
        takeinter()
        waiting()
        darking()
        aft10()
        aft11()
        prt()
        lookmachine1()
        openpanel()
        takeboard()
        closepanel()
        turnon9()
        wait89()
        wait45()
        plugger()
        directions()
        turndrive()
        darko()
        sowest()
        fluff()
        putfluff()
        openbag90()
        putfluffing()
        talkphil()
        westo()
        kitc()
        kit()
        livingroom12()
        dark56()
        tasto()
        survival()
        break
    if playagain2 == 'No':
        print("Game is closing in a few moment")
        time.sleep(4)
        exit()
    else:
        print("Command not found")
        playagain()
print("Life in the Galaxy\nMade By Abdul Muizz (FA17-BCS-003)")
time.sleep(1)
print('''''')
x = str(input("Game Menu\n\n1.Play\n2.Quit\n"))
if x == '1' or x == 'play':
    print("You wake up. The room is spinning very gently round your head. Or at least it would be if you could see\nit which you can't.")
    print('''''')
    print('It is pitch black.')
    wakeup()
    outofbed()
    screwdriver1()
    gown1()
    pocket1()
    gown2()
    pocket2()
    analgesic()
    screwdriver2()
    toothbrush()
    opencurtains()
    frontporch()
    mail()
    fronthouse()
    timepass()
    liedown()
    timepass1()
    timepass2()
    askhouse()
    timepass3()
    towel()
    road()
    road2()
    lookself()
    buysandwich()
    drinkbeer()
    drinkbeer1()
    drinkbeer2()
    east()
    lookdog()
    sandwichtodog()
    north1()
    yell()
    vogonfleet()
    takedevice()
    examinedevice()
    greenbutton()
    dark()
    peanuts()
    glasscase()
    keyboardandswitch()
    dispensingmachine()
    buttonpress()
    redgreenbutton()
    consultguide()
    hanggown()
    dispenserbutton()
    opensatchel()
    mailsatchel()
    takeall()
    weargown()
    pressswitch()
    consultguide1()
    releaseyou()
    pressswitch1()
    plotter()
    consultplotter()
    consultearth()
    portstarboard()
    device123()
    pressgreen1()
    dark1()
    port2()
    brocure()
    pincer()
    putallthings()
    port11()
    takepincer()
    handbag()
    dropallthings()
    south1()
    dropbag()
    cooridorend()
    downwards()
    star()
    hatch()
    port10()
    opendoor()
    consultguide23()
    goaft()
    yes()
    engineroom()
    taken2()
    consultguide11()
    fore()
    carton()
    take1()
    examinegun()
    turnmachine()
    cup()
    consultguide40()
    drive98()
    unplug()
    plugsmall()
    put()
    driveon()
    dark40()
    name()
    east12()
    shoot()
    towelwarp()
    memorial()
    carvename()
    offtowel()
    lookaround()
    takeinter()
    waiting()
    darking()
    aft10()
    aft11()
    prt()
    lookmachine1()
    openpanel()
    takeboard()
    closepanel()
    turnon9()
    wait89()
    wait45()
    plugger()
    directions()
    turndrive()
    darko()
    sowest()
    fluff()
    putfluff()
    openbag90()
    putfluffing()
    talkphil()
    westo()
    kitc()
    kit()
    livingroom12()
    dark56()
    tasto()
    survival()
elif x == '2' or x == 'quit':
    exit()
else:
    exit()
