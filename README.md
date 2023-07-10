# Face Recogniton GUI-APP



# A very Simple Gui app for Face Detection 

  - Collect Face Data
  - Build Face Classifier 
  - Detecte the face
  - REcognize the face and show if its identified or not.
  
  
# Installation

Important note - For now training dataset is not uploaded on github. So as soon as this code is downloaded, inside data folder, do create a folder with the name of a person who you want to train the model with.Then in file train_model.py, just replace your new folder created name on line 10 (Example: data/{your_folder_name)}) Then follow the steps mentioned below.


1 : Install the requirements .

```sh
$ pip install -r  requirements.txt
```

2 : Run The App 

```sh
$ python3 app-gui.py
```

3. 2nd step will run only for collecting the dataset of a person with whom we want to train our model.

4. Then once dataset is collected, we need to train the model. For that run the code in the terminal.

```sh
$ python3 train_model.py
```

5. Now once model is trained, a file named 'face_enc' will be generated. Now we are good to go with face recognition. For that run the command 

```sh
$ python3 face_recognition_in_video.py
```

6. On success of step 5, video cam will be started and in realtime it will display if identified face os recognized or not. 

# APP GUI

### Home Page
![homepage](https://i.ibb.co/c62qvR2/home-page.png)

### Add a User <br>
Add the user you want to train a classifier for <br>
![page1](https://i.ibb.co/t8gdq6s/adduser.png)<br>


### Capture Data and Train Classifier<br>
Capture Data From the face then train the classifier<br>
![page2](https://i.ibb.co/D8JgYhN/capandtraindata.png)<br>

### Users List<br>
List of all the users<br>
![page3](https://i.ibb.co/1KwfVVV/dropdown.png)<br>

### Recognition <br>
A webcam window will popup and start recognition proccess<br>
![page4](https://i.ibb.co/sCtgDDC/4page.png)<br>
>![Face Recognition](https://i.ibb.co/bNpC5wR/jack.png)<br>



<br><br>

Made By ❤ : [Anirudh](anirudh.chawla@radixweb.com)<br>




