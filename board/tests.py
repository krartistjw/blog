from django.test import TestCase, Client
import json

from board.models import Board

client = Client()


class BoardCreateTest(TestCase):
    # 테스트 함수는 test_ 를 붙여주어야 테스트 함수로 인식한다.
    def test_board_post_success(self):
        data = {
            'name': 'John',
            'content': 'somthing',
        }

        response = client.post('/board/', json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            "message": "SUCCESS"
        })

    def test_board_get_list(self):

        response = client.get('/board/1/', {'name':'John','content':'something'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "message": "SUCCESS"
        })


class BoardTestCase(TestCase):
    def setUp(self):
        Board.objects.create(
            name='John',
            content='Content'
        )

    def test_board_detail_get_success(self):
        response = client.get('/board/1')
        self.assertEqual(response.json(), {'name':'John','content':'something'});

    def tearDown(self):
        Board.objects.all().delete()