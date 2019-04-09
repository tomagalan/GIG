import bpy
import math

pool_length = 100
unit_size = 0.2

def create_unit(x):
    bpy.ops.mesh.primitive_cube_add(radius = unit_size/2, location=(unit_size*x, 0, 0))
    bpy.context.scene.objects.active.scale = (1, 30, 1)
    return bpy.context.selected_objects[0]

def create_board1():
    bpy.ops.mesh.primitive_cube_add(radius = unit_size, location=(5, 0, 0))
    bpy.context.scene.objects.active.scale = (18, 4, 0.5)
    return bpy.context.selected_objects[0]

def create_board2():
    bpy.ops.mesh.primitive_cube_add(radius = unit_size, location=(5, 0, 0))
    bpy.context.scene.objects.active.scale = (18, 4, 0.5)
    bpy.context.scene.objects.active.rotation_euler[1] = math.pi / 4
    return bpy.context.selected_objects[0]

def create_board3():
    bpy.ops.mesh.primitive_cube_add(radius = unit_size, location=(5, 0, 0))
    bpy.context.scene.objects.active.scale = (18, 4, 0.5)
    bpy.context.scene.objects.active.rotation_euler[1] = math.pi / 2
    return bpy.context.selected_objects[0]

def create_board4(): 
    bpy.ops.mesh.primitive_cube_add(radius = unit_size, location=(5, 0, 0))
    bpy.context.scene.objects.active.scale = (18, 4, 0.5)
    bpy.context.scene.objects.active.rotation_euler[1] = 3 * math.pi / 4
    return bpy.context.selected_objects[0]

def create_torus1():
    bpy.ops.mesh.primitive_torus_add(major_radius = 12 * unit_size, minor_radius = 1 * unit_size, location=(5, 0, 0))
    bpy.context.scene.objects.active.scale = (1, 1, 4)
    bpy.context.scene.objects.active.rotation_euler[0] = math.pi / 2
    return bpy.context.selected_objects[0]

def create_torus2():
    bpy.ops.mesh.primitive_torus_add(major_radius = 7 * unit_size, minor_radius = 1 * unit_size, location=(5, 0, 0))
    bpy.context.scene.objects.active.scale = (1, 1, 4)
    bpy.context.scene.objects.active.rotation_euler[0] = math.pi / 2
    return bpy.context.selected_objects[0]

def create_house():
    bpy.ops.mesh.primitive_cube_add(radius = unit_size*12, location=(5, 4, 0))
    bpy.context.scene.objects.active.scale = (2, 1, 1)
    
def create_axe():
    bpy.ops.mesh.primitive_cylinder_add(radius = 0.2, location=(5, 1, 0))
    bpy.context.scene.objects.active.scale = (1, 1, 2)
    bpy.context.scene.objects.active.rotation_euler[0] = math.pi / 2
    return bpy.context.selected_objects[0]
   
def waves(t):
    for x in range(0, pool_length):
        pool[x].location.z = math.sin(t+x*unit_size) - 1
        pool[x].keyframe_insert(data_path="location", frame=t)
        board1.rotation_euler[1] += t
        board1.keyframe_insert(data_path="rotation_euler", frame=t)
        board2.rotation_euler[1] += t
        board2.keyframe_insert(data_path="rotation_euler", frame=t)
        board3.rotation_euler[1] += t
        board3.keyframe_insert(data_path="rotation_euler", frame=t)
        board4.rotation_euler[1] += t
        board4.keyframe_insert(data_path="rotation_euler", frame=t)

pool = [create_unit(x) for x in range(0, pool_length)]

board1 = create_board1()
board2 = create_board2()
board3 = create_board3()
board4 = create_board4()
torus1 = create_torus1()
torus2 = create_torus2()
axe = create_axe()
create_house()


for t in range (0, 100):
    waves(t)