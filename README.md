<!--
 * @Descripttion: your project
 * @version: 1.0
 * @Author: JiangFeng
 * @Date: 2023-06-05 14:00:07
 * @LastEditors: JiangFeng
 * @LastEditTime: 2023-06-07 09:46:52
-->

## 0. Target
The **Final** target is to achieve deep learning code training monitoring, which can notify individuals of important information in the form of emails.

## 1. Description
This is a small tool for those who use **SERVERS** to develop and run programs.

## 2. Installation

- You can install this package by pip:
```bash
pip install emailmessage
```

- You can also install from source:
```bash
conda activate [your envs]
python3 setup.py install
```
## 2. Usage

- Change the settings of your QQ email and enable the SMTP service. You can follow the [toturial](www.cnblogs.com/kimsbo/p/10671851.html).

- Record your authorization code and DO NOT show it to others.

- Here is an example:
```python
from emailmessage.mail import Mail

mail = Mail(send_by=[your email], send_to=[target eamil],
            password=[your authorization code])
subject = 'Test emailmessafe'
message = 'Hello, you can use our emailmessage now.'
mail.send_email(subject, message)
```

- Check whether you reveive an email.

## 3. TODO List

- [ ] Add more functions.
- [ ] Support add attachment.
- [ ] Add CHANGELOG.
- [ ] release.