#######################################################
# Name           : Brute Facebook (BF)                #
# File           : lainya.py                          #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############


import time, requests, sys, random, json, datetime, os, re
from bs4 import BeautifulSoup as par

from rich import print as prints
from rich.panel import Panel
from datetime import datetime

from src import cok as tt
from data.loy import Cek_Crack

#----- WARNA RICH ----
bir = '[bold cyan]'
hps  = '[/]'
A2 = "[#AAAAAA]" # Abu-Abu
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
# ---- WARNA PY   ----
M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
# ---- MODULE -----

class Xnxx:
    def __init__(self, cokz, tokz):
        self.id, self.uas = [], []
        self.data_ua, self.asd = {}, 0
        self.cokie = cokz
        self.token = tokz
        self.kontol()

    def jalan(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.03)

    def convert(self, uid):
        if "me" in uid:
            return {"uid":uid}
        elif(re.findall("\w+",uid)):
            r = requests.get(f"https://mbasic.facebook.com/{uid}?_rdr").text
            try:
                user = re.findall('\;rid\=(\d+)\&',str(r))[0]
            except:
                user = uid
        return {"uid":user}

    def kontol(self):
        prints(Panel(f"""[{bir}01{hps}] Check hasil crack
[{bir}02{hps}] Setting user agent
[{bir}03{hps}] Dump id dari id publik
[{bir}04{hps}] Dump id dari followers
[{bir}05{hps}] munculka user agent random
[{merah}00{hps}] Kembali""", title=f"{hijau}FITURE LAINYA{hps}"))
        pil = input(f"  [{M}?{N}] pilih: ")
        if pil in[""," "]:
            prints(Panel(f"[{merah}!{hps}] jangan kosong"));self.kontol()
        elif pil in["1","01"]:
            Cek_Crack()
        elif pil in["2", "02"]:
            self.seting_ua()
        elif pil in["3", "03"]:
            self.dump_flw()
        elif pil in["4", "04"]:
            self.dump_flw()
        elif pil in["5", "05"]:
            self.ua_random()
        elif pil in["0", "00"]:
            tt.Brute()
        else:
            prints(Panel(f"[{merah}!{hps}] input yang benar"));self.kontol()

    def seting_ua(self):
        prints(Panel(f"""[{bir}01{hps}] Gunakan user agent random
[{bir}02{hps}] Gunakan user agent hp sendiri
[{bir}03{hps}] Gunakan user agent bawaan scrpit
[{merah}00{hps}] Kembali """, title=f"{hijau}SETING USER AGENT{hps}"))
        pil = input(f"  [{M}?{N}] pilih: ")
        if pil in["1","01"]:
            try:os.remove("data/ua_ran.txt")
            except:pass
            a = requests.get("https://github.com/Cindy-Aulia/p/blob/main/data/ua.txt").text
            ua=open("data/ua_ran.txt", "w")
            xx=re.findall('line">(.*?)<', str(a))
            for x in xx:
                ua.write(xx+"\n")
            ua=open("data/ua_ran.txt", "r").read().splitlines()
            for i in ua:
                self.uas.append(i)
            prints(Panel("berhasil mengganti user agent"));input(f" [ {O}Kembali{N} ] ");tt.Brute()
        elif pil in["2", "02"]:
           try:os.remove("data/ua.txt")
           except:pass
           prints(Panel("jika ingin menggunakan user hp sendiri silahkan kunjungin situs web ini: [bold green]https://yayanxd.my.id/server[/] lalu klik ikon USER AGENT"))
           ua = input("  [*] masukan user agent: ")
           open("data/ua.txt", "w").write(ua)
           prints(Panel("berhasil mengganti user agent"));input(f" [ {O}Kembali{N} ] ");tt.Brute()
        elif pil in["3", "03"]:
            try:os.remove("data/ua.txt")
            except:pass
            ua = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"
            open("data/ua.txt", "w").write(ua)
            prints(Panel("berhasil mengganti user agent"));input(f" [ {O}Kembali{N} ] ");tt.Brute()
        elif pil in["0", "00"]:
            self.kontol()
        else:
            prints(Panel(f"[{merah}!{hps}] input yang benar"));self.seting_ua()

    def ua_random(self):
        try:os.remove("data/ua.txt")
        except:pass
        prints(Panel(f"""    SILAHKAN PILIH USER AGENT YANG MENURUT ANDA COCOK

[{bir}01{hps}] Samsung   [{bir}05{hps}] Vivo      [{bir}09{hps}] Huawei
[{bir}02{hps}] Nokia     [{bir}06{hps}] Iphone    [{bir}10{hps}] Windows
[{bir}03{hps}] Xiomi     [{bir}07{hps}] Asus      [{bir}11{hps}] Chrome
[{bir}04{hps}] Oppo      [{bir}08{hps}] lenovo    [{bir}12{hps}] Facebook""", title=f"{hijau}UA PILIHAN{hps}"))
        cxx = input(f"{N}└──> ")
        if cxx in["", " "]:
            prints(Panel(f"[{merah}!{hps}] jangan kosong"));self.ua_random()
        elif cxx in["1", "01"]:
            type = 'software_name/samsung-browser'
        elif cxx in["2", "02"]:
            type = 'software_name/nokia-browser'
        elif cxx in["3", "03"]:
            type = 'operating_platform_string/xiaomi-mi-a1'
        elif cxx in["4", "04"]:
            type = 'operating_platform_string/oppo-f1s-a1601'
        elif cxx in["5", "05"]:
            type = 'operating_platform_string/vivo'
        elif cxx in["6", "06"]:
            type = 'operating_platform_string/apple'
        elif cxx in["7", "07"]:
            type = 'operating_platform_string/asus'
        elif cxx in["8", "08"]:
            type = 'operating_platform_string/lenovo'
        elif cxx in["9", "09"]:
            type = 'operating_platform_string/huawei'
        elif cxx in["10"]:
            type = 'operating_system_name/windows'
        elif cxx in["11"]:
            type = 'operating_system_name/chrome-os'
        elif cxx in["12"]:
            type = 'software_name/facebook-app'
        else:
            prints(Panel(f"[{merah}!{hps}] input yang bener"));self.ua_random()
        prints(Panel("    Tekan CTRL terus tekan C untuk berhenti"))
        url = "https://developers.whatismybrowser.com/useragents/explore/"+ type
        with requests.Session() as xyz:
            req = xyz.get(url)
            pra = par(req.content,'html.parser')
            li = re.findall('<td><a class=\".*?\" href=\".*?\">(.*?)</a></td>',str(pra))
            for y in li:
                try:
                    x = f"{hijau}{y}{hps}"
                    self.asd += 1
                    pu = str(self.asd)
                    self.data_ua.update({pu:x.replace('[#AAAAAA]','')})
                    prints(Panel(x,title=f'[{bir}{pu}{hps}]',width=54,title_align='left',style='#FF8F00'))
                    time.sleep(2)
                except KeyboardInterrupt:
                    break
        ch = int(input(f"{N}   └──> "))
        open('data/ua.txt','w').write(self.data_ua[str(ch)])
        pilihan = open('data/ua.txt','r').read()
        prints(Panel(f'''{pilihan}''',title=f'[ {bir}User Agent{hps} ]',subtitle=f'[ {bir}Sukses Diganti{hps} ]',padding=(1,4),width=54,title_align='center',style='#FF8F00'))
        input(f" [ {O}Kembali{N} ] ");tt.Brute()

    def dump_flw(self):
        try:
            nanya_keun = int(input(f"  [{O}?{N}] mau berapa id yang di dump : "))
        except:nanya_keun=1
        nama = input(f"  [{O}?{N}] masukan nama file: ")
        cin = (nama+".json").replace(' ', '_')
        hsl = open(cin, "w")
        prints(Panel(f"[{bir}*{hps}] Ketik 'me' jika ingin dump id dari followers anda."))
        for mnh in range(nanya_keun):
            mnh +=1
            try:user = input(f"  [{O}*{N}] masukan id atau username {H}{mnh}{N} : "); uid = self.convert(user)
            except AttributeError:exit(f"\n  {N}[{M}x{N}] username atau id tidak benar")
            try:
                tol = requests.Session().get('https://graph.facebook.com/%s?fields=subscribers.limit(500000)&access_token=%s'%(uid.get("uid"),self.token),cookies=self.cokie)
                zzz = json.loads(tol.text)
                for x in zzz["subscribers"]["data"]:
                    self.id.append(x["id"]+"<=>"+x["name"]+"\n")
                    w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
                    sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(x['id'],N,datetime.now().strftime('%H:%M:%S'), len(id)
                    )); sys.stdout.flush()
                    time.sleep(0.0050)
                hsl.close()
                self.jalan('\n\n %s[%s✓%s] berhasil dump id dari teman'%(N,H,N))
                print(' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,cin,N))
                print("--------------------------------------------------------")
                input(f" [ {O}Kembali{N} ] ");tt.Brute()
            except KeyError:
                try:os.remove(cin)
                except:pass
                self.jalan('\n  %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
                input(f" [ {O}Kembali{N} ] ");tt.Brute()

    def dump_id(self):
        try:
            nanya_keun = int(input(f"  [{O}?{N}] mau berapa id yang di dump : "))
        except:nanya_keun=1
        nama = input(f"  [{O}?{N}] masukan nama file: ")
        cin = (nama+".json").replace(' ', '_')
        hsl = open(cin, "w")
        prints(Panel(f"[{bir}*{hps}] Ketik 'me' jika ingin dump id dari teman anda."))
        for mnh in range(nanya_keun):
            mnh +=1
            try:user = input(f"  [{O}*{N}] masukan id atau username {H}{mnh}{N} : "); uid = self.convert(user)
            except AttributeError:exit(f"\n  {N}[{M}x{N}] username atau id tidak benar")
            try:
                tol = requests.Session().get('https://graph.facebook.com/%s?fields=friends.limit(5000)&access_token=%s'%(uid.get("uid"),self.token),cookies=self.cokie)
                zzz = json.loads(tol.text)
                for x in zzz["friends"]["data"]:
                    self.id.append(x["id"]+"<=>"+x["name"]+"\n")
                    w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
                    sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(x['id'],N,datetime.now().strftime('%H:%M:%S'), len(id)
                    )); sys.stdout.flush()
                    time.sleep(0.0050)
                hsl.close()
                self.jalan('\n\n %s[%s✓%s] berhasil dump id dari teman'%(N,H,N))
                print(' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,cin,N))
                print("--------------------------------------------------------")
                input(f" [ {O}Kembali{N} ] ");tt.Brute()
            except KeyError:
                try:os.remove(cin)
                except:pass
                self.jalan('\n  %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
                input(f" [ {O}Kembali{N} ] ");tt.Brute()
