import json
import map

mapdatas = {}

def load(file, ldPos):
    global mapdatas
    if file in mapdatas:
        return mapdatas[file]

    with open(file, 'r') as f:
        dataList = json.load(f)

    blocks = []

    for data in dataList:
        blocks.append((data['ldx'] + ldPos[0], data['ldy'] + ldPos[1],
                       data['rux'] + ldPos[0], data['ruy'] + ldPos[1]))

    mapdatas[file] = blocks
    return blocks

def unload(file):
    global mapdatas
    if file in mapdatas:
        del mapdatas[file]
