from .main import letterify

import gradio as gr


def interface_func(num):
    return letterify(num)

iface = gr.Interface(
    fn=letterify, 
    inputs=gr.Number(), 
    outputs="text",
)

iface.launch()