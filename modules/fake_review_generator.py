import json
import random
import nltk
from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="your-key")

# Download necessary NLTK data for tokenization (used for splitting text into words/sentences)
nltk.download('punkt')

def generate_review(prompt="This product is", max_length=50):
    """
    Generates a fake review using OpenAI's ChatCompletion API.
    
    Parameters:
        prompt (str): The starting text for the review (default is "This product is").
        max_length (int): Maximum number of tokens allowed in the generated review (default is 50).
    
    Returns:
        str: The generated review text.
    """
    # Create a chat completion request with the provided prompt and maximum token length.
    # The system message sets the context for generating creative fake reviews.
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative assistant generating fake reviews."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_length
    )
    # Extract and return the generated text from the response.
    return response.choices[0].message.content


def create_reviews(prompts, num_reviews=10):
    """
    Generates multiple fake reviews using random prompts and saves them to a JSON file.
    
    Parameters:
        prompts (list): A list of prompt strings to choose from.
        num_reviews (int): The number of reviews to generate (default is 10).
    """
    reviews = []
    # Loop for the specified number of reviews
    for _ in range(num_reviews):
        # Randomly select a prompt from the list
        prompt = random.choice(prompts)
        # Generate a review using the selected prompt
        review_text = generate_review(prompt)
        # Append the generated review as a dictionary to the list
        reviews.append({"review": review_text})

    # Save the list of generated reviews into a JSON file with indentation for better readability
    with open("2_fake_reviews_prompts.json", "w") as f:
        json.dump(reviews, f, indent=4)

    # Print a message indicating successful generation and saving of reviews
    print(f"Generated {num_reviews} reviews and saved them in 2_fake_reviews_prompts.json")


def generate_review_by_keyword(keyword, max_length=50):
    """
    Generates a fake review based on a given keyword using OpenAI's ChatCompletion API,
    then saves the result to a JSON file.
    
    Parameters:
        keyword (str): A keyword to incorporate in the review prompt.
        max_length (int): Maximum number of tokens allowed in the generated review (default is 50).
    
    Returns:
        str: The generated review text.
    """
    # Formulate a prompt that includes the keyword in the context of a review
    prompt = f"I recently bought a {keyword} and"
    # Request a chat completion using the specified model and prompt
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a creative assistant generating fake reviews."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_length
    )
    # Retrieve and clean the generated text (remove extra whitespace)
    output_text = response.choices[0].message.content.strip()
    # Define the output filename for saving the result
    output_file = '2_fake_review_by_keyword.json'
    # Write the generated review text into the JSON file with proper indentation
    with open(output_file, 'w') as f:
        json.dump(output_text, f, indent=4)

    # Notify the user that the result has been saved
    print(f"Results saved in {output_file}")
    return output_text