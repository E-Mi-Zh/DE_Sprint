from requests_tor import RequestsTor
from bs4 import BeautifulSoup
from time import sleep
import json
import tqdm

req = RequestsTor()

data = {
    "data": []
}

for page in range(0, 5):
    url = f"https://hh.ru/search/vacancy?area=113&search_field=name&search_field=company_name&search_field=description&text=python+разработчик&page=(page)"
    resp = req.get(url)
    print(f"----- Page {page} -----")
    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all(class_ = "serp-item__title")
    #for iter in tqdm.tqdm(tags):
    for iter in tqdm.tqdm(tags):
        print(iter.attrs["href"])
        sleep(2)
        url_object = iter.attrs["href"]
        resp_object = req.get(url_object)
        print(resp_object.status_code)
        while resp_object.status_code != 200:
            sleep(2)
            resp_object = req.get(url_object)
            print(resp_object.status_code)
        soup_object = BeautifulSoup(resp_object.text, "lxml")
        tag_exp = soup_object.find(class_ = "vacancy-description-list-item").find(attrs = {"data-qa":"vacancy-experience"}).text
        tag_salary = soup_object.find(attrs = {"data-qa":"vacancy-salary"}).find(class_ = "bloko-header-section-2 bloko-header-section-2_lite").text
        tag_region = soup_object.find(attrs = {"data-qa":"vacancy-company"}).find(attrs = {"data-qa":"vacancy-view-raw-address"})
        if tag_region:
            tag_region = tag_region.text.split(sep=",")[0]
        else:
            tag_region = soup_object.find(attrs = {"data-qa":"vacancy-company"}).find(attrs = {"data-qa":"vacancy-view-location"}).text
        print(iter.text, tag_exp, tag_salary, tag_region, iter.attrs["href"])
        data["data"].append({"title":iter.text, "work experience": tag_exp, "salary": tag_salary, "region": tag_region})
        with open("home.json", "w") as file:
            json.dump(data, file, ensure_ascii=False)
