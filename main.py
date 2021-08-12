from bs4 import BeautifulSoup
import requests
import csv

def remove_pararaph(args):
    """ remove paragraph tags from the string"""
    args = args.replace("<p>","")
    args = args.replace("</p>", "")
    return args

def split_the_break(args):
    """remove the breaks and creates a list"""
    Quest = []
    Quest = args.split("<br/>")
    return Quest

filename = "prettified.html"

try:
    #This will open the TCS Answer Key File. It is necessary to open it as utf8 encoding
    with open(filename, encoding="utf8") as html_file:
        soup = BeautifulSoup(html_file, 'lxml')
        whole_question_table = []
        counter =0
        for question in soup.find_all('p'):
            good_question_list = split_the_break(remove_pararaph(str(question)))

            """the for loop given below will remove all newlines and whitespaces"""
            for i in range(6):
                good_question_list[i] = good_question_list[i].strip()


            counter = counter +1
            question_no = good_question_list[0].split(".")[0]
            good_question_list.insert(0,"DSSSB SET 1 : Q"+question_no)

            """apending the questions to main big table"""
            whole_question_table.append(good_question_list)
        print("No. of questions PARSED from HTML FILE = {}".format(counter))
    """Everything has been parsed till this stage"""
    """Now, i am going to parse this to a CSV file"""
    with open("Parsed_Questions.csv","a",encoding="utf8") as comp_csv:
        comp_csv_reader = csv.reader(comp_csv)
        comp_csv_writer = csv.writer(comp_csv)
        print("File ","Parsed_Questions.csv"," created")
        counter = 0
        for com_ques_row in whole_question_table:
            comp_csv_writer.writerow(com_ques_row)
            counter+=1
        whole_question_table.clear() #CLEARING the comprehension table after writing all the comprehension questions
    print("Successful parsed {} questions".format(counter))



except FileNotFoundError:
    print("File does not exists!")