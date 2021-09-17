import json, requests, os, re
from dotenv import load_dotenv
from chrome_driver import driver
from global_var import app_names, current_url, current_xpath

load_dotenv()

print("\nStarting script -> CURRENT_VERSION" + "\n*******************\n")
driver.get('https://artifactory.gdn-app.com/artifactory/api/system/version')
current_data = driver.find_element_by_tag_name("body").text
print(current_data)
# print(driver.page_source)

# for idx, i in enumerate(current_url):

# 	print("Getting the CURRENT_VERSION of " + i)
# 	for index, x in enumerate(current_url[i]):
# 		print("X: ", x)
# 		print("Current XPath: ", current_xpath[i])
# 		print("List data: ", current_xpath[i][index])

# 		driver.get(x)
# 		try:
# 			current_data = driver.find_element_by_xpath(current_xpath[i][index]).text
# 			print(current_data)
# 		except:
# 			print("Error: Whether XPath is incorrect or no element was found")

# 		# req_body = {
# 		# 	"id_app": app_names[idx+1],
# 		# 	"current_version": current_data,
# 		# 	"keterangan": x
# 		# }
# 		# jsonData = json.dumps(req_body)

# 		# headers = {
# 		# 	'Content-Type': os.environ['HEADER'],
# 		# 	'accept': os.environ['HEADER']
# 		# }
# 		# post_url = os.environ['CURRENT_POST_URL']
# 		# sendData = requests.post(post_url, headers=headers, data=jsonData)
driver.quit()

print("\nOperation has finished" + "\n*******************")