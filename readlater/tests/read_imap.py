#!/usr/bin/env python3
"""
https://www.thepythoncode.com/code/reading-emails-in-python
"""

from imaplib import IMAP4_SSL
import os
import re
import email.parser
from email.header import decode_header

username = os.getenv('AOL_IMAP_USER')
password = os.getenv('AOL_IMAP_PSWD')
password = "anod sfkp suyl vara"


M = IMAP4_SSL('export.imap.aol.com', 993)
M.login(username, password)
status, messages = M.select('INBOX')
print(status, messages)
messages = int(messages[0])
for i in range(messages):
    print(f"#{i}")
    res, msg = M.fetch(str(i+1), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            print(msg)
            sender, encoding = decode_header(msg.get("From"))[0]
            if isinstance(sender, bytes):
                sender = sender.decode(encoding)
            print("From:", sender)
            if msg.is_multipart():
                print('is multipart')
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email body
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        print(body)
                        urls = re.findall(r'(https?://[^\s]+)', body)
                        print(f"URL= {urls[0]}")


M.close()
M.logout()




"""
msg_body = b'''Received: from 10.253.37.223\r\n by atlas201.aol.mail.gq1.yahoo.com with HTTPS; Sat, 18 Dec 2021 19:29:55 +0000\r\nReturn-Path: <pawlakdp@gmail.com>\r\nX-Originating-Ip: [209.85.219.48]\r\nReceived-SPF: pass (domain of gmail.com designates 209.85.219.48 as permitted sender)\r\nAuthentication-Results: atlas201.aol.mail.gq1.yahoo.com;\r\n dkim=pass header.i=@gmail.com header.s=20210112;\r\n spf=pass smtp.mailfrom=gmail.com;\r\n dmarc=pass(p=NONE,sp=QUARANTINE) header.from=gmail.com;\r\nX-Apparently-To: read.later@aol.com; Sat, 18 Dec 2021 19:29:56 +0000\r\nX-YMailISG: VCQnWZUWLDuaSPD1qW904kKJgTa6LxheU1yTCLr3PqDmpsWI\r\n Q_a.y661In93MeGu9brd2nzELKPPZfqAZ8sAMg1MMjnos0dv8PnX8yzaYukg\r\n 2jNwlWhxQkyJU1iMN1Q0wsiZcDOlpL28W1qYpLqVBN_e.8V9rw8jYyxKBVCg\r\n cLHN4yOXZsUTt4EmENR20F9mjtvLU1_RiHTpz9Dh3_mGouRkusRb9KNLBTr5\r\n dYcxcK2a2Nk_ETz_0Uh8wjT3.H1lv3cwJ7TR7YYsC0QL06XA_QPpsYdCBng5\r\n Z63aLqDtlcZbKAlMOQxkTdGyRwUqe1h8CJZ3g3XZ7CPfS.qPYZul0OE1LKVa\r\n 9nqCF1qP6zffhqxaE7b.KbBECo6iDv4QmYo47PP2cGMZC8Z59Q6oA3Kl6zra\r\n HUqtl2xtTz9G3OjApnk_fQQ5T2rl3qvPmCaG6zrF7BTYfRSB0FSWrP.c0D8f\r\n L.GsqLqa93.6bV8ENdTWeP7CzcgKMTAjCHnDbIL7mEPfzCnwG6tiZPKG4AU8\r\n 6kwW6fteDt1td5NWp07L9CtSknge8uPHuT7BjejfmTMYwxJ8iOwptMbvBHQJ\r\n KipwO4zpck1fGqBnguMhPRLt1Chnik55ugIIjJC4XYi_RMeK68B88SWBKdwJ\r\n GIg_ULK71sxTui_l1Me1v0OOYqW4YQGcOTeOp3g9FIfSeh22OPiU4mrW8zkh\r\n XZiK5l_ryNRYhi2lXcQvNk0H9eu99EAj6JvSyN09D0PRyHJygn5.nC3hjTi6\r\n vVkWpfKeURYWeiCcHoj.zVJS1ZTt2dAjUwN9qkwQeXJIqgM7pKCm5jrj6VIp\r\n crEIUSLmPGD3bQ_biT4PQcnI1vbz2ltXbgJOwWWzNsrLPQM0PljsyTfITtY4\r\n KwT_UbiLrHMxCuxvQSOUd9.sMZeP0ZsGC0ByhChuWxrS7dn5O0ckB36eJmiy\r\n 3LzoCd2DD4aAYrqX1j5_zfeZcq5wucasG8UCq.Flrinegzbb03vhIMgCZnsF\r\n bhHhMpVDhxAHy6TWQb83L_nLc6gW1i8FjkT8t9PFgqJvdYqFimQ7StGLrK1Z\r\n 1uozu5QcwSP.5chodGdu6OPOBA--\r\nReceived: from 209.85.219.48 (EHLO mail-qv1-f48.google.com)\r\n by 10.253.37.223 with SMTPs\r\n (version=TLS1_3 cipher=TLS_AES_128_GCM_SHA256);\r\n Sat, 18 Dec 2021 19:29:55 +0000\r\nReceived: by mail-qv1-f48.google.com with SMTP id kc16so5617376qvb.3\r\n        for <read.later@aol.com>; Sat, 18 Dec 2021 11:29:55 -0800 (PST)\r\nDKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;\r\n        d=gmail.com; s=20210112;\r\n        h=mime-version:from:date:message-id:subject:to;\r\n        bh=jPbsMwzRnqWwl0NVqcxPE2AmvL4Vag4ulPdVf61T/lI=;\r\n        b=oDmN03G/U2W6Nbcgl7QZobuJmp2gMsUq6xgXRIPq4ZeM7MzrolD4EnbZu54KTH3cmD\r\n         K23xGdbsImhNz+hSFDOiw58oQC1uyBSzH2+Ll8J66t94qjt8psee5hpW0EMWBMg+NyQt\r\n         V807gGXVuF15QKME0ID9kDgIcVVo8BLnZtU0VPGaeYjhL2qLI48VI4LNUHKItmdxt1Ir\r\n         dZ+cU8aR9zcqFNAbwc2m5ifj3fJu7eITLAXPMdweki7gU9UU7z6jRWk9MqRXfWErRIiR\r\n         P1SwmBiTfepQcbQzn8lqPaP5ji6Vb2wqo04p4xRmTcRC8GEUUz+Awl+uLrF9DuS4HY6n\r\n
4UaA==\r\nX-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;\r\n        d=1e100.net; s=20210112;\r\n        h=x-gm-message-state:mime-version:from:date:message-id:subject:to;\r\n        bh=jPbsMwzRnqWwl0NVqcxPE2AmvL4Vag4ulPdVf61T/lI=;\r\n        b=qZQpaZFOQPUUai++i/RMytU63TUxZRTyYbEfFvyW6M0Msy8UwrOecOY0Kc6IKGb7X5\r\n         qgwYdImKE/1peXjZhCGyDUcrNfJ0J8BFXMksf2Y3q/trvTSwlRFvVmfijRDmxtCFM8Z0\r\n         1X7mWJTHyrdb2gh/rdmKzqQlwrOBsMezectWABJEIrNZnVLbvog/FnX7mtj6oCvzVX6r\r\n         EIo8B9jCgMFNL3pvSN2K2RjoI44xuCRhtXl6+4Ie0uiT8ozWUMDTfrSV/OCNIr15/Rs+\r\n         1+5sWJ/yqPbaDhth680TnO+TApHdvJsKbbJ3c/x9aCMa/HMea0ET6FUwp/yZvSBJt0aL\r\n         +Nzg==\r\nX-Gm-Message-State: AOAM532lmK6WkYIKo3yH2Q8Nps/WENXn6a1xGwkNWLIFM9OSDiQGWFXq\r\n\tHk+EM/+kjpSegXrHPvcysPaxoMwbNUwwPA4mbH3P2oDaEKs=\r\nX-Google-Smtp-Source: ABdhPJxnXKZOY6GEb9IVHfipeWBlhJgK/FjtIqJMSoSNx/IlyCuFn8Kt+281RYQdSPAv9R55367lLAZsP9BZy7cfyEA=\r\nX-Received: by 2002:ad4:4ee2:: with SMTP id dv2mr1762600qvb.20.1639855795198;\r\n Sat, 18 Dec 2021 11:29:55 -0800 (PST)\r\nMIME-Version: 1.0\r\nFrom: Dariusz PAWLAK <pawlakdp@gmail.com>\r\nDate: Sat, 18 Dec 2021 20:29:43 +0100\r\nMessage-ID: <CANHx0q0TQftnN1WdHZNP0C8i-7Gt5PU8=dYUE1k1eGGQbz4GrQ@mail.gmail.com>\r\nSubject: Log4Shell Scanner - PortSwigger\r\nTo: read.later@aol.com\r\nContent-Type: multipart/alternative; boundary="00000000000027dfe105d370aea2"\r\nContent-Length: 477\r\n\r\n--00000000000027dfe105d370aea2\r\nContent-Type: text/plain; charset="UTF-8"\r\n\r\nhttps://portswigger.net/bappstore/b011be53649346dd87276bca41ce8e8f\r\n\r\n--00000000000027dfe105d370aea2\r\nContent-Type: text/html; charset="UTF-8"\r\nContent-Transfer-Encoding: quoted-printable\r\n\r\n<div dir=3D"auto"><a href=3D"https://portswigger.net/bappstore/b011be536493=\r\n46dd87276bca41ce8e8f">https://portswigger.net/bappstore/b011be53649346dd872=\r\n76bca41ce8e8f</a>=C2=A0</div>\r\n\r\n--00000000000027dfe105d370aea2--\r\n'''



msg = email.message_from_string(msg_body.decode())
print(msg)
print(msg.is_multipart())
print(msg.get_payload(decode=True))

for part in msg.get_payload():
     print("###", part)
"""