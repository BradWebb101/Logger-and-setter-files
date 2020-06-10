#Questions for flynn

import logging
import getpass
from datetime import datetime
import pandas as pd

# class Human:
#     self.eye_color = 'blue'


# class Female(Human):
#     self.hair_length = '30cm'

# class Male(Human):
#     self.hair_length = '30cm'


# Female()


# class Country:
#     def __init__(self, country):
#         self.lanugage = 'english'
#         self.country = country 


# class City(Country)
#     def __init__(self):
#         pass
        


# x = City(Country('Australia'))

from logger import configure_logger

LOGGER = configure_logger(__name__)

class func_validation:

    def __init__(self, text_string):
        self.text_string = text_string
        # self.logger = logging.basicConfig(filename='app.log', 
        #                                   filemode='w', 
        #                                   format='%(name)s - %(levelname)s - %(message)s',
        #                                   datefmt='%H:%M:%S',
        #                                   level=logging.DEBUG)
        self.time_now = datetime.now().time()
        self.user = getpass.getuser()
        self.user_details = 'User: {0} Time: {1}'.format(self.time_now, self.user)

    def data_validator(self):
        if type(self.text_string) == str:
            print('This is a string')
            LOGGER.debug('1. Variable type = str, User: {1} Time: {0}'.format(self.time_now, self.user))

        elif type(self.text_string) == int:
            print('This is not a string but an integer')
            print('we are going to convert it to a string for you')
            LOGGER.debug('2. Variable type = int,  User: {0} Time: {1}'.format(self.time_now, self.user))

            try:
                self.text_string = str(self.text_string)
                #Is this a good idea, making the user details a variable rather than just calling the varaibles as above?
                LOGGER.debug('3. Sucessfully converted to string, ' + self.user_details)
            
            except Exception as error:
                print('Some other error happened')
                #Is this a good way of doing it? or should i do above? 
                LOGGER.error(f'4. The following error took place, {error}, {self.user_details}')
       
        else:
            print('5. This variable is not a String or an Integer')
            LOGGER.warning('The variable enetered was {0} type, havnt coded more than this part'.format(type(self.text_string)))

class sett_validation(object):

    def __init__(self, text_string):
        self.text_string = text_string

    @property
    def text_string(self):
        return self.text_string

    @text_string.setter
    def text_string(self, new_value) -> str:
        return str(self.text_string)
        # if type(new_value) == str:
        #     print('This is a string')
        # elif type(new_value) == int:
        #     print('This is not a string but an integer')
        #     print('we are going to convert it to a string for you')
            # try:
            #     self.text_string = str(self.text_string)
            # except:
            #     print('Some other error happened')

if __name__ == '__main__':
    func_validation('String?').data_validator()
    func_validation(100).data_validator()
    func_validation(pd.DataFrame()).data_validator()