import time
import random
import string
import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from selenium_stealth import stealth

# ==================== [1. 全域配置區 (之後接上資料庫)] ====================
USER_DATA_LIST = [
    {"first": "Wei", "last": "Chen", "pwd": "StrongPassword@991"}
]

SMS_API_KEY = "你的_API_KEY"
SMS_COUNTRY_ID = "6"
# ========================================================

class GoogleRegistrar:
    def __init__(self, user_info):
        self.user = user_info
        self.session_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.driver = self._init_driver()
        self.wait = WebDriverWait(self.driver, 20)

    def _init_driver(self):
        options = uc.ChromeOptions()
        options.add_argument('--lang=zh-TW')
        options.add_argument('--disable-webrtc')
        
        # 鎖定 144 版本
        driver = uc.Chrome(options=options, version_main=144)

        stealth(driver,
                languages=["zh-TW", "zh"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True)
        return driver

    def type_like_human(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.1, 0.2))

    def solve_dropdown_actionchains(self, select_id, presses):
        print(f"[*] 啟動 ActionChains 物理按鍵破解: {select_id} ...")
        try:
            # 1. 找到下拉選單的「父容器」(畫面上真正看得到的那個外框)
            parent_el = self.driver.find_element(By.XPATH, f"//*[@id='{select_id}']/..")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", parent_el)
            time.sleep(0.5)

            # 2. 點擊外框，讓選單彈出並獲取焦點
            try:
                parent_el.click()
            except:
                self.driver.execute_script("arguments[0].click();", parent_el)
            time.sleep(1) # 必須等待動畫展開

            # 3. 呼叫動作鏈發送實體按鍵
            actions = ActionChains(self.driver)
            
            # 暴力狂按「上」鍵 12 次，確保選項回到最頂端 (把預設值洗掉)
            for _ in range(12):
                actions.send_keys(Keys.ARROW_UP)
            actions.pause(0.2)

            # 往下按指定的次數
            for _ in range(presses):
                actions.send_keys(Keys.ARROW_DOWN)
                actions.pause(0.1)

            # 確定選擇
            actions.send_keys(Keys.ENTER)
            actions.perform() # 執行以上所有組合動作
            time.sleep(0.5)

        except Exception as e:
            print(f"[!] ActionChains 操作失敗: {e}")

    def handle_sms_logic(self):
        try:
            print("[*] 啟動簡訊接碼平台...")
            url = f"https://api.sms-activate.org/stora/v1/res/api.php?api_key={SMS_API_KEY}&action=getNumber&service=go&country={SMS_COUNTRY_ID}"
            res = requests.get(url).text
            if "ACCESS_NUMBER" in res:
                p_id = res.split(":")[1]
                p_num = res.split(":")[2]
                print(f"[*] 租借成功: {p_num}")

                p_input = self.wait.until(EC.presence_of_element_located((By.ID, 'phoneNumberId')))
                self.type_like_human(p_input, p_num)
                self.driver.find_element(By.XPATH, '//span[text()="下一步"]').click()

                for _ in range(20):
                    time.sleep(6)
                    status_url = f"https://api.sms-activate.org/stora/v1/res/api.php?api_key={SMS_API_KEY}&action=getStatus&id={p_id}"
                    s_res = requests.get(status_url).text
                    if "STATUS_OK" in s_res:
                        code = s_res.split(":")[1]
                        print(f"[*] 簡訊已抵達: {code}")
                        self.type_like_human(self.wait.until(EC.presence_of_element_located((By.ID, 'code'))), code)
                        self.driver.find_element(By.XPATH, '//span[text()="下一步"]').click()
                        return True
            return False
        except Exception as e:
            print(f"簡訊流程失敗: {e}")
            return False

    import time
import random
import string
import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains # 🌟 終極武器匯入
from selenium_stealth import stealth

# ==================== [ 全域配置區 (之後接上資料庫)] ====================
USER_DATA_LIST = [
    {"first": "Wei", "last": "Chen", "pwd": "StrongPassword@991"}
]

SMS_API_KEY = "你的_API_KEY"
SMS_COUNTRY_ID = "6"
# ========================================================

