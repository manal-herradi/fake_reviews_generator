import json
from openai import OpenAI

# Initialize the OpenAI model for text classification using your API key
client = OpenAI(api_key="your-key")

def detect_fake_review(review_text):
    """
    Detects if a review is generated by AI.
    This function can handle either a single review (as a string) or a list of reviews.

    Parameters:
        review_text (str or list): The review text or a list of review texts.

    Returns:
        The classification result(s) returned by the OpenAI model.
    """
    # Check if the input is a list, meaning multiple reviews are provided
    if isinstance(review_text, list):
        # Process each review in the list by calling the classify_text method on each one
        results = [client.classify_text(review) for review in review_text]
    else:
        # If it's not a list, process it as a single review
        results = client.classify_text(review_text)

    # Specify the output file where the results will be saved in JSON format
    output_file = '4_fake_reviews_results_detection.json'
    
    # Open the specified file in write mode and dump the results with indentation for readability
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)

    # Inform the user that the results have been successfully saved
    print(f"Results saved in {output_file}")
    
    # Return the results from the OpenAI text classification
    return results
