import json
import map

mapdatas = {}

def load(file, data, ldPos):
    global mapdatas
    if file in mapdatas:
        return mapdatas[file]

    with open(file, 'r') as f:
        dataList = json.load(f)

    print('%s load complete' % file)

    if data == 'block':
        return loadBlock(dataList, file, ldPos)
    elif data == 'enemy':
        return loadEnemy(dataList, file, ldPos)

def loadBlock(dataList, file, ldPos):
    blocks = []

    for data in dataList:
        blocks.append((data['ldx'] + ldPos[0], data['ldy'] + ldPos[1],
                       data['rux'] + ldPos[0], data['ruy'] + ldPos[1]))

    mapdatas[file] = blocks
    return blocks

def loadEnemy(dataList, file, ldPos):
    enemys = []

    for data in dataList:
        enemys.append((data['name'], data['x'] + ldPos[0], data['y'] + ldPos[1]))

    mapdatas[file] = enemys
    return enemys

def unload(file):
    global mapdatas
    if file in mapdatas:
        del mapdatas[file]
