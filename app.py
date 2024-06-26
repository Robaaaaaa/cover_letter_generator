import os
from pathlib import Path
import gradio as gr
import asyncio
import pandas as pd
from asyncflows import AsyncFlows
from asyncflows.utils.async_utils import merge_iterators
from asyncflows.log_config import get_logger

log = get_logger()


async def handle_submit(role, resume_text, job_description, name, hiring_manager, referral, company, cand_address, comp_address):
    flow = AsyncFlows.from_file("main.yaml").set_vars(
        role=role,
        resume_text=resume_text,
        job_description=job_description,
        name=name,
        hiring_manager=hiring_manager,
        referral=referral,
        company=company,
        cand_address=cand_address,
        comp_address=comp_address
    )

    async for outputs in flow.stream("generate.result"):
        cover_letter = outputs
        cover_letter = cover_letter.replace("/n ", "\n")
        cover_letter = cover_letter.replace("\r\n", os.linesep)
        yield {
            box: cover_letter
        }

    result = await flow.run()


with gr.Blocks() as demo:
    gr.Markdown("#📝To Generate a cover letter, Fill in the spaces and paste in your resume then click Generate Cover Letter")
    job_description = gr.Textbox(label="Job Description", placeholder="Describe the Job")
    role = gr.Textbox(label="Role", placeholder="What is the Job Title")
    resume_text = gr.Textbox(label="Resume Text", placeholder="Paste your resume here")
    name = gr.Textbox(label="Name", placeholder="What is your")
    hiring_manager = gr.Textbox(label="Hiring Manager", placeholder="Who is the hiring Manager")
    referral = gr.Textbox(label="Referral", placeholder="Where did you know about the job vacancy from")
    company = gr.Textbox(label="Company", placeholder="In which Company or organization are you applying")
    cand_address = gr.Textbox(label="Your Address ", placeholder="Your Address")
    comp_address = gr.Textbox(label="Company's Address", placeholder="Company's Adress")

    with gr.Column():
        box = gr.Textbox(label="Cover Letter", interactive=False)

    submit_button = gr.Button("Generate Cover Letter")

    submit_button.click(
        fn=handle_submit,
        inputs=[role, resume_text, job_description, name, hiring_manager, referral, company, cand_address, comp_address],
        outputs=[box],
    )

if __name__ == "__main__":
    demo.launch()