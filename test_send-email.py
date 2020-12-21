import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.winupon.com"  # 设置服务器
mail_user = "jiangfeng@winupon.com"  # 用户名
mail_pass = "MRJbbk950218."  # 口令

sender = 'jiangfeng@winupon.com'
receivers = ['jiangfeng@winupon.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("JF", 'utf-8')          # 发送者
message['To'] = Header("tester", 'utf-8')        # 接收者
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('Python 带附件邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open(r'D:\BAK_JF\WP\素材\ppt\03.ppt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字(经测试，还是写原名比较好，否则可能出现乱码)
att1["Content-Disposition"] = 'attachment; filename="03.ppt"'
message.attach(att1)

# 构造附件2，传送指定路径下的01.jpg文件
att2 = MIMEText(open(r'D:\BAK_JF\WP\素材\picture\jpg\01.jpg', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="01.jpg"'
message.attach(att2)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")