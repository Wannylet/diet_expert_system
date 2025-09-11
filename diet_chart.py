# report_generator.py
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
import pandas as pd

def generate_report(client_progress: pd.DataFrame) -> None:
    # Graficar usando todas las filas
    plt.figure(figsize=(8,5))
    plt.plot(client_progress['appointment'], client_progress['weight'], marker='o', label='Peso')
    plt.plot(client_progress['appointment'], client_progress['measurements'], marker='o', label='Medidas')
    plt.xlabel('Cita')
    plt.ylabel('Valor')
    plt.title('Progreso del Cliente')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('assets/progress_chart.png')
    plt.close()  # Cerrar la figura para no sobrecargar memoria

    # Crear PDF con reportlab
    c = canvas.Canvas("reports/diet_report.pdf")
    c.drawString(100, 750, "Reporte de Progreso de Dieta")
    c.drawImage("assets/progress_chart.png", 100, 450, width=400, height=300)
    c.showPage()
    c.save()
