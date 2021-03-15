etext is a python module that lets you send text messages using email SMS gateways. Both SMS and MMS are supported.

# Instalation
```
pip install etext
```

# Sending SMS messages
```
from etext import send_sms_via_email

phone_number = "123-123-1234"
message = "hello world!"
provider = "T-Mobile"

sender_credentials = ("email@gmail.com", "email_password")

send_sms_via_email(
    phone_number, message, provider, sender_credentials, subject="sent using etext"
)

```
`number: str` - phone number to text

`message: str` - message to send

`provider: str` - phone provider/carrier [click here to see the supported providers](https://github.com/AlfredoSequeida/etext/blob/master/etext/providers.py).

`sender_credentials: tuple` - email and password for SMTP server

`subject: str = "sent using etext"` - subject for the email header

`smtp_server: str = "smtp.gmail.com"` - smtp server to use (gmail is the default)

`smtp_port: int = 465` - smtp port (465) is the default

note the use of the keyword argument 'subject', some SMS gateways need a message to be formatted as an email, this includes the use of a subject in the header. You can try experimenting with the gateway you are using to see if you need to include text in the subject. Otherwise, you can pass in an empty subject like so:

`subject=""`

by default the smtp client used to send emails is gmail's smtp server on port 465. However, if you want to use a different smtp server or port you can do that using the `smtp_server` and `smtp_port` keyword arguments like this:

```
send_sms_via_email(
    phone_number,
    message,
    provider,
    sender_credentials,
    smtp_server="some_smtp_server",
    smtp_port="502",
)
```

# Sending MMS messages
```
from etext import send_mms_via_email

file_path = "/path/to/file/file.png"

mime_maintype = "image"
mime_subtype = "png"

# note that compared to the first example, this number is formatted differently
# etext removes any characters that are not digits in the number, so feel free
# to format numbers however you want
phone_number = "(123) 123-1234"

message = "hello world!"
provider = "T-Mobile"

sender_credentials = ("email@gmail.com", "email_password")

send_mms_via_email(
    phone_number,
    message,
    file_path,
    mime_maintype,
    mime_subtype,
    provider,
    sender_credentials,
)
```

This method has all of the same parameters as the SMS method but adds three more parameters.

`file_path:str` - the file path of the file to send in the message

`mime_maintype:str` - the mime main type

`mime_subtype:str` - the mime sub type

[here is a resource containing common mime types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)

the format corresponds like this: `mime_maintype/mime_subtype`. As an example, to send a pdf file via MMS, which has the following MIME type: `application/pdf`, we could use these main and subtypes:

```
mime_maintype = "application"
mime_subtype = "pdf"
```

# More
If you are using etext with Gmail, you should set up an app password for use with etext. You can do that by clicking [here](https://myaccount.google.com/apppasswords).