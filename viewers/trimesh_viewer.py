# trimesh does not support animation
# jjcao

import trimesh
import numpy as np

# tmp = trimesh.available_formats()
# tm = trimesh.load('data/chairA.obj', process=False)
# pcd = tm.vertices

pcd = trimesh.load('data/anchor_33_denoise.xyz', process=False)
pcd.colors = np.ones([pcd.shape[0], 4]) * [0.9, 0.0, 0.0, 0.99]
scene = pcd.scene()
#scene.add_geometry(samples)
scene.show()

try:
    # increment the file name
    file_name = 'render_' + '.png'
    # save a render of the object as a png
    png = scene.save_image(resolution=[800, 600],visible=True)
    with open(file_name, 'wb') as f:
        f.write(png)
        f.close()

except BaseException as E:
    print("unable to save image", str(E))
