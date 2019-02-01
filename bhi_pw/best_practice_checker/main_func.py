
import re, json
def check_best_practices(password):
    letter_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    character_list = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=']
    number_list = "1234567890"

    json_response = {}

    json_response['pw_length'] = len(password)
    
    if len(password) < 10:
        json_response['length'] = "bad"
    else:
        json_response['length'] = "ok"

    if re.findall('([A-Z])', password):
        json_response['uppercase'] = "ok"
    else:
        json_response['uppercase'] = "bad"
    
    if re.findall('([1-9])', password):
        json_response['number'] = "ok"
    else:
        json_response['number'] = "bad"

    for character in list(password):
        if character in character_list:
            json_response['special_char'] = "ok"
            break
    else:
        json_response['special_char'] = "bad"


    return json.dumps(json_response)