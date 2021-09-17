import json, requests, os
from dotenv import load_dotenv
from chrome_driver import driver
from global_var import app_names, latest_url, latest_xpath, releaseNote_url

load_dotenv()

print("\nStarting script -> LATEST_VERSION" + "\n*******************\n")

for i in range(len(app_names)):
	latestVersion = ""
	releaseNotes = releaseNote_url[i]
	
	print("Getting the Latest Version and Release Notes of " + app_names[i])
	driver.get(latest_url[i])
	try:
		latest_data = driver.find_element_by_xpath(latest_xpath[i]).text
		latestVersion = latest_data
	except:
		print("Error: Whether XPath is incorrect or no element was found")

	req_body = {
		"id_app": i+1,
 		"latest_version": latestVersion, 
		"release_notes": releaseNotes
	}
	jsonData = json.dumps(req_body)

	headers = {
		'Content-Type': os.environ['HEADER'],
		'accept': os.environ['HEADER']
	}
	post_url = os.environ['LATEST_POST_URL']
	sendData = requests.post(post_url, headers=headers, data=jsonData)
driver.quit()

print("\nOperation has finished" + "\n*******************")