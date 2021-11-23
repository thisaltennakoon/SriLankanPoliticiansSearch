import json
import re
from googletrans import Translator
import time


class Politician:
    def __init__(self):
        self.name = ''
        self.position = ''
        self.party = ''
        self.district = ''
        self.contact_information = ''
        self.overall_rank = ''
        self.participated_in_parliament = ''
        self.related_subjects = ''
        self.date_of_birth = ''
        self.gender = ''
        self.school = ''
        self.first_degree = ''
        self.post_grads = ''
        self.terms_in_parliament = ''
        self.biography = ''

    def print_me(self):
        print("name: " + self.name)
        print("position: " + self.position)
        print("party: " + self.party)
        print("district: " + self.district)
        print("contact_information: " + str(self.contact_information))
        print("overall_rank: " + self.overall_rank)
        print("participated_in_parliament: " + self.participated_in_parliament)
        print("related_subjects: " + str(self.related_subjects))
        print("date_of_birth: " + str(self.date_of_birth))
        print("gender: " + self.gender)
        print("school: " + str(self.school))
        print("first_degree: " + self.first_degree)
        print("post_grads: " + self.post_grads)
        print("terms_in_parliament: " + self.terms_in_parliament)
        print("biography: " + self.biography)
        print("=======================================================================\n")


politicians = []
file1 = open('scraped.txt', 'r', encoding="UTF-8")
Lines = file1.readlines()

for line in Lines:
    temp = json.loads(line)
    politician = Politician()
    politician.name = temp['name']
    politician.position = temp['position']
    politician.party = temp['party']
    politician.district = temp['district']
    politician.contact_information = temp['contact_information']
    politician.overall_rank = temp['overall_rank']
    politician.participated_in_parliament = temp['participated_in_parliament']
    politician.related_subjects = temp['related_subjects']
    politician.date_of_birth = temp['date_of_birth']
    politician.gender = temp['gender']
    politician.school = temp['school']
    politician.first_degree = temp['first_degree']
    politician.post_grads = temp['post_grads']
    politician.terms_in_parliament = temp['terms_in_parliament']
    politician.biography = temp['biography']

    politicians.append(politician)


def remove_new_lines():
    for politician in politicians:
        politician.name = politician.name.strip()
        politician.position = politician.position.strip()
        politician.party = politician.party.strip()
        politician.district = politician.district.strip()

        temp_contact_information = []
        for i in politician.contact_information:
            temp_contact_information.append(i.strip())
        politician.contact_information = temp_contact_information

        politician.overall_rank = politician.overall_rank.strip()
        politician.participated_in_parliament = politician.participated_in_parliament.strip()

        temp_related_subjects = []
        for i in politician.related_subjects:
            temp_related_subjects.append(i.strip())
        politician.related_subjects = temp_related_subjects

        politician.date_of_birth = politician.date_of_birth.strip()
        politician.gender = politician.gender.strip()

        temp_school = []
        for i in politician.school:
            temp_school.append(i.strip())
        politician.school = temp_school

        politician.first_degree = politician.first_degree.strip()
        politician.post_grads = politician.post_grads.strip()
        politician.terms_in_parliament = politician.terms_in_parliament.strip()
        politician.biography = politician.biography.strip()


# remove \t characters
def remove_tab_chars():
    for politician in politicians:
        politician.name = politician.name.replace("\t", "")
        politician.position = politician.position.replace("\t", "")
        politician.party = politician.party.replace("\t", "")
        politician.district = politician.district.replace("\t", "")

        temp_contact_information = []
        for i in politician.contact_information:
            temp_contact_information.append(i.replace("\t", ""))
        politician.contact_information = temp_contact_information

        politician.overall_rank = politician.overall_rank.replace("\t", "")
        politician.participated_in_parliament = politician.participated_in_parliament.replace("\t", "")

        temp_related_subjects = []
        for i in politician.related_subjects:
            temp_related_subjects.append(i.replace("\t", ""))
        politician.related_subjects = temp_related_subjects

        politician.date_of_birth = politician.date_of_birth.replace("\t", "")
        politician.gender = politician.gender.replace("\t", "")

        temp_school = []
        for i in politician.school:
            temp_school.append(i.replace("\t", ""))
        politician.school = temp_school

        politician.first_degree = politician.first_degree.replace("\t", "")
        politician.post_grads = politician.post_grads.replace("\t", "")
        politician.terms_in_parliament = politician.terms_in_parliament.replace("\t", "")
        politician.biography = politician.biography.replace("\t", "")


