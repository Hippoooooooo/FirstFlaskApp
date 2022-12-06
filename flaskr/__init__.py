# Import your dependencies
import os
from flask import Flask, jsonify
from flask_cors import CORS

# Define the create_app function
def create_app(test_config=None):
 # Create and configure the app
 # Include the first parameter: Here, __name__is the name of the current Python module.
 app = Flask(__name__,instance_relative_config=True)
 setup_db(app)
 
 CORS(app)
#  CORS(app,resources={r"/api/*": {"origins":"*"}})
 
 @app.after_request
 
 def after_request(response):
     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
     response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
     return response
    
 @cross_origin
 @app.route("/hello")
 def get_messages():
     return 'Getting Messages'

 # Return the app instance

 @app.route('/')
 def hello_world():
  return jsonify({'message':'Hola Arnau! how are you?'})

 @app.route('/arnau')
 def hello_arnau():
  return 'hello,Arnau ! Coco and Steel, and I are missing you'

 return app