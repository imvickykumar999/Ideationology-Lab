# https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NCqPzrmYABGDvDXRZ2otRGTMvD3g1gchNo0HTKiGEIr3HlCp-RFNAtMwvDEpYACPiCBp2ggt9X5ztsf1LUR5dVhW6nag

import getpass
passw = getpass.getpass('Enter password : ')

def covail(passw=passw,
           l=[
               {'1key1':'1value1', '1key2':'1value2'},
               {'2key1':'2value1', '2key2':'2value2'}
             ],

          toaddr = "imvickykumar999@gmail.com",
          filename = None,
          ):

    if filename == None:
        filename = f"{toaddr.split('@')[0]}.xlsx"

    import pandas as pd
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')

    for i, j in enumerate(l):
        pd.DataFrame(l[i],
         index=[0]
         ).to_excel(writer, sheet_name = f'Sheet {i}')
    writer.save()

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "sagar.sws2000@gmail.com"
    toaddr = "hellovickykumar123@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr

    msg['Subject'] = "COVID19 Slot Notification"
    body = f'''

    Book your Slot here : https://selfregistration.cowin.gov.in/

    This E-Mail is Sent using python code by vicks,
    Slots are... (open attached excel file) below.
    '''
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filename, "rb")

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, passw)

    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()
    return len(l)

print(covail(passw))
