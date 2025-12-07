
from strands_agent import process_query

def handler(event, context):
    query = event.get("text", "")
    if not query:
        return {"statusCode": 400, "body": "No query provided"}
    response = process_query(query)
    return {"statusCode": 200, "body": response}
