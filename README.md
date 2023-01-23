# GPTherapist
GPTherapist

GPTherapist is a Python program that utilizes OpenAI's GPT-3 to create a chatbot therapist experience. The user can choose from various therapeutic practices and prompts to guide their conversation. The program captures the user's input and chatbot's responses in a conversation history to generate context for the model.
Getting started

Clone the repository

    git clone https://github.com/[username]/GPTherapist.git

Install the required packages

    pip install -r requirements.txt

Set your OpenAI API key as an environment variable

    export OPENAI_API_KEY="1234yourKEYhere5678"

If your name is not Nick, search for "Nick" in the python file and replace it with your name.

Run the program

    python3 GPTherapist.py --p 

You can replace --p with --zen, --stoic, --absurd, --cbt, --trans, --emdr to choose different therapeutic practices.

To end the conversation, type "exit"

Argument options

    --p : Contemporary psychoanalysis therapist
    --zen : Zen meditation
    --stoic : Stoicism
    --absurd : Absurdism
    --cbt : Cognitive Behavioral Therapy
    --trans : Transpersonal psychology
    --emdr : Eye Movement Desensitization and Reprocessing
    --deep : Unlock a 'deeper' prompt (can be used with the other arguments))

Note

This program requires a valid OpenAI API key. You can get one by signing up on the OpenAI website.

This is just a simple example of how GPT-3 can be used for creating a chatbot. You can customize the program and the prompt according to your needs and preferences.