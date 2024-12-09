
from jira import JIRA

def create_jira_ticket(server, username, token, project, summary, description):
    """Create a JIRA ticket for governance tasks."""
    jira = JIRA(server=server, basic_auth=(username, token))
    issue_dict = {
        "project": {"key": project},
        "summary": summary,
        "description": description,
        "issuetype": {"name": "Task"}
    }
    return jira.create_issue(fields=issue_dict)
            