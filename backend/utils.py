from reportlab.pdfgen import canvas
import os

def create_pdf_certificate(issuance):
    filename = f"certificate_{issuance.id}.pdf"
    filepath = os.path.join("certificates", filename)
    os.makedirs("certificates", exist_ok=True)
    c = canvas.Canvas(filepath)
    c.setFont("Helvetica", 14)
    c.drawString(100, 750, "SHARE CERTIFICATE")
    c.drawString(100, 720, f"Shareholder: {issuance.shareholder.full_name}")
    c.drawString(100, 700, f"Shares: {issuance.num_shares}")
    c.drawString(100, 680, f"Price per Share: {issuance.price_per_share}")
    c.drawString(100, 660, f"Date: {issuance.issued_at.strftime('%Y-%m-%d')}")
    c.drawString(100, 620, "This certificate confirms the issuance of shares.")
    c.showPage()
    c.save()
    return filepath
