import open3d as o3d
import pyrender
import trimesh
import numpy as np

pcd_in = o3d.io.read_point_cloud("data/anchor_33_denoise.off", format='xyzn')
pts = np.asarray(pcd_in.points)
# colors do not work!
#colors = np.random.uniform(size=pts.shape)
colors = np.ones([pts.shape[0], 4]) * [0.9, 0.0, 0.0, 0.99]
pcd = pyrender.Mesh.from_points(points=pts, normals=np.asarray(pcd_in.normals), colors=colors)

scene = pyrender.Scene()
#scene.add(pcd, pose=np.eye(4))

cam = pyrender.PerspectiveCamera(yfov=np.pi / 3.0, aspectRatio=1.414)
scene.add(cam, pose=np.eye(4))
light = pyrender.PointLight(color=[1.0, 1.0, 1.0], intensity=2.0)
scene.add(light, pose=np.eye(4))


# too slow to render every point with a sphere using pyrender
sm = trimesh.creation.uv_sphere(radius=0.1)
sm.visual.vertex_colors = [1.0, 0.0, 0.0]
tfs = np.tile(np.eye(4), (len(pts), 1, 1))
tfs[:,:3,3] = pts
pts = pyrender.Mesh.from_trimesh(sm, poses=tfs)
scene.add(pts)

pyrender.Viewer(scene, use_raymond_lighting=True)

# render = pyrender.offscreen.OffscreenRenderer(800, 600, point_size=8.0)
# render.render(scene)
