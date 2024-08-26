import cv2

img = cv2.imread('profile.png')
# import pdb; pdb.set_trace()
H, W, _ = img.shape
crop_img = img[0:W, 0:W]

cv2.imwrite('profile2.png', crop_img)
