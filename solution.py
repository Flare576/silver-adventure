#!/usr/bin/env python
import sys
from pexpect import spawn, TIMEOUT, EOF

standard_expect = ['>', '\$', ':']

dunnet = spawn('emacs -batch -l dunnet')
dunnet.logfile_read = sys.stdout
dunnet.expect('>')


def sendOne(command, timeout_val=.01, expected = standard_expect):
    typeIt(command)
    got_expected = True
    try:
        dunnet.expect(expected, timeout=timeout_val)
    except TIMEOUT:
        got_expected = False
    # Clean up pipe
    dunnet.expect([TIMEOUT, EOF], timeout=.01)
    return got_expected


def typeIt(command):
    for character in command:
        dunnet.send(character)
        dunnet.expect(TIMEOUT, .005)
    dunnet.sendline('')


def getCode():
    # dunnet.expect([TIMEOUT], timeout=3)
    typeIt('type foo.txt')
    dunnet.expect('(\d{3})')
    code = dunnet.match.group(1)
    dunnet.expect(['A>'])
    return code


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
            sendOne('get all')
        if got_egg:
            for l in range(2-i):
                sendOne('n')
            break
        direction = flip(direction)


def eggCheck(direction):
    got_egg = sendOne(direction, expected=['egg'])
    if got_egg:
        sendOne('get all')
    return got_egg


def ensureFifthSt(street):
    for k in range(5 - street):
        sendOne('e')


def answerQuestion(direction):
    questions = ['What is your password on the machine called \'pokey\'?',
                 'What password did you use during anonymous ftp to gamma?',
                 'treasures for points?',
                 'What is your login name on the \'endgame\' machine?',
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
    sendOne('answer ' + answers[i])


def flip(direction):
    if direction == 'e':
        return 'w'
    else:
        return 'e'


sendOne('get shovel')
sendOne('e')
sendOne('e')
sendOne('dig')
sendOne('take card')
sendOne('se')
sendOne('take food')
sendOne('se')
sendOne('drop food')
sendOne('take key')
sendOne('sw')
sendOne('take bracelet')
sendOne('ne')
sendOne('nw')
sendOne('nw')
sendOne('ne')
sendOne('ne')
sendOne('ne')
sendOne('w')
sendOne('put card in cabinet')
sendOne('type')
sendOne('toukmond')
sendOne('robert')
sendOne('ftp gamma')
sendOne('anonymous')
sendOne('toukmond')
sendOne('binary')
sendOne('send lamp.o')
sendOne('send shovel.o')
sendOne('send key.o')
sendOne('quit')
sendOne('rlogin gamma')
sendOne('worms')
sendOne('get lamp')
sendOne('e')
sendOne('n')
sendOne('e')
sendOne('get weight')
sendOne('d')
sendOne('drop weight')
sendOne('nw')
sendOne('u')
sendOne('take all')
sendOne('se')
sendOne('d')
sendOne('nw')
sendOne('ne')
sendOne('get preserver')
sendOne('w')
sendOne('s')
sendOne('drop disk')
sendOne('e')
sendOne('turn dial clockwise')
sendOne('turn dial clockwise')
sendOne('turn dial clockwise')
sendOne('turn dial counterclockwise')
sendOne('turn dial counterclockwise')
sendOne('turn dial counterclockwise')
sendOne('w')
sendOne('get all')
sendOne('w')
sendOne('get all')
sendOne('e')
sendOne('n')
sendOne('e')
sendOne('d')
sendOne('nw')
sendOne('u')
sendOne('se')
sendOne('d')
sendOne('nw')
sendOne('nw')
sendOne('s')
sendOne('s')
sendOne('s')
sendOne('s')
sendOne('put diamond in chute')
sendOne('s')
sendOne('get all')
sendOne('e')
sendOne('e')
sendOne('n')
sendOne('d')
sendOne('d')
sendOne('sw')
sendOne('e')
sendOne('u')
sendOne('dig')
sendOne('get all')
sendOne('d')
sendOne('w')
sendOne('ne')
sendOne('u')
sendOne('s')
sendOne('put platinum in urinal')
sendOne('flush')
sendOne('put gold in urinal')
sendOne('flush')
sendOne('n')
sendOne('d')
sendOne('sw')
sendOne('w')
sendOne('d')
sendOne('e')
sendOne('get all')
sendOne('d')
sendOne('s')
sendOne('s')
sendOne('s')
sendOne('put disk in pc')
sendOne('reset', 4, ['time:'])
sendOne('3:22:31', expected=['A>'])
gccCode = getCode()
sendOne('exit')
sendOne('n')
sendOne('n')
sendOne('n')
sendOne('n')
sendOne('n')
sendOne('u')
sendOne('put key in box')
sendOne('u')
sendOne('u')
sendOne('ne')
sendOne('ne')
sendOne('get axe')
sendOne('d')
sendOne('n')
sendOne('w')

sendOne(gccCode)
sendOne('cut ethernet cord')
sendOne('exit')
sendOne('get all')
sendOne('e')
sendOne('n')
sendOne('get all')
sendOne('w')
# Now to find that egg...
findEgg()
sendOne('enter bus')
sendOne('s')
sendOne('s')
sendOne('s')
sendOne('w')
sendOne('w')
sendOne('w')
sendOne('w')
sendOne('w')
sendOne('nw')
sendOne('exit bus')
sendOne('n')
sendOne('e')
sendOne('n')
sendOne('get all')
sendOne('e')
sendOne('get all')
sendOne('put glycerine in jar')
sendOne('s')
sendOne('get all')
sendOne('put acid in jar')
sendOne('w')
sendOne('w')
sendOne('s')
sendOne('se')
sendOne('e')
sendOne('e')
sendOne('e')
sendOne('e')
sendOne('n')
sendOne('n')
sendOne('throw jar')
sendOne('enter train')
sendOne('n')
sendOne('n')
sendOne('put bracelet in disposal')
sendOne('put egg in disposal')
sendOne('put coins in disposal')
sendOne('put ruby in disposal')
sendOne('put silver in disposal')
sendOne('d')
sendOne('get all')
sendOne('u')
sendOne('put amethyst in disposal')
sendOne('u')
sendOne('w')
sendOne('w')
sendOne('s')
sendOne('w')
sendOne('s')
sendOne('se')
sendOne('s')
sendOne('e')
sendOne('s')
sendOne('w')
sendOne('type')
sendOne('rlogin endgame')
sendOne('get all')
sendOne('n')
answerQuestion('n')
answerQuestion('n')
answerQuestion('n')

sendOne('drop diamond')
sendOne('drop bracelet')
sendOne('drop platinum')
sendOne('drop gold')
sendOne('drop egg')
sendOne('drop coins')
sendOne('drop ruby')

answerQuestion('s')
answerQuestion('s')
answerQuestion('s')
sendOne('s')
sendOne('get all')
sendOne('n')
answerQuestion('n')
answerQuestion('n')
answerQuestion('n')
sendOne('n')
sendOne('get all')
sendOne('s')
sendOne('drop mona')
sendOne('drop silver')
sendOne('drop amethyst')
sendOne('n')
sendOne('quit', expected = [EOF])
