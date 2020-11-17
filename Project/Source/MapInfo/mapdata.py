import json

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

def loadDataPos(file, ldPos):
    global mapdatas
    if file in mapdatas:
        return mapdatas[file]

    with open(file, 'r') as f:
        dataList = json.load(f)

    print('%s load complete' % file)

    dataPos = []

    for data in dataList:
        dataPos.append((data['px'] + ldPos[0], data['py'] + ldPos[1], data['by'] + ldPos[0]))

    mapdatas[file] = dataPos

    return dataPos


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
        enemys.append((data['name'], data['x'] + ldPos[0], data['y'] + ldPos[1], data['left']))

    mapdatas[file] = enemys
    return enemys

def unload(file):
    global mapdatas
    if file in mapdatas:
        del mapdatas[file]
