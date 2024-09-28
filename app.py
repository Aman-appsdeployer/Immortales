from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Immortales.html')

@app.route('/family')
def family():
    return render_template('family.html')

@app.route('/family-story')
def family_story():
    return render_template('family-story.html')

@app.route('/cultural')
def cultural():
    return render_template('cultural.html')

@app.route('/kids')
def kids():
    return render_template('kids.html')
    
@app.route('/Immortales')
def Immortales():
    return render_template('Immortales.html')

if __name__ == '__main__':
    # Use the PORT environment variable if it exists, otherwise default to port 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Run the Flask app with the correct host and port
    app.run(debug=True, host='0.0.0.0', port=port)
