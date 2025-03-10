from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team', methods=['GET', 'POST'])
def team_creation():
    companions = [
        {"name": "Astarion", "race": "High Elf", "class": "Rogue"},
        {"name": "Gale", "race": "Human", "class": "Wizard"},
        {"name": "Karlach", "race": "Zariel Tiefling", "class": "Barbarian"},
        {"name": "Lae'zel", "race": "Githyanki", "class": "Fighter"},
        {"name": "Shadowheart", "race": "High Half-Elf", "class": "Cleric of Shar"},
        {"name": "Wyll", "race": "Human", "class": "Warlock"}
    ]
    if request.method == 'POST':
        team = [request.form.get(f'character{i}') for i in range(1, 5)]
        return render_template('team_result.html', team=team)
    
    return render_template('team.html', companions=companions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
