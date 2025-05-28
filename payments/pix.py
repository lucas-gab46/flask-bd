import uuid
import qrcode
import os






class Pix: 
    def __init__(self):
        os.makedirs("static/qr_codes", exist_ok=True)

    def create_payment(self, value):
        bank_payment_id = uuid.uuid4()
        hash_payment = f"hash_payment_{bank_payment_id}_value_{value}"
        img = qrcode.make(hash_payment)

        path = f"static/qr_codes/{bank_payment_id}.png"
        img.save(path)

        return {
            "qr_code_path": path,
            "value": value
        }
