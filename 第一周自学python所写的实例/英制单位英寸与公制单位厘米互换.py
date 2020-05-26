# 一英寸等于2.54厘米
value = float(input('请输入长度：'))
unit = input("请输入单位：")
if unit == '英寸' or unit == 'in':
    print("%f英寸 = %f厘米" % (value, value * 2.54))
elif unit == '厘米' or unit == 'cm':
    print("%f厘米 = %f英寸" % (value, value / 2.54))
else:
    print("请输入有效单位！！！")