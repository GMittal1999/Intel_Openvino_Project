# Intel_Openvino_Project
In this project I have made protype car using various hardware component (Raspberry pi, PI Camera, Motors, wire etc.). The main purpose of this project is to solve various transportation issues. For transportation purpose one always need to depend upon on the man power. But what if we remove that limitation and make the transportation remote control with driver assistant. 


So, in this project I have made a simple website through which one can controlits transport. there will be live feed from the camera using pi camera. I am sending the live feed from the camera using using flask server. 


So what is the roleof openvino in this project.

For drive Assistant part i have used openvino project. Using Object detection of tensorflow I am detecting the object in real time. It will help driver to get full insight of the environment and object around it and he/she can make proper decision.


So, how openvino is benefiting my project?

Actually as I am sending the photo on cloud and if I upload my modal on cloud and then use it for the live feeding there will be huge latency.
So if I use Openvino and move my modal near to the application I can reduce this latency drastically. This is how Openvino is adding advantage to my project.


So How to run my project.

Firstly you have to import the respetive files to run various files these are:- (Flask,RPI.GPO (for integration with raspberry Pi)) 
Actually to integrate the Pi Cam you will require a Camera.py file that i have include in my project.
In this repositary I have not able to to upload the bin file for the object detetion as it too large but you can download it from open vino site as I have used the pre trained model of openvino for my project.
the name of the files will be as follows:
frozen_inference_graph.xml and frozen_inference_graph.bin

Now for my website:-

For this we have to install node and here we will be using express framework.
all the libraries that nedd to be install is given in the file package.jason under the section dependencies.
Here I have work mainly on backened so You will find My UI/UX not that attractive but this is beacause it is a protype only.
Now what are all the files for our Rasperry pi and websites.
RaspberryPi (all files except nodejs folder)
website (only node js folder)


Now how to run my project:-

Under the folder Camera_code there is file named camera_route.py this a file that contain the openvino code. Here check the CPU_Extension I have provided according to your openvino version and OS you have to change it.
Now to run the whole project you have to run three files:-
python_code.py
camera_route.py (under folder camera code) (running this file you have to provide the path of your models xml file through command prompt)
for installing openvino on raspberry pi ypu can
app.js (under folder nodejs)
Here in this python_code.py and camera_code.py I have defined the port So while running You have to free those port or change the code according to your free ports.


When all of this is done. ypo can see when you run your app.js file your website will be open and you can see a input box .
In that input box you have to specify the ip addres of your Raspberry pi and then click on submit.
Now if everythings is done properly you will seelive feed from the camera and object are being detected in it and below that there are controls to to control your car.


Limitations of my project.

for this to implement in the real life one should need a private network whose reach is available allover the world which is very costly.


Future aspects of my project.

You can advance it to self driving concept.
In this I have done object detection only but you can extend the idea to Lane detection distance between vehicles and give proper insight to the driver to make good decision. Then this software will act as good driver assistant.
