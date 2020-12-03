import trimesh
import pyrender
tm = trimesh.load('data/fuze.obj')#chairA
pyrender.Scene.from_trimesh_scene(tm)
pyrender.Viewer(tm, use_raymond_lighting=True)

tm = trimesh.load('data/chairA.obj')#
mesh = pyrender.Mesh.from_trimesh(tm)
scene = pyrender.Scene()
scene.add(mesh)
pyrender.Viewer(scene, use_raymond_lighting=True)