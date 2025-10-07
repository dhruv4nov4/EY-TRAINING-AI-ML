from pydantic import BaseModel

#define a model
class Student(BaseModel):
    name: str
    age: int
    email: str
    is_active: bool = True

#valid data
data = {"name":"Aisha","age":21,"email":"aisha@example.com"}
student = Student(**data)

print(student)
print(student.name)

dataset: students.csv
model: RandomForest
params:
  max_depth: 5
  n_estimators: 100

import configparser

config = configparser.ConfigParser()

config["database"] = {
    "host":"localhost",
    "port":"3306",
    "user":"root",
    "password":"admin123"
}

#write to config file
with open("app.ini","w") as configfile:
    config.write(configfile)

#read from config
config.read("app.ini")
print(config["database"]["host"])

import logging

class InvalidMarksError(Exception):
    pass

def check_marks(marks):
    if marks<0 or marks>100:
        raise InvalidMarksError("Marks must be between 0 and 100")

try:
    check_marks(200)
except InvalidMarksError as e:
    logging.error(e)

import logging

#logging configuration
logging.basicConfig(
    filename='app.log', #log file name
    level=logging.ERROR,  #log levels
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

#example logsss
logging.debug("This is a debug message")
logging.info("Application started")
logging.warning("Low memory warning")
logging.error("File not found error")
logging.critical("Critical system failure")

#normal py class

class Student:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email

#valid data
data = {"name":"Ali","age":"twenty","email":"ali@example.com"}
student = Student(**data)

print(student.age)


import json

student={
    "name":"Vikram",
    "age":22,
    "courses":["AI","ML"],
    "marks":{"AI":89,"ML":90}
}

#write to a json file
with open("student.json",'w') as f:
    json.dump(student,f,indent=4)

#read from json file
with open("student.json",'r') as f:
    data = json.load(f)

print(data["name"])  #vikram will be printed
print(data["marks"]["AI"]) #89

{
    "name": "Vikram",
    "age": 22,
    "courses": [
        "AI",
        "ML"
    ],
    "marks": {
        "AI": 89,
        "ML": 90
    }
}

try:
    value=int(input("Enter a number: "))
    print(10/value)
except ValueError:
    print("You did not enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution finished")

import yaml

config={
    "model":"RandomForest",
    "params":{
        "n_estimators":100,
        "max_depth":5,
    },
    "dataset":"students.csv"
}

#write to YAML file
with open("config.yml","w") as f:
    yaml.dump(config,f)

#read yaml
with open("config.yml","r") as f:
    data = yaml.safe_load(f)

print(data["params"]["n_estimators"]) #100