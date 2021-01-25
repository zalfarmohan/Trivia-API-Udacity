from flask import Flask, request, abort, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Question, Category
import random

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # Create and configure the app.
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    '''
    Todo: setup CORS, Allow '*'
    for origins. Delete the sample route after completing the TODs.
    '''

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    '''
    @TODO: Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type,Authorization, true')
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET, POST, DELETE, PATCH, OPTIONS'
            )
        return response

    def paginate_questions(request, selection):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        questions = [question.format() for question in selection]
        current_questions = questions[start:end]
        return current_questions

# TODO: create an endpoint to handle GET requests for all avaliable categories.
    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories = list(map(Category.format, Category.query.all()))
        ''' formatted_categories = [category.format()
         for category in categories] '''
        if categories is None:
            abort(404)
        return jsonify({
            'success': True,
            'categories': categories
        })
    ''' Create and endpoint to hadnle GET requests for questions,
        including pagination (every 10 questions).
        This endpoint should return a list of questions,
        number of total questions, current category, categories. '''

    @app.route('/questions', methods=['GET'])
    def get_all_questions():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)
        categories = list(map(Category.format, Category.query.all()))
        if len(current_questions) == 0:
            abort(404)
        else:
            pass
        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(Question.query.all()),
            'categories': categories,
            'current_category': None,
        })
    '''
    @TODO: Create an endpoint to DELETE question using a question ID.
    TEST: When you click the trash icon next to a question,
    the question will be removed. This removal will persist in the database
    and when you refresh the page/
    '''
    # Delete a specific question
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def remove_question(question_id):
        try:
            question = Question.query.filter(
                Question.id == question_id).one_or_none()
            # if question id doesn't exists
            # that means request is no match found
            if question is None:
                abort(404)
            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)
            return jsonify({
                'success': True,
                'deleted': question_id,
                'questions': current_questions,
                'total_questions': len(Question.query.all())
            })
        except Exception:
            abort(422)

    '''
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.
    '''

    # Create a question
    @app.route('/questions', methods=['POST'])
    def create_questions():
        """ POST QUESTIOn (Add new Questions) """
        body = request.get_json()
        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_category = body.get('category', None)
        new_difficulty = body.get('difficulty', None)
        try:
            question = Question(
                question=new_question,
                answer=new_answer, category=new_category,
                difficulty=new_difficulty)
            question.insert()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify({
                'success': True,
                'created': question.id,
                'questions': current_questions,
                'total_questions': len(Question.query.all())
            })
        except Exception:
            abort(422)
    '''
    @TODO:
    Create a POST endpoint to get questions based on a searchTerm.
    It should return any questions for whom the searchTerm
    is a substring of the question.

    TEST: Search by any phrase. The questoins list will
    update to include only question that include that
    string within their question.
    Try using the word "Title" to start.
    '''
    # Search a question with a given SearchTerm
    @app.route('/searchQuestions', methods=['POST'])
    def search_questions():
        if request.data:
            page = 1
            if request.args.get('page'):
                page = int(request.args.get('page'))
            search_data = json.loads(request.data.decode('utf-8'))
            if 'searchTerm' in search_data:
                question_search = Question.query.filter(
                    Question.question.ilike(
                        '%'+search_data['searchTerm'] + '%')).paginate(
                            page, QUESTIONS_PER_PAGE, False)
                questions = list(map(Question.format, question_search.items))
                if len(questions) > 0:
                    result = {
                        'success': True,
                        'questions': questions,
                        'total_questions': question_search.total,
                        'current_category': None
                    }
                    return jsonify(result)
            abort(404)
        else:
            abort(422)

    '''
    @TODO:
    Create a GET endpoint to get questions based on category.
    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    '''

    # Get questions from a category.
    @app.route('/categories/<int:category_id>/questions')
    def get_question_by_category(category_id):
        category_data = Category.query.get(category_id)
        page = 1
        if request.args.get('page'):
            page = int(request.args.get('page'))
        categories = list(map(Category.format, Category.query.all()))
        questions_query = Question.query.filter_by(
            category=category_id).paginate(
                page, QUESTIONS_PER_PAGE, False)
        questions = list(map(Question.format, questions_query.items))
        if len(questions) > 0:
            results = {
                'success': True,
                'questions': questions,
                'total_questions': questions_query.total,
                'categories': categories,
                'current_category': Category.format(category_data)
            }
            return jsonify(results)
        else:
            pass
        abort(404)

    '''
    @TODO:
    Create a POST endpoint to get questions to play a quiz.
    This endpoint should take category and previous question
    parameters and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    '''

    # Get a question to play
    @app.route('/quizzes', methods=['POST'])
    def get_questions_for_quiz():
        if request.data:
            search_data = json.loads(request.data.decode('utf-8'))
            if (('quiz_category' in search_data
                and 'id' in search_data['quiz_category'])
                    and 'previous_questions' in search_data):
                question_query = Question.query.filter_by(
                    category=search_data['quiz_category']['id']).filter(
                        Question.id.notin_(
                            search_data['previous_questions'])).all()
                length_of_available_questions = len(question_query)
                if length_of_available_questions > 0:
                    results = {
                        'success': True,
                        'question': Question.format(
                            question_query[random.randrange(
                                0, length_of_available_questions)])
                    }
                else:
                    results = {
                        'success': True,
                        'question': None,
                    }
                return jsonify(results)
            abort(404)
        abort(422)

    '''
    @Todo: create error handlers for
    all expected errors including 404 and 422
    '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'not found for the given resource'})

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422, 'message': 'unprocessable'})

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad Request'})

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal Server Error'})
    return app
