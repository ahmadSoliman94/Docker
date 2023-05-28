import numpy as np
from matplotlib import pyplot as plt

from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_ubyte, img_as_float
from skimage import io

from scipy import ndimage as nd

# 1. gaussian kernel: 
# def gaussian_kernel(size, size_y=None):
#     size = int(size) # size of the kernel
#     if not size_y: # if size_y is not given, then size_y = size
#         size_y = size
#     else:
#         size_y = int(size_y) 
#     x, y = numpy.mgrid[-size:size+1, -size_y:size_y+1] # create a 2D grid
#     g = numpy.exp(-(x**2/float(size)+y**2/float(size_y))) # that is the equation of a gaussian.
#     return g / g.sum() # normalize the kernel.


# gaussian_kernel_array = gaussian_kernel(3)
# print(gaussian_kernel_array)
# plt.imshow(gaussian_kernel_array, cmap=plt.get_cmap('jet'), interpolation='nearest') # 'jet' is the color map , 'nearest' is the interpolation method.  nearest uses the nearest pixel value.
# plt.colorbar()
# plt.show()

#################################################################

# Denoising filters:

img = img_as_float(io.imread("./monalisa_noisy.jpg")) # read the image and convert it to float.

# 1. gaussian filter:
# gaussian_img = nd.gaussian_filter(img, sigma=3) # apply gaussian filter to the image. sigma is the standard deviation of the gaussian kernel.
# plt.imsave(img_path + "denoising/gaussian.jpg", gaussian_img)

# 2. median filter:
# median_img = nd.median_filter(img, size=3) # apply median filter to the image. size is the size of the kernel.
# plt.imsave(img_path + "denoising/median.jpg", median_img)


# Non-local means filters:

sigma_est = np.mean(estimate_sigma(img,channel_axis=-1)) # estimate the standard deviation of the noise.

patch_kw = dict(patch_size=6,      # patch size: 5x5 means 25 pixels, patch_distance=3 means that the search area is 3x3 patches, channel_axis=-1 means that the color channel is the last axis.
                patch_distance=4,  
                channel_axis=-1)

denoise_img = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=False,
                               patch_size=5, patch_distance=3,channel_axis=-1) 
"""
denoise_img = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=False,
                           **patch_kw)
"""
denoise_img_as_8byte = img_as_ubyte(denoise_img) # convert the image to 8-bit unsigned integer.

plt.imshow(denoise_img)
#plt.imshow(denoise_img_as_8byte, cmap=plt.cm.gray, interpolation='nearest')
plt.show()
plt.imsave("./NLM.jpg",denoise_img) 