# Udacity's Full Stack Web Developer (FSWD) Movie Trailer Website Project

## Project Description:
This project required us to write object-oriented Python server-side code to store a list of our favorite movies, including box art imagery and a movie trailer URL. We then needed to use our code to generate a static web page allowing visitors to browse the movies and watch the trailers.

Modification I made to this project included site design modifications and the use of a 3rd Party API to get the information used for the movies.

**Data for the movies used in this project provided by [The Open Movie Database (OMDb) API](https://www.omdbapi.com/) under the Creative Commons [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) License.**


## How to Download Project Files
In order to download this project to your computer you will need to clone it to your machine. In your terminal ` cd ` to the directory you would like to save the files. Then run the following command:
```
$ git clone http://github.com/irishboy922/FSWD-movie-trailer-website.git
```
You can also click on the ![alt text](github-download-btn.png "github button") button to either download a zip version or copy the clone link.

## How to Run the Application and View the Website
Once you have downloaded the files on your local machine, make sure you have ` cd ` into the folder containing the project files and run the following command into your terminal:
```
$ python entertainment_center.py
```
Upon executing the above command, the generated html file should automatically open in your default browser. Please note that since there are multiple synchronous api requests occuring to collect the data for the movies there may be a few second delay before the site opens in the browser. Once the site is loaded it should run smoothly.

## License
[MIT License](https://opensource.org/licenses/MIT)

