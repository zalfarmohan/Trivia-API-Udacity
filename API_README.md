## API REFERENCES

## Getting Started

- Base URL: at present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the fronted configurations.

- Athentication: This version of the application doesn't require authentication or API keys.

## Features

* Endingpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint returns a list of questions, number of total questions, current category, categories.

* Endpoint to handle GET requests for all avalable categories.
* Endpoint to DELETE question using a quetion ID.
* Endpoint to POST a new question, which requires the question and answer text, category, and difficulty score.
* POST endpoint to get quetions based on a category.
* POST endpoint to get questions based on a search term. It returns any question(s) for whom the search term is a substring of the question.
* POST endpoint to get questions to play the quiz. The endpoint takes category and previous questoin paramters and returns a random questions within the given category, if provided, and that is not one of the previous questions.


## Error Handling
Errors are returned as Json objects in the following format:-
 ``` {
     "success": False,
     "error": 422,
     "message": "unprocessable",
 }
```

The API will return the following error types when requests fail:
 - 404: Resource not found
 - 405: Method not allowed
 - 422: Unproccessable
 - 500: Internal Server Error
 - 400: Bad Request

 ### Endpoints
 ### GET / questions
 - General:
    - returns the list of all questions
    - Takes
        - page value (int)[optional]
    - returns
        - success value [bool]
        - A list of question [list]
        - Total number of questions [int]
        - Dictionary of categories as {"id": "type", "id": "type"} [dict]
        - Current category [str]
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
    
 - ``` curl http://127.0.01:5000/questions```
 - ``` curl http://127.0.0.1:5000/questions?page=2```

### GET / categories
- General:
    - Returns the list of all categories
    - Takes
        - N/A
    - Returns
        - A dictionary of categories as ```{"id": "type","id":"type"}``` [dict]
        - Total number of categories [int]
- ``` curl http://127.0.0.1:5000/categories```

## POST /questions
- General: 
    - Creates a new question.
    - Takes
        - Question [String()]
        - Answer [String()]
        - category [Integer]
    - Returns
        - Successs value [boolean]
        - ID of the created question [Integer]
        - Created question [String]
``` curl http://127.0.0.1:5000/questions -X POST - H "Content-Type: application/json" -d '{"question": "Is python case sensitive?","answer": "Yes":,"difficulty":"5","category":"1"}' ```

## POST / searchQuestions
- General:
    - Returns all questions having the searched key words(s) in them which is case-insensitive. Users ilike(%key%) in the SQLAlchemy ORM.
    
    - Takes
        - Search key word(s) [string]
        - Page number as URI parameter [integer] (optional)
        - Example: /searchQuestions?page=2
    
    - Returns
        - Success value [boolean]
        - A list of questions [list]
        - Total number of questions [integer]
        - Current category [String]
    - Results are paginated in groups of 10. includes a request argument to choose page number, starting from 1.

- ``` curl http://127.0.0.1:5000/searchQuestions -X POST -H "Content-Type: application/json" -d '{"searchTerm":"what"}' ```

- ``` curl http://127.0.0.1:5000/searchQuestions?page=2 -X POST -H "Content-Type: application/json" -d '{"searchTerm":"what"}' ```


## DELETE /questions/{question_id}
- General:
    - Deletes the question of the given question id if it exists.
    - Takes
        - Question id as part of the URI [integer]
    - Returns
        - Success value [boolean]
        - id of the deleted question
- ``` curl -X DELETE http://127.0.0.1:5000/questions/10 ```

## GET /categories/{category_id}/questions
- General:
    - Get all questions of the category from the given category id
    - Takes
        - Category id as part of the URI [integer]
        - Page number as URI paramter [integer] (optional)
        - Example /categories/3/questions?page=2
    - Returns
        - Success value [boolean]
        - A list of questions [list]
        - Total number of questions [integer]
        - Current category (string)
    - Results
        - Results are paginated in groups of 10. include a request argument to choose page number, starting from 1.
- ``` curl http://127.0.0.1:5000/categories/3/questions ```
- ``` curl http://127.0.0.1:5000/categories/3/questions?page=2 ```

## POST /quizzes
- General:
    - Get a random questions from the given category not present in the list of previous questions.
    
    - Takes
        - Category id [integer]
        - List of previous questions ids [list]
    - Returns
        - success value [boolean]
        - A question [dict]
        - Current Category [String]
    - The game runs for 5 questions. If the category has less than 5 questions, at first it will return all the questions in that category one by one. If the length of the previous questions id list is equal or greater than the number of questions in this category, a random question from all the question will be returned one by one until the game is over. If this logic is not applied The game will crash when all questions from a category is over.
- ``` curl http://127.0.0.1:5000:/quizzes -X POST - H "Content-Type: application/json" -d '{"previous_questions":[12,10,11, 14], "quiz_category":{"type":Science", "id":"1"}}' ```

# Future updates
- Create and endopint to edit a question.
- Create an endpoint to delete a category
- Create and endpoint to add category.

# All curl commands at once

```
# Get all questions

    curl http://127.0.0.1:5000/questions
    curl http://127.0.0.1:5000/questions?page=3

# Get all categories

    curl http://127.0.0.1:5000/categories

# Create a question

    curl http://127.0.0.1:5000/questions -X POST - H "Content-Type: application/json" -d '{"question": "Is python case sensitive?","answer": "Yes":,"difficulty":"5","category":"1"}'

# Delete a question

    curl -X http://127.0.0.1:5000://questions/2

# Search Questions

    curl http://127.0.0.1:5000/searchQuestions -X POST -H "Content-Type: application/json" -d '{"searchTerm":"what"}'

    curl http://127.0.0.1:5000/searchQuestions?page=2 -X POST -H "Content-Type: application/json" -d '{"searchTerm":"what"}'

# Get all questins from a categories

    curl http://127.0.0.1:5000/categories/3/questions
    curl http://127.0.0.1:5000/categories/3/questions?page=3
    curl http://127.0.0.1:5000/categories/4/questions?page=2

# Get quiz

    curl http://127.0.0.1:5000/categories
    curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions":[12,10,11, 14], "quiz_category": {"type": "Science", "id":"1"}}' ```

