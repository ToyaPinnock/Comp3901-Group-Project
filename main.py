import cv2



# Opencv DNN, dnn_model has a wide variety of pre-trained object identifier
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)

# Accept users input
searchFor = input("Enter object to be found: ")

# shrink the image received from the camera
model.setInputParams(size=(320, 320), scale=1/255)
# Load class lists
classes = []
with open("dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)
#print("Object list")
#print(classes)

# initialize camera
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
height,width,_ = frame.shape #obtain width of frame

imgCenter = int(width/2) #obtain the center of the frame by dividing the width by 2

centerCheck = imgCenter *.30
leftCheck = imgCenter - centerCheck
rightCheck = imgCenter+centerCheck

print('Shape',width,height)
print('Center left right',imgCenter, leftCheck, rightCheck)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # object detection
    (class_ids, scores, bboxes) = model.detect(frame)
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        class_name = classes[class_id]
        # print(x, y, w, h)
        #print(class_id)
        # If object user intends to find is same as the one detected, class name will be printed
        if class_name == searchFor:
            if (x<leftCheck):
                print("On The Left")
            elif (x>rightCheck):
                print("On The Right")
            else:
                print("In Center")
            cv2.putText(frame, class_name + "found", (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (200, 0, 50), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 0, 50), 3)
        else:
            # If not found continue the search
            cv2.putText(frame, "Continue Searching", (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (200, 0, 50), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 0, 50), 3)

    #print("class ids", class_ids)
    #print("scores", scores)
    #print("bboxes", bboxes)

    # Display frame
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
