# /.github/actions/create-symmetric-tag/script.py
import os
from github import Github

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
    repo = g.get_repo('yourusername/yourrepository')  # Replace with your repo details

    commit_sha = os.environ.get('GITHUB_SHA')
    tag_name = os.environ.get('INPUT_TAG_NAME', 'v1.0.0')  # Default to v1.0.0 if not specified
    tag_message = f"Version {tag_name}"

    create_symmetric_tag(repo, tag_name, commit_sha, tag_message)

if __name__ == '__main__':
    main()
