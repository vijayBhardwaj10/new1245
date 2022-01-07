from flask import Flask, jsonify
import time
import platform
my_system = platform.uname()
app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"Time of Call minikube new application deployment": time.time()})
    print(f"System: {my_system.system}")


print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
