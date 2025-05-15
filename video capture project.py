import cv2
cap = cv2.VideoCapture(0)
frame_count = 0
fps =int(input("donner le nombre de frame"))
save_interval = fps * 2
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Camera Feed', frame)
    if frame_count % save_interval == 0:
        frame_name = f"frame_{frame_count}.jpg"
        cv2.imwrite(frame_name, frame)
        print(f"Saved: {frame_name}")
    frame_count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()