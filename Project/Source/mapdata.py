import json

mapdatas = {}

def load(file):
    global mapdatas
    if file in mapdatas:
        return mapdatas[file]

    with open(file, 'r') as f:
        dataList = json.load(f)

    blocks = []

    for data in dataList:
        blocks.append((data['ldx'], data['ldy'], data['rux'], data['ruy']))

    mapdatas[file] = blocks
    return blocks

def unload(file):
    global mapdatas
    if file in mapdatas:
        del mapdatas[file]
