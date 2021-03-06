import cv2 

VID = cv2.VideoCapture(0)

def __main__(camara = 0):
    if camara != 0:
        VID = cv2.VideoCapture(camara)
    while(1):
        
        # Capture the video frame
        # by frame
        ret, frame = VID.read()



        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    VID.release()
    # Destroy all the windows
    cv2.destroyAllWindows()



    __main__()