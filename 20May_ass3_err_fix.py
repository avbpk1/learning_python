# Fix error in code
def flexi_int(num_ch):
   if num_ch.isdigit():
      return int(num_ch)
   else:
      return int('0')
data = ["45,56,,89","89,66,88,75","81,68,80,75"]

for m in data:
   marks = map(flexi_int, m.split(","))
   print(sum(marks))
