## Project Task
    
    Title: Implement a Movie Rating REST API with TDD and LLM Integration
        - Your task is to build a REST API to manage and rate movies. The API must handle two types of entities:
            - Movies 
            - Ratings, and
            - It MUST incorporate Test-Driven Development (TDD) principles and integration with a Large Language Model (LLM) for generating movie summaries.
    
        - You will be graded on:
            - Correctness of the implementation.
            - Use of TDD principles to drive development.
            - Integration and mock testing of an LLM API for generating movie summaries.
        
        - Definitions :
            - Movie Each movie is represented as a JSON object with the following properties:
                - id: A unique integer ID of the movie.
                - title: A string denoting the title of the movie.
                - rating: A float denoting the average rating of the movie, calculated from all associated ratings. If no ratings exist, this   value is null.
                - summary: A string containing a dynamically generated summary for the movie.
            
            Rating: Each rating is represented as a JSON object with the following properties:
                - id: A unique integer ID of the rating.
                - movie: The integer ID of the movie to which the rating is submitted.
                - value: An integer in the range [1-5] denoting the numerical value of the rating.
       
        - Requirements
            Movies Endpoint:
                - POST /movies/:
                    - Accepts a JSON payload with a title field to create a new movie.
                    - Returns the created movie object with a unique ID.
                - GET /movies//:
                    - Retrieves a movie by its ID, including the dynamically generated summary field fetched from an LLM API.
                    - If the movie does not exist, returns a 404 error.
        
            Ratings Endpoint:
                - POST /ratings/:
                    - Accepts a JSON payload with movie (movie ID) and value (rating value) fields to create a new rating.
                    - Updates the average rating of the associated movie.
                    - Returns appropriate error responses for invalid input or nonexistent movies.
       
        - Additional Requirements
            - Use Test-Driven Development (TDD) to build the endpoints.
            - Demonstrate how tests drive your implementation.
            - Integrate a mocked LLM API to generate the summary field for movies.
            - You may simulate the LLM response as part of your implementation.
            - Ensure robust error handling and clean, modular code.

## Basic Requirement:
    - Python3 installed
    - Database : SQLite
    - OpenAI API ( use will need to get an OpenAI api token)

    
## Steps for setting up and running the project:
    - Clone the project

    - Enter into the project directory

    - Setup a virtual environment
        > python3 -m venv env

    - Activate the Environment:
        > source env/bin/activate

    - Install the needed packages:
        > pip install -r requirements.txt
    
    - Setup the Database (Database used : Sqlite)
        > python manage.py makemigration && python manage.py migrate
    
    - Setup the environment variables:
        - Copy the env.example into a new .env file  
        - Replace the demo variable with the right ones

    - Start the Application Server:
        > python manage.py runserver
    

    - Project Breakdown can be accessed from project.md 