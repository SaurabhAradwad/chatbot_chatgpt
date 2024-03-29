import os
import openai
import gradio as gr

openai.api_key = "api key" # paste your open ai api key

start_sequence = "\nAI:"
restart_sequence = "\nHuman:"

#lines = os.listdir("")
# with open('C:\Users\Kunal-PC\Downloads\amazon gpt') as f:
# lines = f.readlines()

prompt = "Your prompt here"


def openai_creat(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return response.choices[0].text


def conversation_history(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_creat(inp)
    history.append((input, output))
    return history, history


blocks = gr.Blocks()

with blocks:
    chatbot = gr.Chatbot()
    massage = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button('Click')
    submit.click(conversation_history, inputs=[massage, state], outputs=[chatbot, state])

blocks.launch(debug=True)
