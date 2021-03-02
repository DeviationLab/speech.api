import secrets
import uuid

# A key consists of a universal unique identifier for a specific user and a project identifier
#
# Uder ID --> xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx-XXXXXXXX <-- Project ID
#                 8     4    4    4        12         8
# Example: 6796095d-eaee-4c24-943b-45432ea531c9-b8826a44

# generates a new API key like described above
def generateNewAPIKey():
    key = str(uuid.uuid4()) + "-" + secrets.token_hex(4)
    return key

# splits a given key into uuid and project id
def parseKey(key):
    uuidKey = key[:36]
    projectKey = key[37:]
    return uuidKey, projectKey
