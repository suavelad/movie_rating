from openai import OpenAI
from decouple import config


def generate_openai_prompt(prompt):
   try:
        client = OpenAI(api_key=config("OPENAI_API_KEY"))

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[{"role": "user", "content": prompt}]
        )
        print(completion.choices[0].message)
        return completion.choices[0].message
   
   except Exception as e:
        print(f"Error generating prompt: {e}")
        return None



def get_movie_summary(title, year, country,language):
  """
  Fetches a movie summary using the OpenAI API.

  Args:
    title: The title of the movie.
    year: The year of release of the movie.
    country: The country of origin of the movie.

  Returns:
    A string containing the movie summary, or an error message if unsuccessful.
  """

  prompt = f"Provide a concise summary of the movie '{title}' released in {year} from {country} which was shot in {language} language."

  try:
    summary = generate_openai_prompt(prompt)
    return summary

  except Exception as e:
    return f"Error processing summary: {e}"



def process_movie_summary(movie):
    print("In the processing Movie Summary")
    
    # Get movie summary from OpenAI API 
    try:
        summary = get_movie_summary(movie.title,movie.release_year,movie.country,movie.language)
    except Exception as e:
        print(f"Error fetching summary: {e}")
        summary = None

    summary = summary if summary else ''

    movie.summary = summary
    movie.save()

from datetime import datetime

def is_valid_year(year):
  """
  Checks if the given year is a valid year.

  Args:
    year: The year to be checked (integer).

  Returns:
    True if the year is valid, False otherwise.
  """

  try:
    datetime(year=year, month=1, day=1)  
    return True
  except ValueError:
    return False
