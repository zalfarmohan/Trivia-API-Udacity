import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        # self.database_name = "trivia"
        # self.database_path = "postgresql://{}:{}@{}/{}".format(
        #     'postgres', 'farhanmadka', 'localhost:5432', self.database_name)
        self.DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
        self.DB_USER = os.getenv('DB_USER', 'postgres')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD', 'farhanmadka')
        self.DB_NAME = os.getenv('DB_NAME', 'trivia')
        self.DB_PATH = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
            self.DB_USER, self.DB_PASSWORD, self.DB_HOST, self.DB_NAME)
        setup_db(self.app, self.DB_PATH)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for
    successful operation and for expected errors.
    """
     # Try to get all the categories with get request
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        
 

    def test_get_paginated_questions(self):
        res = self.client().get('/questions?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['categories']))
        self.assertTrue(len(data['questions']))

    # Testing Post New Questions
    def test_post_new_questions(self):
        posting_new_question = {
            'question': 'Do you love Coding?',
            'answer': 'Yes i love coding..',
            'difficulty': 1,
            'category': 1,
        }
        res = self.client().post('/questions', json=posting_new_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # deleting test question
    def test_delete_questions(self):
        # if you make another test this ID has already been deleted.
        res = self.client().delete('/questions/100')
        data = json.loads(res.data)

        self.assertTrue(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    # testing delete id if request unprocessable
    def test_delete_question(self):
        res = self.client().delete('/questions/10309')
        data = json.loads(res.data)

        self.assertTrue(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # paginatin post seaerch
    def test_post_paginated_search_questions(self):
        posting_new_question = {
            'searchTerm': 'What is',
            }
        res = self.client().post('/searchQuestions', json=posting_new_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['questions'])

      # get pagination questions by category
    def test_get_paginated_questions_by_category(self):
        res = self.client().get('/categories/1/questions?page=1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['categories']))
    # testing if post new question is unprocessable
     # post play quiz
    def test_post_play_quiz(self):
        post_play_quiz = {
            'previous_questions': [],
            'quiz_category': {
                'type': 'Science',
                'id': 1,
            }
        }
        res = self.client().post('/quizzes', json=post_play_quiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])

        
           # if test play quiz unprocessable to post
    def test_422_post_play_quiz(self):
        res = self.client().post('/quizzes')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()