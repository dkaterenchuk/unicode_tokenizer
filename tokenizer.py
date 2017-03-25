#!/usr/bin/env python

"""
#############################################################################
MIT License
Copyright (c) 2017 Denys Katerenchuk
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
#############################################################################


Tokenizes non-english text documents. It works by converting the text to unicode,
then splits into sentences, removes punctuation, and each sentece is split into a list
of words.

NOTE: this script is meant to be called from other programs. Hence, the main method is
only for testing purposes.

Usage:
    $ python tokenize <text_data_dir>

Args:
    text_data_dir - a folder with *.txt files

DEPENDENCIES:
    NLTK
"""

import os
import sys
import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


def tokenize_files(document):
    """
    Tokenizes a document into lists of sentences of words

    :param document: a string
    :return: sentence_list - a tokenized document
    """
    sentence_list = []
    document = document.lower()

    # converts non-english character into unicode
    text = unicode(document, errors='replace')

    # splits the document into sentences
    sent_list = sent_tokenize(text)

    # word tokenization
    for sent in sent_list:
        clean_sent = re.sub(r"[?|$|.|,|!|_|-|#|@|-]", r"", sent)
        sentence_list.append(word_tokenize(clean_sent))

    return sentence_list


def tokenize_documents(data_folder):
    """
    Reads a given directory and processes the files

    :param data_folder: str - a path to data
    :return: document_list - a list of list of words for each document
    """
    document_list = []

    for doc in os.listdir(data_folder):
        if doc.endswith(".txt"):
            with open(data_folder + "/" + doc) as doc_obj:
                document = doc_obj.read()
                sentence_list = tokenize_files(document)
                document_list.append(sentence_list)

    return document_list


def main(data_folder):
    """
    Reads all .txt documents is a given directory, tokenizes the data, and print the results

    NOTE: this function is created to illustrate the usage. Call individual functions of this script

    :param data_folder: - str: path to data directory
    :return:
    """
    tokenized_document_list = tokenize_documents(data_folder)
    print tokenized_document_list


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print __doc__
    else:
        main(sys.argv[1])


