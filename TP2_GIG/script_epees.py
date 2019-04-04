import bpy  

# ***** Déclaration des fonctions *****
# fonction pour générer un maillage et l'ajouter à la scène
def buildMesh(sommets, faces, nom):
    # création du mesh
    mesh_data = bpy.data.meshes.new(nom)
    mesh_data.from_pydata(sommets, [], faces)
    # création de l'objet contenant le mesh, et ajout à la scène
    obj = bpy.data.objects.new("My_Object", mesh_data)
    bpy.context.scene.objects.link(obj)

# fonction pour supprimer de la scène tous les éléments
#def cleanAll():
    #bpy.ops.object.select_all(action='SELECT')
    #bpy.ops.object.delete(use_global=False)

# notre fonction pour générer des épées
def genererEpee(longueurlame, largeurlame, longueurmanche, taillepommeau, taillegarde, sillon):
    
    #Profondeur selon x ou y du sillon éventuel
    dx = largeurlame/10
    dy = largeurlame/10
    
    #Ratio largeur/épaisseur de la lame
    ratio = 4
    
    # Lame simple (sans sillon) : base = losange, hauteur = "longueurlame", largeur (selon y) = "largeurlame"
    if(sillon == 0):
        sommets_lame = [(0.0, largeurlame, 0.0), (largeurlame/8, 0.0, 0.0), (0.0, -largeurlame, 0.0), (-largeurlame/8, 0.0, 0.0),
        (0.0, largeurlame, longueurlame), (largeurlame/8, 0.0, longueurlame), (0.0, -largeurlame, longueurlame), (-largeurlame/8, 0.0, longueurlame), (0.0, 0.0, longueurlame + longueurlame/10)]
        faces_lame = [(0,1,2,3), (1,5,6,2), (0,4,5,1), (3,7,4,0), (2,6,7,3), (5,8,6), (4,8,5), (7,8,4), (6,8,7)]
    
    else:
    # Lame avec sillon : ajout d'un sillon de largeur 2*dy et de profondeur dx
        sommets_lame = [(0.0, largeurlame, 0.0), (largeurlame/ratio-dx, dy, 0.0), (largeurlame/ratio-2*dx, 0.0, 0.0), (largeurlame/ratio-dx, -dy, 0.0), 
        (0.0, -largeurlame, 0.0), (-largeurlame/ratio+dx, -dy, 0.0), (-largeurlame/ratio+2*dx, 0.0, 0.0), (-largeurlame/ratio+dx, dy, 0.0),
        (0.0, largeurlame, longueurlame), (largeurlame/ratio-dx, dy, longueurlame), (largeurlame/ratio-2*dx, 0.0, longueurlame), (largeurlame/ratio-dx, -dy, longueurlame),
        (0.0, -largeurlame, longueurlame), (-largeurlame/ratio+dx, -dy, longueurlame), (-largeurlame/ratio+2*dx, 0.0, longueurlame), (-largeurlame/ratio+dx, dy, longueurlame),
        (0.0, 0.0, longueurlame + longueurlame/10)]
        faces_lame = [(0,8,9,1), (1,9,10,2), (2,10,11,3), (3,11,12,4),
        (12,13,5,4), (13,14,6,5), (14,15,7,6), (15,8,0,7),
        (0,1,2,3,4,5,6,7), (8,16,9), (9,16,10), (10,16,11),
        (11,16,12), (12,16,13), (13,16,14), (14,16,15), (15,16,8)]
    
    # Garde : losange de largeur "taillegarde" (selon y), d'épaisseur "taillegarde"/6
    sommets_garde = [(0.0, taillegarde, 0.0), (taillegarde/6, 0.0, 0.0), (0.0, -taillegarde, 0.0), (-taillegarde/6, 0.0, 0.0),
    (0.0, taillegarde, taillegarde/8), (taillegarde/6, 0.0, taillegarde/8), (0.0, -taillegarde, taillegarde/8), (-taillegarde/6, 0.0, taillegarde/8)]
    faces_garde = [(0,1,2,3), (1,5,6,2), (0,4,5,1), (3,7,4,0), (2,6,7,3), (4,5,6,7)]
    
    # Manche : cylindre de hauteur "longueurmanche" et de rayon 0,1
    bpy.ops.mesh.primitive_cylinder_add(radius=0.1, depth=longueurmanche, location=(0.0, 0.0, -longueurmanche/2.0))
    
    # Pommeau de taille "taillepommeau"
    bpy.ops.mesh.primitive_uv_sphere_add(size=taillepommeau, location=(0.0, 0.0, -longueurmanche))
    
    # création du mesh lame
    mesh_lame = bpy.data.meshes.new("mesh_lame")
    mesh_lame.from_pydata(sommets_lame, [], faces_lame)

    # création de l'objet contenant le mesh lame, et ajout à la scène
    obj = bpy.data.objects.new("Lame", mesh_lame)
    bpy.context.scene.objects.link(obj)
    
    # création du mesh garde
    mesh_garde = bpy.data.meshes.new("mesh_garde")
    mesh_garde.from_pydata(sommets_garde, [], faces_garde)

    # création de l'objet contenant le mesh garde, et ajout à la scène
    obj = bpy.data.objects.new("Garde", mesh_garde)
    bpy.context.scene.objects.link(obj)

# ***** Programme principal *****
#cleanAll()

# Dernier parametre : 0 = sans sillon, 1 = avec sillon
genererEpee(7, 0.4, 1.5, 0.10, 1, 1) # un exemple d'épée

# force l'affichage des ID des faces/edges/verts dans l'interface Blender
bpy.app.debug = True
bpy.context.object.data.show_extra_indices = True 