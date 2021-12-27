import requests
import json
import argparse


def get_open_issues(account_name: str, access_token: str) -> list:
    """ Get open issues related to specific account using access token

    Args:
        - account_name(string): github account name
        - access_token(string): github account access token generated from github for more information 
        check https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
    
    Returns:
        - issues(list): list issues filtered with the data we need 
    """
    headers = {"Accept": "application/vnd.github.v3+json"}
    github_url = "https://api.github.com/issues?state=open"
    response = requests.get(github_url, headers=headers, auth=(
        account_name, access_token))
    issues_data = response.json()
    issues = [{"title": issue.get("title"), "url": issue.get(
        "html_url")} for issue in issues_data]
    return issues


def format_text(issues: list) -> str:
    """ Get markdown formatted text from list of issues

    Args:
        - issues: list of issues with the required data 

    Returns
        - text(string): this is the text which will be used to render the makrdown report
    """
    text = ""
    for issue in issues:
        text += f"### {issue.get('title')} \n"
        text += f"[link]({issue.get('url')}) \n"
    return text


def export_markdown(md_text: str, dist: str):
    """ Export the markwon text into a markdown file

    Args:
        - md_text(string): text fomatted in markdown format
        - dist(string): distination at which the markdown report will be saved
    """
    try:
        with open(dist, "w") as file:
            file.write(md_text)
    except Exception as e:
        print(
            f"Error happened while writing the report file for details: {str(e)}")

if __name__ == "__main__":
    # Getting arguments from user
    parser = argparse.ArgumentParser(
        description='Process Github account and get open issues.')
    parser.add_argument('--account', dest="account_name",
                        required=True,
                        help='Github account name')
    parser.add_argument('--key', dest="access_token",
                        required=True,
                        help='Github account access token/key')
    parser.add_argument('--dist', dest="dist",
                        required=True,
                        help='exported report distination')
    args = parser.parse_args()

    issues = get_open_issues(account_name=args.account_name,
                    access_token=args.access_token)
    md_text = format_text(issues)
    export_markdown(md_text, dist= args.dist)
