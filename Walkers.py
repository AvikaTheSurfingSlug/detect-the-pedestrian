import cv2
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Create our body classifier


# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    bodys = body_classifier.detectMultiScale(gray, 1.2, 3)
    # Extract bounding boxes for any bodies identified
for (x, y, w, h) in bodys:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
    cv2.imshow('Pedestrians.', frame)
    if cv2.waitKey(1) == 32:
        break

cap.release()
cv2.destroyAllWindows()
