## this is the fastAPI server for the restaurant
## you run the server process by typing "uvicorn main:app --host 127.0.0.1 --port 8000" in the terminal
## each menu item from the kitchen is a route in the server signified by the @app.get("/") decorator


from fastapi import FastAPI

app = FastAPI()

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
    return {"message": "Hello from localhost restaurant!", "status": "active"}


@app.get("/hello")
def hello_on_menu():
    return {"hello": "hello is on the menu"}

# Allows you to run the script directly via Python (Step 1: Gatekeeper)
#if __name__ == "__main__":
   # uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
