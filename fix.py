from os import system
from time import sleep
import sys, datetime
import os,sys,time
import requests, json, time, threading, os, sys
from colorama import Fore, init
import itertools
import random
import socket
import shutil
import concurrent.futures

red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.WHITE
system("clear")

if 'linux' in sys.platform:
  r = "\033[91m" # Red
  g = "\033[92m" # Green
  y = "\033[93m" # Yellow
  p = "\033[94m" # Purple
  P = "\033[95m" # Pink
  c = "\033[96m" # Cyan
  w = "\033[97m" # White
  a = "\033[0m"  # Reset
else:
  # Convert String To Variabel Name
  for i in ['r','g','y','p','P','c','w','a']:
    globals()[i] = ""



colors = lambda : random.choice([r,g,y,p,P,c,w])

auth = input(f"\033[1;33;41m•\033[1;37[Input X-Authorization Code\033[1;33m•\033[0m\033[")


record = [{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SBY', 'routePassed': ['SBY', 'BKL'], 'activityRewards': None}, 'Value': 40},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'SBY'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'BKL'], 'activityRewards': None}, 'Value': 20},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SMG'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SBY'], 'activityRewards': None}, 'Value': 13},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'BKL'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'CBN'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SMG'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SBY'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'BKL', 'routePassed': ['BKL', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'JKT'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'CBN'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SMG'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'BKL'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'P_Merak'], 'activityRewards': None}, 'Value': 5}, {'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'JKT'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SMG'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SBY'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'BKL'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'P_Merak'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SMG'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PLB', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 55},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 11},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'JKT'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'BKL'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'PLB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'LPG'], 'activityRewards': None}, 'Value': 10},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'JMB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JMB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'PLB'], 'activityRewards': None}, 'Value': 12},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'LPG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'BKL'], 'activityRewards': None}, 'Value': 1},{"Key":{"sourceCity":"PBR","destinationCity":"BKT","routePassed":["BKT","PBR"],"activityRewards":None},"Value":50},{"Key":{"sourceCity":"PBR","destinationCity":"PDG","routePassed":["PDG","BKT","PBR"],"activityRewards":None},"Value":9},{"Key":{"sourceCity":"BKT","destinationCity":"PDG","routePassed":["PDG","BKT"],"activityRewards":None},"Value":50},]
headers = {'User-Agent': 'UnityEngine-Unity; Version: 2018.4.26f1','X-ReportErrorAsSuccess': 'true','X-PlayFabSDK': 'UnitySDK-2.20.170411','X-Authorization': '','Content-Type': 'application/json','Content-Length': '223','Host': '4ae9.playfabapi.com'}

def mxxxx():
        data = json.dumps({"PlayFabId":None,"InfoRequestParameters":{"GetUserAccountInfo":True,"GetUserInventory":True,"GetUserVirtualCurrency":True,"GetUserData":False,"UserDataKeys":None,"GetUserReadOnlyData":True,"UserReadOnlyDataKeys":None,"GetCharacterInventories":False,"GetCharacterList":False,"GetTitleData":True,"TitleDataKeys":None,"GetPlayerStatistics":False,"PlayerStatisticNames":None}})
        response = requests.post('https://4ae9.playfabapi.com/Client/GetPlayerCombinedInfo', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                chat = backend_data['InfoResultPayload']
                                uang= chat['UserVirtualCurrency']
                                money= uang['RP']

                                fff= chat['AccountInfo']
                                zzz= fff['TitleInfo']
                                www= zzz['TitlePlayerAccount']
                                saa= www['Id']

                                gcc= chat['AccountInfo']
                                id= gcc['TitleInfo']
                                you= id['DisplayName']
                                ketik(f"{red} {white} - Total_Money: {green}{money}   {white}                    ")
                                ketik(f"{red} {white} - Id_Kamu: {green}{saa}               {white}     ")
                                ketik(f"{red} ====================================================")

def create_mission():
        game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR","BKT","PDG"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        return None
                elif parser['code'] == 200:
                        data = parser['data']
                        if "apiError" in str(data):
                                return None
                        else:
                                carrer = data['FunctionResult']['careerSession']
                                return carrer
        else:
                return None

def skip_mission(token):
        data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                logs = backend_data['FunctionResult']


def pass_mission():
        carrer = create_mission()
        if carrer != None:
                token = carrer['token']
                skip_mission(token)
                mxxxx()

headers['X-Authorization'] = auth

def create_peta():
        game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR","BKT","PDG"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        return None
                elif parser['code'] == 200:
                        data = parser['data']
                        if "apiError" in str(data):
                                return None
                        else:
                                carrer = data['FunctionResult']['careerSession']
                                return carrer
        else:
                return None

def skip_mep(token):
        data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                logs = backend_data['FunctionResult']

def pass_sukses():
        carrer = create_peta()
        if carrer != None:
                token = carrer['token']
                skip_mep(token)


headers['X-Authorization'] = auth
	
def ketik(c):
    for e in c + "\n" :
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.005)
system("clear")
kal = datetime.datetime.now()

def ngopi():
    for i in range(jum):
             
             pass_sukses()
             pass_mission()

jum = int(input(f"{yellow}{green}[{red}◕ {yellow}◕ {red}◕{green}] {w}JUMLAH:{red} "))
ngopi()