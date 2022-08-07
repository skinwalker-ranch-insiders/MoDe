import cv2

def draw(frame, contour, cnum):
    if cv2.contourArea(contour) < cnum:
        pass
    status = 1
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)