app_names = [
    'Bitbucket',
    'Artifactory',
    'Bamboo', 
    'Jenkins',
    'Prometheus',
    'Jira',
    'Confluence',
    'SonarQube',
    'Grafana'
]

current_url = {
    'Bitbucket': [
        'https://stash.gdn-app.com/login'
    ],
    'Artifactory': [
        'https://artifactory.gdn-app.com/artifactory/api/system/version'
    ],
    'Bamboo': [
        'https://bamboo.gdn-app.com/'
    ],
    'Jenkins': [
        'https://jenkins-np-gcp.gdn-app.com/',
        'https://prodjenkins-gcp.gdn-app.com/',
        'https://nonprod-infrajenkins.gdn-app.com/'
        # 'https://nonprod-deployjenkins.gdn-app.com/',
        # 'https://prod-infrajenkins.gdn-app.com/',
        # 'https://proddevopsjenkins.gdn-app.com/'
    ],
    'Prometheus': [
        'https://prometheus-prod-gcp.gdn-app.com/status',
        'https://prod-prometheus.gdn-app.com/status'
    ],
    'Jira': [
        'https://jira.gdn-app.com/'
    ],
    'Confluence': [
        'https://confluence.gdn-app.com'
    ],
    'SonarQube': [
        'https://sonar.gdn-app.com/api/server/version'
    ],
    'Grafana': [
        'https://grafana-prod-gcp.gdn-app.com/',
        'https://grafana-np-gcp.gdn-app.com',
        'https://prod-grafana.gdn-app.com'
    ]
}

current_xpath = {
    'Bitbucket': [
        "//*[@id='product-version']"
    ],
    'Artifactory': [
        "(//*[@id='json']//span[@class='type-string'])[1]"
    ],
    'Bamboo': [
        "//div[@class='footer-body']/p/text()[2]"
    ],
    'Jenkins': [
        'https://jenkins-np-gcp.gdn-app.com/',
        'https://prodjenkins-gcp.gdn-app.com/',
        'https://nonprod-infrajenkins.gdn-app.com/'
        # 'https://nonprod-deployjenkins.gdn-app.com/',
        # 'https://prod-infrajenkins.gdn-app.com/',
        # 'https://proddevopsjenkins.gdn-app.com/'
    ],
    'Prometheus': [
        'https://prometheus-prod-gcp.gdn-app.com/status',
        'https://prod-prometheus.gdn-app.com/status'
    ],
    'Jira': [
        'https://jira.gdn-app.com/'
    ],
    'Confluence': [
        'https://confluence.gdn-app.com'
    ],
    'SonarQube': [
        'https://sonar.gdn-app.com/api/server/version'
    ],
    'Grafana': [
        'https://grafana-prod-gcp.gdn-app.com/',
        'https://grafana-np-gcp.gdn-app.com',
        'https://prod-grafana.gdn-app.com'
    ]
}

for idx, i in enumerate(current_url):
    print("\nlength curr ",  len(current_url))
    print("\ncurrent ver ", i)
    print("\nindex ", idx)
    print("\n", current_url[i])
    xpath_list = current_xpath[i]
    print("\nXPATH:  ", xpath_list)
    # for idx2, x in enumerate(current_url[i]):
    #     print("list data ke ", idx2, x)
    #     print("xpath ", current_xpath[i])
    #     print("length list ", len(current_url[i]))

cve_url = [
    'https://www.cvedetails.com/vulnerability-list/vendor_id-3578/product_id-36995', # Bitbucket
    'https://www.cvedetails.com/vulnerability-list/vendor_id-15996/product_id-35352', # Artifactory
    'https://www.cvedetails.com/vulnerability-list/vendor_id-3578/product_id-22350', # Bamboo
    'https://www.cvedetails.com/vulnerability-list/vendor_id-15865/product_id-34004', # Jenkins
    'https://www.cvedetails.com/vulnerability-list/vendor_id-20905/product_id-61503', # Prometheus
    'https://www.cvedetails.com/vulnerability-list/vendor_id-3578/product_id-8170', # Jira
    'https://www.cvedetails.com/vulnerability-list/vendor_id-3578/product_id-6258', # Confluence
    'https://www.cvedetails.com/vulnerability-list/vendor_id-12999/product_id-26632', # SonarQube
    'https://www.cvedetails.com/vulnerability-list/vendor_id-18548/product_id-47055' # Grafana
]

cve_xpath = "//*[@id='vulnslisttable']/tbody/tr[%s]"

latest_url = [
    'https://www.atlassian.com/software/bitbucket/download-archives', # BitBucket
    'https://www.jfrog.com/confluence/display/JFROG/Artifactory+Release+Notes', # Artifactory
    'https://www.atlassian.com/software/bamboo/download', # Bamboo
    'https://github.com/jenkinsci/jenkins/releases', # Jenkins
    'https://github.com/prometheus/prometheus/tags', # Prometheus
    'https://www.atlassian.com/software/jira/update', # Jira
    'https://www.atlassian.com/software/confluence/download-archives', # Confluence
    'https://www.sonarqube.org/downloads/', # SonarQube
    'https://github.com/grafana/grafana/tags' # Grafana
]

latest_xpath = xpath = [
    "//*[@id='accordion-view']//p/a[contains(@class,'product-versions')]", # BitBucket
    "//*[@id='main-content']/div/div[2]//h2[contains(text(), 'Artifactory')][1]", # Artifactory
    "//*[@id='download-view']/div/h4", # Bamboo
    "(//div[contains(@class,'repository-content')]//h1[contains(.,'LTS release')])[1]", # Jenkins
    "//*[@class='Box']/div[2]//h4/a", # Prometheus
    "//*[@id='accordion-view']//p/a[contains(@class,'product-versions')]", # Jira
    "//*[@id='accordion-view']//p/a[contains(@class,'product-versions')]",# Confluence
    "(//*[@id='download']//*[contains(text(),'LTS')])[1]", # SonarQube
    "//*[@class='Box']/div[2]//h4/a" # Grafana
]

releaseNote_url = [
    "https://www.atlassian.com/software/bitbucket/download-archives", # Bitbucket
    "https://www.jfrog.com/confluence/display/JFROG/Artifactory+Release+Notes", #Jfrog
    "https://www.atlassian.com/software/bamboo/download", #Bamboo
    "https://www.jenkins.io/download/", #Jenkins
    "https://github.com/prometheus/prometheus/releases", #Prometheus
    "https://www.atlassian.com/software/jira/download-archives", #Jira
    "https://www.atlassian.com/software/confluence/download-archives", #Confluence
    "https://www.sonarqube.org/downloads/", #SonarQube
    "https://github.com/grafana/grafana/releases" #Grafana
]

# releaseNote_xpath = [
#     "//*[@id='accordion-view']//p/a[contains(@class,'release-notes')]", # Bitbucket
#     "//*[@class='panelContent']/div/ul/li[2]/span/a", #Jfrog
#     "//*[@class='text-longform']//*[contains(@id, 'release-notes')]", #Bamboo
#     "(//*[contains(text(), 'Changelog')])[1]", #Jenkins
#     "//*[@class='release-entry'][1]//div[@class='release-header']/div/div/a", #Prometheus
#     "//*[@id='accordion-view']//p/a[contains(@class,'release-notes')]", #Jira
#     "//*[@id='accordion-view']//p/a[contains(@class,'release-notes')]", #Confluence
#     "//*[@class='downloads-separated weight-medium']//a[contains(text(), 'Release Notes')]", #SonarQube
#     "//*[@class='release-entry'][1]//div[@class='release-header']/div/div/a" #Grafana
# ]