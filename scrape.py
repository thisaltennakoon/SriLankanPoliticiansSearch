import requests
import json
from bs4 import BeautifulSoup


def get_MP_profile_url_list():
    MP_profile_url_list = []
    for page in range(1, 10):
        URL = "https://www.manthri.lk/si/politicians?page=" + str(page)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        people_list = soup.find("ul", class_="people-list")
        job_elements = people_list.find_all("li")

        for i in job_elements:
            temp = str(i.find("h4").find("a"))
            temp_soup = BeautifulSoup(temp, 'html.parser')
            el = temp_soup.find(href=True)
            MP_profile_url_list.append("https://www.manthri.lk" + el['href'])
    return MP_profile_url_list


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


file1 = open("scraped.txt", "a", encoding="UTF-8")  # append mode

count = 1
for mp in get_MP_profile_url_list():
    page = requests.get(mp)

    soup = BeautifulSoup(page.content, "html.parser")
    name_container = soup.find("div", class_="col-md-6 col-sm-6 col-xs-12")
    politician = Politician()
    politician.name = name_container.find("h1").text
    politician.position = name_container.find("p").text

    politician.party = name_container.find("div", class_="details").find("p").text.split(",")[0]
    politician.district = name_container.find("div", class_="details").find("p").text.split(",")[1]

    try:
        email_addresses = \
            name_container.find("div", class_="details").find("p", class_="contact").find_all("span")[1].find("span",
                                                                                                              class_="__cf_email__").attrs[
                'data-cfemail']
    except:
        email_addresses = ''

    politician.contact_information = [
        name_container.find("div", class_="details").find("p", class_="contact").find_all("span")[0].text,
        email_addresses]

    politician.overall_rank = soup.find("span", class_="rank-icon full").text
    politician.participated_in_parliament = soup.find("span", class_="rank-icon has-p").find("strong").text
    politician.related_subjects = []
    try:
        for i in soup.find("div", id="topics-list").find_all("p"):
            politician.related_subjects.append(i.text)
    except:
        pass

    temp_arr = soup.find("div", class_="row content-area bio").find_all("table")[0].find_all("td")
    for i in range(len(temp_arr)):
        if temp_arr[i].text == "ස්ත්‍රී පුරුෂ භාවය:":
            politician.gender = temp_arr[i + 1].text
        if temp_arr[i].text == "උපන්දිනය:":
            politician.date_of_birth = temp_arr[i + 1].text
    try:
        politician.gender = soup.find("div", class_="row content-area bio").find_all("table")[0].find_all("td")[3].text
    except:
        pass

    temp_arr = soup.find("div", class_="row content-area bio").find_all("table")[1].find_all("td")
    for i in range(len(temp_arr)):
        if temp_arr[i].text == "පාසැල:":
            politician.school = [temp_arr[i + 1].text]
        if temp_arr[i].text == "පාසැල 2:":
            politician.school += [temp_arr[i + 1].text]
        if temp_arr[i].text == "පාසැල 3:":
            politician.school += [temp_arr[i + 1].text]
        if temp_arr[i].text == "පාසැල 4:":
            politician.school += [temp_arr[i + 1].text]
        if temp_arr[i].text == "පාසැල 5:":
            politician.school += [temp_arr[i + 1].text]
        if temp_arr[i].text == "ප්‍රථම උපාධිය:":
            politician.first_degree = temp_arr[i + 1].text
        if temp_arr[i].text == "පශ්චාත් උපාධිය:":
            politician.post_grads = temp_arr[i + 1].text

    politician.terms_in_parliament = \
        soup.find("div", class_="row content-area bio").find_all("table")[2].find_all("td")[0].text

    print(count),

    file1.write(json.dumps(politician.__dict__, ensure_ascii=False))
    file1.write("\n")
    count += 1

file1.close()
