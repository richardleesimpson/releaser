releaser
========================

Releaser does the following:
* Interact with a JIRA instance via API
* Read deployment instructions for issues in active sprints
* Build a release directory for active sprints

Requirements
Add a config.json file at the root directory with the following:
{
	"jira_url": "",
	"jira_port": "",
	"jira_user": "",
	"jira_pass": ""
}

I'm currently using a dockerized container of JIRA to test the API, since I don't have an existing instance lying around. You can find it here: `<https://hub.docker.com/r/cptactionhank/atlassian-jira/>`

Pipe dreams for the future:
* Pull actual code to stage in the release directory
* Expose a web interface for the assigned release developer
* Generate release documentation

`Learn more <https://github.com/richard8thday/releaser>`_.