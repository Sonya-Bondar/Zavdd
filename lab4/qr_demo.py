import qrcode


def show_qr():
    qr = qrcode.QRCode()
    qr.add_data("https://github.com")
    qr.make(fit=True)
    qr.print_ascii()