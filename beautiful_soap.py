
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")
print("This is the result:")
#print(results)
#print(results.prettify())


job_elements = results.find_all("div", class_="card-content")

#for job_element in job_elements:
  #  print(job_element, end="\n"*2)

# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print("This is the elment:")
#     print(title_element)
#     print(company_element)
#     print(location_element)
#     print()


# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print("These are the elements:")
#     print(title_element.text)
#     print(company_element.text)
#     print(location_element.text)
#     print()

# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()

#
# python_jobs = results.find_all("h2", string="Python")
# print(python_jobs)


python_jobs = results.find_all(
     "h2", string=lambda text: "python" in text.lower()
 )
 print(python_jobs)

 print(len(python_jobs))






python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

print(python_job_elements)

