# Dance Your Way

Dance Your Way is a website designed alongside Gusto, a London based Latin Dance group

Dancers will come to the website to see what local events are occurring, whilst event organisers will log in to add their events to the database.

---

# Contents

1. [UX](#ux)
2. [Features](#Features)
3. [Technologies](#Technologies)
4. [Languages](#Languages)
5. [Libraries](#Libraries)
6. [Testing](#Testing)
7. [Deployment](#Deployment)
8. [Credits](#Credits)

## UX

##### User Stories

- "As an event organiser, I want to post details about my events, so I can get more customers"
- "As a dancer, I want to view information about events in my city, so I can plan where to go for class"

##### Design Choices

- List of design choices

##### Wireframes

I used [Balsamiq](https://balsamiq.com/) to create detailed wireframes for each page at a mobile level and then at a desktop level to keep with the Mobile First design approach.

As is to be expected certain elements present in the wireframes did not make it into the project itself but may yet do so further down the line.

You can find my wireframes [here](https://github.com/Magnusson95/Dance-Your-Way/tree/master/wireframes).

## Features

##### Existing Features

- List of current features

##### Features Left to Implement

- List of features not yet implemented

## Technologies

- [Github](https://github.com/) to host this project's respositories.
- [Gitpod](https://www.gitpod.io/) IDE of choice for development.
- [Git](https://en.wikipedia.org/wiki/Git) for version control
- [Google Chrome developer tools](https://developers.google.com/web/tools/chrome-devtools) for testing and troubleshooting.
- [Coolors](https://coolors.co/) for colour schemes.

## Languages

- [HTML](https://en.wikipedia.org/wiki/HTML) to build the page.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) to style the page.
- [Javascript](https://en.wikipedia.org/wiki/JavaScript) to add interactivity.
- [Python](https://www.python.org/) to query database

## Libraries

- [Font Awesome](https://fontawesome.com/) for icons.
- [Google Fonts](https://fonts.google.com/) used for fonts.
- [Materialize](https://materializecss.com/) a modern responsive front-end framework based on Material Design.
- [jQuery](https://jquery.com/) used for easier integration of Javascript.
- [Flask](https://www.fullstackpython.com/flask.html) for app routing
- [PyMongo 3.10.1](https://api.mongodb.com/python/current/) Python API for MongoDB

## Testing

##### Internet Browsers

The same process of opening up the live page and meticulously clicking all links, buttons, and re-sizing of windows was utilized in the following browsers:

- Google Chrome - Main browser of choice for development.
- Microsoft Edge – All working as intended
- Mozilla Firefox - No issues. Everything works as intended.
- Safari - All working as intended.

The site has been tested physically on a number of mobile devices including:

- iPhone 5, 7, 10 and 11
- Google Pixel
- Galaxy S9.

Various examples of multiple screen sizes on different pages of the site can be found [here](https://github.com/Magnusson95/Dance-Your-Way/tree/master/wireframes)

Javascript tested through user testing during each stage of writting. Including confirmation of API connection, API verification, API customisation and user testing of jQuery with Google Chrome Developer Tools.

Google Maps API saw no major issues. The Code Institute training was used to implement this API and then further customisation was done through the Google Maps API documentation, meaning no bugs occurred during testing.

Google Maps Geocode API saw no major issues. Testing of multiple addresses showed that the API successfully distinguished the closest related geocode possible. Where the API fails due to false address input, this is caught before the form is submitted, requiring the user to resubmit a new address.

Email JS API saw some minor issues with verification of the API link, this was rectified through resubmitting the API link. Bug messages were built in for successful or unsuccessful runs of the API. This was tested in a number of ways, from various devices and consol messages were checked.

- HTML

  - [The W3C Markup Validation Service](https://validator.w3.org/)

- CSS

  - [The W3C Markup Validation Service](https://jigsaw.w3.org/css-validator)

- JavaScript

  - [JS Hint](https://jshint.com/) - All scripts were checked with JS Hint. All errors were solved, only received a handful of warnings for code only available in ES6.

- Python
  - [PEP8](http://pep8online.com/) - The Python scripts were checked with pep8online. All the errors were solved.

##### Issues and Resolutions

- List of issues

##### Known Issues

- List of issues

# Deployment

You will need the following tools installed on your system:

- [Python 3](https://www.python.org/downloads/)
- An IDE such as [Visual Studio Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/download/)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) 
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

## Local Deployment
The following instructions are based on use on a Windows 10 OS and IDE VS Code. If your OS is different, the commands may be different, but the process, in general, remains the same.

#### Instructions

- Save a copy of the Github repository located at https://github.com/Magnusson95/Dance-Your-Way.
  - Unzip the repo into the chosen folder.
- If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/Magnusson95/Dance-Your-Way
```

- Within the chosen directory, create a virtual environment with the command:
```
python -m venv venv
```  

- Activate the virtual environment with the command:
```
.\venv\bin\activate 
```

- Install all required modules with the command: 
```
pip install -r requirements.txt
```

- Create a `.env` file with your credentials:
e.g
```
  - **MONGO_URI_KEY**: `link to your Mongo DB`
  - **SECRET_KEY**: `your chosen secret key`
  - **GOOGLE_ACCESS_KEY**: `your google API key`
  - **ACCESS_KEY_ID**: `your AWS S3 access key`
  - **ACCESS_SECRET_KEY**: `your mailjs access key`
```

- Create a database in MongoDB Atlas called **events_manager** with the following collections:
  - **countries**
  - **events**
  - **organisers**

- Run the application with the command
```
flask run
```
- Open the website at `http://0.0.0.0:8080/`

## Remote Deployment

#### Instructions
To deploy this app to Heroku you need to follow the steps below:

- Create a **requirements.txt** file so that Heroku can install all the dependencies required to run the app.
  `pip freeze > requirements.txt`

- Create a **Procfile** with the command:
  `echo web: python app.py > Procfile`

- In this step, you have to create a free account on the [Heroku website](https://signup.heroku.com/).
-  Login to the account, click on new and then create a new app. In the following screen, you need to give a name and choose the Europe region.
-  In the menu access the **Deploy** option, after that click on Connect to Github. Just below provide the information from the app's repository on GitHub and select the option Enable Automatic Deploy.
- On the Dashboard of the APP, click on Settings and then click on the option **Reveal config Vars**.
- Now you need to add the following variables to **Reveal config Vars**:
  - **IP**: `0.0.0.0`
  - **PORT**: `8080`
  - **MONGO_URI_KEY**: `link to your Mongo DB`
  - **SECRET_KEY**: `your chosen secret key`
  - **GOOGLE_ACCESS_KEY**: `your google API key`
  - **ACCESS_KEY_ID**: `your AWS S3 access key`
  - **ACCESS_SECRET_KEY**: `your mailjs access key`
- You are now ready to access the deployed app on Heroku.

## Credits

### Content

- All content was created by me or my fellow dance colleauges:
  - [Gabeto](https://www.facebook.com/Tropicsalsa/)
  - [Gusto](https://www.facebook.com/groups/545395699629121/)
  - [Dance Xplosion](https://www.facebook.com/DanceXplosionSibiu)

### Media

- All media was sourced from the facebook accounts of dance colleagues:
  - [Gabeto](https://www.facebook.com/Tropicsalsa/)
  - [Gusto](https://www.facebook.com/groups/545395699629121/)
  - [Dance Xplosion](https://www.facebook.com/DanceXplosionSibiu)