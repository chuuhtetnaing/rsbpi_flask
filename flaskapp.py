from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def	index():
	return render_template('index.html')

@app.route('/aj_pryor')
def	aj_pryor():
	return render_template('Detailed_Cleaning_Visualization_Python.html')

@app.route('/aj_pryor_download_notebook')
def	aj_pryor_download():
	return send_file('resources/alan_jupyter.ipynb', as_attachment=True)

@app.route('/openvpn')
def vpn():
    return send_file('resources/rsbpi.ovpn', as_attachment=True)

if __name__ == '__main__':
	app.run()