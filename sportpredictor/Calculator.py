import numpy as np
from math import log10
from .models import target,sport,medians




class five_antro :
    height_to_age   =0 
    armspan         =0
    foot_to_age     =0
    one_hand_to_age =0
    shoulder_to_age =0
    
    height_level = 0
    arm_level=0
    foot_level=0
    hand_level =0
    shoulder_level=0

    def __init__(self,age,height,armspan,foot,hand,shoulder):
        if age> 18: age =18
        self.height_to_age=height/age
        self.armspan=armspan/height
        self.foot_to_age=foot/age
        self.one_hand_to_age=hand/age
        self.shoulder_to_age=shoulder/age

    def all_level_calcer(self):
        self.height_level_calcer()
        self.arm_level_calcer()
        self.foot_level_calcer()
        self.hand_level_calcer()
        self.shoulder_level_calcer()

    def mean_level(self):
        self.m_level = (sum([self.hand_level,
                                self.height_level,
                                self.foot_level,
                                self.arm_level,
                                self.shoulder_level])/5)
        return self.m_level

    def height_level_calcer(self):
        h_med = medians.objects.get(name="height_to_age")
        stages = (h_med.stage_1_min,h_med.stage_2_min,h_med.stage_3_min,h_med.stage_4_min,h_med.stage_5_min,h_med.stage_5_max)

        h= self.height_to_age
        if h<stages[1]:
            self.height_level =1
        elif h<stages[2]:
            self.height_level =2
        elif h<stages[3]:
            self.height_level =3
        elif h<stages[4]:
            self.height_level =4
        else:
            self.height_level =5
    
    def arm_level_calcer(self):
        h_med = medians.objects.get(name="armspan")
        stages = (h_med.stage_1_min,h_med.stage_2_min,h_med.stage_3_min,h_med.stage_4_min,h_med.stage_5_min,h_med.stage_5_max)

        h= self.armspan
        if h<stages[1]:
            self.arm_level =1
        elif h<stages[2]:
            self.arm_level =2
        elif h<stages[3]:
            self.arm_level =3
        elif h<stages[4]:
            self.arm_level =4
        else:
            self.arm_level =5

    def foot_level_calcer(self):
        h_med = medians.objects.get(name="foot_length_to_age")
        stages = (h_med.stage_1_min,h_med.stage_2_min,h_med.stage_3_min,h_med.stage_4_min,h_med.stage_5_min,h_med.stage_5_max)

        h= self.foot_to_age
        if h<stages[1]:
            self.foot_level =1
        elif h<stages[2]:
            self.foot_level =2
        elif h<stages[3]:
            self.foot_level =3
        elif h<stages[4]:
            self.foot_level =4
        else:
            self.foot_level =5

    def hand_level_calcer(self):
        h_med = medians.objects.get(name="one_hand_length_to_age")
        stages = (h_med.stage_1_min,h_med.stage_2_min,h_med.stage_3_min,h_med.stage_4_min,h_med.stage_5_min,h_med.stage_5_max)

        h= self.one_hand_to_age
        if h<stages[1]:
            self.hand_level =1
        elif h<stages[2]:
            self.hand_level =2
        elif h<stages[3]:
            self.hand_level =3
        elif h<stages[4]:
            self.hand_level =4
        else:
            self.hand_level =5

    def shoulder_level_calcer(self):
        h_med = medians.objects.get(name="shoulder_size")
        stages = (h_med.stage_1_min,h_med.stage_2_min,h_med.stage_3_min,h_med.stage_4_min,h_med.stage_5_min,h_med.stage_5_max)

        h= self.shoulder_to_age
        if h<stages[1]:
            self.shoulder_level =1
        elif h<stages[2]:
            self.shoulder_level =2
        elif h<stages[3]:
            self.shoulder_level =3
        elif h<stages[4]:
            self.shoulder_level =4
        else:
            self.shoulder_level =5


def P_cal(sp_lev,tr_lev):
    if tr_lev <sp_lev:
        return 0
    else:
        if sp_lev<3:
            return 0
        return sp_lev

def P_cal_W(sp_lev,tr_lev):
    if tr_lev <sp_lev:
        return 0
    else:
        return sp_lev

