from __future__ import division
import numpy
import pandas
import statsmodels.api as sm


def simple_heuristic(file_path):
    '''
    In this exercise, we will perform some rudimentary practices similar to those of
    an actual data scientist.
    
    Part of a data scientist's job is to use her or his intuition and insight to
    write algorithms and heuristics. A data scientist also creates mathematical models 
    to make predictions based on some attributes from the data that they are examining.

    We would like for you to take your knowledge and intuition about the Titanic
    and its passengers' attributes to predict whether or not the passengers survived
    or perished. You can read more about the Titanic and specifics about this dataset at:
    http://en.wikipedia.org/wiki/RMS_Titanic
    http://www.kaggle.com/c/titanic-gettingStarted
        
    In this exercise and the following ones, you are given a list of Titantic passengers
    and their associating information. More information about the data can be seen at the 
    link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data. 

    For this exercise, you need to write a simple heuristic that will use
    the passengers' gender to predict if that person survived the Titanic diaster.
    
    You prediction should be 78% accurate or higher.
        
    Here's a simple heuristic to start off:
       1) If the passenger is female, your heuristic should assume that the
       passenger survived.
       2) If the passenger is male, you heuristic should
       assume that the passenger did not surive.
    
    You can access the gender of a passenger via passenger['Sex'].
    If the passenger is male, passenger['Sex'] will return a string "male".
    If the passenger is female, passenger['Sex'] will return a string "female".

    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the Passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associating value should be 1 if the
    passenger survied or 0 otherwise. 

    For example, if a passenger survived:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 1

    Or if a passenger perished in the disaster:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 0
    
    You can also look at the titantic data that you will be working with
    at the link below:
    https://www.dropbox.com/s/r5f9aos8p9ri9sa/titanic_data.csv
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        pid = passenger["PassengerId"]
        if passenger["Sex"] == "male":
            predictions[pid] = 0
        else:
            predictions[pid] = 1
    return predictions


def complex_heuristic(file_path):
    '''
    You are given a list of Titantic passengers and their associating
    information. More information about the data can be seen at the link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data

    For this exercise, you need to write a  more sophisticated heuristic
    that will use the passengers' gender and their social economical class and age 
    to predict if they survived the Titanic diaster. 
    
    You prediction should be 79% accurate or higher.
    
    If the passenger is female or if his/her socio-economical status is high AND
    if the passenger is under 18, you should assume the passenger surived.
    Otherwise, you should assume the passenger perished in the disaster.
    
    Or more specifically in code terms: female or (high status and under 18)
    
    You can access the gender of a passenger via passenger['Sex'].
    If the passenger is male, passenger['Sex'] will return a string "male".
    If the passenger is female, passenger['Sex'] will return a string "female".
    
    You can access the socio-economical status of a passenger via passenger['Pclass']:
    High socio-economical status -- passenger['Pclass'] is 1
    Medium socio-economical status -- passenger['Pclass'] is 2
    Low socio-economical status -- passenger['Pclass'] is 3

    You can access the age of a passenger via passenger['Age'].
    
    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the Passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associating value should be 1 if the
    passenger survied or 0 otherwise. 

    For example, if a passenger survived:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 1

    Or if a passenger perished in the disaster:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 0
    
    You can also look at the titantic data that you will be working with
    at the link below:
    https://www.dropbox.com/s/r5f9aos8p9ri9sa/titanic_data.csv
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        pid = passenger["PassengerId"]
        if passenger["Sex"] == "female":
            predictions[pid] = 1
        elif passenger["Pclass"] == 1 and passenger["Age"] < 18:
            predictions[pid] = 1
        else:
            predictions[pid] = 0
    return predictions


def custom_heuristic(file_path):
    '''
    You are given a list of Titantic passengers and their associating
    information. More information about the data can be seen at the link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data

    For this exercise, you need to write your custom heuristic that will take
    in some combination of the passenger's attributes and predict if the passenger
    survived the titanic diaster.

    Can your custom heuristic beat 80% accuracy?
    
    The available attributes are:
    Pclass          Passenger Class
                    (1 = 1st; 2 = 2nd; 3 = 3rd)
    Name            Name
    Sex             Sex
    Age             Age
    SibSp           Number of Siblings/Spouses Aboard
    Parch           Number of Parents/Children Aboard
    Ticket          Ticket Number
    Fare            Passenger Fare
    Cabin           Cabin
    Embarked        Port of Embarkation
                    (C = Cherbourg; Q = Queenstown; S = Southampton)
                    
    SPECIAL NOTES:
    Pclass is a proxy for socio-economic status (SES)
    1st ~ Upper; 2nd ~ Middle; 3rd ~ Lower

    Age is in Years; Fractional if Age less than One (1)
    If the Age is Estimated, it is in the form xx.5

    With respect to the family relation variables (i.e. SibSp and Parch)
    some relations were ignored.  The following are the definitions used
    for SibSp and Parch.

    Sibling:  Brother, Sister, Stepbrother, or Stepsister of Passenger Aboard Titanic
    Spouse:   Husband or Wife of Passenger Aboard Titanic (Mistresses and Fiances Ignored)
    Parent:   Mother or Father of Passenger Aboard Titanic
    Child:    Son, Daughter, Stepson, or Stepdaughter of Passenger Aboard Titanic
    
    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the Passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associating value should be 1 if the
    passenger survied or 0 otherwise. 

    For example, if a passenger survived:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 1

    Or if a passenger perished in the disaster:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 0
    
    You can also look at the titantic data that you will be working with
    at the link below:
    https://www.dropbox.com/s/r5f9aos8p9ri9sa/titanic_data.csv
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        pid = passenger["PassengerId"]
        if passenger["Sex"] == "female" or \
          (passenger["Pclass"] <= 2 and passenger["Age"] < 16):
            predictions[pid] = 1
        else:
            predictions[pid] = 0
    return predictions

