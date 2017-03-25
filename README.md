# unicode_tokenizer
Tokenizes text with non-english (non-ascii) characters

Tokenizes non-english text documents. It works by converting the text to unicode,
then splits into sentences, removes punctuation, and each sentece is split into a list
of words.

NOTE: this script is meant to be called from other programs. Hence, the main method is
only for testing purposes.

## Usage:
    $ python tokenize <text_data_dir>

## Args:
    text_data_dir - a folder with *.txt files

## DEPENDENCIES:
    NLTK
	
