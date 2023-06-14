# Most Frequent Word Catcher

The "Most Frequent Word Catcher" is a Python algorithm designed to find the most frequently occurring words in a given text and identify their neighboring words. This algorithm can be used to extract key insights from a text corpus and analyze word usage patterns.

## Features

- Identifies the most repeated words in a text
- Captures the neighboring words of the most repeated words
- Counts the occurrences of neighboring words
- Supports removal of common stop words
- Case-insensitive word matching

## Getting Started

To use the "Most Frequent Word Catcher" algorithm, follow these steps:

1. Ensure you have Python installed on your system (version 3.x is recommended).
2. Clone or download this repository to your local machine.

## Usage

1. Place the text you want to analyze in a file named `text.txt` within the project directory.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to execute the algorithm:

    ```bash
    python frequent_word_catcher.py
    ```

4. The program will display the most repeated words in the text and their neighboring words.
5. The program will also provide the count of occurrences for each neighboring word.
6. You can modify the algorithm or customize its behavior by editing the `frequent_word_catcher.py` file.

## Dependencies

The "Most Frequent Word Catcher" algorithm relies on the following dependencies:

- Python (version 3.x)
- NLTK (Natural Language Toolkit) library for text processing

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
