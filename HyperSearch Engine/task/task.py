import os
import numpy as np
# %%
import spacy
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
vectorizer = TfidfVectorizer()
punctuations = string.punctuation
# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def calculate_cosine_similarity(vector1, vector2):
    """
    Calculate the cosine similarity between two vectors.

    Args:
        vector1 (array-like): First vector
        vector2 (array-like): Second vector

    Returns:
        float: Cosine similarity between the two vectors (value between -1 and 1)
    """
    # Reshape vectors if needed to ensure they are 2D arrays
    v1 = np.array(vector1).reshape(1, -1)
    v2 = np.array(vector2).reshape(1, -1)

    # Calculate cosine similarity
    similarity = cosine_similarity(v1, v2)[0][0]

    return similarity

os.chdir(r'C:\Shashank_work\Python_Works\HyperSearch_Engine\HyperSearch Engine\task')
# Path to the corpus folder
docs_folder = os.path.join(os.getcwd(), "corpus")
# Get all files from the corpus folder
files = os.listdir(docs_folder)
# print(files)
# # Print the list of files
# print("Files in corpus folder:")
dataset = []
for file in files:
    with open(os.path.join(docs_folder, file), "r") as f:
        text = f.read()
        dataset.append(text)
        # print(f"{file}: {len(text)}")

X = vectorizer.fit_transform(dataset)
feature_names = vectorizer.get_feature_names_out()
tf_idf_arr = X.toarray()

user_query_request = "yes"
# %%
while user_query_request == "yes":
    ### User entries
    user_query = input("Enter your query, please:")
    query_doc = nlp(user_query)
    query_tokens = {token.text for token in query_doc if token.is_alpha or token.is_digit}

    # search_limit = int(input("Enter the number of search results you want:"))
    # offset_doc_no = int(input("Enter the number of documents you want to skip:"))
    if not query_tokens:
        search_limit = int(input("Enter limit:"))
        offset_doc_no = int(input("Enter offset:"))
        print("No results were found for your query")
        print()
        # print("Do you want to make another request?")
        user_query_request = input("Do you want to make another request? (yes/no)")
        if user_query_request == "no":
            print("Bye!")
            break
    else:
        # user_query = "What is BERT?"
        search_limit = int(input("Enter limit:"))
        offset_doc_no = int(input("Enter offset:"))
        ### Converting the query into the same tfidf space as our dataset using vectorizer.transform() method
        query_vector = vectorizer.transform([user_query])
        query_tf_idf = query_vector.toarray()

        ### Computing cosine similarities between query and the documents
        cosine_similarities = [float(calculate_cosine_similarity(query_tf_idf.tolist()[0],tf_idf_arr[i].tolist()))  for i in range(len(tf_idf_arr))]

        # for i in range(len(files)):
        #     print(f"{files[i]}: {cosine_similarities[i]:.3f}")
        # %%
        ### Printing the results differently taking into account the search_limit and offset_doc_no
        cosine_similarities_dict = dict(zip(files,cosine_similarities))
        cosine_similarities_dict = dict(sorted(cosine_similarities_dict.items(), key=lambda item: item[1], reverse=True))
        # Filter out documents with 0 similarity
        filtered_results = [(file, sim) for file, sim in cosine_similarities_dict.items() if sim > 0]

        # Apply offset and limit
        results_to_display = filtered_results[offset_doc_no:offset_doc_no + search_limit]

        ### Most suited document
        most_suited_doc = results_to_display[0][0]

        # Step 3: Print
        # for file, score in results_to_display:
        #     print(f"{file}: {score:.3f}")
        print()
        print(f'{most_suited_doc}')

        ### Finding the text from the most suitable doc to tokenize the text:
        ind_most_suited_doc = files.index(most_suited_doc)
        text_most_suited_doc = dataset[ind_most_suited_doc]
        doc = nlp(text_most_suited_doc)

        # Step: Match and extract positions from the original doc
        matches = [
            (token.text, token.idx, token.idx + len(token.text) - 1)
            for token in doc
            if token.text in query_tokens
        ]

        # Step: Sort and print
        matches.sort(key=lambda x: x[1])

        for token, start, end in matches:
            print(f"{token} {start} {end}")

        print()
        # print("Do you want to make another request?")
        user_query_request = input("Do you want to make another request? (yes/no)")
        if user_query_request == "no":
            print("Bye!")
            break

# try:
# for i in range(offset_doc_no, offset_doc_no + search_limit):
#     if cosine_similarities[i] > 0:
#         print(f"{files[i]}: {cosine_similarities[i]:.3f}")
#     if i == search_limit+offset_doc_no-1:
#         break
# # except IndexError:
# #         print("No results found")

# %%

# # Example usage of the cosine similarity function
# if __name__ == "__main__":
#     # Sample vectors
#     vector_a = [1, 2, 3, 4, 5]
#     vector_b = [5, 4, 3, 2, 1]
#
#     # Calculate similarity
#     similarity = calculate_cosine_similarity(vector_a, vector_b)
#     print(f"Cosine similarity between vector_a and vector_b: {similarity:.4f}")
#
#     # Another example with different vectors
#     vector_c = [0, 1, 0, 1]
#     vector_d = [1, 0, 1, 0]
#     similarity = calculate_cosine_similarity(vector_c, vector_d)
#     print(f"Cosine similarity between vector_c and vector_d: {similarity:.4f}")
