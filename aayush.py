import streamlit as st
import pyttsx3
import time
from pdf2image import convert_from_path
from PyPDF2 import PdfReader
import openai
import os

# Function to speak text
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def read_pdf(file_path):
    reader = PdfReader(file_path)
    slides_text = [page.extract_text() for page in reader.pages]
    return slides_text

def generate_notes(slides_text):
<<<<<<< HEAD
    
=======
>>>>>>> 5a16dd6f0a0f0ae5cf47b8facc8ffe949a64ca3e
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

def convert_pdf_to_images(pdf_path):
    return convert_from_path(pdf_path)

def main():
    st.title('Automated Study Notes')
    uploaded_file = st.file_uploader("Upload a PDF file", type=['pdf'])

    if uploaded_file:
        with open("test1.pdf", "wb") as f:
            f.write(uploaded_file.read())

        st.write("Uploaded PDF file successfully!")

        page_range = st.text_input("Which pages would you like to go over? (e.g., 1,2,3 or 1-3)")
        
        # Convert PDF to images
        images = convert_pdf_to_images("test1.pdf")

        # Convert PDF to text
        slides_text = read_pdf("test1.pdf")

        # Parse page range
        if "-" in page_range:
            start, end = map(int, page_range.split("-"))
            pages = list(range(start, end+1))
        else:
            pages = list(map(int, page_range.split(',')))

        # Filter based on selected pages
        slides_text = [slides_text[i-1] for i in pages]
        images = [images[i-1] for i in pages]

        if st.button('Generate and Speak Notes'):
            generated_notes = generate_notes(slides_text)

            for i, (image, note) in enumerate(zip(images, generated_notes)):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.image(image, caption=f"Slide {i+1}", use_column_width=True)

                with col2:
                    st.write(f"**Notes for Slide {i+1}**")
                    st.write(note)
                
                speak_text(f"Notes for slide {i+1}: {note}")

                # Wait for 3 seconds or until the user presses the skip button
                with st.empty():
                    for remaining in range(3, 0, -1):
                        st.write(f"Next slide in: {remaining} seconds")
                        time.sleep(1)
                
                if st.button('Skip to next slide'):
                    continue

if __name__ == '__main__':
    main()
<<<<<<< HEAD
=======



#openai.api_key = "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"
>>>>>>> 5a16dd6f0a0f0ae5cf47b8facc8ffe949a64ca3e
