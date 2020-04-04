class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            if '+' in local_name:
                local_name = local_name[:local_name.index('+')]
            ans.add(local_name.replace('.', '') + '@' + domain_name)
        return len(ans)