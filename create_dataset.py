import cv2
import os

def start_capture(name):
        path = "./data/" + name
        detector = cv2.CascadeClassifier("./data/haarcascade_frontalface_default.xml")
        is_new_directory_created = False
        try:
            is_new_directory_created = True
            os.makedirs(path)
            num_of_images = 0
            before_images = 0
        except:
            print('Directory Already Created')
            is_new_directory_created = False
            num_of_images = len(os.listdir(path)) + 1
            before_images = num_of_images - 1
            print(f"num_of_images {num_of_images}")
        vid = cv2.VideoCapture(0)
        while True:

            ret, img = vid.read()
            new_img = None
            if img is not None:
             print(f"vdvd {img.shape}")
             grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
             face = detector.detectMultiScale(image=grayimg, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30))
             for x, y, w, h in face:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)
                cv2.putText(img, "Face Detected", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255))
                cv2.putText(img, str(str(num_of_images)+" images captured"), (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255))
                new_img = img[y:y+h, x:x+w]
             cv2.imshow("FaceDetection", img)
             key = cv2.waitKey(1) & 0xFF


             try :
                cv2.imwrite(str(path+"/"+str(num_of_images)+name+".jpg"), new_img)
                num_of_images += 1
             except :

                pass
             if is_new_directory_created:
                print(f"before_images {before_images}")
                print(f"num_of_images {num_of_images}")
                if key == ord("q") or key == 27 or num_of_images > 20000:
                    break
             else:
                print(f"before_images else {before_images}")
                print(f"num_of_images else {num_of_images}")
                if key == ord("q") or key == 27 or num_of_images > 20000:
                    break
        cv2.destroyAllWindows()
        return num_of_images
