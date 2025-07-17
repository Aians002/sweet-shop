Sweet Shop Management System
A web-based application to manage a sweet shop, built with Python, Flask, and tested using TDD principles. Users can add, delete, view, search, sort, purchase, and restock sweets through a web interface.
Setup

Clone the repository:
git clone <repository-url>
cd sweet-shop-system

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run the Flask application:
python app.py

Access the app at http://127.0.0.1:5000/.

Run the tests:
python -m unittest discover -s tests

Features

Add Sweets: Add new sweets with unique IDs, names, categories, prices, and quantities.
Delete Sweets: Remove sweets by ID.
View Sweets: List all sweets with options to sort by price or name.
Search Sweets: Filter sweets by name, category, or price range.
Sort Sweets: Sort the sweets list by price or name.
Purchase Sweets: Reduce stock by purchasing sweets.
Restock Sweets: Increase stock levels for existing sweets.

Notes

Data is stored in memory using a dictionary, so it resets when the app restarts.
The web interface uses Flask and Bootstrap for a responsive design.
All functionalities are backed by comprehensive unit tests in tests/test_sweet_shop.py.
