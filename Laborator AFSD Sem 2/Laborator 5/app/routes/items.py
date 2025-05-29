from flask import Blueprint, jsonify, request, render_template
import json
import os

# Cream un Blueprint numit 'items'
items_bp = Blueprint('items', __name__)
# Calea catre fisierul JSON cu datele
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'items.json')

# Functie care citeste datele din fisier
def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Functie care salveaza datele in fisier
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Afiseaza pagina principala HTML
@items_bp.route('/')
def home():
    return render_template('index.html')

# Returneaza toate produsele
@items_bp.route('/items', methods=['GET'])
def get_items():
    return jsonify(load_data()), 200

# Returneaza un singur produs dupa id
@items_bp.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    items = load_data()
    item = next((item for item in items if item['id'] == item_id), None)
    return (jsonify(item), 200) if item else ('', 404)

# Adauga un produs nou
@items_bp.route('/items', methods=['POST'])
def add_item():
    items = load_data()
    new_item = request.get_json()

    # Atriubuie un ID (urmatorul) automat
    new_item['id'] = max([item['id'] for item in items], default=0) + 1

    items.append(new_item)
    save_data(items)
    return jsonify(new_item), 201

# Modifica un produs existent
@items_bp.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    items = load_data()
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return '', 404
    updated = request.get_json()
    item.update(updated)
    save_data(items)
    return jsonify(item), 200

# Sterge un produs dupa ID
@items_bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    items = load_data()
    new_items = [item for item in items if item['id'] != item_id]
    if len(new_items) == len(items):
        return '', 404
    save_data(new_items)
    return '', 200