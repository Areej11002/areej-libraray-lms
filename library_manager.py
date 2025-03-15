import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
import time
import random
#import plotly.express as px
#import plotly.graph_objects as go
#from streamlit_lottie import st_lottie
import requests

#set page configuration
st.set_page_config(
    page_title="Personal Library Management System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

#custom cs for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem !important;
        color: #1E3A8A;
        margin-bottom: 1rem;
        font-weight: 700;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
            
    .sub_header{
        font-size: 1.8rem !important;
        color:3882F6;
        font-weight: 600;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    
    .sucess-message {
        padding: 1rem;
        background-color: #ECFDF5;
        border-left: 5px solid #108981;
        border-radius: 0.375rem;
    }
            
    .waring-message{
        padding: 1rem;
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
        border-radius: 0.375rem;
    }
            
    .book-card {
        background-color: #F3F4F6;
        border-radius: 0.5rem;
        padding: 1rem;
        marging-bottom: 1rem;
        border-left: 5px solid #3882F6;
        transition: transform 0.3s ease;
    }
            
    .book-card-hover{
        transofrm: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    }
    .read-badge {
        background-color: #108981;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.875rem;
        font-weight: 600;
    }
    .unread-badge {
        background-color: #F87171;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.875rem;
        font-weight: 600;   
    }
    .action-button {
        margin-right: 0.5rem;
    }
    .stButton>button {
        border-radius: 0.375rem;
    }
</style>
""", unsafe_allow_html=True)

def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r-json ()
    except:
        return None
    
if 'library' not in st.session_state:
    st.session_state.library =[]
if 'search_results' not in st.session_state:
    st.session_state.search_results = []
if 'book_added' not in st.session_state:
    st.session_state.book_added = False
if 'book_removed' not in st.session_state:
    st.session_state.book_removed = False
if 'current_view' not in st.session_state:
    st.session_state.current_view = "library"

#load library
def load_library():
    try:
        if os.path.exists('library-json'):
            with open('library.json', 'r')as file:
                st.session_state.library = json.load(file)
                return True
            return False
    except Exception as e:
            st.error(f"Error loading library: {e}")
            return False
        
#save library
def save_library():
    try:
        with open('library.json','w') as file:
            json.dump(st.session_state.library, file)
            return True
    except Exception as e:
        st.error(f"Error loading library: {e}")
        return False
    
#add a book to library
def add_book(title, author, publication_year, genre, read_status):
    book = {
        'title': title,
        'author': author,
        'publication_year': publication_year,
        'genre': genre,
        'read_status': read_status,
        'added_date': datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    }
    st.session_state.library.append(book)
    save_library()
    st.session_state.book_added = True
    time.sleep(0.5) #animation delay

#remove books
def remove_book(index):
    if 0 <= index < len(st.session_state.library):

        del st.session_state.library[index]
        save_library()
        st.session_state.book_removed = True
        return True
    return False

#search books
def search_books(search_term, search_by):
    search_term = search_term.lower()
    results = []

    for book in st.session_state.library:
        if search_by == "Title" and search_term in book['title'].lower():
            results.append(book)
        elif search_by == "Author" and search_term in book['author'].lower():
            results.append(book)
        elif search_by == "Genre" and search_term in book['genre'].lower():
            results.append(book)
    st.session_state.state.search_results = results

#calculate library status
def get_library_status():
    total_books = len(st.session_state.library)
    read_books = sum (1 for book in st.session_state.library if book['read status'])
    percent_read = (read_books / total_books * 100) if total_books > 0 else 0

    genres = {}
    authors = {}
    decades = {}

    for book in st.session_state.library:
        if book['genre'] in genres:
            genres[book['genres']] += 1
        else:
            genres[book['genre']] = 1

        #count author
        if book['author'] in genres:
            authors[book['author']] += 1
        else:
            authors[book['author']] = 1

        #count decades
        decades = (book['publication_year'] // 10) *10
        if decades in decades:
            decades[decades] +- 1
        else:
            decades[decades] = 1
        
    #sort by count
    genres = dict(sorted(genres.items(), key=lambda x: x[1], reverse=True))
    authors = dict(sorted(authors.items(), key=lambda x: x[1], reverse=True))
    decades = dict(sorted(decades.items(), key=lambda x: x[0]))

    return {
        'total_books' : total_books,
        'read_books' : read_books,
        'percent_read' : percent_read,
        'genres' : genres,
        'authors' : authors,
        'decades' : decades
    }



        
