import cv2

def display_status(frame, gnum, cnum, dnum):
    font = cv2.FONT_HERSHEY_DUPLEX
    # org
    g_org = (1, 60)
    d_org = (1, 90)
    c_org = (1, 120)
    
    # fontScale
    fontScale = 1
    # Blue color in BGR
    color = (255, 0, 0)
    # Line thickness of 1 px
    thickness = 1

    #Using cv2.putText() method
    frame = cv2.putText(frame, "gGaussianBlur:" + str(gnum), 
                       g_org, font, fontScale, color, thickness, cv2.LINE_AA)
    frame = cv2.putText(frame, "<cC>ontourArea:" + str(cnum), 
                       c_org, font, fontScale, color, thickness, cv2.LINE_AA)
    frame = cv2.putText(frame, "dDelta:" + str(dnum), 
                       d_org, font, fontScale, color, thickness, cv2.LINE_AA)
