#Script takes a list of software in a csv and returns the license type 
#by 1. hitting the github api
#or 2. attempting to parse the license file 

from github import Github #pip3 import PyGithub 
from github import Auth 
import csv
import os 

#repolist = ["kubernetes/kubernetes", "elastic/elasticsearch", "fluent/fluentd", "elastic/logstash"]
user = os.getenv('GITHUBUSER')
password = os.getenv('GITHUBPW')

data = csv.reader(open("license-tracker/software.csv", newline=''), delimiter=',')
with open('license-tracker/licenses.csv', mode="r") as infile:
    reader = csv.reader(infile)
    license_dict = {rows[0]:rows[11] for rows in reader}

print(license_dict)


g = Github(user,password)

with open('license-tracker/yourlicenses.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    for x in data: 
        if x[0] in license_dict:
            writer.writerow([x[0], x[1], license_dict[x[0]]])

        else: 
            checkrepo = str(g.get_repo(x[1]).license.name)
            if checkrepo == "Other":
                url = str(g.get_repo(x[1]).get_license().html_url)
                writer.writerow([x[0], x[1], checkrepo, url])
            else:
                writer.writerow([x[0], x[1], checkrepo])