class GoogleRegistrar:
    def __init__(self, user_info):
        self.user = user_info
        self.session_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.driver = self._init_driver()
        self.wait = WebDriverWait(self.driver, 20)

    def _init_driver(self):
        options = uc.ChromeOptions()
        options.add_argument('--lang=zh-TW')
        options.add_argument('--disable-webrtc')
        
        # 鎖定 144 版本
        driver = uc.Chrome(options=options, version_main=144)

        stealth(driver,
                languages=["zh-TW", "zh"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True)
        return driver

    def type_like_human(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.1, 0.2))

    def solve_dropdown_actionchains(self, select_id, presses):
        print(f"[*] 啟動 ActionChains 物理按鍵破解: {select_id} ...")
        try:
            # 1. 找到下拉選單
            parent_el = self.driver.find_element(By.XPATH, f"//*[@id='{select_id}']/..")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", parent_el)
            time.sleep(0.5)

            # 2. 點擊外框，讓選單彈出並獲取焦點
            try:
                parent_el.click()
            except:
                self.driver.execute_script("arguments[0].click();", parent_el)
            time.sleep(1) # 必須等待動畫展開

            # 3. 呼叫動作鏈發送實體按鍵
            actions = ActionChains(self.driver)
            
            # 暴力狂按「上」鍵 12 次，確保選項回到最頂端 (把預設值洗掉)
            for _ in range(12):
                actions.send_keys(Keys.ARROW_UP)
            actions.pause(0.2)

            # 往下按指定的次數
            for _ in range(presses):
                actions.send_keys(Keys.ARROW_DOWN)
                actions.pause(0.1)

            # 確定選擇
            actions.send_keys(Keys.ENTER)
            actions.perform() # 執行以上所有組合動作
            time.sleep(0.5)

        except Exception as e:
            print(f"[!] ActionChains 操作失敗: {e}")

    def handle_sms_logic(self):
        try:
            print("[*] 啟動簡訊接碼平台...")
            url = f"https://api.sms-activate.org/stora/v1/res/api.php?api_key={SMS_API_KEY}&action=getNumber&service=go&country={SMS_COUNTRY_ID}"
            res = requests.get(url).text
            if "ACCESS_NUMBER" in res:
                p_id = res.split(":")[1]
                p_num = res.split(":")[2]
                print(f"[*] 租借成功: {p_num}")

                p_input = self.wait.until(EC.presence_of_element_located((By.ID, 'phoneNumberId')))
                self.type_like_human(p_input, p_num)
                self.driver.find_element(By.XPATH, '//span[text()="下一步"]').click()

                for _ in range(20):
                    time.sleep(6)
                    status_url = f"https://api.sms-activate.org/stora/v1/res/api.php?api_key={SMS_API_KEY}&action=getStatus&id={p_id}"
                    s_res = requests.get(status_url).text
                    if "STATUS_OK" in s_res:
                        code = s_res.split(":")[1]
                        print(f"[*] 簡訊已抵達: {code}")
                        self.type_like_human(self.wait.until(EC.presence_of_element_located((By.ID, 'code'))), code)
                        self.driver.find_element(By.XPATH, '//span[text()="下一步"]').click()
                        return True
            return False
        except Exception as e:
            print(f"簡訊流程失敗: {e}")
            return False

    def run(self):
        try:
            print(f"\n>>> 任務開始: {self.user['first']}")
            self.driver.get('https://accounts.google.com/signup')

            # 1. 姓名頁
            first_input = self.wait.until(EC.element_to_be_clickable((By.NAME, 'firstName')))
            first_input.click()
            self.type_like_human(first_input, self.user['first'])
            self.type_like_human(self.driver.find_element(By.NAME, 'lastName'), self.user['last'])
            self.driver.find_element(By.XPATH, '//span[text()="下一步"] | //span[text()="Next"]').click()

            # 2. 基本資料頁 
            year_el = self.wait.until(EC.element_to_be_clickable((By.ID, 'year')))
            year_el.click()
            self.type_like_human(year_el, str(random.randint(1996, 2004)))
            
            # 月份
            self.solve_dropdown_actionchains('month', random.randint(1, 12))
            
            day_el = self.driver.find_element(By.ID, 'day')
            day_el.click()
            self.type_like_human(day_el, str(random.randint(1, 28)))
            
            # 性別 
            self.solve_dropdown_actionchains('gender', random.randint(1, 2))
            
            self.driver.find_element(By.XPATH, '//span[text()="下一步"] | //span[text()="Next"]').click()

            # 3. 使用者名稱頁
            print("[*] 正在處理使用者名稱設定...")
            time.sleep(3)
            
            # 如果出現「建立自定義地址」選項，先點擊它
            try: 
                self.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"建立")]'))).click()
            except: 
                pass
            
            # 生成初始帳號
            uname = f"{self.user['first'].lower()}{self.user['last'].lower()}{random.randint(100, 9999)}"
            user_input = self.wait.until(EC.presence_of_element_located((By.NAME, 'Username')))
            self.type_like_human(user_input, uname)
            
            # 點擊下一步，並等待 1.5 秒讓 Google 驗證是否重複
            self.driver.find_element(By.XPATH, '//span[text()="下一步"] | //span[text()="Next"]').click()
            time.sleep(1.5)

            try:
                error_msg = self.driver.find_element(By.XPATH, '//div[@aria-live="assertive" and text()!=""]')
                if error_msg.is_displayed():
                    print(f"[!] 發現使用者名稱重複: {uname}，啟動自我修復機制...")
                    try:
                        suggestion_btn = self.driver.find_element(By.XPATH, '//button[contains(@class, "VfPpkd-LgbsSe") and not(contains(@class, "VfPpkd-LgbsSe-OWXEXe-k8QpJ"))]')
                        new_uname = suggestion_btn.text
                        suggestion_btn.click()
                        print(f"[*] 成功套用 Google 建議名稱: {new_uname}")
                        uname = new_uname
                    except:
                        user_input.clear() 
                        uname = f"{uname}{random.randint(10000, 99999)}"
                        self.type_like_human(user_input, uname)

                    time.sleep(1)
                    self.driver.find_element(By.XPATH, '//span[text()="下一步"] | //span[text()="Next"]').click()
                    time.sleep(2)
            except:
                pass

            print(f"[*] 最終確認使用者名稱為: {uname}")

            # 4. 密碼頁
            self.type_like_human(self.wait.until(EC.presence_of_element_located((By.NAME, 'Passwd'))), self.user['pwd'])
            self.type_like_human(self.driver.find_element(By.NAME, 'PasswdAgain'), self.user['pwd'])
            self.driver.find_element(By.XPATH, '//span[text()="下一步"] | //span[text()="Next"]').click()

            # 5. 手機驗證
            time.sleep(5)
            if "verify" in self.driver.current_url or "phone" in self.driver.page_source:
                self.handle_sms_logic()

            print(f"== 註冊成功提交: {uname}@gmail.com ==")
            time.sleep(10)

            # =================================================================
            #  6. 執行五星好評任務 ---
            # 替換成你要評價的目標店家 Google Maps 網址
            # target_place_url = "https://www.google.com/maps/place/你的目標店家URL" 
            # # 你可以選擇留空，或者放入預設評論，甚至隨機挑選評論
            # review_comments = ["服務很棒！", "環境舒適，推薦！", "老闆很親切。", "CP值很高！"]
            
            # self.leave_five_star_review(target_place_url, random.choice(review_comments))

        except Exception as e:
            print(f"\n[!] 🚨 程式中斷，發生錯誤：\n{e}")
            # 將當下崩潰的畫面截圖存下來，方便除錯
            self.driver.save_screenshot("error_screenshot.png")
            print("[*] 崩潰畫面已儲存為 error_screenshot.png，請查看。")
            time.sleep(10) # 停頓 10 秒讓你看清楚停在哪裡

        finally:
            print("[*] 清理資源，關閉瀏覽器...")
            self.driver.quit()
        try:
            print(f"\n>>> 執行開始: {self.user['first']}")
            self.driver.get('https://accounts.google.com/signup')

            # 1. 姓名頁
            first_input = self.wait.until(EC.element_to_be_clickable((By.NAME, 'firstName')))
            first_input.click()
            self.type_like_human(first_input, self.user['first'])
            self.type_like_human(self.driver.find_element(By.NAME, 'lastName'), self.user['last'])
            self.driver.find_element(By.XPATH, '//span[text()="下一步"] | //span[text()="Next"]').click()

            # 2. 基本資料頁 
            year_el = self.wait.until(EC.element_to_be_clickable((By.ID, 'year')))
            year_el.click()
            self.type_like_human(year_el, str(random.randint(1996, 2004)))
            
            # 月份 
            self.solve_dropdown_actionchains('month', random.randint(1, 12))
            
            day_el = self.driver.find_element(By.ID, 'day')
            day_el.click()
            self.type_like_human(day_el, str(random.randint(1, 28)))
            
            # 性別
            self.solve_dropdown_actionchains('gender', random.randint(1, 2))
            
            self.driver.find_element(By.XPATH, '//span[text()="下一步"]').click()

            # 3. 使用者名稱頁
            time.sleep(3)
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"建立")]'))).click()
            except: pass
            
            uname = f"{self.user['first'].lower()}{self.user['last'].lower()}{random.randint(100, 999)}"
            self.type_like_human(self.wait.until(EC.presence_of_element_located((By.NAME, 'Username'))), uname)
            self.driver.find_element(By.XPATH, '//span[text()="下一步"]').click()

            # 4. 密碼頁
            self.type_like_human(self.wait.until(EC.presence_of_element_located((By.NAME, 'Passwd'))), self.user['pwd'])
            self.type_like_human(self.driver.find_element(By.NAME, 'PasswdAgain'), self.user['pwd'])
            self.driver.find_element(By.XPATH, '//span[text()="下一步"]').click()

            # 5. 手機驗證
            time.sleep(5)
            if "verify" in self.driver.current_url or "phone" in self.driver.page_source:
                self.handle_sms_logic()

            print(f"== 註冊成功提交: {uname}@gmail.com ==")
            time.sleep(10)

        finally:
            self.driver.quit()

if __name__ == '__main__':
    for user in USER_DATA_LIST:
        bot = GoogleRegistrar(user)
        bot.run()
        time.sleep(random.randint(15, 25))
