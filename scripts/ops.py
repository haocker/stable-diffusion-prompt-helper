import gradio as gr
from modules import script_callbacks

def on_ui_tabs():
    with gr.Blocks() as ops_interface:
        with gr.Row():
            preview_image_html = gr.HTML(value="<iframe src=\"https://www.wensoft.cn/ops\" style=\"width:100%;height:100vh\"></iframe>")

    return (ops_interface, "Prompt helper", "ops_interface"),

script_callbacks.on_ui_tabs(on_ui_tabs)