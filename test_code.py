from appium import webdriver
from appium.options.android import UiAutomator2Options
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
import pytest


class TestCS:

    def setup(self):
        appium_server_url = "http://localhost:4723"

        capabilities = {"platformName": "android",
                        "appActivity": "com.atg.world.activity.SplashActivity",
                        "appWaitDuration": "5000",
                        "appExecTimeout": "50000",
                        "uiautomator2ServerLaunchTimeout": "50000",
                        "uiautomator2ServerInstallTimeout": "50000",
                        "appPackage": "com.ATG.World",
                        "deviceName": "emulator-5554",
                        "driver": "http://localhost:4723/wd/hub"}

        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities),
                                       strict_ssl=False)
        sleep(5)

    def teardown(self):
        self.driver.quit()

    def test_case(self):
        self.driver.find_element(by=AppiumBy.ID,
                                 value='com.android.permissioncontroller:id/permission_allow_button').click()
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/getStartedTv').click()
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/login_email').click()
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/email_phone_login").send_keys(
            "wiz_saurabh@rediffmail.com")
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/signinbutton").click()
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/password").send_keys("Pass@123")
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/passwordloginbutton").click()
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/btnGotit").click()
        sleep(5)

        # end of login segment

        # testing if image uploads without error

        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/fab').click()
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/image_fab_clicked').click()
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value='android:id/button1').click()
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID,
                                 value='com.android.permissioncontroller:id/permission_allow_button').click()
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/camera_btn').click()
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/img_clicked_btn').click()
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/toolbar_post_action').click()
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/caption_edit_text').send_keys("test text")
        sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/toolbar_post_action').click()
        sleep(5)
