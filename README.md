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
- [W3C Markup Validation](https://validator.w3.org/) used to validate HTML.
- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) used to validate CSS.

## Languages

- [HTML](https://en.wikipedia.org/wiki/HTML) to build the page.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) to style the page.
- [Javascript](https://en.wikipedia.org/wiki/JavaScript) to add interactivity.
- [Python](https://www.python.org/) to query database

## Libraries

- [Font Awesome](https://fontawesome.com/) for icons.
- [Google Fonts](https://fonts.google.com/) used for fonts.
- [jQuery](https://jquery.com/) used for easier integration of Javascript.
- [Flask](https://www.fullstackpython.com/flask.html) for app routing
- [pymongodb]

## Testing

##### Internet Browsers

The same process of opening up the live page and meticulously clicking all links, buttons, and re-sizing of windows was utilized in the following browsers:

- Google Chrome - Main browser of choice for development.
- Microsoft Edge – All working as intended besides flex at minimum width
- Mozilla Firefox - No issues. Everything works as intended.
- Safari - All working as intended.

The site has been tested physically on a number of mobile devices including:

- iPhone 5, 7, 10 and 11
- Google Pixel
- Galaxy S9.

Various examples of multiple screen sizes on different pages of the site can be found [here](#)

Javascript tested through user testing during each stage of writting. Including confirmation of API connection, API verification, API customisation and user testing of jQuery with Google Chrome Developer Tools.

Initial links to the Tableau API did not work, but the removal of jQuery and implementation of pure Javascript, plus a new API key, fixed this issue.

API customisation of of the Tableau Dashboard included some sizing issues, especially when on smaller devices. Each device size was tested individually for rendering issues and subsequently fixed.

Google Maps API saw no major issues. The Code Institute training was used to implement this API and then further customisation was done through the Google Maps API documentation, meaning no bugs occurred during testing.

Email JS API saw some minor issues with verification of the API link, this was rectified through resubmitting the API link. Bug messages were built in for successful or unsuccessful runs of the API. This was tested in a number of ways, from various devices and consol messages were checked.

Speed was also tested using [Pingdom](#) and the site received a performance grade of #/100

##### Issues and Resolutions

- List of issues

##### Known Issues

- All responsiveness working on Microsoft Edge except minimum flex view.

## Deployment

Dance Your Way was developed on GitPod, using git and GitHub to host the repository.

**When deploying Dance Your Way using GitHub Pages be sure to follow these steps:**

1. Navigate to '/Magnuson95/dance-your-way' or alternatively click
2. In the top navigation click on 'settings'.
3. Scroll down to the GitHub Pages area.
4. Select 'Master Branch' from the 'Source' dropdown menu.
5. Click to confirm my selection.
6. Dance Your Way should now be live on GitHub Pages.

**In order to run Dance Your Way locally be sure to follow these steps whilst still on Github:**

1. Navigate to '/Magnusson95/Dance-Your-Way' or alternatively click [here](https://github.com/Magnusson95/Dance-Your-Way).
2. Click the green 'Clone or Download' button.
3. Copy the url in the dropdown box.
4. Using your IDE of choice open up your preferred terminal.
5. Navigate to your desired file location.
6. Copy the following code and input it into your terminal to clone Dance Your Way.

`git clone https://github.com/Magnusson95/Dance-Your-Way.git`

## Credits

### Content

- All content was created by me.

### Media

- List of media provided by #, plus [url](#)