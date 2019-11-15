# Final Project / Djoodle
This repository contains the code for the final project of *CS50's Web Programming with Python and JavaScript* implementing the *djoodle* django application allowing users to create surveys and have their friends vote on them.

## Filestructure

According to the specifications of Django this repository contains one main directory for the whole *djoodle* Django Project as well as one directory for each of the two Django Apps: *survey* and *Users*

### djoodle

There have been only very minor changes to the files in this directory relative to their default contents when they created by the Django `startproject` command.

Those changes include

* *settings.py*: Some additional lines in the end to enable using some additional Features such as *Crispy Forms*.
* *urls.py*: Urlpatterns to include the urls specified in users and survey module.

### Survey

This app contains the main functionality of creating, managing and deleting surveys as well as handling.

I decided to create the following models representing the logic and data structure of my application:
* *Survey*: This represents one Survey including title and description as well as data on the author of the survey as well as the date the survey was created.
* *SurveyOption*: This represents one possible selection on one survey that voters can cast a vote on. This includes a description as well as a foreign key specifiying which survey the option belongs to.
* *Vote*: This model represents a vote cast by one voter whose name is saved in the respective field on a particular surveyoption which is referenced with a foreign key. 

For creating the views I largely rely on djangos model based generic views to enable the functionality to create, update, delete and list objects.


### Users

For the log in part I completely rely on the built in log in view, whereas for the registration I have slightly customize the view using a slightly modified version of the built in UserCreationForm that adds first and last name.
To improve the aesthetics of the forms I format them using *Crispy* Forms in my templates.

## Usage

To see a quick walkthrough of the project check this [Video]( ).
