# nsml.py

# To run this server:
# 1. Make sure you have Flask installed: pip install Flask
# 2. Save this code as nsml.py in the same directory as your HTML file.
# 3. Open your terminal or command prompt, navigate to that directory, and run either:
#    flask --app nsml run
#    OR
#    python nsml.py (after uncommenting app.run() below)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/nsml.py', methods=['POST'])
def receive_data():
    """
    Receives POST requests from the HTML client,
    parses the JSON data, and prints it to the console.
    """
    if request.is_json:
        data = request.get_json()
        print("\n--- Received Data ---")
        print(f"Phase: {data.get('phase')}")
        print(f"Input Data: {data.get('data')}")
        print(f"Timestamp: {data.get('timestamp')}")
        print("---------------------\n")

        # You can add server-side logic here, e.g.:
        # - Save data to a database
        # - Perform authentication checks
        # - Trigger OTP sending via an external service

        # The HTML is designed to proceed independently,
        # but a server can still send a response back.
        return jsonify({"status": "success", "message": "Data received by server"}), 200
    else:
        # If the request is not JSON, return an error
        print("Received non-JSON request.")
        return jsonify({"status": "error", "message": "Request must be JSON"}), 400

if __name__ == '__main__':
    # This block allows you to run the server directly using 'python nsml.py'
    # For development, 'flask --app nsml run' is often preferred as it includes a reloader.
    # When deploying, use a production-ready WSGI server like Gunicorn or uWSGI.
    print("Starting Flask server...")
    print("Access this server by running 'flask --app nsml run' in your terminal.")
    # For direct execution, uncomment the line below (not recommended for production)
    app.run(debug=True) # Uncommented this line