def score_calcer(sp:sport,antr:five_antro):
    point = 0
    total = sp.height_to_age +\
            sp.armspan +\
            sp.foot_length_to_age +\
            sp.one_hand_length_to_age +\
            sp.shoulder_size
    
    if antr.mean_level() >=3:
        point += P_cal(sp.height_to_age,antr.height_level) +\
                    P_cal(sp.armspan,antr.arm_level) +\
                    P_cal(sp.foot_length_to_age,antr.foot_level) +\
                    P_cal(sp.one_hand_length_to_age,antr.hand_level) +\
                    P_cal(sp.shoulder_size,antr.shoulder_level)
    else:
        point += P_cal_W(sp.height_to_age,antr.height_level) +\
                    P_cal_W(sp.armspan,antr.arm_level) +\
                    P_cal_W(sp.foot_length_to_age,antr.foot_level) +\
                    P_cal_W(sp.one_hand_length_to_age,antr.hand_level) +\
                    P_cal_W(sp.shoulder_size,antr.shoulder_level)
    return (point/total)*100




def antro_sport_selector(tr:target):

    antros = five_antro(height=tr.height,
                        age=tr.age,
                        foot=tr.foot_length,
                        hand=tr.one_hand_length,
                        shoulder=tr.shoulder_size,
                        armspan=tr.armspan)

    antros.all_level_calcer()

    log =   "height_level --> " + str(antros.height_level) + "<br>" +\
            "armspan_level --> " + str(antros.arm_level) + "<br>" +\
            "foot_level --> " + str(antros.foot_level) + "<br>" +\
            "hand_level --> " + str(antros.hand_level) + "<br>" +\
            "shoulder_level --> " + str(antros.shoulder_level) + "<br><br>"

    # point_for_every_sport    
    sportss = sport.objects.all()

    dtype = [('en_name', '<U50'), ('point', float)]
    antro_sp_list = np.zeros(0,dtype=dtype)
   
        
    for sp in sportss:
        pnt=score_calcer(sp,antros)
        en_name = sp.en_name
        sp_arr =np.array((en_name,pnt),dtype=antro_sp_list.dtype)
        antro_sp_list = np.append(antro_sp_list,sp_arr)
   
    antro_sp_list_sorted = np.sort(antro_sp_list,order="point")

    log += "<br>" + "<h2>top Sports</h2>" +\
            str(antro_sp_list_sorted[-1]) + "<br>" +\
            str(antro_sp_list_sorted[-2]) + "<br>" +\
            str(antro_sp_list_sorted[-3]) + "<br>" +\
            str(antro_sp_list_sorted[-4]) + "<br>" +\
            str(antro_sp_list_sorted[-5]) + "<br>" 
    
    return antro_sp_list_sorted,log




def fat_calcer(waist,neck,height,hip,gender):
    if gender == "M":
        r1 = (1.0324-(0.19077*log10(waist-neck))+(0.15456*log10(height)))
        res = (495/r1)-450
    elif gender == "F":
        r1 = (1.2975-(0.35004*log10(waist+hip-neck))+(0.22100*log10(height)))
        res = (495/r1)-450
    else:
        res = 0
    return round(res,2)

def recalc_height_to_age_medians():   
    trs = target.objects.all()

    height_to_age_med = medians.objects.get(name = "height_to_age")

    data = []
    for tr in trs:        
        if tr.height and tr.age:
            data.append((tr.height/tr.age))
        
    
    arr = np.array(data)

    d_min =  np.amin(arr)
    d_max =  np.amax(arr)
    mean = np.mean(arr)
    std_deviation = np.std(arr)

    step_1 = (np.amin(arr),mean-(3*std_deviation/2))
    step_2 = (mean-(3*std_deviation/2),mean-(std_deviation/2))
    step_3 = (mean-(std_deviation/2),mean+(std_deviation/2))
    step_4 = (mean+(std_deviation/2),mean+(3*std_deviation/2))
    step_5 = (mean+(3*std_deviation/2),np.amax(arr))



    log = "Height To Age median is <br><br>"
    log +=  "count----->" + str(arr.size)          + " <br> " + \
            "average--->" + str(mean)    + " <br> " + \
            "max------->" + str(d_max)      + " <br> " + \
            "min------->" + str(d_min)      + " <br> " + \
            "deviation->" + str(std_deviation)    + " <br> " + \
            "step_1---->" + str(step_1)         + " <br> " + \
            "step_2---->" + str(step_2)         + " <br> " + \
            "step_3---->" + str(step_3)         + " <br> " + \
            "step_4---->" + str(step_4)         + " <br> " + \
            "step_5---->" + str(step_5)         + " <br> " 


    height_to_age_med.min =  d_min
    height_to_age_med.max =   d_max
    height_to_age_med.Average_value =  mean
    height_to_age_med.count = arr.size 
    height_to_age_med.stage_1_min= step_1[0]
    height_to_age_med.stage_1_max= step_1[1]
    height_to_age_med.stage_2_min= step_2[0]
    height_to_age_med.stage_2_max= step_2[1]
    height_to_age_med.stage_3_min= step_3[0]
    height_to_age_med.stage_3_max= step_3[1]
    height_to_age_med.stage_4_min= step_4[0]
    height_to_age_med.stage_4_max= step_4[1]
    height_to_age_med.stage_5_min= step_5[0]
    height_to_age_med.stage_5_max= step_5[1]

    height_to_age_med.save()

    return log

