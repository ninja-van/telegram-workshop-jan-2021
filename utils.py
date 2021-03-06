from beans.item import Item
from beans.user import User


# Returns given string if it is not None or blank, else return default value provided
def default_if_blank(s, default):
    # FILL IN CODE
    return


# Extracts user id from Telegram request
def get_user_from_request(req_body):
    # FILL IN CODE
    return


# Extracts user's name from Telegram request
def __get_req_from_name(req_from):
    # FILL IN CODE
    return


# Extracts user's input (text or button click) from Telegram request
def get_user_input_from_request(req_body):
    # FILL IN CODE
    return


# Extracts user's commands from Telegram request
def get_user_command_from_request(req_body):
    # FILL IN CODE
    return


# Checks where one or more string params provided are None or blank
def is_not_blank(*string):
    # FILL IN CODE
    return


# Extracts list of Item objects from intent result that were captured from response
def get_items_from_response(intent_result):
    entries = []

    # Assumes at least one context is active
    for captured_item in intent_result.output_contexts[0].parameters['cafe-order-entry']:
        if captured_item.__contains__('item-number'):
            entries.append(Item(captured_item['menu-item'], int(captured_item['item-number'])))
        else:
            entries.append(Item(captured_item['menu-item'], 1))

    return entries
