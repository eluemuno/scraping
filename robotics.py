from RPA.Browser.Selenium import Selenium, By
import re
from datetime import datetime
from dateutil import relativedelta
import textwrap

br = Selenium()


class Robot:
    def __init__(self, name, url, scientist):
        self.name = name
        self.url = url
        self.scientist = scientist

    def say_hello(self):
        print("")
        print(" Hello, my name is " + self.name + ".")
        print(" I will show some information about " + self.scientist + " from Wikipedia in the following order: ")
        print(" -  The first paragraph of " + self.scientist + "'s page, ")
        print(" -  The birth date, ")
        print(" -  The death date, ")
        print(" -  The age at death.")
        print("")

    def say_goodbye(self):
        print("")
        print("This is " + self.name + ", thank you and goodbye.")
        br.close_all_browsers()

    def get_first_paragraph(self):
        br.open_available_browser(self.url + self.scientist)
        # The page for Marrie Curie has a slightly different layout,
        # I have added this little logic below to cater to the difference.
        if self.scientist == 'Marie Curie':
            first_paragraph = br.find_element('xpath://p[3]').text
        else:
            first_paragraph = br.find_element('xpath://p[2]').text
        print("")
        print("First Wikipedia page paragraph:")
        print(textwrap.fill(first_paragraph, 100))

    def get_birth_death_dates(self):
        br.open_available_browser(self.url + self.scientist)
        dob = br.find_element('class:bday').get_attribute("innerHTML")
        # The page for Marrie Curie has a slightly different layout,
        # I have added this little logic below to cater to the difference.
        if self.scientist == 'Marie Curie':
            death_ = br.find_element('xpath://table/tbody/tr[5]/td[1]').get_attribute("innerHTML")
        else:
            death_ = br.find_element('xpath://table/tbody/tr[4]/td[1]').get_attribute("innerHTML")
        dod = re.sub(r"[([{})\]]", "", re.findall(r'\(.*?\)', death_)[0])
        print("")
        print(self.scientist + "'s birth date was: " + dob)
        print("")
        print(self.scientist + "'s death date was: " + dob)
        print("")

        dob_formatted = datetime.strptime(dob, "%Y-%m-%d")
        dod_formatted = datetime.strptime(dod, "%Y-%m-%d")

        date_delta = relativedelta.relativedelta(dod_formatted, dob_formatted)

        print(self.scientist + " was " + str(date_delta.years) + " years old")
