from pico2d import *

def isCollide(a, b):
	if a[0] > b[2]: return False
	if a[2] < b[0]: return False
	if a[1] > b[3]: return False
	if a[3] < b[1]: return False
	return True

def isCollideJumpCheck(a, b):
	if a[0] > b[2]: return False
	if a[0] < b[0]: return False
	if a[2] < b[0]: return False
	if a[2] > b[2]: return False
	if a[1] > b[3]: return False
	if a[3] < b[3]: return False
	return True

def collides(actor, bb):
	return isCollide(actor.getBB(), bb)

def collidesJumpCheck(bb, block):
	return isCollideJumpCheck(bb, block)

def collidesBox(a, b):
	return isCollide(a.getBB(), b.getBB())

def collidesBTB(a, b):
	return isCollide(a.getBTB(), b.getBTB())

def drawCollisionBox(actor):
	if hasattr(actor, 'getBB'):
		draw_rectangle(*actor.getBB())

	if hasattr(actor, 'getBTB'):
		draw_rectangle(*actor.getBTB())
