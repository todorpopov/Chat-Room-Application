Introducing Chat Lounge, a real-time web application built with Python, Django, Channels, 
Redis, and Docker. This project allows users to communicate with each other in a secure, fully-featured chat room.

Features include:

1. Real-time messaging using WebSockets
2. Signing up, logging in, and logging out
3. Support for multiple chat rooms
4. Displaying the number of online users
5. Responsive and easy-to-use UI

The project is built using the Django web framework, which provides a solid foundation for web applications. 
Channels and Redis are used to enable real-time messaging, while Docker is used to run the Redis server.

The project has been deployed to Heroku, you can check it out at: https://django-chat-room-web-app.herokuapp.com/

Preview:

![chat_lounge_gif](https://user-images.githubusercontent.com/29499875/207053715-d7648af4-d585-40ad-a7e2-a0dfd15b119a.gif)

Local Installation

Installation overview:
1. Create a new directory on your machine.
2. Download the repository from GitHub and unzip it into this new directory.
3. Edit the settings.py file inside the chat_project directory.
4. Decide on whether to use a local Redis server or the “InMemoryChannelLayer” setting.
5. Install the dependencies, using the requirements.txt file.
6. Run the web server and go to localhost.

Setting up Locally:

Choose where you’d like to set up the project locally, create a new directory, and download the repository as a zipped file. Then you can unzip the folder inside the new directory and proceed with the next steps.

Editing the Project Settings:

For the app to work correctly, you’ll need to edit a couple of variables inside the settings.py file, which can be found in chat_project/settings.py.
First, set the downloaded_from_github variable to True. By doing this, the app will use a preset SECRET_KEY, instead of looking for it in a file. You can manually set a different key on your own by following the comments.
The next setting that needs to be changed is the redis_caching variable. When this variable is set to True, the app will try to connect to a Redis server at localhost and port 6379. This means that if no server is found, for the app to connect to, the messaging feature will not work. I will explain more about the Redis server in the next step.

Redis and “InMemoryChannelLayer”:

There are two ways of enabling the use of the Channel Layers. First is to use the “InMemoryChannelLayer”, and the second is to use a separate Redis server, to which the app can connect to. I will explain both, but I personally recommend using the “InMemoryChannelLayer”, because of the easier setup.
•	To use the “InMemoryChannelLayer”, you can just leave the redis_caching variable set to False. The official documentation suggests that this is not recommended for production use, but for development and testing only.
•	To use the “RedisChannelLayer”, you’ll have to set up a Redis server locally. The easiest way to do that is with Docker.
You’ll have to install the Docker desktop application and confirm it runs correctly by opening it. Also, make sure to enter:
<br/><br/>*docker*<br/><br/>
in an empty terminal in order to confirm that the CLI works correctly.
Then, open a terminal and enter the following command:
<br/><br/>*docker run -p 6379:6379 -d redis:5*<br/><br/>
This will create a container using the Redis image. Now set the redis_caching variable, located in setting.py, to True.

Installing the Required Dependencies:

Installing the dependencies can be done through the “requirements.txt” file. Open a terminal and enter the following command:
<br/><br/>*pip install -r requirements.txt*<br/><br/>

Running the Server and Testing the Application:

To run the web server, open a terminal and use the cd command to enter the directory where the project is located. Once inside the project’s directory, you can run the following command:
<br/><br/>*daphne chat_project.asgi:application*<br/><br/>
This will run the development server at your localhost (usually: 127.0.0.1:8000). Then, you can copy the displayed address into a browser, and the application should load.
