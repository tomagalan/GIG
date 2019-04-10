import bpy
import math

pool_length = 100
unit_size = 0.2

def newColor(col, name):
    mat = bpy.data.materials.get(name)
    if mat == None:
        mat = bpy.data.materials.new(name)
    mat.diffuse_color = col

def cleanAll():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def create_unit(x):
    bpy.ops.mesh.primitive_cube_add(radius = unit_size/2, location=(unit_size*x-10, 0, 0))
    bpy.context.scene.objects.active.scale = (1, 100, 1)
    return bpy.context.selected_objects[0]

def create_wheel(x,y,z):
    angle = 0
    objects = []
    for _ in range(0,4):
        objects.append(create_board(x,y,z,angle))
        angle += math.pi / 4
    objects.append(create_torus(x,y,z,12))
    objects.append(create_torus(x,y,z,7))
    return objects
        
def create_board(x,y,z,angle):
    bpy.ops.mesh.primitive_cube_add(radius = unit_size, location=(x, y, z))
    bpy.context.scene.objects.active.scale = (18, 4, 0.5)
    bpy.context.scene.objects.active.rotation_euler[1] = angle
    return bpy.context.selected_objects[0]

def create_torus(x,y,z,size):
    bpy.ops.mesh.primitive_torus_add(major_radius = size * unit_size, minor_radius = 1 * unit_size, location=(x, y, z))
    bpy.context.scene.objects.active.scale = (1, 1, 4)
    bpy.context.scene.objects.active.rotation_euler[0] = math.pi / 2
    return bpy.context.selected_objects[0]

def create_house():
    bpy.ops.mesh.primitive_cube_add(radius = unit_size*12, location=(0, 0, 0))
    bpy.context.scene.objects.active.scale = (2, 1, 1)
    
def create_axe():
    bpy.ops.mesh.primitive_cylinder_add(radius = 0.2, location=(0, 0, 0))
    bpy.context.scene.objects.active.scale = (1, 1, 5)
    bpy.context.scene.objects.active.rotation_euler[0] = math.pi / 2
    return bpy.context.selected_objects[0]
   
def waves(t, frame):
    axe.rotation_euler[1] = t
    for x in range(0, pool_length):
        pool[x].location.z = math.sin(t + x * unit_size) - 1
        pool[x].keyframe_insert(data_path="location", frame=frame)     
    for i in range(0,6):
        if(i < 4):
            t += math.pi / 4
        wheel1[i].rotation_euler[1] = t
        wheel2[i].rotation_euler[1] = t
        wheel1[i].keyframe_insert(data_path="rotation_euler", frame=frame)
        wheel2[i].keyframe_insert(data_path="rotation_euler", frame=frame)

def create_hull(taillehull):
    sommets_hull = [(0.0, taillehull/1.5, -taillehull/6), (taillehull/4, 0.0, -taillehull/6), (0.0, -taillehull/1.5, -taillehull/6), (-taillehull/4, 0.0, -taillehull/6),
    (0.0, taillehull/1.5, taillehull/6), (taillehull/4, 0.0, taillehull/6), (0.0, -taillehull/1.5, taillehull/6), (-taillehull/4, 0.0, taillehull/6)]
    faces_hull = [(0,1,2,3), (1,5,6,2), (0,4,5,1), (3,7,4,0), (2,6,7,3), (4,5,6,7)]

    mesh_hull = bpy.data.meshes.new("mesh_hull")
    mesh_hull.from_pydata(sommets_hull, [], faces_hull)
    obj = bpy.data.objects.new("hull", mesh_hull)
    bpy.context.scene.objects.link(obj)
    obj.rotation_euler[2] = math.pi / 2

cleanAll()
pool = [create_unit(x) for x in range(0, pool_length)]
wheel1 = create_wheel(0,4,0)
wheel2 = create_wheel(0,-4,0)
axe = create_axe()
create_hull(10)

for time in range(0,200):
    # modifier = math.sin((time/100)*(math.pi/2))
    waves(0.1 * time, time)