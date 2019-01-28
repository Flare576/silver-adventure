#!/usr/bin/env python
import sys
from pexpect import spawn, TIMEOUT, EOF

standard_expect = ['>', '\$', ':']
keyDelay = 0
lineDelay = .001

def sendOne(dunnet, command, timeout_val=.01, expected = standard_expect):
    typeIt(dunnet, command)
    got_expected = True
    try:
        dunnet.expect(expected, timeout=timeout_val)
    except TIMEOUT:
        got_expected = False
    # Clean up pipe
    dunnet.expect([TIMEOUT, EOF], timeout=lineDelay)
    return got_expected


def typeIt(dunnet, command):
    if keyDelay == 0:
        dunnet.sendline(command)
        dunnet.expect(TIMEOUT, 0)
    else :
        for character in command:
            dunnet.send(character)
            dunnet.expect(TIMEOUT, keyDelay)
        dunnet.sendline('')


def getCode(dunnet):
    # dunnet.expect([TIMEOUT], timeout=3)
    typeIt(dunnet, 'type foo.txt')
    dunnet.expect('(\d{3})')
    code = dunnet.match.group(1)
    dunnet.expect(['A>'])
    return code

