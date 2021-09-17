import json, requests, os
from dotenv import load_dotenv
from chrome_driver import driver
from global_var import app_names, cve_url, cve_xpath

load_dotenv()

print("\nStarting script -> CVE" + "\n*******************\n")

for i in range(len(app_names)):
	cves = ""
	driver.get(cve_url[i])
	index = [3,5,7,9]
	print("Getting the CVEs of " + app_names[i])
	for idx in index:
		try:
			xpath_data = driver.find_element_by_xpath(cve_xpath % idx).text + " @@@" # add delimiter 
			cves += xpath_data
		except:
			print("Error: Can't get anymore data from " + app_names[i] + "\nReason: Index is out of bound" + "\n*******************")

	req_body = {
		"id_app": i+1,
		"cve": cves,
		"cve_link": cve_url[i]
	}
	jsonData = json.dumps(req_body)

	headers = {
		'Content-Type': os.environ['HEADER'],
		'accept': os.environ['HEADER']
	}
	post_url = os.environ['CVE_POST_URL']
	sendData = requests.post(post_url, headers=headers, data=jsonData)
driver.quit()

print("\nOperation has finished" + "\n*******************")