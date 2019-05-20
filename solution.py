#!/usr/bin/env python
import sys
from pexpect import spawn, EOF
from dunnetPytool import sendOne, getCode

dunnet = spawn('emacs -batch -l dunnet', encoding='utf-8')
dunnet.logfile_read = sys.stdout
dunnet.expect('>')

def findEgg():
    direction = 'e'
    got_egg = eggCheck('n')
    for i in range(4):
        for j in range(5):
            got_egg = eggCheck(direction) or got_egg
            if got_egg:
                st = 4 - j if direction == 'w' else j + 1
                ensureFifthSt(st)
                break
        if i < 3:
            up_egg = eggCheck('n')
            got_egg = up_egg or got_egg
            if direction == 'w' and up_egg:
                ensureFifthSt(0)
        if i == 0:
            sendOne(dunnet, 'get all')
        if got_egg:
            for l in range(2-i):
                sendOne(dunnet, 'n')
            break
        direction = flip(direction)


def eggCheck(direction):
    got_egg = sendOne(dunnet, direction, expected=['egg'])
    if got_egg:
        sendOne(dunnet, 'get all')
    return got_egg


def ensureFifthSt(street):
    for k in range(5 - street):
        sendOne(dunnet, 'e')


def answerQuestion(direction):
    questions = ['What is your password on the machine called ‘pokey‘?',
                 'What password did you use during anonymous ftp to gamma?',
                 'treasures for points?',
                 'What is your login name on the ‘endgame’ machine?',
                 'What is the nearest whole dollar to the price of the shovel?',
                 'What is the name of the bus company serving the town?',
                 'Give either of the two last names in the mailroom, other than your own.',
                 'What cartoon character is on the towel?',
                 'What is the last name of the author of EMACS?',
                 'How many megabytes of memory is on the CPU board for the Vax?',
                 'Which street in town is named after a U.S. state?',
                 'How many pounds did the weight weigh?',
                 'Name the STREET which runs right over the subway stop.',
                 'How many corners are there in town (excluding the one with the Post Office)?',
                 'What type of bear was hiding your key?',
                 'Name either of the two objects you found by digging.',
                 'What network protocol is used between pokey and gamma?']
    answers = ['robert',
               'toukmond',
               '4',
               'toukmond',
               '20',
               'mobytours',
               'collier',
               'snoopy',
               'stallman',
               '2',
               'vermont',
               '10',
               '4',
               '24',
               'grizzly',
               'cpu',
               'tcp/ip']
    dunnet.sendline(direction)
    i = dunnet.expect(questions)
    sendOne(dunnet, 'answer ' + answers[i])


def flip(direction):
    if direction == 'e':
        return 'w'
    else:
        return 'e'

