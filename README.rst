releaser
========

Features
--------

- Interact with a JIRA instance via API
- Read deployment instructions for issues in active sprints
- Build a release directory for active sprints

Requirements
------------

Add a **config.json** file at the root directory with the following:

.. code-block:: http

    {
        "jira_protocol": "https",
        "jira_host": "example.atlassian.net",
        "jira_port": "8080",
        "jira_user": "user",
        "jira_pass": "pass",
    }

Pipe dreams for the future
--------------------------

- Pull actual code to stage in the release directory
- Expose a web interface for the assigned release developer
- Generate release documentation
