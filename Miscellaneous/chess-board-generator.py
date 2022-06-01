a= "<td class=\"white\"></td>"
b = "<td class=\"black\"></td>"


row = []
for i in range(5):
    if i % 2 == 0:
        row.append(a)
    else:
        row.append(b)


row2= []
for i in range(5):
    if i % 2 == 0:
        row2.append(b)
    else:
        row2.append(a)

original_row = "".join(row)
original_row2 = "".join(row2)


for i in range(5):
    if i % 2 == 0:
        print(f"<tr>{original_row}</tr>")
    else:
        print(f"<tr>{original_row2}</tr>")