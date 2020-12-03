from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# can not handle |points|>2000 interactively. 
n = 1000

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# mesh = Poly3DCollection(vertices[model.faces], alpha=0.1)
# face_color = (1.0, 1.0, 0.9)
# edge_color = (0, 0, 0)
# mesh.set_edgecolor(edge_color)
# mesh.set_facecolor(face_color)
# ax.add_collection3d(mesh)

# ax.scatter(joints[:, 0], joints[:, 1], joints[:, 2], color='r')

# if plot_joints:
#     ax.scatter(joints[:, 0], joints[:, 1], joints[:, 2], alpha=0.1)
# plt.show()