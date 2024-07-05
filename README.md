# Product Management Interview Assistant

## Project Description

The Product Management Interview Assistant is a dynamic tool designed to assist in product management interviews. It leverages generative AI to simulate interview questions and speech capabilities to enhance the user experience. The assistant can generate interview questions based on difficulty levels (Easy, Medium, Hard) and question types (Product Sense, Market Research, Behavioral, User Experience), facilitating interview preparation for aspiring product managers.

### Key Features

- **Dynamic Interview Simulation**: Offers a variety of interview questions based on selected difficulty levels and question types.
- **Speech Recognition and Text-to-Speech**: Allows interaction via voice commands for answering questions and receiving prompts.
- **Follow-up Question Generation**: Generates context-aware follow-up questions to simulate realistic interview scenarios.
- **Integration with Generative AI**: Utilizes LangChain Groq API for generating intelligent responses and follow-up questions.

## Installation

To run the Product Management Interview Assistant locally, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
2. **Setup Virtual Environment**
   
   ``pip install virtualenv
   python -m venv env``

3. **Activate the virtual environment**
   
- On Windows:
  ```
  env\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source env/bin/activate
  ```
  
4. **Install the dependencies**
   
   ``
   pip install -r requirements.txt
   ``

5. **Set up environment variables**

  ``
  GROQ_API_KEY="your_groq_api_key"
  ``

6. **Run the application**

   ``
   python app.py
    ``

7. Follow on-screen instructions to interact with the assistant.

### Notes
Ensure your microphone is connected and accessible for speech recognition.
Replace "your_groq_api_key" with your actual Groq API key.

### Contributing
Please feel free to submit a Pull Request by CREATING A NEW BRANCH for every build. Let's preserve each version without complexities.

