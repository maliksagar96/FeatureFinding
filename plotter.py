import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import tiff_file
from bpass import bpass
import sys

coord_all = np.load('fov0/feat62.npy')

coord = coord_all[np.where(coord_all[:,5]==110)]		#Separating out 0th frame data

# coord = np.load('lp.npy')

x = np.array(coord[:,0])
y = np.array(coord[:,1])

image0 = tiff_file.imread('200Frames.tif')

image = image0[110,:,:]

image = np.transpose(image,(1,0))

fig = plt.figure()
implot=plt.imshow(image,'gray',interpolation='none',origin='lower')
n = plt.plot(y,x,'go',markeredgecolor='b',markersize=1,label='Weeks')
plt.show()
# plt.savefig(sys.argv[1])

