#!/usr/bin/env python
import sys
from pexpect import spawn, EOF
from dunnetPytool import sendOne, getCode

dunnet = spawn('emacs -batch -l dunnet', encoding='utf-8')
dunnet.logfile_read = sys.stdout
dunnet.expect('>')

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
sendOne(dunnet, 'dun-inventory=\'(1 7 10 11 12 15 17 18 23 24 25 26)\'')
sendOne(dunnet, 'moby')
sendOne(dunnet, 'dun-endgame=t')
sendOne(dunnet, 'dun-uexit=nil')
sendOne(dunnet, 'dun-current-room=102')
sendOne(dunnet, 'exit')
sendOne(dunnet, 'drop diamond')
sendOne(dunnet, 'drop bracelet')
sendOne(dunnet, 'drop platinum')
sendOne(dunnet, 'drop gold')
sendOne(dunnet, 'drop egg')
sendOne(dunnet, 'drop coins')
sendOne(dunnet, 'drop ruby')
sendOne(dunnet, 'drop mona')
sendOne(dunnet, 'drop silver')
sendOne(dunnet, 'drop amethyst')
sendOne(dunnet, 'drop bill')

sendOne(dunnet, 'n')
sendOne(dunnet, 'quit', expected = [EOF])
