import cv2 as cv
import os
import uuid

def get_image():
    CLASS_NAME = 'none'

    if not os.path.exists(CLASS_NAME):
        os.mkdir(CLASS_NAME)
    

    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
        
    i = 0    
    
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame. Exiting ...")
            break
        
        file_name = f'{str(uuid.uuid4())}.jpg'
        file_path = os.path.join(CLASS_NAME, file_name)
        
        i+= 1
        if i % 10 == 0:
            cv.imwrite(file_path, frame)
      
        cv.imshow('frame', frame)
        
        if cv.waitKey(1) == ord('q') or i > 500:
            break
  
    cap.release()
    cv.destroyAllWindows()
    
    
if __name__ == "__main__":
   get_image()