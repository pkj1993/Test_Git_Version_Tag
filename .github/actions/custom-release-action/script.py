# /.github/actions/create-symmetric-tag/script.py
import os
import re
from github import Github

def increment_version(version, version_bump):
    major, minor, patch = map(int, version.split('.'))
    
    if version_bump == 'Major':
        new_version = f'{major + 1}.0.0'
    elif version_bump == 'Minor':
        new_version = f'{major}.{minor + 1}.0'
    else:
        new_version = f'{major}.{minor}.{patch + 1}'
    
    return new_version

def create_symmetric_tag(repo, tag_name, commit_sha, tag_message):
    # Create a local tag
    os.system(f'git tag -a {tag_name} {commit_sha} -m "{tag_message}"')

    # Push the local tag to remote
    os.system(f'git push origin {tag_name}')

    # Create a GitHub release
    repo.create_git_release(
        tag=tag_name,
        name=f'Release {tag_name}',
        message=f'Release notes for {tag_name}'
    )

def main():
    github_token = os.environ.get('GITHUB_TOKEN')
    g = Github(github_token)
    repo = g.get_repo('pkj1993/Test_Git_Version_Tag')  # Replace with your repo details

    commit_sha = os.environ.get('GITHUB_SHA')
    version_bump = os.environ.get('INPUT_VERSION_BUMP', 'Bugfix')  # Default to 'Bugfix'
    current_version = '1.0.0'  # Get the current version from your project

    next_version = increment_version(current_version, version_bump)

    create_symmetric_tag(repo, next_version, commit_sha, f"Version {next_version}")

if __name__ == '__main__':
    main()
