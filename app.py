import gradio as gr
from openai import OpenAI
import os

os.environ[
    'OPENAI_API_KEY'] = "YOUR_API_KEY_HERE"
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def get_ai_response(input: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        stream=True,  # Enable token streaming
        temperature=0.2,
        messages=[
            {"role": "system", "content":
                """
                You are a robot for guiding pilgrims during 
                Hajj and Omrah in Makkah and Madinah.
                You will be asked in Arabic. And your job is to answer in Arabic.
                Your answers should be related to Hajj, Omrah, Makkah and Madinah.
                """},
            {"role": "user", "content": input}
        ])

    partial_response = ""
    for stream_response in response:
        token = stream_response.choices[0].delta.content or ""
        partial_response += token
        yield partial_response


with gr.Blocks() as demo:
    gr.Markdown("""
  <br>

  # مساعدك في الحج والعمرة
  ### By نجلاء الصاعدي
  <br>
  """)
    with gr.Row():
        with gr.Column():
            question = gr.Textbox(lines=5, label="اكتب سؤالك هنا:")
            # gr.Examples(examples=["Write a poem in cockney accent telling why West Ham are massive.",
            #                       "Write a poem about love."], inputs=question)
            btn = gr.Button(value="إرسال")
        with gr.Column():
            answer = gr.Textbox(lines=15, label="Response from AI:")

        btn.click(fn=get_ai_response, inputs=question, outputs=answer)

        demo.queue()
        demo.launch(share=False, debug=False)
