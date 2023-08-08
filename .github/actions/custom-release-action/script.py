import os
import re
from github import Github

def determine_next_version(current_version):
    major, minor, patch = map(int, current_version.split('.'))
    # Logic to determine next version based on SemVer rules
    next_version = f'{major}.{minor}.{patch + 1}'
    return next_version

def main():
    current_version = '1.0.0'  # Retrieve the current version from your project
    next_version = determine_next_version(current_version)

    # Tag the repository with the new version
    os.system(f'git tag -a {next_version} -m "Version {next_version}"')
    os.system('git push --tags')

    # Create a GitHub release
    g = Github(os.environ['GITHUB_TOKEN'])
    repo = g.get_repo('yourusername/yourrepository')
    repo.create_git_release(
        tag=next_version,
        name=f'Release {next_version}',
        message=f'Changelog and release notes for {next_version}'
    )

if __name__ == '__main__':
    main()

