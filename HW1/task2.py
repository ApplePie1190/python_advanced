import re
from collections import Counter


def most_common_words(text):
    cleaned_text = re.sub(r'[^\w\s]', ' ', text).lower()
    words = cleaned_text.split()
    word_counts = Counter(words)
    return [word for word, count in word_counts.most_common(10)]


if __name__ == '__main__':
    text = '''
    Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first 
    released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. 
    Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-
    scale projects.
    Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including procedural, 
    object-oriented, and functional programming. Python is often described as a "batteries included" language due to its 
    comprehensive standard library.
    Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. 
    CPython, the reference implementation of Python, is open source software and has a community-based development model, 
    as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software 
    Foundation.
    Python's popularity and beginner-friendly reputation has spawned numerous libraries, frameworks, and tools specifically 
    for Python development. Some of the most popular include Django, Flask, NumPy, and SciPy.'''
    common_words = most_common_words(text)
    print(common_words) 
