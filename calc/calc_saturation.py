from handlers import handle_Temperature, handle_Pressure, handle_Temperature_back, handle_Pressure_back
from CoolProp import CoolProp
from numpy import arange

def transformVary(vary, unit, start, end, range):
    if vary == "温度":
        s = handle_Temperature(start,unit)
        e = handle_Temperature(end,unit)
        r = handle_Temperature(start+range,unit) - handle_Temperature(start,unit)
    elif vary == "压力":
        s = handle_Pressure(start,unit)
        e = handle_Pressure(end,unit)
        r = handle_Temperature(start+range,unit) - handle_Temperature(start,unit)
    return s,e,r

def calc_saturation(working_fluid, type, vary, unit, start, end, range, units):
    s,e,r = transformVary(vary, unit, start, end, range)
    if type == "饱和气液":
        return calc_saturation_vapor_liquid(working_fluid, vary, s, e, r, units)
    # elif type == "熔化线":
    #     return calc_saturation_melting(working_fluid, vary, s, e, r)
    # elif type == "升华线":
    #     return calc_saturation_sublimation(working_fluid, vary, s, e, r)
    else:
        return None

def calc_saturation_vapor_liquid(working_fluid, vary, s, e, r, units):
    results = ["True"]
    if vary == "温度":
        for temperature in arange(s,e+r,r):
            result = [handle_Temperature_back(temperature,units[0])]

            try:            
                vapor_properties = CoolProp.PropsSI(['P', 'D', 'H', 'S'], 'T', temperature, 'Q', 1, working_fluid) # 计算饱和汽相的属性
                liquid_properties = CoolProp.PropsSI(['P', 'D', 'H', 'S'], 'T', temperature, 'Q', 0, working_fluid) # 计算饱和液相的属性

                result.append(handle_Pressure_back(liquid_properties[0],units[1])) # 液体压力，单位为MPa
                result.append(handle_Pressure_back(vapor_properties[0],units[1]))  # 蒸汽压力，单位为Pa
                result.append(liquid_properties[1]) # 液体密度，单位为kg/m^3
                result.append(vapor_properties[1]) # 蒸气密度，单位为kg/m^3
                result.append(liquid_properties[2]/1000)  # 液体焓，单位为kJ/kg
                result.append(vapor_properties[2]/1000)  # 蒸汽焓，单位为kJ/kg
                result.append(liquid_properties[3]/1000)  # 液体熵，单位为kJ/(kg*K)
                result.append(vapor_properties[3]/1000)  # 蒸汽熵，单位为kJ/(kg*K)
                results.append(result)
            except:
                results[0] = "False"

    elif vary == "压力":
        pass
    return results

