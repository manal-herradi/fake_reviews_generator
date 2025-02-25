import json
from nltk.tokenize import sent_tokenize

def clean_review(review_text):
    """
    Improves the readability of reviews by limiting each review to a maximum of 3 sentences.
    
    Parameters:
        review_text (str or list): A single review as a string or a list of review strings.
    
    Returns:
        list: A list of dictionaries where each dictionary contains the original review and its cleaned version.
    """
    # If a single review string is provided, wrap it in a list for consistent processing.
    if isinstance(review_text, str):
        review_text = [review_text]

    # Process each review:
    # - Tokenize the review into sentences using NLTK's sent_tokenize.
    # - Keep only the first 3 sentences.
    # - Create a dictionary with the original review and the cleaned version.
    cleaned_reviews = [
        {
            "original": review,
            "cleaned": " ".join(sent_tokenize(review)[:3])
        }
        for review in review_text
    ]

    # Define the output filename where the cleaned reviews will be saved in JSON format.
    output_file = '3_cleaned_fake_review(s).json'
    
    # Open the file in write mode and dump the list of cleaned reviews with indentation for readability.
    with open(output_file, 'w') as f:
        json.dump(cleaned_reviews, f, indent=4)

    # Print a confirmation message indicating where the results are saved.
    print(f"Results saved in {output_file}")
    
    # Return the list of cleaned review dictionaries.
    return cleaned_reviews