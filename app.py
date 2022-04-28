# --- Import the required modules:
# Note: If you store scripts in a folder (website in this case), python treats it as a package.
# What that means is that all the classes / functions in those scripts can be imported from website, 
# rather than the individual file names.
from website import create_app, create_database

if __name__ == "__main__":
    app = create_app()
    app.run(debug = True, 
            host="192.168.0.11", 
            port=5000)