# PyPerformance

## 1. Prepare Test Results
```bash
cd docker
docker-compose.yaml up -d
```
Note: This step can take longer than 1 hour.


## 2. Compare Results
If all containers are stopped and the `docker/results/output` has contained only `analysis.py`, please run below command.:
```bash
docker start docker-compare
```

## 3. Show Result
open `Compare.png`, `speed_up.csv`, and `details.jpg` from `docker/results/output` directory to show compare results.