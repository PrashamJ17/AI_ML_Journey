# PRACTICE WQUESTINS OF ALL THE TOPICS DONE TILL NOW - TILL OOPs, exception handling , ...
# till - WEEK-4 + Additonal content


# p-1

def p1(games,scores):
    '''
    2 inputs - no. of games and a list of scores in each games
    We are maintaining 2 list - one for high scores and one for low scores
    Then we travese through both the list and check if i == i-1 , 
    if not then respective count increases by 1
    output - list of high score and low score record breaks
    '''

    high_scores = [] # high scores list after each game
    low_scores = [] # low scores list after each game
    low_count = 0 # count low score record break
    high_count = 0 # count high score record break

    max = scores[0]
    min = scores[0]
    high_scores.append(scores[0])
    low_scores.append(scores[0])

    # for i in range(1,games) : # for each game , high scre and low score

    #     if scores[i] > high_scores[i-1] :
    #         high_scores.append(scores[i]) # if higher score than previous one 
    #         high_count += 1
    #     else :
    #         high_scores.append(high_scores[i-1]) # if not then same higher score is same as previous one

    #     if scores[i] < low_scores[i-1] :
    #         low_scores.append(scores[i]) # if score lower than previous lowest score 
    #         low_count += 1
    #     else :
    #         low_scores.append(low_scores[i-1]) # if not then apend previous lowest score
    
    # print(high_scores)
    # print(low_scores)

    for i in range(games):
        if scores[i] > max :
            max = scores[i]
            high_count += 1
        if scores[i] < min :
            min = scores[i]
            low_count += 1

    
    return [high_count,low_count]

# total_rec_break = p1(9,[10,5,20,20,4,5,2,25,1])
# print(total_rec_break)


class Student :
    '''
    Accept - take input - name, roll no, marks for 2 subj - marks-1 , marks-2, 
    display - displays the details for every student
    search - searches for a particular stud from the list of students -> take roll no and then search as per roll no -> then display the details 
    delete - deletes the record of a particular student with roll no match 
    update - this method updates the roll no -> ask for old roll no and new roll no - replace old with new
    exit
    '''
    '''
    This will be a menu driven program - with 6 above optns 
    '''
    students = {} # dictionary to store details of each student

    def __init__(self): 
        self.__menu()
    
    def __menu(self):
        menu = input('''
1. Accept Student Details
2. Display Student Details
3. Search Details of a Student
4. Delete Detail of a student
5. Update Student Deauls
6. Exit
''')
        if menu == '1':
            self.p2_accept()
        elif menu == '2':
            self.p2_display()
        elif menu == '3':
            self.p2_search()
        elif menu == '4':
            self.p2_delete()
        elif menu == '5':
            self.p2_update()
        elif menu == '6' :
            exit()
        else :
            print('Wrong Input')
            self.__menu()
        
    def p2_accept(self) :
        name = input('\nEnter Name of Student: ')
        Roll_no = input('Enter Roll No of Student: ')
        Marks1 = input('Enter marks of subject-1: ')
        Marks2 = input('Enter marks of subject-2: ')
        Student.students[Roll_no] = {"Name" : name,"Roll No" :Roll_no,"Marks1" :Marks1,"Marks2":Marks2}
        self.__menu()
    
    def p2_display(self):
        print("\nList of Students : ")
        for i in Student.students :
            for j in Student.students[i] :
                print(f"{j} : {Student.students[i][j]}")
            print('\n')
        self.__menu()

    def p2_search(self):
        search_roll = input('\nEnter Roll No to search : ')
        if search_roll in Student.students :
            for i in Student.students[search_roll]:
                print(f"\n{i} : {Student.students[search_roll][i]}")
        else :
            print(f"{search_roll} roll no. Not Found")
        
        self.__menu()

    def p2_delete(self):
        del_roll = input("\nEnter roll no to delete : ")
        Student.students.pop(del_roll)

        print(Student.students)
        self.__menu()

    def p2_update(self):
        old_roll = input("\nEnter old Roll no : ")
        new_roll = input("Enter new Roll no : ")

        Student.students[new_roll] = Student.students[old_roll].copy() 
        Student.students[new_roll]['Roll No'] = new_roll
        Student.students.pop(old_roll)
    
        print(Student.students)

        self.__menu()

# s = Student()

import datetime,zoneinfo

def p3():

    timezones = {
        "UTC":             "UTC",
        "New York":        "America/New_York",
        "Los Angeles":     "America/Los_Angeles",
        "London":          "Europe/London",
        "Paris":           "Europe/Paris",
        "India (IST)":     "Asia/Kolkata",
        "Tokyo":           "Asia/Tokyo",
        "Sydney":          "Australia/Sydney",
        "Dubai":           "Asia/Dubai",
    }

    for labels,tz in timezones.items():
        now = datetime.datetime.now(zoneinfo.ZoneInfo(tz))
        print(f"{labels:<15} {now.strftime("%d/%m/%Y, %H:%M:%S %Z")}")

        # labels:<15 -> < means left align text and 15 is width 
        # <	-->Left-align the text
        # 15 -->Pad to a total width of 15 characters
# p3()

def p4(L):
    evens = [i for i in L if i%2==0]
    odds = [i for i in L if i%2!=0]

    print(f"Even = {len(evens)}, Odd = {len(odds)}")

# p4([2, 7, 5, 64, 14])

def p5(n):
    n = 64 + n
    for i in range(n,64,-1):
        for j in range(64,i-1):
            print("--",end='')
        for j in range(n,i-1,-1):
            print(f"{chr(j)}-",end='')
        for k in range(j+1,n+1):
            print(f"{chr(k)}-",end='')
        for j in range(64,i-1):
            print("--",end='')
        print("")


    for l in range(64,n-1):
        for m in range(64,l+1) :
            print("--",end='')
        for m in range(n,l+1,-1):
            print(f"{chr(m)}-",end='')
        for n in range(m+1,n+1):
            print(f"{chr(n)}-",end='')
        for m in range(64,l+1) :
            print("--",end='')
        print("")
        
# p5(10)

def p6(S):
    l = []
    count = 1
    for i in range(len(S)) :
        if i == len(S)-1:
            l.append((count,S[i]))
            break
        elif S[i] == S[i+1] :
            count += 1
        else :
            l.append((count,S[i]))
            count = 1
    output = ''
    for i in l :
        output += f"{i} "
    print(output)
        

# p6('1222311')

def p7():
    n = int(input(""))
    words_list = []
    words = []
    for i in range(n):
        word = input()
        if word not in words_list :
            words_list.append(word)
        words.append(word)
    
    print(len(words_list))
    for i in words_list :
        print(words.count(i),end = ' ')
    print()
    
# p7()

def p8() :
    n = int(input('Enter no. of english letters : '))
    alph = []
    for i in range(n):
        lett = input(f'Enter letter-{i+1} : ')
        alph.append(lett)
    k = int(input("Enter no of indices to select : "))

