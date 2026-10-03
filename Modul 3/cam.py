import cv2
cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    cv2.imshow('my cam', frame)
    cv2.waitKey(1)

# etar maddhome ami amr video camera automatic on kore amr video capture korte parbo