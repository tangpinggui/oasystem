#coding=utf-8
from SDK.CCPRestSDK import REST
import ConfigParser

accountSid = '8aaf0708624670f201626c0dcd610fc7'
# 说明：主账号，登陆云通讯网站后，可在控制台首页中看到开发者主账号ACCOUNT SID。

accountToken = 'a6f7b822fab647adb804bac41b02f576'
# 说明：主账号Token，登陆云通讯网站后，可在控制台首页中看到开发者主账号AUTH TOKEN。

appId = '8aaf0708624670f201626c0dcdc60fce'
# 请使用管理控制台中已创建应用的APPID。

serverIP = 'app.cloopen.com'
# 说明：请求地址，生产环境配置成app.cloopen.com。

serverPort = '8883'
# 说明：请求端口 ，生产环境为8883.

softVersion = '2013-12-26'  # 说明：REST API版本号保持不变。


def sendTemplateSMS(to, datas, tempId):
    '''
    to: 短信接收手机号码集合,用英文逗号分开,如 '13810001000,13810011001',最多一次发送200个。
    datas：内容数据，需定义成数组方式，如模板中有两个参数，定义方式为array['Marry','Alon']。
    templateId: 模板Id,如使用测试模板，模板id为"1"，如使用自己创建的模板，则使用自己创建的短信模板id即可。
    '''
    # 初始化REST SDK
    rest = REST(serverIP, serverPort, softVersion)
    rest.setAccount(accountSid, accountToken)
    rest.setAppId(appId)

    result = rest.sendTemplateSMS(to, datas, tempId)
    for k, v in result.iteritems():
        if k == 'templateSMS':
            for k, s in v.iteritems():
                print '%s:%s' % (k, s)
        else:
            print '%s:%s' % (k, v)

