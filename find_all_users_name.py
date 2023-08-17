from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    messages = data['messages']
    s = []
    for i in messages:
        if 'actor' in i.keys():
            if i['actor'] not in s:
                s.append(i['actor'])
        else:
            if i['from'] not in s:
                s.append(i['from'])
    return s
print(find_all_users_name(read_data('data/result.json')))