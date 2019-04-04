import bpy
import mathutils
import math

# permet de construire une liste des voisins de chaque face
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

# pour rajouter des nouvelles couleurs
def newColor(col, name):
    mat = bpy.data.materials.get(name)
    if mat == None:
        mat = bpy.data.materials.new(name)
    mat.diffuse_color = col

# pour donner une couleur à une face spécifique
# ATTENTION blender doit être en mode OBJECT lors 
# de l'appel pour que cette fonction marche
def setColor(obj, idFace, color):
    if color not in obj.data.materials:
        obj.data.materials.append(bpy.data.materials[color])
    obj.data.polygons[idFace].material_index = obj.data.materials.find(color)

# pour donner une couleur à tout un objet
# ATTENTION blender doit être en mode OBJECT lors 
# de l'appel pour que cette fonction marche
def setColorAll(obj, color):
    if color not in obj.data.materials:
        obj.data.materials.append(bpy.data.materials[color])
    indexMat = obj.data.materials.find(color)
    for p in obj.data.polygons:
        obj.data.polygons[p.index].material_index = indexMat

# pour récupérer les faces sélectionnées
# ATTENTION blender doit être en mode OBJECT lors 
# de l'appel pour que cette fonction marche
def getSelectedFacesID(obj):
    selfaces = []
    for f in obj.data.polygons:
        if f.select:
            selfaces.append(f.index)
    return selfaces

# calcule l'angle entre 2 normales
def angle(n1, n2):
    angle = n1.angle(n2) * 180 / math.pi
    return math.fabs(angle)


####################################################################################


# on fait les traitement en mode OBJECT
editmode = False
if bpy.context.active_object.mode == 'EDIT':
    editmode = True
    bpy.ops.object.mode_set(mode = 'OBJECT')
    
# quelques nouvelles couleurs
newColor((1,1,1), "blanc")
newColor((1,0,0), "rouge")
newColor((1,1,0), "jaune")

# on récupère notre objet
monObj = bpy.context.scene.objects['bunnyLowPoly']

# on colore toutes les faces en blanc
setColorAll(monObj, "blanc")

# liste des faces sélectionnées
curSel = getSelectedFacesID(monObj)

# angle max entre 2 faces (en degrés)
maxAngle = 17

# faces déjà colorées
checkedFaces = []

while curSel:
    
    #Liste temporaire qui contiendra les nouvelles faces de départ
    curSelTemp = []
    
    # on récupère la liste des faces sélectionnées, 
    # et on les set en rouge 
    for s in curSel:
        setColor(monObj, s, "rouge")

    # on construit la liste de tous les voisinages
    FA = buildFaceAdjacency(monObj)
    for s in curSel:
        for v in FA[s]:
            if angle(monObj.data.polygons[s].normal, monObj.data.polygons[v].normal) <= maxAngle and v not in checkedFaces:
                setColor(monObj, v, "rouge")
                checkedFaces.append(v)
                curSelTemp.append(v)
            
    # on définit les prochaines faces de départ pour le prochain tour de boucle
    curSel = curSelTemp

# on repasse dans le mode d'origine
if editmode:
    bpy.ops.object.mode_set(mode = 'EDIT')