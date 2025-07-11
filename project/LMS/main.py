# python3 main.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from DB import mysql, init_app


# Load env variables
load_dotenv()

app = Flask(__name__)
CORS(app)
init_app(app)

app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT'))

Owner = """
 █████╗ ███████╗██╗  ██╗██████╗  █████╗ ███████╗██╗   ██╗██╗     
██╔══██╗██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║   ██║██║     
███████║███████╗███████║██████╔╝███████║█████╗  ██║   ██║██║     
██╔══██║╚════██║██╔══██║██╔══██╗██╔══██║██╔══╝  ██║   ██║██║     
██║  ██║███████║██║  ██║██║  ██║██║  ██║██║     ╚██████╔╝███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝

"""
print(Owner)

# 🖥️ start the server
@app.route('/', methods=['GET'])
def Start_server():
    result = "server is running"
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=5000)