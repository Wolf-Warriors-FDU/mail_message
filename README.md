<!--
 * @Descripttion: your project
 * @version: 1.0
 * @Author: JiangFeng
 * @Date: 2023-06-05 14:00:07
 * @LastEditors: JiangFeng
 * @LastEditTime: 2023-06-06 20:32:03
-->

## 0. Description
This is a small tool for those who use **SERVERS** to develop and run programs.

## 1. Usage

- Change the settings of your QQ email and enable the SMTP service. You can follow the [toturial](www.cnblogs.com/kimsbo/p/10671851.html).

- Record your authorization code and DO NOT show it to others.

- modified your own information [here](https://github.com/fengjiang5/mail_message/blob/af6ebd1b40f0b3241e098e364ff5e23e9a15fbe0/mail.py#LL16C1-L18C29) in main.py.

- Run in the Terminal by :

```bash
python3 mail.py --send_by [send_by] --send_to [send_to]  --password [password] --subject [subject] --message [message]
```
- or modify the message in mail.sh and run :
```bash
bash ./email.sh
```

## 2. TODO List

- [ ] Add more functions.
- [ ] Support add attachment.