data1 = [1056, '412Perch','92Grounds','1000Sq. Mete', '1Grounds','3Cents','24Guntha','4125Perch', '34.46Sq.Yard', '1000Sq. Meter', '5.31Acres', '3600', '1141-1421', '4689-333', '550']

converted_data = []
for val in data:
    #print(val)
    if isinstance(val, str):
        #print(val,"hi",len(val),"iii",val[:-1])
        if '-' in val:
            x, y = val.split("-")
            avg = (float(x) + float(y)) / 2.0
            converted_data.append(avg)
        elif 'Perch' in val:
            converted_data.append(float(val[:-5]) * 272.25)
            #print(val[:-5],"hi",converted_data)
        elif 'Guntha' in val:
            converted_data.append(float(val[:-6]) * 1089)
        elif 'Sq. Yard' in val:
            converted_data.append(float(val[:-9]) * 9)
        elif 'Sq. Mete' in val:
            converted_data.append(float(val[:-9])* 10.76391)
        elif 'Sq. Meter' in val:
            converted_data.append(float(val[:-10]) * 10.76391)
        elif 'Grounds' in val:
            converted_data.append(float(val[:-7]) * 2400)
            #print(val[:-7],"hi",converted_data,"zi",val)
        elif 'Acres' in val:
            converted_data.append(float(val[:-5]) * 43560)
        elif 'Cents' in val:
            converted_data.append(float(val[:-5]) * 435.6)
        else:
            converted_data.append(float(val))
    else:
        converted_data.append(float(val))
        
print(len(converted_data))
