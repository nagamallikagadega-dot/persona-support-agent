# Persona-Support-Agent

## Project Overview
An intelligent customer support agent that adapts its response style based on the customer's communication persona using Google Gemini AI and RAG pipeline.

## Features
- Persona Detection (Technical Expert, Frustrated User, Business Executive)
- RAG Pipeline with ChromaDB vector database
- Adaptive response generation using Gemini AI
- Streamlit Web UI
- Human escalation for sensitive issues

## Tech Stack
- Python 3.11
- Google Gemini AI
- ChromaDB
- LangChain
- Streamlit
- PyPDF

## Setup Instructions
1. Clone the repository
2. Install dependencies: pip install -r requirements.txt
3. Add Gemini API key in .env file
4. Run: streamlit run app.py

## Project Structure
- src/ - Core source code
- data/ - Knowledge base documents
- app.py - Main web application
