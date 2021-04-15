from datetime import datetime


outter_keys = ["data", "included"]
# we need to send inner_keys_data to class Articles
inner_keys_data = ["type", "id", "attributes", "relationships"]
inner_keys_included = inner_keys_data[:3]
data_attributes = ["title", "body", "created", "updated"]
included_attributes = ["name", "age", "gender"]

# todo: write validation functions


def validate_outter(data_outter: dict):
    keys = list(data.keys())
	for key in keys:
		if key not in outter_keys:
			raise ValueError


def validate_data(data: dict):
    validate_outter(data)

    validate_inner(data["data"])

    validate_attributes(data["data"]["attributes"])
    validate_relationships(data["data"]["relationships"])


def validate_inner(inner_data: dict):
	if not isinstance(inner_data, dict):
		raise ValueError

	global inner_keys_data
	for key in list(dict_inner_data.keys()):
		if key not in inner_keys_data:
			raise ValueError


def validate_attributes(attributes_values):
    if not isinstance(attributes_values, dict):
		raise ValueError
	for key in list(attributes_values.keys()):
		if not key in data_attributes:
			raise ValueError


def validate_relationships(relationships_data: dict):
    keys = list(relationships_data.keys())
    values = list(relationships_data.values())
    if len(keys) != 1:
        raise KeyError("length of keys is not valid")
    if keys[0] != "author":
        raise KeyError("'data' -> 'relationships'")
    for key, value in values.items():
        if key != "data":
            raise KeyError("'data' -> 'relationships' -> 'author'")
        if not isinstance(value, dict):
            raise ValueError("'data' -> 'relationships' -> 'author' -> 'data'")
        

validate_values(data):
    dict_inner = data["data"][0]
    included_dict = data["included"][0]
    status, mesasge = validate_inner_values(dict_inner)
    validate_included_values(included_dict)


validate_inner_values(dict_inner):
    values = list(dict_inner.values())
    keys = list(dict_inner.keys())
    for key, value in dict_inner.items():
        if isinstance(value, str):
		try:
			date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
		except ValueError:
			if key == "created" or key == "updated":
				return False, "invalid data format"
			# if exception occured but string is not data format
                string_data_validation(key, value)
        if isinstance(value, dict):
            dict_data_validation(value)
        if isinstance(value, list):
            list_data_validation(value)
    
