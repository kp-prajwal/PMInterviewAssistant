import os
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import wave
import tempfile

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

llm = ChatGroq(model_name="mixtral-8x7b-32768", temperature=0.7, max_tokens=1024)

conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory()
)

def text_to_speech(text):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts = gTTS(text=text, lang='en')
        tts.save(fp.name)
        playsound(fp.name)
    os.unlink(fp.name)

def speech_to_text():
    while True:
        print("Speak now...")
        duration = 7  # Record for 7 seconds
        fs = 44100
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()

        # Save as WAV file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as fp:
            with wave.open(fp.name, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(fs)
                wf.writeframes((recording * 32767).astype(np.int16).tobytes())

            r = sr.Recognizer()
            with sr.AudioFile(fp.name) as source:
                audio = r.record(source)

        os.unlink(fp.name)

        # Recognize speech using Google Speech Recognition
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio, please try again.")
            text_to_speech("I could not understand you, please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            text_to_speech("There was an error with the speech recognition service, please try again.")
            return ""

def ask_question(question):
    print("Interview Buddy:", question)
    text_to_speech(question)
    return speech_to_text()

def generate_follow_up(context):
    prompt = f"Based on the following context about a product management interview, generate a relevant follow-up question:\n\n{context}\n\nFollow-up question:"
    return conversation.predict(input=prompt)

def interview_buddy():
    print("Welcome to your dynamic product management interview buddy!")
    text_to_speech("Welcome to your dynamic product management interview buddy!")

    while True:
        print("Please choose your difficulty level: Easy, Medium, or Hard.")
        text_to_speech("Please choose your difficulty level: Easy, Medium, or Hard.")
        difficulty_level = speech_to_text().lower()
        if difficulty_level in ['easy', 'medium', 'hard']:
            text_to_speech(f"You chose {difficulty_level} difficulty level.")
            break
        else:
            print("Invalid difficulty level. Please choose again.")
            text_to_speech("Invalid difficulty level. Please choose Easy, Medium, or Hard.")

    while True:
        print("Select the types of questions you want to be asked: Product Sense, Market Research, Behavioral, User Experience.")
        text_to_speech("Select the types of questions you want to be asked: Product Sense, Market Research, Behavioral, User Experience.")
        question_types = speech_to_text().lower()
        if any(q_type in question_types for q_type in ['product sense', 'market research', 'behavioral', 'user experience']):
            text_to_speech(f"You selected {question_types} questions.")
            break
        else:
            print("Invalid question type. Please choose from: Product Sense, Market Research, Behavioral, User Experience.")
            text_to_speech("Invalid question types. Please choose again.")

    questions = {
        "easy": {
            "product sense": [
                "Can you describe a recent project you worked on?",
                "What is your favorite aspect of product management?",
                "How do you approach setting goals for a new project?"
            ],
            "market research": [
                "How do you conduct basic market research?",
                "What factors do you consider when assessing market demand?",
                "Describe a time when market research influenced a product decision.",
                "How do you gather customer feedback for a new product?",
                "What are some important metrics to measure market potential?"
            ],
            "behavioral": [
                "Describe a time when you had to work under pressure.",
                "How do you handle conflicts within a team?",
                "Tell me about a challenging situation you faced and how you resolved it.",
                "What motivates you in your work?",
                "How do you prioritize tasks in a fast-paced environment?"
            ],
            "user experience": [
                "How do you ensure your product meets user needs?",
                "Describe a time when user feedback led to product improvements.",
                "What methods do you use to test product usability?",
                "How do you incorporate user-centered design principles?",
                "Describe a situation where you had to balance user feedback with business goals."
            ]
        },
        "medium": {
            "product sense": [
                "How do you prioritize features in a product roadmap?",
                "Describe a time when you had to pivot a product strategy.",
                "What are key considerations when defining a product roadmap?",
                "How do you align product features with customer needs?",
                "Describe a successful product launch strategy."
            ],
            "market research": [
                "How do you analyze competitors' products?",
                "What tools and methods do you use for competitive analysis?",
                "Describe a time when competitive analysis influenced a product decision.",
                "How do you validate market demand for a new product idea?",
                "What are the challenges of conducting global market research?"
            ],
            "behavioral": [
                "Describe a time when you had to resolve a conflict between team members.",
                "How do you handle disagreements with stakeholders?",
                "Tell me about a time when you had to manage a difficult team member.",
                "How do you ensure team cohesion during project execution?",
                "What strategies do you use to build strong relationships with stakeholders?"
            ],
            "user experience": [
                "How do you conduct usability testing for a product?",
                "Describe a time when user research led to a significant product improvement.",
                "What methods do you use to gather qualitative user feedback?",
                "How do you prioritize user experience enhancements?",
                "Describe a project where you successfully improved user retention rates."
            ]
        },
        "hard": {
            "product sense": [
                "Describe a time when you had to make a critical product decision under uncertainty.",
                "How do you prioritize conflicting stakeholder requirements?",
                "What strategies do you use to mitigate product risks?",
                "Tell me about a product failure you experienced and what you learned from it.",
                "How do you manage multiple product initiatives simultaneously?"
            ],
            "market research": [
                "How do you assess market trends and their impact on product strategy?",
                "Describe a time when you successfully introduced a disruptive product to the market.",
                "What are the ethical considerations in market research?",
                "How do you analyze complex market data to inform strategic decisions?",
                "What strategies do you use to identify emerging market opportunities?"
            ],
            "behavioral": [
                "Describe a challenging leadership situation you faced and how you resolved it.",
                "How do you foster innovation within a product team?",
                "Tell me about a time when you had to make a decision that went against popular opinion.",
                "How do you handle high-pressure situations that affect product delivery?",
                "What strategies do you use to manage team performance during tight deadlines?"
            ],
            "user experience": [
                "Describe a project where you successfully implemented a user-centered design approach.",
                "How do you integrate accessibility considerations into product design?",
                "Tell me about a time when you had to balance conflicting user needs.",
                "What metrics do you use to measure the success of UX improvements?",
                "How do you advocate for user experience in cross-functional teams?"
            ]
        }
    }

    # Fetch selected questions based on difficulty and question types
    selected_questions = []
    for q_type in question_types.split(", "):
        if q_type in questions[difficulty_level]:
            selected_questions.extend(questions[difficulty_level][q_type])
        else:
            print(f"Invalid question type '{q_type}', skipping.")

    context = ""
    for question in selected_questions:
        answer = ask_question(question)
        if answer.lower() == 'quit':
            break
        context += f"Q: {question}\nA: {answer}\n\n"

        # Generate and ask a follow-up question
        follow_up = generate_follow_up(context)
        follow_up_answer = ask_question(follow_up)
        if follow_up_answer.lower() == 'quit':
            break
        context += f"Follow-up: {follow_up}\nA: {follow_up_answer}\n\n"

    print("Thank you for using the product management interview buddy. Good luck with your interviews!")
    text_to_speech("Thank you for using the product management interview buddy. Good luck with your interviews!")

if __name__ == "__main__":
    interview_buddy()
