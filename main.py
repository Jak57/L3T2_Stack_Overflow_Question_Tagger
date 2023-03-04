import streamlit as st
from streamlit_quill import st_quill # text editor
from streamlit_ace import st_ace # for showing code editor
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES

import numpy as np
from sklearn import datasets
from PIL import Image # for displaying image

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC # support vector classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt
import pandas as pd # importing pandas
#import pickle # for saving/loading ML model

from ai_project import final_prediction # commenting here
import time # for showing spinner

st.title(" :pencil: Stack Overflow Question Tagger")

st.write("""
## :question: Ask a public question
""")

def sidebar_content():
    # showing stack overflow logo
    image = Image.open('images/stack_overflow_logo.png')
    st.sidebar.image(image)

    dataset_name = st.sidebar.selectbox("Select Dataset", ("StackSample"))
    classifier_name = st.sidebar.selectbox("Select Classifier", ("OneVsRestClassifier"))
    return dataset_name, classifier_name

dataset_name, classifier_name = sidebar_content()

# content in the main page
# showing rules for asking questions
st.info('''
:mag_right: **Writing a good question**

You are ready to ask a programming-related question and this form will help guide
you through the process.

:page_with_curl: Steps
+ Summarize your problem in a one-line title.
+ Describe your problem in more detail.
+ Describe what you tried and what you expected to happen.
+ Review your question and post it to the site.

''')

st.subheader('''
Title
''')

question = ""
q1 = ""
q2 = ""
q3 = ""

topic = st.text_input(
    label="Be specific and imagine you’re asking a question to another person.",
    placeholder="e.g. Is there any R function for finding the index of an element in a vector?")

title = str(topic)

st.subheader('''
What are the details of your problem?
''')
st.write("Introduce the problem and expand on what you put in the title. Minimum 20 characters.")

def problem_description():
    """
    Returns questions description
    """
    st.write("Write your text here:")
    content = st_quill(
        placeholder="Write your text here",
        key="quill"
    )
    st.markdown("---")

    if content:
        return str(content)
    else:
        return ""

description = " " + problem_description()
problem_code = " "
question = title + description + problem_code

if st.button("Predict Tag", type="primary"):
    with st.spinner('Wait for prediction...'):
        time.sleep(4)
    
    predictions = final_prediction(question)
    print(len(question))
    for i in range(len(predictions)):
        st.success(predictions[i])

