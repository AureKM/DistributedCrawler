class URLDistribution:
    @staticmethod
    def round_robin(urls, num_workers):
        """轮询分发策略"""
        for i, url in enumerate(urls):
            worker_id = i % num_workers
            print(f"Assigning {url} to Worker {worker_id}")

    @staticmethod
    def hash_distribution(urls, num_workers):
        """哈希分发策略"""
        for url in urls:
            worker_id = hash(url) % num_workers
            print(f"Assigning {url} to Worker {worker_id}")