import requests
import openpyxl
from openpyxl.styles import Font, PatternFill, Color, colors

request_url = "http://10.181.131.252:60007/predict"
# input_header = {"x-api-key": ""}

class APILibrary:
    def __init__(self):
        self._api_output = None
        self._core_api_output = None
        self._core_api_output_confident = None
        self._expected_output = None

    def run_api_for_functional_test(self, file_name):
        error_message = None
        with open(file_name, 'rb') as document_file:
            files = {'image': document_file}
            self._api_output = requests.post(request_url, files=files).json()

        # self._api_output = requests.post(request_url, headers=input_header, files=files).json()[0][0]['text']

        # try:
        #     if "sangat panjang" in file_name:
        #         error_message = "Media duration more than 30s"
        #         assert False
        #     with open(file_name, 'rb') as document_file:
        #         files = {'file': document_file}
        #         self._api_output = requests.post(request_url, headers=input_header, files=files).json()[0][0]['text']


        # except:
        #     if error_message != None:
        #         assert False, error_message
        #     else:
        #         assert False, 'API failed to execute using current input file.'

    def api_should_run_successfully(self):
        # assert "message" not in self._api_output, "API expected to run successfully, instead returned the following error output:\n\"%s\"" % (self._api_output)
        # assert "message" in self._api_output, "API expected to run successfully, instead returned the following error output:\n\"%s\"" % (self._api_output)
        assert "status" in self._api_output and self._api_output['status'] == 'success', "API expected to run successfully, instead returned the following error output:\n\"%s\"" % (self._api_output)

    def api_output_should_be(self, expected_spoof):
        self.set_expected_output(expected_spoof)
        self.set_api_output()
        self.set_api_output_confident()

        test_passed = self._expected_output == self._core_api_output
        error_message = 'Expected\t: "%s"\nOutput\t\t: "%s"\nConfident\t: "%s' % (self._expected_output, self._core_api_output, self._core_api_output_confident)

        assert test_passed, error_message

    def set_api_output(self):
        self._core_api_output = self._api_output['result'][0]['real']

    def set_api_output_confident(self):
        self._core_api_output_confident = self._api_output['result'][0]['conf']

    def set_expected_output(self, expected_spoof):
        # with open(expected_transcript, 'r', encoding='utf-8') as document_file:
        #     self._expected_output = document_file.readline()
        self._expected_output = int(expected_spoof)


