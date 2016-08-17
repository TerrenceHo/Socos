import numpy as np
import pandas as pd
import matplotlib.pylab as plt

def timefunc(interval_col):#translate time string to int
    h = []
    for hours in interval_col:
        if(hours == "0-1 hours"):
            h.append(0)
        elif(hours == "1-2 hours"):
            h.append(1)
        elif(hours == "2-3 hours"):
            h.append(2)
        elif(hours == "3-4 hours"):
            h.append(3)
        elif(hours == "4-5 hours"):
            h.append(4)
        elif(hours == "5-6 hours"):
            h.append(5)
        elif(hours == "6+ hours"):
            h.append(6)
        else:
            h.append(0)
    return h

def timefunc2(interval_col):
    h=[]
    for hours in interval_col:
        if hours == "0 hours":
            h.append(0)
        elif hours == "1 hour" or hours == "1 hours":
            h.append(1)
        elif hours == "2 hours":
            h.append(2)
        elif hours == "3 hours":
            h.append(3)
        elif hours == "4 hours":
            h.append(4)
        elif hours == "5 hours":
            h.append(5)
        elif hours == "6+ hours":
            h.append(6)
        else:
            h.append(0)
    return h

def childRankFunc(interval_col): #translates string(ex."not much like my child") to a number
    h = []
    for answer in interval_col:
        if answer == "Very much like my child":
            h.append(1)
        elif(answer == "Mostly like my child"):
            h.append(2)
        elif(answer == "Somewhat like my child"):
            h.append(3)
        elif(answer == "Not much like my child"):
            h.append(4)
        elif answer == "Not like my child":
            h.append(5)
        else:
            h.append(0)
    return h

def yesNoFunc(interval_col):
    h=[]
    for answer in interval_col:
        if answer == "No":
            h.append(1)
        elif answer == "Yes":
            h.append(2)
        else:
            h.append(0)
    return h

df = pd.read_csv("hopeLutheranChurchSurvey.csv")#read/load data

df["One-OneInt"]=timefunc2(df["On average, how much time per day do you spend with your child for one-on-one activities?"])
df["TimeSchoolworkInt"]=timefunc2(df["On average, how much time per day does your child spend on his/her schoolwork?"])
df["ElectronicTimeInt"]=timefunc2(df["On average, how much time per day does your child spend using electronics (such as television, computers, etc.)?"])
df["HardWorkerInt"]=childRankFunc(df["My child is a hard worker."])
df["HappyInt"]=childRankFunc(df["My child remains unaffected when someone close to him/her is happy."])
df["MoodsInt"]=childRankFunc(df["My child is “in tune” with other people’s moods."])
df["FocusInt"]=childRankFunc(df["My child has difficulty maintaining his/her focus on projects that take more than a few months to complete."])
df["ExcitementInt"]=childRankFunc(df["When someone else is feeling excited, my child tends to get excited too."])
df["SetbacksInt"]=childRankFunc(df["Setbacks don’t discourage my child. He/She does not give up easily."])
df["CompletionInt"]=childRankFunc(df["My child finishes whatever he/she begins."])
df["DodgingInt"]=childRankFunc(df["When a friend starts to talk about his/her problems, my child tries to steer the conversation towards something else."])
df["DistractedInt"]=childRankFunc(df["New ideas and projects sometimes distract my child from previous ones."])
df["InterestsInt"]=childRankFunc(df["My child's interests change from year to year."])
df["DifferentGoalsInt"]=childRankFunc(df["My child often sets a goal but later chooses to pursue a different one."])
df["ApatheticInt"]=childRankFunc(df["My child does not feel sympathy for people who cause their own serious illnesses."])
df["SetbacksInt"]=childRankFunc(df["My child has overcome setbacks to conquer an important challenge."])
df["EmpathyInt"]=childRankFunc(df["My child can tell when others are sad even when they do not say anything."])
df["DiligenceInt"]=childRankFunc(df["My child is diligent. He/She never gives up."])
df["LostFocusInt"]=childRankFunc(df["My child has been obsessed with a certain idea or project for a short time but later lost interest."])
df["KindnessInt"]=childRankFunc(df["My child enjoys making other people feel better."])
df["ConcernInt"]=childRankFunc(df["My child has tender, concerned feelings for people less fortunate than him/her."])
df["RespectInt"]=childRankFunc(df["It upsets my child to see someone being treated disrespectfully."])
df["MisfortunteInt"]=childRankFunc(df["Other people’s misfortunes do not disturb my child a great deal."])
print(df)





