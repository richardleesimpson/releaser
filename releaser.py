import json, base64, requests

# load_config reads a config.json file in the root directory and returns a config object
def load_config():
	# Read a config json file
	with open('config.json') as file:
		config = json.load(file)

	# base64 encode username:password to use in JIRA API request header
	config['jira_auth'] = base64.b64encode(bytes(config['jira_user'] + ':' + config['jira_pass'], 'utf_8')).decode('utf_8')

	return config

# list_boards requests agile boards via JIRA API
def list_boards(config):
	# Make a request
	r = requests.get(config['jira_protocol'] + '://' + config['jira_host'] + '/rest/agile/1.0/board', headers={'Authorization': 'Basic ' + config['jira_auth']})

	# Encode response as json
	j = json.loads(r.text)

	# Return boards listed in values
	return j['values']

# list_board_sprints requests sprints in an agile board via JIRA API
def list_board_sprints(config, boardid, opts):
	# TODO: Default opts and check nulls
	# TODO: Use opts in the request

	# Make a request
	r = requests.get(config['jira_protocol'] + '://' + config['jira_host'] + '/rest/agile/1.0/board/' + boardid + '/sprint?state=active', headers={'Authorization': 'Basic ' + config['jira_auth']})

	# Encode response as json
	j = json.loads(r.text)

	# Return sprints listed in values
	return j['values']

# list_sprint_issues requests issues in a sprint via JIRA API
def list_sprint_issues(config, sprintid, opts):
	# TODO: Default opts and check nulls
	# TODO: Use opts in the request

	# Make a request
	r = requests.get(config['jira_protocol'] + '://' + config['jira_host'] + '/rest/agile/1.0/sprint/' + sprintid + '/issue', headers={'Authorization': 'Basic ' + config['jira_auth']})

	# Encode response as json
	j = json.loads(r.text)

	# Return issues
	return j['issues']

# Gentlemen, start your engines.
print ("Hello world")

# Load the config file
config = load_config()

# TODO: Add VPN support for intranet-hosted JIRA instances. Grr...
# Get agile boards in the JIRA instance
boards = list_boards(config)

# Iterate over boards
for b in boards:
	#
	print('Board: ' + b['name'])
	boardid = str(b['id'])

	# Get sprints in the board
	sprints = list_board_sprints(config, boardid, {})

	# Iterate over sprints
	for s in sprints:
		print('Sprint: ' + s['name'])
		sprintid = str(s['id'])

		# TODO: Begin building a release directory for the sprint

		# Get issues in the sprint
		issues = list_sprint_issues(config, sprintid, {})
		print(issues)

		# Iterate over issues
		for i in issues:
			print('Issue: ' + i['key'])
			print(i)

			# TODO: Add this issue to the release directory

		# TODO: Finalize and publish the release directory
