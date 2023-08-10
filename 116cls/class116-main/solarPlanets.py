import cv2
image=cv2.imread("solar-system.jpg")
cv2.putText(image,
            "Sun",
            (20,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255))
cv2.imshow("display image",image)
cv2.waitKey(0)