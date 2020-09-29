# Pizza-shop

# Description
This  is a flask application that allows users to log in and choose among the pizzas available with topping of their liking and place an order. they can register and long in in future with the username and password
## Live Link
[View Site](httpherokuapp.com)

## Screenshot




## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app pitches based on categories and commenting section|
| Select the desired pizza | **buy** | Form that you input your comment|
| Click on submit |  | place the order with the desired topping|





## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
 https://github.com/beckynayere/Pizza-Shop
  ```
2. Move to the folder and install requirements
  ```bash
  cd pitch-minute
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.6 manage.py server
  ```
5. Testing the application
  ```bash
  python3.6 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)
* javascript
* bootstrap
* css


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 



## License
* *MIT License:*
