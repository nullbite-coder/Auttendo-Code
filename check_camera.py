def camer(input_cam):
    import cv2

    # Loading the face cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    icam = input_cam
    cap = cv2.VideoCapture(icam)

    while True:
        _, img = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(
            gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)

        cv2.imshow('Webcam Check', img)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
