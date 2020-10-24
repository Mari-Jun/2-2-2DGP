from pico2d import *

def isCollide(a, b):
	if a[0] > b[2]: return False
	if a[2] < b[0]: return False
	if a[1] > b[3]: return False
	if a[3] < b[1]: return False
	return True

def isCollideJump(a, b):
	if a[0] > b[2]: return False
	if a[2] < b[0]: return False
	if a[1] > b[3]: return False
	if a[3] < b[3]: return False
	return True

def collidesBlock(actor, block):
	return isCollide(actor.getBB(), block)

def collidesBlockJump(actor, block):
	return isCollideJump(actor.getBB(), block)

def collidesBox(a, b):
	return isCollide(a.getBB(), b.getBB())

def drawCollisionBox(actor):
    if hasattr(actor, 'getBB'):
        draw_rectangle(*actor.getBB())
