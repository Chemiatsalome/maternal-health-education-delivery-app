from modelintergration import get_chatbot_response_birth
import json

# Run the test
print("Fetching a maternal health quiz question...\n")
response = get_chatbot_response_birth()

# Pretty-print the response
print(json.dumps(response, indent=4))
