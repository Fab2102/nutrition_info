from flask import Flask, render_template, jsonify

app = Flask(__name__)


DESIRED_ORDER = [
    "Brennwert",
    "Fett",
    "- davon gesättigte Fettsäuren",
    "Kohlenhydrate",
    "- davon Zucker",
    "Eiweiß",
    "Salz"
]
    
    
wine_data = {
    "GV_HB": {"Brennwert": "308 kJ / 74 kcal", "Fett": "<0.1 g", "- davon gesättigte Fettsäuren": "<0.01 g", "Kohlenhydrate": "1.2 g","- davon Zucker": "0.4 g","Eiweiß": "<0.1 g", "Salz": "<0.1 g"},
    "GV_STB": {"Brennwert": "309 kJ / 75 kcal", "Fett": "<0.1 g", "- davon gesättigte Fettsäuren": "<0.01 g", "Kohlenhydrate": "1.3 g","- davon Zucker": "0.5 g","Eiweiß": "<0.1 g", "Salz": "<0.1 g"},
    "GV_MT": {"Brennwert": "308 kJ / 74 kcal", "Fett": "<0.1 g", "- davon gesättigte Fettsäuren": "<0.01 g", "Kohlenhydrate": "1.2 g","- davon Zucker": "0.4 g","Eiweiß": "<0.1 g", "Salz": "<0.1 g"},
    "GV_AR": {"Brennwert": "308 kJ / 74 kcal", "Fett": "<0.1 g", "- davon gesättigte Fettsäuren": "<0.01 g", "Kohlenhydrate": "1.2 g","- davon Zucker": "0.4 g","Eiweiß": "<0.1 g", "Salz": "<0.1 g"},
    
    "GM": {"Brennwert": "308 kJ / 74 kcal", "Fett": "<0.1 g", "- davon gesättigte Fettsäuren": "<0.01 g", "Kohlenhydrate": "1.2 g","- davon Zucker": "0.4 g","Eiweiß": "<0.1 g", "Salz": "<0.1 g"},
    "RR": {"Brennwert": "308 kJ / 74 kcal", "Fett": "<0.1 g", "- davon gesättigte Fettsäuren": "<0.01 g", "Kohlenhydrate": "1.2 g","- davon Zucker": "0.4 g","Eiweiß": "<0.1 g", "Salz": "<0.1 g"},
    "WB": {"Brennwert": "308 kJ / 74 kcal", "Fett": "<0.1 g", "- davon gesättigte Fettsäuren": "<0.01 g", "Kohlenhydrate": "1.2 g","- davon Zucker": "0.4 g","Eiweiß": "<0.1 g", "Salz": "<0.1 g"},
    "RV_STB": {"Brennwert": "308 kJ / 74 kcal", "Fett": "<0.1 g", "- davon gesättigte Fettsäuren": "<0.01 g", "Kohlenhydrate": "1.2 g","- davon Zucker": "0.4 g","Eiweiß": "<0.1 g", "Salz": "<0.1 g"},
    
    "ZW_ROSE": {"Brennwert": "308 kJ / 74 kcal", "Fett": "<0.1 g", "- davon gesättigte Fettsäuren": "<0.01 g", "Kohlenhydrate": "1.2 g","- davon Zucker": "0.4 g","Eiweiß": "<0.1 g", "Salz": "<0.1 g"},
    "ZW_C": {"Brennwert": "308 kJ / 74 kcal", "Fett": "<0.1 g", "- davon gesättigte Fettsäuren": "<0.01 g", "Kohlenhydrate": "1.2 g","- davon Zucker": "0.4 g","Eiweiß": "<0.1 g", "Salz": "<0.1 g"},
    "ZW_RE": {"Brennwert": "308 kJ / 74 kcal", "Fett": "<0.1 g", "- davon gesättigte Fettsäuren": "<0.01 g", "Kohlenhydrate": "1.2 g","- davon Zucker": "0.4 g","Eiweiß": "<0.1 g", "Salz": "<0.1 g"}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data/<wine_name>')
def get_data(wine_name):
    data = wine_data.get(wine_name, {})
    sorted_data = [(key, data.get(key, 'N/A')) for key in DESIRED_ORDER]
    return jsonify(sorted_data)


if __name__ == '__main__':
    app.run(debug=True)
