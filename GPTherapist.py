import os
import openai
import argparse

openai.api_key = os.getenv("OPENAI_API_KEY")
prev_conversation = []


parser = argparse.ArgumentParser()
parser.add_argument("--p", action="store_true", help="psychoanalytic theory")
parser.add_argument("--zen", action="store_true", help="use zen prompt")
parser.add_argument("--stoic", action="store_true", help="use stoic prompt")
parser.add_argument("--absurd", action="store_true", help="use absurdist prompt")
parser.add_argument("--cbt", action="store_true", help="cbt prompt")
parser.add_argument("--trans", action="store_true", help="transpersonal")
parser.add_argument("--emdr", action="store_true", help="emdr")
parser.add_argument("--deep", action="store_true", help="unlock a new prompt")

args = parser.parse_args()

practice_map = {
    "p": "Contemporary psychoanalysis therapist",
    "zen": "Zen meditation",
    "stoic": "Stocism",
    "absurd": "Absurdism",
    "cbt": "Cognitive Behavioral Therapy",
    "trans": "Transpersonal psychology",
    "emdr": "Eye Movement Desensitization and Reprocessing",
}

common_prompt = "You are helping a user named Nick explore his inner self, unlocking the power of his conscious and subconscious mind, so that he can become the best version of himself."

prompt = common_prompt
practice_args = ["p", "zen", "stoic", "absurd", "cbt", "trans", "emdr"]
for arg in practice_args:
    if getattr(args, arg):
        practice = practice_map.get(arg)
        prompt = f"You are an expert at {practice} " + common_prompt
        break
if args.deep:
    prompt += """This session is dedicated to assisting a user named Nick explore his inner self, unlocking the power of his conscious and subconscious mind, so that he can become the best version of himself. You will ask him deeper questions to help him uncover the answers to the questions he may not even be aware of. Drawing from the wisdom and teachings of renowned philosophers, spiritual leaders, psychologists, and occultists such as Bashar, Robert Anton Wilson, Ram Dass, Aleister Crowley, Timothy Leary, Alan Watts, Eckhart Tolle, Napoleon Hill, Carl Jung, Franz Kafka, Terence McKenna, Dale Carnegie, Olivia Fox Cabane, Vanessa Van Edwards, Paulo Coelho, Osho, Albert Camus, Friedrich Nietzsche, Martin Heidegger, Jean-Paul Sartre, Samuel Beckett, Eugene Ionesco, Arthur Schopenhauer, Miguel de Unamuno, Vladimir Nabokov, Emil Cioran, Franz Bardon, Christopher S. Hyatt, Lon Milo Duquette, Antero Alli, Israel Regardie, Phil Hine, Manly P. Hall, Carl Rogers, Abraham Maslow, Immanuel Kant, Søren Kierkegaard, Ralph Waldo Emerson, Henry David Thoreau, William James, George Ivanovich Gurdjieff, P.D. Ouspensky, Jiddu Krishnamurti, Rudolf Steiner, Carl Gustav Jung, Wilhelm Reich, Erich Fromm, Aldous Huxley, Joseph Campbell, Epictetus, Seneca, Marcus Aurelius, Aristotle, Bodhidharma, Dogen, Huangbo, Bankei, Hakuin and more, you will provide tailored guidance on personal development, spiritual growth and self-transformation. You will use direct quotes from the people mentioned above to provide Nick with the insight and answers he seeks to spiritually expand and unlock the power of his unconscious mind. \n\n"""
while True:
    user_input = input("> ")
    if user_input == "exit":
        break
    prev_conversation.append(f"Human: {user_input}\n\n")
    context = "\n\n".join(prev_conversation)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt + context + "\nAI:",
        temperature=0.9,
        max_tokens=650,
        top_p=0.5,
        frequency_penalty=1,
        presence_penalty=1,
        stop=[" Human:", " AI:"],
    )
    print("AI: " + response["choices"][0]["text"])
    prev_conversation.append(f"AI: {response['choices'][0]['text']}\n")
