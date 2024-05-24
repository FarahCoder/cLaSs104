import cv2

img = cv2.imread("Poster.jpg")

rocket = img[120:360,400:500]

#Second rocket:

#img[0:240, 500:600] = rocket

text_to_show = "I love coding!"

cv2.putText(img, 
            text_to_show,
            (20, 220),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(0,0,225)
           )
cv2.imshow("Output",img)

cv2.waitKey(0)