import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')  #set video codecs using fourcc
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480)) #four arguements in total filename, codec, framerate , pixels

print(cap.isOpened())
while(cap.isOpened()):   #check for if frame is opened 
    ret, frame = cap.read()
    if ret == True:
       print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  #get frame height and width
       print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

       out.write(frame)  #same as dev.off() write file in frames

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #convert original frame filter to Grey Scale
       cv2.imshow('frame', gray)

       if cv2.waitKey(1) & 0xFF == ord('q'): #wait for key q to be pressed
         break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()