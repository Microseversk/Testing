import pytest
import requests
from lib.api_helper import *


class TestHttpChecks:
	def test_http_root_response_status_200(self):
		assert get_page().status_code == 200

	def test_root_response_text(self):
		assert get_page().text

	def test_http_result_response_status_200(self):
		assert post_form(data={'input_text':'aaa'},path='result').status_code == 200

	def test_http_root_response_content_type_text_html(self):
		assert get_page('result').headers['Content-Type'] == 'text/html; charset=utf-8'

	def test_http_result_response_content_type_app_json(self):
		assert post_form(data={'input_text':'aaa'},path='result').headers['Content-Type'] == 'application/json'


class TestPalindromicCounterSubs:
	invalid_input_data = [
		'123',
		"123abc123",
		"abc123abc",
		'ABC',
		"abcABC",
		"abcABCabc",
		"ABCabcABC",
		"абц",
		"абцabcабц",
		"abcабцabc",
		'異體字',
		"異體字abc異體字",
		"abc異體字abc",
		" ",
		"abc ",
		" abc",
		"abc abc",
		"@#!",
		"!@#abc!@#",
		"abc!@#abc",
		"()",
		"[]",
		"{}",
		"<>",
		"()abc()",
		"[]abc[]",
		"{}abc{}}",
		"<>abc<>",
		"abc()abc",
		"abc[]abc",
		"abc{}abc",
		"abc<>abc"
	]

	@pytest.mark.parametrize("data", [
		pytest.param(['aaa', 6], id='aaa=6'),
		pytest.param(['abc', 3],id='abc=3'),
		pytest.param(['aaabccc', 13],id='aaabccc=13'),
		pytest.param(['asdasd', 6],id='asdasd=6'),
		pytest.param(['ytreeeeqweeeeerrreee', 45],id='ytreeeeqweeeeerrreee=45')
	])
	def test_input_value_valid_response_answer_count_correct(self,data):
		assert post_form(data={'input_text':data[0]},path='result').json()['count'] == data[1]

	@pytest.mark.parametrize("data",[
		pytest.param('a', id='left_on_bound'),
		pytest.param('aa', id='left_gt_bound'),
		pytest.param('a' * 999, id='right_lt_bound'),
		pytest.param('a' * 1000, id='right_on_bound'),
	])
	def test_input_length_valid_response_status_200(self,data):
		assert post_form(data={'input_text':data},path='result').status_code == 200

	@pytest.mark.parametrize("data", [
		pytest.param('', id='left_lt_bound'),
		pytest.param('a' * 1001, id='left_gt_bound'),
	])
	def test_input_length_invalid_response_status_400(self, data):
		assert post_form(data={'input_text': data}, path='result').status_code == 400


	@pytest.mark.parametrize("data",invalid_input_data)
	def test_input_value_invalid_response_status_400(self,data):
		assert post_form(data={'input_text':data},path='result').status_code == 400

	def test_form_no_data_response_status_400(self):
		assert post_form(data={}, path='result').status_code == 400
	def test_form_key_invalid_response_status_400(self):
		assert post_form(data={'wrong_key': 'aa'}, path='result').status_code == 400

	def test_form_extra_key_response_status_200(self):
		assert post_form(data={'input_text': 'aa', 'extra_key': 2}, path='result').status_code == 200

	def test_form_extra_key_response_correct_answer_count(self):

		assert post_form(data={'input_text': 'aa', 'extra_key': 2}, path='result').json()['count']
