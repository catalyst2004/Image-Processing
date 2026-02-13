import cv2 as cv # to import the opencv module 
img = cv.imread("img_1") # to read the image from the specified location
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) #to convert the image into grayscale
cv.imshow("Window_is_Open",gray) #to show the image 
h,w,c = img.shape #to find the image size and channels
print("The details o fthe image is as:\n") 
print(f"\nHeight: {h}\n Width: {w}\n Channel: {c}\n")
cv.waitKey(0) #to hold the output on the screen until any key is pressed.
cv.destroyAllWindows() # to destroy all the open windows on the panel.



