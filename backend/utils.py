from reportlab.pdfgen import canvas
import os

def create_pdf_certificate(issuance):
    filename = f"certificate_{issuance.id}.pdf"
    filepath = os.path.join("certificates", filename)
    os.makedirs("certificates", exist_ok=True)
    c = canvas.Canvas(filepath)
    c.setFont("Helvetica", 14)
    c.drawString(100, 750, "SHARE CERTIFICATE")
    c.drawString(100, 720, f"Shareholder: {issuance.shareholder.name}")
    c.drawString(100, 700, f"Shares: {issuance.shares}")
    c.drawString(100, 680, f"Price per Share: {issuance.price}")
    c.drawString(100, 660, f"Date: {issuance.date.strftime('%Y-%m-%d')}")
    c.drawString(100, 620, "This certificate confirms the issuance of shares.")
    c.showPage()
    c.save()
    return filepath
