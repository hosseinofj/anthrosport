import numpy as np
from math import log10

from .models import target,sport,medians


def fat_calcer(waist,neck,height,hip,gender):
    if gender == "M":
        r1 = (1.0324-(0.19077*log10(waist-neck))+(0.15456*log10(height)))
        res = (495/r1)-450
    else:
        r1 = (1.2975-(0.35004*log10(waist+hip-neck))+(0.22100*log10(height)))
        res = (495/r1)-450
    return res


def Param_calc(tr:target):
    age = tr.age
    if age > 18 : age = 18

    height_to_age = round(tr.height/age,3)
    one_hand_length_to_age = round(tr.one_hand_length/age,3)
    armspan= round(tr.armspan/tr.height,3)
    foot_length_to_age= round(tr.foot_length/tr.height,3)
    shoulder_size= round(tr.shoulder_size)
    fat= round(tr.fat,2)
    back_flexibility= round(tr.back_flexibility)
    shoulder_flexibility= round(tr.shoulder_flexibility)
    finger_ratio= round(tr.finger_ratio_2_4)

    anaerobic= round(tr.super_test_1)
    Lactic_anaerobic= round(tr.super_test_1-tr.super_test_2)
    Aerobic= round(tr.super_test_1-tr.super_test_3)

    dic = {"height_to_age" : height_to_age,
            "one_hand_length_to_age" : one_hand_length_to_age,
            "armspan" : armspan,
            "foot_length_to_age" : foot_length_to_age,
            "shoulder_size" : shoulder_size,
            "fat" : fat,
            "back_flexibility" : back_flexibility,
            "shoulder_flexibility" : shoulder_flexibility,
            "finger_ratio" : finger_ratio,
            "anaerobic" : anaerobic,
            "Lactic_anaerobic" : Lactic_anaerobic,
            "Aerobic" : Aerobic,

    }
    return dic


def score_calcer(sp:sport,sample:dict):
    res= 0 

    res = res + (sp.height_to_age * sample["height_to_age"])
    res = res + (sp.one_hand_length_to_age * sample["one_hand_length_to_age"])
    res = res + (sp.armspan * sample["armspan"])
    res = res + (sp.foot_length_to_age * sample["foot_length_to_age"])
    res = res + (sp.shoulder_size * sample["shoulder_size"])
    res = res + (sp.fat * sample["fat"])
    res = res + (sp.back_flexibility * sample["back_flexibility"])
    res = res + (sp.shoulder_flexibility * sample["shoulder_flexibility"])
    res = res + (sp.finger_ratio * sample["finger_ratio"])
    res = res + (sp.anaerobic * sample["anaerobic"])
    res = res + (sp.Lactic_anaerobic * sample["Lactic_anaerobic"])
    res = res + (sp.Aerobic * sample["Aerobic"])
    
    return res

def sport_predictor(params:dict):
    

    height_to_age_normalized =params["height_to_age"] -  medians.objects.get(name="height_to_age").value
    one_hand_length_to_age_normalized =params["one_hand_length_to_age"] -  medians.objects.get(name="one_hand_length_to_age").value
    armspan_normalized =params["armspan"] -  medians.objects.get(name="armspan").value
    foot_length_to_age_normalized =params["foot_length_to_age"] -  medians.objects.get(name="foot_length_to_age").value
    shoulder_size_normalized =params["shoulder_size"] -  medians.objects.get(name="shoulder_size").value
    fat_normalized =params["fat"] -  medians.objects.get(name="fat").value
    back_flexibility_normalized =params["back_flexibility"] -  medians.objects.get(name="back_flexibility").value
    shoulder_flexibility_normalized =params["shoulder_flexibility"] -  medians.objects.get(name="shoulder_flexibility").value
    finger_ratio_normalized =params["finger_ratio"] -  medians.objects.get(name="finger_ratio").value
    anaerobic_normalized =params["anaerobic"] -  medians.objects.get(name="anaerobic").value
    Lactic_anaerobic_normalized =params["Lactic_anaerobic"] -  medians.objects.get(name="Lactic_anaerobic").value
    Aerobic_normalized =params["Aerobic"] -  medians.objects.get(name="Aerobic").value


    normalized_dic = {"height_to_age" : height_to_age_normalized,
            "one_hand_length_to_age" : one_hand_length_to_age_normalized,
            "armspan" : armspan_normalized,
            "foot_length_to_age" : foot_length_to_age_normalized,
            "shoulder_size" : shoulder_size_normalized,
            "fat" : fat_normalized,
            "back_flexibility" : back_flexibility_normalized,
            "shoulder_flexibility" : shoulder_flexibility_normalized,
            "finger_ratio" : finger_ratio_normalized,
            "anaerobic" : anaerobic_normalized,
            "Lactic_anaerobic" : Lactic_anaerobic_normalized,
            "Aerobic" : Aerobic_normalized,

    }



    sportss = sport.objects.all()

    dtype = [('en_name', 'S20'), ('point', float)]
    sp_list = np.zeros(0,dtype=dtype)
    
    
    for sp in sportss:


        pnt=score_calcer(sp,normalized_dic)
        sp_arr =np.array([(sp.en_name,pnt)],dtype=sp_list.dtype)
        sp_list = np.append(sp_list,sp_arr)




    sp_list = np.sort(sp_list,order="point")



    return sp_list[-5:]



