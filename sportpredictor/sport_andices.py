import pandas as pd


sample_data = {
    "name":"hossein Jafari",
    "age":28,
    "height":186,
    "one_hand":85,
    "foot_lenght":108,
    "shoulder_size":45,
    "armspan":210,
    }

sample_data3 = {
    "name":"sajjad asghari",
    "age":36,
    "height":175,
    "one_hand":76,
    "foot_lenght":85,
    "shoulder_size":46,
    "armspan":178,
    }
    
sample_data4 = {
    "name":"esmail salami",
    "age":25,
    "height":180,
    "one_hand":72,
    "foot_lenght":89,
    "shoulder_size":48,
    "armspan":182,
    }


    
sample_data5 = {
    "name":"sina atashbari",
    "age":23,
    "height":170,
    "one_hand":68,
    "foot_lenght":83,
    "shoulder_size":42,
    "armspan":170,
    }


def score_estimation(row):
    h = sample_data["height"]/sample_data["age"]
    o = sample_data["one_hand"]/sample_data["age"]
    f = sample_data["foot_lenght"]/sample_data["age"]
    s = sample_data["shoulder_size"]/sample_data["age"]
    a = sample_data["armspan"]/sample_data["height"]

    height_to_age = row['height_to_age']
    one_hand_to_age = row['one_hand_to_age']
    foot_lenght_to_age = row['foot_lenght_to_age']
    shoulder_size_to_age = row['shoulder_size_to_age']
    armspan_to_height = row['armspan_to_height']

    score = (height_to_age * h) + (one_hand_to_age * o) + (foot_lenght_to_age * f) + (shoulder_size_to_age * s) + (armspan_to_height * a)

    return score



Data = pd.read_excel("./sports_docs_formula/all.xlsx").set_index(['en_name', 'fa_name'])

#feature_name = Data.columns
# 'height_to_age', 'one_hand_to_age', 'foot_lenght_to_age', 'shoulder_size_to_age', 'armspan_to_height']

score = []

for ind in Data.index: 
    score.append(score_estimation(Data.loc[ind]))

print(score)

socre_df = pd.DataFrame(data = score, 
                        index = Data.index , 
                        columns = ['Score']).sort_values(by=['Score'] , ascending=False)


first_five = [x for x in socre_df.index[:5]]

print(socre_df.head(5))
