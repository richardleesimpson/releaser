import json, base64, requests

# load_config reads a config.json file in the root directory and returns a config object
def load_config():
	# Read a config json file
	with open('config.json') as file:
		config = json.load(file)

	# base64 encode username:password to use in JIRA API request header
	config['jira_auth'] = base64.b64encode(bytes(config['jira_user'] + ':' + config['jira_pass'], 'utf_8')).decode('utf_8')

	return config

# 
def get_boards(config):
	return requests.get('http://' + config['jira_url'] + '/rest/agile/1.0/board', headers={'Authorization': 'Content ' + config['jira_auth']})

def get_board_sprints(config, boardid, opts):
	# TODO: Default opts and check nulls
	# TODO: Use opts in the request

	return requests.get('http://' + config['jira_url'] + '/rest/agile/1.0/board/' + boardid + '/sprint?state=active', headers={'Authorization': 'Content ' + config['jira_auth']})

def get_sprint_issues(config, boardid, sprintid, opts):
	# TODO: Default opts and check nulls
	# TODO: Use opts in the request

	return requests.get('http://' + config['jira_url'] + '/rest/agile/1.0/board/' + boardid + 'sprint/' + sprintid + '/issue', headers={'Authorization': 'Content ' + config['jira_auth']})

# Gentlemen, start your engines.
print ("Hello world")

# Load the config file
config = load_config()
print(config)

# TODO: Add VPN support for intranet-hosted JIRA instances. Grr...
boards = get_boards(config)

# Iterate over boards
# for board in boards
# 	# Get sprints in the board
# 	sprints = get_board_sprints(config, board.id, {
# 		"state": "active",
# 	})

# 	# Begin building release directory

# 	# Iterate over sprints
# 	for sprint in sprints
# 		# Get issues in the sprint
# 		issues = get_sprint_issues(config, board.id, sprint.id, {
# 			# ...
# 		})

# 		#

	# Add any additional non-issue items to the directory

	# Publish the release directory

#result = requests.get('http://' + config['jira_url'] + '/rest/agile/1.0/board', headers={'Authorization': 'Content ' + encoded})

# Return all boards
# url = 'http://JIRA_URL/rest/agile/1.0/board'

# Example board in response:
# {
# "id": 72,
# "self": "http://JIRA_URL/rest/agile/1.0/board/72",
# "name": "Software Releases",
# "type": "scrum"
# },

# Return all active sprints from a board
# url = 'http://JIRA_URL/rest/agile/1.0/board/72/sprint?state=active'

# Example sprint in response:
# {
# "id": 71,
# "self": "http://JIRA_URL/rest/agile/1.0/sprint/71",
# "state": "active",
# "name": "5.18.17 Release Sprint",
# "startDate": "2017-04-24T13:20:08.781-07:00",
# "endDate": "2017-05-18T13:20:00.000-07:00",
# "originBoardId": 72
# }

# Return all issues in a sprint
# url = 'http://JIRA_URL/rest/agile/1.0/board/72/sprint/71/issue'
