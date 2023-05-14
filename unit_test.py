# Unit tests #
import pytest
import requests
from unittest import mock

# Simple unit test for fun that reads a file and returns the new lines of it (\n)
def read_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    # Remove empty lines
    lines = [line.strip() for line in lines if line.strip()]
    
    return lines

def test_read_file(tmp_path):
    # Create a temporary file with known contents
    file_contents = "Line 1\nLine 2\n\nLine 4\n"
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w") as f:
        f.write(file_contents)
    
    # Call the function
    result = read_file(file_path)
    
    # Check that the function returns the expected number of non-empty lines
    expected_result = 3
    assert len(result) == expected_result



def test_read_file_with_mock():
    # Define the contents of the mock file
    mock_file_contents = "Line 1\nLine 2\n\nLine 4\n"

    # Set up the mock open function to return the mock file contents
    with mock.patch("builtins.open", mock.mock_open(read_data=mock_file_contents)):
        # Call the function with a dummy file name
        result = read_file("dummy_file.txt")

        # Check that the function returns the expected number of non-empty lines
        expected_result = 3
        assert len(result) == expected_result




# Test a function that makes a request for json
def get_data():
    response = requests.get("https://api.example.com/data")
    return response.json()

def test_get_data_with_mock():
    # Define the contents of the mock response
    mock_response_data = {"key1": "value1", "key2": "value2"}

    # Set up the mock response object
    mock_response = mock.Mock()
    mock_response.json.return_value = mock_response_data
    mock_response.status_code = 200

    # Set up the mock request function to return the mock response object
    with mock.patch.object(requests, "get", return_value=mock_response):
        # Call the function
        result = get_data()

        # Check that the function returns the expected data
        assert result == mock_response_data


# Test a function that makes a request for json and status code
def get_data_2():
    response = requests.get("https://api.example.com/data")
    return response

def test_get_data_2_with_mock():
    # Define the contents of the mock response
    mock_response_data = {"key1": "value1", "key2": "value2"}
    mock_status_code = 200

    # Set up the mock response object
    mock_response = mock.Mock()
    mock_response.json.return_value = mock_response_data
    mock_response.status_code = mock_status_code

    # Set up the mock request function to return the mock response object
    with mock.patch.object(requests, "get", return_value=mock_response):
        # Call the function
        response = get_data_2()

        # Check that the response status code matches the expected value
        assert response.status_code == mock_status_code

        # Check that the response JSON data matches the expected value
        assert response.json() == mock_response_data



# Seafair Unit test

# @action(detail=True, methods=["post"], url_path="claim-profile")
# def claim_profile(self, request: Request, pk: str) -> Response:
#     seafarer_usecases.claim_profile(pk, request.user.user_id)
#     return EmptyResponse()


# from unittest import mock
# from django.test import RequestFactory
# from myapp.views import MyView

# def test_claim_profile():
#     # create a mock Request object
#     request_factory = RequestFactory()
#     request = request_factory.post('/my-url/')
#     request.user = mock.Mock(user_id='123')

#     # create an instance of MyView
#     view = MyView()

#     # mock the seafarer_usecases.claim_profile method
#     with mock.patch.object(seafarer_usecases, 'claim_profile') as mock_claim_profile:
#         # call the claim_profile method
#         response = view.claim_profile(request, pk='456')

#         # assert that the seafarer_usecases.claim_profile method was called with the correct arguments
#         mock_claim_profile.assert_called_once_with('456', '123')

#         # assert that the response is an EmptyResponse
#         assert isinstance(response, EmptyResponse)
