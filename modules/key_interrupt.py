import cv2
import datetime
import modules.key_clip_writer as KeyClipWriter
buffer_size = 684

consecFrames = 0

def key_interrupt(status, show_status, gnum, cnum, dnum, out_dir, frame,
                 updateConsecFrames, codec, frameWidth, frameHeight, kcw):
    key = cv2.waitKey(1)

    if key == ord('Q'):
        if status == 1:
            quit()
    if key == ord('h'): 
        if status == 1 and show_status == 0:
            show_status = 1
        else:
            show_status = 0
    if key == ord('G'):
        if status == 1:
            gnum = (gnum + 2)
    if key == ord('g'):
        if status == 1:
            if gnum == 1:
                gnum = 1
            else:
                gnum = (gnum - 2)
    if key == ord('C'):
        if status == 1:
            cnum = (cnum + 1)
    if key == ord('c'):
        if status == 1:
            if cnum == 1:
                cnum = 1
            else:
                cnum = (cnum - 1)
    if key == ord('>'):
        if status == 1:
            cnum = (cnum + 200)
    if key == ord('<'):
        if status == 1:
            if cnum < 201:
                cnum = 1
            else:
                cnum = (cnum - 200)
    if key == ord('D'):
        if status == 1:
            dnum = (dnum + 1)
    if key == ord('d'):
        if status == 1:
            if dnum == 1:
                dnum = 1
            else:
                dnum = (dnum - 1)
    if key == ord('r'):
        if status == 1:
            # Reset settings
            gnum = 25
            cnum = 10000 
            dnum = 5
    if key == ord('s'):
        timestamp = datetime.datetime.now()
        img_name = "{}/{}.png".format(out_dir, 
                   timestamp.strftime("%Y%m%d-%H%M%S"))
        cv2.imwrite(img_name, frame)
        count += 1
    if key == ord('S'):
        if not kcw.recording:
            timestamp = datetime.datetime.now()
            p = "{}/{}.mp4".format(out_dir,
                timestamp.strftime("%Y%m%d-%H%M%S"))
            kcw.start(p, cv2.VideoWriter_fourcc(*codec), 20, frameWidth, frameHeight)
    if updateConsecFrames:
        consecFrames += 1
    # update the key frame clip buffer
    kcw.update(frame)
    # if we are recording and reached a threshold on consecutive
    # number of frames with no action, stop recording the clip
    if kcw.recording and consecFrames == buffer_size:
        kcw.finish()
    if key == ord('x'):
        if kcw.recording:
            kcw.finish()
    if key == ord('p'):
        cv2.waitKey(-1)