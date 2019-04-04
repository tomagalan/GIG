import bpy
import mathutils
import math

# Construire une liste des voisins de chaque face
def buildFaceAdjacency(obj):
    dic = {}
    for p in obj.data.polygons:
        for ek in p.edge_keys:
            if ek not in dic:
                dic[ek] = []
            dic[ek].append(p.index)
    dicF = {}
    for k in dic.keys():
        if len(dic[k]) == 2:
            if dic[k][0] not in dicF:
                dicF[dic[k][0]] = []
            if dic[k][1] not in dicF[dic[k][0]]:
                dicF[dic[k][0]].append(dic[k][1])
            if dic[k][1] not in dicF:
                dicF[dic[k][1]] = []
            if dic[k][0] not in dicF[dic[k][1]]:
                dicF[dic[k][1]].append(dic[k][0])
    return dicF

# Ajouter des nouvelles couleurs
def newColor(col, name):
    mat = bpy.data.materials.get(name)
    if mat == None:
        mat = bpy.data.materials.new(name)
    mat.diffuse_color = col

# Donner une couleur à une face spécifique (mode OBJECT)
def setColor(obj, idFace, color):
    if color not in obj.data.materials:
        obj.data.materials.append(bpy.data.materials[color])
    obj.data.polygons[idFace].material_index = obj.data.materials.find(color)

# Donner une couleur à tout un objet (mode OBJECT)
def setColorAll(obj, color):
    if color not in obj.data.materials:
        obj.data.materials.append(bpy.data.materials[color])
    indexMat = obj.data.materials.find(color)
    for p in obj.data.polygons:
        obj.data.polygons[p.index].material_index = indexMat

# Calculer l'angle entre 2 normales
def angle(face1, face2):
    return -mathutils.geometry.distance_point_to_plane(face2.center, face1.center, face1.normal)

####################################################################################


# On récupère notre objet
monObj = bpy.context.scene.objects['gargoyle.002']
    
# Nouvelles couleurs
newColor((1,1,1), "blanc")
newColor((1,0,0), "rouge")
newColor((1,1,0), "jaune")
newColor((0,1,1), "cyan")
newColor((0,0,1), "bleu")


# On colore toutes les faces en blanc
setColorAll(monObj, "blanc")

# On construit le dictionnaire des voisins
FA = buildFaceAdjacency(monObj)

# Parcours des faces de l'objet
for face in monObj.data.polygons:
    count = 0;
    for neigh in FA[face.index]:
        if angle(face, monObj.data.polygons[neigh]) < 0:
            count -= 1
        elif angle(face, monObj.data.polygons[neigh]) > 0:
            count += 1
    if count == -3:
        setColor(monObj, face.index, "bleu")
    elif count == -1:
        setColor(monObj, face.index, "cyan")
    elif count == 1:
        setColor(monObj, face.index, "jaune")
    elif count == 3:
        setColor(monObj, face.index, "rouge") 
        