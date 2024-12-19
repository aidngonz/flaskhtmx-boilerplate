from flask import Flask, render_template, request
from models.counter import update_counter  # Import the update_counter function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', counter=update_counter('no_action'))  # Just display the current counter initially

@app.route('/r', methods=['POST'])
def update():
    action = request.form.get('action')  # Get the action (increment or decrement)
    new_counter = update_counter(action)  # Call the update_counter function from the model
    return render_template('counter.html', counter=new_counter)  # Return updated counter

if __name__ == '__main__':
    app.run(debug=True)
