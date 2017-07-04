from bs4 import BeautifulSoup
from lxml import html
import requests
from links import links


def get_page_data(page_url):
    info_output = ""
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, "lxml")

    company_logo = soup.find("div", "col-md-3").find("img").get("src")
    company_name = soup.find("div", "col-md-9").find("h3").string
    info_output += company_logo + " | "
    info_output += company_name + " | "

    data_areas = [soup.find("div", "col-md-9").find_all("tr"),
                  soup.find("div", "col-md-4").find_all("tr"),
                  soup.find("div", id="menu").find_all("tr"),
                  soup.find("div", id="menu1").find_all("tr"),
                  soup.find("div", id="menu3").find_all("tr"),
                  soup.find("div", id="menu4").find_all("tr")]

    for tr_item in data_areas:
        for td_item in tr_item:
            data_item = td_item.find_all("td")[-1].string
            if data_item is None:
                info_output += "none" + " | "
            else:
                info_output += data_item.replace("\r\n","").replace("\n","") + " | "

    info_output += info_output + page_url

    projects = company_name + " | "
    tr_projects = soup.find("div", id="menu2").find_all("tr")
    for td_item in tr_projects:
        data_item = td_item.find_all("td")[-1].string
        if data_item is None:
            info_output += "none" + " | "
        else:
            projects += data_item.replace("\n","") + " | "

    return info_output, projects

data_out_file = open("teknoag.csv", "a")
projects_out_file = open("projects.csv", "a")


i=1
for link in links:
    print(str(i)+" "+link)
    # Create a tuple
    link.replace("\r\n", "")
    link.replace("\n", "")
    tpl = get_page_data(page_url=link)
    # Save information data
    data_out_file.writelines(tpl[0])
    data_out_file.writelines("\n")
    # Save projects data
    projects_out_file.writelines(tpl[1])
    projects_out_file.writelines("\n")
    i += 1