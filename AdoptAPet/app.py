#!/usr/bin/python
"""
CodeAcademy: Adopt A Pet - Introduction to Flask
"""

from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:
  <ul>
  <li><a href='/animals/dogs'>Dogs</a></li>
  <li><a href='/animals/cats'>Cats</a></li>
  <li><a href='/animals/rabbits'>Rabbits</a></li>
  </ul>
  '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = '''<h1>List of pets</h1>
  <ul>'''

  pet_list = enumerate(pets[pet_type])
  for pet_id, pet in pet_list:
    html += f'<li><a href="/animals/{pet_type}/{pet_id}">{pet["name"]}</a></li>\n'
  html += "</ul>"
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  return f'''
  <h1>{pet["name"]}</h1>
  <img src={pet["url"]}>
  <p>{pet["description"]}
  <ul>
  <li>Age: {pet["age"]}</li>
  <li>Breed: {pet["breed"]}</li>
  </ul>
  '''

if __name__ == "__main__":
    app.run(debug=True)

