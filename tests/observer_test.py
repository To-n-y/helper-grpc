# import pytest
# from service.observer_service import ObserverService
#
#
# class TestWordsRequest:
#     @pytest.mark.webtest
#     def test_make_request(self, test_url):
#         request_maker = WordsRequest(test_url)
#         assert len(request_maker.make_request()) > 10000
#
#
# class TestParser:
#     @pytest.mark.timeout(1)
#     def test_parse_words(self, test_html):
#         test_parser = Parser()
#         request_maker_mock = MagicMock()
#         request_maker_mock.make_request = MagicMock(return_value=test_html)
#         test_parser.req_maker = request_maker_mock
#         assert 2 == len(test_parser.parse_words())
#
#     @pytest.mark.respx(assert_all_mocked=True)
#     def test_parse_words2(self, respx_mock, test_url, test_html):
#         route = (respx_mock
#                  .get(test_url)
#                  .mock(return_value=httpx.Response(200, text=test_html)))
#         test_parser = Parser()
#         with httpx.Client() as client:
#             response = client.get(test_url)
#             assert response.status_code == 200
#             assert len(test_parser.parse_words()) == 2
#
#
# class TestGame:
#     @pytest.mark.parametrize(('word', 'arr', 'result'), [
#         ('academy', [1, 1, 0, 0, 0, 1, 1], 'ac___my'),
#         ('oxygen', [0, 0, 0, 0, 1, 0], '____e_'),
#         ('matrix', [1, 1, 1, 1, 1, 1], 'matrix'),
#         ('subway', [0, 0, 0, 0, 0, 0], '______'),
#         ('wizard', [1, 0, 1, 0, 1, 0], 'w_z_r_')
#     ])
#     def test_curr(self, word: str, arr: list[int], result: str):
#         test_game = Game()
#         test_word = word
#         test_arr = arr
#         assert test_game.curr(test_word, arr) == result
#
#     @pytest.mark.slow
#     def test_set_guess_word(self, test_arr):
#         test_game = Game()
#         with patch(
#             'tests.main_test.Parser.parse_words',
#             return_value=test_arr) as mock:
#             test_game.set_guess_word()
#             assert test_game.guess_word in test_arr
#         with patch(
#             'tests.main_test.Parser.parse_words',
#             side_effect=Exception):
#             test_game.set_guess_word()
#             assert test_game.guess_word in reserve_data
