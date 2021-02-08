# SES SMTP Credentials Generation
To use the SMTP interface of AWS SES, you need to generate credentials based on the secret access
key of an IAM user. AWS does provide an example script in [the documentation][ses-smtp-doc], but
copying code out of the documentation isn't very user friendly. This tool does the same thing, but
its easier to install (if you already have a working python environment).

## Installation
This code can be installed from pypi. E.g. using pip or pipx.
```shell
# with pipx, recommended for a cli tool
pipx install ses-smtp-credentials
# with pip
pip install ses-smtp-credentials
```

# Usage
You need to supply the secret access key and the region.
ses-smtp-credentials will ask you for missing information, so both are optional arguments.

```
# Interactive
ses-smtp-credentials

# Non-interactive
ses-smtp-credentials --secret SECRET_ACCESS_KEY --region REGION 
```

## License
This code was based on sample code from [the AWS documentation][ses-smtp-doc] that was released
under a [modified MIT license][ses-smtp-licence] on [GitHub][ses-smtp-src]. In the documentation
it's called "smtp_credentials_generate.py". The same license has been adapted to this repository. 
See the LICENSE file. 


[ses-smtp-doc]: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-credentials.html
[ses-smtp-licence]: https://github.com/awsdocs/amazon-ses-developer-guide/blob/3c0d65cbb63c8aaebfc4d005ca96d3b0332e0430/LICENSE-SAMPLECODE
[ses-smtp-src]: https://github.com/awsdocs/amazon-ses-developer-guide/blob/3c0d65cbb63c8aaebfc4d005ca96d3b0332e0430/doc-source/smtp-credentials.md
