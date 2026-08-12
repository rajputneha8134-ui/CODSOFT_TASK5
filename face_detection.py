import cv2


def main():
    print("=" * 50)
    print("        👤 FACE DETECTION SYSTEM")
    print("=" * 50)

    # Load pre-trained Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    # Open webcam
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("❌ Unable to access the webcam.")
        return

    print("✅ Camera started successfully.")
    print("Press 'q' to exit.")

    while True:

        # Read frame from webcam
        success, frame = camera.read()

        if not success:
            print("❌ Unable to read camera frame.")
            break

        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        # Detect faces
        faces = face_cascade.detectMultiScale(
            gray_frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(50, 50)
        )

        # Draw rectangle around each detected face
        for (x, y, width, height) in faces:

            cv2.rectangle(
                frame,
                (x, y),
                (x + width, y + height),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "Face Detected",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        # Display number of detected faces
        cv2.putText(
            frame,
            f"Faces: {len(faces)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # Display webcam
        cv2.imshow(
            "Face Detection - Press Q to Exit",
            frame
        )

        # Exit when Q is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    camera.release()
    cv2.destroyAllWindows()

    print("Camera closed.")
    print("Thank you for using Face Detection System!")


if __name__ == "__main__":
    main()