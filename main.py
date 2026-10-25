## this is the fastAPI server for the restaurant
## you run the server process by typing "uvicorn main:app --host 127.0.0.1 --port 8000" in the terminal
## each menu item from the kitchen is a route in the server signified by the @app.get("/") decorator


from fastapi import FastAPI

app = FastAPI()

# 1. Our static menu list (simulating a database)
MENU_ITEMS = {
    "burger": {"price": 9.99, "category": "Main Course", "spicy": False},
    "pizza": {"price": 12.99, "category": "Main Course", "spicy": False},
    "tacos": {"price": 8.50, "category": "Appetizer", "spicy": True}
}

# Define a route (Step 3: Your Python Code Brain)
@app.get("/")
def read_root():
    # ---------------------------------------------
    # YOUR CUSTOM LOGIC GOES HERE!
    # For example: 
    # - Calculate a metric
    # - Open a local file
    # - Call an AI model
    # ---------------------------------------------
    return {"message": "Welcome to the Localhost Restaurant!", "status": "active"}


# 2. Dynamic Route using a Path Parameter ({item_name})
@app.get("/menu/{item_name}")
def get_menu_item(item_name: str):
    # Check if the requested item exists in our dictionary
    if item_name in MENU_ITEMS:
        return {"item": item_name, "details": MENU_ITEMS[item_name]}
    else:
        return {"error": "Dish not found on the menu!"}, 404
