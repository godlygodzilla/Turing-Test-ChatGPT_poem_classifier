import pandas as pd
import openai

# Configure your OpenAI API key
openai.api_key = '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'

def generate_review(poem):
    # Define the prompt for the OpenAI API
    prompt = f"This poem is about {poem}. Please write a review for it."

    # Generate the review using the OpenAI API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.1,
        top_p=1.0,
    )

    # Extract the generated review from the API response
    review = response.choices[0].text.strip()

    return review

def classify_poem(poem):
    # Define the prompt for the OpenAI API
    prompt = f"Classify the following poem into one of the categories:\n{poem}\nClass:"

    # Use the OpenAI API for text classification
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=20,
        n=1,
        temperature=0.1,
        top_p=1,
        stop=None
    )

    # Extract the predicted class from the API response
    predicted_class = response.choices[0].text.strip()

    return predicted_class

# Load the Excel file using pandas
df = pd.read_excel('C:/Users/aakar/Downloads/Book 15 (2).xlsx', sheet_name='Sheet1')

# Add new columns for the review and classification
df['Review'] = ''
df['Classification'] = ''

# Iterate over the rows in the DataFrame
for row in df.itertuples(index=False):
    poem = row.Poem

    # Generate the review
    review = generate_review(poem)

    # Classify the poem
    predicted_class = classify_poem(poem)

    # Update the DataFrame with the generated review and classification
    df.loc[df['Poem'] == poem, 'Review'] = review
    df.loc[df['Poem'] == poem, 'Classification'] = predicted_class

# Save the updated DataFrame to a new Excel file
df.to_excel('poems_with_reviews.xlsx', index=False)

print("Results saved to poems_with_reviews.xlsx")





