import cv2 as cv

# GRAB EVERY n frames, making the framerate 1/n of the original
n = 4
# Video name
vidname = "video.MOV"
vid = cv.VideoCapture(vidname)
if not vid.isOpened():
    print("Error with input")
    exit(0)
frame_width = int(vid.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(vid.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(vid.get(cv.CAP_PROP_FPS) / n)
# Output
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, fps, (frame_width, frame_height))
counter = n
while vid.isOpened():
    ret, frame = vid.read()
    if ret:
        if (counter == n):
            counter = 0
            out.write(frame)
            cv.imshow('Frame', frame)
        counter += 1
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
vid.release()
out.release()
cv.destroyAllWindows()
