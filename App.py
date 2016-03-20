import cv2

refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
    global refPt, cropping, image

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    elif (event == cv2.EVENT_MOUSEMOVE) & cropping:
        image = clone.copy()
        cv2.rectangle(image, refPt[0], (x,y), (255, 255, 255), 4)
        cv2.rectangle(image, refPt[0], (x,y), (0, 0, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
        cv2.imshow("image", image)
        if len(refPt) == 2:
            roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
            cv2.imshow("ROI", roi)
            cv2.waitKey(0)



image = cv2.imread("/home/ahmed/1.png")
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

cv2.destroyAllWindows()
