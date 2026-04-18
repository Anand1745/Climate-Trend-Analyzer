from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(kpis):
    doc = SimpleDocTemplate("outputs/reports/report.pdf")
    styles = getSampleStyleSheet()

    content = []

    for k,v in kpis.items():
        content.append(Paragraph(f"{k}: {v}", styles['Normal']))

    doc.build(content)