def remove_extra_spaces():
    for politician in politicians:

        politician.name = re.sub(' +', ' ', politician.name)
        politician.position = re.sub(' +', ' ', politician.position)
        politician.party = re.sub(' +', ' ', politician.party)
        politician.district = re.sub(' +', ' ', politician.district)

        temp_contact_information = []
        for i in politician.contact_information:
            temp_contact_information.append(re.sub(' +', ' ', i))
        politician.contact_information = temp_contact_information

        politician.overall_rank = re.sub(' +', ' ', politician.overall_rank)
        politician.participated_in_parliament = re.sub(' +', ' ', politician.participated_in_parliament)

        temp_related_subjects = []
        for i in politician.related_subjects:
            temp_related_subjects.append(re.sub(' +', ' ', i))
        politician.related_subjects = temp_related_subjects

        politician.date_of_birth = re.sub(' +', ' ', politician.date_of_birth)
        politician.gender = re.sub(' +', ' ', politician.gender)

        temp_school = []
        for i in politician.school:
            temp_school.append(re.sub(' +', ' ', i))
        politician.school = temp_school

        politician.first_degree = re.sub(' +', ' ', politician.first_degree)
        politician.post_grads = re.sub(' +', ' ', politician.post_grads)
        politician.terms_in_parliament = re.sub(' +', ' ', politician.terms_in_parliament)
        politician.biography = re.sub(' +', ' ', politician.biography)


def decodeEmail(e):
    de = ""
    k = int(e[:2], 16)

    for i in range(2, len(e) - 1, 2):
        de += chr(int(e[i:i + 2], 16) ^ k)

    return de


def decode_email_address():
    for politician in politicians:
        try:
            politician.contact_information[1] = decodeEmail(politician.contact_information[1])
        except:
            pass


# replace wijitha හේරත් with විජිත හේරත්
politicians[212].name = "විජිත හේරත්"

# remove "#" from the begining of the overall_rank
for politician in politicians:
    politician.overall_rank = politician.overall_rank[1:]

# replece male and පිරිමි values in gender
for politician in politicians:
    if politician.gender == "male" or politician.gender == "පිරිමි":
        politician.gender = "පුරුෂ"


def translate_school_names():
    translator = Translator()
    for politician in politicians:
        if len(politician.school) == 1 and politician.school[0] == '':
            continue
        temp_school = []
        for i in politician.school:
            if i == '':
                continue
            temp_school.append(translator.translate(i, src='en', dest='si').text)
            time.sleep(2)
        politician.school = temp_school


def translate_first_degree():
    translator = Translator()
    for politician in politicians:
        if politician.first_degree == '':
            continue
        else:
            politician.first_degree = translator.translate(politician.first_degree, src='en', dest='si').text
            time.sleep(2)


def translate_first_degree():
    translator = Translator()
    for politician in politicians:
        if politician.post_grads == '':
            continue
        else:
            politician.post_grads = translator.translate(politician.post_grads, src='en', dest='si').text
            time.sleep(2)


def generate_biography():
    for politician in politicians:
        if not (politician.date_of_birth == ''):
            politician.biography += politician.name
            if politician.gender == 'පුරුෂ' or politician.gender == "පිරිමි":
                politician.biography += " මහතා "
            elif politician.gender == "ස්ත්‍රී":
                politician.biography += " මහත්මිය "
            politician.biography += politician.date_of_birth + " දින උපත ලබා ඇත."

        if not (politician.school[0] == ''):
            if politician.gender == 'පුරුෂ' or politician.gender == "පිරිමි":
                politician.biography += "මෙතුමා "
            else:
                politician.biography += "මෙතුමිය "
            for i in politician.school:
                politician.biography += i + " "
            if len(politician.school) > 1:
                politician.biography += "යන පාසල්වල අධ්යාපනය ලබා ඇත."
            else:
                politician.biography += "යන පාසලේ අධ්යාපනය ලබා ඇත."
        if not (politician.first_degree == ''):
            politician.biography += "තම ප්‍රථම උපාධිය " + politician.first_degree + " ලබාගෙන ඇත."
        if not (politician.post_grads == ''):
            politician.biography += 'ඊට අමතරව ' + politician.post_grads + ' පශ්චාත් උපාධිය ද සම්පූර්ණ කර ඇත.'
        politician.biography += politician.terms_in_parliament + " " + politician.party + " නියෝජනය කරමින් පාර්ලිමේන්තුවේ අසුන් ගෙන සිටී."


remove_new_lines()
remove_extra_spaces()
remove_tab_chars()
decode_email_address()
generate_biography()

file1 = open("preprocessed.json", "a", encoding="UTF-8")  # append mode
file1.write("[")
for politician in politicians:
    file1.write(json.dumps(politician.__dict__, ensure_ascii=False))
    file1.write(",")
    politician.print_me()
file1.write("]")
file1.close()
