import bpy
import math

pool_length = 50
unit_size = 0.2

def create_unit(x):
    bpy.ops.mesh.primitive_cube_add(radius = unit_size, location=(unit_size*2*x, 0, 0))
    bpy.context.scene.objects.active.scale = (1, 30, 1)
    return bpy.context.selected_objects[0]

def create_boat(x):
    bpy.ops.mesh.primitive_cube_add(radius = unit_size, location=(unit_size*pool_length*x, 0, 0))
    bpy.context.scene.objects.active.scale = (10, 10, 2)
    return bpy.context.selected_objects[0]

def waves(t):
    for x in range(0, pool_length):
        pool[x].location.z = math.sin(t+x*2*unit_size)
        pool[x].keyframe_insert(data_path="location", frame=t)
        boat.rotation_euler[1] = t
        boat.keyframe_insert(data_path="rotation_euler", frame=t)

pool = [create_unit(x) for x in range(0, pool_length)]

boat = create_boat(0)

for t in range (0, 100):
    waves(t)