# Quiz Application with Microservices

## General overview
_A a quiz application that allows testing the user's knowledge about design patterns and refactorings_

## Diagram of the system and its constituent parts.
![Diagram of the system](./diagram.png)

## Patterns used, and WHY those patterns were chosen. 
In terms of the design pattern used, we implemented the MVC (Model-View-Controller) pattern. We chose this pattern because it promotes a clear separation of responsibilities within an application.

**Model**: The model is responsible for handling data and logic. In our case, this functionality resides in the models files `UserModel.py` and `QuestionModel.py`. It interacts with the database and handles the necessary logic to process the received information.

**View**: The view is responsible for displaying the user interface and capturing user input. In our case, it is implemented in the React application (`Frontend/quizzapp`). Here, requests are made to the backend based on the operation or query to be performed. The response is then processed to fit each element within the React components.

**Controller**: The controller acts as an intermediary between the model and the view, controlling the flow of data and interactions. In this case, it is implemented in the `controller.py` file. We define the routes and validate the responses received from the controller.

This clear division of responsibilities facilitates code maintenance and modification since changes in one part of the pattern have minimal impact on the other parts.

Additionally, dividing an application into well-defined components allows us to reuse code in different projects. This promotes code reusability and saves development time.

Moreover, due to the separation of responsibilities, it is easier to test the different parts of the application in isolation, ensuring the reliability and quality of each component.

Lastly, we would like to highlight how following this model facilitated our collaborative work. We were able to work on different aspects of the application simultaneously without interfering with each other's work. The clear separation of concerns provided a smooth collaborative workflow.

As for **the UML diagram**, there are various classes that perform specific functions so that together the functionalities of our application can be offered. 
- Initially, there is a class for the DBManager, which allows establishing the connection to the stored data in DynamoDB, in order to apply operations that generate the appropriate information for the app. 
- On the other hand, there are the User and MCQuestion classes, which contain as such the fields that are required to update the database, so they act in the Model, since they have the necessary methods to create a user, give the questions to be answered and the final ranking, and these things are related too with the Controller, because we can get the exact data that we need. 
- Finally, the App class is related to the View, since it makes use of the methods of the Model classes to generate the specific information for a user's game, which is used to display in the graphical interface, so it also has the necessary methods to render the frontend’s components. 

So, the proper division of workloads _allows our application to have a high level of availability and performance_, since users register, see their own information such as their name and score, and access a global data source to interact with our app, in order to obtain their questions, their answers and the leaderboard.

## Prerequisites
Before getting started, make sure you have the following requirements:

* An AWS account with permissions to perform operations on DynamoDB.
* The environment where you will deploy should have at least 2GB of memory.
* Git installed in the environment.
* Python 3 installed in the environment.
* Npm installed in the environment (Using nvm is recommended).
* Inbound and outbound connections enabled.

## Installation and Running the Application

The application is currently fully functional when used locally. Follow the instructions below to install it:

1. Clone this repository to your local environment and ensure that you meet the prerequisites.

### Backend Setup

2. Navigate to the "backend" folder.

3. Create a virtual environment to install Python dependencies.

```shell
python3 -m venv venv
```

4. Activate the virtual environment.

```shell
source venv/bin/activate
```

5. Install the necessary dependencies for the project within the virtual environment. These dependencies are listed in the "requirements.txt" file.

```shell
pip install -r requirements.txt
```

6. Create a "config.py" file and enter the following AWS credentials for the DynamoDB environment you will be using:

```python
AWS_ACCESS_KEY_ID = "your_access_key_id"
AWS_SECRET_ACCESS_KEY = "your_secret_access_key"
AWS_SESSION_TOKEN = "your_session_token"
REGION_NAME = "region_name"
```

7. Run the script using the following command:

```shell
python app.py
```

8. Access the '/create' route in your browser to create the necessary tables in DynamoDB (Do this just once).

9. Access the DynamoDB service from AWS and manually insert the "pool of questions" found in the 'poolQuestions.py' file.

Done! The backend configuration is ready.

**Note:** If tou want to run the unitests for each class, just run the following command in the terminal:
```shell
python3 -m unittest discover -s tests
```

### Frontend Setup

10. Navigate to the "Frontend/quizzapp" folder.

11. Set up npm using the command:

```shell
npm install
```

12. Create a .env and enter the REACT_APP_BACKEND_URL where the frontend will be doing the requests

```env
REACT_APP_BACKEND_URL=http://backend-host:backend-port
```

13. Run the application with the following command:

```shell
npm start
```

Done! The frontend configuration is ready. You can now use the app.

**Note:** Remember that these steps are for setting up the project locally, and it's necessary for both the backend and frontend to be located in the same place.

🚀🎉 Enjoy your experience with the application!


## Acknowledgments and References

### Deployment in Different Locations

This project is designed to be deployed in different locations, allowing the backend and frontend to be in separate instances. Only the frontend would need to be modified to update the API endpoint if necessary.

If you decide to deploy the backend and frontend in different locations, follow these steps:

1. Deploy the backend in the desired location, making sure to configure the necessary credentials for the AWS environment.

2. In the frontend code, update the API endpoint to the new location where the backend is deployed. Replace the existing endpoint with the new URL or hostname.

3. Set up inbound rules and allow traffic to the ports 3000 (React) and 5000 (Flask)

By following these steps, you can successfully deploy the backend and frontend in different locations, ensuring they communicate with each other correctly 😊.

### Notes

We deployed our web application in the following link 'http://44.216.61.126:3000/'. But since we are working in a learner lab, we can't keep running the server for a long period of time. 

However, you can see a demo of the app running in the following link: https://youtu.be/8UzSEpN2K8k