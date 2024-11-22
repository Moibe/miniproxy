import gradio as gr
import funciones

with gr.Blocks(css="footer {visibility: True}") as main:

    input1 = gr.Image()
    result = gr.Text()
   
    with gr.Row():
        demo = gr.Interface(
            fn=funciones.performa,
            inputs=[input1], 
            outputs=[result]
            )

main.launch(share=True, show_error=True)