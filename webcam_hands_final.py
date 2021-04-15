#For webcam input:
import cv2
import mediapipe as mp
import os


#fonction pour afficher le rectangle
def draw_rectangle(hand_landmarks, image):
    image_height, image_width, _ = image.shape
    keypoints = []
    for data_point in hand_landmarks.landmark:
        keypoints.append({
                            'X': data_point.x*image_width,
                            'Y': data_point.y*image_height,                            
                            })
    
    X_min = image_width
    X_max = 0
    Y_min = image_height
    Y_max = 0

    #print(keypoints[0]['X'])
    for x in range(len(keypoints)):
        if (keypoints[x]['X']) < X_min:
            X_min = (keypoints[x]['X'])
        if (keypoints[x]['X']) > X_max:
            X_max = (keypoints[x]['X'])

    for y in range(len(keypoints)):
        if (keypoints[y]['Y']) < Y_min:
            Y_min = (keypoints[y]['Y'])
        if (keypoints[y]['Y']) > Y_max:
            Y_max = (keypoints[y]['Y'])

    startX = int(X_min -0.05* image_width)
    startY = int(Y_min -0.05* image_height)
    endX = int(X_max +0.05* image_width)
    endY = int(Y_max +0.05* image_height)
    rect = cv2.rectangle(image, (startX, startY), (endX, endY), (155, 255, 0), 2)
    return(rect)

#############fin de la fonction

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        image =  draw_rectangle(hand_landmarks, image)
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()