def recalc_armspan_medians():
    trs = target.objects.all()

    armspan = medians.objects.get(name = "armspan")

    data = []
    for tr in trs:        
        if tr.height and tr.armspan:
            data.append((tr.armspan/tr.height))
        
    
    arr = np.array(data)

    d_min =  np.amin(arr)
    d_max =  np.amax(arr)
    mean = np.mean(arr)
    std_deviation = np.std(arr)

    step_1 = (np.amin(arr),mean-(3*std_deviation/2))
    step_2 = (mean-(3*std_deviation/2),mean-(std_deviation/2))
    step_3 = (mean-(std_deviation/2),mean+(std_deviation/2))
    step_4 = (mean+(std_deviation/2),mean+(3*std_deviation/2))
    step_5 = (mean+(3*std_deviation/2),np.amax(arr))



    log = "armspan median is <br><br>"
    log +=  "count----->" + str(arr.size)          + " <br> " + \
            "average--->" + str(mean)     + " <br> " + \
            "max------->" + str(d_max)      + " <br> " + \
            "min------->" + str(d_min)      + " <br> " + \
            "deviation->" + str(std_deviation)    + " <br> " + \
            "step_1---->" + str(step_1)         + " <br> " + \
            "step_2---->" + str(step_2)         + " <br> " + \
            "step_3---->" + str(step_3)         + " <br> " + \
            "step_4---->" + str(step_4)         + " <br> " + \
            "step_5---->" + str(step_5)         + " <br> " 


    armspan.min =  d_min
    armspan.max =   d_max
    armspan.Average_value =  mean
    armspan.count = arr.size 
    armspan.stage_1_min= step_1[0]
    armspan.stage_1_max= step_1[1]
    armspan.stage_2_min= step_2[0]
    armspan.stage_2_max= step_2[1]
    armspan.stage_3_min= step_3[0]
    armspan.stage_3_max= step_3[1]
    armspan.stage_4_min= step_4[0]
    armspan.stage_4_max= step_4[1]
    armspan.stage_5_min= step_5[0]
    armspan.stage_5_max= step_5[1]

    armspan.save()

    return log

def recalc_foot_length_to_age_medians():  
    trs = target.objects.all()
    med = medians.objects.get(name = "foot_length_to_age")

    data = []
    for tr in trs:        
        if tr.foot_length and tr.age:
            data.append((tr.foot_length/tr.age))
        
    
    arr = np.array(data)

    d_min =  np.amin(arr)
    d_max =  np.amax(arr)
    mean = np.mean(arr)
    std_deviation = np.std(arr)

    step_1 = (np.amin(arr),mean-(3*std_deviation/2))
    step_2 = (mean-(3*std_deviation/2),mean-(std_deviation/2))
    step_3 = (mean-(std_deviation/2),mean+(std_deviation/2))
    step_4 = (mean+(std_deviation/2),mean+(3*std_deviation/2))
    step_5 = (mean+(3*std_deviation/2),np.amax(arr))



    log = "foot_length_to_age median is <br><br>"
    log +=  "count----->" + str(arr.size)          + " <br> " + \
            "average--->" + str(mean)     + " <br> " + \
            "max------->" + str(d_max)      + " <br> " + \
            "min------->" + str(d_min)      + " <br> " + \
            "deviation->" + str(std_deviation)    + " <br> " + \
            "step_1---->" + str(step_1)         + " <br> " + \
            "step_2---->" + str(step_2)         + " <br> " + \
            "step_3---->" + str(step_3)         + " <br> " + \
            "step_4---->" + str(step_4)         + " <br> " + \
            "step_5---->" + str(step_5)         + " <br> " 


    med.min =  d_min
    med.max =   d_max
    med.Average_value =  mean
    med.count = arr.size 
    med.stage_1_min= step_1[0]
    med.stage_1_max= step_1[1]
    med.stage_2_min= step_2[0]
    med.stage_2_max= step_2[1]
    med.stage_3_min= step_3[0]
    med.stage_3_max= step_3[1]
    med.stage_4_min= step_4[0]
    med.stage_4_max= step_4[1]
    med.stage_5_min= step_5[0]
    med.stage_5_max= step_5[1]

    med.save()

    return log

