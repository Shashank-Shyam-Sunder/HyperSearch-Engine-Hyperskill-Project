# HyperSearch Engine

A powerful text search engine that uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorization and cosine similarity to find the most relevant documents from a corpus based on user queries.

## Overview

The HyperSearch Engine is designed to search through a collection of text documents and return the most relevant results based on semantic similarity. It uses advanced natural language processing techniques to understand queries and match them with appropriate documents.

## Features

- **TF-IDF Vectorization**: Converts text documents and queries into numerical vectors for comparison
- **Cosine Similarity**: Measures the similarity between query and document vectors
- **Interactive Query Interface**: Command-line interface for real-time searching
- **Token Matching**: Highlights matching tokens in the most relevant document with their positions
- **Customizable Results**: Supports limit and offset parameters for result pagination
- **Natural Language Processing**: Uses spaCy for advanced text tokenization and processing

## Project Structure

```
HyperSearch Engine/
├── README.md            # This file
├── .gitignore           # Git ignore file
├── requirements_project.txt  # Project dependencies
├── requirements.txt     # Test dependencies
└── task/
    ├── task.py          # Main search engine implementation
    └── corpus/          # Document collection for searching
        ├── Branching.txt
        ├── Functional decomposition.txt
        ├── Intro to text representation.txt
        ├── Introduction to Python.txt
        ├── Invoking a function.txt
        └── Reader and Writer interfaces.txt
```

## Dependencies

The following Python packages are required:

- `numpy`: For numerical operations and vector calculations
- `spacy`: For natural language processing and tokenization
- `scikit-learn`: For TF-IDF vectorization and cosine similarity
- `string`: For punctuation handling (built-in)
- `os`: For file system operations (built-in)

### Installation

1. Install the required packages from the project root:
```bash
pip install -r requirements_project.txt
```

Or install manually:
```bash
pip install numpy spacy scikit-learn
```

2. Download the spaCy English language model:
```bash
python -m spacy download en_core_web_sm
```

## Usage

1. **Navigate to the task directory from project root**:
```bash
cd "HyperSearch Engine/task"
```

2. **Run the search engine**:
```bash
python task.py
```

3. **Follow the interactive prompts**:
   - Enter your search query when prompted
   - Specify the number of results you want (limit)
   - Specify how many results to skip (offset)
   - Choose whether to make another search

## How It Works

### 1. Document Processing
The engine reads all text files from the `corpus/` directory and processes them using TF-IDF vectorization, which:
- Calculates term frequency for each word in each document
- Applies inverse document frequency to weight rare terms higher
- Creates numerical vectors representing each document

### 2. Query Processing
When you enter a query:
- The query is tokenized using spaCy
- Only alphabetic and numeric tokens are considered
- The query is transformed into the same TF-IDF vector space as the documents

### 3. Similarity Calculation
The engine:
- Computes cosine similarity between the query vector and all document vectors
- Ranks documents by similarity score (0-1, where 1 is perfect match)
- Filters out documents with zero similarity

### 4. Result Display
For the most relevant document:
- Shows the document filename
- Displays matching tokens with their character positions in the document
- Supports pagination through limit and offset parameters

## Corpus Content

The current corpus contains educational materials on:

- **Branching.txt** (381 bytes): Programming control structures
- **Functional decomposition.txt** (835 bytes): Software design principles
- **Intro to text representation.txt** (725 bytes): Text processing concepts
- **Introduction to Python.txt** (953 bytes): Python programming basics
- **Invoking a function.txt** (721 bytes): Function calling in programming
- **Reader and Writer interfaces.txt** (508 bytes): I/O interface concepts

## Example Usage

```
Enter your query, please: Python functions
Enter limit: 3
Enter offset: 0

Introduction to Python.txt

Python 45 51
functions 123 132
function 145 153

Do you want to make another request? (yes/no): no
Bye!
```

## Key Functions

### `calculate_cosine_similarity(vector1, vector2)`
Calculates the cosine similarity between two vectors.

**Parameters:**
- `vector1`: First vector (array-like)
- `vector2`: Second vector (array-like)

**Returns:**
- `float`: Cosine similarity value between -1 and 1

## Customization

### Adding New Documents
1. Place new `.txt` files in the `corpus/` directory
2. Restart the application - it will automatically include new documents

### Modifying Search Parameters
- **Limit**: Controls how many results to display
- **Offset**: Controls how many top results to skip (useful for pagination)

## Technical Details

- **Vector Space**: Uses TF-IDF transformation to create document and query vectors
- **Similarity Metric**: Cosine similarity for measuring document relevance
- **Tokenization**: spaCy's English language model for advanced text processing
- **Preprocessing**: Filters out non-alphanumeric tokens for cleaner matching

## Performance Notes

- The TF-IDF model is built once when the application starts
- Query processing is real-time after initial model creation
- Larger corpus collections will require more memory and processing time
- Consider using more advanced models (Word2Vec, BERT) for better semantic understanding

## Troubleshooting

**Common Issues:**

1. **spaCy model not found**: Run `python -m spacy download en_core_web_sm`
2. **No results found**: Try broader or different search terms
3. **Import errors**: Ensure all dependencies are installed via pip

**File Path Issues:**
- The script expects to run from the task directory
- Corpus folder should be in the same directory as task.py
- Use proper Windows path separators when modifying file paths