import cv2

frameWidth = 640
frameHeight = 480
haarcascadesPath = "Resources/haarcascades/haarcascade_russian_plate_number.xml"
nPlateCascade = cv2.CascadeClassifier(haarcascadesPath)
minArea = 200
color = (255, 0, 255)
videoPath = "Resources/numberPlate.mp4"
cap = cv2.VideoCapture(videoPath) # webcam = 0
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
# cap.set if using webcam
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlate = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
    for (x, y, w, h) in numberPlate:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255,255,0), 2)
            cv2.putText(img, 'NumberPlate', (x, y-5), cv2.FONT_ITALIC, 1, color, 2)
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow('Plate', imgRoi)
    cv2.imshow('Result', img)
    if cv2.waitKey(1) & 0xFF == ord('s'): # press to save
        cv2.imshow('Result', img)
        cv2.imwrite('Resources/Scanned/NoPlate_' + str(count) + '.jpg', imgRoi)
        cv2.rectangle(img, (0, 0), (270, 80), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, 'SAVED', (20, 50), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)
        cv2.waitKey(500)
        count += 1

