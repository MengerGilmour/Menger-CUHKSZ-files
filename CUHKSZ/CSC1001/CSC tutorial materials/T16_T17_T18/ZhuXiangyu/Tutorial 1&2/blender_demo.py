import bpy
import numpy as np

if 'Cube' in bpy.data.objects:
    bpy.data.objects.remove(bpy.data.objects['Cube'], do_unlink=True)

num_sample = 20
ts = (np.pi*2)* np.linspace(0, 1, num_sample)
ys = np.sin(ts)

radius = 0.3
ball_radius = radius*np.ones(num_sample)
centers = np.zeros((num_sample, 3))
centers[:, 0] = ts
centers[:, 1] = ys

for i in range(num_sample):
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=ball_radius[i], 
        location=(centers[i,0], centers[i,1], centers[i,2])
    )
