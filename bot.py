import os
import openai
import gradio as gr

openai.api_key = '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'

start_sequence = "\nAI:"
restart_sequence = "\nHuman:"

#lines = os.listdir("")
# with open('C:\Users\Kunal-PC\Downloads\amazon gpt') as f:
# lines = f.readlines()

prompt = " Black (Renewed)		4.5 out of 5 stars	1,210 ratings	Only 3 left in stock - order soon. PlayStation 4 Slim 500GB Console [Discontinued] (Renewed)		4.5 out of 5 stars	1,243 ratings	Only 10 left in stock - order soon."


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
