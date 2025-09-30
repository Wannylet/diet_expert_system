# report_generator.py
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
import pandas as pd
import random

def generate_report(client_progress: pd.DataFrame) -> None:
    num = random.randint(1, 1000)
    namePDF = f"diet_report_ {num} .pdf"
    namePNG = f"progress_chart_ {num} .png"

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
    plt.savefig('assets/' + namePNG)
    plt.close()  # Cerrar la figura para no sobrecargar memoria

    # Crear PDF con reportlab
    c = canvas.Canvas("reports/" + namePDF)
    c.drawString(100, 750, "Reporte de Progreso de Dieta")
    c.drawImage("assets/" + namePNG, 100, 450, width=400, height=300)
    c.showPage()
    c.save()
