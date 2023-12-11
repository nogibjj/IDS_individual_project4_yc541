# Basic Website Template
from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        query = request.form['search_query']
        client = OpenAI(
            # Replace it with your own api key
            api_key = ''
        )
        response = client.chat.completions.create(
        messages=[
            {
            "role": "user",
            "content": query,
            }
        ],
        model="gpt-3.5-turbo",
        )
        return render_template('search_results.html', response=response.choices[0].message.content)
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)