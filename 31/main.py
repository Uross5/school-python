import requests

number_of_tech_jobs = 0
for page in range(1, 4):
    print(f"Viewing page {page}\n")

    params = {"page": page}
    response = requests.get("https://www.arbeitnow.com/api/job-board-api", params=params)

    api_data = response.json()
    jobs = api_data.get("data", [])

    if response.ok:
        print(f"Total jobs returned: {len(jobs)}")

        for job in jobs:
            tags = job.get('tags', [])
            is_remote = job.get('remote', False)
            has_engineering_tags = any(tag.lower() == "engineering" for tag in tags)

            if has_engineering_tags and not is_remote:
                number_of_tech_jobs += 1



    else:
        print(f"Request failed with status code: {response.status_code}")

print(f"Total number of jobs: {number_of_tech_jobs}")
