from flask import Flask, render_template,request, send_file
import io
import torch
import  gc
# from torch import autocast 
from torch.cuda.amp import autocast


app = Flask(__name__)
def run_inference(prompt):
  return prompt
@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route('/results', methods= ["POST"])
def submit():
    if request.method == 'POST':
        prompt = request.form.get("Prompt")
        img_data = run_inference(prompt)
    return render_template("results.html",n=img_data)