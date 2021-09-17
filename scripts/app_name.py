import json, requests, os
from dotenv import load_dotenv
from global_var import app_names

load_dotenv()

print("\nStarting script -> APP_NAMES" + "\n*******************\n")

for i in range(len(app_names)):
	app_name_data = {
		"app_name": app_names[i]
	}
	jsonData = json.dumps(app_name_data)

	headers = {
		'Content-Type': os.environ['HEADER'],
		'accept': os.environ['HEADER']
	}
	post_url = os.environ['APP_POST_URL']
	sendData = requests.post(post_url, headers=headers, data=jsonData)

print("\nOperation has finished" + "\n*******************")