sendOne(dunnet, 'get shovel')
sendOne(dunnet, 'e')
sendOne(dunnet, 'e')
sendOne(dunnet, 'dig')
sendOne(dunnet, 'take card')
sendOne(dunnet, 'se')
sendOne(dunnet, 'take food')
sendOne(dunnet, 'se')
sendOne(dunnet, 'drop food')
sendOne(dunnet, 'take key')
sendOne(dunnet, 'sw')
sendOne(dunnet, 'take bracelet')
sendOne(dunnet, 'ne')
sendOne(dunnet, 'nw')
sendOne(dunnet, 'nw')
sendOne(dunnet, 'ne')
sendOne(dunnet, 'ne')
sendOne(dunnet, 'ne')
sendOne(dunnet, 'w')
sendOne(dunnet, 'put card in cabinet')
sendOne(dunnet, 'type')
sendOne(dunnet, 'toukmond')
sendOne(dunnet, 'robert')
sendOne(dunnet, 'ftp gamma')
sendOne(dunnet, 'anonymous')
sendOne(dunnet, 'toukmond')
sendOne(dunnet, 'binary')
sendOne(dunnet, 'send lamp.o')
sendOne(dunnet, 'send shovel.o')
sendOne(dunnet, 'send key.o')
sendOne(dunnet, 'quit')
sendOne(dunnet, 'rlogin gamma')
sendOne(dunnet, 'worms')
sendOne(dunnet, 'get lamp')
sendOne(dunnet, 'e')
sendOne(dunnet, 'n')
sendOne(dunnet, 'e')
sendOne(dunnet, 'get weight')
sendOne(dunnet, 'd')
sendOne(dunnet, 'drop weight')
sendOne(dunnet, 'nw')
sendOne(dunnet, 'u')
sendOne(dunnet, 'take all')
sendOne(dunnet, 'se')
sendOne(dunnet, 'd')
sendOne(dunnet, 'nw')
sendOne(dunnet, 'ne')
sendOne(dunnet, 'get preserver')
sendOne(dunnet, 'w')
sendOne(dunnet, 's')
sendOne(dunnet, 'drop disk')
sendOne(dunnet, 'e')
sendOne(dunnet, 'turn dial clockwise')
sendOne(dunnet, 'turn dial clockwise')
sendOne(dunnet, 'turn dial clockwise')
sendOne(dunnet, 'turn dial counterclockwise')
sendOne(dunnet, 'turn dial counterclockwise')
sendOne(dunnet, 'turn dial counterclockwise')
sendOne(dunnet, 'w')
sendOne(dunnet, 'get all')
sendOne(dunnet, 'w')
sendOne(dunnet, 'get all')
sendOne(dunnet, 'e')
sendOne(dunnet, 'n')
sendOne(dunnet, 'e')
sendOne(dunnet, 'd')
sendOne(dunnet, 'nw')
sendOne(dunnet, 'u')
sendOne(dunnet, 'se')
sendOne(dunnet, 'd')
sendOne(dunnet, 'nw')
sendOne(dunnet, 'nw')
sendOne(dunnet, 's')
sendOne(dunnet, 's')
sendOne(dunnet, 's')
sendOne(dunnet, 's')
sendOne(dunnet, 'put diamond in chute')
sendOne(dunnet, 's')
sendOne(dunnet, 'get all')
sendOne(dunnet, 'e')
sendOne(dunnet, 'e')
sendOne(dunnet, 'n')
sendOne(dunnet, 'd')
sendOne(dunnet, 'd')
sendOne(dunnet, 'sw')
sendOne(dunnet, 'e')
sendOne(dunnet, 'u')
sendOne(dunnet, 'dig')
sendOne(dunnet, 'get all')
sendOne(dunnet, 'd')
sendOne(dunnet, 'w')
sendOne(dunnet, 'ne')
sendOne(dunnet, 'u')
sendOne(dunnet, 's')
sendOne(dunnet, 'put platinum in urinal')
sendOne(dunnet, 'flush')
sendOne(dunnet, 'put gold in urinal')
sendOne(dunnet, 'flush')
sendOne(dunnet, 'n')
sendOne(dunnet, 'd')
sendOne(dunnet, 'sw')
sendOne(dunnet, 'w')
sendOne(dunnet, 'd')
sendOne(dunnet, 'e')
sendOne(dunnet, 'get all')
sendOne(dunnet, 'd')
sendOne(dunnet, 's')
sendOne(dunnet, 's')
sendOne(dunnet, 's')
sendOne(dunnet, 'put disk in pc')
sendOne(dunnet, 'reset', 4, ['time:'])
sendOne(dunnet, '3:22:31', expected=['A>'])
gccCode = getCode(dunnet)
sendOne(dunnet, 'exit')
sendOne(dunnet, 'n')
sendOne(dunnet, 'n')
sendOne(dunnet, 'n')
sendOne(dunnet, 'n')
sendOne(dunnet, 'n')
sendOne(dunnet, 'u')
sendOne(dunnet, 'put key in box')
sendOne(dunnet, 'u')
sendOne(dunnet, 'u')
sendOne(dunnet, 'ne')
sendOne(dunnet, 'ne')
sendOne(dunnet, 'get axe')
sendOne(dunnet, 'd')
sendOne(dunnet, 'n')
sendOne(dunnet, 'w')

