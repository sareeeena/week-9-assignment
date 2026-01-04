import json

raw_log = '[{"status": "OK", "msg": "Boot"}, {"status": "ERROR", "msg": "Disk full"}]'

try:
    # Convert string -> List of Dictionaries
    events = json.loads(raw_log)
    
    error_count = 0
    last_error_msg = ""
    
    for event in events:
        if event['status'] == "ERROR":
            error_count += 1
            last_error_msg = event['msg']
            
    print(f"Errors: {error_count}, Last: {last_error_msg}")

except json.JSONDecodeError:
    print("Error: The string provided was not valid JSON.")