import cv2

def main():
    camera = cv2.VideoCapture(0) #build-in camera in Mac
    #camera = cv2.VideoCapture(-1) #camera in Pi?
    #camera.set(3, 640)
    #camera.set(4, 480)
    if not camera.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, image = camera.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
            
        cv2.imshow('Original', image)
        
        b_w_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('B/W', b_w_image)
        
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
    camera.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()