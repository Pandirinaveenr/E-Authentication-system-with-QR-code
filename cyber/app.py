

# USAGE
import numpy

import face_recognition
import cv2
import os
match=0

def predict():
   
    # Load images.
    print("[INFO] quantifying faces...")   
    image_1 = face_recognition.load_image_file("dataset/dhoni/Dh (9).jpg")
    image_1_face_encoding = face_recognition.face_encodings(image_1)[0]
        
    image_2 = face_recognition.load_image_file("dataset/modi/modi (10).jpg")
    image_2_face_encoding = face_recognition.face_encodings(image_2)[0]
    
    image_3 = face_recognition.load_image_file("dataset/yuvraj/yuvi (10).jpg")
    image_3_face_encoding = face_recognition.face_encodings(image_3)[0]
            
    image_4 = face_recognition.load_image_file("dataset/sharukh/sha (5).jpg")
    image_4_face_encoding = face_recognition.face_encodings(image_4)[0]
    
    #mypart
    image_5 = face_recognition.load_image_file("dataset/ElonMask/image19.jpeg")
    image_5_face_encoding = face_recognition.face_encodings(image_5)[0]
            
        
    # Create arrays of known face encodings and their names
    known_face_encodings = [
            
            image_1_face_encoding,
            image_2_face_encoding,
            image_3_face_encoding,
            image_4_face_encoding,
            image_5_face_encoding
            
        ]
    known_face_names = [
            
            "MS Dhoni",
            "Norendro Modi",
            "Youvraj",
            "Sharukh Khan",
            "Elon Musk"
        ]
        
    # Initializing  variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
        
    # Get a reference to webcam #0 (the default one)
    
    print("[INFO] starting video stream...")
    video_capture = cv2.VideoCapture(0)
    
    ret, frame = video_capture.read()
    
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
    # Convert the image from BGR color (which OpenCV uses) to
    #RGB color (which face_recognition uses)
    #  rgb_small_frame = small_frame[:, :, ::-1]
    rgb_small_frame = numpy.ascontiguousarray(small_frame[:, :, ::-1])
    
    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    
    face_names = []
    print("i am naresh")
    
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        global match
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        if True in matches:
            global match
            match=1
         # If a match was found in known_face_encodings, just use the first one.
    if match==1:
        print("naresh")
    else:   
        print("akbhar")

 
        
 
