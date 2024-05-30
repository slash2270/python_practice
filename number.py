# 數字 number
print(f"加:{1 + 2} 減:{2 - 1} 乘:{1 * 2} 除:{1 / 2} 除取整:{1 // 2} 餘:{1 % 2} 次方:{2 ** 2}")
print(
    f"type(1):{type(1)} type(3/2):{type(3 / 2)} int(5.1):${int(5.1)} int(9/2):${int(9 / 2)} int('5'):{int('5')} int("
    f"'+2'):{int('+2')} int(True):{int(True)} int(False):{int(False)}")
print(
    f"int('101', 2):{int('101', 2)} int('101', 8):{int('101', 8)} int('101', 10):{int('101', 10)} "
    f"int('101', 16):{int('101', 16)}")
# 浮點數 float
print(f"1.0+5:{1.0 + 5} 1.0+True:{1.0+True} 1.0+False:{1.0 + False} float(5):{float(5)} float('5'):{float('5')}"
      f" float('5.1'):{float('5.1')} float(True):{float(True)} float(False):{float(False)}")
# 底數 radix, base
decimal = 11
binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)
print(f"0b1111二進制:{0b1111} 0o1111八進制:{0o1111} 0x1111十六進制:{0x1111} Decimal:{decimal} Binary:{binary} "
      f"Octal:{octal} Hexadecimal:{hexadecimal} Bin=>Dec:{int(binary, 2)} Oct=>Dec:{int(octal, 8)} "
      f"Hex=>Dec:{int(hexadecimal, 16)}")

