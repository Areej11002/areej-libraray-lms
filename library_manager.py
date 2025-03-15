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


