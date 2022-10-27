# flask app

from flask import Flask
from utils import get_by_pk, get_all, get_by_skill, templates, get_position, load_candidates

app = Flask(__name__)


@app.route("/")
def page_index():
    return f"""
    <pre>
    Имя кандидата - {templates[0]['name']}\n
    Позиция кандидата - {templates[0]['position']}\n
    Навыки через запятую - {templates[0]['skills']}\n 
    
    Имя кандидата - {templates[1]['name']}\n
    Позиция кандидата - {templates[1]['position']}\n
    Навыки через запятую - {templates[1]['skills']}\n 
    
    Имя кандидата - {templates[2]['name']}\n
    Позиция кандидата - {templates[2]['position']}\n
    Навыки через запятую - {templates[2]['skills']}\n 
    
    Имя кандидата - {templates[3]['name']}\n
    Позиция кандидата - {templates[3]['position']}\n
    Навыки через запятую - {templates[3]['skills']}\n 
    
    Имя кандидата - {templates[4]['name']}\n
    Позиция кандидата - {templates[4]['position']}\n
    Навыки через запятую - {templates[4]['skills']}\n 
    
    Имя кандидата - {templates[5]['name']}\n
    Позиция кандидата - {templates[5]['position']}\n
    Навыки через запятую - {templates[5]['skills']}\n 
    
    Имя кандидата - {templates[6]['name']}\n
    Позиция кандидата - {templates[6]['position']}\n
    Навыки через запятую - {templates[6]['skills']}\n 
    
    </pre>
        """


@app.route("/candidate/")
def page_main():
    return f"""
    <img src='{templates[1]['picture']}'>
    <pre>
    
    Имя кандидата - {templates[1]['name']}\n
    Позиция кандидата - {templates[1]['position']}\n
    Навыки через запятую - {templates[1]['skills']}\n 
    
    </pre>
    """


@app.route("/skills/")
def find_skills():
    for candidates in range(len(load_candidates())):
        if 'python' in templates[candidates]['skills']:
            return f"""
                <pre>
        
                Имя кандидата - {templates[candidates]['name']}\n
                Позиция кандидата - {templates[candidates]['position']}\n
                Навыки через запятую - {templates[candidates]['skills']}\n 
                
                </pre>
                """


app.run()
