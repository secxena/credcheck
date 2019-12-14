<p align="center">
<img src="https://raw.githubusercontent.com/secxena/credcheck/master/credcheck.png">
</p>
<p align="center">
  <a href="http://makeapullrequest.com">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome">
  </a>
    <a href="https://github.com">
    <img src="https://img.shields.io/github/contributors/secxena/credcheck.svg" alt="Contributors">
  </a>
    <a href="https://creativecommons.org/publicdomain/zero/1.0/">
    <img src="https://img.shields.io/badge/license-CC0-green.svg?style=flat-square" alt="CC0">
  </a>
</p>
# Features

- [x] Check credentils of given target. 
- [x] Check credentials passivly(using regex).
- [x] CMD-line script.
- [x] Use as library


# Todos
- [ ] Publish on pypi
- [ ] Inclusion of api docs
- [ ] Pin-pointed regexes for Creds
- [ ] Test cases
- [ ] Multiple subparsers
- [ ] CredCheck class for the library
- [ ] Complete regex

# Uses
## Command line usage
```
python main.py --service strip --token sk_live_r3s7_0f_7h3_d37ails
```
## Library Usage
```python
from credcheck.core.cred_check_active import dynamicTest
from credcheck.core.cred_check_utils import CredUtils
service = 'strip'
credentials = {'TOKEN':'sk_live_r3s7_0f_7h3_d37ails'}
stripCred = dynamicTest()
stripCred.checkIt(service,credentails)
```
## Contributing
- Areas to contribute
- Write test cases to make this framework more robust
- Write regex for static testing of Credentials
- Include complete API blocks from https://any-api.com/ to extend the scope of credcheck

### Prerequisites

Install all dependency via

```
pip install -r requirements.txt
```

## Authors

* **Apoorv Raj Saxena** 

## License

This project is licensed under the MIT License


