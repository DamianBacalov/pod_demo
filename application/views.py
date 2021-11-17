from application import app
from flask import render_template


@app.route("/")
def home():
    local_ip = ""
    return render_template('home.html', 
                            node_name=app.config["NODE_NAME"], 
                            namespace=app.config["POD_NAMESPACE"], 
                            pod_name=app.config["POD_NAME"], 
                            pod_ip=app.config["POD_IP"])
