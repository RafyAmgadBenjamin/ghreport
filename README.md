### Ghreport

#### Introduction 
This is a tool that helps you to track the issues on github and filter them with some basic criteria

#### prerequests 
- you need to generate an access key/token for the account you are going to use 

for more information check this [link](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

####  Download 
```bash
git clone https://github.com/RafyAmgadBenjamin/ghreport.git
```

#### Install requirements 
```bash
pip install -r requirements.txt
```

#### Arguments 
- `-h --help` for help about the arguments and quick description about the tool
- `--account` Github account name you are going to use,  it is `required`
- `--key` Github account access token/key, it is `required`
- `--dest` Exported report destination, it is `required`
- `--ndays` Number of days to include in filtering the issues, it is `required`

#### Examples
- Get help 
```bash
python3 main.py -h
```

```bash
usage: main.py [-h] --account ACCOUNT_NAME --key ACCESS_TOKEN --dest DEST --ndays NO_DAYS

Process Github account and get open issues.

optional arguments:
  -h, --help            show this help message and exit
  --account ACCOUNT_NAME
                        Github account name
  --key ACCESS_TOKEN    Github account access token/key
  --dest DEST           Exported report destination
  --ndays NO_DAYS       Number of days to include in filtering the issues
```

- Filter issues
```bash
python3 main.py --key account_key/token --dest ./report.md --account account_name --ndays 5
```