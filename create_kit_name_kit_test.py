import sender_stand_request
import data


def get_kit_create(name):
    current_kit_create = data.kit_create.copy()
    current_kit_create['name'] = name
    return current_kit_create


def get_new_user_token():
    sender_stand_request.post_new_user(data.user_body)
    res = sender_stand_request.auth()
    if res.ok:
        return res.json('authToken')
    else:
        return ''


def positive_assert(name):
    kit_create = get_kit_create(name)
    auth_token = get_new_user_token()
    kit_res = sender_stand_request.post_new_client_kit(kit_create, auth_token)
    assert kit_res.status_code == 201


def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")


def test_create_kit_russian_letter_in_name_get_success_response(): #провал
    positive_assert("Мария")


def test_create_kit_has_special_symbol_in_in_name_get_success_response(): #провал
    positive_assert("№%@")


def test_create_kit_has_space_in_in_name_get_success_response(): #провал
    positive_assert("Человек и КО")


def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")


def negative_assert_symbol(name):
    kit_create = get_kit_create(name)
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_create, auth_token)
    assert response.status_code == 400
    assert response.json()['code'] == 400
    assert response.json()['message'] == "Не все необходимые параметры были переданы"


def test_create_user_0_letter_in_first_name_get_error_response(): #провал
    negative_assert_symbol("")

def test_create_user_512_letter_in_first_name_get_error_response(): #провал
    negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test_create_user_empty_first_name_get_error_response(): #провал
    negative_assert_symbol(None)


def test_create_kit_number_in_name_get_success_response(): #провал
    negative_assert_symbol(123)