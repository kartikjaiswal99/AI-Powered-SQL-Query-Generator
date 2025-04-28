
---

# AI-Powered SQL Query Generator

This is an intelligent web application that allows users to convert natural language questions into SQL queries. The app integrates the Google Gemini 1.5 Pro API to generate accurate SQL queries based on user input and retrieve data from an SQLite database. Built using Python, Streamlit, and SQLite, the app provides a simple and interactive interface to query data from a database using conversational language.

## Features

- **Natural Language to SQL Conversion**: Converts user input (natural language questions) into SQL queries to interact with an SQLite database.
- **Real-Time Data Retrieval**: Executes the AI-generated SQL queries on an SQLite database to retrieve real-time results.
- **Streamlit Interface**: A clean and intuitive web interface to input questions and view results in real-time.
- **Optimized Prompts**: Engineered precise prompts for the Google Gemini 1.5 Pro model to ensure accurate query generation under different scenarios.

## Technologies Used

- **Streamlit**: For building the web application interface.
- **Google Gemini 1.5 Pro API**: Used to generate SQL queries from natural language input.
- **SQLite**: Database used for storing and retrieving data.
- **Python**: Programming language for the backend logic.
- **Prompt Engineering**: Fine-tuned prompts for generating accurate SQL queries.

## Installation

### Prerequisites

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-sql-query-generator.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the `.env` file with your Google Gemini API key:
   - Create a `.env` file in the root directory and add your API key:
   ```text
   GOOGLE_API_KEY=your_google_gemini_api_key
   ```
5. For using existing database entries u can run this file:
   ```bash
   python sql.py
   ```


### Running the Application

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to `http://localhost:8501` to interact with the app.

## Usage

1. **Input a Question**: In the web app, type a natural language question related to the SQLite database (e.g., "How many students are there in class A?").
2. **Get SQL Query**: The app will generate a corresponding SQL query using the Google Gemini 1.5 Pro model.
3. **View Results**: The app will execute the generated SQL query on the SQLite database and display the results.

## Example - 1

**Question**: "What is the average marks of students in Data Science class?"
- **Generated SQL Query**: `SELECT AVG(MARKS) FROM STUDENT WHERE CLASS = 'Data Science';`
- **Result**: Displays the average marks of students in the Data Science class from the SQLite database.

## Example - 2

### **Question**:
"Show me the names of students who scored above the average marks in their respective classes, along with their course name, section, and the name of the teacher instructing that course, student marks in descending order."

### **Generated SQL Query**:
```sql
SELECT 
    s.NAME, 
    c.COURSE_NAME, 
    s.SECTION, 
    t.NAME AS TEACHER_NAME, 
    s.MARKS
FROM 
    STUDENT s
INNER JOIN 
    COURSE c ON s.CLASS_ID = c.ID
INNER JOIN 
    TEACHER t ON c.INSTRUCTOR_ID = t.ID
WHERE 
    s.MARKS > (
        SELECT AVG(MARKS) 
        FROM STUDENT s2 
        WHERE s2.CLASS_ID = s.CLASS_ID
    )
ORDER BY 
    s.MARKS DESC;

