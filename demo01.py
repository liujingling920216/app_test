import time
from appium import webdriver

des = {
    'platformName': 'Android',
    'platformVersion': '8.0',  #填写android虚拟机的系统版本
    'deviceName': 'Samsung Galaxy S8',   #填写安卓虚拟机的设备名称
    'appPackage': 'com.android.calculator2',   #填写被测试包名
    'appActivity': '.Calculator',    #填写被测试app入口
    'udid': '192.168.56.103:5555',  # 填写通过命令行 adb devices 查看到的 uuid（指定已连接在MAC上的虚拟机）
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True,
}
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', des)
# driver.find_element_by_id('com.android.calculator2:id/digit_1').click()      #(取resource-id、id、name)
# driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
# time.sleep(2)
# driver.find_element_by_accessibility_id('plus').click()     #(取content-desc)
# driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
# time.sleep(2)
# driver.find_element_by_accessibility_id('equals').click()

# driver.find_element_by_xpath('//android.widget.Button[@text=9]').click()
# driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.calculator2:id/op_add"]').click()
# driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.calculator2:id/digit_3"]').click()
# driver.find_element_by_xpath('//android.widget.Button[@content-desc="equals" and @index="5"]').click()

# driver.find_element_by_xpath('//android.widget.Button[@text=9]').click()
# driver.find_element_by_xpath('//android.widget.Button[contains(@resource-id,":id/del")]').click()
# driver.find_element_by_xpath('//android.widget.Button[ends-with(@resource-id,"/digit_4")]').click()


#
# driver.find_element_by_android_uiautomator('text("9")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("8")').click()
#
# driver.find_element_by_android_uiautomator('resourceId("com.android.calculator2:id/digit_6")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.calculator2:id/digit_6")').click()
#
# driver.find_element_by_android_uiautomator('className("android.widget.Button")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button").text("9")').click()
#
# driver.find_element_by_android_uiautomator('description("delete")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().description("delete")').click()

# 后代元素定位
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.calculator2:iad/pad_numeric").childSelector(className("android.widget.Button").instance(1))').click()

# 兄弟元素定位
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.calculator2:id/digit_9")').click()
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.calculator2:id/digit_9").fromParent(text("3"))').click()

