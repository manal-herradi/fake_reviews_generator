import json
import random

def generate_starting_prompts(num_prompts=5):
    """
    Get multiple neutral starting sentences for a product review.
    
    Args:
        num_prompts (int): The number of starting prompts to generate (default is 5).
        
    Returns:
        list: A list containing the selected starting prompts.
    """
    # A list of pre-written neutral sentences.
    neutral_sentences = [
        "After using this product for some time, I can say that",
        "Upon trying this product, I found that",
        "I’ve been using this for a while now, and I think that",
        "Having tested this product, I can confidently say that",
        "From my experience with this product, I believe that",
        "Based on my use of this product, it seems that",
        "This item, when used as intended, appears to be",
        "In my opinion, after using it, this product seems to be",
        "This product provides a satisfactory experience in",
        "After some use, I can conclude that this product is",
        "Having used this product for a few weeks, it’s clear that",
        "From what I’ve observed, this product works in",
        "I found that this product offers a reasonable performance in",
        "After a few tries, I can confirm that this product",
        "In my experience, this product seems to perform well in",
        "It’s evident that this product is suitable for",
        "When considering this product, it’s apparent that",
        "This product seems to meet its purpose in",
        "My time with this product has shown that",
        "This item seems to deliver its promises in"
    ]

    # Randomly select 'num_prompts' sentences from the list.
    # Using random.choices allows selection with repetition (the same sentence may be chosen more than once)!
    selected_prompts = random.choices(neutral_sentences, k=num_prompts)

    # Specify the output file name where the selected prompts will be saved in JSON format.
    output_file = '1_starting_prompts.json'
    
    # Open the output file in write mode and dump the selected prompts into it with pretty-printing (indentation) ;)
    with open(output_file, 'w') as f:
        json.dump(selected_prompts, f, indent=4)
    
    # Print a confirmation message to the console.
    print(f"Results saved to {output_file}")
    
    # Return the list of selected prompts.
    return selected_prompts