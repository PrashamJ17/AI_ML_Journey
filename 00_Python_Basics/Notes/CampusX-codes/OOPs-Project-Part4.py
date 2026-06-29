# OOP - PROJECT
# NLP - CLOUD Playground

# NLP cloud - API provider - 
# API - Application Programming Interface - its like a function that is present on a server
# we want to access some that function of the server, and to access that server we need its URL > which is called API , that connects us with that function and gives output on the basis of right inputs . 

# import nlpcloud

# client = nlpcloud.Client("gpt-oss-120b", "", gpu=True)
# client.entities(
#     """John Doe started learning Javascript when he was 15 years old. After a couple of years he switched to Python and starter learning low level programming. He is now a Go expert at Google.""",
#     searched_entity="programming languages"
# )


# what are we making ? 
# - we are making a CLI/terminal app that has login/register features , like a real app 
# - the app will privde different functionalities or uses - 1. NER (entity extraction) 2. Sentiment Analysis 3. Language Detection
# - All the above use some ML in the background 
# - What will we do is we will will create our own frontent - taking inputs from the user and then sending those inputs to the backend where the functions will work and give the output
# - the backend is some ML programming - which we will access via API from NLP cloud
# - The output from the server is fetched and displayed on the terminal 

# STEPS - 
# 1. create a login/register/exit page or first-menu 
# 2. if new user -> register -> after register login again
# 3. Store the credentials in a dictionary database - with key as email - as every user has a unique email 
# 4. 'email' = ['name','password'] 
# 5. for already a user - login - 
# i) first check if the email is present  
# ii) if not then send to register page
# iii) if the email verifies then check the password 
# iv) if incorrect - then try again - maxm 3 tries or loop 
# v) you can add an option of forget password -> enter new password ,
# 6. After login - show user second-menu of uses/functions
# 7. show all the 3 functions - ask user to choose 
# 8. then take inputs from the user -> fetch the output -> display
# 9. Ask if he want to go again or switch to different function or exit .
# 10. Exit


# Classes - 
# 1. USER -  2. Login(USER) 3. Register(USER)  
# 2. For the functions 

import nlpcloud
class User:

    __database = {}

    def __init__(self):

        self.__name = ''
        self.__email = ''
        self.__pswd = ''

        self.__first_menu()

    @classmethod
    def get_db(cls):
        return cls.__database

    def __first_menu(self):

        first_menu = input('''Welcome To Prasham's NLP APP!\n\n1. Already a User ? Login - Type 1 \n2. New User ?  Register Type 2 \n3. Exit? Type 3\n''')
        if first_menu == '1' :
            self.__login()
        elif first_menu == '2' :
            self.__register()
        else :
            exit()
    
    def __login(self):

        print('Login Page !\n')

        self.__email = input('Enter Email : \n')

        if self.__email not in User.__database :
            print('\nEmail Not Registered!\n')
            new_user = input('New User? Register - Type 2\n')
            if new_user == '2':
                self.__register()
            else :
                self.__first_menu()
            
        self.__pswd = input('Enter Password : \n') 

        if self.__pswd != User.__database[self.__email][1] :
            print('Incorrect Password! Try Again\n') 
            forget_pswd = input('Forget Password ? Set New Password - Type 2\nGo to Login - Type 1\n')
            if forget_pswd == '1':
                self.__pswd = input('\nEnter Password : \n')
                User.__database[self.__email][1] = self.__pswd
                print("\nPassword Set !")
                self.__login()
            elif forget_pswd == '2' :
                self.__login()
        else:
            self.__second_menu()

    def __register(self):
        
        print('Register Page ! \n')

        self.__name = input('Enter Name : \n')

        self.__email = input('Enter Email : \n')
        if '@' not in self.__email :
            print('Incorrect Email')
            self.__email = input('Enter Email : \n')
        
        self.__pswd = input('Enter Password : \n')

        User.__database[self.__email] = [self.__name,self.__pswd]
        print(f"{self.__email} Registered Successfully !")

        self.__login()

    def __second_menu(self):
        print('\nWelcome !\n')

        second_menu = input('''\nUse Cases - \n1. NER - Entity Extraction - To use Type 1\n2. Language Detection - To use Type 2\n3. Sentiment Analysis - To use Type 3\n4. To Exit - Type 4\n''')
        if second_menu == '1':
            NLPService.Ner()
        elif second_menu == '2':
            NLPService.Lang_Det()
        elif second_menu == '3':
            NLPService.Sent_Ana()
        else :
            exit()
    