## Endpoint Request and Response Samples
# Get all questions
    
    Request : `curl http://127.0.0.1:5000/questions`
    
    Response:

    ```
   {
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }, 
    {
      "id": 7, 
      "type": "Technology"
    }
  ], 
  "current_category": null, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Scarab", 
      "category": 4, 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ], 
  "success": true, 
  "total_questions": 27
} 
```

# Get all categories

Request:

`curl http://127.0.0.1:5000/categories`

Responses:
``` {
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }, 
    {
      "id": 7, 
      "type": "Technology"
    }
  ], 
  "success": true
} 
```
# Create a question

`curl http://127.0.0.1:5000/questions -X POST - H "Content-Type: application/json" -d '{"question": "Is python case sensitive?","answer": "Yes":,"difficulty":"5","category":"1"}'`

Request:
` '{"question": "Is python case sensitive?","answer": "Yes":,"difficulty":"5","category":"1"}' `

Response::

``` 
{
  "created": 116, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Scarab", 
      "category": 4, 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ], 
  "success": true, 
  "total_questions": 30
}
```

# Delete a question
Request: `curl -X DELETE http://127.0.0.1:5000/questions/17 `

Response:

```
{
  "deleted": 17, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Scarab", 
      "category": 4, 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }, 
    {
      "answer": "R.E. Grant Govan", 
      "category": 6, 
      "difficulty": 1, 
      "id": 96, 
      "question": "Who was the 1st president of BCCI ( Board of Control for Cricket in India )?"
    }
  ], 
  "success": true, 
  "total_questions": 29
}
 ```

# Search Questions
Request: `curl http://127.0.0.1:5000/searchQuestions -X POST -H "Content-Type: application/json" -d '{"searchTerm":"what"}' `

Responses:
```
{
  "current_category": null, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Referee", 
      "category": 6, 
      "difficulty": 2, 
      "id": 97, 
      "question": "What is the name of person which controls a football match"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Field", 
      "category": 7, 
      "difficulty": 1, 
      "id": 105, 
      "question": "What is part of a database that holds only one type of information?"
    }, 
    {
      "answer": "Uninterruptable Power Supply", 
      "category": 7, 
      "difficulty": 5, 
      "id": 106, 
      "question": "Sometimes computers and cache registers in a foodmart are connected to a UPS system. What does UPS mean?"
    }, 
    {
      "answer": "Local Area Network", 
      "category": 7, 
      "difficulty": 5, 
      "id": 107, 
      "question": "What do we call a collection of two or more computers that are located within a limited distance of each other and that are connected to each other directly or indirectly?"
    }, 
    {
      "answer": "1972", 
      "category": 7, 
      "difficulty": 4, 
      "id": 108, 
      "question": "In what year was the \"@\" chosen for its use in e-mail addresses?"
    }, 
    {
      "answer": "To provide power to essential equipment", 
      "category": 7, 
      "difficulty": 3, 
      "id": 110, 
      "question": "What will a UPS be used for in a building?"
    }, 
    {
      "answer": "Random Access Memory", 
      "category": 1, 
      "difficulty": 5, 
      "id": 114, 
      "question": "What stand for RAM? "
    }
  ], 
  "success": true, 
  "total_questions": 10
}

```
# Get all questions from a category
Request: `curl http://127.0.0.1:5000/categories/1/questions`

Response:
```
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }, 
    {
      "id": 7, 
      "type": "Technology"
    }
  ], 
  "current_category": {
    "id": 1, 
    "type": "Science"
  }, 
  "questions": [
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Hydrogen sulphide", 
      "category": 1, 
      "difficulty": 1, 
      "id": 100, 
      "question": "\t Brass gets discoloured in air because of the presence of which of the following gases in air?"
    }, 
    {
      "answer": "Bromine", 
      "category": 1, 
      "difficulty": 1, 
      "id": 101, 
      "question": "Which of the following is a non metal that remains liquid at room temperature?"
    }, 
    {
      "answer": "it has a high dipole moment", 
      "category": 1, 
      "difficulty": 5, 
      "id": 102, 
      "question": "Water is a good solvent of ionic salts because"
    }, 
    {
      "answer": "Lithium", 
      "category": 1, 
      "difficulty": 4, 
      "id": 103, 
      "question": "Which of the following is the lightest metal?"
    }, 
    {
      "answer": "Yes i love coding..", 
      "category": 1, 
      "difficulty": 1, 
      "id": 111, 
      "question": "Do you love Coding?"
    }, 
    {
      "answer": "Yes i love coding..", 
      "category": 1, 
      "difficulty": 1, 
      "id": 112, 
      "question": "Do you love Coding?"
    }, 
    {
      "answer": "Random Access Memory", 
      "category": 1, 
      "difficulty": 5, 
      "id": 114, 
      "question": "What stand for RAM? "
    }
  ], 
  "success": true, 
  "total_questions": 12
}

```

# GET a quiz
 
 Request:

 ` curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions":[12,10,11, 14], "quiz_category": {"type": "Science", "id":"1"}}' `

Responses:

```
{
  "question": {
    "answer": "Yes", 
    "category": 1, 
    "difficulty": 5, 
    "id": 115, 
    "question": "Is python case sensitive?"
  }, 
  "success": true
}


```
