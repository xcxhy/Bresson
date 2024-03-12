'''
Author: your name
Date: 2024-03-10 01:30:16
LastEditTime: 2024-03-13 00:49:45
LastEditors: DESKTOP-6KCA68K
Description: In User Settings Edit
FilePath: \Bresson\Gemini\gemini.py
'''
import os
os.environ['http_proxy'] = 'http://127.0.0.1:7890/'
os.environ['https_proxy'] = 'http://127.0.0.1:7890/'
import argparse
import google.generativeai as genai
genai.configure(api_key="AIzaSyChYt5oIJWPuX7do96lnwzCII7nT3K6EUU")
from IPython.display import display
from IPython.display import Markdown
import PIL.Image
from log_utils import build_logger
logger  = build_logger("gemini", "gemini.log")

# 定义一个调用gemini api的类，用用于实现单轮和多轮对话，同时开放API接口

class Gemini_Inference(object):
    def __init__(self):
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)
    def init_model(self, model_name):
        if "vision" in model_name:
            self.mode = "dual"
        else:
            self.mode = "single"
        self.model = genai.GenerativeModel(model_name)
        
    