# report_generator.py
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas

def generate_report(client_data):
    # Generar gráficos con matplotlib
    plt.plot(client_data['cita'], client_data['peso'], label='Peso')
    plt.plot(client_data['cita'], client_data['medidas'], label='Medidas')
    plt.legend()
    plt.savefig('assets/progress_chart.png')
    
    # Crear PDF con reportlab
    c = canvas.Canvas("reports/diet_report.pdf")
    c.drawString(100, 750, "Reporte de Progreso de Dieta")
    c.drawImage("assets/progress_chart.png", 100, 450, width=400, height=300)
    c.showPage()c.save()