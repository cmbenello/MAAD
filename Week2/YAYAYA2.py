import cv2
import numpy as np
import random

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
combination_list = [['eren','doggy'],['imposter','winky'],['licky','whirl']]

choice = 2
video1 = 'Gifs/' + combination_list[choice][0] + '.gif'
video2 = 'Gifs/' + combination_list[choice][1] + '.gif'
title = combination_list[choice][0] + " + " + combination_list[choice][1]
cap = cv2.VideoCapture(video1)
cap2 = cv2.VideoCapture(video2)
frame = cap.read()[1]

width, height = len(frame[0]), len(frame)
size_act = (width, height)
size_full = (3224,1964)

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  ret2, frame2 = cap2.read()

  if ret == True and ret2 == True:

    parity = random.randint(1,6)
    # Display the resulting frame
    for x in range(len(frame)):
        for y in range(len(frame[0])):
            if x % parity == 0 and y % parity == 0:
                frame[x][y] = frame2[x][y]
    resized = cv2.resize(frame, size_full)
    cv2.imshow(title,resized)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  elif not ret:
      cap = cv2.VideoCapture(video1)
  elif not ret2:
      cap2 = cv2.VideoCapture(video2)
  #else: # use break to only play once
    #cap = cv2.VideoCapture(video)
    #break


# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