def recalc_one_hand_length_to_age_medians():
    trs = target.objects.all()
    med = medians.objects.get(name = "one_hand_length_to_age")

    data = []
    for tr in trs:        
        if tr.one_hand_length and tr.age:
            data.append((tr.one_hand_length/tr.age))
        
    
    arr = np.array(data)

    d_min =  np.amin(arr)
    d_max =  np.amax(arr)
    mean = np.mean(arr)
    std_deviation = np.std(arr)

    step_1 = (np.amin(arr),mean-(3*std_deviation/2))
    step_2 = (mean-(3*std_deviation/2),mean-(std_deviation/2))
    step_3 = (mean-(std_deviation/2),mean+(std_deviation/2))
    step_4 = (mean+(std_deviation/2),mean+(3*std_deviation/2))
    step_5 = (mean+(3*std_deviation/2),np.amax(arr))



    log = "one_hand_length_to_age median is <br><br>"
    log +=  "count----->" + str(arr.size)          + " <br> " + \
            "average--->" + str(mean)     + " <br> " + \
            "max------->" + str(d_max)      + " <br> " + \
            "min------->" + str(d_min)      + " <br> " + \
            "deviation->" + str(std_deviation)    + " <br> " + \
            "step_1---->" + str(step_1)         + " <br> " + \
            "step_2---->" + str(step_2)         + " <br> " + \
            "step_3---->" + str(step_3)         + " <br> " + \
            "step_4---->" + str(step_4)         + " <br> " + \
            "step_5---->" + str(step_5)         + " <br> " 


    med.min =  d_min
    med.max =   d_max
    med.Average_value =  mean
    med.count = arr.size 
    med.stage_1_min= step_1[0]
    med.stage_1_max= step_1[1]
    med.stage_2_min= step_2[0]
    med.stage_2_max= step_2[1]
    med.stage_3_min= step_3[0]
    med.stage_3_max= step_3[1]
    med.stage_4_min= step_4[0]
    med.stage_4_max= step_4[1]
    med.stage_5_min= step_5[0]
    med.stage_5_max= step_5[1]

    med.save()
    return log

def recalc_shoulder_size_medians():
    trs = target.objects.all()
    med = medians.objects.get(name = "shoulder_size")
    
    data = []
    for tr in trs:        
        if tr.shoulder_size and tr.age:
            data.append((tr.shoulder_size/tr.age))
        
    
    arr = np.array(data)

    d_min =  np.amin(arr)
    d_max =  np.amax(arr)
    mean = np.mean(arr)
    std_deviation = np.std(arr)

    step_1 = (np.amin(arr),mean-(3*std_deviation/2))
    step_2 = (mean-(3*std_deviation/2),mean-(std_deviation/2))
    step_3 = (mean-(std_deviation/2),mean+(std_deviation/2))
    step_4 = (mean+(std_deviation/2),mean+(3*std_deviation/2))
    step_5 = (mean+(3*std_deviation/2),np.amax(arr))



    log = "shoulder_size median is <br><br>"
    log +=  "count----->" + str(arr.size)          + " <br> " + \
            "average--->" + str(mean)     + " <br> " + \
            "max------->" + str(d_max)      + " <br> " + \
            "min------->" + str(d_min)      + " <br> " + \
            "deviation->" + str(std_deviation)    + " <br> " + \
            "step_1---->" + str(step_1)         + " <br> " + \
            "step_2---->" + str(step_2)         + " <br> " + \
            "step_3---->" + str(step_3)         + " <br> " + \
            "step_4---->" + str(step_4)         + " <br> " + \
            "step_5---->" + str(step_5)         + " <br> " 


    med.min =  d_min
    med.max =   d_max
    med.Average_value =  mean
    med.count = arr.size 
    med.stage_1_min= step_1[0]
    med.stage_1_max= step_1[1]
    med.stage_2_min= step_2[0]
    med.stage_2_max= step_2[1]
    med.stage_3_min= step_3[0]
    med.stage_3_max= step_3[1]
    med.stage_4_min= step_4[0]
    med.stage_4_max= step_4[1]
    med.stage_5_min= step_5[0]
    med.stage_5_max= step_5[1]

    med.save()
    return log




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
        
        if tr.finger_4:
            h_sum += (tr.finger_2/tr.finger_4)
            h_cnt += 1 
        
    if h_cnt == 0: return
    finger_ratio_med.value = h_sum/h_cnt
    finger_ratio_med.count = h_cnt
    finger_ratio_med.save()


    return



