from flask import Flask, request, jsonify
import socket


app = Flask(__name__)

def fib(n):
    if n <= 0:
        print("Incorrect input. Cannot be less or equal to 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    number = request.args.get('number')
    if number == True:
        return jsonify(fib(int(number))), 200
    else:
        return jsonify('Number is not provided'), 400


@app.route('/register', methods=['PUT'])
def register():
    data = request.get_json()
    hostname = data.get('hostname')
    ip = data.get('ip')
    as_ip = data.get('as_ip')
    as_port = int(data.get('as_port'))

    if hostname == True and ip == True and as_ip == True and as_port == True:
        sock = socket.socket(socket.AP_INET, socket.SOCK_DGRAM)
        message = "TYPE=A\nAME={}\nVALUE={}\nTTL=10".format(hostname, ip)
        sock.sendto(message.encode(), (as_ip, as_port))
        mes, _ = sock.recvfrom(2048)
        sock.close()
        if mes.decode() == 'Failed':
            return jsonify("Failed"), 500
        else:
            return jsonify("Success"), 201
    else:
        return jsonify("No parameters"), 400

app.run(host='0.0.0.0',
        port=9090,
        debug=True)

