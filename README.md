# Udacity's Full Stack Web Developer (FSWD) Movie Trailer Website Project

## Project Description
This project required us to write object-oriented Python server-side code to store a list of our favorite movies, including box art imagery and a movie trailer URL. We then needed to use our code to generate a static web page allowing visitors to browse the movies and watch the trailers.

Modifications I made to this project included changing the site design, the use of a 3rd Party API to get the information used for the movies, and the inclusion of extra information about each movie, such as movie rating, IMDB review score, and a short summary of the movie's plot.

**The data for the movies used in this project provided by [The Open Movie Database (OMDb) API](https://www.omdbapi.com/) under the Creative Commons [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) License.**


## How to Download Project Files
In order to download this project to your computer you will need to clone it to your machine. In your terminal ` cd ` to the directory you would like to save the files. Then run the following command:
```
$ git clone http://github.com/irishboy922/FSWD-movie-trailer-website.git
```
You can also click on the ![alt text](github-download-btn.png "github button") button to either download a zip version or copy the clone link.

## How to Run the Application and View the Website
Once you have downloaded the files on your local machine, you will need to make sure you have the [Requests](http://docs.python-requests.org/en/master/) Python library installed on your machine. To check if you have it installed, open your terminal and type ` $ python -c "import requests" `. If you get back this ` ImportError: No module named requests ` error message then you need to install it.

To install the Requests library, type the following command in your terminal:
```
$ pip install requests
```
If you do not have PIP installed yet, please follow [this](http://docs.python-guide.org/en/latest/starting/installation/) tutorial. Note that if you have Python 2.7.9 (and up) or Python 3.4 (and up) installed from python.org, you should already have pip and setuptools installed. Though they may need to be upgraded.

Once you have the Requests library installed make sure you have switched (` cd `) to the folder containing the project files and run the following command into your terminal:
```
$ python entertainment_center.py
```
Upon executing the above command, the generated html file should automatically open in your default browser. Please note that since there are multiple synchronous api requests occuring to collect the data for the movies there may be a few second delay before the site opens in the browser. Once the site is loaded it should run smoothly.

## How to Use the Site
Using the site is pretty straight forward. Once the site has been generated and opened in your browser, a list of movie posters will be displayed. If you _hover_ over a movie poster, detailed information, such as the title, rating, story plot, and IMDB review will appear. If you _click_ on the movie poster, a movie trailer will appear and autoplay.

Enjoy!

## License
[MIT License](https://opensource.org/licenses/MIT)

