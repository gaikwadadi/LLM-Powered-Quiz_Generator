# Interactive LLM-Powered Quiz Generator

This project is an interactive quiz generator powered by OpenAI's GPT model, built using Streamlit. Users can customize the quiz by selecting the topic, difficulty level, number of questions, question type, and other specific parameters. The application leverages OpenAI's `ChatCompletion` API to dynamically create quizzes with options for multiple-choice, true/false, and short-answer questions.

## Features

* Interactive UI built with Streamlit
* Dynamic quiz generation based on user inputs
* Multiple question types: Multiple Choice, True/False, Short Answer
* Option to include explanations for each answer
* Customizable quiz parameters: difficulty, sub-topics, audience, and more
* Real-time LLM integration for content generation

## Technologies Used

* **Streamlit** for the web interface
* **OpenAI GPT (gpt-3.5-turbo)** for quiz generation
* **Python** for backend logic and API integration

---

## Setup Instructions

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/your-username/interactive-llm-quiz-generator.git
   cd interactive-llm-quiz-generator
   ```

2. **Create and Activate Virtual Environment (Recommended):**

   ```sh
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set OpenAI API Key:**
   Ensure your OpenAI API Key is set as an environment variable:

   ```sh
   export OPENAI_API_KEY='your_openai_api_key'
   ```

5. **Run the Application:**

   ```sh
   streamlit run app.py
   ```

6. **Access the App:**
   Visit [http://localhost:8501](http://localhost:8501) in your web browser.

---

## Usage

1. Fill in the quiz parameters such as:

   * Topic
   * Difficulty Level
   * Number of Questions
   * Question Type
   * Specific Sub-topics
   * Context Keywords
   * Target Audience
   * Language
   * Include Explanations

2. Click **Generate Quiz** to create the quiz.

3. The quiz will be generated dynamically and displayed in the interface.

---

## Project Structure

```
interactive-llm-quiz-generator/
├── app.py                   # Main application script
├── README.md                # Documentation
├── requirements.txt         # Dependencies
└── .env                     # Environment variables (optional)
```

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature:

   ```sh
   git checkout -b feature-name
   ```
3. Commit your changes:

   ```sh
   git commit -m 'Add some feature'
   ```
4. Push to the branch:

   ```sh
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

* OpenAI for the GPT model
* Streamlit for interactive UI

Feel free to reach out if you have any questions or suggestions!
