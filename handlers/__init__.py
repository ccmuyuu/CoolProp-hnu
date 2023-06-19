
def handle_Temperature(value, unit):
    if unit == "K":
        return value
    elif unit == "°C":
        return value + 273.15
    elif unit == "°F":
        return (value + 459.67) * 5/9
    elif unit == "°R":
        return value * 5/9
    # elif unit == "T/Tc":
    #     return value * Tc  # 这里的 Tc 是您定义的临界温度常量
    else:
        return None  # 对于未知单位，返回 None 或者引发异常，具体根据需要自行处理
    
def handle_Pressure(value, unit):
    if unit == "Pa":
        return value
    elif unit == "kPa":
        return value * 1000
    elif unit == "MPa":
        return value * 1e6
    elif unit == "bar":
        return value * 1e5
    elif unit == "atm":
        return value * 101325
    elif unit == "mmHg":
        return value * 133.322
    elif unit == "inHg":
        return value * 3386.39
    elif unit == "psia":
        return value * 6894.76
    # elif unit == "p/pc":
    #     return value * pc
    # 添加其他单位的转换规则
    else:
        return None
    
def handle_Volume(value, unit):
    if unit == "m3":
        return value
    elif unit == "cm3":
        return value * 1e-6
    elif unit == "dm3":
        return value * 0.001
    elif unit == "L":
        return value * 0.001
    elif unit == "in3":
        return value * 1.63871e-5
    elif unit == "ft3":
        return value * 0.0283168
    elif unit == "gal":
        return value * 0.00378541
    # elif unit == "V/Vc":
    #     return value * Vc
    # 添加其他单位的转换规则
    else:
        return None
    
def handle_MassMole(value, unit):
    if unit == "g; mol":
        return value
    elif unit == "kg; kmol":
        return value * 1000
    elif unit == "lbm; lbmol":
        return value * 453.592
    # 添加其他单位的转换规则
    else:
        return None
    
def handle_Energy(value, unit):
    if unit == "J":
        return value
    elif unit == "kJ":
        return value * 1000
    elif unit == "cal":
        return value * 4.184
    elif unit == "kcal":
        return value * 4184
    elif unit == "Btu":
        return value * 1055.06
    elif unit == "/RTc":
        return value * 8314.4621
    # 添加其他单位的转换规则
    else:
        return None
    
def handle_Sound_Speed(value, unit):
    if unit == "m/s":
        return value
    elif unit == "cm/s":
        return value / 100
    elif unit == "in/s":
        return value * 0.0254
    elif unit == "ft/s":
        return value * 0.3048
    elif unit == "mph":
        return value * 0.44704
    # 添加其他单位的转换规则
    else:
        return None

def handle_Viscosity(value, unit):
    if unit == "Pa-s":
        return value
    elif unit == "mPa-s":
        return value / 1000
    elif unit == "μPa-s":
        return value / 1000000
    elif unit == "g/cm-s":
        return value * 1000
    elif unit == "Poise":
        return value * 0.1
    elif unit == "cPoise":
        return value * 0.001
    elif unit == "lbm/ft-s":
        return value * 1.48816394
    elif unit == "lbm/ft-h":
        return value * 4.133789e-4
    # 添加其他单位的转换规则
    else:
        return None
    
def handle_Thermal_Conductivity(value, unit):
    if unit == "W/m-K":
        return value
    elif unit == "mW/m-K":
        return value / 1000
    elif unit == "g-cm/s3-K":
        return value * 0.01
    elif unit == "cal/s-cm-K":
        return value * 418.4
    elif unit == "lbm-ft/s3-°F":
        return value * 1.730734e3
    elif unit == "lbf/s-°F":
        return value * 1.355818
    elif unit == "Btu/h-ft-°F":
        return value * 0.577789
    elif unit == "Btu-in/h-ft2-°F":
        return value * 4.882427
    # 添加其他单位的转换规则
    else:
        return None

def handle_Surface_Tension(value, unit):
    if unit == "N/m":
        return value
    elif unit == "mN/m":
        return value / 1000
    elif unit == "dyn/cm":
        return value / 10
    elif unit == "lbf/ft":
        return value * 47.88
    # 添加其他单位的转换规则
    else:
        return None
    
def handle_Temperature_back(value, unit):
    if unit == "K":
        return value
    elif unit == "°C":
        return value - 273.15
    elif unit == "°F":
        return value * 9/5 - 459.67
    elif unit == "°R":
        return value * 9/5
    # elif unit == "T/Tc":
    #     return value / Tc  # 这里的 Tc 是您定义的临界温度常量
    else:
        return None  # 对于未知单位，返回 None 或者引发异常，具体根据需要自行处理
    
def handle_Pressure_back(value, unit):
    if unit == "Pa":
        return value
    elif unit == "kPa":
        return value / 1000
    elif unit == "MPa":
        return value / 1e6
    elif unit == "bar":
        return value / 1e5
    elif unit == "atm":
        return value / 101325
    elif unit == "mmHg":
        return value / 133.322
    elif unit == "inHg":
        return value / 3386.39
    elif unit == "psia":
        return value / 6894.76
    # elif unit == "p/pc":
    #     return value / pc
    # 添加其他单位的转换规则
    else:
        return None