sendOne(dunnet, gccCode)
sendOne(dunnet, 'cut ethernet cord')
sendOne(dunnet, 'exit')
sendOne(dunnet, 'get all')
sendOne(dunnet, 'e')
sendOne(dunnet, 'n')
sendOne(dunnet, 'get all')
sendOne(dunnet, 'w')
# Now to find that egg...
findEgg()
sendOne(dunnet, 'enter bus')
sendOne(dunnet, 's')
sendOne(dunnet, 's')
sendOne(dunnet, 's')
sendOne(dunnet, 'w')
sendOne(dunnet, 'w')
sendOne(dunnet, 'w')
sendOne(dunnet, 'w')
sendOne(dunnet, 'w')
sendOne(dunnet, 'nw')
sendOne(dunnet, 'exit bus')
sendOne(dunnet, 'n')
sendOne(dunnet, 'e')
sendOne(dunnet, 'n')
sendOne(dunnet, 'get all')
sendOne(dunnet, 'e')
sendOne(dunnet, 'get all')
sendOne(dunnet, 'put glycerine in jar')
sendOne(dunnet, 's')
sendOne(dunnet, 'get all')
sendOne(dunnet, 'put acid in jar')
sendOne(dunnet, 'w')
sendOne(dunnet, 'w')
sendOne(dunnet, 's')
sendOne(dunnet, 'se')
sendOne(dunnet, 'e')
sendOne(dunnet, 'e')
sendOne(dunnet, 'e')
sendOne(dunnet, 'e')
sendOne(dunnet, 'n')
sendOne(dunnet, 'n')
sendOne(dunnet, 'throw jar')
sendOne(dunnet, 'enter train')
sendOne(dunnet, 'n')
sendOne(dunnet, 'n')
sendOne(dunnet, 'put bracelet in disposal')
sendOne(dunnet, 'put egg in disposal')
sendOne(dunnet, 'put coins in disposal')
sendOne(dunnet, 'put ruby in disposal')
sendOne(dunnet, 'put silver in disposal')
sendOne(dunnet, 'd')
sendOne(dunnet, 'get all')
sendOne(dunnet, 'u')
sendOne(dunnet, 'put amethyst in disposal')
sendOne(dunnet, 'u')
sendOne(dunnet, 'w')
sendOne(dunnet, 'w')
sendOne(dunnet, 's')
sendOne(dunnet, 'w')
sendOne(dunnet, 's')
sendOne(dunnet, 'se')
sendOne(dunnet, 's')
sendOne(dunnet, 'e')
sendOne(dunnet, 's')
sendOne(dunnet, 'w')
sendOne(dunnet, 'type')
sendOne(dunnet, 'rlogin endgame')
sendOne(dunnet, 'get all')
sendOne(dunnet, 'n')
answerQuestion('n')
answerQuestion('n')
answerQuestion('n')

sendOne(dunnet, 'drop diamond')
sendOne(dunnet, 'drop bracelet')
sendOne(dunnet, 'drop platinum')
sendOne(dunnet, 'drop gold')
sendOne(dunnet, 'drop egg')
sendOne(dunnet, 'drop coins')
sendOne(dunnet, 'drop ruby')

answerQuestion('s')
answerQuestion('s')
answerQuestion('s')
sendOne(dunnet, 's')
sendOne(dunnet, 'get all')
sendOne(dunnet, 'n')
answerQuestion('n')
answerQuestion('n')
answerQuestion('n')
sendOne(dunnet, 'n')
sendOne(dunnet, 'get all')
sendOne(dunnet, 's')
sendOne(dunnet, 'drop mona')
sendOne(dunnet, 'drop silver')
sendOne(dunnet, 'drop amethyst')
sendOne(dunnet, 'n')
sendOne(dunnet, 'quit', expected = [EOF])
