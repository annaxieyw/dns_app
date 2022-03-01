from flask import Flask, request, jsonify
import socket
import requests

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = int(request.args.get('as_port'))

    if hostname == True and fs_port == True and as_ip == True and as_port == True and number == True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = "TYPE=A\nNAME={}".format(hostname)
        sock.sendto(message.encode(), (as_ip, as_port))
        mes, _ = sock.recvfrom(2048)
        sock.close()
        sdc = mes.decode().split('\n')
        value = sdc[2].split('=')[1]
        req = requests.get("http://fibonacci?number={}".format(value, fs_port, number))
        return jsonify(req.json()), 200
    else:
        return jsonify("No parameters"), 400

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
