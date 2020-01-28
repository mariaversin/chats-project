# Chat Analysis

![image](https://github.com/mariaversin/chats-analysis/blob/master/api.png)

The goal of this project is to analyze the conversations of my team to ensure they are happy :smiley:.

## Main goal 

##### Analyze the conversations coming from a chat like slack

**How?**

(L1) Writing an API in Flask just to store chat messages in mySQL

(L2) Extracting sentiment from chat messages and perform a report over a whole conversation 

(L3) Recommending friends to a user based on the contents from chat documents using a recommender system with NLP analysis 

(L4) Creating an image of the API with Docker --> In process

(L5) Heroku --> In process


**API endpoints**
```python
@app.route('/')
```
- Returns all data of MySQL database 

```python
@app.route('/add', methods=['POST'])
```
- Add new user: Username, text, idChat, idUser, idMessage

```python
@app.route('/edit/<string:idMessage>')
```
- To edit users
```python
@app.route('/update/<string:idMessage>', methods = ['POST']')
```
- To confirm user update successfully
```python
@app.route('/delete/<string:idMessage>')
```
- To delete users (you will have to confirm to continue with user deletion)
```python
@app.route('/analyze/<string:idChat>')
```
- Returns the sentiment analysis of the idChat. There are 3 values, positive, negative and neutral, whose sum is 1.
```python
@app.route('/sentiment/<idUser>')
```
- Returns the sentiment analysis of the idUser.
```python
@app.route('/friendship/<name>')
```
- Gives you a recommended friendship

## **Installation & Technologies**

1. __Python 3.6__

1. __LAMP__: It is used to create and deploy dynamic web applications.
[To install LAMP in ubuntu 19.10](https://www.digitalocean.com/community/tutorials/como-instalar-en-ubuntu-18-04-la-pila-lamp-linux-apache-mysql-y-php-es)
- Linux --> operating system for the web application
- Apache --> web server
- Mysql --> database
- Php --> to process dynamic content

2. __Flask__: Framework that allows you to create web applications quickly and with a minimum number of lines of code.

- Flask 1.1.1
- Flask-MySQLdb 0.2.0 (to connect to Mysql)

3. __NLTK 3.4.5__: set of libraries and programs for the processing of symbolic natural language and statistics for the Python programming language.


## **How to use?**

1. When you have everything installed, - I also installed MySQL Worckbench - you have to import the database that is in the __input folder__. How to do it? Very easy: in scheme, you create a new scheme, you click on it with the right button, and in the drop-down you select Table Data Import, and there you already select your file. It allows you to import both in .csv and .json format.


2. You've to have a MySQL password. Save it in an __.env__ under the name of the SECRET_KEY variable. 
__E.g__: SECRET_KEY = "your-password" 

