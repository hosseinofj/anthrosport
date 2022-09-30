import pandas as pd
from models import sport,medians

#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
# import sport Data indexies
#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
# Data = pd.read_excel("./sports_docs_formula/all.xlsx").set_index(['en_name'])


# for ind in Data.index: 
#     dt = Data.loc[ind]
#     print(ind)
#     sp = sport(en_name=ind,fa_name=dt['fa_name'],height_to_age = int(dt['height_to_age']),
#                 armspan = int(dt['armspan_to_height']),
#                 foot_length_to_age = int(dt['foot_lenght_to_age']),
#                 one_hand_length_to_age = int(dt['one_hand_to_age']),
#                 shoulder_size = int(dt['shoulder_size_to_age']),
#                 fat = int(dt['fat']),
#                 back_flexibility = int(dt['back_flexibility']),
#                 shoulder_flexibility = int(dt['shoulder_flexibility']),
#                 finger_ratio = int(dt['finger_4_2']),
#                 anaerobic = int(dt['anaerobic']),
#                 Lactic_anaerobic = int(dt['lactic anaerobic']),
#                 Aerobic = int(dt['aerobic']))
#     sp.save()


# print(Data)


#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
#*********************************************************************************


#********************************************************************************



def Add_targets():


    Data = pd.read_excel("./sports_docs_formula/PreData.xlsx").set_index(['Target'])
    Data = Data.replace({np.nan: None})

    for ind in Data.index:
        tar = Data.loc[ind]

        name = tar

        gender="F"
        if tar["gender"] == 1 : gender="M"

        age_list=[0,1,11,13,15,17,19]
        age = age_list[int(tar["age"])]
        
        height = tar["height/age"] * age

        hand = tar["hand/age"] * age
        foot = tar["foot/age"] * age
        shoulder = tar["shoulder"] 

        armspan = tar["armspan"] * height
        fat = tar["fat"]
        bac_flex = tar["back_flexibility"]
        sh_flex = tar["shoulder_flexibility"]
        tr = target(name=name,gender=gender,
                    age=age,height=height,
                    one_hand_length=hand,
                    foot_length=foot,
                    shoulder_size=shoulder,
                    armspan=armspan,fat=fat,
                    back_flexibility=bac_flex,
                    shoulder_flexibility=sh_flex)
        tr.save()

#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
#*********************************************************************************

