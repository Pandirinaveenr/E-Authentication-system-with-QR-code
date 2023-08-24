from django.shortcuts import render
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from cyber.settings import *
from user.models import *

# import face_recognition
import cv2
cv2.useOpenVX()
import numpy
import os
from datetime import datetime
import random
import yagmail
import qrcode

global random_number
match=0

# Create your views here.
def userlogin(request):
    return render(request, 'userlogin.html')

def userhome(request):
    return render(request, 'user/userhome1.html')

def register(request):
    return render(request,'register.html')

def userregister(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        phone = request.POST.get('phonenumber')
        images = request.FILES['file']
        if not images.name.endswith('.jpg'):
            messages.error(request, 'This is not jpg file')
        fs = FileSystemStorage()
        filename= fs.save(images.name, images)
        detect_filename = fs.save(images.name, images)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        user = usermodel.objects.create(email=email, password=password, name=name, phone=phone, images=uploaded_file_url)
        messages.success(request, 'User Registered Successfully')
        return render(request, 'register.html',{})
    else:
        messages.error(request, 'User Registered Un-Successfully')
        return render(request, 'register.html')
    
def userlogincheck(request):
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     ranges = password.split(";")
    #     outputString = ""
    #     for i in range(len(ranges)):
    #         range_val = ranges[i].split(",")
    #         start = int(range_val[0])
    #         end = int(range_val[1])

    #         if start == 1 and end == 9:
    #             outputString += "A "
    #         elif start == 1 and end == 10:
    #             outputString += "I "
    #         elif start == 1 and end == 11:
    #             outputString += "Q "
    #         elif start == 1 and end == 12:
    #             outputString += "Y "
    #         elif start == 1 and end == 13:
    #             outputString += "7 "
    #         elif start == 2 and end == 9:
    #             outputString += "B "
    #         elif start == 2 and end == 10:
    #             outputString += "J "
    #         elif start == 2 and end == 11:
    #             outputString += "R "
    #         elif start == 2 and end == 12:
    #             outputString += "Z "
    #         elif start == 2 and end == 13:
    #             outputString += "8 "
    #         elif start == 3 and end == 9:
    #             outputString += "C "
    #         elif start == 3 and end == 10:
    #             outputString += "K "
    #         elif start == 3 and end == 11:
    #             outputString += "S "
    #         elif start == 3 and end == 12:
    #             outputString += "1 "
    #         elif start == 3 and end == 13:
    #             outputString += "9 "
    #         elif start == 4 and end == 9:
    #             outputString += "D "
    #         elif start == 4 and end == 10:
    #             outputString += "L "
    #         elif start == 4 and end == 11:
    #             outputString += "T "
    #         elif start == 4 and end == 12:
    #             outputString += "2 "
    #         elif start == 4 and end == 13:
    #             outputString += "0 "
    #         elif start == 5 and end == 9:
    #             outputString += "E "
    #         elif start == 5 and end == 10:
    #             outputString += "M "
    #         elif start == 5 and end == 11:
    #             outputString += "U "
    #         elif start == 5 and end == 12:
    #             outputString += "3 "
    #         elif start == 5 and end == 13:
    #             outputString += "@ "
    #         elif start == 6 and end == 9:
    #             outputString += "F "
    #         elif start == 6 and end == 10:
    #             outputString += "N "
    #         elif start == 6 and end == 11:
    #             outputString += "V "
    #         elif start == 6 and end == 12:
    #             outputString += "4 "
    #         elif start == 6 and end == 13:
    #             outputString += "- "
    #         elif start == 7 and end == 9:
    #             outputString += "G "
    #         elif start == 7 and end == 10:
    #             outputString += "O "
    #         elif start == 7 and end == 11:
    #             outputString += "W "
    #         elif start == 7 and end == 12:
    #             outputString += "5 "
    #         elif start == 7 and end == 13:
    #             outputString += "_ "
    #         elif start == 8 and end == 9:
    #             outputString += "H "
    #         elif start == 8 and end == 10:
    #             outputString += "P "
    #         elif start == 8 and end == 11:
    #             outputString += "X "
    #         elif start == 8 and end == 12:
    #             outputString += "6 "
    #         elif start == 8 and end == 13:
    #             outputString += "$ "
    #         else:
    #             outputString += "Invalid input "
    #     user = usermodel.objects.filter(email=email, password=outputString.lower())
    #     return render(request, 'user/userhome.html')
    # else:
    #     messages.error(request, 'User Login Un-Successfully')
    #     return render(request, 'userlogin.html')
    return render(request, 'user/userhome.html')
    
def userlogout(request):
    return render(request, 'user/usrfd.html')

def usrfd(request):
    return render(request, 'user/usrfd.html')

def facedetect(request):
    #     # Load images.
    # print("[INFO] quantifying faces...")   
    # image_1 = face_recognition.load_image_file("media/dataset/Akbar/pass photo.JPG")
    # image_1_face_encoding = face_recognition.face_encodings(image_1)[0]
    # print("read image successfully")
        
    # image_2 = face_recognition.load_image_file("media/dataset/Shreya A/2.jpeg")
    # image_2_face_encoding = face_recognition.face_encodings(image_2)[0]
    
    # image_3 = face_recognition.load_image_file("media/dataset/Shreya B/1.jpeg")
    # image_3_face_encoding = face_recognition.face_encodings(image_3)[0]
            
    # image_4 = face_recognition.load_image_file("media/dataset/Tejaswini/2.jpeg")
    # image_4_face_encoding = face_recognition.face_encodings(image_4)[0]
    
    # #mypart
    # image_5 = face_recognition.load_image_file("media/dataset/Tina/1.jpeg")
    # image_5_face_encoding = face_recognition.face_encodings(image_5)[0]

    # # Create arrays of known face encodings and their names
    # known_face_encodings = [
            
    #         image_1_face_encoding,
    #         image_2_face_encoding,
    #         image_3_face_encoding,
    #         image_4_face_encoding,
    #         image_5_face_encoding
            
    #     ]
    # known_face_names = [
            
    #         "Akbar",
    #         "Shreya A",
    #         "Shreya B",
    #         "Tejaswini",
    #         "Tina"
    #     ]
    # # Initializing  variables
    # face_locations = []
    # face_encodings = []
    # face_names = []
    # process_this_frame = True

    # # Get a reference to webcam #0 (the default one)
    
    # print("[INFO] starting video stream...")
    # video_capture = cv2.VideoCapture(0)
    
    # ret, frame = video_capture.read()
    
    # # Resize frame of video to 1/4 size for faster face recognition processing
    # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
    # # Convert the image from BGR color (which OpenCV uses) to
    # #RGB color (which face_recognition uses)
    # #  rgb_small_frame = small_frame[:, :, ::-1]
    # rgb_small_frame = numpy.ascontiguousarray(small_frame[:, :, ::-1])
    
    # # Only process every other frame of video to save time
    # if process_this_frame:
    #     # Find all the faces and face encodings in the current frame of video
    #     face_locations = face_recognition.face_locations(rgb_small_frame)
    #     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    
    # face_names = []
    
    # for face_encoding in face_encodings:
    #     print("hi")
    #     # See if the face is a match for the known face(s)
    #     global match
    #     matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    #     print("hi1")
    #     if True in matches:
    #         global match
    #         match=1
    #         print("hi2")
    #      # If a match was found in known_face_encodings, just use the first one.
    # if match==1:
    #     print("detect")
    #     return render(request, "user/userlogin.html")
    # else:
    #     print("not detect")
    #     return render(request, 'user/usrfd.html')
    return render(request, "user/userlogin.html")

def otpcheck(request):
    global random_number
    email = request.POST['email']
    user = usermodel.objects.filter(email=email)
    try:
        random_number = random.randint(1000, 9999)
        otpcheck.random_number= random_number
        print(random_number)
        qr_code = qrcode.make(random_number)
        qr_code_path= "media/qrcode.png"
        qr_code.save(qr_code_path)

        user = 'antishouldersurfing@gmail.com'
        app_password = 'ulppslsizblqhmds' # a token for gmail
        to = email
        subject = 'One-Time Password'
        content = f'''
        <p>Dear User,</p>
        <p>Thank you for using our service.</p>
        <p>Your one-time password is Generated as QR, Please scan the QR the and enter the OTP</p>
        <p>Regards,</p>
        <p>Team Anti shoulder-surfing attack platform</p>
        </table>
        '''
        with yagmail.SMTP(user, app_password) as yag:
            yag.send(to, subject, content, attachments=qr_code_path)
            print('Sent email successfully')
    except:
        pass
    messages.error(request, 'Please enter Registred Email')
    return render(request, 'user/userhome.html')

def otpverify(request):
    random_number=otpcheck.random_number
    otp = int(request.POST.get('otp'))
    print(random_number)
    print("hello:",otp)
    if otp==random_number:
        return render(request, 'user/userhome1.html')
    else:
        messages.error(request, 'Please enter correct OTP')
        return render(request, 'user/userhome.html')