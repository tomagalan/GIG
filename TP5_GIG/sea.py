# Ajouter des primites simples
import bpy  

pool_width = 10
pool_height = 10
pool_depth = 10
voxel_size = 0.2

def create_voxel(x, y, z):
    # ajouter un carré
    bpy.ops.mesh.primitive_cube_add(radius=voxel_size, location=(voxel_size*2*x, voxel_size*2*y, voxel_size*2*z))
    return bpy.context.selected_objects[0]

def get_voxel(x,y,z):
    return pool[x][y][z]

def create_pool():
    for x in range(0, pool_width):
        for y in range(0, pool_height):
            for z in range(0,pool_depth):
                pool[x][y][z] = create_voxel(x,y,z)
                
pool = [[[create_voxel(x,y,z) for z in range(0, pool_depth)] for y in range(0, pool_height)] for x in range(0, pool_width)]

    
#create_pool()