class NLPService :

    @staticmethod
    def Ner():
        print('Entity Extraction')

    @staticmethod
    def Lang_Det():
        print('Language Detection')

    @staticmethod
    def Sent_Ana():
        
        para = input('Enter The Paragraph')

        client = nlpcloud.Client("distilbert-base-uncased-emotion", "2b58d7fb9af09e617ee525e78c7766b6d8c5bb61", gpu=False, lang="en")
        response = client.sentiment(para)

        print(response)

        # L = []
        # for i in response['scored_labels']:
        #     L.append(i['score'])

        # index = sorted(list(enumerate(L)),key=lambda x:x[1],reverse=True)[0][0]

        # print(response['scored_labels'][index]['label'])


us1 = User()


# class User:

#     __database = {}

#     def __init__(self):

#         self.__name = ''
#         self.__email = ''
#         self.__pswd = ''

#         # self.__first_menu()

#     @classmethod
#     def get_db(cls):
#         return cls.__database

#     def __first_menu(self):

#         first_menu = input('''Welcome To Prasham's NLP APP!\n\n1. Already a User ? Login - Type 1 \n2. New User ?  Register Type 2 \n3. Exit? Type 3\n''')
#         if first_menu == '1' :
#             Login().__login()
#         elif first_menu == '2' :
#             Register().__register()
#         else :
#             exit()
    


# class Login(User):
#     def __init__(self):
#         super().__init__()
#         self.__login()

#     def __login(self):

#         print('Login Page !\n')

#         self.__email = input('Enter Email : \n')

#         if self.__email not in User.get_db() :
#             print('\nEmail Not Registered!\n')
#             new_user = input('New User? Register - Type 2\n')
#             if new_user == '2':
#                 Register().__register()
#             else :
#                 self.__first_menu()
            
#         self.__pswd = input('Enter Password : \n') 

#         if self.__pswd != User.get_db()[self.__email][1] :
#             print('Incorrect Password! Try Again\n') 
#             forget_pswd = input('Forget Password ? Set New Password - Type 2\nGo to Login - Type 1\n')
#             if forget_pswd == '1':
#                 self.__pswd = input('\nEnter Password : \n')
#                 User.get_db()[self.__email][1] = self.__pswd
#                 print("\nPassword Set !")
#                 self.__login()
#             elif forget_pswd == '2' :
#                 self.__login()
#         else:
#             NLPService()


#         # def __second_menu(self):
#         #     print('\nWelcome !\n')

#         #     second_menu = input('''\nUse Cases - \n1. NER - Entity Extraction - To use Type 1\n2. Language Detection - To use Type 2\n3. Sentiment Analysis - To use Type 3\n4. To Exit - Type 4\n''')
#         #     if second_menu == '1':
#         #         NLPService.__Ner()
#         #     elif second_menu == '2':
#         #         NLPService.__Lang_Det()
#         #     elif second_menu == '3':
#         #         NLPService.__Sent_Ana()
#         #     else :
#         #         exit()
        
# class Register(User):

#     def __init__(self):
#         super().__init__()
#         self.__register()
    
#     def __register(self):
        
#         print('Register Page ! \n')

#         self.__name = input('Enter Name : \n')

#         self.__email = input('Enter Email : \n')
#         if '@' not in self.__email :
#             print('Incorrect Email')
#             self.__email = input('Enter Email : \n')
        
#         self.__pswd = input('Enter Password : \n')

#         User.get_db()[self.__email] = [self.__name,self.__pswd]
#         print(f"{self.__email} Registered Successfully !")

#         Login().__login()
    

# class NLPService :

#     def __init__(self):

#         print('\nWelcome !\n')

#         second_menu = input('''\nUse Cases - \n1. NER - Entity Extraction - To use Type 1\n2. Language Detection - To use Type 2\n3. Sentiment Analysis - To use Type 3\n4. To Exit - Type 4\n''')
#         if second_menu == '1':
#             self.__Ner()
#         elif second_menu == '2':
#             self.__Lang_Det()
#         elif second_menu == '3':
#             self.__Sent_Ana()
#         else :
#             exit()
    
#     @staticmethod
#     def __Ner():
#         pass

#     @staticmethod
#     def __Lang_Det():
#         pass

#     @staticmethod
#     def __Sent_Ana():
#         pass


# us1 = Login()