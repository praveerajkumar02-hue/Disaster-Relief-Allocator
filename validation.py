def validate_identity(requester_id):
    valid_ids = {
        "NGO001",
        "NGO002",
        "NGO003",
        "NGO004",
        "NGO005"
    }

    requester_id = requester_id.strip().upper()

    if not requester_id:
        return False, "Please enter a Requester ID."

    if requester_id not in valid_ids:
        return False, "Invalid Requester ID. Please use a registered NGO ID."

    return True, "Valid Requester ID."


def check_duplicate(requests, requester_id, location, resource_type):

    requester_id = requester_id.strip().upper()
    location = location.strip().lower()
    resource_type = resource_type.strip().lower()

    for request in requests:

        if (
            request["requester_id"].strip().upper() == requester_id
            and request["location"].strip().lower() == location
            and request["resource_type"].strip().lower() == resource_type
        ):
            return True

    return False