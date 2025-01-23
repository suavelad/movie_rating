
## API Request and Response

    Movie API
        POST {base_url}/api/movies
        Payload: 
             {
                "title": "Lxlx",
                "description": "New Movie4",
                "release_year": 2026,
                "country": "Nigeria",
                "language": "French",
                "production_company": "Netflix",
                "director": "Jack"
            }
        Response:
            {
                "id": 2,
                "average_rating": null,
                "title": "New Movie 2",
                "description": "New Movie 2",
                "release_year": 2024,
                "country": "Nigeria",
                "language": "English",
                "production_company": "Netflix",
                "director": "Jack",
                "summary": null
            }

        GET {base_url}/api/movies/{movie_id}
        
        Response:
            {
                "id": 6,
                "title": "New Movie 5",
                "rating": 6.67,
                "summary": "It is a love movie"
            }
        
      Movie Rating API
        POST {base_url}/api/ratings/
        Payload: 
                {
                    "movie_id": "6",
                    "email": "sunnexajayi3@gmail.com",
                    "comments": "" //optional
                    "score": 5
                }
        Response:
            {
                "movie_id": 6,
                "email": "sunnexajayi4@gmail.com",
                "score": 4,
                "movie_title": "New Movie 5"
            }
    
     API Doc can be accessed: {base_url}/api/doc/


## LLM Implementation
    I made use of OpenAI prompt API to get the movie summary.


## Challenges:
    1. LLM Implementation: Due to my current novice experience with LLM , I had to rely on OpenAI API system
    2. I could not test the LLM Implementation because I had exhausted my  quota


## Solution Brief:
    From this implementation, A user can :
        - Create a movie
            - When creating a movie, the following activities are done:
                - Validation : 
                        - ensure there is no duplication : I create the title, year, country, lanuage  are unique 
                        - a valid release year is used
                - Generate the movie Summary:
                    - Upon creation of the movie, I call the LLM function to generate the movie summary and update the Database with it

        - Fetch a movie by id
            - I validate that the movie id exist first
            - When fetching the movie, the rating is calculated each time the API is called

        - Rate a Movie
            - When Creating a movie rating , the following activities are done:
                - Validation:
                    - validate that the movie id is valid
                    - validate that the score inputted is within the valid range 
                
            - Save the rating