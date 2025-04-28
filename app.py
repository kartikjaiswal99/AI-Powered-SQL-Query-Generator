from dotenv import load_dotenv
load_dotenv() # Loading environment variables from .env file


import streamlit as st
import os
import sqlite3

import google.generativeai as genai


# configure out API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to Load GOOgle gemini model and provide sql query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content([prompt[0], question])
    return response.text

# fun to retrieve query from the sql database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        curr = conn.cursor()
        curr.execute(sql)
        rows = curr.fetchall()
        conn.commit()
        conn.close()
        for row in rows:
            print(row)
        return rows
    except sqlite3.Error as e:
        st.error(f"Database error: {e}")
        return []


prompt = [
    """
    You are an expert AI assistant specialized in converting natural language questions into highly optimized SQL queries.

    Database Information:
    - Database Name: STUDENT
    - Tables:
      1. STUDENT
         - Columns: ID (Integer, Primary Key), NAME (Text), CLASS_ID (Integer, Foreign Key to COURSE.ID), SECTION (Text), MARKS (Integer)
      2. COURSE
         - Columns: ID (Integer, Primary Key), COURSE_NAME (Text), INSTRUCTOR_ID (Integer, Foreign Key to TEACHER.ID)
      3. TEACHER
         - Columns: ID (Integer, Primary Key), NAME (Text), DEPARTMENT (Text)

    Relationships:
    - STUDENT.CLASS_ID references COURSE.ID
    - COURSE.INSTRUCTOR_ID references TEACHER.ID

    Rules you must follow:
    - Strictly generate **only the SQL query** based on the question.
    - Do NOT wrap your SQL query inside triple backticks (```), markdown formatting, or any tags.
    - Avoid mentioning the word "SQL" in the output.
    - Always end every query with a semicolon (;).
    - Never provide explanations, apologies, or commentary — only the final SQL query.
    - Use appropriate JOINs when the query requires combining data from multiple tables.
    - If aggregation (COUNT, AVG, SUM) is needed, use correct GROUP BY or WHERE clauses.
    - Handle ambiguous questions with reasonable assumptions.
    - Always ensure case-insensitive handling of table and column names.
    - Prefer INNER JOIN unless otherwise necessary.

    Example Conversions:
    1. Question: How many student records are there?
       Query: SELECT COUNT(*) FROM STUDENT;

    2. Question: List all students studying in the Data Science course.
       Query: SELECT STUDENT.NAME FROM STUDENT INNER JOIN COURSE ON STUDENT.CLASS_ID = COURSE.ID WHERE COURSE.COURSE_NAME = 'Data Science';

    3. Question: Show the names of students along with their course names.
       Query: SELECT STUDENT.NAME, COURSE.COURSE_NAME FROM STUDENT INNER JOIN COURSE ON STUDENT.CLASS_ID = COURSE.ID;

    4. Question: Retrieve names of all instructors teaching a course.
       Query: SELECT DISTINCT TEACHER.NAME FROM TEACHER INNER JOIN COURSE ON TEACHER.ID = COURSE.INSTRUCTOR_ID;

    5. Question: List student names, course names, and their instructor names.
       Query: SELECT STUDENT.NAME, COURSE.COURSE_NAME, TEACHER.NAME FROM STUDENT INNER JOIN COURSE ON STUDENT.CLASS_ID = COURSE.ID INNER JOIN TEACHER ON COURSE.INSTRUCTOR_ID = TEACHER.ID;

    6. Question: Find the average marks scored by students in DevOps.
       Query: SELECT AVG(STUDENT.MARKS) FROM STUDENT INNER JOIN COURSE ON STUDENT.CLASS_ID = COURSE.ID WHERE COURSE.COURSE_NAME = 'DevOps';

    Think internally step-by-step to plan, but output only the final SQL query without extra text.
    """
]



st.set_page_config(
    page_title="SQL Query Generator",
    page_icon="🔎",
    layout="centered",
)

st.title("SQL Query Generator App")
st.markdown("**Ask your questions in plain English and retrieve results from the database!**")
st.write("---")

# Input box
question = st.text_input("Enter your question:", key="input")

# Button
if st.button("Generate and Query"):
    with st.spinner("Generating SQL and querying the database..."):
        response = get_gemini_response(question, prompt)
        st.code(response, language="sql")

        data = read_sql_query(response, "database.db")

        if data:
            st.success("Query successful! Here are the results:")
            st.table(data)
        else:
            st.warning("No results found or invalid query.")

st.write("---")
st.caption("Kartik Jaiswal")