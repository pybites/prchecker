from github import Github

from dates import get_date_range

gh = Github()


def get_prs(month, username):
    created = get_date_range(month)

    import pdb;pdb.set_trace
    prs = gh.search_issues('',
                            author=username,
                            type='pr',
                            created=created)
    return prs
