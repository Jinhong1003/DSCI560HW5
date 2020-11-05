# DSCI560HW5
Practice of Visualization and docker

### <1>.step to install and run your visualization

1.Clone files in this github reposiroty to local machine

2.enter the directory of the project

3.pip install pip virtualenv

4.Create a virtual environment,under the directory of project

5.activate the envronment in terminal ,source venv/bin/activate,venv is the name of the environment,
,download the packeget in requirements.txt for creating a new environment use pip. pip install -r requirements.txt

6.under this new environment, input "Bokeh serve --show INF560HW5.py" in terminal

7.It will pop out a webpage of this visualization.

8.There are three figures in the dashborad, for the second one and third one, users can choose the date they want.When user move mouse to the exact node they want, it will show the exact number.
<img width="1085" alt="image" src="https://user-images.githubusercontent.com/54864182/98058761-5b8e1600-1dfa-11eb-8f61-e825b23c324c.png">

<img width="974" alt="image" src="https://user-images.githubusercontent.com/54864182/98058814-78c2e480-1dfa-11eb-87a7-5dd8344d1a79.png">


### <2>. step-by-step instructions of executing codes using docker 
1.Make sure your local computer have already installed docker desktop

2.Clone files in this github reposiroty to local machine in terminal,eg:git clone https://github.com/Jinhong1003/DSCI560HW5.git

3.Build image in the directory you cloned the file in terminal.(eg: docker build --tag app1 .)

4.Make sure you bulid the image successfully in terminal.(eg:docker images) it will show the images you have

5.Run the image in your terminal. (eg: docker run -p 5006:5006 -it app1)

6.In your terminal , it will show something like "2020-11-05 02:16:50,850 Bokeh app running at: http://localhost:5006/INF560HW5"

7.Browse the website "http://localhost:5006/INF560HW5",  Our visualization will be showed.

Congretuations!
