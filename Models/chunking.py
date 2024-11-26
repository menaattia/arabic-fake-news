import pandas as pd

def chunk_text_by_words(df, chunk_size=120):
    # Initialize an empty list to store the new rows
    chunked_data = []

    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        text, label = row['text'], row['label']
        
        # Split the text into words
        words = text.split()
        
        # Chunk the text into segments of chunk_size words
        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i + chunk_size])
            chunked_data.append({'text': chunk, 'label': label})
    
    # Convert the list of new rows into a DataFrame
    chunked_df = pd.DataFrame(chunked_data)
    return chunked_df
