# [News On The Go](https://github.com/Miss-Faith/News-On-The-Go)
#### By [Faith Mwangi](https://github.com/miss-faith)
### Description
A landing page that provides users News. The landing page provides a list of news sources. On click a user is redirected to articles under the news source. To read an article in full, the user clicks on the read link that provides the articles source.
## Site
### Setup Requirements

##Developer
## Prerequisites
**Installing Python**

Make sure that you have [Python3 installed](https://realpython.com/installing-python/) on your machine.

You may check your Python version by running:

```bash
$python --version
```

Depending on your installation you might have access to Python3 interpreter either by running `python` or `python3`.

```bash
$python
```
Note that in this repository whenever you see `python` it will be assumed that it is Python **3**.

**Cloning**
Fork the repository and Git clone to your local machine. Access the file and run the program on the code editor, ubuntu, mac or windows terminal.
```bash
$git clone https://github.com/user-name/News-On-The-Go/
$cd News-On-The-Go
```

**Creating a Virtual Environment**
Inside the News on the Go directory create a virtual environment by running
```bash
$python3 -m venv --without-pip virtual
```
activate the virtual environment by running
```bash
$source virtual/bin/activate
```
**Adding dependencies**
Install pip
```bash
$curl https://bootstrap.pypa.io/get-pip.py | python
```
Install Flask
```bash
(virtual) home:~// $pip install flask
```
Install Bootstrap
```bash
(virtual) home:~// $pip install flask-bootstrap
```
Install Flask Script
```bash
(virtual) home:~// $pip install flask-script
```

Depending on your installation the pip package manager may be accessible either by running `pip` or `pip3`.

**Getting an API key**
To get an api key, click here: [News API](https://newsapi.org/). Follow directions to get your own key.

create a start.sh file replace the add the yout api Key and run command

export NEWS_API_KEY='<Add your api Key here>'
python3. manage.py server


**Running the app** 
To make the program executable, run:
```bash
(virtual) home:~// $chmod a+x start.sh
```
To run the program, run:
```bash
(virtual) home:~// $./start.sh
```
Follow the local link generated to view your live site

**Running tests** 
To run test cases:
```bash
(virtual) home:~// $python3 manage.py test
```

## Technology Used
### Frameworks
* Flask
* Bootstrap
###Languages
* Python
* CSS
* HTML
### Other resources
* [Coolors](https://coolors.co/)
* [Google Fonts](https://fonts.google.com/)


## Development
### Want to contribute? Great!
To fix a bug or enhance an existing module, follow these steps:
* Fork the repo
* Create a new branch ('git checkout -b improve-feature')
* Make the appropriate changes in the files
* Add changes to reflect the changes made
* Commit your changes ('git commit -am 'Improve feature')
* Push to the branch ('git push origin improve-feature')
* Create a Pull Request
### Bug / Feature Request
If you find a bug/error, kindly open an issue [here](https://github.com/miss-faith/News-On-The-Go/issues/new)
Include your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/miss-faith/News-On-The-Go/issues/new)
Include sample queries and their corresponding results.
## To-Do
Future update to include a data base that stores information accessible when the application is closed and re-opened
## Contact information
[Faith Mwangi](https://github.com/miss-faith)

[Email](faith.mwangi@student.moringaschool.com)
## License
MIT License
Copyright (c) 2022 **Faith Mwangi**