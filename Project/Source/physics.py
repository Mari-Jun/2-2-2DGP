from pico2d import *

def collidesBox(a, b):
	(la, ba, ra, ta) = a.getBB()
	(lb, bb, rb, tb) = b.getBB()

	if la > rb: return False
	if ra < lb: return False
	if ba > tb: return False
	if ta < bb: return False

	return True

def drawCollisionBox(actor):
    if hasattr(actor, 'getBB'):
        draw_rectangle(*actor.getBB())