def medians_adding(params):
    meds = medians.objects.all()
    
    for m in meds:
        sum = m.value * m.count + params[m.name]
        m.count +=1
        m.value = sum/m.count
        m.save()

    return



def recalc_height_to_age_medians():

    
    trs = target.objects.all()


    height_to_age_med = medians.objects.get(name = "height_to_age")

    h_sum = 0
    h_cnt = 0
    for tr in trs:
        
        if tr.height and tr.age:
            h_sum += (tr.height/tr.age)
            h_cnt += 1 
        

    height_to_age_med.value = h_sum/h_cnt
    height_to_age_med.count = h_cnt
    height_to_age_med.save()


    return

def recalc_armspan_medians():

    
    trs = target.objects.all()


    armspan_med = medians.objects.get(name = "armspan")

    h_sum = 0
    h_cnt = 0
    for tr in trs:
        
        if tr.height and tr.armspan:
            h_sum += (tr.armspan/tr.height)
            h_cnt += 1 
        

    armspan_med.value = h_sum/h_cnt
    armspan_med.count = h_cnt
    armspan_med.save()


    return

def recalc_foot_length_to_age_medians():

    
    trs = target.objects.all()


    foot_length_to_age_med = medians.objects.get(name = "foot_length_to_age")

    h_sum = 0
    h_cnt = 0
    for tr in trs:
        
        if tr.foot_length and tr.age:
            h_sum += (tr.foot_length/tr.age)
            h_cnt += 1 
        

    foot_length_to_age_med.value = h_sum/h_cnt
    foot_length_to_age_med.count = h_cnt
    foot_length_to_age_med.save()


    return

def recalc_one_hand_length_to_age_medians():

    
    trs = target.objects.all()


    one_hand_length_to_age_med = medians.objects.get(name = "one_hand_length_to_age")

    h_sum = 0
    h_cnt = 0
    for tr in trs:
        
        if tr.one_hand_length and tr.age:
            h_sum += (tr.one_hand_length/tr.age)
            h_cnt += 1 
        

    one_hand_length_to_age_med.value = h_sum/h_cnt
    one_hand_length_to_age_med.count = h_cnt
    one_hand_length_to_age_med.save()


    return

def recalc_shoulder_size_medians():

    
    trs = target.objects.all()


    shoulder_size_med = medians.objects.get(name = "shoulder_size")

    h_sum = 0
    h_cnt = 0
    for tr in trs:
        
        if tr.shoulder_size :
            h_sum += (tr.shoulder_size)
            h_cnt += 1 
        

    shoulder_size_med.value = h_sum/h_cnt
    shoulder_size_med.count = h_cnt
    shoulder_size_med.save()


    return

def recalc_fat_medians():

    
    trs = target.objects.all()


    fat_med = medians.objects.get(name = "fat")

    h_sum = 0
    h_cnt = 0
    for tr in trs:
        
        if tr.fat :
            h_sum += (tr.fat)
            h_cnt += 1 
        

    fat_med.value = h_sum/h_cnt
    fat_med.count = h_cnt
    fat_med.save()


    return

def recalc_back_flexibility_medians():

    
    trs = target.objects.all()


    back_flexibility_med = medians.objects.get(name = "back_flexibility")

    h_sum = 0
    h_cnt = 0
    for tr in trs:
        
        if tr.back_flexibility :
            h_sum += (tr.back_flexibility)
            h_cnt += 1 
        

    back_flexibility_med.value = h_sum/h_cnt
    back_flexibility_med.count = h_cnt
    back_flexibility_med.save()


    return

def recalc_shoulder_flexibility_medians():

    
    trs = target.objects.all()


    shoulder_flexibility_med = medians.objects.get(name = "shoulder_flexibility")

    h_sum = 0
    h_cnt = 0
    for tr in trs:
        
        if tr.shoulder_flexibility:
            h_sum += (tr.shoulder_flexibility)
            h_cnt += 1 
        

    shoulder_flexibility_med.value = h_sum/h_cnt
    shoulder_flexibility_med.count = h_cnt
    shoulder_flexibility_med.save()


    return

def recalc_finger_ratio_medians():
    
    trs = target.objects.all()


    finger_ratio_med = medians.objects.get(name = "finger_ratio")

    h_sum = 0
    h_cnt = 0
    for tr in trs:
        
        if tr.finger_ratio_2_4:
            h_sum += (tr.finger_ratio_2_4)
            h_cnt += 1 
        
    if h_cnt == 0: return
    finger_ratio_med.value = h_sum/h_cnt
    finger_ratio_med.count = h_cnt
    finger_ratio_med.save()


    return












