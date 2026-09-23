import requests


class JobFinder:
    API_URL = "https://www.arbeitnow.com/api/job-board-api"

    def __init__(self, tag, remote_status, number_of_pages):
        self.__tag = tag.strip().lower()
        self.__remote_status = remote_status
        self.__number_of_pages = number_of_pages

    def get_jobs_from_page(self, page):
        jobs = []
        params = {"page": page}
        response = requests.get(self.API_URL, params=params)
        if response.ok:
            api_data = response.json()
            jobs = api_data.get("data", [])
        return jobs

    def job_filter(self, job):
        tags = job.get("tags", [])
        remote = job.get("remote", False)
        has_matching_tag = any(tag.strip().lower() == self.__tag for tag in tags)
        has_matching_remote = remote == self.__remote_status
        return has_matching_tag and has_matching_remote

    def count_matches(self):
        count = 0
        for page in range(1, self.__number_of_pages + 1):
            jobs = self.get_jobs_from_page(page)
            for job in jobs:
                if self.job_filter(job):
                    count += 1
        return count
