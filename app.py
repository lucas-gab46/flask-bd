from flask import Flask, jsonify, request, render_template, url_for
from datetime import datetime, timedelta

from extensions import db
from models.payment import Payment
from payments.pix import Pix

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/payments/pix', methods=['POST'])
def pix():
    data = request.get_json()
    if 'value' not in data:
        return jsonify({"Message": "Invalid Value"}), 400

    expiration_date = datetime.now() + timedelta(hours=30, minutes=10, seconds=14)

    new_payment = Payment(
        value=data['value'],
        expiration_date=expiration_date,
        paid=False
    )

    pix_obj = Pix()
    data_payment_pix = pix_obj.create_payment(data['value'])
    new_payment.qr_code = data_payment_pix["qr_code_path"]

    db.session.add(new_payment)
    db.session.commit()

    return jsonify({
        "expiration_date": expiration_date.isoformat(),
        "message": "The payment was created",
        "Payment": new_payment.to_dict()
    })

@app.route('/payments/pix/confirmar', methods=['POST'])
def confirmar_pix():
    data = request.get_json()
    payment_id = data.get('payment_id')
    payment = Payment.query.get(payment_id)

    if not payment:
        return jsonify({'message': 'Payment not found'}), 404

    payment.paid = True
    db.session.commit()

    return jsonify({'message': 'The payment was confirmed'})

@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    payment = Payment.query.get(payment_id)
    
    if not payment:
        return jsonify({'message': 'Payment not found'}), 404
    now = datetime.now()

    return render_template('payment.html', payment=payment, now=now)

@app.route('/payment/confirmar/<int:payment_id>', methods=['GET'])
def confirmar_pagamento(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    return render_template('confirmar_pagamento.html', payment=payment)
if __name__ == '__main__':
    app.run(debug=True)

