import io
import csv
import pandas as pd
from bs4 import BeautifulSoup
from soup import the_soup


soup = BeautifulSoup(the_soup, "html.parser")

dl_elements = soup.find_all("dl")

data = []

for dl_element in dl_elements:
    company_name = dl_element.find("span").text

    about = dl_element.find("dd").find_all("p")[1].text

    benefits = dl_element.find("dd").find_all("p")[3].text

    data.append([company_name, about, benefits])

with open("gitdata.xls", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Company Name", "About", "Benefits"])

    for row in data:
        writer.writerow(row)

