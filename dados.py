import psycopg2
import csv
import tkinter as tk
from tkinter import ttk


conn = psycopg2.connect(
    host="144.22.211.147",
    port="5436",
    user="bear",
    password="dev!!!00",
    database="upbet"
)


pagamentos_afiliados = []
with open('./afiliados/affiliates.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pagamentos_afiliados.append(row)


cursor = conn.cursor()

resultados = []

for pagamento in pagamentos_afiliados:
    affiliate_id = pagamento['affiliate_id']
    query = f"""
SELECT customer_id, SUM(amount) AS total_bets
FROM bets
GROUP BY customer_id;
"""
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        customer_id, total_apostas = row
        resultados.append({
            'affiliate_id': affiliate_id,
            'customer_id': customer_id,
            'total_apostas': total_apostas,
            'payment': float(pagamento['payment'])
        })


for resultado in resultados:
    affiliate_id = resultado['affiliate_id']
    total_apostas = resultado['total_apostas']
    pagamento = resultado['payment']
    
   
    query = f"""
        SELECT porcent
        FROM limits
        WHERE amount <= {total_apostas}
        ORDER BY amount DESC
        LIMIT 1
    """
    cursor.execute(query)
    row = cursor.fetchone()
    if row:
        porcent = row[0]
    else:
      
        porcent = 50
    
    
    pagamento_final = (porcent / 100) * pagamento
    
 
    resultado['porcentagem'] = porcent
    resultado['pagamento_final'] = pagamento_final


conn.close()
cursor.close()


root = tk.Tk()
root.title("Relatório de Pagamentos de Afiliados")


columns = ('Afiliado ID', 'Cliente ID', 'Total de Apostas', 'Pagamento', 'Porcentagem', 'Pagamento Final')
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col,)
tree.pack(fill='both', expand=True)


for resultado in resultados:
    tree.insert('', 'end', values=(
        resultado['affiliate_id'],
        resultado['customer_id'],
        resultado['total_apostas'],
        resultado['payment'],
        f"{resultado['porcentagem']}%",
        resultado['pagamento_final']
    ))

root.mainloop()
