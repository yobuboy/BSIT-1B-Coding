import openpyxl as op

book = op.Workbook()
order = book.active

order ['A1'] = "Order ID"
order ['B1'] = "Customer Name"
order['C1'] = "Product"
order['D1'] = "Quantity"
order['E1'] = "Price"
order['F1'] = "Total"

book.save("Alba_Database.xlsx")