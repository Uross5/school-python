from JobFinder import JobFinder


def main():
    job_finder = JobFinder("engineering", False, 3)
    total_matches = job_finder.count_matches()
    print(total_matches)


if __name__ == "__main__":
    main()