def recalc_aeros_medians():
    
    trs = target.objects.all()


    Aerobic_med = medians.objects.get(name = "Aerobic")
    Lactic_anaerobic_med = medians.objects.get(name = "Lactic_anaerobic")
    anaerobic_med = medians.objects.get(name = "anaerobic")

    h_sum = 0
    h_cnt = 0
    for tr in trs:
        
        if tr.finger_4:
            h_sum += (tr.super_test_3)
            h_cnt += 1 
        
    if h_cnt == 0: return
    Aerobic_med.value = h_sum/h_cnt
    Aerobic_med.count = h_cnt
    Aerobic_med.save()

    h_sum = 0
    h_cnt = 0
    for tr in trs:
        
        if tr.finger_4:
            h_sum += (tr.super_test_2)
            h_cnt += 1 
        
    if h_cnt == 0: return
    Lactic_anaerobic_med.value = h_sum/h_cnt
    Lactic_anaerobic_med.count = h_cnt
    Lactic_anaerobic_med.save()


    h_sum = 0
    h_cnt = 0
    for tr in trs:
        
        if tr.finger_4:
            h_sum += (tr.super_test_1)
            h_cnt += 1 
        
    if h_cnt == 0: return
    anaerobic_med.value = h_sum/h_cnt
    anaerobic_med.count = h_cnt
    anaerobic_med.save()

    return








# def Param_calc(tr:target):
#     age = tr.age
#     if age > 18 : age = 18

#     height_to_age =             round(tr.height/age,3)
#     one_hand_length_to_age =    round(tr.one_hand_length/age,3)
#     armspan=                    round(tr.armspan/tr.height,3)
#     foot_length_to_age=         round(tr.foot_length/tr.age,3)
#     shoulder_size=              round(tr.shoulder_size,2)
#     fat=                        round(tr.fat,2)
#     if not tr.back_flexibility:
#         back_flexibility =      0
#     else:
#         back_flexibility=       round(tr.back_flexibility)
#     if tr.shoulder_flexibility:
#         shoulder_flexibility=   round(tr.shoulder_flexibility)
#     else:
#         shoulder_flexibility=   0
    
#     if not tr.finger_4:
#         finger_ratio=           0
#     else:
#         finger_ratio=           round(tr.finger_2/tr.finger_4)
#     try:
#         anaerobic=              round(tr.super_test_1)
#         Lactic_anaerobic=       round(tr.super_test_2)
#         Aerobic=                round(tr.super_test_3)
#     except:
#         anaerobic =             0
#         Lactic_anaerobic =      0
#         Aerobic =               0


#     dic = {"height_to_age" : height_to_age,
#             "one_hand_length_to_age" : one_hand_length_to_age,
#             "armspan" : armspan,
#             "foot_length_to_age" : foot_length_to_age,
#             "shoulder_size" : shoulder_size,
#             "fat" : fat,
#             "back_flexibility" : back_flexibility,
#             "shoulder_flexibility" : shoulder_flexibility,
#             "finger_ratio" : finger_ratio,
#             "anaerobic" : anaerobic,
#             "Lactic_anaerobic" : Lactic_anaerobic,
#             "Aerobic" : Aerobic,

#     }
#     return dic





# def medians_adding(params):
#     meds = medians.objects.all()
    
#     for m in meds:
#         sum = m.value * m.count + params[m.name]
#         m.count +=1
#         m.value = sum/m.count
#         m.save()

#     return
