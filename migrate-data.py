import requests

DEBUG=True
# DEBUG=False

def debug(message):
  if DEBUG:
    print message

def get_workspaces(auth_headers):
  r = requests.get("https://api.azendoo.com/workspaces.json", headers=auth_headers)
  return r.json()

def select_workspace(workspaces):
  debug("TODO Ask the user which workspace to import")
  return "5502a1c5324f7165f4000013" # Chouette Coop

def import_workspace(id, auth_headers):
  debug("Importing workspace:")
  r = requests.get("https://api.azendoo.com/workspaces/" + id + ".json", headers=auth_headers)
  data = r.json()
  import_users(data[u'relationships'], auth_headers)
  import_tasks(data[u'task_list_id'], auth_headers)

def import_users(users, auth_headers):
  debug("Importing users:")
  debug("TODO Implement me")
  pass

def import_tasks(task_list_id, auth_headers):
  debug("Importing tasks:")
  debug("TODO Implement me")
  pass

# Generate Token
EMAIL=raw_input("Azendoo email: ")
PASSWORD=raw_input("Azendoo password: ")

r = requests.post("https://api.azendoo.com/tokens", params={'email': EMAIL, 'password':PASSWORD})
token = r.json()[u'access_token']

debug("Token: " + token)

# Do the actual job
auth_headers = {'Authorization': "Token token=" + token}

workspace_id = select_workspace(get_workspaces(auth_headers))
import_workspace(workspace_id, auth_headers)