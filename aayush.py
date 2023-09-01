import streamlit as st
import pdfplumber
import openai
import pyttsx3
import time

# Function to speak text
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def read_pdf(file_path):
    slides_text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            slides_text.append(page.extract_text())
    return slides_text

def generate_notes(slides_text):
    generated_notes = []
    for slide in slides_text:
        prompt = f"Create study notes for the following slide content:\n{slide}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150
        )
        generated_notes.append(response.choices[0].text.strip())
    return generated_notes

def main():
    st.title('Automated Study Notes')

    pdf_path = st.text_input('Enter the path to your slides PDF:', 'test1.pdf')
    if st.button('Generate and Speak Notes'):
        slides_text = read_pdf(pdf_path)
        generated_notes = generate_notes(slides_text)
        
        for i, note in enumerate(generated_notes):
            # Using markdown to highlight the current note
            notes_to_show = [f"**{note}**" if j == i else note for j, note in enumerate(generated_notes)]
            st.write("---")
            st.markdown("\n".join(notes_to_show))
            speak_text(f"Notes for the current slide: {note}")

            # This delay is only to let the speaking finish. Replace with real-time tracking if possible.
            time.sleep(3)

if __name__ == '__main__':
    main()



#openai.api_key = "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"
