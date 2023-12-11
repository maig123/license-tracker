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

data = csv.reader(open("license-tracker/repos.csv", newline=''), delimiter=',')
g = Github(user,password)

with open('license-tracker/license.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for x in data: 
        test = str(g.get_repo(x[1]).license.name)
        if test == "Other":
            url = str(g.get_repo(x[1]).get_license().html_url)
            writer.writerow([x[0], x[1], test, url])
        else:
            writer.writerow([x[0], x[1], test])

#container image name to github repo to lookup information. is there a better way of doing this? 
container_dict = {
    
    'quay.io/prometheus/prometheus': "prometheus/prometheus",
    'grafana/grafana': "grafana/grafana",
    'docker.elastic.co/elasticsearch/elasticsearch': "elasticsearch/elasticsearch",
    'docker.elastic.co/kibana/kibana': "elasticsearch/kibana",

}