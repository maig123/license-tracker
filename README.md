# license-tracker
Looks up GitHub license info for a set of software

# how it works 
uses pygithub to lookup the license from a list provided in list.csv with github's api. would require list of software to be exported to that csv file. output is placed in a licenses.csv file with the source, licensetype, license url. if license type is "Other", also adds the link to the license. 

